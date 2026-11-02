"""TeX for the blueprint importer: arguments, a project's macros, and Markdown.

Blueprints are written for plasTeX and LaTeX. This reads the part of TeX they
use: groups and arguments, the macros a project defines, and the text and
formulas of its statements, which become Markdown with TeX formulas for
MathJax. A project's macros are expanded where they are used, since the vault
has one macro table for every project and AutoformBot turns off definitions
inside formulas.
"""

from __future__ import annotations

import re
import textwrap
import unicodedata
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass, field

from trough.vault import MATH_SPAN, safe_math_markdown

CONTROL = re.compile(r"\\(?:[A-Za-z@]+|.)", re.S)
PARBREAK = re.compile(r"\n[ \t]*\n\s*")
CODE_ENV = re.compile(r"\s*\{\s*([^{}]*?)\s*\}")  # the environment a \begin opens
EXPANSION_DEPTH = 24


def strip_comment(line: str) -> str:
    """The line up to its first unescaped %."""
    i = line.find("%")
    while i >= 0:
        backslashes = len(line[:i]) - len(line[:i].rstrip("\\"))
        if backslashes % 2 == 0:
            return line[:i]
        i = line.find("%", i + 1)
    return line


def group_end(text: str, i: int) -> int:
    """The index just past the {...} group that opens at text[i], or len(text) if it never closes."""
    depth = 0
    j = i
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    return len(text)


def bracket_end(text: str, i: int) -> int:
    """The index just past the [...] that opens at text[i]; braces inside are skipped whole."""
    depth = 0
    j = i
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            j = group_end(text, j)
            continue
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    return len(text)


def skip_space(text: str, i: int) -> int:
    while i < len(text) and text[i] in " \t\n":
        i += 1
    return i


def argument(text: str, i: int) -> tuple[str, int] | None:
    """One argument at text[i:], after spaces: a braced group's contents, or one token."""
    i = skip_space(text, i)
    if i >= len(text):
        return None
    if text[i] == "{":
        end = group_end(text, i)
        return text[i + 1 : end - 1], end
    match = CONTROL.match(text, i)
    if match:
        return match.group(), match.end()
    return text[i], i + 1


def optional(text: str, i: int) -> tuple[str, int] | None:
    """An optional [...] argument at text[i:], after spaces."""
    j = skip_space(text, i)
    if j < len(text) and text[j] == "[":
        end = bracket_end(text, j)
        return text[j + 1 : end - 1], end
    return None


def squeeze(text: str) -> str:
    """*text* on one line, each run of white space one space, as TeX reads a label."""
    return " ".join(text.split())


def names(text: str) -> list[str]:
    """The comma-separated names of a \\lean or \\uses argument."""
    return [squeeze(name) for name in text.split(",") if name.strip()]


def environment_end(text: str, i: int, env: str) -> tuple[int, int]:
    """For an environment whose body starts at text[i]: where the body ends, and where its
    \\end{env} ends. Nested environments of the same name are skipped."""
    pattern = re.compile(r"\\(begin|end)\s*\{" + re.escape(env) + r"\}")
    depth = 1
    for match in pattern.finditer(text, i):
        depth += 1 if match.group(1) == "begin" else -1
        if depth == 0:
            return match.start(), match.end()
    return len(text), len(text)


@dataclass
class Macro:
    nargs: int = 0
    default: str | None = None  # the first argument's default, when that argument is optional
    body: str = ""
    primitive: bool = False  # \let to a command that is no macro: its body is that command, read no further


DEFINER = re.compile(r"\\(?:(?:re)?newcommand|providecommand|DeclareMathOperator|DeclareRobustCommand)\*?|\\[gex]?def(?![A-Za-z])|\\let(?![A-Za-z])")


def definitions(text: str, macros: dict[str, Macro] | None = None) -> dict[str, Macro]:
    """The macros text defines with \\newcommand, \\renewcommand, \\providecommand,
    \\DeclareMathOperator, \\def or \\let, added to *macros*; a later definition wins."""
    macros = dict(macros or {})
    for match in DEFINER.finditer(text):
        command = match.group()
        i = match.end()
        if command.startswith("\\let"):
            target = argument(text, i)
            if not target:
                continue
            j = skip_space(text, target[1])
            j = j + 1 if text[j : j + 1] == "=" else j
            source = argument(text, j)
            if source and target[0].startswith("\\") and source[0].startswith("\\"):
                macros[target[0][1:]] = macros.get(source[0][1:], Macro(body=source[0], primitive=True))
            continue
        if command.endswith("def"):
            name = CONTROL.match(text, skip_space(text, i))
            if not name:
                continue
            params_end = text.find("{", name.end())
            if params_end < 0:
                continue
            params = text[name.end() : params_end]
            body_end = group_end(text, params_end)
            macros[name.group()[1:]] = Macro(params.count("#"), None, text[params_end + 1 : body_end - 1])
            continue
        name_arg = argument(text, i)
        if not name_arg or not name_arg[0].strip().startswith("\\"):
            continue
        name = name_arg[0].strip()[1:]
        if command.startswith("\\DeclareMathOperator"):
            body = argument(text, name_arg[1])
            if body:
                star = "*" if command.endswith("*") else ""
                macros[name] = Macro(body=f"\\operatorname{star}{{{body[0]}}}")
            continue
        j = name_arg[1]
        nargs, default = 0, None
        count = optional(text, j)
        if count and count[0].strip().isdigit():
            nargs, j = int(count[0].strip()), count[1]
            first = optional(text, j)
            if first:
                default, j = first
        body = argument(text, j)
        if body is None or (command.startswith("\\providecommand") and name in macros):
            continue
        macros[name] = Macro(nargs, default, body[0])
    return macros


def substitute(body: str, args: list[str]) -> str:
    out = re.sub(r"#([1-9])", lambda m: args[int(m.group(1)) - 1] if int(m.group(1)) <= len(args) else "", body)
    return out.replace("##", "#")


def expand(text: str, macros: dict[str, Macro], depth: int = 0) -> str:
    """text with the macros expanded. \\gdef or \\def of a \\csname adds to *macros* (a
    project can define macros as it goes); \\csname X\\endcsname uses macro X."""
    if depth > EXPANSION_DEPTH:
        return text
    out: list[str] = []
    i = 0
    while i < len(text):
        c = text[i]
        if c != "\\":
            j = text.find("\\", i)
            j = len(text) if j < 0 else j
            out.append(text[i:j])
            i = j
            continue
        match = CONTROL.match(text, i)
        name = match.group()[1:]
        j = match.end()
        if name == "expandafter":
            i = j
            continue
        code = CODE_ENV.match(text, j) if name == "begin" else None
        if code and code.group(1) in CODE_BLOCKS:  # a listing keeps every character
            stop = re.compile(r"\\end\s*\{" + re.escape(code.group(1)) + r"\}").search(text, code.end())
            out.append(text[i : stop.start() if stop else len(text)])
            i = stop.start() if stop else len(text)
            continue
        if name in ("gdef", "def", "xdef", "edef") and text.startswith("\\csname", skip_space(text, j)):
            start = skip_space(text, j) + len("\\csname")
            end = text.find("\\endcsname", start)
            body = argument(text, end + len("\\endcsname")) if end >= 0 else None
            if body:
                macros[expand(text[start:end], macros, depth + 1).strip()] = Macro(body=body[0])
                i = body[1]
                continue
        if name == "csname":
            end = text.find("\\endcsname", j)
            if end >= 0:
                macro = macros.get(expand(text[j:end], macros, depth + 1).strip())
                out.append(expand(macro.body, macros, depth + 1) if macro else "")
                i = end + len("\\endcsname")
                continue
        macro = macros.get(name)
        if macro is None:
            out.append(match.group())
            i = j
            continue
        if macro.primitive:
            out.append(macro.body)
            i = j
            continue
        args: list[str] = []
        needed = macro.nargs
        if macro.default is not None:
            first = optional(text, j)
            args.append(first[0] if first else macro.default)
            j = first[1] if first else j
            needed -= 1
        for _ in range(needed):
            arg = argument(text, j)
            if arg is None:
                break
            args.append(arg[0])
            j = arg[1]
        body = expand(substitute(macro.body, args), macros, depth + 1)
        # A control word ends at the first non-letter: keep "\op x" from becoming "\diamondx".
        if re.search(r"\\[A-Za-z]+$", body) and j < len(text) and text[j].isalpha():
            body += " "
        out.append(body)
        i = j
    return "".join(out)


ACCENTS = {"'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308", "~": "\u0303", "=": "\u0304", ".": "\u0307",
           "u": "\u0306", "v": "\u030c", "H": "\u030b", "c": "\u0327", "k": "\u0328", "r": "\u030a", "b": "\u0331",
           "d": "\u0323"}
LETTERS = {"ss": "ß", "o": "ø", "O": "Ø", "ae": "æ", "AE": "Æ", "oe": "œ", "OE": "Œ", "aa": "å", "AA": "Å",
           "l": "ł", "L": "Ł", "i": "ı", "j": "ȷ", "S": "§", "P": "¶", "dag": "†", "ddag": "‡", "copyright": "©",
           "ldots": "…", "dots": "…", "textellipsis": "…", "textendash": "–", "textemdash": "—",
           "textquoteright": "’", "textquoteleft": "‘", "textquotedblleft": "“", "textquotedblright": "”",
           "LaTeX": "LaTeX", "TeX": "TeX", "textbackslash": "\\\\", "textasciitilde": "~", "textbar": "|",
           "textless": "$<$", "textgreater": "$>$", "textdegree": "°", "pounds": "£", "euro": "€"}
SYMBOLS = {"%": "%", "&": "&", "#": "\\#", "_": "\\_", "$": "\\$", "{": "{", "}": "}", " ": " ", ",": " ",
           ";": " ", ":": " ", "!": "", "/": "", "-": "", "\\": " ", "\n": " ", "\t": " ", "@": ""}
EMPHASIS = {"emph", "textit", "textsl", "mathit"}
STRONG = {"textbf"}
CODE = {"texttt", "path", "lstinline"}
TRANSPARENT = {"textrm", "textsf", "textup", "textnormal", "textmd", "textsc", "mbox", "hbox", "text", "underline",
               "uline", "textlf", "foreignlanguage", "selectlanguage", "texorpdfstring", "NoCaseChange"}
DROPPED = {"label", "lean", "uses", "proves", "discussion", "alsoIn", "index", "hspace", "vspace", "hskip", "includegraphics",
           "vskip", "phantom", "hphantom", "vphantom", "color", "pagecolor", "setlength", "addtolength",
           "addcontentsline", "nocite", "bibliographystyle", "bibliography", "raisebox", "kern", "rule"}
QUIET = {"leanok", "mathlibok", "notready", "noindent", "indent", "medskip", "bigskip", "smallskip", "newline",
         "linebreak", "pagebreak", "newpage", "clearpage", "centering", "raggedright", "raggedleft", "par",
         "relax", "protect", "nobreak", "allowbreak", "quad", "qquad", "enspace", "thinspace", "normalfont",
         "rm", "sf", "sc", "upshape", "mdseries", "small", "footnotesize", "scriptsize", "tiny", "normalsize",
         "large", "Large", "LARGE", "huge", "Huge", "maketitle", "tableofcontents", "displaystyle", "hfill",
         "vfill", "break", "ignorespaces", "unskip", "xspace", "/", "item"}
SWITCHES = {"bf": "strong", "bfseries": "strong", "it": "em", "itshape": "em", "em": "em", "sl": "em",
            "slshape": "em", "tt": None, "ttfamily": None}
REFS = {"ref", "cref", "Cref", "autoref", "nameref", "eqref", "cpageref", "Cpageref", "pageref", "vref", "Vref",
        "labelcref", "namecref", "nameCref"}
CITES = {"cite", "citep", "citet", "citealp", "citealt", "parencite", "textcite", "autocite", "footcite", "citeauthor"}
DISPLAY_MATH = {"equation": None, "equation*": None, "displaymath": None, "math": None, "align": "aligned",
                "align*": "aligned", "flalign": "aligned", "flalign*": "aligned", "eqnarray": "aligned",
                "eqnarray*": "aligned", "gather": "gathered", "gather*": "gathered", "multline": "gathered",
                "multline*": "gathered", "alignat": "alignedat", "alignat*": "alignedat"}
INNER_MATH = {"split", "aligned", "gathered", "cases", "array", "matrix", "pmatrix", "bmatrix", "Bmatrix", "vmatrix",
              "Vmatrix", "smallmatrix", "CD", "dcases", "alignedat"}
# Math symbols that a blueprint sometimes writes outside a formula, where TeX would stop;
# plasTeX prints them, and so does this, as a formula.
MATH_ONLY = {"infty", "leq", "geq", "le", "ge", "neq", "ne", "times", "cdot", "cdots", "pm", "mp", "to", "mapsto",
             "in", "notin", "subset", "subseteq", "cup", "cap", "setminus", "emptyset", "partial", "nabla", "ell",
             "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta", "eta", "theta", "vartheta", "iota",
             "kappa", "lambda", "mu", "nu", "xi", "pi", "rho", "sigma", "tau", "upsilon", "phi", "varphi", "chi",
             "psi", "omega", "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Phi", "Psi", "Omega"}
LISTS = {"itemize": "ul", "enumerate": "ol", "description": "dl", "compactitem": "ul", "compactenum": "ol"}
QUOTES = {"quote", "quotation", "displayquote"}
OMITTED = {"tikzcd": "a commutative diagram", "tikzpicture": "a picture", "algorithm": "an algorithm",
           "picture": "a picture", "xy": "a diagram"}
CODE_BLOCKS = {"verbatim", "verbatim*", "Verbatim", "lstlisting", "minted"}
TABULARS = {"tabular", "tabular*", "tabularx", "array*"}
FLOATS = {"figure": "Figure", "figure*": "Figure", "table": "Table", "table*": "Table", "wrapfigure": "Figure"}
RULES = re.compile(r"\\(?:hline|toprule|midrule|bottomrule|cline\s*\{[^}]*\}|cmidrule\s*(?:\([^)]*\))?\s*\{[^}]*\})")


@dataclass
class Para:
    text: str


@dataclass
class Display:
    tex: str


@dataclass
class ListBlock:
    kind: str
    items: list[tuple[str, list]] = field(default_factory=list)


@dataclass
class Quote:
    blocks: list


@dataclass
class Omitted:
    what: str


@dataclass
class Code:
    text: str
    language: str = ""


@dataclass
class Table:
    rows: list[list[str]]  # Markdown cells; the first row is the header


def tagged(tex: str, tag: Callable[[str], str | None]) -> str:
    """A display's TeX with each \\label that *tag* numbers shown as that number at the end of
    its row, since AutoformBot turns \\tag off."""
    if "\\label" not in tex:
        return tex
    rows: list[str] = []
    depth = 0
    start = 0
    for match in re.finditer(r"\\(?:begin|end)\s*\{[^}]*\}|\\\\|\\.|[{}]", tex):
        token = match.group()
        if token == "{" or token.startswith("\\begin"):
            depth += 1
        elif token == "}" or token.startswith("\\end"):
            depth -= 1
        elif token == "\\\\" and depth == 0:
            rows.append(tex[start : match.start()])
            rows.append(token)
            start = match.end()
    rows.append(tex[start:])
    out = []
    for row in rows:
        numbers = [tag(squeeze(label)) for label in re.findall(r"\\label\s*\{([^{}]*)\}", row)]
        row = re.sub(r"\\label\s*\{[^{}]*\}", "", row)
        shown = [number for number in numbers if number]
        if shown:
            row = row.rstrip() + "\\qquad\\text{" + ", ".join(f"({number})" for number in shown) + "}"
        out.append(row)
    return "".join(out)


def math_text(tex: str, display: bool) -> str:
    """A formula's TeX as MathJax will read it: labels and tags out, no blank lines."""
    tex = re.sub(r"\\(?:label|tag\*?)\s*\{[^{}]*\}", "", tex)
    tex = re.sub(r"\\(?:nonumber|notag)(?![A-Za-z])", "", tex)
    tex = re.sub(r"\\ensuremath(?![A-Za-z])", "", tex)
    tex = re.sub(r"\\bm(?![A-Za-z])", r"\\boldsymbol", tex)
    lines = [line.strip() for line in tex.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines) if display else " ".join(lines).strip()


def closing_dollar(text: str, i: int, delimiter: str) -> int:
    """Where the formula that starts at text[i] ends: the next unescaped *delimiter* outside
    the braces the formula opens, so $\\text{a $b$}$ is one formula."""
    depth = 0
    j = i
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif depth <= 0 and text.startswith(delimiter, j):
            return j
        j += 1
    return len(text)


class Writer:
    """Turns a blueprint's TeX into Markdown. *ref* gives the Markdown for a reference to a
    label, *bib* each citation key's label and link, and *tag* the number a display shows
    for one of its labels (None to show none)."""

    def __init__(self, macros: dict[str, Macro], ref: Callable[[str, str], str] | None = None,
                 bib: dict[str, tuple[str, str | None]] | None = None, markdown: bool = True,
                 tag: Callable[[str], str | None] | None = None):
        self.macros = macros
        self.ref = ref or (lambda label, command: label)
        self.bib = bib or {}
        self.markdown = markdown
        self.tag = tag or (lambda label: None)
        self.unknown: Counter[str] = Counter()

    # ---- entry points

    def statement(self, tex: str) -> str:
        """Markdown for the text of a statement or proof."""
        return render(self.blocks(expand(tex, self.macros)))

    def plain(self, tex: str) -> str:
        """One line of text for a title: formatting dropped, formulas kept as TeX, and a
        reference as the words it links."""
        writer = Writer(self.macros, lambda label, command: unlinked(self.ref(label, command)), self.bib,
                        markdown=False)
        text = writer.inline(expand(tex, self.macros))
        self.unknown.update(writer.unknown)
        return close_quotes(re.sub(r"\s+", " ", text).strip())

    def citation(self, keys: list[str], note: str | None) -> str:
        """(label, label, note), as author-year styles print it: each label linked to its work
        when the bibliography gives a link, and the note, already written, as it is."""
        works = []
        for key in keys:
            label, url = self.bib.get(key, (key, None))
            if not self.markdown:
                works.append(label)
            elif url:
                works.append(f"[{self.text(label)}]({link_url(url)})")
            else:
                works.append(self.text(label))
        return "(" + ", ".join(works + ([note] if note else [])) + ")"

    # ---- block level

    def blocks(self, tex: str) -> list:
        out: list = []
        para: list[str] = []

        def flush() -> None:
            text = close_quotes(re.sub(r"\s+", " ", "".join(para)).strip())
            para.clear()
            if text:
                out.append(Para(text))

        def display(formula: str, end: int) -> int:
            """Add a display; punctuation just after it moves inside, before any number the
            display shows, so it opens no paragraph."""
            flush()
            stop = re.match(r"\s*([.,;:])(?=\s|$)", tex[end:])
            if stop:
                # On the last row: before its number, inside the rows' environment.
                tail = re.search(r"(?:\\qquad\\text\{[^{}]*\}\s*)?(?:\\end\{(?:aligned|gathered|alignedat|split)\}\s*)?$",
                                 formula)
                cut = tail.start() if tail.group() else len(formula.rstrip())
                formula = formula[:cut].rstrip() + stop.group(1) + formula[cut:]
            out.append(Display(math_text(formula.rstrip(), True)))
            return end + stop.end() if stop else end

        i = 0
        while i < len(tex):
            brk = PARBREAK.match(tex, i)
            if brk:
                flush()
                i = brk.end()
                continue
            if tex.startswith("$$", i):
                end = closing_dollar(tex, i + 2, "$$")
                i = display(tagged(tex[i + 2 : end], self.tag), end + 2)
                continue
            if tex.startswith("\\[", i):
                end = tex.find("\\]", i + 2)
                end = len(tex) if end < 0 else end
                i = display(tagged(tex[i + 2 : end], self.tag), end + 2)
                continue
            if tex.startswith("\\begin", i) and re.match(r"\\begin\s*\{", tex[i:]):
                env_arg = argument(tex, i + len("\\begin"))
                env = env_arg[0].strip()
                body_start = env_arg[1]
                body_end, end = environment_end(tex, body_start, env)
                body = tex[body_start:body_end]
                if env in DISPLAY_MATH or env in INNER_MATH:
                    i = display(self.display_env(env, tagged(body, self.tag)), end)
                    continue
                elif env in LISTS:
                    flush()
                    out.extend(self.list_block(env, body))
                elif env in QUOTES:
                    flush()
                    out.append(Quote(self.blocks(body)))
                elif env in OMITTED:
                    flush()
                    out.append(Omitted(OMITTED[env]))
                elif env in CODE_BLOCKS:
                    flush()
                    out.append(self.code(env, body))
                elif env in TABULARS:
                    flush()
                    out.append(self.table(env, body))
                elif env in FLOATS:
                    flush()
                    out.extend(self.float(env, body))
                else:
                    flush()
                    out.extend(self.blocks(self.skip_env_args(env, body)))
                i = end
                continue
            if tex.startswith("\\par", i) and not tex[i + 4 : i + 5].isalpha():
                flush()
                i += 4
                continue
            j = self.inline_step(tex, i, para)
            i = j
        flush()
        return out

    def display_env(self, env: str, body: str) -> str:
        if env in INNER_MATH:
            return f"\\begin{{{env}}}{body}\\end{{{env}}}"
        inner = DISPLAY_MATH[env]
        if inner is None:
            return body
        if inner == "alignedat":
            count = argument(body, 0)
            columns, body = (count[0], body[count[1]:]) if count else ("1", body)
            return f"\\begin{{alignedat}}{{{columns}}}{body}\\end{{alignedat}}"
        return f"\\begin{{{inner}}}{body}\\end{{{inner}}}"

    @staticmethod
    def code(env: str, body: str) -> Code:
        """A verbatim block, as typed; a listing's language, when it names one."""
        language = ""
        if env == "lstlisting" or env == "Verbatim":
            options = optional(body, 0) if body.lstrip(" \t").startswith("[") else None
            if options:
                body = body[options[1] :]
                named = re.search(r"language\s*=\s*\{?([\w+#-]+)", options[0])
                language = named.group(1) if named else ""
        elif env == "minted":
            name = argument(body, 0)
            if name:
                language, body = name[0].strip(), body[name[1] :]
        lines = body.split("\n")
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        return Code(textwrap.dedent("\n".join(lines)), language.lower())

    def table(self, env: str, body: str) -> Table:
        """A tabular as a Markdown table: its first row is the header."""
        for _ in range(2 if env in ("tabular*", "tabularx") else 1):  # a width, then the column spec
            arg = argument(body, 0)
            body = body[arg[1] :] if arg else body
        rows = []
        for row in split_top(RULES.sub(" ", body), "\\\\"):
            if not row.strip():
                continue
            cells = []
            for cell in split_top(row, "&"):
                span = re.match(r"\s*\\multicolumn\s*\{(\d+)\}\s*\{[^}]*\}\s*", cell)
                if span:
                    text = argument(cell, span.end())
                    cell = text[0] if text else ""
                cells.append(table_cell(self.inline(cell)))
                cells += [""] * (int(span.group(1)) - 1 if span else 0)
            rows.append(cells)
        return Table(rows)

    def float(self, env: str, body: str) -> list:
        """A figure or table: what of it can be shown, and its caption, headed with its number."""
        placement = optional(body, 0) if body.lstrip(" \t").startswith("[") else None
        body = body[placement[1] :] if placement else body
        if env == "wrapfigure":  # its place and width
            for _ in range(2):
                arg = argument(body, 0)
                body = body[arg[1] :] if arg else body
        caption = re.search(r"\\caption\s*(?:\[[^\]]*\])?\s*(?=\{)", body)
        text = None
        if caption:
            end = group_end(body, caption.end())
            text = body[caption.end() + 1 : end - 1]
            body = body[: caption.start()] + "\x00" + body[end:]
        numbers = [number for label in re.findall(r"\\label\s*\{([^{}]*)\}", body + (text or ""))
                   if (number := self.tag(squeeze(label)))]
        head = f"**{numbers[0] if numbers else FLOATS[env]}.**"
        before, _, after = body.partition("\x00")
        above = [block for block in self.blocks(before) if not isinstance(block, Omitted)]
        below = [block for block in self.blocks(after) if not isinstance(block, Omitted)]
        if FLOATS[env] == "Figure" and not above + below:
            note = "*(The picture is not reproduced here.)*"
            return [Para(f"{head} {self.inline(text).strip()} {note}" if text else f"{head} {note}")]
        lead = [Para(f"{head} {self.inline(text).strip()}")] if text else []
        # The caption stays where the source put it, above or below what it describes.
        return above + lead + below

    @staticmethod
    def skip_env_args(env: str, body: str) -> str:
        # minipage{width}, and the like: drop a leading argument that is a length.
        if env in ("minipage", "center", "flushleft", "flushright", "small", "footnotesize"):
            opt = optional(body, 0)
            body = body[opt[1]:] if opt else body
            if env == "minipage":
                arg = argument(body, 0)
                body = body[arg[1]:] if arg else body
        return body

    def list_block(self, env: str, body: str) -> list:
        """The list, after any text before its first \\item: where a theorem-like environment
        cut a list in two, the second half opens with the rest of the item it was in."""
        block = ListBlock(LISTS[env])
        starts = []
        depth = 0
        for match in re.finditer(r"\\(?:begin|end)\s*\{[^}]*\}|\\item(?![A-Za-z])|\\.|[{}]", body):
            token = match.group()
            if token.startswith("\\begin") or token == "{":
                depth += 1
            elif token.startswith("\\end") or token == "}":
                depth -= 1
            elif token.startswith("\\item") and depth == 0:
                starts.append(match)
        for k, match in enumerate(starts):
            end = starts[k + 1].start() if k + 1 < len(starts) else len(body)
            item = body[match.end() : end]
            label = ""
            opt = optional(item, 0)
            if opt:
                label, item = self.inline(opt[0]), item[opt[1]:]
            block.items.append((label, self.blocks(item)))
        lead = self.blocks(body[: starts[0].start()] if starts else body)
        return lead + [block] if block.items else lead

    # ---- inline level

    def inline(self, tex: str) -> str:
        """Markdown for TeX inside a paragraph: block constructs become inline ones."""
        para: list[str] = []
        i = 0
        while i < len(tex):
            if tex.startswith("$$", i):
                end = closing_dollar(tex, i + 2, "$$")
                para.append(self.inline_math(tex[i + 2 : end]))
                i = end + 2
                continue
            if tex.startswith("\\[", i):
                end = tex.find("\\]", i + 2)
                end = len(tex) if end < 0 else end
                para.append(self.inline_math(tex[i + 2 : end]))
                i = end + 2
                continue
            if tex.startswith("\\begin", i) and re.match(r"\\begin\s*\{", tex[i:]):
                env_arg = argument(tex, i + len("\\begin"))
                env = env_arg[0].strip()
                body_end, end = environment_end(tex, env_arg[1], env)
                body = tex[env_arg[1] : body_end]
                if env in DISPLAY_MATH or env in INNER_MATH:
                    para.append(self.inline_math(self.display_env(env, body)))
                elif env in OMITTED:
                    para.append(f"({OMITTED[env]} in the source)")
                else:
                    para.append(" " + self.inline(re.sub(r"\\item(?![A-Za-z])\s*(\[[^\]]*\])?", "; ", body)) + " ")
                i = end
                continue
            i = self.inline_step(tex, i, para)
        return "".join(para)

    def inline_math(self, tex: str) -> str:
        text = math_text(tex, False)
        return f"${safe_math_markdown('$' + text + '$')[1:-1]}$" if text else ""

    def inline_step(self, tex: str, i: int, para: list[str]) -> int:
        """Convert the construct at tex[i] into para; return where the next one starts."""
        c = tex[i]
        if c == "$":
            end = closing_dollar(tex, i + 1, "$")
            para.append(self.inline_math(tex[i + 1 : end]))
            return end + 1
        if tex.startswith("\\(", i):
            end = tex.find("\\)", i + 2)
            end = len(tex) if end < 0 else end
            para.append(self.inline_math(tex[i + 2 : end]))
            return end + 2
        if c == "\\":
            return self.command(tex, i, para)
        if c == "{":
            end = group_end(tex, i)
            para.append(self.group(tex[i + 1 : end - 1]))
            return end
        if c == "}":
            return i + 1
        j = i
        while j < len(tex) and tex[j] not in "\\${}" and not PARBREAK.match(tex, j):
            j += 1
        para.append(self.text(tex[i:j]))
        return j if j > i else i + 1

    def group(self, tex: str) -> str:
        match = re.match(r"\s*\\([A-Za-z]+)(?![A-Za-z])", tex)
        if match and match.group(1) in SWITCHES:
            inner = self.inline(tex[match.end():]).strip()
            style = SWITCHES[match.group(1)]
            return self.styled(inner, style)
        return self.inline(tex)

    def styled(self, inner: str, style: str | None) -> str:
        if not inner or not self.markdown or style is None:
            return inner
        mark = "**" if style == "strong" else "*"
        return f"{mark}{inner}{mark}"

    def text(self, run: str) -> str:
        run = run.replace("~", " ").replace("---", "—").replace("--", "–")
        run = run.replace("``", "“").replace("''", "”").replace("`", "‘")
        if not self.markdown:
            return run
        # A bracket is escaped only where it would close a link: an escaped \[ that opens a
        # paragraph ending in \] reads as display math.
        run = re.sub(r"([*_#])", r"\\\1", run)
        run = re.sub(r"\](?=[(\[:])", r"\\]", run)
        return run.replace("<", "$<$").replace(">", "$>$")

    def command(self, tex: str, i: int, para: list[str]) -> int:
        match = CONTROL.match(tex, i)
        name = match.group()[1:]
        j = match.end()
        if len(name) == 1 and not name.isalpha():
            if name in ACCENTS:
                return self.accent(tex, j, name, para)
            para.append(SYMBOLS.get(name, "") if self.markdown else SYMBOLS.get(name, "").replace("\\", ""))
            return j
        if name in ACCENTS and len(name) == 1:
            return self.accent(tex, j, name, para)
        if name in LETTERS:
            letter = LETTERS[name]
            para.append(letter if self.markdown else letter.replace("$", "").replace("\\\\", "\\"))
            return j
        if name in QUIET:
            para.append(" " if name in ("quad", "qquad", "enspace", "thinspace", "newline", "linebreak", "item") else "")
            return j
        if name in DROPPED:
            return self.skip_args(tex, j, name)
        if name in SWITCHES:
            return j
        if name in EMPHASIS or name in STRONG:
            arg = argument(tex, j)
            if not arg:
                return j
            para.append(self.styled(self.inline(arg[0]).strip(), "strong" if name in STRONG else "em"))
            return arg[1]
        if name in CODE:
            arg = argument(tex, j)
            if not arg:
                return j
            code = self.plain_text(arg[0])
            para.append(f"`{code}`" if self.markdown and code else code)
            return arg[1]
        if name in TRANSPARENT:
            arg = argument(tex, j)
            if not arg:
                return j
            if name == "texorpdfstring":
                # The second argument is for PDF bookmarks; titles here keep their formulas.
                second = argument(tex, arg[1])
                para.append(self.inline(arg[0]))
                return second[1] if second else arg[1]
            if name == "foreignlanguage":
                second = argument(tex, arg[1])
                para.append(self.inline(second[0]) if second else "")
                return second[1] if second else arg[1]
            para.append(self.inline(arg[0]))
            return arg[1]
        if name == "ensuremath":
            arg = argument(tex, j)
            if arg:
                para.append(self.inline_math(arg[0]))
                return arg[1]
            return j
        if name in REFS:
            star = j < len(tex) and tex[j] == "*"
            arg = argument(tex, j + star)
            if not arg:
                return j
            links = [self.ref(label, name) for label in names(arg[0])]
            para.append(", ".join(links[:-1]) + (" and " if len(links) > 1 else "") + links[-1] if links else "")
            return arg[1]
        if name in CITES:
            notes = []
            k = j
            while (opt := optional(tex, k)) is not None:
                notes.append(opt[0])
                k = opt[1]
            arg = argument(tex, k)
            if not arg:
                return j
            note = re.sub(r"\s+", " ", self.inline(notes[-1])).strip() if notes and notes[-1].strip() else None
            para.append(self.citation(names(arg[0]), note))
            return arg[1]
        if name == "href":
            url = argument(tex, j)
            label = argument(tex, url[1]) if url else None
            if not label:
                return j
            text = self.inline(label[0]).strip()
            target = tex_url(url[0])
            para.append(f"[{text}]({link_url(target)})" if self.markdown and is_web(target) else text)
            return label[1]
        if name == "url":
            url = argument(tex, j)
            if not url:
                return j
            target = tex_url(url[0])
            para.append(f"<{target}>" if self.markdown and is_web(target) else target)
            return url[1]
        if name == "footnote":
            arg = argument(tex, j)
            if not arg:
                return j
            para.append(f" ({self.inline(arg[0]).strip()})")
            return arg[1]
        if name == "hyperref":
            opt = optional(tex, j)
            arg = argument(tex, opt[1] if opt else j)
            if not arg:
                return j
            text = self.inline(arg[0]).strip()
            para.append(self.ref(opt[0].strip(), name) if opt and not text else text)
            return arg[1]
        if name == "textcolor":
            color = argument(tex, j)
            arg = argument(tex, color[1]) if color else None
            if not arg:
                return j
            para.append(self.inline(arg[0]))
            return arg[1]
        if name in ("begin", "end"):
            arg = argument(tex, j)
            return arg[1] if arg else j
        if name in MATH_ONLY:
            para.append(self.inline_math("\\" + name) if self.markdown else "\\" + name)
            return j
        # Unknown: keep what a reader can use, the text of its last braced argument.
        self.unknown[name] = self.unknown[name] + 1
        k, last = j, None
        while k < len(tex) and tex[k] == "{":
            end = group_end(tex, k)
            last = tex[k + 1 : end - 1]
            k = end
        if last is not None:
            para.append(self.inline(last))
            return k
        return j

    def accent(self, tex: str, j: int, name: str, para: list[str]) -> int:
        arg = argument(tex, j)
        if not arg:
            return j
        base = arg[0]
        base = {"\\i": "i", "\\j": "j"}.get(base, base)
        if len(base) != 1:
            para.append(self.inline(base))
            return arg[1]
        para.append(unicodedata.normalize("NFC", base + ACCENTS[name]))
        return arg[1]

    @staticmethod
    def skip_args(tex: str, j: int, name: str) -> int:
        star = j < len(tex) and tex[j] == "*"
        k = j + star
        opt = optional(tex, k)
        k = opt[1] if opt else k
        count = {"setlength": 2, "addtolength": 2, "addcontentsline": 3, "raisebox": 2}.get(name, 1)
        if name in ("kern", "hskip", "vskip"):
            match = re.match(r"\s*-?[\d.]+\s*[a-z]{2}", tex[k:])
            return k + match.end() if match else k
        for _ in range(count):
            arg = argument(tex, k)
            if not arg:
                break
            k = arg[1]
        if name == "raisebox":
            arg = argument(tex, k)
            k = arg[1] if arg else k
        return k

    def plain_text(self, tex: str) -> str:
        writer = Writer(self.macros, self.ref, self.bib, markdown=False)
        return re.sub(r"\s+", " ", writer.inline(tex)).strip()


def cited(text: str) -> list[str]:
    """The keys text cites, in order."""
    pattern = r"\\(?:" + "|".join(sorted(CITES)) + r")\*?(?:\s*\[[^\]]*\])*\s*\{([^}]*)\}"
    return [key for match in re.finditer(pattern, text) for key in names(match.group(1))]


def unlinked(markdown: str) -> str:
    """markdown as plain text: each link's words without its target, and the escapes undone
    outside formulas."""
    words = re.sub(r"\[((?:\\.|[^\]\\])*)\]\([^)\s]*\)", lambda link: link.group(1), markdown)
    out, last = [], 0
    for match in MATH_SPAN.finditer(words):
        out.append(re.sub(r"\\([\\`*_\[\]#])", r"\1", words[last : match.start()]))
        out.append(match.group())
        last = match.end()
    out.append(re.sub(r"\\([\\`*_\[\]#])", r"\1", words[last:]))
    return "".join(out)


def is_web(url: str) -> bool:
    return url.startswith(("http://", "https://", "mailto:"))


def tex_url(url: str) -> str:
    """A URL as its TeX spells it, the escapes undone: \\# is #, and $\\sim$ or \\~{} is ~."""
    url = re.sub(r"\$\\sim\$|\\~\{\}|\\textasciitilde(?:\{\})?", "~", url.strip())
    return re.sub(r"\\([#%_&~])", r"\1", url)


def link_url(url: str) -> str:
    """A URL safe inside a Markdown link: no spaces or parentheses."""
    return url.strip().replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def render(blocks: list, indent: int = 0) -> str:
    """Markdown for blocks; list items indent their contents by four spaces, as
    Python-Markdown requires."""
    parts = []
    for block in blocks:
        if isinstance(block, Para):
            parts.append(paragraph_start(block.text))
        elif isinstance(block, Display):
            if block.tex:
                parts.append(f"$$\n{safe_math_markdown('$$' + block.tex + '$$')[2:-2]}\n$$")
        elif isinstance(block, ListBlock):
            items = []
            for number, (label, item) in enumerate(block.items, 1):
                marker = f"{number}. " if block.kind == "ol" and not label else "- "
                body = render(item)
                if label:
                    lead = f"**{label}**" if block.kind == "dl" else label
                    body = f"{lead} {body}" if body and not body.startswith("$$") else f"{lead}\n\n{body}".rstrip()
                first, *rest = body.split("\n") if body else [""]
                # An item that opens with a display keeps it on the marker line: "- $$".
                items.append("\n".join([(marker + first).rstrip(), *("    " + line if line else "" for line in rest)]))
            # An item of several lines ends in an indented line, which would swallow the next
            # marker as its continuation; blank lines between items keep each one its own.
            parts.append(("\n\n" if any("\n" in item for item in items) else "\n").join(items))
        elif isinstance(block, Quote):
            inner = render(block.blocks)
            parts.append("\n".join("> " + line if line else ">" for line in inner.split("\n")))
        elif isinstance(block, Omitted):
            parts.append(f"*({block.what.capitalize()} in the source is not reproduced here.)*")
        elif isinstance(block, Code):
            fence = "~~~~" if "```" in block.text else "```"
            parts.append(f"{fence}{block.language}\n{block.text}\n{fence}")
        elif isinstance(block, Table) and block.rows:
            width = max(len(row) for row in block.rows)
            rows = [row + [""] * (width - len(row)) for row in block.rows]
            lines = ["| " + " | ".join(rows[0]) + " |", "|" + " --- |" * width]
            lines += ["| " + " | ".join(row) + " |" for row in rows[1:]]
            parts.append("\n".join(lines))
    return "\n\n".join(part for part in parts if part.strip())


def split_top(text: str, separator: str) -> list[str]:
    """text split at *separator* outside braces and environments; an escaped character, such
    as \\&, never separates."""
    parts, depth, start = [], 0, 0
    for match in re.finditer(r"\\(?:begin|end)\s*\{[^}]*\}|" + re.escape(separator) + r"|\\.|[{}]", text):
        token = match.group()
        if token == "{" or token.startswith("\\begin"):
            depth += 1
        elif token == "}" or token.startswith("\\end"):
            depth -= 1
        elif token == separator and depth == 0:
            parts.append(text[start : match.start()])
            start = match.end()
    parts.append(text[start:])
    return parts


def table_cell(markdown: str) -> str:
    """A cell's Markdown on one line, with no bar that would end the cell: in a formula a bar
    becomes \\vert."""
    markdown = re.sub(r"\s+", " ", markdown).strip()
    out, last = [], 0
    for match in MATH_SPAN.finditer(markdown):
        out.append(markdown[last : match.start()].replace("|", "\\|"))
        out.append(match.group().replace("\\|", "\\Vert ").replace("|", "\\vert "))
        last = match.end()
    out.append(markdown[last:].replace("|", "\\|"))
    return "".join(out)


def close_quotes(text: str) -> str:
    """text with the ' that closes each ‘ made ’, as TeX prints `quoted'; an apostrophe
    inside a word stays as typed, and formulas are left alone."""
    if "‘" not in text:
        return text
    out = list(text)
    quoted = False
    i = 0
    while i < len(text):
        if text.startswith("$$", i):
            i = closing_dollar(text, i + 2, "$$") + 2
            continue
        c = text[i]
        if c == "$":
            i = closing_dollar(text, i + 1, "$") + 1
            continue
        if c == "\\":
            i += 2
            continue
        if c == "‘":
            quoted = True
        elif c == "'" and quoted and not text[i + 1 : i + 2].isalpha():
            out[i] = "’"
            quoted = False
        i += 1
    return "".join(out)


def paragraph_start(text: str) -> str:
    """Keep a paragraph's first characters from reading as a list, heading or quote."""
    match = re.match(r"(\d+)([.)])(\s)", text)
    if match:
        return f"{match.group(1)}\\{match.group(2)}{text[match.end(2):]}"
    if re.match(r"[-+*](\s)", text):
        return "\\" + text
    return text
