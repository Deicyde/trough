"""Write an AutoformBot vault: containers, leaves, their paths and their pages.

A container is a directory holding a README.md; a leaf is one statement page.
Containers list their entries in order. An entry either owns its node, which
then lives in the container's directory, or refers to a node that lives
elsewhere, so one article can appear in several lists but has one home.
Text can sit between the entries: AutoformBot shows each owned leaf's card in
place of its line, so the page reads in the order it is written.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

# `autoform audit` reports a container with more than 24 children; 20 leaves room.
MAX_CHILDREN = 20
ARTICLE_ID = re.compile(r"^article_id: (af_[0-9a-f]{24})$", re.M)
MATH_SPAN = re.compile(r"(?s)(?<!\\)(?P<dollars>\${1,2}).*?(?<!\\)(?P=dollars)|\\\(.*?\\\)|\\\[.*?\\\]")


@dataclass(eq=False)
class Leaf:
    """One statement page."""

    title: str
    slug: str
    fields: list[tuple[str, str]]
    body: str
    sources: list[tuple[str, str]] = field(default_factory=list)
    depends: list[Leaf] = field(default_factory=list)
    proof_depends: list[Leaf] = field(default_factory=list)
    informal: list[Leaf] = field(default_factory=list)
    no_depends: str = "This node has no prerequisites."
    notes: list[tuple[str, str]] = field(default_factory=list)  # (heading, Markdown) sections before Sources
    path: Path = Path()


@dataclass(eq=False)
class Entry:
    """A line of a container's listing: the node, and whether it lives here."""

    node: Leaf | Container
    owned: bool = True
    label: str | None = None
    before: str = ""  # Markdown between the previous line and this one

    @property
    def text(self) -> str:
        return self.label or self.node.title


@dataclass(eq=False)
class Container:
    title: str
    slug: str
    entries: list[Entry] = field(default_factory=list)
    prose: str = ""
    navigation: str | None = None
    path: Path = Path()
    tail: str = ""  # Markdown after the last entry
    article_id: str | None = None  # an authored page's, which wins over the one the page had

    @property
    def children(self) -> list[Leaf | Container]:
        return [entry.node for entry in self.entries if entry.owned]


def slugify(text: str, limit: int = 48) -> str:
    # In math, font commands go and other commands keep their names: $\C$ reads "C".
    text = re.sub(
        r"\$[^$]*\$",
        lambda math: re.sub(r"\\([A-Za-z]+)", r" \1 ", re.sub(r"\\(?:math[a-z]*|operatorname|text)\b", " ", math.group())),
        text,
    )
    text = re.sub(r"[\u2010-\u2015\u2212]", "-", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", re.sub(r"['’]", "", text.lower())).strip("-")
    return slug[:limit].rstrip("-") or "untitled"


def short(text: str, limit: int = 32) -> str:
    """A label cut at a word boundary, for part titles."""
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def range_title(group: list[Entry], number: int, total: int) -> str:
    if len(group) == 1:
        return f"Part {number} of {total}"
    return f"{short(group[0].text)} to {short(group[-1].text)}"


def link_text(text: str) -> str:
    """Text for a link label, its brackets escaped outside code spans, which show a backslash as is."""
    parts = re.split(r"(`+[^`]*`+)", text)
    return "".join(part if index % 2 else part.replace("[", "\\[").replace("]", "\\]")
                   for index, part in enumerate(parts))


def chunk(container: Container, title: Callable[[list[Entry], int, int], str] = range_title) -> Container:
    """Nest a long listing into transparent parts so no page lists more than MAX_CHILDREN."""
    entries = container.entries
    if len(entries) <= MAX_CHILDREN:
        return container
    size = MAX_CHILDREN
    while -(-len(entries) // size) > MAX_CHILDREN:
        size *= MAX_CHILDREN
    groups = [entries[start : start + size] for start in range(0, len(entries), size)]
    parts = []
    for number, group in enumerate(groups, 1):
        part = Container(title(group, number, len(groups)), f"part-{number:02d}", group, navigation="transparent")
        if number == len(groups):
            part.tail, container.tail = container.tail, ""
        parts.append(Entry(chunk(part, title)))
    container.entries = parts
    return container


def assign_paths(node: Container, directory: Path) -> None:
    node.path = directory / "README.md"
    taken: set[str] = set()
    for child in node.children:
        base, number = child.slug, 1
        while child.slug in taken:
            number += 1
            child.slug = f"{base}-{number}"
        taken.add(child.slug)
        if isinstance(child, Container):
            assign_paths(child, directory / child.slug)
        else:
            child.path = directory / f"{child.slug}.md"


def walk(node: Container):
    yield node
    for child in node.children:
        if isinstance(child, Container):
            yield from walk(child)
        else:
            yield child


def rel(source: Path, target: Path) -> str:
    """Relative link from one vault file to another."""
    common = 0
    for left, right in zip(source.parent.parts, target.parts):
        if left != right:
            break
        common += 1
    up = len(source.parent.parts) - common
    return "/".join([".."] * up + list(target.parts[common:]))


def safe_math_markdown(text: str) -> str:
    """Keep TeX comparisons from opening raw-HTML tags inside site cards."""
    return MATH_SPAN.sub(lambda span: re.sub(r"<(?=[A-Za-z_\\])", r"\\lt ", span.group()), text)


def frontmatter(fields: list[tuple[str, str]], previous: str | None) -> str:
    """The page's front matter, keeping the article_id it had unless fields give one (an authored
    article's, which wins)."""
    match = None if any(key == "article_id" for key, _ in fields) else ARTICLE_ID.search(previous or "")
    lines = ([f"article_id: {match.group(1)}"] if match else []) + [f"{key}: {value}" for key, value in fields]
    return "---\n" + "\n".join(lines) + "\n---\n\n" if lines else ""


def facts(node: Leaf | Container) -> list[tuple[str, str]]:
    """What AutoformBot reads about the page, from its front matter or its annotation."""
    if isinstance(node, Leaf):
        return node.fields
    return ([("article_id", node.article_id)] if node.article_id else []) + (
        [("navigation", node.navigation)] if node.navigation else [])


def render_container(node: Container, vault: Path, previous: str | None, front: bool = True) -> str:
    here = node.path.relative_to(vault)
    lines = [f"# {node.title}", ""]
    if node.prose:
        lines += [node.prose.strip(), ""]

    def link(entry: Entry) -> str:
        return f"- [{link_text(entry.text)}]({rel(here, entry.node.path.relative_to(vault))})"

    if node.entries and all(
        isinstance(entry.node, Container) and entry.node.navigation == "transparent" for entry in node.entries
    ):
        # Pagination parts read as sections of this page. Each heading still links
        # its part, which keeps the part, and the depth of its children, in the
        # site navigation built from these links.
        for entry in node.entries:
            part = entry.node
            heading = f"[{link_text(part.title)}]({rel(here, part.path.relative_to(vault))})"
            lines += [f"## {heading}", "", *(link(item) for item in part.entries), ""]
        lines.pop()
    else:
        for entry in node.entries:
            if entry.before:
                lines += ([""] if lines[-1] else []) + [entry.before.strip(), ""]
            lines.append(link(entry))
    if node.tail:
        lines += ["", node.tail.strip()]
    return (frontmatter(facts(node), previous) if front else "") + "\n".join(lines).rstrip() + "\n"


def render_leaf(leaf: Leaf, vault: Path, previous: str | None, front: bool = True) -> str:
    here = leaf.path.relative_to(vault)

    def links(nodes: list[Leaf]) -> list[str]:
        return [f"- [{link_text(node.title)}]({rel(here, node.path.relative_to(vault))})" for node in nodes]

    lines = [f"# {leaf.title}", "", leaf.body.strip(), "", "## Depends on", ""]
    lines += links(leaf.depends) if leaf.depends else [leaf.no_depends]
    if leaf.proof_depends:
        lines += ["", "## Proof depends on", "", *links(leaf.proof_depends)]
    if leaf.informal:
        lines += ["", "## Informally uses", "", *links(leaf.informal)]
    for heading, text in leaf.notes:
        lines += ["", f"## {heading}", "", text.strip()]
    if leaf.sources:
        lines += ["", "## Sources", ""]
        lines += [f"- [{link_text(label)}]({url})" for label, url in leaf.sources]
    return (frontmatter(leaf.fields, previous) if front else "") + "\n".join(lines) + "\n"


def render_tree(root: Container, vault: Path, *, include_root: bool = True, annotated: bool = False) -> dict[Path, str]:
    """Every page under *root*, keeping each existing page's article_id; with *annotated*, the facts
    go in annotations (links.py) and the pages have no front matter."""
    files: dict[Path, str] = {}
    for node in walk(root):
        if node is root and not include_root:
            continue
        previous = node.path.read_text(encoding="utf-8") if node.path.is_file() else None
        if isinstance(node, Container):
            files[node.path] = render_container(node, vault, previous, not annotated)
        else:
            files[node.path] = render_leaf(node, vault, previous, not annotated)
    return files
