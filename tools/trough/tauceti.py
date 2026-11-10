"""The Tau Ceti chapter: the declarations its roadmaps' statuses name and the results its docstrings name.

Tau Ceti's roadmaps (TauCetiRoadmap) each carry a generated STATUS.md whose
"Named results" and "Notable definitions and infrastructure" link declarations
in Tau Ceti's documentation. A model writes those files and names at most five
results in each, so the chapter also maps the declarations whose docstrings name
a result (tools/trough/tauceti_select.py chooses them), with the forms of one
result in one article. The rest of a roadmap, its plan, its suggested signatures
and its frontier, is what the library may add, so it is left out. Each article's
text is its declaration's docstring and signature, read at the pinned Tau Ceti
commit by lean/tauceti/TauCetiDeps.lean, which also gives the edges. Parts follow
the library's top-level areas; a roadmap's section holds what its status names
and the named results in the modules it alone claims, and an area's section the
rest.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, unquote

from . import tauceti_select
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
    # A title opening on a variable, "p-adic measures", keeps its case.
    return title if re.match(r"[a-z](?![a-z])", title) else title[:1].upper() + title[1:]


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
# A bold opening is a title when it is a whole sentence: a period or colon ends it, inside the bold
# or just after. It may wrap a line, and hold a lone "*" ("Weak-* compactness").
LEAD = re.compile(r"^\s*\*\*(?P<title>(?:[^*\n]|\n(?!\s*\n)|\*(?!\*))+?)(?:[.:]\*\*|\*\*[.:])\s*")
# How far past a bold opening the period or colon that ends its sentence may be, and how much of
# that sentence a title takes.
SENTENCE = 200
CONTINUATION = 60


# An area with fewer articles joins its part's "Other results", and a part with fewer joins
# "Other Areas". A folder of modules below the areas goes to the one roadmap whose status names at
# least FOLDER_MIN declarations there.
AREA_MIN = 3
PART_MIN = 10
FOLDER_MIN = 2


@dataclass
class Sources:
    rev: str
    date: str
    roadmap_rev: str
    roadmaps: list[dict]
    deps: dict | None  # lean/tauceti/TauCetiDeps.lean's dump, once the data workflow has run
    selection: dict | None = None  # tools/select_tauceti.py's choice, once the data workflow has run


def load_sources(data: Path) -> Sources | None:
    """The Tau Ceti data under data/tauceti/, or None before the first refresh."""
    directory = data / "tauceti"
    if not (directory / "roadmaps.json").is_file() or not (directory / "source.json").is_file():
        return None
    source = json.loads((directory / "source.json").read_text(encoding="utf-8"))
    roadmaps = json.loads((directory / "roadmaps.json").read_text(encoding="utf-8"))
    deps_path = directory / "deps.json"
    deps = json.loads(deps_path.read_text(encoding="utf-8")) if deps_path.is_file() else None
    selection_path = directory / "selection.json"
    selection = json.loads(selection_path.read_text(encoding="utf-8")) if selection_path.is_file() else None
    return Sources(source["rev"], source.get("date", ""), roadmaps["rev"], roadmaps["roadmaps"], deps, selection)


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


def sentence_end(doc: str, start: int) -> int | None:
    """Where the sentence a bold opening begins ends: the first period or colon from *start* that
    is outside code, math and brackets and is followed by a space or the end, before a blank line
    and within SENTENCE characters."""
    depth, code, math = 0, False, False
    for i in range(start, min(len(doc), start + SENTENCE)):
        char = doc[i]
        if char == "`":
            code = not code
        elif code:
            continue
        elif char == "$":
            math = not math
        elif math:
            continue
        elif char in "([":
            depth += 1
        elif char in ")]":
            depth = max(0, depth - 1)
        elif char == "\n" and re.match(r"\n[ \t]*\n", doc[i:]):
            return None
        elif char in ".:" and depth == 0 and (i + 1 == len(doc) or doc[i + 1].isspace()):
            return i
    return None


def title_and_text(name: str, doc: str | None) -> tuple[str, str]:
    """A declaration's title and the rest of its docstring. A docstring that opens with a bold
    sentence ("**The density theorem.**") is titled by it; one that opens with bold words the
    sentence goes on from ("**Young's inequality** for an `L¹` kernel: ...") by the whole sentence,
    or by the bold words alone, above the whole docstring, when the rest of the sentence is long or
    holds a link; any other by the declaration's name."""
    doc = (doc or "").strip()
    lead = LEAD.match(doc)
    if lead:
        return " ".join(lead.group("title").split()), doc[lead.end():].strip()
    bold = tauceti_select.BOLD.match(doc)
    end = sentence_end(doc, bold.end()) if bold else None
    if bold and end is not None:
        rest = doc[bold.end():end]
        if len(rest) > CONTINUATION or "](" in rest:
            return " ".join(bold.group("title").split()).rstrip(".:,;"), doc
        return " ".join((bold.group("title") + rest).split()), doc[end + 1:].strip()
    return name, doc


# Module names that do not read as words when split.
AREA_TITLES = {"MvPolynomial": "Multivariate Polynomials", "KrullSchmidt": "Krull–Schmidt", "Perm": "Permutations"}


def area_title(word: str) -> str:
    """A module name as words, each as written: "NumberTheory" reads "Number Theory", "PDE" stays."""
    if word in AREA_TITLES:
        return AREA_TITLES[word]
    return " ".join(re.findall(r"[A-Z]+\d*(?![a-z])|[A-Z]?[a-z]+\d*|\d+", word)) or word


def top(module: str) -> str:
    """The top-level area of a Tau Ceti module: "NumberTheory" for TauCeti.NumberTheory.Chebotarev."""
    parts = module.split(".")
    return parts[1] if len(parts) > 1 else ""


def area_of(module: str) -> tuple[str, str]:
    """The area of a Tau Ceti module, its first two levels under TauCeti: ("NumberTheory",
    "Chebotarev") for TauCeti.NumberTheory.Chebotarev.Density."""
    parts = module.split(".")
    return (top(module), parts[2] if len(parts) > 2 else "")


def assumes(record: dict, statement: str) -> bool:
    """Whether a declaration's binders, after its name and before its signature's first top-level
    colon, mention a proposition by its full name or its last component."""
    _, _, binders = (record.get("signature") or "").strip().partition(" ")
    forms = "|".join(re.escape(form) for form in (statement, statement.rsplit(".", 1)[-1]))
    depth = 0
    for i, char in enumerate(binders):
        if char in "([{⦃⟨":
            depth += 1
        elif char in ")]}⦄⟩":
            depth -= 1
        elif char == ":" and depth == 0 and binders[i + 1:i + 2] != "=":
            return re.search(rf"(?<![\w.])(?:{forms})(?![\w.])", binders[:i]) is not None
    return False


def lean_line(name: str, record: dict, uses_sorry: bool, assumed: dict | None) -> str:
    link = f"[`{name}`]({doc_url(name, record['module'])})"
    if assumed:
        statement = assumed["statement"]
        link += f", assuming [`{statement}`]({doc_url(statement, assumed['module'])}), a proposition Tau Ceti defines"
    if uses_sorry:
        what = "proof" if KIND_COMMANDS.get(record["kind"], record["kind"]) == "theorem" else "definition"
        return f"Tau Ceti states this as {link}; its {what} reaches `sorry`."
    return f"Formalized in Tau Ceti as {link}."


def other_forms(names: list[str], records: dict[str, dict], incomplete: set[str], assumed: dict[str, dict]) -> str:
    """The other forms of an article's result: each one's title, Lean line and signature."""
    blocks = []
    for name in names:
        record = records[name]
        title, _ = title_and_text(name, record.get("doc"))
        shown = escape(name) if title == name else safe_math_markdown(title)
        blocks.append(f"**{shown}.** {lean_line(name, record, name in incomplete, assumed.get(name))}")
        if record.get("signature"):
            blocks.append(fence(record["signature"]))
    return "\n\n".join(blocks)


def build_leaf(sources: Sources, members: list[str], records: dict[str, dict], homes: list[dict], title: str,
               text: str, incomplete: set[str], assumed: dict[str, dict]) -> Leaf:
    """An article on its lead declaration, members[0], and the other forms of its result. *title* is
    Markdown; a declaration in *incomplete* reaches `sorry`, itself or through a declaration mapped
    here."""
    lead = members[0]
    record = records[lead]
    kind = KIND_COMMANDS.get(record["kind"], record["kind"])
    fields = [("declaration", kind), ("origin", "cited"), ("lean", ", ".join(members)), ("statement", "formalized")]
    if kind == "theorem" and lead not in incomplete:
        fields.append(("proof", "formalized"))
    body = [clean_doc(text)] if text else []
    if record.get("signature"):
        body.append(fence(record["signature"]))
    notes = [("Lean", lean_line(lead, record, lead in incomplete, assumed.get(lead)))]
    if len(members) > 1:
        notes.append(("Other forms", other_forms(members[1:], records, incomplete, assumed)))
    leaf = Leaf(title, slugify(title), fields, "\n\n".join(body) or f"Tau Ceti gives `{lead}` no docstring.", notes=notes)
    url = doc_url(lead, record["module"])
    leaf.sources = [
        (f"Tau Ceti documentation: `{lead}`", url),
        (f"Source of `{lead}` in {record['module'].replace('.', '/')}.lean",
         source_url(sources.rev, record["module"], record.get("line"))),
    ] + [(f"Tau Ceti roadmap status: {roadmap['title']}",
          f"https://github.com/{ROADMAP_REPO}/blob/{sources.roadmap_rev}/{roadmap['path']}/STATUS.md")
         for roadmap in homes]
    leaf.no_depends = "Its statement uses no other declaration mapped here."
    return leaf


def gather(names: list[str], records: dict[str, dict], named: set[str]) -> list[list[str]]:
    """The articles, each a list of declarations with its lead first. Forms of one result in one
    area share an article (tauceti_select.group_key, with the possessives the mapped docstrings
    write). A declaration a status names leads its own article, and each form no status names joins
    the one whose title shares the most words with its own. Otherwise the lead is a form Tau Ceti's
    website shows, else a form not titled by names alone ("Perron–Frobenius"), then the form titled
    by the result's name alone, else the one with the shortest title that is not a Lean name. A
    definition a status names stands alone."""
    titles = {name: tauceti_select.title(records[name].get("doc")) for name in names}
    possessives = tauceti_select.possessive_names([{"d": records[name].get("doc")} for name in names])
    groups: dict[tuple[str, tuple[str, str]], list[str]] = defaultdict(list)
    articles: list[list[str]] = []
    for name in names:
        if titles[name] and (records[name]["kind"] == "theorem" or name not in named):
            groups[(tauceti_select.group_key(titles[name], possessives), area_of(records[name]["module"]))].append(name)
        else:
            articles.append([name])
    for (key, _), members in sorted(groups.items()):
        order = sorted(members, key=lambda name: (title_key(titles[name]), name))
        leads = [name for name in order if name in named]
        rest = [name for name in order if name not in named]
        if leads:
            words = {name: set(re.findall(r"\w+", titles[name].casefold())) for name in members}
            forms: dict[str, list[str]] = {lead: [] for lead in leads}
            for name in rest:
                forms[max(leads, key=lambda lead: len(words[lead] & words[name]))].append(name)
            articles += [[lead, *forms[lead]] for lead in leads]
        else:
            shown = {name: title_and_text(name, records[name].get("doc"))[0] for name in rest}
            lead = min(rest, key=lambda name: (name not in tauceti_select.SHOWCASE, names_only(shown[name]),
                                               not tauceti_select.plain_title(shown[name], key), shown[name] == name,
                                               len(shown[name]), name))
            articles.append([lead, *(name for name in rest if name != lead)])
    return articles


def names_only(title: str) -> bool:
    """Whether a title is names joined by dashes and nothing more ("Perron–Frobenius")."""
    match = tauceti_select.JOINED.match(title)
    return bool(match) and match.end() == len(title)


def claims(roadmaps: list[dict], records: dict[str, dict]) -> tuple[dict[str, Counter], dict[str, Counter]]:
    """For each module, and each folder of modules, how many declarations each roadmap's status names
    there."""
    modules: dict[str, Counter] = defaultdict(Counter)
    folders: dict[str, Counter] = defaultdict(Counter)
    for roadmap in roadmaps:
        for name in roadmap["names"]:
            if name in records:
                module = records[name]["module"]
                modules[module][roadmap["path"]] += 1
                folders[module.rsplit(".", 1)[0]][roadmap["path"]] += 1
    return modules, folders


def place(module: str, modules: dict[str, Counter], folders: dict[str, Counter]) -> str | tuple[str, str]:
    """Where a result no status names goes: the roadmap whose status names a declaration in its
    module, when that is one roadmap; else, for a folder of modules below the areas, the one
    roadmap whose status names declarations there, at least FOLDER_MIN of them; else its area."""
    claim = modules.get(module)
    if claim:
        return next(iter(claim)) if len(claim) == 1 else area_of(module)
    folder = module.rsplit(".", 1)[0]
    claim = folders.get(folder)
    if claim and folder.count(".") >= 3 and len(claim) == 1 and sum(claim.values()) >= FOLDER_MIN:
        return next(iter(claim))
    return area_of(module)


def chapter(sources: Sources) -> tuple[Container, dict[str, int], dict[str, str]]:
    """The chapter's root, its counts, and each mapped name's documentation page (for
    hooks/lean-links.json). A declaration named by several roadmaps lives in the first by title
    and is listed in the others."""
    # Only declarations in Tau Ceti's own modules: a status may link a name that now lives in Mathlib.
    records = {name: record for name, record in (sources.deps or {}).get("declarations", {}).items()
               if (record.get("module") or "").split(".")[0] == "TauCeti"}
    incomplete = reaching_sorry(records)
    roadmaps = sorted(sources.roadmaps, key=lambda roadmap: title_key(roadmap["title"]))
    named = {name for roadmap in roadmaps for name in roadmap["names"] if name in records}
    selection = sources.selection or {}
    chosen = {name for name in selection.get("chosen", {}) if name in records}
    assumed = {name: entry for name, entry in selection.get("assuming", {}).items()
               if name in records and assumes(records[name], entry["statement"])}
    homes: dict[str, list[dict]] = defaultdict(list)
    for roadmap in sources.roadmaps:
        for name in roadmap["names"]:
            if name in records:
                homes[name].append(roadmap)
    first: dict[str, str] = {}
    for roadmap in roadmaps:
        for name in roadmap["names"]:
            first.setdefault(name, roadmap["path"])
    articles = gather(sorted(named | chosen), records, named)
    article_of = {member: members[0] for members in articles for member in members}
    titles = display_titles(records, {members[0] for members in articles})
    leaves = {members[0]: build_leaf(sources, members, records, homes[members[0]], *titles[members[0]], incomplete,
                                     assumed) for members in articles}
    modules, folders = claims(roadmaps, records)
    added: dict[str | tuple[str, str], list[str]] = defaultdict(list)
    for members in articles:
        lead = members[0]
        if lead not in named:
            added[place(records[lead]["module"], modules, folders)].append(lead)
    for leads in added.values():
        leads.sort(key=lambda lead: (title_key(leaves[lead].title), lead))
    stats: dict[str, int] = defaultdict(int)
    tree = f"{TAUCETI_REPO}/tree/{sources.rev}"
    at = f"as Tau Ceti has them at commit [{sources.rev[:8]}]({tree})"
    sections: dict[str, list[tuple[Container, Counter]]] = defaultdict(list)
    for roadmap in roadmaps:
        names = [name for name in roadmap["names"] if name in records]
        if not names:
            stats["roadmaps_left_out"] += 1
            continue
        section = Container(safe_math_markdown(roadmap["title"]), slugify(roadmap["title"]))
        readme = f"https://github.com/{ROADMAP_REPO}/blob/{sources.roadmap_rev}/{roadmap['path']}/README.md"
        more = added.pop(roadmap["path"], [])
        section.prose = (f"The declarations the status of Tau Ceti's [roadmap]({readme}) names"
                         + (", and the other results named in the modules where only this status names declarations, "
                            f"or in folders below the areas where only it names {FOLDER_MIN} or more," if more else "")
                         + f" {at}.")
        areas: Counter = Counter()
        for name in names:
            owned = first[name] == roadmap["path"]
            section.entries.append(Entry(leaves[name], owned=owned))
            areas[top(records[name]["module"])] += 2 if owned else 1
        for lead in more:
            section.entries.append(Entry(leaves[lead]))
            areas[top(records[lead]["module"])] += 2
        sections[min(areas, key=lambda area: (-areas[area], area))].append((section, Counter()))
    others: dict[str, list[str]] = defaultdict(list)
    for (area, sub), leads in sorted((key, leads) for key, leads in added.items() if isinstance(key, tuple)):
        if not sub or len(leads) < AREA_MIN:
            others[area] += leads
            continue
        section = Container(area_title(sub), slugify(area_title(sub)))
        section.prose = f"Results named in Tau Ceti's `TauCeti.{area}.{sub}` modules and in no roadmap's section, {at}."
        section.entries = [Entry(leaves[lead]) for lead in leads]
        sections[area].append((section, Counter(area=1)))
    for area, leads in sorted(others.items()):
        section = Container("Other results", "other-results")
        section.prose = f"Results named in the rest of Tau Ceti's `TauCeti.{area}` modules and in no roadmap's section, {at}."
        section.entries = [Entry(leaves[lead]) for lead in sorted(leads, key=lambda lead: (title_key(leaves[lead].title), lead))]
        sections[area].append((section, Counter(other=1)))
    small: list[tuple[Container, Counter]] = []
    parts = []
    for area in sorted(sections, key=lambda area: title_key(area_title(area))):
        ordered = sorted(sections[area], key=lambda item: (item[1]["other"], item[1]["area"], title_key(item[0].title)))
        if sum(entry.owned for section, _ in ordered for entry in section.entries) < PART_MIN:
            # An area's own sections become one, titled by the area.
            rest = [entry for section, kind in ordered if kind for entry in section.entries]
            ordered = [item for item in ordered if not item[1]]
            if rest:
                section = Container(area_title(area), slugify(area_title(area)))
                section.prose = f"Results named in Tau Ceti's `TauCeti.{area}` modules and in no roadmap's section, {at}."
                section.entries = sorted(rest, key=lambda entry: (title_key(entry.node.title), entry.node.title))
                ordered.append((section, Counter(area=1)))
            small += ordered
        else:
            taken = {re.sub(r"s\b", "", title_key(section.title)) for section, kind in ordered if not kind}
            for section, kind in ordered:
                if kind["area"] and re.sub(r"s\b", "", title_key(section.title)) in taken:
                    section.title += ": other results"
            part = Container(area_title(area), slugify(area_title(area)))
            part.prose = (f"Results in Tau Ceti's `TauCeti.{area}` modules, and the roadmaps whose articles are mostly "
                          "there: by roadmap, then by area.")
            part.entries = [Entry(chunk(section)) for section, _ in ordered]
            parts.append(Entry(chunk(part)))
        stats["roadmaps"] += sum(1 for _, kind in ordered if not kind)
        stats["areas"] += sum(1 for _, kind in ordered if kind)
    if small:
        part = Container("Other Areas", "other-areas")
        part.prose = ("The areas of Tau Ceti with too few articles for a part of their own"
                      + (": by roadmap, then by area." if any(not kind for _, kind in small) else "."))
        part.entries = [Entry(chunk(section)) for section, kind in sorted(small, key=lambda item: (bool(item[1]),
                                                                                                   title_key(item[0].title)))]
        parts.append(Entry(chunk(part)))
    members_of = {members[0]: members for members in articles}
    for lead, leaf in leaves.items():
        members = members_of[lead]
        statement = {article_of[other] for member in members for other in records[member].get("statement", [])
                     if other in article_of} - {lead}
        proof = {article_of[other] for member in members for other in records[member].get("proof", [])
                 if other in article_of} - {lead} - statement
        leaf.depends = [leaves[other] for other in sorted(statement, key=lambda other: (title_key(leaves[other].title), other))]
        leaf.proof_depends = [leaves[other] for other in sorted(proof, key=lambda other: (title_key(leaves[other].title), other))]
        stats["statement_edges"] += len(leaf.depends)
        stats["proof_edges"] += len(leaf.proof_depends)
        stats["forms"] += len(members) > 1
    for name in article_of:
        stats["theorems" if KIND_COMMANDS.get(records[name]["kind"], records[name]["kind"]) == "theorem" else "definitions"] += 1
        stats["sorry"] += name in incomplete
    stats["cycles"] = break_cycles(list(leaves.values()))
    stats["articles"] = len(leaves)
    stats["declarations"] = len(article_of)
    stats["named"] = len(named)
    stats["chosen"] = len(chosen - named)
    stats["parts"] = len(parts)
    stats["missing"] = len({name for roadmap in sources.roadmaps for name in roadmap["names"]} - records.keys())
    root = Container("Tau Ceti", "tauceti", parts)
    root.prose = intro(sources, stats)
    chunk(root)
    links = {name: doc_url(name, records[name]["module"]) for name in sorted(article_of)}
    return root, dict(stats), links


def reaching_sorry(records: dict[str, dict]) -> set[str]:
    """The declarations that reach `sorry`: the dump's own mark stops at the next declaration mapped
    here, so a mark passes along the edges to what uses it."""
    marked = {name for name, record in records.items() if record.get("sorry")}
    changed = True
    while changed:
        changed = False
        for name, record in records.items():
            if name not in marked and marked & set(record.get("statement", []) + record.get("proof", [])):
                marked.add(name)
                changed = True
    return marked


def display_titles(records: dict[str, dict], named: set[str]) -> dict[str, tuple[str, str]]:
    """Each article's title as Markdown, and the rest of its lead's docstring. A title two articles
    share is followed by each one's name."""
    raw = {name: title_and_text(name, records[name].get("doc")) for name in sorted(named & records.keys())}
    counts = Counter(title for title, _ in raw.values())
    out = {}
    for name, (title, text) in raw.items():
        if title == name:
            out[name] = (escape(name), text)
        elif counts[title] > 1:
            out[name] = (f"{safe_math_markdown(title)} (`{name}`)", text)
        else:
            out[name] = (safe_math_markdown(title), text)
    return out


def intro(sources: Sources, stats: dict[str, int]) -> str:
    rev = f"[{sources.rev[:8]}]({TAUCETI_REPO}/tree/{sources.rev})"
    date = f" ({sources.date[:10]})" if sources.date else ""
    roadmaps = f"[{sources.roadmap_rev[:8]}](https://github.com/{ROADMAP_REPO}/tree/{sources.roadmap_rev})"
    missing = stats["missing"]
    return "\n\n".join([
        f"[Tau Ceti](https://taucetiproject.org/), read at commit {rev}{date}, with its roadmaps at {roadmaps}: "
        f"{stats['articles']:,} articles on {stats['declarations']:,} of its declarations, in parts by the library's "
        f"top-level areas. {stats['named']:,} are the declarations a roadmap's status names as a result or a "
        "notable definition. A model writes the statuses and names at most five results in each, so the other "
        f"{stats['chosen']:,} are results Tau Ceti's own docstrings name: a theorem whose docstring opens with a bold "
        "title naming a result after a person (\"Burnside's pᵃqᵇ theorem\", \"Schur-Weyl duality\", \"Hille–Yosida\"), "
        "a title such as "
        "\"The cellular approximation theorem\", or a short title pinned to a textbook theorem; a definition that "
        "carries such a theorem as data; and the four theorems Tau Ceti's website shows. The forms of one result in one "
        "area share an article. "
        + ("The one name the statuses give that Tau Ceti does not have at this commit has no article. " if missing == 1
           else f"The {missing} names the statuses give that Tau Ceti does not have at this commit have no article. "
           if missing else "")
        + "A roadmap's plan, its suggested signatures and its frontier say what Tau Ceti may add, so they are left "
        "out, and so is the statuses' prose: a model writes it, and Tau Ceti does not check it.",
        f"Each of the {stats['roadmaps']} roadmaps whose status names a declaration has a section, in the part where "
        "most of its articles are. It holds what the status names and the other named results near them: those in a "
        "module where no other roadmap's status names a declaration, or else in a folder of modules below the areas "
        f"where this status names at least {FOLDER_MIN} declarations and no other names any. The other named results "
        f"are in {stats['areas']} sections by "
        f"area, a module's first two levels under `TauCeti`; an area with fewer than {AREA_MIN} of them joins its "
        f"part's *Other results*, and a part with fewer than {PART_MIN} articles joins *Other Areas*.",
        "Each article's text is its declaration's docstring and signature, under Tau Ceti's Apache-2.0 license; a "
        "docstring that opens with a bold title, or with bold words its first sentence goes on from, gives the article "
        "its title. Dependencies come from Tau Ceti's declarations (`lean/tauceti/TauCetiDeps.lean`): under "
        "*Depends on*, the articles that a statement reaches through the statements of declarations not mapped here, "
        "and under *Proof depends on*, those a proof reaches through any chain of Tau Ceti declarations not mapped "
        "here. A theorem or definition that reaches `sorry`, itself or through a declaration mapped here, says so, and "
        "one stated from a proposition Tau Ceti defines says what it assumes.",
    ])
