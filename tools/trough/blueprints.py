"""Chapters for the libraries mapped from their leanblueprints: one article per node in Lean.

Each library's chapter follows its blueprint's chapters and sections. A node
whose Lean declarations the blueprint names becomes an article when \\leanok on
its statement or proof makes it formalized or \\mathlibok puts it in Mathlib;
any other node only plans a declaration and has none. A Mathlib node whose
first Lean name heads an article of the Mathlib chapter is that article.
Dependencies are the \\uses: a statement's under "Depends on", a proof's
under "Proof depends on".

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
from trough.tex import Writer, cited, expand
from trough.vault import MATH_SPAN, Container, Entry, Leaf, chunk, rel, slugify, walk

KINDS = {"theorem": "theorem", "lemma": "lemma", "proposition": "proposition", "corollary": "corollary",
         "definition": "definition", "sublemma": "lemma", "conjecture": "theorem", "claim": "lemma"}
LINK = re.compile(r"\]\(trough:([^)\s]*)\)")  # a placeholder's target is percent-encoded
# References that print only a number in LaTeX, so the text before them names the kind.
NUMBER_ONLY = {"ref", "pageref", "vref", "Vref", "labelcref", "cpageref", "Cpageref", "nameref", "hyperref"}
PREFIX = re.compile(r"^[A-Za-z]{1,12}:(?=.)")
STRUCTURE_SCHEMA = "trough-blueprint-structure/v1"
# A LeanArchitect file: module/A/B.tex for module A.B, or a node's module/A/B.artifacts/<label>.tex.
ARCHITECT_MODULE = re.compile(rf"^{leanblueprint.ARCHITECT}/module/(.+?)(?:\.artifacts/.*|\.tex)$")


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

    def source(self, where: Where) -> tuple[str, str]:
        """Where the text at *where* comes from in the repository: a label and a link. TeX that
        LeanArchitect wrote comes from the attributes in a Lean module, so that file is named."""
        module = ARCHITECT_MODULE.match(where.file)
        if module:
            return f"{module.group(1)}.lean", f"{self.url}/blob/{self.rev}/{module.group(1)}.lean"
        path = f"{self.entry_dir}/{where.file}" if self.entry_dir else where.file
        return f"{where.file}, line {where.line}", f"{self.url}/blob/{self.rev}/{path}#L{where.line}"


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


@dataclass
class Event:
    """Something a page shows, at its place in the document."""

    offset: int
    kind: str  # "card", "aside", "aside proof", "proof pointer" or "prose"
    item: Node | Prose
    unit: Unit | None


def in_lean(node: Node) -> bool:
    """Whether the blueprint names the node's Lean declarations and marks them formalized, the
    statement at least, or in Mathlib. The map records what the project contains, not what it
    plans, so any other node has no article: AutoformBot could only show it as work to do."""
    return bool(node.lean) and (node.leanok or node.mathlibok or bool(node.proof and node.proof.leanok))


# The last sentence of a paragraph that leads into what follows: it ends in a colon or "the
# following", or stops at a word or comma.
LEAD_IN = re.compile(r"(?:^|(?<=[.!?])\s+)(?=[^.!?]*[.!?]?\s*\Z)(?:[^\n]*:|[^\n]*\b(?:the following|as follows)\.|[^\n]*[A-Za-z0-9,])\s*\Z")


def without_lead_in(markdown: str) -> str:
    """*markdown* without its closing sentence when that sentence leads into a result left out."""
    head, _, last = markdown.rpartition("\n\n")
    if last.startswith(("#", "$$", "|", "- ", "* ", "```")) or re.match(r"\d+\. ", last):
        return markdown
    match = LEAD_IN.search(last)
    if not match:
        return markdown
    kept = last[:match.start()].rstrip()
    return "\n\n".join(part for part in (head, kept) if part)


def chapter(project: Project, blueprint: Blueprint, mathlib_heads: dict[str, Leaf]) -> Built:
    """The chapter for *project*. *mathlib_heads* maps a Mathlib declaration to the
    Mathlib-chapter article it heads, for nodes in Mathlib.

    Each part, chapter and section with anything in it is a page; smaller units are
    headings on their section's page. A page reads in the blueprint's order: its
    prose, remarks and examples, and each node's card where the node stands. A
    labelled display, figure or table shows a number, counted on its page, that
    references print."""
    captions = {**{kind: kind.capitalize() for kind in KINDS}, **blueprint.captions}
    dochome = blueprint.links.get("dochome", "https://leanprover-community.github.io/mathlib4_docs")
    nodes = [node for node in blueprint.graph if in_lean(node)]
    present = set(nodes)
    # A section whose every node is left out goes with its prose, which is about those results; one
    # that never had a node, such as an introduction, stays.
    with_nodes = {id(unit) for node in blueprint.graph for unit in ancestors(node.unit)}
    dead = with_nodes - {id(unit) for node in nodes for unit in ancestors(node.unit)}

    def gone(unit: Unit | None) -> bool:
        return any(id(sub) in dead for sub in ancestors(unit))
    unit_index = {id(unit): k for k, unit in enumerate(blueprint.units)}
    stats = Counter(nodes=len(nodes), left_out=len(blueprint.graph) - len(nodes))

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
        if target == current[0]:
            return escape(text)  # the article that is being written
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
        text = writer.plain(node.body).lstrip(" ;,.:") if node.body else ""
        words = re.findall(r"(?:\$[^$]*\$|[^\s$])+", text)
        if not words:
            return f"{caption(node)} ({node.where.file.rsplit('/', 1)[-1]}, line {node.where.line})"
        cut = 1
        while cut < len(words) and len(" ".join(words[:cut])) < 40:
            cut += 1
        ended = words[cut - 1].endswith((".", "!", "?"))
        return f"{caption(node)}: {' '.join(words[:cut])}" + ("…" if cut < len(words) and not ended else "")

    leaf_of: dict[Node, Leaf] = {}
    owned: set[Node] = set()
    for node in nodes:
        if node.mathlibok and node.lean and node.lean[0] in mathlib_heads:
            leaf_of[node] = mathlib_heads[node.lean[0]]
            stats["mathlib_shared"] += 1
        else:
            owned.add(node)

    # What the pages show, in the blueprint's order. A proof that stands apart from its
    # statement leaves a pointer where it stands; a remark's proof stands where it is.
    events = [Event(node.offset, "card", node, node.unit) for node in nodes]
    if project.text:
        events += [Event(prose.offset, "prose", prose, prose.unit) for prose in blueprint.prose]
        for node in blueprint.nodes:
            if not node.graph:
                events.append(Event(node.offset, "aside", node, node.unit))
                if node.proof is not None:
                    events.append(Event(node.proof.offset, "aside proof", node, node.proof.unit))
        between = sorted(event.offset for event in events)
        for node in nodes:
            if node in owned and node.proof is not None and any(node.end <= at < node.proof.offset for at in between):
                events.append(Event(node.proof.offset, "proof pointer", node, node.proof.unit))
    if project.text:
        events += [Event(node.offset, "left out", node, node.unit) for node in blueprint.graph
                   if node not in present and not gone(node.unit)]
    events.sort(key=lambda event: event.offset)
    hidden = [event for event in events if gone(event.unit)]
    read_only = {id(event) for event in hidden}
    every_event, events = events, [event for event in events if id(event) not in read_only]
    shown = {id(unit) for event in events for unit in ancestors(event.unit) if unit.level <= 2}

    texts = [text or "" for event in events if event.kind not in ("proof pointer", "left out")
             for text in ([event.item.text] if isinstance(event.item, Prose)
                          else [event.item.title, event.item.body, *([event.item.proof.title, event.item.proof.body]
                                                                     if event.item.proof else [])])]
    texts += [unit.title for unit in blueprint.units]
    bib = bibtex.bibliography([project.directory / "src" / name for name in blueprint.bibliography],
                              [key for text in texts for key in cited(text)]) if project.text else {}

    # Equations, figures and tables: numbered on their page in the blueprint's order, before
    # any text refers to one.
    numbers: dict[str, tuple[str, str]] = {}  # label: its number, and the key of the article that shows it
    kinds: dict[str, str] = {}  # a figure's or table's label: "Figure" or "Table"
    counts: Counter = Counter()
    for event in events if project.text else []:
        if event.kind not in ("card", "aside", "prose") or (event.kind == "card" and event.item not in owned):
            continue
        article = event.item.id if event.kind == "card" else key(event.unit)
        for label in event.item.equations:
            if label not in numbers:
                counts[key(event.unit)] += 1
                numbers[label] = (str(counts[key(event.unit)]), article)
        for label, kind in event.item.floats:
            if label not in numbers:
                counts[key(event.unit), kind] += 1
                numbers[label] = (str(counts[key(event.unit), kind]), article)
                kinds[label] = kind.capitalize()
    stats["equations"] = len(numbers) - len(kinds)
    current = ["#root"]  # the article whose text is being written

    # What a reference to text that is left out points to: the place in the project's TeX.
    left_out_labels: dict[str, Node | Prose] = {}
    for item in [*(node for node in blueprint.graph if node not in present),
                 *(event.item for event in hidden if event.kind in ("prose", "aside"))]:
        for label in [*item.equations, *(label for label, _ in item.floats)]:
            left_out_labels.setdefault(label, item)

    def source_link(text: str, item: Node | Prose | Unit) -> str:
        stats["refs_to_left_out"] += 1
        return f"[{escape(text)}]({project.source(item.where)[1]})"

    def ref(label: str, command: str) -> str:
        target = blueprint.labels.get(label)
        if isinstance(target, Node):
            text = display(target)
            if command in NUMBER_ONLY:
                text = writer.plain(target.title) if target.title else short_id(target.id)
            if target.graph and target not in present or not target.graph and gone(target.unit):
                return source_link(text, target)
            return placeholder(text, target.id if target.graph else key(target.unit))
        if isinstance(target, Unit):
            home = page_unit(target)
            title = writer.plain(target.title)
            if gone(target):
                return source_link(title, target)
            return placeholder(title, key(target)) if home is None or id(home) in shown else escape(title)
        if label in left_out_labels:
            item = left_out_labels[label]
            if isinstance(item, Node):
                return source_link(display(item), item)
            return source_link(writer.plain(item.unit.title) if item.unit else project.name, item)
        if isinstance(target, tuple) and label in numbers:
            number, article = numbers[label]
            if label in kinds:
                text = number if command in NUMBER_ONLY else f"{kinds[label]} {number}"
            else:
                text = number if command in NUMBER_ONLY else f"({number})"
            if article == current[0]:
                return text
            # A number in a page's own text may end up in one of its parts; resolve() is told where.
            return placeholder(text, article if not article.startswith("#") else f"#label:{label}")
        stats["unresolved_refs"] += 1
        return f"({escape(label)})" if isinstance(target, tuple) else escape(label)

    def tag(label: str) -> str | None:
        if label not in numbers:
            return None
        return f"{kinds[label]} {numbers[label][0]}" if label in kinds else numbers[label][0]

    writer = Writer(blueprint.macros, ref, bib, tag=tag)

    lean_links: dict[str, str] = {}
    for node in blueprint.graph:
        current[0] = node.id
        if node in owned:
            leaf_of[node] = leaf(project, node, caption(node), heading(node), writer, dochome, blueprint, lean_links,
                                 stats)
        elif node not in present and project.text:
            # Read but not shown: its TeX may define macros that later text uses.
            writer.statement(node.body)
            if node.proof is not None:
                writer.statement(node.proof.body)

    # Dependencies: a node's \uses that name nodes, a proof's apart from its statement's.
    for node in nodes:
        if node not in owned:
            continue
        mine = leaf_of[node]
        statement = unique(leaf_of[target] for target in targets_of(node.uses, blueprint)
                           if target is not node and target in present)
        proof = unique(leaf_of[target] for target in targets_of(node.proof_uses, blueprint)
                       if target is not node and target in present)
        mine.depends = statement
        mine.proof_depends = [item for item in proof if item not in statement]
        if not statement and any(target is not node for target in targets_of(node.uses, blueprint)):
            mine.no_depends = "Its statement uses no other node that has an article here."
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
        last = opened.get(id(home), [])
        common = 0
        while common < min(len(chain), len(last)) and chain[common] is last[common]:
            common += 1
        for depth, sub in enumerate(chain[common:], common):
            write(home, f"{'#' * min(6, depth + 2)} {escape(writer.plain(sub.title) or 'Untitled')}")
        opened[id(home)] = chain

    # Pages whose last text was a left-out node. A remark there that carries a proof goes with the node:
    # leanblueprint gives a proof to the nearest environment before it, so that proof is often the node's.
    trailing: set[int] = set()
    for event in every_event:
        node = event.item
        if event.kind == "left out":
            home = page(event.unit)
            if pending.get(id(home)):
                if not pending[id(home)][-1].startswith("#"):
                    pending[id(home)][-1] = without_lead_in(pending[id(home)][-1])
            elif not home.entries:
                home.prose = without_lead_in(home.prose)
            trailing.add(id(home))
            stats["left_out_shown_at"] += 1
            continue
        if id(event) not in read_only:
            home = page(event.unit)
            if event.kind in ("aside", "aside proof") and id(home) in trailing and node.proof is not None:
                read_only.add(id(event))
            elif event.kind != "proof pointer":
                trailing.discard(id(home))
        if id(event) in read_only:
            # Left out with its section, but read: its TeX may define macros that later text uses.
            if event.kind == "prose":
                writer.statement(node.text)
            elif event.kind == "aside":
                writer.statement(node.body)
            elif event.kind == "aside proof":
                writer.statement(node.proof.body)
            continue
        home = page(event.unit)
        if event.kind == "card":
            open_headings(home, event.unit)
            add(home, Entry(leaf_of[node], node in owned))
            continue
        current[0] = key(event.unit)
        if event.kind == "prose":
            markdown = writer.statement(node.text)
        elif event.kind == "aside":
            title = f" ({escape(writer.plain(node.title))})" if node.title else ""
            markdown = run_in(f"**{caption(node)}{title}.**", writer.statement(node.body))
        elif event.kind == "aside proof":
            markdown = run_in(proof_head(node.proof, writer), writer.statement(node.proof.body))
        else:
            target = placeholder(display(node), node.id)
            markdown = (f"*{escape(writer.plain(node.proof.title))}: shown with {target}.*" if node.proof.title
                        else f"*The proof of {target} is shown with its statement.*")
        if markdown:
            open_headings(home, event.unit)
            write(home, markdown)
            stats[event.kind] += 1
    for container in [root, *pages.values()]:
        container.tail = "\n\n".join(pending.pop(id(container), []))
    for node in nodes:
        for label in [node.id, *node.labels]:
            targets[label] = leaf_of[node]
    for container in [*pages.values(), root]:
        chunk(container)

    # Where each number in a page's own text ended up: the page, or one of its parts.
    for label, (number, article) in numbers.items():
        if article.startswith("#"):
            home = targets[article]
            shown_as = re.compile(re.escape(f"**{kinds[label]} {number}.**") if label in kinds
                                  else r"\\text\{[^{}]*\(" + number + r"\)[^{}]*\}")
            targets[f"#label:{label}"] = next(
                (part for part in walk(home)
                 if isinstance(part, Container) and (part is home or part.navigation == "transparent")
                 and any(shown_as.search(text) for text in [part.prose, part.tail, *(e.before for e in part.entries)])),
                home)
    stats["containers"] = len(pages)
    stats["problems"] = len(blueprint.problems)
    return Built(root, targets, lean_links, dict(stats), writer.unknown)


def proof_head(proof: Proof, writer: Writer) -> str:
    """How a proof begins: its own title, as in \\begin{proof}[Note for category theorists], or Proof."""
    return f"*{escape(writer.plain(proof.title))}.*" if proof.title else "*Proof.*"


def ancestors(unit: Unit | None):
    """*unit* and the units it is in, innermost first."""
    while unit is not None:
        yield unit
        unit = unit.parent


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
    if node.mathlibok:
        fields += [("mathlib", "true"), ("mathlib_declaration", ", ".join(node.lean))]
        stats["mathlib"] += 1
    else:
        fields += [("lean", ", ".join(node.lean)), ("statement", "formalized")]
        if proof_ok:
            fields.append(("proof", "formalized"))
            stats["proofs_formalized"] += 1
        stats["statements_formalized"] += 1
        for name in node.lean:
            lean_links[name] = f"{dochome}/find/#doc/{name}"
    if node.discussion and blueprint.links.get("github"):
        fields.append(("discussion", f"{blueprint.links['github']}/issues/{node.discussion.strip().lstrip('#')}"))
    if lean_lines:
        lead = "Formalized as" if statement_ok else "The blueprint names"
        notes.append(("Lean", f"{lead} " + ", ".join(lean_lines) + "."))
    place, source = project.source(node.where)
    if project.text:
        body = writer.statement(node.body) or f"A {caption.lower()} of the blueprint of {project.name}, with no text."
        if node.proof is not None:
            proof = writer.statement(node.proof.body)
            if proof:
                notes.insert(0, ("Proof", run_in(proof_head(node.proof, writer), proof) if node.proof.title else proof))
    else:
        body = (f"The blueprint of {project.name} states this {caption.lower()} at [{place}]({source}). The "
                "project gives no license, so trough does not reproduce its text.")
    leaf_ = Leaf(escape(title), slugify(node.id), fields, body, notes=notes)
    leaf_.sources = [(f"{project.name} blueprint: {place}", source)]
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
        f"The blueprint of {project.name}, read at commit {rev}{date}: one article for each of its {nodes:,} nodes "
        "whose Lean declarations it names and marks formalized, or in Mathlib"
        + (f". Its other {stats['left_out']:,} nodes have no article, and a section of only those is left out: "
           "the map records what the project contains, not what it plans" if stats["left_out"] else "")
        + ". A node the blueprint marks `\\leanok` is formalized here, its proof too when that is marked, and "
        "`\\mathlibok` puts it in Mathlib. Dependencies are the blueprint's `\\uses`: a statement's under *Depends on*, a "
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
