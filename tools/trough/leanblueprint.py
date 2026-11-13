"""Read a leanblueprint: its chapters, nodes, proofs and the marks on them.

This follows what leanblueprint and plastexdepgraph do with a blueprint's web
entry file, without plasTeX:

- the document is the entry file with every \\input and \\include expanded;
- the graph's nodes are the theorem-like environments of the kinds in the
  package's thms= option (by default definition, lemma, proposition, theorem
  and corollary); other theorem-like environments, such as remarks, are not;
- a node's id is the last \\label that lands on it, which may be one in its
  proof; the last \\lean and the last \\uses in an environment win;
- a proof belongs to the node its \\proves names, or else to the nearest
  theorem-like environment before it in the same sectioning unit, and a later
  proof of the same environment replaces an earlier one;
- \\leanok marks a statement, or a proof, as formalized; \\mathlibok marks a
  node as in Mathlib (and formalized); \\notready marks it as not ready.

A blueprint can also be LeanArchitect output, which `lake build :blueprint`
writes under .lake/build/blueprint from each declaration's @[blueprint]
attribute: a module file defines each node with \\newleannode{label}{\\input
{file}} and the module with \\newleanmodule{Module}{...}, and the document
places them with \\inputleannode and \\inputleanmodule. The reader reads those
files from a copy of that directory, as if their text stood where it is placed.
"""

from __future__ import annotations

import bisect
import re
from dataclasses import dataclass, field
from pathlib import Path

from trough.tex import (
    CONTROL,
    FLOATS,
    LISTS,
    argument,
    bracket_end,
    definitions,
    environment_end,
    group_end,
    names,
    optional,
    skip_space,
    squeeze,
    strip_comment,
)

DEFAULT_THMS = ("definition", "lemma", "proposition", "theorem", "corollary")
SECTIONING = ("part", "chapter", "section", "subsection", "subsubsection")
INPUT = re.compile(r"\\(input|include|inputleanmodule|inputleannode)\s*\{([^}]*)\}")
VERBATIM = re.compile(r"\\begin\s*\{(verbatim\*?|Verbatim|lstlisting|minted)\}")
ARCHITECT = "leanarchitect"  # where a copy of LeanArchitect's .lake/build/blueprint sits, beside the TeX
ARCHITECT_PATH = re.compile(r"(?:^|/)\.lake/build/blueprint/(.+)$")
UNREAD = re.compile(r" names no (?:file|module|node)$| nests too deep$")  # problems that leave text unread
# Files an \input can name that hold no blueprint text: a bibliography a LaTeX run writes, or Markdown
# such as an authors list. When one is missing, nothing the blueprint says is left unread.
NOT_TEX = (".bbl", ".md")
SECTION = re.compile(r"\\(part|chapter|section|subsection|subsubsection)(\*?)(?![A-Za-z])")
MATH = re.compile(
    r"(?s)\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)"
    r"|\\begin\s*\{(equation|align|gather|multline|eqnarray|flalign|alignat|displaymath|math)(\*?)\}.*?\\end\s*\{\1\2\}"
)


@dataclass
class Where:
    file: str
    line: int


@dataclass(eq=False)
class Proof:
    body: str
    leanok: bool
    uses: list[str]
    labels: list[str]
    where: Where
    title: str | None = None  # its optional argument, as in \\begin{proof}[Proof of the main theorem]
    offset: int = 0  # where in the document it starts
    unit: Unit | None = None


@dataclass(eq=False)
class Unit:
    """A chapter, section or smaller sectioning unit."""

    level: int  # index into SECTIONING
    title: str
    where: Where
    label: str | None = None
    parent: Unit | None = None
    offset: int = 0  # where in the document it starts


@dataclass(eq=False)
class Prose:
    """A run of the document's text between its sectioning commands and environments."""

    text: str
    where: Where
    unit: Unit | None
    offset: int
    equations: list[str] = field(default_factory=list)
    floats: list[tuple[str, str]] = field(default_factory=list)  # (label, "figure" or "table")


@dataclass(eq=False)
class Node:
    env: str
    title: str | None
    body: str
    labels: list[str]
    lean: list[str]
    leanok: bool
    mathlibok: bool
    notready: bool
    discussion: str | None
    uses: list[str]
    where: Where
    unit: Unit | None
    graph: bool  # one of the thms kinds, so a node of the dependency graph
    proof: Proof | None = None
    equations: list[str] = field(default_factory=list)
    id: str = ""
    offset: int = 0  # where in the document it starts
    end: int = 0  # and where its statement ends
    floats: list[tuple[str, str]] = field(default_factory=list)  # (label, "figure" or "table")

    @property
    def proof_uses(self) -> list[str]:
        return self.proof.uses if self.proof else []


@dataclass
class Blueprint:
    files: list[str]
    macros: dict
    captions: dict[str, str]  # theorem-like environment -> its printed name
    thms: tuple[str, ...]
    units: list[Unit]
    nodes: list[Node]  # every theorem-like environment, in document order
    labels: dict[str, object]  # label -> Node, Unit, ("equation", its Node or Prose) or ("figure"/"table", ...)
    links: dict[str, str]  # home, github, dochome
    problems: list[str]
    prose: list[Prose] = field(default_factory=list)  # in document order, from the first sectioning unit on
    bibliography: list[str] = field(default_factory=list)  # the .bib files it cites from

    @property
    def graph(self) -> list[Node]:
        return [node for node in self.nodes if node.graph]


class Document:
    """A blueprint's TeX with \\input expanded and comments removed, and where each line is from."""

    def __init__(self, root: Path, entry: str, architect: Path | None = None):
        self.root = root
        self.architect = architect or root / ARCHITECT
        self.lean_nodes: dict[str, str] = {}  # LeanArchitect: a node's label -> the file of its TeX
        self.lean_modules: dict[str, tuple[str, list[tuple[int, str]]]] = {}  # a module -> its file and lines
        self.files: list[str] = []
        self.parts: list[str] = []
        self.starts: list[int] = []
        self.origins: list[Where] = []
        self.missing: list[str] = []  # each \input or \include that names no file, with its place
        self.size = 0
        if self.resolve(entry) is None:
            raise FileNotFoundError(f"no blueprint entry file {entry} in {root}")
        self.visit(entry, 0)
        self.text = "".join(self.parts)

    def resolve(self, name: str) -> str | None:
        """The file *name* names, as a path under root; LeanArchitect's output, wherever the
        build put it, is read from the copy in architect and named under leanarchitect/."""
        base, prefix = self.root, ""
        lake = ARCHITECT_PATH.search(name)
        if lake:
            base, prefix, name = self.architect, f"{ARCHITECT}/", lake.group(1)
        for candidate in (name, f"{name}.tex"):
            path = (base / candidate).resolve()
            if path.is_file() and path.is_relative_to(base.resolve()):
                return prefix + path.relative_to(base.resolve()).as_posix()
        return None

    def path(self, rel: str) -> Path:
        """Where the file that resolve() named *rel* is."""
        if rel.startswith(f"{ARCHITECT}/"):
            return self.architect / rel.removeprefix(f"{ARCHITECT}/")
        return self.root / rel

    def visit(self, name: str, depth: int, origin: str = "") -> None:
        rel = self.resolve(name)
        if rel is None and name.endswith(NOT_TEX):
            self.missing.append(f"{origin}: \\input{{{name}}} holds no blueprint text; skipped")
            return
        if rel is None or depth > 16:
            self.missing.append(f"{origin}: \\input{{{name}}} names no file" if rel is None
                                else f"{origin}: \\input{{{name}}} nests too deep")
            return
        if rel not in self.files:
            self.files.append(rel)
        text = self.path(rel).read_text(encoding="utf-8")
        if rel.startswith(f"{ARCHITECT}/") and "\\newleanmodule" in text:
            self.define(rel, text)
            return
        self.emit(rel, list(enumerate(text.split("\n"), 1)), depth)

    def emit(self, rel: str, lines: list[tuple[int, str]], depth: int) -> None:
        """Add *lines* of file *rel*: comments out and inputs expanded, except inside verbatim
        environments, which keep every character."""
        verbatim = None
        for number, raw in lines:
            if verbatim:
                close = re.search(r"\\end\s*\{" + re.escape(verbatim) + r"\}", raw)
                if not close:
                    self.add(raw, rel, number, newline=True)
                    continue
                self.add(raw[: close.start()], rel, number, newline=False)
                raw, verbatim = raw[close.start() :], None
            while True:
                code = strip_comment(raw)
                opening = VERBATIM.search(code)
                head = code[: opening.end()] if opening else code
                position = 0
                for match in INPUT.finditer(head):
                    self.add(head[position : match.start()], rel, number, newline=False)
                    self.expand(match.group(1), match.group(2).strip(), f"{rel}:{number}", depth)
                    position = match.end()
                if not opening:
                    self.add(head[position:], rel, number, newline=True)
                    break
                self.add(head[position:], rel, number, newline=False)
                rest = raw[opening.end() :]
                close = re.search(r"\\end\s*\{" + re.escape(opening.group(1)) + r"\}", rest)
                if not close:
                    self.add(rest, rel, number, newline=True)
                    verbatim = opening.group(1)
                    break
                self.add(rest[: close.start()], rel, number, newline=False)
                raw = rest[close.start() :]

    def expand(self, command: str, name: str, origin: str, depth: int) -> None:
        """Put in what \\input, \\include, \\inputleanmodule or \\inputleannode names."""
        if command == "inputleanmodule":
            if name in self.lean_modules and depth < 16:
                self.emit(*self.lean_modules[name], depth + 1)
            else:
                self.missing.append(f"{origin}: \\inputleanmodule{{{name}}} names no module")
        elif command == "inputleannode":
            if name in self.lean_nodes:
                self.visit(self.lean_nodes[name], depth + 1, origin)
            else:
                self.missing.append(f"{origin}: \\inputleannode{{{name}}} names no node")
        else:
            self.visit(name, depth + 1, origin)

    def define(self, rel: str, text: str) -> None:
        """Record what a LeanArchitect module file defines: each node's file, and the module's
        content, which \\inputleanmodule places."""
        code = "\n".join(strip_comment(line) for line in text.split("\n"))
        for match in re.finditer(r"\\newleannode\s*\{([^}]*)\}\s*\{\s*\\input\s*\{([^}]*)\}\s*\}", code):
            self.lean_nodes[match.group(1).strip()] = match.group(2).strip()
        for match in re.finditer(r"\\newleanmodule\s*\{([^}]*)\}\s*(?=\{)", code):
            end = group_end(code, match.end())
            first = code.count("\n", 0, match.end()) + 1
            body = code[match.end() + 1 : end - 1]
            self.lean_modules[match.group(1).strip()] = (rel, list(enumerate(body.split("\n"), first)))

    def add(self, text: str, file: str, line: int, newline: bool) -> None:
        self.starts.append(self.size)
        self.origins.append(Where(file, line))
        text = text + ("\n" if newline else "")
        self.parts.append(text)
        self.size += len(text)

    def where(self, offset: int) -> Where:
        return self.origins[max(0, bisect.bisect_right(self.starts, offset) - 1)]


def theorem_kinds(text: str) -> dict[str, str]:
    """Each environment that \\newtheorem declares, with its printed name."""
    captions: dict[str, str] = {}
    for match in re.finditer(r"\\newtheorem(\*?)\s*\{([^}]+)\}", text):
        i = match.end()
        opt = optional(text, i)
        i = opt[1] if opt else i
        caption = argument(text, i)
        captions[match.group(2).strip()] = caption[0].strip() if caption else match.group(2).strip().capitalize()
    return captions


def package_thms(text: str) -> tuple[str, ...]:
    match = re.search(r"\\usepackage\s*\[([^\]]*)\]\s*\{blueprint\}", text)
    if match:
        for option in match.group(1).split(","):
            key, _, value = option.partition("=")
            if key.strip() == "thms" and value.strip():
                return tuple(kind.strip() for kind in value.split("+") if kind.strip())
    return DEFAULT_THMS


def masked(body: str) -> str:
    """body with its formulas blanked out, so a \\label found in what is left is not an equation's."""
    return MATH.sub(lambda match: " " * len(match.group()), body)


def macro_args(body: str, name: str) -> list[str]:
    values = []
    for match in re.finditer(r"\\" + name + r"(?![A-Za-z])", body):
        arg = argument(body, match.end())
        if arg and body[skip_space(body, match.end()) : skip_space(body, match.end()) + 1] == "{":
            values.append(arg[0])
    return values


def floats_in(text: str) -> list[tuple[str, str]]:
    """The labels of the figures and tables in text, with which each is."""
    found = []
    for match in re.finditer(r"\\begin\s*\{(" + "|".join(re.escape(env) for env in FLOATS) + r")\}", text):
        body_end, _ = environment_end(text, match.end(), match.group(1))
        for label in macro_args(text[match.end() : body_end], "label"):
            found.append((squeeze(label), FLOATS[match.group(1)].lower()))
    return found


def flag(body: str, name: str) -> bool:
    return re.search(r"\\" + name + r"(?![A-Za-z])", body) is not None


def read(root: Path, entry: str, architect: Path | None = None) -> Blueprint:
    """The blueprint whose web entry file is root/entry. *architect* is LeanArchitect's
    output directory, when it is not the copy in root/leanarchitect."""
    document = Document(root, entry, architect)
    text = document.text
    problems: list[str] = list(document.missing)
    begin = re.search(r"\\begin\s*\{document\}", text)
    body_start = begin.end() if begin else 0
    captions = theorem_kinds(text[:body_start] or text)
    thms = package_thms(text[:body_start] or text)
    macros = definitions(text)
    links = {}
    for key in ("home", "github", "dochome"):
        value = macro_args(text[:body_start] or text, key)
        if value:
            links[key] = value[-1].strip().rstrip("/")

    # Sectioning units.
    units: list[Unit] = []
    unit_at: list[tuple[int, Unit]] = []
    headings: list[tuple[int, int]] = []  # where each unit's heading, with its \label, starts and ends
    stack: list[Unit] = []
    for match in SECTION.finditer(text, body_start):
        level = SECTIONING.index(match.group(1))
        i = match.end()
        short = optional(text, i)
        i = short[1] if short else i
        title = argument(text, i)
        if not title:
            continue
        while stack and stack[-1].level >= level:
            stack.pop()
        unit = Unit(level, title[0], document.where(match.start()), parent=stack[-1] if stack else None,
                    offset=match.start())
        after = text[title[1] : title[1] + 400]
        label = re.match(r"\s*\\label\s*\{([^}]*)\}", after)
        if label:
            unit.label = squeeze(label.group(1))
        stack.append(unit)
        units.append(unit)
        unit_at.append((title[1], unit))
        headings.append((match.start(), title[1] + (label.end() if label else 0)))
    offsets = [offset for offset, _ in unit_at]

    def unit_of(offset: int) -> Unit | None:
        k = bisect.bisect_right(offsets, offset) - 1
        return unit_at[k][1] if k >= 0 else None

    # Theorem-like environments and proofs, in document order.
    kinds = set(captions) | set(thms)
    pattern = re.compile(r"\\begin\s*\{(" + "|".join(re.escape(kind) for kind in sorted(kinds | {"proof"})) + r")\}")
    blocks = []
    for match in pattern.finditer(text, body_start):
        env = match.group(1)
        body_end, end = environment_end(text, match.end(), env)
        body = text[match.end() : body_end]
        title = None
        stripped = len(body) - len(body.lstrip())
        if body[stripped : stripped + 1] == "[":
            close = bracket_end(body, stripped)
            title, body = body[stripped + 1 : close - 1], body[close:]
        blocks.append((match.start(), end, env, title, body))

    # Each block's innermost enclosing block, if any. A proof inside another block with no
    # theorem-like environment before it there is part of that block's text.
    enclosing: list[int | None] = []
    open_blocks: list[int] = []
    for k, (start, end, *_) in enumerate(blocks):
        while open_blocks and blocks[open_blocks[-1]][1] <= start:
            open_blocks.pop()
        enclosing.append(open_blocks[-1] if open_blocks else None)
        open_blocks.append(k)
    absorbed = {
        k for k, block in enumerate(blocks)
        if block[2] == "proof" and enclosing[k] is not None
        and not any(enclosing[j] == enclosing[k] and blocks[j][2] != "proof" for j in range(enclosing[k] + 1, k))
    }
    inner = [k for k in range(len(blocks)) if enclosing[k] is not None and k not in absorbed]

    def holder(j: int) -> int | None:
        """The block whose text holds block j: the one enclosing it, past any absorbed proof."""
        k = enclosing[j]
        while k in absorbed:
            k = enclosing[k]
        return k

    def own(k: int, body: str, pointer: bool = False) -> str:
        """Block k's body without the blocks nested in it that stand on their own: blanked, or
        with *pointer* a marker where each theorem-like one was, for a reference to it."""
        result = body
        for j in inner:
            if holder(j) == k:
                nested = text[blocks[j][0] : blocks[j][1]]
                stand_in = " " * len(nested) if not pointer else ("" if blocks[j][2] == "proof" else f"\x00{j}\x00")
                result = result.replace(nested, stand_in, 1)
        return result

    nodes: list[Node] = []
    node_of: dict[int, Node] = {}
    shown: list[tuple[Node | Proof, int]] = []  # texts whose markers name nested nodes
    labels: dict[str, object] = {}
    last: tuple[Node, Unit | None] | None = None  # the last outermost theorem-like environment, and its unit
    for k, (start, end, env, title, body) in enumerate(blocks):
        if k in absorbed:
            continue
        unit = unit_of(start)
        mine = own(k, body)
        float_labels = floats_in(mine)
        plain = masked(mine)
        own_labels = [squeeze(label) for label in macro_args(plain, "label")
                      if squeeze(label) not in {label for label, _ in float_labels}]
        equations = [squeeze(label) for label in macro_args(mine, "label")
                     if squeeze(label) not in own_labels and squeeze(label) not in {label for label, _ in float_labels}]
        lean = names(macro_args(mine, "lean")[-1]) if macro_args(mine, "lean") else []
        uses = names(macro_args(mine, "uses")[-1]) if macro_args(mine, "uses") else []
        where = document.where(start)
        if env == "proof":
            proof = Proof(own(k, body, pointer=True), flag(mine, "leanok") or flag(mine, "mathlibok"), uses,
                          own_labels, where, title, start, unit)
            target = None
            proves = macro_args(mine, "proves")
            if proves:
                target = labels.get(squeeze(proves[-1]))
                if not isinstance(target, Node):
                    problems.append(f"{where.file}:{where.line}: \\proves{{{squeeze(proves[-1])}}} names no theorem")
                    target = None
            if target is None and enclosing[k] is not None:
                siblings = [j for j in range(enclosing[k] + 1, k) if enclosing[j] == enclosing[k] and j in node_of]
                target = node_of[siblings[-1]] if siblings else None
            elif target is None and last is not None and last[1] is unit:
                target = last[0]
            if target is None:
                problems.append(f"{where.file}:{where.line}: a proof with no theorem before it")
                continue
            target.proof = proof
            shown.append((proof, k))
            for label in own_labels:
                labels[label] = target
                target.labels.append(label)
            for label in equations:
                labels.setdefault(label, ("equation", target))
                if label not in target.equations:
                    target.equations.append(label)
            for label, kind in float_labels:
                labels.setdefault(label, (kind, target))
                target.floats.append((label, kind))
            continue
        node = Node(
            env=env,
            title=title,
            body=own(k, body, pointer=True),
            labels=own_labels,
            lean=lean,
            leanok=flag(mine, "leanok") or flag(mine, "mathlibok"),
            mathlibok=flag(mine, "mathlibok"),
            notready=flag(mine, "notready"),
            discussion=(macro_args(mine, "discussion") or [None])[-1],
            uses=uses,
            where=where,
            unit=unit,
            graph=env in thms,
            equations=equations,
            offset=start,
            end=end,
            floats=float_labels,
        )
        for label in own_labels:
            labels[label] = node
        for label in equations:
            labels.setdefault(label, ("equation", node))
        for label, kind in float_labels:
            labels.setdefault(label, (kind, node))
        nodes.append(node)
        node_of[k] = node
        shown.append((node, k))
        if enclosing[k] is None:
            last = (node, unit)
    for unit in units:
        if unit.label:
            labels.setdefault(unit.label, unit)

    # Ids: the last label, or for an unlabelled node one made from its unit and place.
    taken = set(labels)
    counters: dict[str, int] = {}
    for node in nodes:
        if node.labels:
            node.id = node.labels[-1]
            continue
        base = f"{node.env}-{(node.where.file.rsplit('/', 1)[-1]).removesuffix('.tex')}"
        counters[base] = counters.get(base, 0) + 1
        node.id = f"{base}-{counters[base]}"
        while node.id in taken:
            counters[base] += 1
            node.id = f"{base}-{counters[base]}"
        taken.add(node.id)
        labels[node.id] = node
    # A node stated inside another's text stands on its own; that text refers to it there.
    for item, _ in shown:
        item.body = re.sub("\x00(\\d+)\x00", lambda marker: f" (\\cref{{{node_of[int(marker.group(1))].id}}}) ",
                           item.body)

    # Prose: the runs of text between headings and the outermost environments, up to
    # \end{document}. A list that an environment interrupts goes on after it.
    end_document = re.search(r"\\end\s*\{document\}", text)
    stop = end_document.start() if end_document else len(text)
    heading_starts = {start for start, _ in headings}
    events = sorted([(body_start, body_start), *headings,
                     *[(start, end) for k, (start, end, *_) in enumerate(blocks) if enclosing[k] is None]])
    prose: list[Prose] = []
    open_lists: list[str] = []
    for k, (start, end) in enumerate(events):
        if start in heading_starts:
            open_lists = []
        following = min(events[k + 1][0] if k + 1 < len(events) else stop, stop)
        run = text[end:following]
        reopened = "".join(f"\\begin{{{env}}}" for env in open_lists)
        for match in re.finditer(r"\\(begin|end)\s*\{(" + "|".join(LISTS) + r")\}", run):
            if match.group(1) == "begin":
                open_lists.append(match.group(2))
            elif open_lists:
                open_lists.pop()
        if not run.strip() or end >= stop:
            continue
        offset = end + len(run) - len(run.lstrip())
        float_labels = floats_in(run)
        equations = [squeeze(label) for label in macro_args(run, "label")
                     if squeeze(label) not in {squeeze(other) for other in macro_args(masked(run), "label")}]
        prose.append(Prose(reopened + run.strip(), document.where(offset), unit_of(offset), offset, equations,
                           float_labels))
        for label in equations:
            labels.setdefault(label, ("equation", prose[-1]))
        for label, kind in float_labels:
            labels.setdefault(label, (kind, prose[-1]))

    # Bibliographies: each .bib that \bibliography or \addbibresource names.
    bibliography: list[str] = []
    for match in re.finditer(r"\\(?:bibliography|addbibresource)\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}", text):
        for name in names(match.group(1)):
            found = document.resolve(name if name.endswith(".bib") else f"{name}.bib")
            if found is None:
                problems.append(f"{document.where(match.start()).file}:{document.where(match.start()).line}: "
                                f"\\bibliography{{{name}}} names no file")
            elif found not in bibliography:
                bibliography.append(found)

    for node in nodes:
        for label in node.uses + node.proof_uses:
            if label not in labels:
                problems.append(f"{node.where.file}:{node.where.line}: \\uses{{{label}}} names no label")
    return Blueprint(document.files, macros, captions, thms, units, nodes, labels, links, problems, prose, bibliography)
