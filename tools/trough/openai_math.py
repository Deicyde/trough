"""The chapter on OpenAI Math: an article per result family of OpenAI's manuscript collection.

openai/math holds research manuscripts written by an OpenAI model, 721 of them in
373 result families at the time of writing, and Lean formalizations of some of
their results. CONTENTS.md lists the families in order, each with its
description and its manuscripts' titles, PDFs and abstracts; overview.tex files
the families under subjects. A family with Lean has a page, lean/docs/NNN.md,
whose scope section says what the Lean covers and whose table links a statement
file under lean/ComparatorChallenges/ for each formalized result. Each statement
file has a configuration beside it that names the declarations it states and the
module whose declarations of the same names prove them. tools/refresh_openai_math.py
reads a checkout at a pinned commit into data/openai-math/: the subjects and
families, the manuscripts, the Lean pages, each statement as the statement file
writes it, and where the repository's Lean declares its proof, read by
trough.leansource without Lean. The chapter has a part per subject and an article
per family, with a block per manuscript and per formalized result. The articles
have no edges.
"""

from __future__ import annotations

import json
import posixpath
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote as percent

import yaml

from . import leansource
from .blueprints import Built, escape
from .formal_conjectures import OPAQUE, natural, plural
from .vault import Container, Entry, Leaf, chunk, slugify

SCHEMA = "trough-openai-math/v1"
REPO = "openai/math"
GITHUB = "https://github.com"
TITLE = "OpenAI Math: a model's research manuscripts and their Lean (OpenAI)"
# A cell of CONTENTS.md's table, a family or a manuscript.
CELL = re.compile(r"<td>\n\n(?P<cell>.*?)\n\n</td>", re.S)
FAMILY = re.compile(r"\*\*(?P<number>\d{3})\. (?P<title>.+?)\*\*\s*(?P<description>.*)", re.S)
# A manuscript's title links its PDF; a URL may hold balanced parentheses.
MANUSCRIPT = re.compile(r"&emsp;\[(?P<title>(?:[^\[\]\n]|\[[^\[\]\n]*\])*)\]\((?P<path>(?:[^()\s]|\([^()\s]*\))+)\)"
                        r"(?P<note>[^\n]*)(?:\n\n(?P<abstract>.*))?", re.S)
LEAN_LINK = re.compile(r"\s*\(\[Lean\]\((?P<doc>lean/docs/\d+\.md)\)\)\s*$")
SUBJECT = re.compile(r"\\cataloguesection\{(?P<title>[^{}]*)\}")
ENTRY = re.compile(r"\\resultentry\{(?P<number>\d{3})\}")
HEADING = re.compile(r"^# (?P<title>.+?)\s*$")
LINK = re.compile(r"(?<!!)\[(?P<text>(?:[^\[\]\n]|\[[^\[\]\n]*\])*)\]\((?P<target>(?:[^()\s]|\([^()\s]*\))+)\)")
IMPORT = re.compile(r"^import\s+(?P<module>OAI(?:\.[^\s.]+)+)\s*$", re.M)
# GitHub's inline formula, $`...`$, and the HTML CONTENTS.md writes.
GITHUB_MATH = re.compile(r"\$`(?P<tex>.+?)`\$", re.S)
SCRIPT = re.compile(r"<(?P<tag>sup|sub)>(?P<inner>.*?)</(?P=tag)>", re.S)
ITALIC = re.compile(r"<i>(?P<inner>.*?)</i>", re.S)
# An italic symbol with its superscripts and subscripts, which make one formula.
SCRIPTED = re.compile(r"<i>(?P<base>[^<\s]{1,12})</i>(?P<scripts>(?:<(?:sup|sub)>.*?</(?:sup|sub)>)+)", re.S)
ENTITY = re.compile(r"&(?:#(?P<number>[0-9]+)|(?P<name>gt|lt|amp|emsp|nbsp|quot));")
NAMED = {"gt": ">", "lt": "<", "amp": "&", "emsp": "", "nbsp": " ", "quot": '"'}
UNESCAPED_BRACE = re.compile(r"(?<!\\)\{")
NO_DEPENDS = "No dependencies are recorded: the collection records none between its families."
LEAN_NAMES = 8  # the names a card's Lean row shows
# The bytes of article Markdown a listing page folds in before its next article starts a page.
PAGE_BUDGET = 300_000


# Reading the collection.

def markdown(text: str) -> str:
    """CONTENTS.md's text as the site's Markdown: GitHub's $`...`$ formulas as $...$, superscripts and subscripts
    as formulas, italics as emphasis and character references as their characters, which the site requires."""
    def scripts(text: str) -> str:
        return SCRIPT.sub(lambda match: ("^" if match["tag"] == "sup" else "_") + "{"
                          + ITALIC.sub(r"\g<inner>", match["inner"]).strip() + "}", text)

    text = GITHUB_MATH.sub(lambda match: f"${match['tex'].strip()}$", text)
    text = SCRIPTED.sub(lambda match: f"${match['base']}{scripts(match['scripts'])}$", text)
    text = SCRIPT.sub(lambda match: f"${scripts(match.group())}$", text)
    text = ITALIC.sub(lambda match: f"*{match['inner'].strip()}*", text)
    text = ENTITY.sub(lambda match: chr(int(match["number"])) if match["number"] else NAMED[match["name"]], text)
    return text.strip()


def read_contents(text: str) -> tuple[list[dict], list[str]]:
    """CONTENTS.md's families in order, each with its number, title, description, Lean page and manuscripts."""
    families: list[dict] = []
    problems: list[str] = []
    for match in CELL.finditer(text):
        cell = match["cell"].strip()
        if family := FAMILY.fullmatch(cell):
            description = family["description"].strip()
            lean = LEAN_LINK.search(description)
            families.append({"number": family["number"], "title": markdown(family["title"]).rstrip("."),
                             "description": markdown(description[: lean.start()] if lean else description),
                             "doc": lean["doc"] if lean else None, "manuscripts": []})
        elif manuscript := MANUSCRIPT.fullmatch(cell):
            if not families:
                problems.append("CONTENTS.md lists a manuscript before any family")
                continue
            families[-1]["manuscripts"].append({
                "title": markdown(manuscript["title"]), "path": manuscript["path"],
                "note": markdown(manuscript["note"]).lstrip(" —-").strip(),
                "abstract": markdown(manuscript["abstract"] or "")})
        else:
            problems.append(f"CONTENTS.md has a cell that is neither a family nor a manuscript: {cell[:80]!r}")
    numbers = Counter(family["number"] for family in families)
    problems += [f"CONTENTS.md lists family {number} {count} times" for number, count in numbers.items() if count > 1]
    problems += [f"CONTENTS.md: family {family['number']} has no manuscripts" for family in families
                 if not family["manuscripts"]]
    return families, problems


def read_overview(text: str) -> list[dict]:
    """The subjects overview.tex files the families under, in its order, each with its families' numbers."""
    marks = sorted([(match.start(), "subject", match["title"]) for match in SUBJECT.finditer(text)]
                   + [(match.start(), "entry", match["number"]) for match in ENTRY.finditer(text)])
    subjects: list[dict] = []
    for _, kind, value in marks:
        if kind == "subject":
            subjects.append({"title": value.replace("--", "–"), "families": []})
        elif subjects:
            subjects[-1]["families"].append(value)
    return subjects


def section(text: str, heading: str) -> str | None:
    """The text under a `## heading` of a Lean page, to the next `## ` heading."""
    match = re.search(rf"(?m)^## {re.escape(heading)}\s*$", text)
    if not match:
        return None
    rest = text[match.end():]
    end = re.search(r"(?m)^## ", rest)
    return (rest[: end.start()] if end else rest).strip()


def read_doc(text: str, path: str) -> tuple[dict, list[str]]:
    """A family's Lean page: its title, the papers it names, its scope and its results, each a label and the
    statement file it links."""
    lines = text.split("\n")
    title = HEADING.match(lines[0]) if lines else None
    scope, table = section(text, "Scope"), section(text, "Comparator links")
    if not title or scope is None or table is None:
        return {}, [f"{path} lacks its title, its Scope section or its Comparator links section"]
    problems: list[str] = []
    papers = [posixpath.normpath(posixpath.join(posixpath.dirname(path), match["target"]))
              for match in LINK.finditer(text[: text.find("## Scope")]) if match["target"].endswith(".pdf")]
    results = []
    for row in table.split("\n"):
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if not row.startswith("|") or len(cells) < 2 or set(row) <= set("|- ") or cells[-1] == "Comparator statement":
            continue
        links = list(LINK.finditer(cells[-1]))
        if len(links) != 1:
            problems.append(f"{path}: a Comparator links row does not link one statement file: {row[:80]!r}")
            continue
        target, _, fragment = links[0]["target"].partition("#")
        result = {"label": " | ".join(cells[:-1]),
                  "challenge": posixpath.normpath(posixpath.join(posixpath.dirname(path), target))}
        # A row may link one declaration of a statement file by its line.
        if line := re.fullmatch(r"L(\d+)", fragment):
            result["line"] = int(line[1])
        results.append(result)
    if not results:
        problems.append(f"{path} links no statement file")
    return {"path": path, "title": title["title"], "papers": papers, "scope": scope, "results": results}, problems


def read_configs(lean: Path) -> tuple[dict[str, dict], list[str]]:
    """Each statement file's configuration, by the statement file's path under the repository, from the
    configuration's challenge_module."""
    configs: dict[str, dict] = {}
    problems: list[str] = []
    for path in sorted((lean / "ComparatorChallenges").rglob("*.json"), key=lambda path: natural(path.as_posix())):
        name = path.relative_to(lean.parent).as_posix()
        try:
            config = json.loads(path.read_text(encoding="utf-8"))
            module = config["challenge_module"]
            config = {"config": name, "challenge_module": module, "solution_module": config["solution_module"],
                      "theorems": list(config.get("theorem_names") or []),
                      "definitions": list(config.get("definition_names") or [])}
        except (ValueError, KeyError, TypeError) as error:
            problems.append(f"{name} does not read: {error!r}")
            continue
        configs["lean/" + module.replace(".", "/") + ".lean"] = config
    return configs, problems


def module_path(module: str) -> str:
    return "lean/" + module.replace(".", "/") + ".lean"


def solution_files(checkout: Path) -> list[str]:
    """The files the refresh reads proofs from: each solution module and, for one that is checked out but does not
    declare every name its configuration names, the OAI modules it imports. A sparse checkout adds these in two
    rounds."""
    configs, _ = read_configs(checkout / "lean")
    wanted = {module_path(config["solution_module"]) for config in configs.values()}
    for config in configs.values():
        path = checkout / module_path(config["solution_module"])
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        declared = {declaration.name for declaration in leansource.declarations(text, relaxed=True) or []}
        if not set(config["theorems"] + config["definitions"]) <= declared:
            wanted |= {module_path(match["module"]) for match in IMPORT.finditer(leansource.blank(text))}
    return sorted(wanted, key=natural)


def read_main_results(checkout: Path) -> tuple[set[str], list[str]]:
    """The statement files of formalization.yaml's main results, by their configurations' paths."""
    path = checkout / "lean" / "formalization.yaml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        rows = data["status"]["main_results"]
    except (OSError, yaml.YAMLError, KeyError, TypeError) as error:
        return set(), [f"lean/formalization.yaml does not read: {error!r}"]
    return {"lean/" + row["comparator_config"] for row in rows if isinstance(row, dict) and row.get("comparator_config")}, []


class Lean:
    """The declarations of the files read so far, by file."""

    def __init__(self, checkout: Path):
        self.checkout = checkout
        self.files: dict[str, dict[str, leansource.Declaration] | None] = {}
        self.counts: Counter = Counter()

    def declared(self, path: str) -> dict[str, leansource.Declaration] | None:
        if path not in self.files:
            file = self.checkout / path
            if not file.is_file():
                self.files[path] = None
            else:
                found = leansource.declarations(file.read_text(encoding="utf-8"), relaxed=True)
                self.counts["lean_files"] += 1
                self.counts["unread_files"] += found is None
                self.files[path] = {declaration.name: declaration for declaration in found or []
                                    if declaration.name and not declaration.private}
        return self.files[path]

    def find(self, name: str, module: str) -> dict | None:
        """Where the solution module, or a module it imports, declares *name*."""
        path = module_path(module)
        candidates = [path]
        if (self.checkout / path).is_file():
            candidates += [module_path(match["module"]) for match in
                           IMPORT.finditer(leansource.blank((self.checkout / path).read_text(encoding="utf-8")))]
        for candidate in candidates:
            found = (self.declared(candidate) or {}).get(name)
            if found:
                return {"file": candidate, "line": found.line, "kind": found.kind, "sorry": found.proof_sorry}
        return None


def read(checkout: Path) -> tuple[dict, dict[str, list[dict]], dict, list[str]]:
    """The collection's subjects, its families by subject (with their Lean), the counts, and what does not read."""
    problems: list[str] = []
    try:
        families, found = read_contents((checkout / "CONTENTS.md").read_text(encoding="utf-8"))
        subjects = read_overview((checkout / "overview.tex").read_text(encoding="utf-8"))
    except OSError as error:
        return {}, {}, {}, [f"{error.filename} does not read"]
    problems += found
    by_number = {family["number"]: family for family in families}
    filed = [number for subject in subjects for number in subject["families"]]
    problems += [f"overview.tex files family {number}, which CONTENTS.md does not list"
                 for number in filed if number not in by_number]
    problems += [f"overview.tex does not file family {number}" for number in by_number if number not in set(filed)]
    problems += [f"overview.tex files family {number} more than once"
                 for number, count in Counter(filed).items() if count > 1]
    configs, found = read_configs(checkout / "lean")
    problems += found
    main, found = read_main_results(checkout)
    problems += found
    lean = Lean(checkout)
    counts: Counter = Counter()
    for family in families:
        counts["families"] += 1
        counts["manuscripts"] += len(family["manuscripts"])
        if not family["doc"]:
            family["lean"] = None
            continue
        file = checkout / family["doc"]
        if not file.is_file():
            problems.append(f"family {family['number']} links {family['doc']}, which is missing")
            family["lean"] = None
            continue
        doc, found = read_doc(file.read_text(encoding="utf-8"), family["doc"])
        problems += found
        if not doc:
            family["lean"] = None
            continue
        counts["families_with_lean"] += 1
        for result in doc["results"]:
            counts["results"] += 1
            config = configs.get(result["challenge"])
            if config is None:
                problems.append(f"{family['doc']} links {result['challenge']}, which has no configuration")
                continue
            result |= {"config": config["config"], "main": config["config"] in main, "statements": []}
            counts["results_main"] += result["main"]
            stated = lean.declared(result["challenge"])
            if stated is None:
                problems.append(f"{result['challenge']} is missing or its scopes don't close")
                continue
            named = [(name, "theorem") for name in config["theorems"]] + [
                (name, "definition") for name in config["definitions"]]
            if "line" in result:
                # A row that links a line states the declaration there, or the first one after it.
                after = sorted((stated[name].line, name, kind) for name, kind in named
                               if name in stated and stated[name].line >= result["line"])
                exact = [(name, kind) for line, name, kind in after if line == result["line"]]
                named = exact or [(name, kind) for _, name, kind in after[:1]]
                if not named:
                    problems.append(f"{family['doc']} links line {result['line']} of {result['challenge']}, after "
                                    "every declaration its configuration names")
            for name, kind in named:
                declaration = stated.get(name)
                if declaration is None or declaration.statement is None:
                    problems.append(f"{result['challenge']} does not state {name}, which {config['config']} names")
                    continue
                proof = lean.find(name, config["solution_module"])
                counts["statements"] += 1
                counts["proofs_found" if proof else "proofs_not_found"] += 1
                counts["proofs_with_sorry"] += bool(proof and proof["sorry"])
                result["statements"].append({"name": name, "role": kind, "kind": declaration.kind,
                                             "line": declaration.line, "statement": declaration.statement,
                                             "proof": proof, "module": module_path(config["solution_module"])})
        family["lean"] = doc
    counts["lean_files"], counts["unread_files"] = lean.counts["lean_files"], lean.counts["unread_files"]
    counts["subjects"] = len(subjects)
    counts["main_results"] = len(main)
    linked = {result.get("config") for family in families if family.get("lean") for result in family["lean"]["results"]}
    counts["main_results_unlinked"] = len(main - linked)
    by_subject = {subject["title"]: [by_number[number] for number in subject["families"] if number in by_number]
                  for subject in subjects}
    return {"subjects": subjects}, by_subject, dict(sorted(counts.items())), problems


# The chapter, from the data.

def load(data: Path) -> dict | None:
    """data/openai-math/'s source, structure and families, when they are there."""
    directory = data / "openai-math"
    shards = sorted((directory / "families").glob("*.json"))
    if not ((directory / "source.json").is_file() and (directory / "structure.json").is_file() and shards):
        return None
    families = {family["number"]: family for shard in shards
                for family in json.loads(shard.read_text(encoding="utf-8"))["families"]}
    return {"source": json.loads((directory / "source.json").read_text(encoding="utf-8")),
            "structure": json.loads((directory / "structure.json").read_text(encoding="utf-8")), "families": families}


def blob(source: dict, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{source['repo']}/blob/{source['rev']}/{percent(path)}" + (f"#L{line}" if line else "")


def at(source: dict) -> str:
    return f"[{source['rev'][:8]}]({GITHUB}/{source['repo']}/tree/{source['rev']})"


def braces(text: str) -> str:
    """Each brace outside code and formulas escaped: a line that ends in `{...}` would be read as an attribute list,
    which the site does not publish."""
    parts, last = [], 0
    for match in OPAQUE.finditer(text):
        parts += [UNESCAPED_BRACE.sub(r"\\{", text[last:match.start()]), match.group()]
        last = match.end()
    return "".join(parts) + UNESCAPED_BRACE.sub(r"\\{", text[last:])


def relink(text: str, directory: str, source: dict) -> str:
    """The relative links of the collection's text pointed at its files at the pin. A URL stays as it is."""
    def link(match: re.Match) -> str:
        target = match["target"]
        if "://" in target or target.startswith(("#", "mailto:")):
            return match.group()
        return f"[{match['text']}]({blob(source, posixpath.normpath(posixpath.join(directory, target)))})"

    return LINK.sub(link, text)


def proof_line(statement: dict, source: dict) -> str:
    proof = statement["proof"]
    if proof is None:
        return (f"Its proof is in [{statement['module']}]({blob(source, statement['module'])}) or a file it imports "
                "further down, which this chapter does not read.")
    where = f"[{proof['file']}, line {proof['line']}]({blob(source, proof['file'], proof['line'])})"
    if proof["sorry"]:
        return f"Declared in {where}, where its value contains `sorry`."
    return f"{'Defined' if statement['role'] == 'definition' else 'Proved'} in {where}."


def result_block(result: dict, source: dict) -> str:
    lines = [f"## Lean: {braces(result['label'])}", ""]
    challenge = f"[{posixpath.basename(result['challenge'])}]({blob(source, result['challenge'])})"
    lines += [f"Stated in {challenge}"
              + ("; one of the main results in the repository's formalization.yaml." if result.get("main") else "."),
              ""]
    for statement in result.get("statements", []):
        lines += ["```lean", statement["statement"], "```", "", proof_line(statement, source), ""]
    return "\n".join(lines).rstrip()


def manuscript_block(manuscript: dict, source: dict, formalized: bool) -> str:
    lines = [f"## {braces(manuscript['title'])}", ""]
    if manuscript["abstract"]:
        lines += [braces(manuscript["abstract"]), ""]
    tail = f"[The manuscript]({blob(source, manuscript['path'])})"
    if manuscript["note"]:
        tail += f", {manuscript['note']}"
    lines.append(tail + ("; the Lean below formalizes results from it." if formalized else "."))
    return "\n".join(lines)


def tally(families: list[dict]) -> Counter:
    counts: Counter = Counter()
    for family in families:
        counts["families"] += 1
        counts["manuscripts"] += len(family["manuscripts"])
        if family["lean"]:
            counts["formalized"] += 1
            for result in family["lean"]["results"]:
                for statement in result.get("statements", []):
                    counts["statements"] += 1
                    proof = statement["proof"]
                    counts["proved" if proof and not proof["sorry"] else "unproved"] += 1
    return counts


def article(family: dict, data: dict, links: dict[str, str]) -> Leaf:
    """A family's article: a line placing it, its description, a block per manuscript and, when it has Lean, the
    Lean page's scope and a block per result."""
    source = data["source"]
    counts = tally([family])
    lean = family["lean"]
    opening = (f"{plural(counts['manuscripts'], 'manuscript')}"
               + (f" and {plural(counts['statements'], 'Lean statement')}" if counts["statements"] else
                  ", with no Lean" if not lean else "")
               + f", quoted from [{source['repo']}]({GITHUB}/{source['repo']}) at commit {at(source)}.")
    parts = [opening, braces(family["description"])]
    papers = set(lean["papers"]) if lean else set()
    parts += [manuscript_block(manuscript, source, manuscript["path"] in papers)
              for manuscript in family["manuscripts"]]
    if lean:
        parts.append("## The Lean formalization\n\n" + braces(relink(lean["scope"], posixpath.dirname(lean["path"]),
                                                                    source)))
        parts += [result_block(result, source) for result in lean["results"] if "config" in result]
    names = [statement["name"] for result in (lean["results"] if lean else []) for statement in result.get("statements", [])
             if statement["proof"]]
    fields = [("declaration", "section"), ("origin", "cited")]
    if names:
        shown = list(dict.fromkeys(names))[:LEAN_NAMES]
        fields += [("lean", ", ".join(shown)), ("statement", "formalized")]
        if counts["proved"] == counts["statements"]:
            fields.append(("proof", "formalized"))
        for result in lean["results"]:
            for statement in result.get("statements", []):
                if statement["name"] in shown and statement["proof"]:
                    links[statement["name"]] = blob(source, statement["proof"]["file"], statement["proof"]["line"])
    title = f"{family['number']}. {family['title']}"
    leaf = Leaf(escape(title), slugify(title), fields, "\n\n".join(parts), no_depends=NO_DEPENDS)
    leaf.sources = [(f"{source['repo']} at {source['rev'][:8]}: CONTENTS.md", blob(source, "CONTENTS.md"))]
    if lean:
        leaf.sources.append((f"{source['repo']} at {source['rev'][:8]}: {lean['path']}", blob(source, lean["path"])))
    return leaf


def credit(source: dict) -> str:
    return (f"The descriptions, titles, abstracts, Lean pages and statements are quoted from "
            f"[{source['repo']}]({GITHUB}/{source['repo']}) at commit {at(source)}, under its Apache-2.0 license.")


def described(counts: Counter) -> str:
    """How many families have Lean, and how many of their statements are proved in a file read, in words."""
    if not counts["statements"]:
        return "none with Lean"
    proved = ("all proved" if counts["proved"] == counts["statements"] else f"{counts['proved']:,} of them proved")
    return (f"{counts['formalized']:,} with Lean: {plural(counts['statements'], 'statement')}, {proved} in a file "
            "this chapter reads")


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and the links of the names its cards' Lean rows show (for
    hooks/lean-links.json). A part per subject, an article per family."""
    source, structure, families = data["source"], data["structure"], data["families"]
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    parts = []
    for subject in structure["subjects"]:
        members = [families[number] for number in subject["families"] if number in families]
        container = Container(escape(subject["title"]), slugify(subject["title"]))
        for family in members:
            leaf = article(family, data, links)
            targets[f"openai-math-{family['number']}"] = leaf
            container.entries.append(Entry(leaf))
        counts = tally(members)
        stats.update(counts)
        container.prose = "\n\n".join([
            f"{plural(counts['families'], 'result family', 'result families')} in *{escape(subject['title'])}*, "
            f"with {plural(counts['manuscripts'], 'manuscript')}; {described(counts)}.", credit(source)])
        chunk(container, budget=PAGE_BUDGET)
        targets[f"openai-math-{slugify(subject['title'])}"] = container
        parts.append(Entry(container))
        stats["parts"] += 1
    root = Container(TITLE, "openai-math", parts)
    root.prose = intro(data, stats)
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items()))


def intro(data: dict, stats: Counter) -> str:
    source = data["source"]
    counts = source["counts"]
    unlinked = counts.get("main_results_unlinked", 0)
    return "\n\n".join([
        f"[OpenAI Math]({GITHUB}/{source['repo']}) is a collection of mathematical manuscripts written by an OpenAI "
        "model, which its README calls raw research data rather than polished papers, with Lean formalizations of "
        f"some of their results. This chapter maps it at commit {at(source)} ({source['date'][:10]}).",
        f"Its {plural(stats['manuscripts'], 'manuscript')} form "
        f"{plural(stats['families'], 'result family', 'result families')}, an article each, under the "
        f"{plural(stats['parts'], 'subject')} of its overview; {described(stats)}.",
        "No Lean is run here. Each statement is quoted from the repository's statement file, which leaves its proof "
        "as `sorry` by design; its proof is the declaration of the same name in the solution module the statement's "
        "configuration names, or in a module that one imports, read from the source text. A statement is proved "
        "here when that declaration's value holds no `sorry`, whatever it uses. "
        + (f"{plural(unlinked, 'main result')} of the repository's formalization.yaml "
           f"{'is' if unlinked == 1 else 'are'} not linked from any family's Lean page. " if unlinked else "")
        + "The families have no recorded dependencies.",
        credit(source),
    ])
