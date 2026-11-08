"""The Formal Conjectures chapter: one article per problem file, a card per statement it keeps.

Formal Conjectures (google-deepmind/formal-conjectures) states open and solved
problems in Lean, a file per problem under FormalConjectures/<source folder>/.
Every statement carries one `@[category ...]` attribute (research open,
research solved, textbook, API or test), often `@[AMS ...]` subject codes and
`@[formal_proof using ... at "url"]` links to proofs elsewhere.
tools/refresh_formal_conjectures.py reads a checkout at a pinned commit into
data/formal-conjectures/: each file's title and module docstring, and for each
research or textbook statement its name, category, subjects, proof links,
docstring, Lean statement and whether its proof holds `sorry`, as
trough.leansource reads the source without Lean. Test and API statements are
counted, not kept. The chapter has a part per source folder, an index by
subject and a page per FC100 subset list; the problems have no edges.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from . import leansource
from .blueprints import Built, escape
from .ff import safe
from .mathlib import fence
from .vault import Container, Entry, Leaf, chunk, range_title, slugify

SCHEMA = "trough-fc/v1"
REPO = "google-deepmind/formal-conjectures"
GITHUB = "https://github.com"
SITE = "https://google-deepmind.github.io/formal-conjectures/"
ROOT = "FormalConjectures"
SUBSETS = "Subsets"
KEPT = ("research open", "research solved", "textbook")
FOLDED = {"test": "test", "API": "api"}
CATEGORY = re.compile(r"^category (textbook|research open|research solved|test|API)$")
AMS = re.compile(r"^AMS((?: \d+)+)$")
FORMAL_PROOF = re.compile(r'^(conditional )?formal_proof using (formal_conjectures|lean4|other_system) at "([^"\\]*)"'
                          r"(?: assuming ((?:[^\s,]+ ?)+))?$")
TITLE = re.compile(r"^(?:#[ \t]+(.+?)[ \t]*#*|Title:[ \t]*(.+?))[ \t]*$")
REFERENCES = re.compile(r"^[ \t]*\*{0,2}References?\*{0,2}:?\*{0,2}:?", re.M | re.I)
REFERENCE = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])+)\]\(((?:[^\s()]|\([^\s()]*\))+)\)|(https?://[^\s)>\]]+)")
DECL_NAME = re.compile(rf"decl_name%\s+({leansource.NAME})")
SUBJECT = re.compile(r"/--\s*((?:(?!-/).)*?)\s*-/\s*\|\s*«(\d+)»", re.S)


def module_name(path: str) -> str:
    """The Lean module a file under the repository is, with «» around a component that is not an identifier."""
    parts = path.removesuffix(".lean").split("/")
    return ".".join(part if re.match(r"^[A-Za-z_][\w']*$", part) else f"«{part}»" for part in parts)


def title_and_doc(doc: str) -> tuple[str, str]:
    """A module docstring's title, its first line when that is a `# ` heading or starts `Title:`, and the rest
    of its text."""
    first, _, rest = doc.partition("\n")
    if match := TITLE.match(first):
        return match.group(1) or match.group(2), rest.strip()
    return "", doc.strip()


def reference(doc: str) -> dict | None:
    """The first link after the module docstring's references label."""
    label = REFERENCES.search(doc)
    if not label:
        return None
    link = REFERENCE.search(doc, label.end())
    if not link:
        return None
    if link.group(3):
        return {"text": link.group(3), "url": link.group(3)}
    return {"text": link.group(1), "url": link.group(2)}


def attributes(declaration: leansource.Declaration) -> tuple[list[str], list[int], list[dict], list[str]]:
    """A declaration's categories, AMS codes and formal proof links, and the attributes that name one of these
    but don't read as one."""
    categories, ams, proofs, unread = [], [], [], []
    for attribute in declaration.attributes:
        word = attribute.split(" ", 1)[0]
        if word == "category":
            if match := CATEGORY.match(attribute):
                categories.append(match.group(1))
            else:
                unread.append(attribute)
        elif word == "AMS":
            if match := AMS.match(attribute):
                ams += [int(code) for code in match.group(1).split()]
            else:
                unread.append(attribute)
        elif "formal_proof" in attribute.split(" ")[:2]:
            if match := FORMAL_PROOF.match(attribute):
                proof = {"system": match.group(2), "url": match.group(3)}
                if match.group(1):
                    proof["assuming"] = (match.group(4) or "").split()
                proofs.append(proof)
            else:
                unread.append(attribute)
    return categories, ams, proofs, unread


def read_module(text: str, path: str) -> dict:
    """A problem file's record: its title and module docstring, the research and textbook statements it
    keeps, how many test and API statements it has, and the categorized declarations it could not read."""
    return categorized(text, path)[0]


def categorized(text: str, path: str) -> tuple[dict, dict[str, str]]:
    """A problem file's record, and the category of each declaration it reads one for."""
    named: dict[str, str] = {}
    title, doc = title_and_doc(leansource.module_doc(text) or "")
    record = {"file": path, "module": module_name(path), "folder": path.split("/")[1],
              "title": title, "doc": doc, "reference": reference(doc),
              "statements": [], "folded": {"test": 0, "api": 0}, "unread": []}
    found = leansource.scan(text)
    if found is None:
        record["unread"].append({"name": "", "line": 0, "why": "its scopes do not close as they open"})
        return record, named
    for declaration in sorted(found.values(), key=lambda declaration: declaration.line):
        categories, ams, proofs, unread = attributes(declaration)
        if not categories and not unread:
            continue
        unended = declaration.statement is None and categories[0] in KEPT if categories else False
        why = ("an attribute that does not read: " + "; ".join(unread) if unread else
               "more than one category" if len(categories) > 1 else
               "no `:=` or `where` found to end its statement" if unended else "")
        if why:
            record["unread"].append({"name": declaration.name, "line": declaration.line, "why": why})
            continue
        category = categories[0]
        named[declaration.name] = category
        if category in FOLDED:
            record["folded"][FOLDED[category]] += 1
            continue
        record["statements"].append({
            "name": declaration.name, "kind": declaration.kind, "category": category,
            "ams": sorted(set(ams)), "formal_proofs": proofs, "doc": declaration.doc,
            "statement": declaration.statement, "line": declaration.line, "sorry": declaration.proof_sorry,
        })
    return record, named


def read_subset(text: str, path: str, statements: dict[str, tuple[str, str]]) -> dict:
    """An FC100 list: its title, its module docstring and the names it lists, each with the file and category
    of the statement it names (None when no categorized declaration has that full name)."""
    title, doc = title_and_doc(leansource.module_doc(text) or "")
    names = []
    for match in DECL_NAME.finditer(leansource.blank(text)):
        file, category = statements.get(match.group(1), (None, None))
        names.append({"name": match.group(1), "file": file, "category": category})
    return {"file": path, "title": title or path.rsplit("/", 1)[-1].removesuffix(".lean"), "doc": doc, "names": names}


def subjects(ams_source: str) -> dict[str, str]:
    """The AMS subject names Formal Conjectures gives its `AMS` attribute's codes, from the docstrings of
    FormalConjecturesUtil/Attributes/AMS.lean's constructors."""
    return {code: " ".join(name.split()) for name, code in SUBJECT.findall(ams_source)}


def read(checkout: Path, paths: list[str]) -> tuple[list[dict], list[dict]]:
    """Every problem file's record and every FC100 list's, from the .lean files under FormalConjectures/."""
    problems, subset_texts, named = [], {}, {}
    for path in paths:
        text = (checkout / path).read_text(encoding="utf-8")
        if path.split("/")[1] == SUBSETS:
            subset_texts[path] = text
            continue
        problem, categories = categorized(text, path)
        problems.append(problem)
        for name, category in categories.items():
            named.setdefault(name, (path, category))
    subsets = [read_subset(text, path, named) for path, text in subset_texts.items()]
    return problems, subsets


# The chapter, from the data.

# The source folders in the order of their parts, the largest first, with each part's title. A folder not
# named here comes after them.
FOLDERS = {
    "ErdosProblems": "Erdős problems",
    "OEIS": "OEIS",
    "Wikipedia": "Wikipedia",
    "GreensOpenProblems": "Green's open problems",
    "WrittenOnTheWallII": "Written on the Wall II",
    "Paper": "Papers",
    "Arxiv": "arXiv",
    "Mathoverflow": "MathOverflow",
    "Books": "Books",
    "Other": "Other",
    "Kourovka": "Kourovka",
    "Millennium": "Millennium problems",
    "OptimizationConstants": "Optimization constants",
    "OpenQuantumProblems": "Open quantum problems",
    "HilbertProblems": "Hilbert's problems",
    "LittProblems": "Litt's problems",
}
ERDOS = "ErdosProblems"
ERDOS_SITE = "https://www.erdosproblems.com"
STATEMENT_KINDS = ("theorem", "lemma")
NO_DEPENDS = ("No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, "
              "which edges between statements need.")


def load(data: Path) -> dict | None:
    """data/formal-conjectures/'s source and problems, when both are there."""
    source, problems = data / "formal-conjectures" / "source.json", data / "formal-conjectures" / "problems.json"
    if not (source.is_file() and problems.is_file()):
        return None
    return json.loads(source.read_text(encoding="utf-8")) | json.loads(problems.read_text(encoding="utf-8"))


def natural(path: str) -> list:
    """A sort key that orders the numbers in a path by value: ErdosProblems/9 before ErdosProblems/10."""
    return [int(part) if part.isdigit() else part.casefold() for part in re.split(r"(\d+)", path)]


def blob(rev: str, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{REPO}/blob/{rev}/{path}" + (f"#L{line}" if line else "")


def at(rev: str) -> str:
    return f"[{rev[:8]}]({GITHUB}/{REPO}/tree/{rev})"


def href(url: str) -> str:
    """A URL as a Markdown link target can hold it."""
    return url.replace(" ", "%20").replace("(", "%28").replace(")", "%29").replace("<", "%3C").replace(">", "%3E")


def plain_link(url: str) -> str:
    return f"[{escape(url)}]({href(url)})"


def quote(markdown: str) -> str:
    """Quoted Markdown as a blockquote, so its headings and lists stay inside the quote."""
    return "\n".join(f"> {line}".rstrip() for line in safe(markdown).split("\n"))


def erdos_number(problem: dict) -> int | None:
    """The number of an Erdős problem's file, when its title names the same number."""
    stem = problem["file"].rsplit("/", 1)[-1].removesuffix(".lean")
    if problem["folder"] != ERDOS or not stem.isdigit():
        return None
    match = re.search(r"(\d+)", problem["title"])
    return int(stem) if match and int(match.group(1)) == int(stem) else None


def title_of(problem: dict) -> str:
    return problem["title"] or problem["file"].rsplit("/", 1)[-1].removesuffix(".lean")


def proof_at(proof: dict) -> str:
    what = "a proof in another system" if proof["system"] == "other_system" else "a Lean proof"
    if "assuming" in proof:
        what += " assuming " + ", ".join(f"`{name}`" for name in proof["assuming"]) if proof["assuming"] else " under a condition"
    return f"{what} is at {plain_link(proof['url'])}"


def status(statement: dict) -> str:
    """A card's status line, from the statement's category, its proof links and whether its proof holds sorry."""
    category, proofs = statement["category"], statement["formal_proofs"]
    elsewhere = "; ".join(proof_at(proof) for proof in proofs)
    also = f" {elsewhere[:1].upper()}{elsewhere[1:]}." if elsewhere else ""
    if statement["kind"] not in STATEMENT_KINDS:
        return f"A definition (`{statement['kind']}`), not a statement; its category attribute says {category}." + also
    if not statement["sorry"]:
        return ("Textbook result, proved here." if category == "textbook" else "Proved here.") + also
    if category == "research open":
        return "Open: stated without proof." + also
    if category == "research solved":
        return f"Solved: stated here; {elsewhere}." if elsewhere else "Solved: stated here without proof."
    return "Textbook result, stated without proof." + also


def outcome(statement: dict) -> str:
    """The status a statement counts under in the chapter's totals."""
    if statement["kind"] not in STATEMENT_KINDS:
        return "definition"
    if not statement["sorry"]:
        return "textbook proved" if statement["category"] == "textbook" else "proved"
    if statement["category"] == "research open":
        return "open"
    if statement["category"] == "research solved":
        return "solved with proof" if statement["formal_proofs"] else "solved"
    return "textbook"


def plural(count: int, word: str, words: str | None = None) -> str:
    return f"{count:,} {word if count == 1 else words or word + 's'}"


def card(statement: dict, file: str, rev: str, subjects: dict[str, str]) -> str:
    """A statement's section of its problem's article."""
    lines = [f"## `{statement['name']}`", "", status(statement)]
    if statement["doc"]:
        lines += ["", quote(statement["doc"])]
    lines += ["", fence(statement["statement"]), ""]
    codes = ", ".join(f"[{code:02d} {escape(subjects.get(str(code), 'AMS ' + str(code)))}](trough:fc-ams-{code})"
                      for code in statement["ams"])
    lines.append(f"Category `{statement['category']}`" + (f"; AMS {codes}" if codes else "")
                 + f". Declared in [{file}, line {statement['line']}]({blob(rev, file, statement['line'])}).")
    return "\n".join(lines)


def counts(problem: dict) -> str:
    """The line counting a problem's statements, the test and API ones included."""
    tally = Counter(statement["category"] for statement in problem["statements"])
    kinds = [plural(tally[category], label, labels) for category, label, labels in (
        ("research open", "open", "open"), ("research solved", "solved", "solved"),
        ("textbook", "textbook result", "textbook results")) if tally[category]]
    total = len(problem["statements"])
    line = (f"The file states {plural(total, 'research or textbook statement')}: "
            + (", ".join(kinds[:-1]) + " and " + kinds[-1] if len(kinds) > 1 else kinds[0]) + ".")
    folded = [plural(problem["folded"][key], f"{label} statement") for key, label in (("test", "test"), ("api", "API"))
              if problem["folded"][key]]
    if folded:
        line += f" It also has {' and '.join(folded)}, counted here but not shown."
    return line


def article(problem: dict, rev: str, subjects: dict[str, str]) -> Leaf:
    """A problem file's article: its module docstring, then a card per statement it keeps."""
    title = escape(title_of(problem))
    file = problem["file"]
    parts = [quote(problem["doc"])] if problem["doc"] else []
    parts.append(f"*Quoted from [{file}]({blob(rev, file)}) in [Formal Conjectures]({GITHUB}/{REPO}) (Google DeepMind) "
                 f"at commit {at(rev)}, Apache-2.0, as are the docstrings and Lean statements below.*")
    sources = [(f"{file} at {rev[:8]}", blob(rev, file))]
    if (number := erdos_number(problem)) is not None:
        page = f"{ERDOS_SITE}/{number}"
        parts.append(f"The problem's page on erdosproblems.com: {plain_link(page)}.")
        sources.append((f"erdosproblems.com/{number}", page))
    elif problem["reference"]:
        sources.append((problem["reference"]["text"], href(problem["reference"]["url"])))
    parts.append(counts(problem))
    parts += [card(statement, file, rev, subjects) for statement in problem["statements"]]
    statements = problem["statements"]
    fields = [("declaration", statements[0]["kind"]), ("origin", "cited"),
              ("lean", ", ".join(statement["name"] for statement in statements)), ("statement", "formalized")]
    if all(statement["kind"] in STATEMENT_KINDS and not statement["sorry"] for statement in statements):
        fields.append(("proof", "formalized"))
    leaf = Leaf(title, slugify(title_of(problem)), fields, "\n\n".join(parts), no_depends=NO_DEPENDS)
    leaf.sources = sources
    return leaf


def no_article(problems: list[dict], rev: str) -> str:
    if not problems:
        return ""
    files = ", ".join(f"[{escape(title_of(problem))}]({blob(rev, problem['file'])})" for problem in problems)
    return (f"No article: {plural(len(problems), 'file')} here {'states' if len(problems) == 1 else 'state'} no research "
            f"or textbook statement: {files}.")


def folder_title(folder: str) -> str:
    return FOLDERS.get(folder) or re.sub(r"(?<=[a-z])(?=[A-Z])", " ", folder)


def erdos_sections(articles: list[tuple[dict, Leaf]]) -> list[Entry]:
    """The Erdős part's sections, by hundreds of problem number."""
    groups: dict[int, list[Leaf]] = {}
    for problem, leaf in articles:
        stem = problem["file"].rsplit("/", 1)[-1].removesuffix(".lean")
        groups.setdefault(int(stem) // 100 if stem.isdigit() else -1, []).append(leaf)
    sections = []
    for hundred, leaves in sorted(groups.items()):
        if hundred < 0:
            title, slug = "Other files", "other"
        else:
            low, high = max(1, hundred * 100), hundred * 100 + 99
            title, slug = f"Problems {low} to {high}", f"{low}-{high}"
        section = Container(title, slug, [Entry(leaf) for leaf in leaves])
        section.prose = f"The Erdős problems numbered {title.split(' ', 1)[1]} that Formal Conjectures states, one article each."
        sections.append(Entry(chunk(section)))
    return sections


def numbered(entries: list[Entry]):
    """Part titles for a long list that count its entries: "Entries 1 to 20"."""
    place = {id(entry): number for number, entry in enumerate(entries, 1)}

    def title(group: list[Entry], number: int, total: int) -> str:
        if id(group[0]) in place and id(group[-1]) in place:
            return f"Entries {place[id(group[0])]} to {place[id(group[-1])]}"
        return range_title(group, number, total)

    return title


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and each statement's source line (for
    hooks/lean-links.json). A part per source folder, then the subject index and the FC100 lists."""
    rev, subjects = data["rev"], data["subjects"]
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    by_folder: dict[str, list[dict]] = {}
    for problem in sorted(data["problems"], key=lambda problem: natural(problem["file"])):
        by_folder.setdefault(problem["folder"], []).append(problem)
    order = [folder for folder in FOLDERS if folder in by_folder] + sorted(set(by_folder) - set(FOLDERS))
    leaves: dict[str, Leaf] = {}
    in_order: list[tuple[dict, Leaf]] = []
    parts: list[Entry] = []
    orphans: list[dict] = []
    for folder in order:
        problems = by_folder[folder]
        articles = [(problem, article(problem, rev, subjects)) for problem in problems if problem["statements"]]
        empty = [problem for problem in problems if not problem["statements"]]
        stats["problems"] += len(problems)
        stats["without_statements"] += len(empty)
        for problem, leaf in articles:
            leaves[problem["file"]] = leaf
            in_order.append((problem, leaf))
            targets[f"fc-{problem['file']}"] = leaf
            for statement in problem["statements"]:
                stats[outcome(statement)] += 1
                links[statement["name"]] = blob(rev, problem["file"], statement["line"])
        for problem in problems:
            stats["test"] += problem["folded"]["test"]
            stats["api"] += problem["folded"]["api"]
            stats["unread"] += len(problem["unread"])
        if not articles:
            orphans += empty
            continue
        title = folder_title(folder)
        where = f"[FormalConjectures/{folder}]({GITHUB}/{REPO}/tree/{rev}/{ROOT}/{folder})"
        part = Container(title, slugify(title))
        part.prose = "\n\n".join(filter(None, [
            f"The {plural(len(articles), 'problem file')} in {where} that state a research or textbook statement, at commit "
            f"{at(rev)}, one article each" + (", in sections by hundreds of problem number." if folder == ERDOS else "."),
            f"Their docstrings and Lean statements are quoted from [Formal Conjectures]({GITHUB}/{REPO}) (Google DeepMind) "
            "at that commit, under its Apache-2.0 license.",
            (f"Formal Conjectures' [README for this folder]({blob(rev, f'{ROOT}/{ERDOS}/README.md')}) asks contributors to "
             f"keep each docstring as close as possible to the problem's text on [erdosproblems.com]({ERDOS_SITE}), and to "
             "copy it from the site's LaTeX. Each article links its problem's page there.") if folder == ERDOS else "",
        ]))
        part.tail = no_article(empty, rev)
        part.entries = erdos_sections(articles) if folder == ERDOS else [Entry(leaf) for _, leaf in articles]
        if folder != ERDOS:
            chunk(part)
        parts.append(Entry(part))
        stats["folders"] += 1
    stats["articles"] = len(in_order)
    stats["statements"] = sum(len(problem["statements"]) for problem, _ in in_order)

    # The subject index: a page per top-level AMS code that a kept statement names.
    by_subject: dict[int, list[Leaf]] = {}
    for problem, leaf in in_order:
        for code in sorted({code for statement in problem["statements"] for code in statement["ams"]}):
            by_subject.setdefault(code, []).append(leaf)
    subject_pages = []
    for code, members in sorted(by_subject.items()):
        name = subjects.get(str(code), f"AMS {code}")
        page = Container(escape(name), f"{code:02d}-{slugify(name)}", [Entry(leaf, owned=False) for leaf in members])
        page.prose = (f"The {plural(len(members), 'problem')} with a statement whose `AMS` attribute names {code:02d}, "
                      f"{escape(name)}, in the Mathematics Subject Classification. A problem with statements in several "
                      "subjects is listed under each; its article sits in its source folder's part.")
        targets[f"fc-ams-{code}"] = page
        subject_pages.append(Entry(chunk(page)))
    stats["subjects"] = len(subject_pages)
    index = Container("By subject", "by-subject", subject_pages)
    index.prose = ("The problems by subject: a page per top-level class of the Mathematics Subject Classification that a "
                   "statement's `AMS` attribute names, titled as Formal Conjectures names it.")
    targets["fc-by-subject"] = index
    parts.append(Entry(chunk(index)))

    # The FC100 lists.
    lists = []
    for subset in sorted(data["subsets"], key=lambda subset: natural(subset["file"])):
        page = Container(escape(subset["title"]), slugify(subset["title"]))
        missing = []
        for item in subset["names"]:
            leaf = leaves.get(item["file"] or "")
            if leaf is None:
                missing.append(item)
                continue
            page.entries.append(Entry(leaf, owned=False, label=f"`{item['name']}` ({item['category']}), in {leaf.title}"))
        page.prose = "\n\n".join(filter(None, [
            quote(subset["doc"]) if subset["doc"] else "",
            f"*Quoted from [{subset['file']}]({blob(rev, subset['file'])}) in [Formal Conjectures]({GITHUB}/{REPO}) "
            f"(Google DeepMind) at commit {at(rev)}, Apache-2.0.*",
            f"The {plural(len(subset['names']), 'statement')} the list names, each linked to its problem's article.",
        ]))
        if missing:
            page.tail = ("Without an article here: " + ", ".join(
                f"`{item['name']}`" + (f" ({item['category']}, in [{item['file']}]({blob(rev, item['file'])}))" if item["file"]
                                       else ", which the reading does not find") for item in missing) + ".")
        stats["subset_names"] += len(subset["names"])
        stats["subset_missing"] += len(missing)
        lists.append(Entry(chunk(page, numbered(page.entries))))
    if lists:
        subsets = Container("FC100 subsets", "fc100-subsets", lists)
        subsets.prose = (f"Formal Conjectures' {plural(len(lists), 'benchmark list')} in "
                         f"[FormalConjectures/{SUBSETS}]({GITHUB}/{REPO}/tree/{rev}/{ROOT}/{SUBSETS}), a page each.")
        targets["fc-subsets"] = subsets
        parts.append(Entry(subsets))
    root = Container("Formal Conjectures", "formal-conjectures", parts)
    root.prose = intro(data, stats)
    root.tail = no_article(orphans, rev).replace("here", "in a folder with no article", 1)
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items()))


def intro(data: dict, stats: Counter) -> str:
    rev = data["rev"]
    solved = stats["solved with proof"] + stats["solved"]
    proved = stats["proved"] + stats["textbook proved"]
    textbook = stats["textbook"] + stats["textbook proved"]
    definitions = (f" {plural(stats['definition'], 'definition')} carrying a category attribute "
                   f"{'is' if stats['definition'] == 1 else 'are'} shown as such.") if stats["definition"] else ""
    return "\n\n".join([
        f"[Formal Conjectures]({GITHUB}/{REPO}), from Google DeepMind, states open and solved mathematical problems in "
        f"Lean, with a site at {SITE}. This chapter maps it as read at commit {at(rev)} ({data['date'][:10]}), Lean "
        f"toolchain {data['toolchain']}: a part per source folder of `{ROOT}/`, an article per problem file and, in "
        "it, a card per statement.",
        f"Every statement carries one `category` attribute: research open, research solved, textbook, API or test. The "
        f"articles show the first three, {plural(stats['statements'], 'statement')} in "
        f"{plural(stats['articles'], 'article')}: {stats['open']:,} open and stated without proof, {solved:,} solved "
        f"({stats['solved with proof']:,} of them with a `formal_proof` link to a proof elsewhere), {textbook:,} textbook "
        f"results, and {proved:,} of these proved here.{definitions} The {stats['test']:,} test and {stats['api']:,} API "
        f"statements are counted in their problem's article, not shown. {plural(stats['without_statements'], 'problem file')} "
        f"{'states' if stats['without_statements'] == 1 else 'state'} none of the first three and "
        f"{'has' if stats['without_statements'] == 1 else 'have'} no article; their folder's page lists them.",
        "A card's status line reads the statement's category, its `formal_proof` links and whether the text of its proof "
        "in the file contains `sorry`: “Open: stated without proof.”; “Solved: stated here; a Lean proof is at …” when "
        "a link gives one, and “Solved: stated here without proof.” when none does; “Proved here.” when the proof's "
        "text holds no `sorry`, which, like Formal Conjectures' own `hasSorryFreeProof`, says nothing of the statements "
        "that proof uses. Formal Conjectures marks a link `formal_conjectures` when the proof fills this statement as "
        "written, and `lean4` when the problem is solved in Lean elsewhere, perhaps as an equivalent statement.",
        "No Lean is run for this chapter. Statements, docstrings and attributes are read from the source text: a "
        "statement is a named declaration with a category in the `@[...]` list right before it, its Lean statement "
        "runs to the `:=` that starts its proof, and its name is read under the namespaces it sits in. A statement "
        "with no name, an `example`, is left out, as Formal Conjectures' own site leaves it out. The articles have no "
        "dependencies: the problems form a flat collection, and edges between statements need Lean.",
        f"Two indexes link the articles: [by subject](trough:fc-by-subject), from the `AMS` attributes' top-level "
        f"classes of the Mathematics Subject Classification ({stats['subjects']} subjects), and the "
        "[FC100 subsets](trough:fc-subsets), Formal Conjectures' benchmark lists.",
        f"The docstrings and Lean statements are quoted from [Formal Conjectures]({GITHUB}/{REPO}) (Google DeepMind) at "
        f"commit {at(rev)}, under its Apache-2.0 license, with each article naming its file. Formal Conjectures asks "
        "that the Erdős problems' docstrings follow erdosproblems.com; the Erdős part says how, and each Erdős article "
        "links its problem's page there.",
    ])
