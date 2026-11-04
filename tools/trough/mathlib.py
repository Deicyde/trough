"""The Mathlib chapter: one article per concept on Mathlib's four curated lists.

Mathlib's maintainers keep docs/overview.yaml, docs/undergrad.yaml, docs/100.yaml
and docs/1000.yaml, and Mathlib's CI checks that every declaration they name
exists. Each list item names declarations, a module, a URL, or nothing yet.
Items naming the same set of declarations are one article, placed where the
item ranked first (overview, undergraduate, 100, 1000+) puts it; every other
list links to it. An item naming nothing is an article of its own, marked
not ready. data/mathlib/concept-deps.json, written by lean/ConceptDeps.lean in
GitHub Actions, gives each declaration's kind, docstring, signature and the
nearest list declarations its statement and proof use.
"""

from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, unquote

import yaml

from .vault import Container, Entry, Leaf, chunk, safe_math_markdown, slugify
from .wiki import LEAN_LINK, Authored, link_citations, linked

LISTS = ("overview", "undergrad", "100", "1000")
LIST_TITLES = {
    "overview": "Mathlib overview",
    "undergrad": "Undergraduate mathematics",
    "100": "Freek Wiedijk's 100 theorems",
    "1000": "1000+ theorems",
}
LIST_SLUGS = {"overview": "overview", "undergrad": "undergraduate", "100": "hundred-theorems", "1000": "thousand-plus"}
LIST_PROSE = {
    "overview": (
        "Mathlib's own overview of what it contains, area by area "
        "([docs/overview.yaml]({yaml}))."
    ),
    "undergrad": (
        "The undergraduate curriculum Mathlib tracks, with the topics it does not cover yet "
        "([docs/undergrad.yaml]({yaml}))."
    ),
    "100": (
        "Freek Wiedijk's list of 100 famous theorems, with Mathlib's formalizations and the "
        "ones done elsewhere ([docs/100.yaml]({yaml}))."
    ),
    "1000": (
        "The theorems of Wikipedia's list of theorems, as collected by the "
        "[1000+ theorems project](https://1000-plus.github.io/), grouped by Mathematics Subject "
        "Classification ([docs/1000.yaml]({yaml}))."
    ),
}
DOCS = "https://leanprover-community.github.io/mathlib4_docs"
MATHLIB_REPO = "https://github.com/leanprover-community/mathlib4"
# Wanted items carry no Lean kind; a title naming a result is read as a theorem.
THEOREM_TITLE = re.compile(
    r"(?i)\b(theorem|lemma|formula|inequalit|identit|law|criteri|conjecture|principle|test|rule|"
    r"paradox|bound|estimate|equality|reciprocity|classification|expansion|decomposition)"
)
# Lean constant kinds that are not declaration commands, as the command that makes them.
KIND_COMMANDS = {"constructor": "def", "recursor": "def", "quot": "def"}
# How many of a module's documented declarations a module article names.
MODULE_DECLARATIONS = 12
# Coarse sections of the Mathematics Subject Classification, so the 1000+ list's
# root page stays short. A section holding one code is that code's page.
MSC_SECTIONS = (
    ("General topics, history and foundations", ("00", "01", "03")),
    ("Combinatorics and ordered structures", ("05", "06", "08")),
    ("Number theory", ("11",)),
    ("Algebra", ("12", "13", "14", "15", "16", "17", "18", "19", "20", "22")),
    (
        "Analysis",
        ("26", "28", "30", "31", "32", "33", "34", "35", "37", "39", "40", "41", "42", "43", "44", "45", "46", "47", "49"),
    ),
    ("Geometry and topology", ("51", "52", "53", "54", "55", "57", "58")),
    ("Probability and statistics", ("60", "62")),
    (
        "Applied mathematics",
        ("65", "68", "70", "74", "76", "78", "80", "81", "82", "83", "85", "86", "90", "91", "92", "93", "94", "97"),
    ),
)


@dataclass(eq=False)
class Item:
    """One entry of one curated list."""

    list: str
    key: str
    path: tuple[str, ...]
    title: str
    line: int
    decls: tuple[str, ...] = ()
    module: str | None = None
    url: str | None = None
    statement: str | None = None
    authors: str | None = None
    note: str | None = None
    links: dict[str, str] = field(default_factory=dict)

    @property
    def heading(self) -> str:
        """The title as a heading. The tree lists' keys are lowercase and get a capital; the
        100 and 1000+ titles are written as titles ("e is Transcendental") and stay as they are."""
        return capitalize(self.title) if self.list in ("overview", "undergrad") else self.title

    @property
    def label(self) -> str:
        return f"{self.key}. {self.heading}" if self.list == "100" else self.heading


@dataclass(eq=False)
class Article:
    items: list[Item]
    decls: tuple[str, ...] = ()
    module: str | None = None
    leaf: Leaf | None = None

    @property
    def home(self) -> Item:
        return self.items[0]

    @property
    def kind(self) -> str:
        return "decl" if self.decls else "module" if self.module else "wanted"


@dataclass
class Sources:
    """Everything the chapter is generated from."""

    rev: str
    date: str
    lists: dict[str, list[Item]]
    deps: dict | None
    thousand_plus: dict | None


def title_key(title: str) -> str:
    """A title for matching across lists, which differ in quotes, dashes, case and a leading "The"."""
    text = title.translate(str.maketrans("‘’–—", "''--")).casefold().strip()
    return re.sub(r"^the\s+", "", text)


def capitalize(title: str) -> str:
    return title[:1].upper() + title[1:] if title[:1].islower() else title


def text(node: yaml.Node | None) -> str | None:
    if node is None:
        return None
    if isinstance(node, yaml.ScalarNode):
        # 1000.yaml copies a few titles from Wikipedia with HTML entities such as &ndash;.
        return None if node.tag.endswith(":null") else html.unescape(node.value.strip())
    if isinstance(node, yaml.SequenceNode):
        return ", ".join(filter(None, (text(child) for child in node.value)))
    raise ValueError(f"line {node.start_mark.line + 1}: expected text")


def compose(path: Path) -> yaml.MappingNode:
    with path.open(encoding="utf-8") as handle:
        node = yaml.compose(handle, Loader=yaml.SafeLoader)
    if not isinstance(node, yaml.MappingNode):
        raise ValueError(f"{path}: expected a mapping")
    return node


def tree_items(name: str, root: yaml.MappingNode) -> list[Item]:
    """overview.yaml and undergrad.yaml: nested headings over `title: value` leaves.

    As on the community website, a value holding "http" is a link, one holding
    "/" a module's documentation page, an empty one an item Mathlib lacks, and
    anything else a declaration name.
    """
    items: list[Item] = []

    def visit(node: yaml.MappingNode, path: tuple[str, ...]) -> None:
        for key, value in node.value:
            title = text(key) or ""
            if isinstance(value, yaml.MappingNode):
                visit(value, path + (title,))
                continue
            item = Item(name, "/".join(path + (title,)), path, title, key.start_mark.line + 1)
            leaf = text(value) or ""
            if "http" in leaf:
                item.url = leaf
            elif "/" in leaf:
                item.module = leaf.removesuffix(".html").replace("/", ".")
            elif leaf:
                item.decls = (leaf,)
            items.append(item)

    visit(root, ())
    return items


def record_items(name: str, root: yaml.MappingNode) -> list[Item]:
    """100.yaml and 1000.yaml: one record per key."""
    items: list[Item] = []
    for key, value in root.value:
        if not isinstance(value, yaml.MappingNode):
            raise ValueError(f"{name}.yaml line {key.start_mark.line + 1}: expected a record")
        fields = {text(k): v for k, v in value.value}
        item = Item(name, text(key) or "", (), text(fields.get("title")) or text(key) or "", key.start_mark.line + 1)
        if "decl" in fields:
            item.decls = (text(fields["decl"]) or "",)
        elif "decls" in fields:
            item.decls = tuple(filter(None, (text(child) for child in fields["decls"].value)))
        item.statement = text(fields.get("statement"))
        item.authors = text(fields.get("authors"))
        item.url = text(fields.get("url"))
        item.note = text(fields.get("note")) or text(fields.get("comment"))
        links = fields.get("links")
        if isinstance(links, yaml.MappingNode):
            item.links = {text(k) or "": text(v) or "" for k, v in links.value}
        items.append(item)
    return items


def load_sources(data: Path, deps: bool = True) -> Sources:
    """The lists, and unless `deps` is false the dump, which must be of the lists' Mathlib commit."""
    directory = data / "mathlib"
    source = json.loads((directory / "source.json").read_text(encoding="utf-8"))
    lists = {}
    for name in LISTS:
        root = compose(directory / "yaml" / f"{name}.yaml")
        lists[name] = tree_items(name, root) if name in ("overview", "undergrad") else record_items(name, root)
    deps_file = directory / "concept-deps.json"
    dump = json.loads(deps_file.read_text(encoding="utf-8")) if deps and deps_file.is_file() else None
    if dump is not None and dump.get("mathlib_rev") != source["rev"]:
        raise ValueError(
            f"{deps_file} was computed at Mathlib {dump.get('mathlib_rev')}, but the lists are at {source['rev']}: "
            "rerun the Mathlib data workflow"
        )
    thousand_file = data / "thousand-plus.json"
    thousand_plus = json.loads(thousand_file.read_text(encoding="utf-8")) if thousand_file.is_file() else None
    return Sources(source["rev"], source.get("date", ""), lists, dump, thousand_plus)


def merge(lists: dict[str, list[Item]]) -> list[Article]:
    """One article per concept.

    Items naming the same set of declarations, or the same first declaration, are
    one concept: an article's first declaration is the one that takes its credit.
    The article keeps its first item's declarations, since a list item that bundles
    several results (Freek's "Sylow's Theorem") is not all of them at once.
    Sharing only a later declaration does not merge two items, since a common
    lemma does not make two results the same. An item naming nothing is known by
    its title alone: the same title in another list is the same concept, a second
    one in the same list is not.
    """
    articles: dict[object, Article] = {}
    for name in LISTS:
        for item in lists[name]:
            if item.decls:
                article = articles.get(frozenset(item.decls)) or articles.get(("first", item.decls[0]))
                if article is None:
                    article = Article([item], item.decls)
                    articles[("first", item.decls[0])] = article
                else:
                    article.items.append(item)
                articles.setdefault(frozenset(item.decls), article)
                continue
            if item.statement:
                key: object = ("statement", item.statement)
            elif item.module:
                key = ("module", item.module)
            else:
                key = ("wanted", title_key(item.title))
                if key in articles and any(other.list == item.list for other in articles[key].items):
                    key = ("item", item.list, item.key)
            if key in articles:
                articles[key].items.append(item)
            else:
                articles[key] = Article([item], (), item.module)
    return list(dict.fromkeys(articles.values()))


def concept_names(articles: list[Article]) -> list[str]:
    return sorted({name for article in articles for name in article.decls})


def module_names(articles: list[Article]) -> list[str]:
    return sorted({article.module for article in articles if article.module})


def concept_key(article: Article) -> str:
    """What an authored article names its concept by: the first declaration, the statement or
    module, or for one Mathlib lacks "<list>:<item key>"."""
    if article.decls:
        return article.decls[0]
    statement = next((item.statement for item in article.items if item.statement), None)
    return statement or article.module or f"{article.home.list}:{article.home.key}"


def module_path(module: str) -> str:
    return module.replace(".", "/") + ".lean"


def doc_url(name: str, module: str | None) -> str:
    anchor = quote(name, safe=".'_-!?«»")
    if module:
        return f"{DOCS}/{module.replace('.', '/')}.html#{anchor}"
    return f"{DOCS}/find?pattern={anchor}#doc"


def source_url(rev: str, module: str, line: int | None) -> str | None:
    if not module.split(".")[0] in ("Mathlib", "Archive", "Counterexamples"):
        return None
    return f"{MATHLIB_REPO}/blob/{rev}/{module_path(module)}" + (f"#L{line}" if line else "")


def item_source(sources: Sources, item: Item) -> tuple[str, str]:
    url = f"{MATHLIB_REPO}/blob/{sources.rev}/docs/{item.list}.yaml#L{item.line}"
    if item.list == "overview":
        return f"Mathlib overview: {' › '.join(item.path)}", url
    if item.list == "undergrad":
        return f"Mathlib undergraduate list: {' › '.join(item.path)}", url
    if item.list == "100":
        return f"Freek Wiedijk's 100 theorems, no. {item.key}", url
    return f"1000+ theorems list: {item.key}", url


def list_reference(item: Item) -> str:
    """An item's list, for prose."""
    if item.list in ("overview", "undergrad"):
        return "Mathlib's overview" if item.list == "overview" else "Mathlib's undergraduate list"
    return f"Freek Wiedijk's list (no. {item.key})" if item.list == "100" else f"the 1000+ list ({item.key})"


def wikipedia_url(page: str) -> str:
    title, _, section = page.partition("#")
    url = "https://en.wikipedia.org/wiki/" + quote(title.replace(" ", "_"), safe="_,'-:!")
    return url + ("#" + quote(section.replace(" ", "_"), safe="_,'-:!.") if section else "")


def link_url(url: str) -> str:
    """A URL safe inside a Markdown link: no spaces or parentheses."""
    return url.strip().replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def note_text(note: str) -> str:
    """A list's note as a sentence, with bare URLs made links."""
    note = re.sub(r"(?<![(<\[])\bhttps?://[^\s)>\]]+?(?=[.,;:]?(?:\s|$))", lambda url: f"<{url.group()}>", note.strip())
    return note if note.endswith((".", "!", "?")) else note + "."


def clean_doc(doc: str) -> str:
    """A docstring as statement prose: headings become bold lines, citations link to
    Mathlib's bibliography, math stays safe."""
    lines = []
    for line in doc.strip().splitlines():
        heading = re.match(r"^\s*#+\s+(.*)$", line)
        lines.append(f"**{heading.group(1).strip()}**" if heading else line.rstrip())
    text = "\n".join(lines).strip()
    # doc-gen4 reads a link to a bare key, [Zwillinger](zwillinger2003), and a bracketed
    # key, [axler2024], as citations of Mathlib's docs/references.bib.
    text = re.sub(r"\]\(([A-Za-z][\w-]*)\)", rf"]({DOCS}/references.html#ref_\1)", text)
    text = re.sub(r"(?<![\]\w])\[([A-Za-z]+\d{4}[a-z]?)\](?![(\[])", rf"[\1]({DOCS}/references.html#ref_\1)", text)
    return safe_math_markdown(text)


def fence(code: str) -> str:
    ticks = "```"
    while ticks in code:
        ticks += "`"
    return f"{ticks}lean\n{code.strip()}\n{ticks}"


def default_kind(article: Article) -> str:
    if article.home.list in ("100", "1000") or THEOREM_TITLE.search(article.home.title):
        return "theorem"
    return "definition"


def thousand_entry(sources: Sources, item: Item) -> tuple[str, dict]:
    """The 1000+ project's key and entry for a 1000.yaml item. A few of Mathlib's keys are ones
    the project has since replaced; those match the entry whose Wikipedia page is the title."""
    entries = (sources.thousand_plus or {}).get("entries") or {}
    if item.key in entries:
        return item.key, entries[item.key]
    listed = {other.key for other in sources.lists["1000"]}
    title = title_key(item.title)
    for key, entry in entries.items():
        if key not in listed and any(title_key(page.partition("#")[0]) == title for page in entry.get("wikipedia", [])):
            return key, entry
    return item.key, {}


def external_lines(sources: Sources, article: Article) -> tuple[list[str], list[tuple[str, str]]]:
    """Prose and links about formalizations and references outside Mathlib."""
    prose: list[str] = []
    links: list[tuple[str, str]] = []
    for item in article.items:
        if item.list == "1000":
            key, entry = thousand_entry(sources, item)
            # The project's rows are keyed by bare Wikidata ids, and only its all-theorems
            # page has a row for every theorem.
            qid = re.sub(r"[A-Z]$", "", key)
            links.append((f"1000+ theorems project: {key}", f"https://1000-plus.github.io/all.html?length=-1#{qid}"))
            for page in entry.get("wikipedia", [])[:1]:
                links.append((f"Wikipedia: {page.replace('#', ' § ')}", wikipedia_url(page)))
            links.append((f"Wikidata: {qid}", f"https://www.wikidata.org/wiki/{qid}"))
            others = sorted(prover for prover in entry.get("others", {}) if prover != "lean")
            if others and not article.decls:
                names = {"hol_light": "HOL Light", "rocq": "Rocq", "isabelle": "Isabelle", "metamath": "Metamath",
                         "mizar": "Mizar", "coq": "Rocq"}
                prose.append(
                    "The 1000+ theorems project records formalizations in "
                    + ", ".join(names.get(prover, prover) for prover in others) + "."
                )
        if item.url and item.list == "1000":
            prose.append("Mathlib's 1000+ list links a formalization.")
            links.append(("Formalization linked by the 1000+ list", link_url(item.url)))
        if item.url and item.list == "undergrad":
            links.append(("Reference given by Mathlib's undergraduate list", link_url(item.url)))
        if item.links and not article.decls:
            prose.append("Formalized outside Mathlib; the 100 theorems list links the formalization.")
        for label, url in item.links.items():
            links.append((f"Outside Mathlib: {label}", link_url(url)))
        if item.note:
            # Another list's note is about that list's item, which may be a narrower result.
            whose = "" if item is article.home else capitalize(list_reference(item)) + ": "
            prose.append(whose + note_text(item.note))
    return list(dict.fromkeys(prose)), list(dict.fromkeys(links))


def build_leaf(sources: Sources, article: Article, claimed: frozenset[str] = frozenset()) -> Leaf:
    home = article.home
    title = home.heading
    concepts = (sources.deps or {}).get("concepts", {})
    prose, external = external_lines(sources, article)
    item_links = [item_source(sources, item) for item in article.items]
    if article.kind == "decl":
        records = [concepts.get(name) for name in article.decls]
        first = records[0] or {}
        kind = KIND_COMMANDS.get(first.get("kind"), first.get("kind")) or default_kind(article)
        fields = [("declaration", kind), ("origin", "cited"), ("mathlib", "true"),
                  ("mathlib_declaration", ", ".join(article.decls))]
        if first.get("module") and source_url(sources.rev, first["module"], None):
            fields.append(("mathlib_file", module_path(first["module"])))
        body: list[str] = []
        many = len(article.decls) > 1
        if many:
            body.append(f"Mathlib records this with {len(article.decls)} declarations.")
        for name, record in zip(article.decls, records):
            record = record or {}
            doc = clean_doc(record["doc"]) if record.get("doc") else ""
            if many:
                body.append(f"`{name}`" + (f": {doc}" if doc else "."))
            elif doc:
                body.append(doc)
            else:
                body.append(f"Mathlib states this as `{name}`.")
            if record.get("signature"):
                body.append(fence(record["signature"]))
        extras: dict[tuple[str, ...], list[Item]] = defaultdict(list)
        for item in article.items[1:]:
            extra = tuple(name for name in item.decls if name not in article.decls)
            if extra:
                extras[extra].append(item)
        for extra, items in extras.items():
            refs = " and ".join(list_reference(item) for item in items)
            body.append(capitalize(refs) + (" also cite " if len(items) > 1 else " also cites ")
                        + ", ".join(f"`{name}`" for name in extra) + ".")
        body += prose
        links = []
        for name, record in zip(article.decls, records):
            record = record or {}
            links.append((f"Mathlib documentation: `{name}`", doc_url(name, record.get("module"))))
            src = source_url(sources.rev, record["module"], record.get("line")) if record.get("module") else None
            if src:
                links.append((f"Source of `{name}` in {module_path(record['module'])}", src))
        leaf = Leaf(title, slugify(title), fields, "\n\n".join(body), links + item_links + external)
        if not sources.deps:
            leaf.no_depends = "Dependencies are computed by the Mathlib data workflow and are not in yet."
        elif not any(records):
            leaf.no_depends = "Mathlib's declaration graph had no record of it, so its dependencies are unknown."
        else:
            leaf.no_depends = "Its statement uses no other concept on these lists."
        return leaf
    if article.kind == "module":
        module = article.module or ""
        modules = (sources.deps or {}).get("modules", {})
        doc = (modules.get(module) or {}).get("doc") or ""
        first_paragraph = re.split(r"\n\s*\n", re.sub(r"(?m)^#+ .*$", "", doc).strip(), maxsplit=1)[0]
        body = []
        if first_paragraph:
            body.append(clean_doc(first_paragraph))
        body.append(f"Mathlib covers this with the module `{module}` rather than a single declaration.")
        body += prose
        fields = [("declaration", default_kind(article)), ("origin", "cited"), ("mathlib", "true")]
        # autoform credits a Mathlib article to its declarations; a module's are its
        # documented ones that no other article claims, in source order, the first
        # MODULE_DECLARATIONS of them.
        documented = (modules.get(module) or {}).get("decls") or []
        declared = [name for name in documented if name not in claimed][:MODULE_DECLARATIONS]
        if declared:
            fields.append(("mathlib_declaration", ", ".join(declared)))
            more = len(documented) - len(declared)
            body.append(
                f"Its {len(documented)} documented declarations include "
                + ", ".join(f"`{name}`" for name in declared)
                + (f", and {more} more." if more > 0 else ".")
            )
        fields.append(("mathlib_file", module_path(module)))
        links = [(f"Mathlib documentation: {module}", f"{DOCS}/{module.replace('.', '/')}.html")]
        src = source_url(sources.rev, module, None)
        if src:
            links.append((f"Source: {module_path(module)}", src))
        leaf = Leaf(title, slugify(title), fields, "\n\n".join(body), links + item_links + external)
        leaf.no_depends = "Dependencies are tracked for single declarations only."
        return leaf
    statements = [item.statement for item in article.items if item.statement]
    body = []
    if statements:
        record = concepts.get(statements[0]) or {}
        body.append(f"Mathlib states this as `{statements[0]}` but does not prove it.")
        if record.get("signature"):
            body.append(fence(record["signature"]))
    elif any(item.authors and item.list == "1000" for item in article.items):
        authors = next(item.authors for item in article.items if item.authors)
        body.append(f"Mathlib's 1000+ list marks this formalized by {authors}, without naming a declaration.")
    elif home.list == "undergrad":
        body.append("Not yet in Mathlib: its undergraduate list names no declaration for this topic.")
    elif home.list == "100":
        body.append("Not in Mathlib.")
    else:
        body.append("Not yet in Mathlib: its 1000+ list names no declaration for this theorem.")
    body += prose
    fields = [("declaration", default_kind(article)), ("origin", "cited"), ("not_ready", "true")]
    leaf = Leaf(title, slugify(title), fields, "\n\n".join(body), item_links + external)
    leaf.no_depends = "Its prerequisites are not mapped yet."
    return leaf


def tree_container(sources: Sources, name: str, articles_by_item: dict[int, Article],
                   areas: dict[tuple[str, ...], str] | None = None,
                   targets: dict[str, Leaf | Container] | None = None) -> Container:
    """overview and undergrad: the list's own headings, in its order. An overview section with an
    authored page (areas) opens with its text."""
    yaml_url = f"{MATHLIB_REPO}/blob/{sources.rev}/docs/{name}.yaml"
    root = Container(LIST_TITLES[name], LIST_SLUGS[name], prose=LIST_PROSE[name].format(yaml=yaml_url))
    by_path: dict[tuple[str, ...], Container] = {(): root}
    for item in sources.lists[name]:
        for depth in range(1, len(item.path) + 1):
            path = item.path[:depth]
            if path not in by_path:
                node = Container(capitalize(path[-1]), slugify(path[-1]))
                if name == "overview" and areas and path in areas:
                    node.prose = areas[path]
                if name == "overview" and targets is not None:
                    targets["area:" + "/".join(path)] = node
                by_path[path[:-1]].entries.append(Entry(node))
                by_path[path] = node
        article = articles_by_item[id(item)]
        owned = article.home is item
        by_path[item.path].entries.append(Entry(article.leaf, owned, None if owned else item.label))
    for node in by_path.values():
        if node is not root:
            chunk(node)
    return root


def hundred_container(sources: Sources, articles_by_item: dict[int, Article]) -> Container:
    yaml_url = f"{MATHLIB_REPO}/blob/{sources.rev}/docs/100.yaml"
    root = Container(LIST_TITLES["100"], LIST_SLUGS["100"], prose=LIST_PROSE["100"].format(yaml=yaml_url))
    items = sorted(sources.lists["100"], key=lambda item: int(item.key) if item.key.isdigit() else 10**9)
    for item in items:
        article = articles_by_item[id(item)]
        owned = article.home is item
        root.entries.append(Entry(article.leaf, owned, item.label))

    def numbers(group: list[Entry], number: int, total: int) -> str:
        first, last = (entry.text.split(".", 1)[0] for entry in (group[0], group[-1]))
        return f"Theorems {first} to {last}"

    return chunk(root, numbers)


def thousand_container(sources: Sources, articles_by_item: dict[int, Article]) -> Container:
    yaml_url = f"{MATHLIB_REPO}/blob/{sources.rev}/docs/1000.yaml"
    root = Container(LIST_TITLES["1000"], LIST_SLUGS["1000"], prose=LIST_PROSE["1000"].format(yaml=yaml_url))
    names = (sources.thousand_plus or {}).get("msc_names", {})
    by_code: dict[str, list[Item]] = defaultdict(list)
    for item in sources.lists["1000"]:
        by_code[thousand_entry(sources, item)[1].get("msc", "")].append(item)

    def code_container(code: str) -> Container:
        title = f"{code} {names[code]}" if code in names else "Unclassified"
        node = Container(title, slugify(title))
        for item in sorted(by_code[code], key=lambda item: (item.title.casefold(), item.key)):
            article = articles_by_item[id(item)]
            owned = article.home is item
            node.entries.append(Entry(article.leaf, owned, item.label))
        return chunk(node)

    placed: set[str] = set()
    for title, codes in MSC_SECTIONS:
        present = [code for code in codes if code in by_code]
        placed.update(present)
        if len(present) == 1:
            node = code_container(present[0])
            node.title, node.slug = title, slugify(title)
            root.entries.append(Entry(node))
        elif present:
            section = Container(title, slugify(title), [Entry(code_container(code)) for code in present])
            root.entries.append(Entry(chunk(section)))
    rest = sorted(code for code in by_code if code not in placed)
    if len(rest) == 1:
        root.entries.append(Entry(code_container(rest[0])))
    elif rest:
        section = Container("Other and unclassified", "other", [Entry(code_container(code)) for code in rest])
        root.entries.append(Entry(chunk(section)))
    return root


def sort_key(article: Article) -> tuple[str, str]:
    return (article.leaf.title.casefold() if article.leaf else "", ",".join(article.decls))


def link_edges(sources: Sources, articles: list[Article]) -> dict[str, int]:
    """Article edges from the declaration-level fronts, acyclic and transitively reduced.

    The dump gives, for each list declaration, the nearest list declarations its
    statement and its proof reach through declarations on no list. Merging
    declarations into articles can close a cycle; a depth-first search in title
    order moves each edge that closes one to "Informally uses". A statement
    dependency already reached through another statement dependency, or a proof
    dependency reached through any other dependency, is then left out.
    """
    stats = {"statement_raw": 0, "proof_raw": 0, "informal": 0, "statement": 0, "proof": 0}
    concepts = (sources.deps or {}).get("concepts")
    if not concepts:
        return stats
    # A declaration in two articles stands for the one whose first declaration it is.
    by_decl = {article.decls[0]: article for article in articles if article.decls}
    for article in articles:
        for name in article.decls:
            by_decl.setdefault(name, article)
    nodes = sorted((article for article in articles if article.decls), key=sort_key)
    stmt: dict[Article, set[Article]] = {article: set() for article in nodes}
    proof: dict[Article, set[Article]] = {article: set() for article in nodes}
    for article in nodes:
        for name in article.decls:
            record = concepts.get(name) or {}
            stmt[article].update(by_decl[other] for other in record.get("statement", []) if other in by_decl)
            proof[article].update(by_decl[other] for other in record.get("proof", []) if other in by_decl)
        stmt[article].discard(article)
        proof[article].discard(article)
        proof[article] -= stmt[article]
        stats["statement_raw"] += len(stmt[article])
        stats["proof_raw"] += len(proof[article])

    informal: dict[Article, set[Article]] = defaultdict(set)
    state: dict[Article, int] = {}
    for root in nodes:
        if root in state:
            continue
        state[root] = 1
        stack = [(root, iter(sorted(stmt[root] | proof[root], key=sort_key)))]
        while stack:
            node, children = stack[-1]
            child = next(children, None)
            if child is None:
                state[node] = 2
                stack.pop()
                continue
            if state.get(child) == 1:
                stmt[node].discard(child)
                proof[node].discard(child)
                informal[node].add(child)
                stats["informal"] += 1
            elif child not in state:
                state[child] = 1
                stack.append((child, iter(sorted(stmt[child] | proof[child], key=sort_key))))

    index = {article: number for number, article in enumerate(nodes)}
    reach_stmt: dict[Article, int] = {}
    reach_all: dict[Article, int] = {}
    order: list[Article] = []
    done: set[Article] = set()
    for root in nodes:
        stack = [(root, False)]
        while stack:
            node, expanded = stack.pop()
            if node in done:
                continue
            if expanded:
                done.add(node)
                order.append(node)
                continue
            stack.append((node, True))
            stack.extend((child, False) for child in sorted(stmt[node] | proof[node], key=sort_key) if child not in done)
    for node in order:
        statement_bits = all_bits = 0
        for child in stmt[node]:
            statement_bits |= (1 << index[child]) | reach_stmt[child]
        for child in stmt[node] | proof[node]:
            all_bits |= (1 << index[child]) | reach_all[child]
        reach_stmt[node], reach_all[node] = statement_bits, all_bits
    for node in nodes:
        keep_stmt = {
            child for child in stmt[node]
            if not any(other is not child and reach_stmt[other] >> index[child] & 1 for other in stmt[node])
        }
        both = stmt[node] | proof[node]
        keep_proof = {
            child for child in proof[node]
            if not any(other is not child and reach_all[other] >> index[child] & 1 for other in both)
        }
        node.leaf.depends = [child.leaf for child in sorted(keep_stmt, key=sort_key)]
        node.leaf.proof_depends = [child.leaf for child in sorted(keep_proof, key=sort_key)]
        node.leaf.informal = [child.leaf for child in sorted(informal[node], key=sort_key)]
        stats["statement"] += len(keep_stmt)
        stats["proof"] += len(keep_proof)
    return stats


def disambiguate(articles: list[Article]) -> None:
    """Add to each shared title the nearest section that tells its articles apart."""
    groups: dict[str, list[Article]] = defaultdict(list)
    for article in articles:
        groups[title_key(article.leaf.title)].append(article)
    for group in groups.values():
        if len(group) < 2:
            continue
        contexts = [(LIST_TITLES[article.home.list], *article.home.path) for article in group]
        for depth in range(1, max(map(len, contexts)) + 1):
            names = [context[-min(depth, len(context))] for context in contexts]
            if len(set(names)) == len(names):
                for article, name in zip(group, names):
                    article.leaf.title = f"{article.leaf.title} ({name})"
                break


def citation_urls(sources: Sources, authored: dict[str, Authored]) -> dict[str, str]:
    """Each cited name's documentation page, from the module the dump's cited section gives it.
    A name with no record there, or one Mathlib deprecates, stops the chapter rather than publish
    a citation that leads nowhere: the Mathlib data workflow reads every cited name, and on a pull
    request its patch brings the records of new ones."""
    deps = sources.deps or {}
    records, unresolved = deps.get("cited") or {}, set(deps.get("unresolved") or [])
    urls, problems = {}, []
    for article in authored.values():
        for match in LEAN_LINK.finditer(article.body):
            name = unquote(match.group(1) or match.group(2))
            record = records.get(name)
            if record is None:
                problems.append(f"{article.path} cites {name}, which "
                                + ("Mathlib does not have at this pin" if name in unresolved else
                                   "the Mathlib data have no record of yet: apply the Mathlib data workflow's patch"))
            elif record.get("deprecated") is not None:
                replacement = record["deprecated"].get("replacement")
                problems.append(f"{article.path} cites {name}, which Mathlib deprecates"
                                + (f"; cite {replacement}" if replacement else ""))
            else:
                urls[name] = doc_url(name, record.get("module"))
    if problems:
        raise ValueError("citations that cannot be linked:\n" + "\n".join(dict.fromkeys(problems)))
    return urls


def apply_authored(articles: list[Article], authored: dict[str, Authored], urls: dict[str, str],
                   targets: dict[str, Leaf | Container]) -> int:
    """Put each authored article in place of its concept's generated text and dependencies."""
    count = 0
    for article in articles:
        written = authored.get(concept_key(article))
        if written is None:
            continue
        leaf = article.leaf
        leaf.body = link_citations(written.body, urls)
        leaf.fields = [("article_id", written.article_id), *leaf.fields]
        for attribute in ("depends", "proof_depends"):
            keys = getattr(written, attribute)
            unknown = [key for key in keys if not isinstance(targets.get(key), Leaf)]
            if unknown:
                raise ValueError(f"{written.path}: no article for {', '.join(unknown)}")
            setattr(leaf, attribute, [targets[key] for key in keys])
        leaf.informal = []
        leaf.no_depends = "Its article names no prerequisites."
        count += 1
    if count:
        check_acyclic([article.leaf for article in articles])
    return count


def check_acyclic(leaves: list[Leaf]) -> None:
    """Stop if prerequisites close a cycle. Lean's edges alone close none (link_edges), so an
    authored article's list is in any cycle found."""
    state: dict[int, int] = {}
    for root in leaves:
        if id(root) in state:
            continue
        state[id(root)] = 1
        path = [root]
        stack = [iter(root.depends + root.proof_depends)]
        while stack:
            child = next(stack[-1], None)
            if child is None:
                state[id(path.pop())] = 2
                stack.pop()
            elif state.get(id(child)) == 1:
                cycle = path[path.index(child):] + [child]
                raise ValueError("prerequisites close a cycle: " + " -> ".join(leaf.title for leaf in cycle))
            elif id(child) not in state:
                state[id(child)] = 1
                path.append(child)
                stack.append(iter(child.depends + child.proof_depends))


def chapter(sources: Sources, authored: dict[str, Authored] | None = None
            ) -> tuple[Container, dict[str, int], dict[str, Leaf | Container]]:
    """The chapter, its numbers, and the pages a trough: link can name: every concept by its
    key, and each overview section as "area:<headings>"."""
    authored = authored or {}
    articles = merge(sources.lists)
    claimed = frozenset(concept_names(articles))
    for article in articles:
        article.leaf = build_leaf(sources, article, claimed)
    disambiguate(articles)
    articles_by_item = {id(item): article for article in articles for item in article.items}
    edge_stats = link_edges(sources, articles)
    targets: dict[str, Leaf | Container] = {concept_key(article): article.leaf for article in articles}
    known = set(targets) | {key for key in authored if key.startswith("area:")}
    stray = sorted(key for key in authored if key not in known)
    if stray:
        raise ValueError(f"authored articles about no concept of this chapter: "
                         f"{', '.join(str(authored[key].path) for key in stray)}")
    urls = citation_urls(sources, authored)
    written = apply_authored(articles, authored, urls, targets)
    areas = {tuple(key.removeprefix("area:").split("/")): link_citations(article.body, urls)
             for key, article in authored.items() if key.startswith("area:")}
    formalized = sum(article.kind != "wanted" for article in articles)
    wanted = len(articles) - formalized
    rev_link = f"[{sources.rev[:8]}]({MATHLIB_REPO}/tree/{sources.rev})"
    date = f" ({sources.date[:10]})" if sources.date else ""
    if sources.deps:
        edges = (
            f"An article's *Depends on* list names the nearest concepts on these lists that its "
            f"statement uses, and *Proof depends on* those its proof uses, counting its helper lemmas in "
            f"the same Mathlib file and, for a lemma from another file, the listed theorems it is proved "
            f"from there. Both are read from Mathlib's declaration graph by `lean/ConceptDeps.lean` in GitHub Actions; a "
            f"dependency already reached through another is left out. This leaves {edge_stats['statement']:,} statement and "
            f"{edge_stats['proof']:,} proof edges, from {edge_stats['statement_raw']:,} and "
            f"{edge_stats['proof_raw']:,} nearest-concept edges"
            + (f"; {edge_stats['informal']} edges that would close a cycle are listed as *Informally uses*." if edge_stats["informal"] else ".")
        )
    else:
        edges = "Dependency edges come from a GitHub Actions run over Mathlib's declaration graph, which has not reached this page yet."
    prose = "\n\n".join(
        [
            "Mathlib's maintainers keep four curated lists of what the library contains: an overview of its "
            "main concepts, an undergraduate curriculum, Freek Wiedijk's 100 theorems, and the theorems of "
            "the 1000+ theorems project. This chapter has one article per concept on those lists, read at "
            f"Mathlib commit {rev_link}{date}: {len(articles):,} articles, {formalized:,} of them in Mathlib "
            f"and {wanted:,} not yet.",
            "Items that name the same declarations in several lists, or name none and share a title, are one "
            "article, placed in the first list that has it; the other lists link to it. An article in Mathlib names its declarations, "
            "with their documentation and source. One that Mathlib lacks is marked not ready, since its "
            "prerequisites are not mapped; its page says when Mathlib states it without a proof or another "
            "project has formalized it.",
            edges,
        ]
        + ([f"{written:,} {'article is' if written == 1 else 'articles are'} written for this wiki: original text, "
            "whose citations link to Mathlib's documentation, and prerequisites chosen for the reader."]
           if written else [])
    )
    root = Container("Mathlib", "mathlib", prose=prose)
    root.entries = [
        Entry(tree_container(sources, "overview", articles_by_item, areas, targets)),
        Entry(tree_container(sources, "undergrad", articles_by_item)),
        Entry(hundred_container(sources, articles_by_item)),
        Entry(thousand_container(sources, articles_by_item)),
    ]
    unplaced = sorted(f"area:{'/'.join(path)}" for path in areas if "area:" + "/".join(path) not in targets)
    if unplaced:
        raise ValueError(f"authored area pages for no section of the overview: {', '.join(unplaced)}")
    for article in authored.values():
        unknown = [key for key in linked(article) if key not in targets]
        if unknown:
            raise ValueError(f"{article.path}: no article for {', '.join(dict.fromkeys(unknown))}")
    stats = dict(edge_stats, articles=len(articles), formalized=formalized, wanted=wanted, authored=written)
    return root, stats, targets
