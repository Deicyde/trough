"""Chapters for the libraries mapped from their leanblueprints: one article per node.

Each library's chapter follows its blueprint's chapters and sections. A node
becomes an article whose status follows the blueprint's marks: \\leanok on a
statement or a proof makes it formalized, \\mathlibok puts it in Mathlib, and
\\notready marks it not ready. A Mathlib node whose first Lean name heads an
article of the Mathlib chapter is that article. Dependencies are the \\uses:
a statement's under "Depends on", a proof's under "Proof depends on".

A library's sources live in data/blueprints/<id>/: source.json pins the
commit, and src/ holds the TeX files the blueprint reads. A library whose
text trough may not reproduce has structure.json instead, with what the
refresh read from its TeX: titles, labels, Lean names, marks and places.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, unquote

from trough import bibtex, leanblueprint
from trough.leanblueprint import Blueprint, Node, Prose, Proof, Unit, Where
from trough.tex import Writer, expand
from trough.vault import MATH_SPAN, Container, Entry, Leaf, chunk, rel, slugify, walk

KINDS = {"theorem": "theorem", "lemma": "lemma", "proposition": "proposition", "corollary": "corollary",
         "definition": "definition", "sublemma": "lemma", "conjecture": "theorem", "claim": "lemma"}
LINK = re.compile(r"\]\(trough:([^)\s]*)\)")  # a placeholder's target is percent-encoded
# References that print only a number in LaTeX, so the text before them names the kind.
NUMBER_ONLY = {"ref", "pageref", "vref", "Vref", "labelcref", "cpageref", "Cpageref", "nameref", "hyperref"}
PREFIX = re.compile(r"^[A-Za-z]{1,12}:(?=.)")
STRUCTURE_SCHEMA = "trough-blueprint-structure/v1"


@dataclass
class Project:
    id: str
    name: str
    repo: str
    rev: str
    date: str
    entry: str  # the web entry file, as a path in the repository
    license: str | None
    text: bool  # whether trough may reproduce the blueprint's text
    directory: Path

    @property
    def url(self) -> str:
        return f"https://github.com/{self.repo}"

    @property
    def entry_dir(self) -> str:
        return self.entry.rsplit("/", 1)[0] if "/" in self.entry else ""

    def source_url(self, where: Where) -> str:
        path = f"{self.entry_dir}/{where.file}" if self.entry_dir else where.file
        return f"{self.url}/blob/{self.rev}/{path}#L{where.line}"


def load_projects(data: Path, libraries: list[dict]) -> list[Project]:
    """The blueprint libraries with sources under data/blueprints/, in catalog order."""
    projects = []
    for library in libraries:
        directory = data / "blueprints" / library["id"]
        if not (directory / "source.json").is_file():
            continue
        source = json.loads((directory / "source.json").read_text(encoding="utf-8"))
        projects.append(Project(library["id"], library["name"], source["repo"], source["rev"], source.get("date", ""),
                                source["entry"], source.get("license"), bool(source.get("text", True)), directory))
    return projects


def load_blueprint(project: Project) -> Blueprint:
    if project.text:
        return leanblueprint.read(project.directory / "src", project.entry.rsplit("/", 1)[-1])
    return from_structure(json.loads((project.directory / "structure.json").read_text(encoding="utf-8")))


def structure(blueprint: Blueprint) -> dict:
    """What a blueprint shows without its text: titles, labels, Lean names, marks and places.
    Titles are stored with the project's macros expanded."""
    index = {id(unit): k for k, unit in enumerate(blueprint.units)}

    def title(tex: str | None) -> str | None:
        return expand(tex, dict(blueprint.macros)).strip() if tex else tex

    return {
        "schema": STRUCTURE_SCHEMA,
        "links": blueprint.links,
        "captions": blueprint.captions,
        "thms": list(blueprint.thms),
        "units": [
            {"level": unit.level, "title": title(unit.title), "label": unit.label, "file": unit.where.file,
             "line": unit.where.line, "parent": index[id(unit.parent)] if unit.parent else None,
             "offset": unit.offset}
            for unit in blueprint.units
        ],
        "nodes": [
            {"id": node.id, "env": node.env, "title": title(node.title), "labels": node.labels, "lean": node.lean,
             "leanok": node.leanok, "mathlibok": node.mathlibok, "notready": node.notready,
             "discussion": node.discussion, "uses": node.uses, "file": node.where.file, "line": node.where.line,
             "unit": index[id(node.unit)] if node.unit else None, "graph": node.graph, "equations": node.equations,
             "offset": node.offset,
             "proof": None if node.proof is None else {
                 "leanok": node.proof.leanok, "uses": node.proof.uses, "labels": node.proof.labels,
                 "file": node.proof.where.file, "line": node.proof.where.line}}
            for node in blueprint.nodes
        ],
        "problems": blueprint.problems,
    }


def from_structure(data: dict) -> Blueprint:
    units: list[Unit] = []
    for item in data["units"]:
        parent = units[item["parent"]] if item["parent"] is not None else None
        units.append(Unit(item["level"], item["title"], Where(item["file"], item["line"]), item["label"], parent,
                          item.get("offset", 0)))
    nodes: list[Node] = []
    labels: dict[str, object] = {}
    for item in data["nodes"]:
        proof = item["proof"]
        node = Node(
            env=item["env"], title=item["title"], body="", labels=list(item["labels"]), lean=list(item["lean"]),
            leanok=item["leanok"], mathlibok=item["mathlibok"], notready=item["notready"],
            discussion=item["discussion"], uses=list(item["uses"]), where=Where(item["file"], item["line"]),
            unit=units[item["unit"]] if item["unit"] is not None else None, graph=item["graph"],
            proof=None if proof is None else Proof("", proof["leanok"], list(proof["uses"]), list(proof["labels"]),
                                                   Where(proof["file"], proof["line"])),
            equations=list(item["equations"]), id=item["id"], offset=item.get("offset", 0),
        )
        nodes.append(node)
        for label in node.labels:
            labels[label] = node
        labels.setdefault(node.id, node)
        for label in node.equations:
            labels.setdefault(label, ("equation", node))
    for unit in units:
        if unit.label:
            labels.setdefault(unit.label, unit)
    return Blueprint([], {}, data.get("captions", {}), tuple(data.get("thms", leanblueprint.DEFAULT_THMS)), units,
                     nodes, labels, data.get("links", {}), list(data.get("problems", [])))


def escape(text: str) -> str:
    """Markdown-escape text for a title or a link, leaving its formulas alone."""
    parts = []
    last = 0
    for match in MATH_SPAN.finditer(text):
        parts.append(re.sub(r"([*_\[\]\\`])", r"\\\1", text[last : match.start()]))
        parts.append(match.group())
        last = match.end()
    parts.append(re.sub(r"([*_\[\]\\`])", r"\\\1", text[last:]))
    return "".join(parts)


def short_id(label: str) -> str:
    return PREFIX.sub("", label)


@dataclass
class Built:
    """A built chapter: its root, its articles by label, and what render's Lean rows should link."""

    root: Container
    targets: dict[str, Leaf | Container]
    lean_links: dict[str, str]
    stats: dict[str, int]
    unknown: Counter


def chapter(project: Project, blueprint: Blueprint, mathlib_heads: dict[str, Leaf]) -> Built:
    """The chapter for *project*. *mathlib_heads* maps a Mathlib declaration to the
    Mathlib-chapter article it heads, for nodes in Mathlib.

    Each part, chapter and section with anything in it is a page; smaller units are
    headings on their section's page. A page reads in the blueprint's order: its
    prose, remarks and examples, and each node's card where the node stands. A
    labelled display shows a number, counted on its page, that references print."""
    captions = {**{kind: kind.capitalize() for kind in KINDS}, **blueprint.captions}
    dochome = blueprint.links.get("dochome", "https://leanprover-community.github.io/mathlib4_docs")
    nodes = blueprint.graph
    unit_index = {id(unit): k for k, unit in enumerate(blueprint.units)}
    bib = bibtex.bibliography([project.directory / "src" / name for name in blueprint.bibliography]) if project.text else {}
    stats = Counter(nodes=len(nodes))

    def caption(node: Node) -> str:
        return captions.get(node.env, node.env.capitalize())

    def page_unit(unit: Unit | None) -> Unit | None:
        while unit is not None and unit.level > 2:
            unit = unit.parent
        return unit

    def key(unit: Unit | None) -> str:
        """The target key of the page that shows *unit*."""
        unit = page_unit(unit)
        return "#root" if unit is None else f"#unit-{unit_index[id(unit)]}"

    def placeholder(text: str, target: str) -> str:
        return f"[{escape(text)}](trough:{quote(target, safe='')})"

    def display(node: Node) -> str:
        """How the text refers to a node; an article's own heading drops the caption, which
        AutoformBot prints from its declaration."""
        return writer.plain(node.title) if node.title else f"{caption(node)} {short_id(node.id)}"

    def heading(node: Node) -> str:
        if node.title:
            return writer.plain(node.title)
        if node.labels:
            return short_id(node.id)
        # No label and no title: the made-up id is in no blueprint, so say what the node says.
        words = re.findall(r"\$[^$]*\$|\S+", writer.plain(node.body)) if node.body else []
        if not words:
            return f"{caption(node)} ({node.where.file.rsplit('/', 1)[-1]}, line {node.where.line})"
        cut = 1
        while cut < len(words) and len(" ".join(words[:cut])) < 40:
            cut += 1
        return f"{caption(node)}: {' '.join(words[:cut])}" + ("…" if cut < len(words) else "")

    asides = [node for node in blueprint.nodes if not node.graph] if project.text else []
    events: list[Node | Prose] = sorted([*nodes, *asides, *(blueprint.prose if project.text else [])],
                                        key=lambda event: event.offset)
    shown = {id(unit) for event in events for unit in ancestors(event.unit) if unit.level <= 2}
    numbers: dict[str, tuple[str, str]] = {}  # an equation's label: its number, and the article that shows it
    current = ["#root"]  # the article whose text is being written

    def ref(label: str, command: str) -> str:
        target = blueprint.labels.get(label)
        if isinstance(target, Node):
            text = display(target)
            if command in NUMBER_ONLY:
                text = writer.plain(target.title) if target.title else short_id(target.id)
            return placeholder(text, target.id if target.graph else key(target.unit))
        if isinstance(target, Unit):
            home = page_unit(target)
            title = writer.plain(target.title)
            return placeholder(title, key(target)) if home is None or id(home) in shown else escape(title)
        if isinstance(target, tuple) and label in numbers:
            number, article = numbers[label]
            text = number if command in NUMBER_ONLY else f"({number})"
            return text if article == current[0] else placeholder(text, article)
        stats["unresolved_refs"] += 1
        return f"({escape(label)})" if isinstance(target, tuple) else escape(label)

    writer = Writer(blueprint.macros, ref, bib, tag=lambda label: numbers[label][0] if label in numbers else None)
    leaf_of: dict[Node, Leaf] = {}
    owned: set[Node] = set()
    for node in nodes:
        if node.mathlibok and node.lean and node.lean[0] in mathlib_heads:
            leaf_of[node] = mathlib_heads[node.lean[0]]
            stats["mathlib_shared"] += 1
        else:
            owned.add(node)

    # Equations: numbered on their page in the blueprint's order, before any text refers to one.
    counts: Counter = Counter()
    for event in events if project.text else []:
        if isinstance(event, Node) and event.graph and event not in owned:
            continue
        article = event.id if isinstance(event, Node) and event.graph else key(event.unit)
        for label in event.equations:
            if label not in numbers:
                counts[key(event.unit)] += 1
                numbers[label] = (str(counts[key(event.unit)]), article)
    stats["equations"] = len(numbers)

    lean_links: dict[str, str] = {}
    for node in nodes:
        if node in owned:
            current[0] = node.id
            leaf_of[node] = leaf(project, node, caption(node), heading(node), writer, dochome, blueprint, lean_links,
                                 stats)

    # Dependencies: a node's \uses that name nodes, a proof's apart from its statement's.
    for node in nodes:
        if node not in owned:
            continue
        mine = leaf_of[node]
        statement = unique(leaf_of[target] for target in targets_of(node.uses, blueprint) if target is not node)
        proof = unique(leaf_of[target] for target in targets_of(node.proof_uses, blueprint) if target is not node)
        mine.depends = statement
        mine.proof_depends = [item for item in proof if item not in statement]
        stats["statement_edges"] += len(mine.depends)
        stats["proof_edges"] += len(mine.proof_depends)
    stats["informal"] = break_cycles([leaf_of[node] for node in nodes if node in owned])
    stats["unresolved"] = sum(1 for node in nodes for label in node.uses + node.proof_uses if label not in blueprint.labels)

    # Pages, filled in the blueprint's order.
    root = Container(project.name, project.id, prose=intro(project, blueprint, stats))
    targets: dict[str, Leaf | Container] = {"#root": root}
    pages: dict[int, Container] = {}
    pending: dict[int, list[str]] = {}  # text waiting for the next line of a page's listing
    opened: dict[int, list[Unit]] = {}  # the units whose headings a page has shown last

    def page(unit: Unit | None) -> Container:
        unit = page_unit(unit)
        if unit is None:
            return root
        if id(unit) not in pages:
            parent = page(unit.parent)
            title = writer.plain(unit.title) or "Untitled"
            pages[id(unit)] = Container(title, slugify(title))
            add(parent, Entry(pages[id(unit)]))
            targets[key(unit)] = pages[id(unit)]
        return pages[id(unit)]

    def add(container: Container, entry: Entry) -> None:
        entry.before = "\n\n".join(pending.pop(id(container), []))
        container.entries.append(entry)

    def write(container: Container, markdown: str) -> None:
        if container.entries:
            pending.setdefault(id(container), []).append(markdown)
        else:
            container.prose = f"{container.prose}\n\n{markdown}".strip()

    def open_headings(home: Container, unit: Unit | None) -> None:
        """Show the headings of the units below *home*'s that *unit* is in, unless shown last."""
        chain = [sub for sub in ancestors(unit) if sub.level > 2][::-1]
        base = page_unit(unit).level if page_unit(unit) is not None else 2
        last = opened.get(id(home), [])
        common = 0
        while common < min(len(chain), len(last)) and chain[common] is last[common]:
            common += 1
        for sub in chain[common:]:
            write(home, f"{'#' * min(6, sub.level - base + 1)} {escape(writer.plain(sub.title) or 'Untitled')}")
        opened[id(home)] = chain

    for event in events:
        home = page(event.unit)
        if isinstance(event, Node) and event.graph:
            open_headings(home, event.unit)
            add(home, Entry(leaf_of[event], event in owned))
            continue
        current[0] = key(event.unit)
        markdown = writer.statement(event.text) if isinstance(event, Prose) else aside(event, caption(event), writer)
        if markdown:
            open_headings(home, event.unit)
            write(home, markdown)
            stats["prose" if isinstance(event, Prose) else "asides"] += 1
    for container in [root, *pages.values()]:
        container.tail = "\n\n".join(pending.pop(id(container), []))
    for node in nodes:
        for label in [node.id, *node.labels]:
            targets[label] = leaf_of[node]
    for container in [*pages.values(), root]:
        chunk(container)
    stats["containers"] = len(pages)
    stats["problems"] = len(blueprint.problems)
    return Built(root, targets, lean_links, dict(stats), writer.unknown)


def ancestors(unit: Unit | None):
    """*unit* and the units it is in, innermost first."""
    while unit is not None:
        yield unit
        unit = unit.parent


def aside(node: Node, caption: str, writer: Writer) -> str:
    """A remark, example or other theorem-like text that is no node, as its page shows it."""
    title = f" ({escape(writer.plain(node.title))})" if node.title else ""
    text = run_in(f"**{caption}{title}.**", writer.statement(node.body))
    if node.proof is not None:
        text += "\n\n" + run_in("*Proof.*", writer.statement(node.proof.body))
    return text


def run_in(head: str, body: str) -> str:
    """*head* starting the first paragraph of *body*, or above it when *body* opens with a
    display, a list or a quote."""
    if not body:
        return head
    if re.match(r"\$\$|[-+*>] |\d+\. |\*\(", body):
        return f"{head}\n\n{body}"
    return f"{head} {body}"


def leaf(project: Project, node: Node, caption: str, title: str, writer: Writer, dochome: str,
         blueprint: Blueprint, lean_links: dict[str, str], stats: Counter) -> Leaf:
    kind = KINDS.get(node.env, node.env)
    fields = [("declaration", kind), ("origin", "cited")]
    notes: list[tuple[str, str]] = []
    lean_lines = [f"[`{name}`]({dochome}/find/#doc/{name})" for name in node.lean]
    statement_ok = node.leanok or bool(node.proof and node.proof.leanok)
    proof_ok = bool(node.proof and node.proof.leanok)
    if node.mathlibok and node.lean:
        fields += [("mathlib", "true"), ("mathlib_declaration", ", ".join(node.lean))]
        stats["mathlib"] += 1
    elif node.mathlibok:
        notes.append(("Lean", "The blueprint marks this as in Mathlib but names no declaration."))
        stats["mathlib_without_name"] += 1
    elif statement_ok and node.lean:
        fields += [("lean", ", ".join(node.lean)), ("statement", "formalized")]
        if proof_ok:
            fields.append(("proof", "formalized"))
            stats["proofs_formalized"] += 1
        stats["statements_formalized"] += 1
        for name in node.lean:
            lean_links[name] = f"{dochome}/find/#doc/{name}"
    elif statement_ok:
        notes.append(("Lean", "The blueprint marks this formalized but names no Lean declaration."))
        stats["formalized_without_name"] += 1
    if node.notready and not statement_ok:
        fields.append(("not_ready", "true"))
    if node.discussion and blueprint.links.get("github"):
        fields.append(("discussion", f"{blueprint.links['github']}/issues/{node.discussion.strip().lstrip('#')}"))
    if lean_lines and not any(heading == "Lean" for heading, _ in notes):
        lead = "Formalized as" if statement_ok else "The blueprint names"
        notes.append(("Lean", f"{lead} " + ", ".join(lean_lines) + "."))
    source = project.source_url(node.where)
    if project.text:
        body = writer.statement(node.body) or f"A {caption.lower()} of the blueprint of {project.name}, with no text."
        if node.proof is not None:
            proof = writer.statement(node.proof.body)
            if proof:
                notes.insert(0, ("Proof", proof))
    else:
        body = (f"The blueprint of {project.name} states this {caption.lower()} at "
                f"[{node.where.file}, line {node.where.line}]({source}). The project gives no license, so trough "
                "does not reproduce its text.")
    leaf_ = Leaf(escape(title), slugify(node.id), fields, body, notes=notes)
    leaf_.sources = [(f"{project.name} blueprint: {node.where.file}, line {node.where.line}", source)]
    leaf_.no_depends = "Its statement uses no other node of the blueprint."
    return leaf_


def targets_of(labels: list[str], blueprint: Blueprint) -> list[Node]:
    out = []
    for label in labels:
        target = blueprint.labels.get(label)
        if isinstance(target, Node) and target.graph:
            out.append(target)
    return out


def unique(items) -> list:
    return list(dict.fromkeys(items))


def break_cycles(leaves: list[Leaf]) -> int:
    """Move each dependency that closes a cycle to "Informally uses"; return how many moved."""
    state: dict[int, int] = {}
    moved = 0
    for root in leaves:
        if id(root) in state:
            continue
        state[id(root)] = 1
        stack = [(root, iter(root.depends + root.proof_depends))]
        while stack:
            node, children = stack[-1]
            child = next(children, None)
            if child is None:
                state[id(node)] = 2
                stack.pop()
                continue
            if state.get(id(child)) == 1:
                for edges in (node.depends, node.proof_depends):
                    if child in edges:
                        edges.remove(child)
                node.informal.append(child)
                moved += 1
            elif id(child) not in state:
                state[id(child)] = 1
                stack.append((child, iter(child.depends + child.proof_depends)))
    return moved


def intro(project: Project, blueprint: Blueprint, stats: Counter) -> str:
    rev = f"[{project.rev[:8]}]({project.url}/tree/{project.rev})"
    date = f" ({project.date[:10]})" if project.date else ""
    nodes = stats["nodes"]
    lines = [
        f"The blueprint of {project.name}, read at commit {rev}{date}: {nodes:,} nodes, one article each. A node the "
        "blueprint marks `\\leanok` is formalized here, its proof too when that is marked, and `\\mathlibok` "
        "puts it in Mathlib. Dependencies are the blueprint's `\\uses`: a statement's under *Depends on*, a "
        "proof's under *Proof depends on*.",
    ]
    if project.text:
        lines.append(
            f"The text is the blueprint's, under its {project.license} license: each page has a section's prose, "
            "remarks and examples in the blueprint's order, with each node's statement and proof where the node "
            "stands."
        )
    else:
        lines.append(
            "The project gives no license, so this chapter has each node's title, Lean names, marks and "
            "dependencies, and links to its text in the blueprint, but not the text."
        )
    return "\n\n".join(lines)


def resolve(built: Built, vault: Path) -> None:
    """Point the chapter's text links at the articles they name, once paths are assigned."""

    def fix(text: str, here: Path) -> str:
        def link(match: re.Match) -> str:
            target = built.targets[unquote(match.group(1))]
            return f"]({rel(here, target.path.relative_to(vault))})"

        return LINK.sub(link, text)

    for node in walk(built.root):
        here = node.path.relative_to(vault)
        if isinstance(node, Container):
            node.prose = fix(node.prose, here)
            node.tail = fix(node.tail, here)
            for entry in node.entries:
                entry.before = fix(entry.before, here)
        else:
            node.body = fix(node.body, here)
            node.notes = [(heading, fix(text, here)) for heading, text in node.notes]
