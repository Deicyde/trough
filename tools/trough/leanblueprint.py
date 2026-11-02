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
"""

from __future__ import annotations

import bisect
import re
from dataclasses import dataclass, field
from pathlib import Path

from trough.tex import (
    CONTROL,
    argument,
    bracket_end,
    definitions,
    environment_end,
    names,
    optional,
    skip_space,
    strip_comment,
)

DEFAULT_THMS = ("definition", "lemma", "proposition", "theorem", "corollary")
SECTIONING = ("part", "chapter", "section", "subsection", "subsubsection")
INPUT = re.compile(r"\\(?:input|include)\s*\{([^}]*)\}")
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


@dataclass(eq=False)
class Unit:
    """A chapter, section or smaller sectioning unit."""

    level: int  # index into SECTIONING
    title: str
    where: Where
    label: str | None = None
    prose: str = ""
    parent: Unit | None = None


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
    labels: dict[str, object]  # label -> Node, Unit, or ("equation", Node)
    links: dict[str, str]  # home, github, dochome
    problems: list[str]

    @property
    def graph(self) -> list[Node]:
        return [node for node in self.nodes if node.graph]


class Document:
    """A blueprint's TeX with \\input expanded and comments removed, and where each line is from."""

    def __init__(self, root: Path, entry: str):
        self.root = root
        self.files: list[str] = []
        self.parts: list[str] = []
        self.starts: list[int] = []
        self.origins: list[Where] = []
        self.size = 0
        self.visit(entry, 0)
        self.text = "".join(self.parts)

    def resolve(self, name: str) -> str | None:
        for candidate in (name, f"{name}.tex"):
            path = (self.root / candidate).resolve()
            if path.is_file() and path.is_relative_to(self.root.resolve()):
                return path.relative_to(self.root.resolve()).as_posix()
        return None

    def visit(self, name: str, depth: int) -> None:
        rel = self.resolve(name)
        if rel is None or depth > 16:
            return
        if rel not in self.files:
            self.files.append(rel)
        for number, raw in enumerate((self.root / rel).read_text(encoding="utf-8").split("\n"), 1):
            code = strip_comment(raw)
            position = 0
            for match in INPUT.finditer(code):
                self.add(code[position : match.start()], rel, number, newline=False)
                self.visit(match.group(1).strip(), depth + 1)
                position = match.end()
            self.add(code[position:], rel, number, newline=True)

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


def flag(body: str, name: str) -> bool:
    return re.search(r"\\" + name + r"(?![A-Za-z])", body) is not None


def read(root: Path, entry: str) -> Blueprint:
    """The blueprint whose web entry file is root/entry."""
    document = Document(root, entry)
    text = document.text
    problems: list[str] = []
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
        unit = Unit(level, title[0], document.where(match.start()), parent=stack[-1] if stack else None)
        after = text[title[1] : title[1] + 400]
        label = re.match(r"\s*\\label\s*\{([^}]*)\}", after)
        if label:
            unit.label = label.group(1).strip()
        stack.append(unit)
        units.append(unit)
        unit_at.append((title[1], unit))
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
        if env != "proof":
            stripped = len(body) - len(body.lstrip())
            if body[stripped : stripped + 1] == "[":
                close = bracket_end(body, stripped)
                title, body = body[stripped + 1 : close - 1], body[close:]
        else:
            opt = optional(body, 0)
            body = body[opt[1]:] if opt and body.lstrip().startswith("[") else body
        blocks.append((match.start(), end, env, title, body))

    def own(start: int, end: int, body: str) -> str:
        """The body without the environments nested inside it."""
        result = body
        for s, e, *_ in blocks:
            if start < s and e <= end:
                nested = text[s:e]
                result = result.replace(nested, " " * len(nested), 1)
        return result

    nodes: list[Node] = []
    labels: dict[str, object] = {}
    last: Node | None = None
    last_unit: Unit | None = None
    for start, end, env, title, body in blocks:
        unit = unit_of(start)
        mine = own(start, end, body)
        plain = masked(mine)
        own_labels = [label.strip() for label in macro_args(plain, "label")]
        equations = [label.strip() for label in macro_args(mine, "label") if label.strip() not in own_labels]
        lean = names(macro_args(mine, "lean")[-1]) if macro_args(mine, "lean") else []
        uses = names(macro_args(mine, "uses")[-1]) if macro_args(mine, "uses") else []
        where = document.where(start)
        if env == "proof":
            proof = Proof(body, flag(mine, "leanok"), uses, own_labels, where)
            target = None
            proves = macro_args(mine, "proves")
            if proves:
                target = labels.get(proves[-1].strip())
                if not isinstance(target, Node):
                    problems.append(f"{where.file}:{where.line}: \\proves{{{proves[-1].strip()}}} names no theorem")
                    target = None
            if target is None and last is not None and last_unit is unit:
                target = last
            if target is None:
                problems.append(f"{where.file}:{where.line}: a proof with no theorem before it")
                continue
            target.proof = proof
            for label in own_labels:
                labels[label] = target
                target.labels.append(label)
            for label in equations:
                labels.setdefault(label, ("equation", target))
            continue
        node = Node(
            env=env,
            title=title,
            body=body,
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
        )
        for label in own_labels:
            labels[label] = node
        for label in equations:
            labels.setdefault(label, ("equation", node))
        nodes.append(node)
        last, last_unit = node, unit
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

    # Prose: what a unit says before its first environment or subunit.
    starts = sorted([start for start, *_ in blocks] + [m.start() for m in SECTION.finditer(text, body_start)])
    for offset, unit in unit_at:
        k = bisect.bisect_right(starts, offset)
        stop = starts[k] if k < len(starts) else len(text)
        end_document = re.search(r"\\end\s*\{document\}", text[offset:stop])
        stop = offset + end_document.start() if end_document else stop
        prose = text[offset:stop]
        prose = re.sub(r"^\s*\\label\s*\{[^}]*\}", "", prose)
        unit.prose = prose.strip()

    for node in nodes:
        for label in node.uses + node.proof_uses:
            if label not in labels:
                problems.append(f"{node.where.file}:{node.where.line}: \\uses{{{label}}} names no label")
    return Blueprint(document.files, macros, captions, thms, units, nodes, labels, links, problems)
