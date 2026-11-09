"""The Analysis I chapter: Terence Tao's Lean companion to his Analysis I, and to An introduction to measure theory.

teorth/analysis keeps a Lean module per section of Analysis I (Analysis/Section_6_1.lean and so on, the
chapter epilogues and the appendix sections, in the order of its literate.toml) and per section of the
measure theory book (Analysis/MeasureTheory/Section_1_1_1.lean and on, with a Notation module). Each
module's docstring titles its section, and its declarations' docstrings carry the book's labels
("Definition 6.1.3", "Exercise 6.1.2"). tools/refresh_analysis.py reads a checkout at a pinned commit into
data/analysis/: each section's title, module docstring and the other sections it imports, and its labelled
items in file order, each with the declarations carrying its label as trough.leansource reads them without
Lean, `example`s included. The chapter has a part per book, a page per chapter, an article per section with
a block per label, and edges from the imports between sections.
"""

from __future__ import annotations

import json
import re
import tomllib
from collections import Counter
from pathlib import Path

from . import leansource
from .blueprints import Built, escape
from .ff import opening, safe
from .formal_conjectures import quote
from .mathlib import fence
from .vault import Container, Entry, Leaf, chunk, slugify

SCHEMA = "trough-analysis/v1"
REPO = "teorth/analysis"
GITHUB = "https://github.com"
ANALYSIS_I, MEASURE_THEORY = "analysis-i", "measure-theory"
BOOKS = {ANALYSIS_I: "Analysis I", MEASURE_THEORY: "An introduction to measure theory"}
README, MT_README, LITERATE = "README.md", "Analysis/MeasureTheory/README.md", "literate.toml"
SECTION = re.compile(r"^Analysis\.(?:Section_(?P<chapter>\d+)_(?P<section>\d+|epilogue)|"
                     r"Appendix_(?P<appendix>[A-Z])_(?P<part>\d+))$")
MT_SECTION = re.compile(r"^Analysis\.MeasureTheory\.(?:Section_(?P<chapter>\d+)_(?P<section>\d+)_(?P<sub>\d+)|"
                        r"(?P<notation>Notation))$")
HEADING = re.compile(r"^#[ \t]+(?:(?:Analysis I|Introduction to Measure Theory),[ \t]+)?(?P<title>.+?)[ \t]*$")
IMPORT = re.compile(r"^(?:public[ \t]+)?(?:meta[ \t]+)?import[ \t]+(?:all[ \t]+)?(\S+)", re.M)
LABEL_KINDS = ("Definition", "Theorem", "Lemma", "Proposition", "Corollary", "Exercise", "Example", "Remark", "Axiom",
               "Assumption")
# A number as the book writes it, with a part or a prime: 6.1.3, A.1.1, 2.1, 3.6.2a, 1.1.23', 1.3.8(vi'').
NUMBER = r"(?:[A-Z]\.)?\d+(?:\.\d+)*[a-z]?'*(?:\([a-z]+'*\))?"
ONE_LABEL = rf"(?P<kind>{'|'.join(LABEL_KINDS)})s?[ \t]+{NUMBER}"
# A label, or several joined by slashes: "Theorem 11.4.1(a) / Exercise 11.4.1".
LABEL = re.compile(rf"^{ONE_LABEL}(?:[ \t]*/[ \t]*(?:{'|'.join(LABEL_KINDS)})s?[ \t]+{NUMBER})*")
# Verso's `{given}` role, which names a docstring's variables before its text and may come before the label.
GIVEN = re.compile(r"^(?:\{given\b[^}\n]*\}`[^`\n]*`\s*)+")
# The site's README lists the chapters of Analysis I, and the measure theory README the sections of its chapter 1.
README_CHAPTER = re.compile(r"^- _?(?P<title>(?:Chapter (?P<chapter>\d+)|Appendix (?P<appendix>[A-Z])): .+?)_?[ \t]*$",
                            re.M)
README_GROUP = re.compile(r"^ {2}- (?P<title>Section (?P<group>\d+\.\d+): .+?)[ \t]*$", re.M)


def module_name(path: str) -> str:
    """The Lean module a file is, with «» around a component that is not an identifier."""
    parts = path.removesuffix(".lean").split("/")
    return ".".join(part if re.match(r"^[A-Za-z_][\w']*$", part) else f"«{part}»" for part in parts)


def module_file(module: str) -> str:
    return module.replace("«", "").replace("»", "").replace(".", "/") + ".lean"


def place(module: str) -> tuple[str, str, str] | None:
    """A section module's book, chapter and section number; None for a module of neither book. The measure
    theory book's chapter here is the section its subsections are in (1.1), and Notation's is 0."""
    if match := SECTION.match(module):
        if match["appendix"]:
            return ANALYSIS_I, match["appendix"], f"{match['appendix']}.{match['part']}"
        section = match["section"]
        return ANALYSIS_I, match["chapter"], (f"{match['chapter']} epilogue" if section == "epilogue"
                                              else f"{match['chapter']}.{section}")
    if match := MT_SECTION.match(module):
        if match["notation"]:
            return MEASURE_THEORY, "0", "0"
        group = f"{match['chapter']}.{match['section']}"
        return MEASURE_THEORY, group, group if match["sub"] == "0" else f"{group}.{match['sub']}"
    return None


def number_key(number: str) -> list:
    return [int(part) if part.isdigit() else part for part in re.split(r"[. ]", number)]


def title_and_doc(doc: str) -> tuple[str, str]:
    """A module docstring's title, from its first line when that is a `# ` heading and without the book's
    name, and the rest of its text."""
    first, _, rest = doc.partition("\n")
    if match := HEADING.match(first):
        return match["title"], rest.strip()
    return "", doc.strip()


def label(doc: str) -> tuple[str, str, bool] | None:
    """The book label a docstring starts with, as written, its kind (the first label's, singular), and
    whether one of its labels is an exercise."""
    match = LABEL.match(GIVEN.sub("", doc))
    if not match:
        return None
    text = match.group()
    return text, match["kind"], bool(re.search(r"(?:^|/)[ \t]*Exercises?\b", text))


def declaration_record(declaration: leansource.Declaration) -> dict:
    """What the data keeps of a declaration or an example. Its value holds `sorry` when the text after its
    statement does, or, when no `:=` or `where` ends a statement, when any of its text does."""
    sorry = declaration.proof_sorry if declaration.statement is not None else declaration.sorry
    return {"name": declaration.name, "kind": declaration.kind, "line": declaration.line, "doc": declaration.doc,
            "statement": declaration.statement, "sorry": sorry}


def unread_labels(text: str, read_lines: set[int]) -> list[dict]:
    """The labelled docstrings that no declaration or example the reading keeps carries, as on a `private`
    declaration, a notation or a structure's field, with the line of what follows each."""
    code = leansource.blank_attributes(leansource.blank(text))
    out = []
    for start, end, kind in leansource.spans(text):
        if kind != "doc":
            continue
        found = label(leansource.docstring(text[start + 3:end - 2]))
        if not found:
            continue
        after = re.search(r"\S", code[end:])
        line = code.count("\n", 0, end + after.start()) + 1 if after else code.count("\n") + 1
        if line in read_lines:
            continue
        word = re.match(r"[^\s(:]+", code[end + after.start():]).group() if after else ""
        why = ("on a private declaration, which the reading leaves out" if word == "private"
               else f"on a `{word}` command, which declares nothing the reading keeps" if word
               else "at the end of the file")
        out.append({"label": found[0], "line": line, "why": why})
    return out


def read_section(text: str, path: str) -> dict:
    """A section module's record: its title and module docstring, the modules it imports, its labelled
    items in file order, each a label with the declarations carrying it, and the declarations and examples
    with no label, counted."""
    module = module_name(path)
    book, chapter, number = place(module)
    title, doc = title_and_doc(leansource.module_doc(text) or "")
    imports = IMPORT.findall(leansource.blank(text))
    record = {"module": module, "file": path, "book": book, "chapter": chapter, "number": number, "title": title,
              "doc": doc, "imports": imports, "items": [], "unlabelled": {"declarations": 0, "examples": 0},
              "unread": []}
    read = leansource.scan_with_examples(text)
    if read is None:
        record["unread"].append({"label": "", "line": 0, "why": "its scopes do not close as they open"})
        return record
    found, examples = read
    items: dict[str, dict] = {}
    for declaration in sorted([*found.values(), *examples], key=lambda declaration: declaration.line):
        labelled = label(declaration.doc)
        if not labelled:
            record["unlabelled"]["examples" if declaration.kind == "example" else "declarations"] += 1
            continue
        text_label, kind, exercise = labelled
        if text_label not in items:
            items[text_label] = {"label": text_label, "kind": kind, "exercise": exercise, "declarations": []}
            record["items"].append(items[text_label])
        items[text_label]["declarations"].append(declaration_record(declaration))
    record["unread"] = unread_labels(text, {declaration.line for declaration in [*found.values(), *examples]})
    return record


def chapter_titles(readme: str, mt_readme: str) -> dict[str, dict[str, str]]:
    """The titles the READMEs give Analysis I's chapters and appendices, and the measure theory book's
    sections that hold subsections, from their lists of sections."""

    def listing(text: str) -> str:
        start = re.search(r"^## Sections\b.*$", text, re.M)
        if not start:
            return ""
        end = re.search(r"^## ", text[start.end():], re.M)
        return text[start.end():start.end() + end.start()] if end else text[start.end():]

    analysis_i = {match["chapter"] or match["appendix"]: match["title"] for match in README_CHAPTER.finditer(listing(readme))}
    groups = {match["group"]: match["title"] for match in README_GROUP.finditer(listing(mt_readme))}
    return {ANALYSIS_I: analysis_i, MEASURE_THEORY: groups}


def read(checkout: Path, paths: list[str]) -> dict:
    """The record of a checkout's sections, in book order, and of its other modules, from its .lean files
    under Analysis/, its literate.toml and its READMEs."""
    literate = tomllib.loads((checkout / LITERATE).read_text(encoding="utf-8"))
    order = literate.get("order_children", {}).get("Analysis", [])
    titles = {module: entry.get("title", "") for module, entry in literate.get("modules", {}).items()}
    sections, others = [], []
    by_module = {module_name(path): path for path in paths}
    for path in paths:
        module = module_name(path)
        text = (checkout / path).read_text(encoding="utf-8")
        if place(module) is None:
            title, doc = title_and_doc(leansource.module_doc(text) or "")
            others.append({"module": module, "file": path, "title": title, "doc": doc})
            continue
        sections.append(read_section(text, path))
    rank = {module: index for index, module in enumerate(order)}
    sections.sort(key=lambda section: (section["book"] != ANALYSIS_I, rank.get(section["module"], len(rank)),
                                       number_key(section["number"])))
    known = {section["module"] for section in sections}
    for section in sections:
        section["imports"] = [module for module in section["imports"] if module in known]
        if section["module"] in titles:
            section["literate_title"] = titles[section["module"]]
    readme, mt_readme = (path.read_text(encoding="utf-8") if path.is_file() else ""
                         for path in (checkout / README, checkout / MT_README))
    return {"readme": {ANALYSIS_I: paragraphs(readme), MEASURE_THEORY: paragraphs(mt_readme)},
            "chapters": chapter_titles(readme, mt_readme), "sections": sections, "others": others,
            "missing": [module for module in order if module not in by_module]}


def paragraphs(readme: str) -> list[str]:
    """A README's paragraphs between its title and its first section."""
    head = re.split(r"^## ", readme, maxsplit=1, flags=re.M)[0]
    head = re.sub(r"\A\s*# [^\n]*\n", "", head)
    return [part.strip() for part in re.split(r"\n\s*\n", head) if part.strip()]


def counts(sections: list[dict]) -> Counter:
    """The labelled items and their declarations, by book and by kind and status."""
    tally: Counter = Counter()
    for section in sections:
        tally[f"{section['book']} sections"] += 1
        for item in section["items"]:
            tally[f"{section['book']} items"] += 1
            for declaration in item["declarations"]:
                tally[f"{section['book']} declarations"] += 1
                tally[f"{section['book']} {item['kind']} {outcome(declaration, item)}"] += 1
    return tally


def outcome(declaration: dict, item: dict) -> str:
    """The status a declaration counts under: proved, stated, exercise, definition, definition sorry, axiom."""
    if declaration["kind"] == "axiom":
        return "axiom"
    if declaration["kind"] not in STATEMENT_KINDS:
        return "definition sorry" if declaration["sorry"] else "definition"
    if not declaration["sorry"]:
        return "proved"
    return "exercise" if item["exercise"] else "stated"


STATEMENT_KINDS = ("theorem", "lemma", "example")


# The chapter, from the data.

TITLE = "Analysis I and An introduction to measure theory"
SITE = "https://teorth.github.io/analysis/"
MATHLIB_REPO = "https://github.com/leanprover-community/mathlib4"
BOOK_SITES = {ANALYSIS_I: "https://terrytao.wordpress.com/books/analysis-i/",
              MEASURE_THEORY: "https://terrytao.wordpress.com/books/an-introduction-to-measure-theory/"}
NO_DEPENDS = "Its Lean file imports no other section's file."
# Whether the articles link the repository's site: a job on GitHub Actions fetched a sample of its section pages,
# Verso and doc-gen4, and the host served each (2026-11-09).
SITE_SERVED = True
STATUS = {"proved": "Proved here.", "stated": "Stated without proof.", "exercise": "An exercise, stated without proof.",
          "definition": "A definition.", "definition sorry": "A definition whose value is left as `sorry`.",
          "axiom": "An axiom."}
# Verso's markup: a role such as {name}`x` or {lean (type := "T")}`x`, and its formulas $`x` and $$`x`.
ROLE = re.compile(r"\{(?P<role>[A-Za-z][\w.]*)(?P<args>[^{}\n]*)\}(?P<ticks>`+)(?P<code>.*?)(?<!`)(?P=ticks)(?!`)", re.S)
VERSO_MATH = re.compile(r"(?<![\\$])(?P<dollars>\${1,2})(?P<ticks>`+)(?P<code>.*?)(?<!`)(?P=ticks)(?!`)", re.S)


def load(data: Path) -> dict | None:
    """data/analysis/'s source and sections, when both are there."""
    source, sections = data / "analysis" / "source.json", data / "analysis" / "sections.json"
    if not (source.is_file() and sections.is_file()):
        return None
    return json.loads(source.read_text(encoding="utf-8")) | json.loads(sections.read_text(encoding="utf-8"))


def blob(rev: str, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{REPO}/blob/{rev}/{path}" + (f"#L{line}" if line else "")


def at(rev: str) -> str:
    return f"[{rev[:8]}]({GITHUB}/{REPO}/tree/{rev})"


def markdown(verso: str) -> str:
    """Verso docstring markup as Markdown: a role's code as a code span, a role Verso hides ({given -show})
    left out, and Verso's formulas as TeX between dollars. The words are unchanged."""

    def role(match: re.Match) -> str:
        if match["role"] == "given" and re.search(r"(?:^|\s)-show\b", match["args"]):
            return ""
        return match["ticks"] + match["code"] + match["ticks"]

    text = VERSO_MATH.sub(lambda match: match["dollars"] + match["code"] + match["dollars"], ROLE.sub(role, verso))
    return text.strip()


def title_of(section: dict) -> str:
    """The section's title from its module docstring, completed from literate.toml when the docstring names
    the section only."""
    title = section["title"] or section["module"]
    literate = section.get("literate_title", "")
    if ":" not in title and ". " in literate:
        return f"{title}: {literate.split('. ', 1)[1]}"
    return title


def stem(module: str) -> str:
    return module.rsplit(".", 1)[-1].replace("«", "").replace("»", "")


def plural(count: int, word: str, words: str | None = None) -> str:
    return f"{count:,} {word if count == 1 else words or word + 's'}"


def listing(parts: list[str]) -> str:
    return ", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else "".join(parts)


def tally(items: list[dict]) -> str:
    """How a list of labelled items' declarations stand: proved, stated, exercises, definitions."""
    outcomes = Counter(outcome(declaration, item) for item in items for declaration in item["declarations"])
    stated = outcomes["stated"] + outcomes["exercise"]
    definitions = outcomes["definition"] + outcomes["definition sorry"]
    parts = [plural(outcomes["proved"], "proved here", "proved here")] if outcomes["proved"] else []
    if stated:
        parts.append(f"{stated:,} stated without proof"
                     + (f" ({outcomes['exercise']:,} of them exercises)" if outcomes["exercise"] else ""))
    if definitions:
        parts.append(plural(definitions, "definition")
                     + (f" ({outcomes['definition sorry']:,} with a value left as `sorry`)" if outcomes["definition sorry"] else ""))
    if outcomes["axiom"]:
        parts.append(plural(outcomes["axiom"], "axiom"))
    return listing(parts)


def block(item: dict, file: str, rev: str) -> str:
    """A labelled item's section of its article: its label, then each declaration carrying it, with its status,
    its docstring and its Lean statement."""
    lines = [f"## {escape(item['label'])}"]
    for declaration in item["declarations"]:
        where = f"[line {declaration['line']}]({blob(rev, file, declaration['line'])})"
        head = (f"An `example` ({where})." if declaration["kind"] == "example"
                else f"`{declaration['name']}` ({declaration['kind']}, {where}).")
        lines += ["", f"{head} {STATUS[outcome(declaration, item)]}"]
        if declaration["doc"]:
            lines += ["", quote(markdown(declaration["doc"]))]
        if declaration["statement"] is None:
            lines += ["", "Its statement is not shown: no `:=` or `where` ends it."]
        else:
            lines += ["", fence(declaration["statement"])]
    return "\n".join(lines)


def summary(section: dict) -> str:
    """The line counting a section's labelled items and declarations, the ones with no label included."""
    items = section["items"]
    declarations = sum(len(item["declarations"]) for item in items)
    if items:
        line = (f"The file has {plural(len(items), 'labelled item')}, carried by "
                f"{plural(declarations, 'declaration')}: {tally(items)}.")
    else:
        line = "The file has no labelled items."
    unlabelled = [plural(section["unlabelled"][key], word) for key, word in (("declarations", "declaration"),
                                                                             ("examples", "example"))
                  if section["unlabelled"][key]]
    if unlabelled:
        line += f" It also has {listing(unlabelled)} with no label, counted here but not shown."
    for unread in section["unread"]:
        if unread["line"]:
            line += (f" The docstring labelled {escape(unread['label'])} at line {unread['line']} is "
                     f"{unread['why']}.")
        else:
            line += f" Its declarations are not read: {unread['why']}."
    return line


def doc_links(section: dict) -> list[tuple[str, str]]:
    """The repository's own pages for a section: its Verso page, for a section of Analysis I, and its
    documentation page."""
    if not SITE_SERVED:
        return []
    path = section["module"].replace(".", "/")
    links = [("Verso page", f"{SITE}{path}/")] if section["book"] == ANALYSIS_I else []
    return links + [("Documentation", f"{SITE}docs/{path}.html")]


def article(section: dict, rev: str) -> Leaf:
    """A section's article: its module docstring, then a block per labelled item in file order."""
    file = section["file"]
    parts = [quote(markdown(section["doc"]))] if section["doc"] else []
    parts.append(f"*Quoted from [{file}]({blob(rev, file)}) in [{REPO}]({GITHUB}/{REPO}) at commit {at(rev)}, "
                 "Apache-2.0, as are the docstrings and Lean statements below.*")
    parts.append(summary(section))
    parts += [block(item, file, rev) for item in section["items"]]
    named = [declaration for item in section["items"] for declaration in item["declarations"] if declaration["name"]]
    fields = []
    if named:
        fields = [("declaration", named[0]["kind"]), ("origin", "cited"),
                  ("lean", ", ".join(declaration["name"] for declaration in named)), ("statement", "formalized")]
        if not any(declaration["sorry"] for item in section["items"] for declaration in item["declarations"]):
            fields.append(("proof", "formalized"))
    leaf = Leaf(escape(title_of(section)), slugify(stem(section["module"])), fields, "\n\n".join(parts),
                no_depends=NO_DEPENDS)
    leaf.sources = [(f"{file} at {rev[:8]}", blob(rev, file)), *doc_links(section)]
    return leaf


def others_page(others: list[dict], rev: str) -> Container:
    """The page listing the repository's modules outside both books, by title, with no articles."""
    lines = []
    for other in others:
        link = f"[`{other['module']}`]({blob(rev, other['file'])})"
        if other["title"]:
            lines.append(f"- {link}: {escape(markdown(other['title']))}.")
        elif other["doc"]:
            words = safe(opening(markdown(other["doc"])))
            lines.append(f"- {link}, whose module docstring opens “{words}”" + ("" if words.endswith((".", "…")) else "."))
        else:
            lines.append(f"- {link}, with no module docstring.")
    page = Container("Other modules", "other-modules")
    page.prose = "\n\n".join([
        f"The {plural(len(others), 'Lean module')} in [{REPO}]({GITHUB}/{REPO}) at commit {at(rev)} that belong to "
        "neither book; its README lists several of them as content unrelated to the textbook. Each is listed by the title of its module docstring, or by the docstring's opening when it has no title, "
        "quoted from the repository under its Apache-2.0 license; they have no articles.",
        "\n".join(lines),
    ])
    return page


def chapter(data: dict) -> tuple[Built, dict[str, str], list[tuple[str, str]]]:
    """The chapter's root, with its articles and counts; each labelled declaration's source line (for
    hooks/lean-links.json); and the imports that point forward in a book's order. A part per book and a page
    for the modules of neither."""
    rev, sections = data["rev"], data["sections"]
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    leaves = {section["module"]: article(section, rev) for section in sections}
    order = {section["module"]: index for index, section in enumerate(sections)}
    book_of = {section["module"]: section["book"] for section in sections}
    forward = []
    for section in sections:
        leaf = leaves[section["module"]]
        leaf.depends = [leaves[module] for module in section["imports"]]
        stats["edges"] += len(leaf.depends)
        forward += [(section["module"], module) for module in section["imports"]
                    if book_of[module] == section["book"] and order[module] > order[section["module"]]]
        stats[f"{section['book']} sections"] += 1
        for item in section["items"]:
            stats["items"] += 1
            for declaration in item["declarations"]:
                stats["declarations"] += 1
                stats[outcome(declaration, item)] += 1
                if declaration["name"]:
                    links[declaration["name"]] = blob(rev, section["file"], declaration["line"])
        stats["unread"] += len(section["unread"])
    stats["forward"] = len(forward)

    credit = (f"The titles are quoted from [{REPO}]({GITHUB}/{REPO}) at commit {at(rev)}, under its Apache-2.0 license, "
              "as are the module docstrings, docstrings and Lean statements in the articles.")
    parts = []
    for book, group_word in ((ANALYSIS_I, "chapter"), (MEASURE_THEORY, "section")):
        members = [section for section in sections if section["book"] == book]
        if not members:
            continue
        titles = data["chapters"].get(book, {})
        entries: list[Entry] = []
        groups: dict[str, Container] = {}
        for section in members:
            leaf = leaves[section["module"]]
            if section["chapter"] == "0":
                entries.append(Entry(leaf))
                continue
            if section["chapter"] not in groups:
                key = section["chapter"]
                fallback = f"Appendix {key}" if key.isalpha() else f"{group_word.capitalize()} {key}"
                group = Container(escape(titles.get(key, fallback)), slugify(fallback))
                groups[key] = group
                entries.append(Entry(group))
            groups[section["chapter"]].entries.append(Entry(leaf))
        for key, group in groups.items():
            what = ("subsections of this section" if book == MEASURE_THEORY
                    else "sections of this appendix" if key.isalpha() else "sections of this chapter")
            group.prose = f"The {what}, one article each. {credit}"
            chunk(group)
        part = Container(BOOKS[book], book, entries)
        if book == ANALYSIS_I:
            part.prose = (f"The {plural(len(members), 'section module')} of *Analysis I*, in the order of the repository's "
                          "literate.toml, on a page per chapter and appendix; a chapter's epilogue comes after its "
                          f"sections, as there. {credit}")
        else:
            part.prose = (f"The {plural(len(members), 'section module')} of *An introduction to measure theory*, in the "
                          "book's numbering: the Notation module, then the subsections of Chapter 1 on a page per "
                          f"section. {credit}")
        targets[f"analysis-{book}"] = part
        parts.append(Entry(part))
    if data["others"]:
        page = others_page(data["others"], rev)
        targets["analysis-others"] = page
        parts.append(Entry(page))
    root = Container(TITLE, "analysis", parts)
    root.prose = intro(data, stats, forward)
    stats["articles"] = len(leaves)
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items())), forward


def intro(data: dict, stats: Counter, forward: list[tuple[str, str]]) -> str:
    rev = data["rev"]
    sections = data["sections"]
    by_book = {book: [section for section in sections if section["book"] == book] for book in BOOKS}
    analysis_i, measure = by_book[ANALYSIS_I], by_book[MEASURE_THEORY]
    epilogues = sum(section["number"].endswith("epilogue") for section in analysis_i)
    appendix = sum(section["chapter"].isalpha() for section in analysis_i)
    notation = sum(section["chapter"] == "0" for section in measure)
    readme = data["readme"]
    rows = [f"- Repository: [{REPO}]({GITHUB}/{REPO}), read at commit {at(rev)} ({data['date'][:10]}), the newest "
            "commit on its main branch whose “Build book” run passed.",
            f"- Lean toolchain {data['toolchain']}, Mathlib at [{data['mathlib'][:8]}]({MATHLIB_REPO}/tree/{data['mathlib']}).",
            "- License: Apache-2.0.",
            f"- Written by Terence Tao, with the repository's [contributors]({GITHUB}/{REPO}/graphs/contributors)."]
    if SITE_SERVED:
        rows.append(f"- Its site, {SITE}, has a Verso page for each section of Analysis I and doc-gen4 documentation "
                    "for every module; each article links its section's pages.")
    books = []
    for book, members in by_book.items():
        items = [item for section in members for item in section["items"]]
        if items:
            books.append(f"In {BOOKS[book]}, {plural(len(items), 'item')} carried by "
                         f"{plural(sum(len(item['declarations']) for item in items), 'declaration')}: {tally(items)}.")
    statuses = [
        "- “Proved here.”: a theorem, lemma or example whose proof, its text from that `:=` on, holds no `sorry`. "
        "This says nothing of the results the proof uses, which may themselves be stated without proof.",
        "- “Stated without proof.”: a theorem, lemma or example whose proof holds `sorry`; “An exercise, stated "
        "without proof.” when its label names an exercise.",
        "- “A definition.”: any other declaration (a `def`, `abbrev`, `structure`, `class`, `inductive` or "
        "`instance`) whose value holds no `sorry`; “A definition whose value is left as `sorry`.” when it does.",
    ]
    if stats["axiom"]:
        statuses.append("- “An axiom.”: an `axiom` declaration, which has no proof.")
    unread = stats["unread"]
    names = {section["module"]: title_of(section) for section in sections}
    edges = (f"An edge from one section to another means that the first section's Lean file imports the other's: "
             f"{plural(stats['edges'], 'import')} between sections in all. It says nothing of which results use "
             "which. Each article lists them as what it depends on, shown on the site as “Statement uses”; its imports "
             "of Mathlib and of modules outside both books are not shown. ")
    if forward:
        edges += (f"{plural(len(forward), 'import points', 'imports point')} forward in its book's order: "
                  + listing([f"{escape(names[source])} imports {escape(names[target])}" for source, target in forward]) + ".")
    else:
        edges += "No import points forward in its book's order."
    return "\n\n".join(part for part in [
        f"[{REPO}]({GITHUB}/{REPO}) is Terence Tao's Lean companion to his textbook "
        f"[*Analysis I*]({BOOK_SITES[ANALYSIS_I]}), with a companion to his book "
        f"[*An introduction to measure theory*]({BOOK_SITES[MEASURE_THEORY]}) in `Analysis/MeasureTheory/`. Its "
        "README says:",
        quote("\n\n".join(readme[ANALYSIS_I][:2])) if readme[ANALYSIS_I] else "",
        "and the README of its measure theory companion:" if readme[MEASURE_THEORY] else "",
        quote("\n\n".join(readme[MEASURE_THEORY][:2])) if readme[MEASURE_THEORY] else "",
        "So the exercises are left as `sorry` by design, as the first README says.",
        "\n".join(["## Facts", "", *rows]),
        "## This map",
        f"This chapter has an article for each of the {plural(len(sections), 'section module')} at that commit: "
        f"{len(analysis_i)} of [Analysis I](trough:analysis-{ANALYSIS_I}) ({len(analysis_i) - epilogues - appendix} "
        f"sections, {epilogues} chapter epilogues and {appendix} appendix sections), on a page per chapter, and "
        f"{len(measure)} of [An introduction to measure theory](trough:analysis-{MEASURE_THEORY}) "
        f"({'its Notation module and ' if notation else ''}{len(measure) - notation} sections), on a page per section "
        "of its Chapter 1. An article quotes its section's module docstring, then has a block for each label of the "
        "book that a docstring in the file starts with (“Definition 6.1.3”, “Exercise 6.1.2”), in file order: the "
        "declarations carrying that label, each with its docstring, its Lean statement, its line in the source and "
        "its status. Several declarations can carry one label, and an `example`, which has no name, counts as a "
        "declaration. Declarations whose docstring starts with no label are counted in each article but not shown."
        + (f" [Other modules](trough:analysis-others) lists the {plural(len(data['others']), 'module')} that belong "
           "to neither book." if data["others"] else ""),
        f"There are {plural(stats['items'], 'labelled item')}, carried by {plural(stats['declarations'], 'declaration')}. "
        + " ".join(books),
        "No Lean is run for this chapter. Statuses are read from the source text: a declaration's Lean statement is "
        "its text up to the `:=` or `where` that starts its value, and its status reads that value.",
        "\n".join(statuses),
        "A label is the kind and number a docstring starts with, after any Verso `{given}` role. A `private` "
        "declaration is not read, as Lean renames it, and neither is a notation"
        + (f"; {plural(unread, 'labelled docstring is', 'labelled docstrings are')} on such a declaration, as "
           f"{'its article says' if unread == 1 else 'their articles say'}." if unread else "."),
        "The docstrings are written in Verso's markup. The pages show a role such as `` {name}`x` `` as the code "
        "`x`, leave out the variables a `{given -show}` role names, as Verso's own pages do, and show Verso's "
        "formulas, `` $`x` ``, in TeX. The words are the repository's.",
        edges,
        f"The titles, module docstrings, docstrings, Lean statements and README text are quoted from [{REPO}]"
        f"({GITHUB}/{REPO}) at commit {at(rev)}, under its Apache-2.0 license; the books themselves are not quoted.",
    ] if part)
