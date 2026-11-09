"""The Lean Pool chapter: one article per project card.

Lean Pool (github.com/LeanPool/lean-pool) keeps Lean projects outside Mathlib's
scope, each in a directory under LeanPool/ with a card, LeanPool/projects/<slug>.yaml:
its title, summary, authors, sources, license, provenance, MSC2020 classes and
main results, each a declaration with an informal statement. Lean Pool's CI
checks that every name the card lists under `main_declarations` exists.
tools/refresh_lean_pool.py reads the cards at a pinned commit into
data/lean-pool/, with the module, line and kind of each main result's
declaration as trough.leansource finds it in the project's directory, without
Lean. The chapter has a section per top-level MSC2020 class, that of the
card's first code, and an article per card. Articles have no edges: edges
between declarations need Lean, which this chapter does not run.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote

import yaml

from . import leansource
from .blueprints import escape
from .ff import CODE, is_apache, plural
from .mathlib import title_key
from .vault import Container, Entry, Leaf, chunk, range_title, short, slugify

SCHEMA = "trough-lean-pool/v1"
REPO = "LeanPool/lean-pool"
GITHUB = "https://github.com"
DOCS = "https://leanpool.github.io/lean-pool"
MATHLIB_REPO = "https://github.com/leanprover-community/mathlib4"
# The keys Lean Pool's quality gate requires of a card that the chapter reads.
REQUIRED = ("slug", "title", "summary", "entry_module", "authors", "source", "license", "provenance",
            "main_declarations", "main_results", "msc")
LICENSES = ("Apache-2.0", "MIT")
SOURCE_KEYS = ("title", "authors", "citation", "doi", "arxiv", "url", "paper_url", "paper", "manuscript_url",
               "manuscript", "mathematical_source", "note", "notes", "github_repo", "commit")
# Source keys that name a document to link, and the word for it.
DOCUMENTS = {"paper_url": "paper", "paper": "paper", "manuscript_url": "manuscript", "manuscript": "manuscript"}
# Lean Pool's own words for each provenance, from its CONTRIBUTING.md: who wrote the Lean proofs.
PROVENANCE = {"human": "written by people", "AI": "mostly produced by an AI system",
              "mix": "both contributed substantially"}
MEANS = {"human": "its Lean proofs were “written by people”",
         "AI": "its Lean proofs were “mostly produced by an AI system”",
         "mix": "people and AI “both contributed substantially” to its Lean proofs"}
# The top-level classes of MSC2020, in order.
MSC = {
    "00": "General and overarching topics; collections",
    "01": "History and biography",
    "03": "Mathematical logic and foundations",
    "05": "Combinatorics",
    "06": "Order, lattices, ordered algebraic structures",
    "08": "General algebraic systems",
    "11": "Number theory",
    "12": "Field theory and polynomials",
    "13": "Commutative algebra",
    "14": "Algebraic geometry",
    "15": "Linear and multilinear algebra; matrix theory",
    "16": "Associative rings and algebras",
    "17": "Nonassociative rings and algebras",
    "18": "Category theory; homological algebra",
    "19": "K-theory",
    "20": "Group theory and generalizations",
    "22": "Topological groups, Lie groups",
    "26": "Real functions",
    "28": "Measure and integration",
    "30": "Functions of a complex variable",
    "31": "Potential theory",
    "32": "Several complex variables and analytic spaces",
    "33": "Special functions",
    "34": "Ordinary differential equations",
    "35": "Partial differential equations",
    "37": "Dynamical systems and ergodic theory",
    "39": "Difference and functional equations",
    "40": "Sequences, series, summability",
    "41": "Approximations and expansions",
    "42": "Harmonic analysis on Euclidean spaces",
    "43": "Abstract harmonic analysis",
    "44": "Integral transforms, operational calculus",
    "45": "Integral equations",
    "46": "Functional analysis",
    "47": "Operator theory",
    "49": "Calculus of variations and optimal control; optimization",
    "51": "Geometry",
    "52": "Convex and discrete geometry",
    "53": "Differential geometry",
    "54": "General topology",
    "55": "Algebraic topology",
    "57": "Manifolds and cell complexes",
    "58": "Global analysis, analysis on manifolds",
    "60": "Probability theory and stochastic processes",
    "62": "Statistics",
    "65": "Numerical analysis",
    "68": "Computer science",
    "70": "Mechanics of particles and systems",
    "74": "Mechanics of deformable solids",
    "76": "Fluid mechanics",
    "78": "Optics, electromagnetic theory",
    "80": "Classical thermodynamics, heat transfer",
    "81": "Quantum theory",
    "82": "Statistical mechanics, structure of matter",
    "83": "Relativity and gravitational theory",
    "85": "Astronomy and astrophysics",
    "86": "Geophysics",
    "90": "Operations research, mathematical programming",
    "91": "Game theory, economics, finance, and other social and behavioral sciences",
    "92": "Biology and other natural sciences",
    "93": "Systems theory; control",
    "94": "Information and communication theory, circuits",
    "97": "Mathematics education",
}
MSC_CODE = re.compile(r"^(\d\d)[A-Z-](\d\d|xx|XX)$")


def load_yaml(text: str) -> object:
    """A YAML file with every scalar kept as the text it is written as, so an arXiv id such as 2311.05760
    keeps its last digit."""
    return yaml.load(text, Loader=yaml.BaseLoader)


def strings(value: object) -> list[str]:
    return [item for item in value if isinstance(item, str)] if isinstance(value, list) else []


def read_card(text: str, where: str) -> dict:
    """A card's mapping; raises ValueError when it lacks a key the chapter reads, or has a license, provenance
    or first MSC2020 code the chapter does not know."""
    try:
        card = load_yaml(text)
    except yaml.YAMLError as error:
        raise ValueError(f"{where}: {error}") from error
    if not isinstance(card, dict):
        raise ValueError(f"{where}: not a mapping")
    missing = [key for key in REQUIRED if not card.get(key)]
    if missing:
        raise ValueError(f"{where}: lacks {', '.join(missing)}")
    if not all(isinstance(card[key], str) for key in ("slug", "title", "summary", "entry_module", "license",
                                                      "provenance")):
        raise ValueError(f"{where}: slug, title, summary, entry_module, license or provenance is not text")
    if card["license"] not in LICENSES:
        raise ValueError(f"{where}: license {card['license']!r}, not Apache-2.0 or MIT")
    if card["provenance"] not in PROVENANCE:
        raise ValueError(f"{where}: unknown provenance {card['provenance']!r}")
    msc = strings(card["msc"])
    if not msc or not (code := MSC_CODE.match(msc[0])) or code.group(1) not in MSC:
        raise ValueError(f"{where}: first MSC2020 code {msc[:1]!r} is not one of a known class")
    if not isinstance(card["source"], dict) or not isinstance(card["main_results"], list) or \
            len(card["entry_module"].split(".")) != 2 or card["entry_module"].split(".")[0] != "LeanPool":
        raise ValueError(f"{where}: source, main_results or entry_module not as Lean Pool writes them")
    if not all(isinstance(result, dict) and isinstance(result.get("declaration"), str)
               and isinstance(result.get("informal"), str) for result in card["main_results"]):
        raise ValueError(f"{where}: a main result lacks a declaration or informal text")
    return card


def read(path: Path, checkout: Path) -> str:
    """A file's text; raises ValueError naming the file when it is not UTF-8."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise ValueError(f"{path.relative_to(checkout).as_posix()}: {error}") from error


def scan_project(checkout: Path, directory: str, names: list[str]) -> tuple[dict[str, tuple[str, leansource.Declaration]],
                                                                           Counter]:
    """Where the project's files declare each name: LeanPool/<directory>.lean and the .lean files under
    LeanPool/<directory>/. A name two files declare is not placed, as one of the readings is wrong: a project
    imports all its files together, so Lean would refuse it. Also counts the files read, the files whose scopes
    don't close and the names declared twice."""
    root = checkout / "LeanPool"
    files = [root / f"{directory}.lean"] + sorted((root / directory).rglob("*.lean"))
    # A file can declare a name only if its text holds the name's last component.
    lasts = {leansource.split(name)[-1] for name in names if leansource.split(name)}
    places: dict[str, list[tuple[str, leansource.Declaration]]] = {}
    counts: Counter = Counter()
    for path in files:
        if not path.is_file():
            continue
        text = read(path, checkout)
        if not any(last in text for last in lasts):
            continue
        counts["files_read"] += 1
        found = leansource.scan(text)
        if found is None:
            counts["files_unclosed"] += 1
            continue
        file = path.relative_to(checkout).as_posix()
        for name in names:
            if name in found and file not in [place for place, _ in places.get(name, [])]:
                places.setdefault(name, []).append((file, found[name]))
    counts["declared_twice"] = sum(len(found) > 1 for found in places.values())
    return {name: found[0] for name, found in places.items() if len(found) == 1}, counts


def read_project(checkout: Path, card: dict, notice: dict) -> tuple[dict, Counter]:
    """A card's record, each main result with where the scan finds its declaration. Raises ValueError when
    the card's entry module is not in the checkout."""
    directory = card["entry_module"].split(".")[1]
    if not (checkout / "LeanPool" / f"{directory}.lean").is_file():
        raise ValueError(f"LeanPool/projects/{card['slug']}.yaml: its entry module, LeanPool/{directory}.lean, "
                         "is not in the checkout")
    main = set(strings(card["main_declarations"]))
    results = [result for result in card["main_results"] if isinstance(result, dict) and result.get("declaration")]
    places, counts = scan_project(checkout, directory, [result["declaration"] for result in results])
    main_results = []
    for result in results:
        name = result["declaration"]
        place = places.get(name)
        main_results.append({"declaration": name, "informal": result.get("informal", ""), "main": name in main}
                            | ({"source_ref": result["source_ref"]} if result.get("source_ref") else {})
                            | {"module": place[0].removesuffix(".lean").replace("/", ".") if place else None,
                               "line": place[1].line if place else None, "kind": place[1].kind if place else None,
                               "sorry": place[1].sorry if place else None})
    source = card["source"]
    entry = notice.get(directory)
    note = entry.get("note") if isinstance(entry, dict) else None
    # Most cards put a provenance note at the top level, and some under source.
    provenance_note = next((value for value in (card.get("provenance_note"), source.get("provenance_note"))
                            if isinstance(value, str) and value.strip()), None)
    record = {
        "slug": card["slug"],
        "title": card["title"],
        "summary": card["summary"],
        "msc": strings(card["msc"]),
        "authors": strings(card["authors"]),
        **({"contributors": strings(card["contributors"])} if strings(card.get("contributors")) else {}),
        "source": {key: strings(source[key]) if key == "authors" else source[key]
                   for key in SOURCE_KEYS if source.get(key) and (key == "authors" or isinstance(source[key], str))},
        "license": card["license"],
        # The note Lean Pool's NOTICE.extra.yml keeps for a project published under MIT: its copyright line,
        # or a remark about it.
        "notice": note if card["license"] == "MIT" and isinstance(note, str) and note.strip() else None,
        "provenance": card["provenance"],
        **({"provenance_note": provenance_note} if provenance_note else {}),
        "directory": directory,
        "main_results": main_results,
    }
    return record, counts


def read_pool(checkout: Path, rev: str, date: str) -> tuple[dict, dict, Counter]:
    """The pool's source record and its cards' record at the checkout's commit, and the scan's counts. Raises
    ValueError when the repository is not Apache-2.0, it has no cards, or a card is not as the chapter reads it."""
    license_file = checkout / "LICENSE"
    if not license_file.is_file() or not is_apache(license_file.read_text(encoding="utf-8")):
        raise ValueError("LICENSE is not the Apache License 2.0")
    manifest = checkout / "lake-manifest.json"
    packages = json.loads(manifest.read_text(encoding="utf-8")).get("packages", []) if manifest.is_file() else []
    toolchain = checkout / "lean-toolchain"
    notice_file = checkout / "NOTICE.extra.yml"
    try:
        notice = load_yaml(read(notice_file, checkout)) if notice_file.is_file() else {}
    except yaml.YAMLError as error:
        raise ValueError(f"NOTICE.extra.yml: {error}") from error
    notice = notice if isinstance(notice, dict) else {}
    cards = sorted((checkout / "LeanPool" / "projects").glob("*.yaml"))
    if not cards:
        raise ValueError("no cards in LeanPool/projects/")
    projects, counts = [], Counter()
    for path in cards:
        card = read_card(read(path, checkout), f"LeanPool/projects/{path.name}")
        if card["slug"] != path.stem:
            raise ValueError(f"LeanPool/projects/{path.name}: slug {card['slug']!r} is not its file's name")
        project, scanned = read_project(checkout, card, notice)
        projects.append(project)
        counts.update(scanned)
    source = {
        "repo": REPO,
        "rev": rev,
        "date": date,
        "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else "",
        "mathlib": next((package.get("rev", "") for package in packages if package.get("name") == "mathlib"), ""),
    }
    return source, {"schema": SCHEMA, "rev": rev, "projects": projects}, counts


def found_count(record: dict) -> int:
    """How many main results the scan places, for the refresh's drop check."""
    return sum(1 for project in record["projects"] for result in project["main_results"] if result["module"])



# The chapter, from the records.

NO_DEPENDS = ("No dependencies are recorded: edges between declarations need Lean, and this chapter reads the "
              "source text without running it.")


def load(data: Path) -> tuple[dict, dict] | None:
    """data/lean-pool/'s source and cards records, when the refresh has written them."""
    folder = data / "lean-pool"
    if not (folder / "projects.json").is_file():
        return None
    return (json.loads((folder / "source.json").read_text(encoding="utf-8")),
            json.loads((folder / "projects.json").read_text(encoding="utf-8")))


def plain(segment: str) -> str:
    """Text outside code spans with Markdown's marks escaped, but for brackets: a link to the page escapes them
    itself, and a backslash before one would open a formula, so only a "](", which could make a link, is
    escaped. A "<" that could open HTML and an "&" that could start a character reference are shown in code,
    as the site publishes neither and Markdown has no escape for them."""
    out = escape(segment).replace("#", "\\#").replace("\\[", "[").replace("\\]", "]").replace("](", "\\](")
    return re.sub(r"<(?=[A-Za-z/!?])|&(?=#|[A-Za-z][A-Za-z0-9]*;)", lambda mark: f"`{mark.group()}`", out)


def text(value: str) -> str:
    """Card text as written, for a page: its code spans kept, Markdown's other marks escaped, and its
    whitespace, but for paragraph breaks, single spaces."""
    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", value.strip()):
        flat = " ".join(paragraph.split())
        out, last = [], 0
        for match in CODE.finditer(flat):
            out += [plain(flat[last:match.start()]), match.group()]
            last = match.end()
        paragraphs.append("".join(out) + plain(flat[last:]))
    return "\n\n".join(paragraphs)


def closed(quoted: str) -> str:
    """A quotation that ends a sentence: a period after it, unless it ends with one."""
    return f"“{quoted}”" + ("" if quoted.endswith((".", "!", "?")) else ".")


def code(name: str) -> str:
    return f"`` {name} ``" if "`" in name else f"`{name}`"


def href(url: str) -> str:
    """A URL as a Markdown link's target: its spaces, parentheses and angle brackets percent-encoded."""
    return quote(url.strip(), safe="/:?#[]@!$&'*+,;=%~")


def tree(source: dict, path: str = "") -> str:
    return f"{GITHUB}/{source['repo']}/tree/{source['rev']}" + (f"/{path}" if path else "")


def blob(source: dict, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{source['repo']}/blob/{source['rev']}/{path}" + (f"#L{line}" if line else "")


def at(source: dict) -> str:
    return f"[{source['rev'][:8]}]({tree(source)})"


def doc_url(name: str, module: str) -> str:
    anchor = quote(name, safe=".'_-!?«»")
    return f"{DOCS}/{module.replace('.', '/')}.html#{anchor}"


def card_path(project: dict) -> str:
    return f"LeanPool/projects/{project['slug']}.yaml"


def msc_class(project: dict) -> str:
    return project["msc"][0][:2]


def result_line(source: dict, result: dict) -> str:
    """A main result: its declaration, linked to the documentation and its line at the pin when the scan finds
    it, and the card's informal statement, quoted."""
    name = code(result["declaration"])
    if result["module"]:
        file = result["module"].replace(".", "/") + ".lean"
        kind = result["kind"] + ("; a main declaration" if result["main"] else "")
        head = (f"[{name}]({doc_url(result['declaration'], result['module'])}) ({kind}), declared in "
                f"[{file}, line {result['line']}]({blob(source, file, result['line'])})")
        if result["sorry"]:
            head += ", where its text contains `sorry`, so it is stated without proof"
    else:
        head = (f"{name}, {'a main declaration that' if result['main'] else 'which'} the scan does not find declared "
                "in the project's files at this commit")
    line = f"- {head}: “{text(result['informal'])}”"
    if result.get("source_ref"):
        line += f" Its source, as the card gives it: “{text(result['source_ref'])}”"
    return line


def source_links(project: dict) -> list[str]:
    """The card's sources: DOI, then arXiv, then URL, then a paper or manuscript it links, with its notes on them,
    and the project's own repository and commit."""
    source = project["source"]
    links = []
    if source.get("doi"):
        links.append(f"[doi:{text(source['doi'])}]({href('https://doi.org/' + source['doi'])})")
    if source.get("arxiv"):
        links.append(f"[arXiv:{text(source['arxiv'])}]({href('https://arxiv.org/abs/' + source['arxiv'])})")
    repository = f"{GITHUB}/{source['github_repo']}" if source.get("github_repo") else ""
    commit = source.get("commit", "")
    # A URL that is the project's repository, or the repository at the card's commit, is the row below.
    if source.get("url") and source["url"].rstrip("/") not in (repository, f"{repository}/tree/{commit}"):
        links.append(f"[{text(source['url'])}]({href(source['url'])})")
    for key, word in DOCUMENTS.items():
        if re.match(r"https?://", source.get(key, "")) and source[key] != source.get("url"):
            links.append(f"[{word}]({href(source[key])})")
    rows = []
    if links or source.get("title") or source.get("citation"):
        work = f"*{text(source['title'])}*" if source.get("title") else ""
        if work and source.get("authors"):
            work += f" by {text(', '.join(source['authors']))}"
        citation = text(source["citation"]) if source.get("citation") else ""
        rows.append("- Source: " + ", ".join(filter(None, [work, citation, *links])) + ".")
    if source.get("mathematical_source"):
        rows.append(f"- Mathematical source, as the card gives it: {closed(text(source['mathematical_source']))}")
    for key in ("note", "notes"):
        if source.get(key):
            rows.append(f"- The card's note on its source: {closed(text(source[key]))}")
    if repository:
        rows.append(f"- Project repository: [{source['github_repo']}]({repository})"
                    + (f", at commit [{commit[:8]}]({repository}/tree/{commit})" if re.fullmatch(r"[0-9a-f]{40}", commit)
                       else f", at commit {text(commit)}" if commit else "") + ".")
    return rows


def project_note(source: dict, project: dict) -> str:
    rows = [f"- Authors: {text(', '.join(project['authors']))}."]
    if project.get("contributors"):
        rows.append(f"- Contributors: {text(', '.join(project['contributors']))}.")
    rows += source_links(project)
    provenance = project["provenance"]
    rows.append(f"- Provenance: {provenance}, which in Lean Pool's terms means {MEANS[provenance]}."
                + (f" The card's note: “{text(project['provenance_note'])}”" if project.get("provenance_note") else ""))
    if project["license"] == "MIT":
        line = "- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0"
        if not project["notice"]:
            line += "."
        elif project["notice"].startswith("Copyright"):
            line += f", keeping its copyright line: {closed(text(project['notice']))}"
        else:
            line += f". Lean Pool's notice file notes: {closed(text(project['notice']))}"
        rows.append(line)
    else:
        rows.append(f"- License: {project['license']}.")
    rows.append(f"- MSC2020: {', '.join(project['msc'])}.")
    rows.append(f"- In Lean Pool: [LeanPool/{project['directory']}]({tree(source, 'LeanPool/' + project['directory'])}), "
                f"from the card [{card_path(project)}]({blob(source, card_path(project))}).")
    return "\n".join(rows)


def article(source: dict, project: dict) -> tuple[Leaf, dict[str, str]]:
    """A card's article, and the documentation links of the main declarations its Lean row names."""
    results = project["main_results"]
    named = [result for result in results if result["main"] and result["module"]]
    placed = [result for result in results if result["module"]]
    # The kind of the first main declaration placed, else of the first main result placed; with none placed, the
    # article is exposition, with no kind to claim.
    fields = [("declaration", (named or placed)[0]["kind"]), ("origin", "cited")] if placed else []
    if named:
        fields += [("lean", ", ".join(result["declaration"] for result in named)), ("statement", "formalized")]
        # An alias is of a declaration Lean Pool's CI builds without `sorry`, theorem or definition.
        if all(result["kind"] in ("theorem", "lemma", "alias") and not result["sorry"] for result in named):
            fields.append(("proof", "formalized"))
    body = "\n\n".join([
        "\n>\n".join(f"> {paragraph}" for paragraph in text(project["summary"]).split("\n\n")),
        f"*Quoted from the card [{card_path(project)}]({blob(source, card_path(project))}) of "
        f"[{source['repo']}]({GITHUB}/{source['repo']}) at commit {at(source)}, Apache-2.0.*",
    ])
    found = sum(1 for result in results if result["module"])
    if len(results) == 1:
        lead = (f"The card lists one main result, with its informal statement quoted from the card. The scan "
                f"{'finds' if found else 'does not find'} its declaration in the project's files at commit {at(source)}.")
    else:
        lead = (f"The card lists {len(results)} main results, each with its informal statement quoted from the card. "
                f"The scan finds {found} of their declarations in the project's files at commit {at(source)}.")
    if found:
        lead += (" A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily "
                 "from its main branch, and its line at this commit.")
    notes = [("Main results", "\n\n".join([lead, "\n".join(result_line(source, result) for result in results)])),
             ("Project", project_note(source, project))]
    leaf = Leaf(text(project["title"]), project["slug"], fields, body, notes=notes, no_depends=NO_DEPENDS)
    leaf.sources = [(f"Lean Pool at {source['rev'][:8]}: {card_path(project)}", blob(source, card_path(project))),
                    (f"Lean Pool at {source['rev'][:8]}: LeanPool/{project['directory']}",
                     tree(source, f"LeanPool/{project['directory']}"))]
    return leaf, {result["declaration"]: doc_url(result["declaration"], result["module"]) for result in named}


def chapter(source: dict, record: dict) -> tuple[Container, Counter, list[tuple[Container, dict[str, str]]]]:
    """The chapter's root and counts, and each part with the documentation links of its articles' main
    declarations (for hooks/lean-links.json). A part per top-level MSC2020 class, an article per card."""
    stats: Counter = Counter()
    by_class: dict[str, list[tuple[Leaf, dict[str, str]]]] = {number: [] for number in MSC}
    for project in record["projects"]:
        by_class[msc_class(project)].append(article(source, project))
        stats["articles"] += 1
        stats[f"provenance_{project['provenance']}"] += 1
        stats[f"license_{project['license']}"] += 1
        for result in project["main_results"]:
            stats["main_results"] += 1
            stats["main_results_found"] += bool(result["module"])
            stats["main_declarations"] += result["main"]
            stats["main_declarations_found"] += result["main"] and bool(result["module"])
            stats["sorry"] += bool(result["sorry"])
    parts = []
    for number, name in MSC.items():
        members = by_class[number]
        if not members:
            continue
        members.sort(key=lambda pair: title_key(pair[0].title))
        # The slug names the class by the words before its first comma or semicolon: 91-game-theory.
        part = Container(name, f"{number}-{slugify(re.split(r'[,;]', name)[0])}", [Entry(leaf) for leaf, _ in members])
        named_class = f"“{name}”" if re.search(r"[,;]", name) else name
        part.prose = (f"The Lean Pool projects whose card's first MSC2020 code is in class {number}, {named_class}: "
                      + ("1 article." if len(members) == 1 else f"{len(members)} articles, one per card."))
        links: dict[str, str] = {}
        for _, names in members:
            for key, url in names.items():
                links.setdefault(key, url)
        # A page of one article is titled by the article.
        parts.append((chunk(part, lambda group, number, total: short(group[0].text) if len(group) == 1
                            else range_title(group, number, total)), links))
        stats["parts"] += 1
    root = Container("Lean Pool", "lean-pool", [Entry(part) for part, _ in parts])
    root.prose = intro(source, record, stats)
    chunk(root, lambda group, number, total: f"MSC2020 classes {group[0].node.slug[:2]} to {group[-1].node.slug[:2]}")
    return root, stats, parts


def intro(source: dict, record: dict, stats: Counter) -> str:
    return "\n\n".join([
        f"[Lean Pool]({GITHUB}/{source['repo']}) keeps Lean projects that are outside Mathlib's scope. As its README "
        "describes, each is imported from a permissively licensed repository into a directory of its own, brought to "
        "Lean Pool's Lean and Mathlib, and merged once it passes Lean Pool's CI and an LLM review. This chapter maps "
        f"its {stats['articles']} projects at commit {at(source)}"
        + (f" ({source['date'][:10]})" if source.get("date") else "")
        + f", built with Lean {source['toolchain']}"
        + (f" and Mathlib at [{source['mathlib'][:8]}]({MATHLIB_REPO}/tree/{source['mathlib']})" if source.get("mathlib")
           else "")
        + ". Each project has a card, `LeanPool/projects/<slug>.yaml`, with its title, summary, authors, sources, "
        "license, provenance, MSC2020 classes and main results, each a Lean declaration with an informal statement. "
        f"There is a section per top-level MSC2020 class, the class of the first code a card lists "
        f"({stats['parts']} sections), and an article per card, titled by the card's title. An article quotes the card's summary, names "
        "its authors, links its sources and the project's own repository, gives its provenance and license, and "
        "lists its main results.",
        f"The cards list {stats['main_results']:,} main results, {stats['main_declarations']:,} of them among the "
        "cards' main declarations, whose names Lean Pool's CI checks with `#check`. No Lean is run for this chapter: "
        "each main result's declaration is looked for in its project's files by reading the source text, following "
        "`namespace`, `section` and `end`, and a name counts only when a declaration command names it in full under "
        "the namespaces it sits in, in one file of the project. The scan finds "
        f"{stats['main_results_found']:,} of the {stats['main_results']:,} declarations, and "
        f"{stats['main_declarations_found']:,} of the {stats['main_declarations']:,} main declarations. A found "
        "declaration links its page in Lean Pool's [documentation](" + DOCS + "/), which Lean Pool rebuilds daily "
        "from its main branch, and its line at the pinned commit; a main result the scan does not find keeps its "
        "informal statement and says so. Articles show no Lean signatures and have no dependencies, as edges "
        "between declarations need Lean.",
        "A card's provenance says who wrote the project's Lean proofs, in the words of Lean Pool's contributing guide: "
        f"“human” (“{PROVENANCE['human']}”), “AI” (“{PROVENANCE['AI']}”) or “mix” (“{PROVENANCE['mix']}”). "
        f"Of the cards, {stats['provenance_AI']} say AI, {stats['provenance_human']} human and "
        f"{stats['provenance_mix']} mix.",
        "The quoted text is the cards', in Lean Pool's repository under the Apache-2.0 license, as written, except "
        "that a < before a letter, or an & that would start a character reference, which the site cannot show as "
        "text, is set in code. Each article names the project's authors and gives the sources its card names: "
        "links to a DOI, arXiv, a URL and a paper or manuscript, a citation, the mathematical source, and the card's "
        "notes on them. Of the projects, "
        f"{stats['license_MIT']} were published under the MIT license, and Lean Pool redistributes them under "
        "Apache-2.0; where Lean Pool's notice file keeps a copyright line or a note for one, its article quotes it.",
    ])
