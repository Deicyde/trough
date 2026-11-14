"""Read Lean 4 source without Lean: the declarations a file makes, by full name.

Comments, docstrings, strings and attributes are blanked first, so a name inside
them is never read as a declaration. Scopes follow `namespace`, `section`,
`mutual` and `end`, and `_root_` puts a name at the top level. The reading is
conservative, because a declaration it wrongly reports is worse than one it
misses: a file whose scopes do not close as they open declares nothing, a
declaration counts only when its command names it on the keyword's line, names
Lean makes itself (constructors, fields, `ext` lemmas, an anonymous instance's
name) are not read, a `private` declaration counts as not declared (Lean renames
it), and nothing after `#exit` is read. An indented `end` inside a declaration
is part of it, as a notation may use the word, and `end section` closes a scope
and opens a section, as Lean reads it. One risk remains: a declaration
written inside a syntax quotation, as a macro may build one, reads as the file's
own.

Each declaration also carries what is attached to it: its docstring, the
attributes of the `@[...]` list before it, and its statement, the text up to the
`:=` or `where` that starts its value, with whether that value holds `sorry`.
declarations() also gives, in file order, the `private` declarations under the
names they are written with and the anonymous instances with no name, for a
reader that has to account for every attribute a file writes; with *relaxed*,
it also reads a name written on the line after its keyword and a modifier
written before the keyword's line (`@[simp] noncomputable` above a `def`).
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

KINDS = {"theorem": "theorem", "lemma": "lemma", "def": "def", "abbrev": "abbrev", "instance": "instance",
         "structure": "structure", "class": "class", "inductive": "inductive", "opaque": "opaque",
         "axiom": "axiom", "irreducible_def": "def", "alias": "alias"}
COMPONENT = r"(?:«[^»\n]*»|[^\s.:()\[\]{}⟨⟩,«»@]+)"
NAME = rf"{COMPONENT}(?:\.{COMPONENT})*"
MODIFIERS = r"(?:(?:private|protected|noncomputable|partial|unsafe|nonrec|public|meta|scoped|local)\s+)*"
# "open Foo in", "set_option x y in": a prefix that scopes one command.
IN_PREFIX = r"(?:(?:open|set_option|omit|include)\b[^\n]*?\bin\s+)*"
# Batteries' `proof_wanted`, and the `theorem_wanted` and `def_wanted` commands a library may define: a statement
# whose proof, or a definition whose value, is deferred. declarations() reads them only when asked.
WANTED_KINDS = {"proof_wanted": "proof_wanted", "theorem_wanted": "theorem_wanted", "def_wanted": "def_wanted"}


def declaration_pattern(kinds: dict[str, str]) -> re.Pattern:
    return re.compile(
        rf"^[ \t]*{IN_PREFIX}(?P<modifiers>{MODIFIERS})(?:class\s+(?=inductive\b))?(?P<kind>{'|'.join(kinds)})\b[ \t]*"
        rf"(?:\(priority\s*:=[^)\n]*\)[ \t]*)?(?P<name>{NAME})?",
        re.M,
    )


DECLARATION = declaration_pattern(KINDS)
DECLARATION_WANTED = declaration_pattern(KINDS | WANTED_KINDS)
NAMESPACE = re.compile(rf"^[ \t]*namespace[ \t]+(?P<name>{NAME})[ \t]*$")
SECTION = re.compile(rf"^[ \t]*(?:(?:noncomputable|public)[ \t]+)*section(?:[ \t]+(?P<name>{NAME}))?[ \t]*$")
MUTUAL = re.compile(r"^[ \t]*mutual[ \t]*$")
END = re.compile(rf"^[ \t]*end(?:[ \t]+(?P<name>{NAME}))?[ \t]*$")
# A line at column 0 that starts a command ends the declaration before it.
def command_pattern(kinds: dict[str, str]) -> re.Pattern:
    return re.compile(
        rf"^(?:{IN_PREFIX}{MODIFIERS}(?:{'|'.join(kinds)}|example|namespace|section|end|open|variable|universe|"
        r"set_option|attribute|mutual|notation|infix|infixl|infixr|prefix|postfix|macro|macro_rules|syntax|elab|"
        r"elab_rules|alias|export|initialize|omit|include|deriving|#\w+)\b)"
    )


COMMAND = command_pattern(KINDS)
COMMAND_WANTED = command_pattern(KINDS | WANTED_KINDS)
SORRY = re.compile(r"(?<![\w.'])(?:sorry|sorryAx|admit)(?![\w'!?])|^[ \t]*(?:·[ \t]*)?stop(?![\w'!?])(?!\s*:=)", re.M)
EXIT = re.compile(r"^#exit\b")
RAW_STRING = re.compile(r'r(#*)"')
NOT_NAMES = {"where", "extends", "deriving"}
# A modifier ending the text before a declaration's keyword line.
MODIFIER_BEFORE = re.compile(r"(?<![\w.'])(?:private|protected|noncomputable|partial|unsafe|nonrec|public|meta)\s*$")
# What decides where a statement ends: brackets, `:=` or a `where` that gives the value by fields, and the
# `let` and `have` whose own `:=` comes first.
VALUE_TOKENS = re.compile(r"«[^»\n]*»|:=|[(\[{⟨⦃)\]}⟩⦄]|(?<![\w.'])(?:let|have|letI|haveI|where)(?![\w'!?])")
OPENERS, CLOSERS = "([{⟨⦃", ")]}⟩⦄"


@dataclass(frozen=True)
class Declaration:
    name: str
    kind: str
    line: int
    sorry: bool  # its text in the file holds `sorry`, `sorryAx`, `admit` or a `stop` tactic
    doc: str = ""  # its docstring, without the delimiters
    attributes: tuple[str, ...] = ()  # each attribute of its `@[...]` list, as written, whitespace collapsed
    statement: str | None = None  # its text up to the `:=` or `where` that starts its value; None when not found
    proof_sorry: bool = False  # its value, the text from there on, holds what `sorry` marks
    private: bool = False  # written `private`: Lean renames it, so scan() leaves it out


def spans(text: str) -> list[tuple[int, int, str]]:
    """The comments, docstrings, strings and character literals of the text, in order, as
    (start, end, kind); kind is "comment", "doc" (a declaration's docstring), "module doc" or "string"."""
    found: list[tuple[int, int, str]] = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if text.startswith("--", i):
            end = text.find("\n", i)
            end = n if end < 0 else end
            found.append((i, end, "comment"))
            i = end
        elif text.startswith("/-", i):
            # A docstring's body starts after "/--" or "/-!", so "/--/" opens one.
            depth, j = 1, i + 3 if text[i + 2:i + 3] in ("-", "!") else i + 2
            while j < n and depth:
                if text.startswith("/-", j):
                    depth += 1
                    j += 2
                elif text.startswith("-/", j):
                    depth -= 1
                    j += 2
                else:
                    j += 1
            kind = "doc" if text.startswith("/--", i) else "module doc" if text.startswith("/-!", i) else "comment"
            found.append((i, min(j, n), kind))
            i = j
        elif c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            found.append((i, min(j + 1, n), "string"))
            i = j + 1
        elif c == "r" and (i == 0 or not (text[i - 1].isalnum() or text[i - 1] in "_'!?.")) and (
                raw := RAW_STRING.match(text, i)):
            # A raw string has no escapes and ends at a quote followed by as many hashes as opened it.
            close_at = text.find('"' + raw.group(1), raw.end())
            end = n if close_at < 0 else close_at + 1 + len(raw.group(1))
            found.append((i, end, "string"))
            i = end
        elif c == "«":
            j = text.find("»", i)
            i = n if j < 0 else j + 1
        elif c == "'" and (i == 0 or not (text[i - 1].isalnum() or text[i - 1] in "_'!?.")):
            literal = re.compile(r"'(?:\\[^\n]|\\u\{[0-9a-fA-F]+\}|[^\\'\n])'").match(text, i)
            if literal:
                found.append((i, literal.end(), "string"))
                i = literal.end()
            else:
                i += 1
        else:
            i += 1
    return found


def clear(text: str, cleared: list[tuple[int, int, str]]) -> str:
    """The text with each span turned to spaces, keeping every newline."""
    out, last = [], 0
    for start, end, _ in cleared:
        out += [text[last:start], re.sub(r"[^\n]", " ", text[start:end])]
        last = end
    return "".join(out) + text[last:]


def blank(text: str) -> str:
    """The text with comments, docstrings, strings and character literals turned to spaces, keeping
    every newline, so line numbers and columns stay where they were."""
    return clear(text, spans(text))


def blank_attributes(text: str) -> str:
    """Blank each `@[...]` attribute list, which may span lines and nest brackets."""
    out = list(text)
    i = text.find("@[")
    while i >= 0:
        depth, j = 0, i + 1
        while j < len(text):
            if text[j] == "[":
                depth += 1
            elif text[j] == "]":
                depth -= 1
                if not depth:
                    break
            j += 1
        for k in range(i, min(j + 1, len(text))):
            if out[k] != "\n":
                out[k] = " "
        i = text.find("@[", j + 1)
    return "".join(out)


def scan(text: str) -> dict[str, Declaration] | None:
    """Each declaration the file makes, by full name; None when its scopes don't close as they open."""
    found = declarations(text)
    if found is None:
        return None
    named: dict[str, Declaration] = {}
    for declaration in found:
        if declaration.name and not declaration.private:
            named.setdefault(declaration.name, declaration)
    return named


def declarations(text: str, relaxed: bool = False, wanted: bool = False) -> list[Declaration] | None:
    """Each declaration the file writes, in order: those scan() gives, the `private` ones under their written
    full names, and the anonymous instances, whose name is ""; None when its scopes don't close as they open.
    With *relaxed*, a name on the line after its keyword counts too, and a modifier on the lines before the
    keyword's does not stand between the declaration and its attributes. With *wanted*, the WANTED_KINDS
    commands are declarations too, of their own kinds."""
    declaration, command = (DECLARATION_WANTED, COMMAND_WANTED) if wanted else (DECLARATION, COMMAND)
    found_spans = spans(text)
    code = clear(text, found_spans)
    # Comments go but strings stay, for reading attributes.
    plain = clear(text, [span for span in found_spans if span[2] != "string"])
    docs = {end: start for start, end, kind in found_spans if kind == "doc"}
    lines = blank_attributes(code).split("\n")
    source = text.split("\n")
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line) + 1)
    scopes: list[tuple[str, str]] = []  # (kind, the header's last component or "")
    found: list[Declaration] = []
    # name, kind, line, head, body start, its lines, private
    open_decl: tuple[str, str, int, int, int, list[str], bool] | None = None

    def close() -> None:
        nonlocal open_decl
        if open_decl:
            name, kind, line, head, start, body, private = open_decl
            joined = "\n".join(body)
            cut = value_start(joined)
            column = head - offsets[line - 1]
            if relaxed:
                # The keyword line's own indentation: an attribute list before the keyword is no indentation.
                column = len(source[line - 1]) - len(source[line - 1].lstrip(" "))
            statement = None if cut is None else dedent(text[head:start + cut].rstrip(), column)
            doc, attributes = attached(text, code, plain, docs, head, relaxed)
            found.append(Declaration(name, kind, line, bool(SORRY.search(joined)), doc, attributes, statement,
                                     cut is not None and bool(SORRY.search(joined[cut:])), private))
        open_decl = None

    for number, line in enumerate(lines, 1):
        if EXIT.match(line):
            break
        if open_decl and line[:1].strip() and command.match(line):
            close()
        if match := NAMESPACE.match(line):
            close()
            scopes += [("namespace", part) for part in split(match["name"])]
            continue
        if match := SECTION.match(line):
            close()
            scopes.append(("section", match["name"] or ""))
            continue
        if MUTUAL.match(line):
            close()
            scopes.append(("mutual", ""))
            continue
        if (match := END.match(line)) and not (open_decl and line[:1].isspace()):
            close()
            if match["name"] == "section":
                # `section` is a keyword, not a name, so Lean reads `end section` as `end`, then a new `section`.
                if not scopes or scopes.pop()[1]:
                    return None
                scopes.append(("section", ""))
            elif match["name"]:
                # `end A.B` closes a section named A.B, or namespaces A and B.
                if scopes and scopes[-1] == ("section", match["name"]):
                    scopes.pop()
                    continue
                parts = split(match["name"])
                if len(scopes) < len(parts):
                    return None
                for part in reversed(parts):
                    if scopes.pop() != ("namespace", part):
                        return None
            elif not scopes or scopes.pop()[1]:
                return None
            continue
        if match := declaration.match(line):
            close()
            name = match["name"]
            if relaxed and not name and not line[match.end():].strip():
                following = next((later for later in lines[number:] if later.strip()), "")
                token = re.match(rf"[ \t]+({NAME})(?=[\s:({{\[]|$)", following)
                if token and (token.group(1)[0].isalpha() or token.group(1)[0] in "_«") and token.group(1) not in NOT_NAMES:
                    name = token.group(1)
            anonymous = match["kind"] == "instance" and (not name or name in NOT_NAMES)
            if anonymous:
                # An anonymous instance's `where` belongs to its body.
                full, rest = "", match.start("name") if name else match.end()
            elif not name or name in NOT_NAMES:
                continue
            else:
                full = name[len("_root_."):] if name.startswith("_root_.") else ".".join(
                    [part for kind, part in scopes if kind == "namespace"] + [name])
                rest = match.end()
            base = offsets[number - 1]
            open_decl = (full, (KINDS | WANTED_KINDS)[match["kind"]], number, base + match.start("modifiers"), base + rest,
                         [line[rest:]], "private" in match["modifiers"].split())
            continue
        if open_decl:
            open_decl[5].append(line)
    close()
    return found


def value_start(code: str) -> int | None:
    """Where a declaration's value starts in its blanked text after the name: at the first `:=` outside
    brackets that no `let` or `have` before it claims, or at a `where` outside brackets before it. None when
    there is neither, as for a definition by pattern matching, or when the brackets close before they open."""
    depth, claimed = 0, Counter()
    for token in VALUE_TOKENS.finditer(code):
        word = token.group()
        if word[0] == "«":
            continue
        if word in OPENERS:
            depth += 1
        elif word in CLOSERS:
            claimed[depth] = 0
            depth -= 1
            if depth < 0:
                return None
        elif word == "where":
            if depth == 0:
                return token.start()
        elif word == ":=":
            if claimed[depth]:
                claimed[depth] -= 1
            elif depth == 0:
                return token.start()
        else:
            claimed[depth] += 1
    return None


def attached(text: str, code: str, plain: str, docs: dict[int, int], head: int,
             relaxed: bool = False) -> tuple[str, tuple[str, ...]]:
    """The docstring and attributes written before the declaration that starts at *head*: an `@[...]` list
    right before it, and a docstring right before that, with nothing but space and comments between; with
    *relaxed*, modifiers may stand between the list and the declaration's line."""

    def back(j: int) -> int:
        while j > 0 and code[j - 1].isspace() and j not in docs:
            j -= 1
        return j

    attributes: list[str] = []
    j = back(head)
    while relaxed and (modifier := MODIFIER_BEFORE.search(code[max(0, j - 24):j])):
        j = back(j - len(modifier.group()))
    while j > 0 and code[j - 1] == "]" and j not in docs:
        depth, k = 0, j - 1
        while k >= 0:
            if code[k] == "]":
                depth += 1
            elif code[k] == "[":
                depth -= 1
                if not depth:
                    break
            k -= 1
        if k < 1 or code[k - 1] != "@":
            break
        attributes[:0] = split_attributes(plain[k + 1:j - 1])
        j = back(k - 1)
    doc = docstring(text[docs[j] + 3:j - 2]) if j in docs else ""
    return doc, tuple(attributes)


def split_attributes(listing: str) -> list[str]:
    """The attributes of an `@[...]` list's inside, split at its top-level commas, whitespace outside strings
    collapsed."""
    parts, current, depth, i = [], [], 0, 0
    while i < len(listing):
        c = listing[i]
        if c == '"':
            j = i + 1
            while j < len(listing) and listing[j] != '"':
                j += 2 if listing[j] == "\\" else 1
            current.append(listing[i:j + 1])
            i = j + 1
            continue
        if c in OPENERS:
            depth += 1
        elif c in CLOSERS:
            depth -= 1
        if c == "," and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(c)
        i += 1
    parts.append("".join(current))
    return [text for text in (collapse(part) for part in parts) if text]


def collapse(text: str) -> str:
    """The text with each run of whitespace outside strings made one space."""
    pieces = re.split(r'("(?:\\.|[^"\\])*"?)', text)
    return "".join(piece if index % 2 else re.sub(r"\s+", " ", piece) for index, piece in enumerate(pieces)).strip()


def docstring(inside: str) -> str:
    """A docstring's text: its first line stripped, the rest without their common indentation."""
    lines = inside.split("\n")
    rest = [line for line in lines[1:] if line.strip()]
    width = min((len(line) - len(line.lstrip(" ")) for line in rest), default=0)
    return "\n".join([lines[0].strip()] + [line[width:].rstrip() for line in lines[1:]]).strip()


def dedent(statement: str, column: int) -> str:
    """A statement whose first line starts at *column*, with that much indentation taken off the others."""
    first, *rest = statement.split("\n")
    return "\n".join([first] + [line[min(column, len(line) - len(line.lstrip(" "))):] for line in rest])


def module_doc(text: str) -> str | None:
    """The file's first module docstring (`/-! ... -/`), its text as docstring() gives it."""
    for start, end, kind in spans(text):
        if kind == "module doc":
            return docstring(text[start + 3:end - 2])
    return None


def split(name: str) -> list[str]:
    return re.findall(COMPONENT, name)


IDENTIFIER = re.compile(rf"^{NAME}$")


def is_name(text: str) -> bool:
    """Whether text reads as one Lean name, not several names or a signature."""
    return bool(IDENTIFIER.match(text)) and not text.startswith(".") and not text[:1].isdigit()
