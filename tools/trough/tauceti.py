"""The Tau Ceti chapter: one article per declaration a roadmap's status names, as Tau Ceti has it.

Tau Ceti's roadmaps (TauCetiRoadmap) each carry a generated STATUS.md whose
"Named results" and "Notable definitions and infrastructure" link declarations
in Tau Ceti's documentation. Those links pick what the chapter maps; the rest of
the roadmap, its plan, its suggested signatures and its frontier, is what the
library may add, so it is left out. Each article's text is its declaration's
docstring and signature, read at the pinned Tau Ceti commit by
lean/tauceti/TauCetiDeps.lean, which also gives the edges.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, unquote

from .blueprints import break_cycles, escape
from .mathlib import fence, title_key
from .vault import Container, Entry, Leaf, chunk, safe_math_markdown, slugify

ROADMAPS_SCHEMA = "trough-tauceti-roadmaps/v1"
ROADMAP_REPO = "TauCetiProject/TauCetiRoadmap"
SECTIONS = ("Named results", "Notable definitions and infrastructure")
# Tau Ceti's documentation has lived at both hosts; a declaration's anchor is its full name.
DOC_LINK = re.compile(
    r"\]\(https://(?:taucetiproject\.org|taucetiproject\.github\.io/TauCeti)/docs/[^)#\s]*\.html#([^)\s]+)\)"
)
TITLE = re.compile(r"^# +(?:Roadmap: *)?(.+?)\s*$", re.M)


def status_names(status: str) -> list[str]:
    """The declarations a STATUS.md links under its named results and notable definitions, in order."""
    names: list[str] = []
    for section in re.split(r"(?m)^(?=#{2,3} )", status):
        heading = section.split("\n", 1)[0].lstrip("#").strip()
        if heading in SECTIONS:
            names += [unquote(anchor) for anchor in DOC_LINK.findall(section)]
    return list(dict.fromkeys(names))


def roadmap_title(readme: str, fallback: str) -> str:
    match = TITLE.search(readme)
    if not match:
        return fallback
    title = match.group(1)
    return title[:1].upper() + title[1:]


def read_roadmaps(checkout: Path) -> list[dict]:
    """Each roadmap with a STATUS.md that names a declaration, by path in the checkout."""
    roadmaps = []
    for status in sorted(checkout.glob("*/*/STATUS.md")):
        directory = status.parent
        names = status_names(status.read_text(encoding="utf-8"))
        if not names:
            continue
        readme = directory / "README.md"
        text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
        roadmaps.append({
            "id": directory.name,
            "path": directory.relative_to(checkout).as_posix(),
            "title": roadmap_title(text, directory.name),
            "names": names,
        })
    return roadmaps


TAUCETI_REPO = "https://github.com/TauCetiProject/TauCeti"
DOCS = "https://taucetiproject.org/docs"
KIND_COMMANDS = {"constructor": "def", "recursor": "def", "quot": "def"}
LEAD = re.compile(r"^\s*\*\*(?P<title>[^*\n]+?)[.:]?\*\*[.:]?\s*")


@dataclass
class Sources:
    rev: str
    date: str
    roadmap_rev: str
    roadmaps: list[dict]
    deps: dict | None  # lean/tauceti/TauCetiDeps.lean's dump, once the data workflow has run


def load_sources(data: Path) -> Sources | None:
    """The Tau Ceti data under data/tauceti/, or None before the first refresh."""
    directory = data / "tauceti"
    if not (directory / "roadmaps.json").is_file() or not (directory / "source.json").is_file():
        return None
    source = json.loads((directory / "source.json").read_text(encoding="utf-8"))
    roadmaps = json.loads((directory / "roadmaps.json").read_text(encoding="utf-8"))
    deps_path = directory / "deps.json"
    deps = json.loads(deps_path.read_text(encoding="utf-8")) if deps_path.is_file() else None
    return Sources(source["rev"], source.get("date", ""), roadmaps["rev"], roadmaps["roadmaps"], deps)


def doc_url(name: str, module: str) -> str:
    anchor = quote(name, safe=".'_-!?«»")
    return f"{DOCS}/{module.replace('.', '/')}.html#{anchor}"


def source_url(rev: str, module: str, line: int | None) -> str:
    return f"{TAUCETI_REPO}/blob/{rev}/{module.replace('.', '/')}.lean" + (f"#L{line}" if line else "")


def clean_doc(doc: str) -> str:
    """A docstring as article prose: headings become bold lines, and the citations doc-gen4
    reads, [Name](key) and [key2024], link to Tau Ceti's bibliography."""
    lines = []
    for line in doc.strip().splitlines():
        heading = re.match(r"^\s*#+\s+(.*)$", line)
        lines.append(f"**{heading.group(1).strip()}**" if heading else line.rstrip())
    text = "\n".join(lines).strip()
    text = re.sub(r"\]\(([A-Za-z][\w-]*)\)", rf"]({DOCS}/references.html#ref_\1)", text)
    text = re.sub(r"(?<![\]\w])\[([A-Za-z]+\d{4}[a-z]?)\](?![(\[])", rf"[\1]({DOCS}/references.html#ref_\1)", text)
    return safe_math_markdown(text)


def title_and_text(name: str, doc: str | None) -> tuple[str, str]:
    """A declaration's title, its docstring's bold lead if it opens with one, else its name; and the
    rest of the docstring."""
    doc = (doc or "").strip()
    lead = LEAD.match(doc)
    if lead:
        return lead.group("title").strip(), doc[lead.end():].strip()
    return name, doc


def build_leaf(sources: Sources, name: str, record: dict, homes: list[dict]) -> Leaf:
    title, text = title_and_text(name, record.get("doc"))
    kind = KIND_COMMANDS.get(record["kind"], record["kind"])
    fields = [("declaration", kind), ("origin", "cited"), ("lean", name), ("statement", "formalized")]
    if kind == "theorem" and not record.get("sorry"):
        fields.append(("proof", "formalized"))
    body = [clean_doc(text)] if text else []
    if record.get("signature"):
        body.append(fence(record["signature"]))
    url = doc_url(name, record["module"])
    if kind == "theorem" and record.get("sorry"):
        lean = f"Tau Ceti states this as [`{name}`]({url}); its proof uses `sorry`."
    else:
        lean = f"Formalized in Tau Ceti as [`{name}`]({url})."
    leaf = Leaf(escape(title) if title == name else safe_math_markdown(title), slugify(title), fields,
                "\n\n".join(body) or f"Tau Ceti gives `{name}` no docstring.", notes=[("Lean", lean)])
    leaf.sources = [
        (f"Tau Ceti documentation: `{name}`", url),
        (f"Source of `{name}` in {record['module'].replace('.', '/')}.lean",
         source_url(sources.rev, record["module"], record.get("line"))),
    ] + [(f"Tau Ceti roadmap status: {roadmap['title']}",
          f"https://github.com/{ROADMAP_REPO}/blob/{sources.roadmap_rev}/{roadmap['path']}/STATUS.md")
         for roadmap in homes]
    leaf.no_depends = "Its statement uses no other declaration mapped here."
    return leaf


def chapter(sources: Sources) -> tuple[Container, dict[str, int], dict[str, str]]:
    """The chapter's root, its counts, and each mapped name's documentation page (for
    hooks/lean-links.json). A declaration named by several roadmaps lives in the first by title
    and is listed in the others."""
    records = (sources.deps or {}).get("declarations", {})
    homes: dict[str, list[dict]] = defaultdict(list)
    for roadmap in sources.roadmaps:
        for name in roadmap["names"]:
            if name in records:
                homes[name].append(roadmap)
    leaves: dict[str, Leaf] = {}
    sections: list[Entry] = []
    stats: dict[str, int] = defaultdict(int)
    tree = f"{TAUCETI_REPO}/tree/{sources.rev}"
    for roadmap in sorted(sources.roadmaps, key=lambda roadmap: title_key(roadmap["title"])):
        names = [name for name in roadmap["names"] if name in records]
        if not names:
            stats["roadmaps_left_out"] += 1
            continue
        title = safe_math_markdown(roadmap["title"])
        section = Container(title, slugify(roadmap["title"]))
        readme = f"https://github.com/{ROADMAP_REPO}/blob/{sources.roadmap_rev}/{roadmap['path']}/README.md"
        section.prose = (f"The declarations the status of Tau Ceti's [roadmap]({readme}) names, as Tau Ceti has "
                         f"them at commit [{sources.rev[:8]}]({tree}).")
        for name in names:
            if name in leaves:
                section.entries.append(Entry(leaves[name], owned=False))
                continue
            leaves[name] = build_leaf(sources, name, records[name], homes[name])
            section.entries.append(Entry(leaves[name]))
        sections.append(Entry(chunk(section)))
    for name, leaf in leaves.items():
        record = records[name]
        leaf.depends = sorted({leaves[other] for other in record.get("statement", []) if other in leaves and other != name},
                              key=lambda node: title_key(node.title))
        leaf.proof_depends = sorted({leaves[other] for other in record.get("proof", [])
                                     if other in leaves and other != name and leaves[other] not in leaf.depends},
                                    key=lambda node: title_key(node.title))
        stats["statement_edges"] += len(leaf.depends)
        stats["proof_edges"] += len(leaf.proof_depends)
        kind = dict(leaf.fields)["declaration"]
        stats["theorems" if kind == "theorem" else "definitions"] += 1
        stats["sorry"] += bool(kind == "theorem" and record.get("sorry"))
    stats["cycles"] = break_cycles(list(leaves.values()))
    stats["articles"] = len(leaves)
    stats["roadmaps"] = len(sections)
    stats["missing"] = len({name for roadmap in sources.roadmaps for name in roadmap["names"]} - records.keys())
    root = Container("Tau Ceti", "tauceti", sections)
    root.prose = intro(sources, stats)
    chunk(root)
    links = {name: doc_url(name, records[name]["module"]) for name in leaves}
    return root, dict(stats), links


def intro(sources: Sources, stats: dict[str, int]) -> str:
    rev = f"[{sources.rev[:8]}]({TAUCETI_REPO}/tree/{sources.rev})"
    date = f" ({sources.date[:10]})" if sources.date else ""
    roadmaps = f"[{sources.roadmap_rev[:8]}](https://github.com/{ROADMAP_REPO}/tree/{sources.roadmap_rev})"
    missing = stats["missing"]
    return "\n\n".join([
        f"[Tau Ceti](https://taucetiproject.org/), read at commit {rev}{date}, with its roadmaps at {roadmaps}: one "
        f"article for each of the {stats['articles']:,} declarations that a roadmap's status names as a result or a "
        f"notable definition, in a section for each of the {stats['roadmaps']} roadmaps that name one. "
        + ("The one name the statuses give that Tau Ceti does not have at this commit has no article. " if missing == 1
           else f"The {missing} names the statuses give that Tau Ceti does not have at this commit have no article. "
           if missing else "")
        + "A roadmap's plan, its suggested signatures and its frontier say what Tau Ceti may add, so they are left "
        "out, and so is the statuses' prose: a model writes it, and Tau Ceti does not check it.",
        "Each article's text is its declaration's docstring and signature, under Tau Ceti's Apache-2.0 license; a "
        "docstring that opens with a bold title gives the article its title. Dependencies come from Tau Ceti's "
        "declarations (`lean/tauceti/TauCetiDeps.lean`): under *Depends on*, the declarations mapped here that a "
        "statement reaches through the statements of declarations not mapped here, and under *Proof depends on*, "
        "those a proof reaches through any chain of Tau Ceti declarations not mapped here. A theorem whose proof "
        "reaches `sorry` is shown as stated, not proved.",
    ])
