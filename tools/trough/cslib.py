"""The CSLib chapter: the Lean Computer Science Library, a module per article.

leanprover/cslib organizes its Lean in folders under Cslib/, one area each (Foundations, Computability,
Languages, Logics, Algorithms, Crypto and smaller ones), and documents each module the way Mathlib does: a module
docstring with a `#` title, its main definitions and statements, and a docstring on each definition.
tools/refresh_cslib.py reads a checkout at a pinned commit into data/cslib/ without Lean: each module's title,
docstrings, the authors its header names and its public declarations, as trough.leansource reads them, with the
area READMEs' descriptions. The chapter has a part per area, a page per folder and an article per module, with a
block per declaration in file order.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from . import leansource
from .ff import is_apache
from .formal_conjectures import module_name

SCHEMA = "trough-cslib/v1"
REPO = "leanprover/cslib"
GITHUB = "https://github.com"
LIBRARY = "Cslib"
INDEX = "Cslib.lean"
# A header's copyright holders and its optional list of authors, which AUTHORS.md says name a file's authors.
COPYRIGHT = re.compile(r"^Copyright \(c\) \d{4}(?:[-–]\d{4})? (?P<holders>.+?)\.? All rights reserved\.?$", re.M)
AUTHORS = re.compile(r"^Authors?:[ \t]*(?P<authors>.+(?:\n(?![A-Z][a-z]+:)[ \t]*\S.*)*)", re.M)
# A section of a README or docstring that says what the library plans, not what it has.
PLANS = re.compile(r"^(?:plans?|future work|todo|roadmap)\b", re.I)
HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
TODO_LINE = re.compile(r"^[ \t]*(?:[-*][ \t]+)?TODO\b")
# Definitions whose whole text is shown: their fields or constructors say what they are.
WHOLE = ("structure", "class", "inductive")


def without_plans(markdown: str) -> str:
    """The Markdown without its sections on plans, future work or TODOs, each up to the next heading of its level
    or above, and without lines that start with TODO; a cut inside the text is marked with …"""
    out: list[str] = []
    skipping: int | None = None
    fence = False
    for line in markdown.split("\n"):
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        heading = None if fence else HEADING.match(line)
        if heading and skipping is not None and len(heading.group(1)) <= skipping:
            skipping = None
        if skipping is not None:
            continue
        if heading and PLANS.match(heading.group(2).strip("*_ ")):
            skipping = len(heading.group(1))
            out.append("…")
            continue
        if not fence and TODO_LINE.match(line):
            out.append("…")
            continue
        out.append(line)
    text = "\n".join(out)
    # Consecutive cuts are one, and a cut at the end of the text is no mark.
    text = re.sub(r"…(?:\s*\n\s*…)+", "…", text)
    return re.sub(r"(?:\s*\n)*\s*…\s*\Z", "", text).strip()


def header(text: str) -> dict:
    """The copyright holders and the authors the file's opening comment names."""
    spans = leansource.spans(text)
    first = spans[0] if spans and spans[0][2] == "comment" and not text[:spans[0][0]].strip() else None
    comment = text[first[0] + 2:first[1] - 2] if first else ""
    holders, authors = COPYRIGHT.search(comment), AUTHORS.search(comment)
    return {"copyright": holders["holders"].strip() if holders else "",
            "authors": " ".join(authors["authors"].split()) if authors else ""}


def readme_text(text: str) -> str:
    """A README's text after its copyright block and title, without its plans."""
    text = re.sub(r"(?s)\A\s*<pre>.*?</pre>\s*", "", text)
    text = re.sub(r"\A\s*#[ \t]+[^\n]*\n", "", text)
    return without_plans(text)


def statement_of(text: str, declaration: leansource.Declaration) -> str:
    """What a block shows of a declaration: a structure's, class's or inductive type's whole text, with its fields
    or constructors; any other's statement, the text up to the `:=` or `where` that starts its value, or its header
    when neither ends it, as for a definition by cases."""
    if declaration.kind in WHOLE or declaration.statement is None:
        return whole(text, declaration.line, declaration.kind not in WHOLE)
    return declaration.statement


def whole(text: str, line: int, header_only: bool = False) -> str:
    """A declaration's text from its keyword's line while lines are indented, blank or a `deriving` clause; with
    *header_only*, it also stops at a line that starts a `|` case."""
    lines = leansource.blank_attributes(leansource.blank(text)).split("\n")
    source = text.split("\n")
    column = len(lines[line - 1]) - len(lines[line - 1].lstrip())
    kept = [source[line - 1][column:]]
    for number in range(line, len(lines)):
        code = lines[number]
        stripped = code.strip()
        if header_only and (not stripped or stripped.startswith("|")):
            break
        if stripped and len(code) - len(code.lstrip()) <= column and not stripped.startswith("deriving"):
            break
        kept.append(source[number])
    return leansource.dedent("\n".join(kept).rstrip(), column)


def read_module(text: str, path: str) -> dict:
    """A module's record: its title, docstrings and public declarations in file order; `items` is None when its
    scopes don't close as they open. The module docstring is the first `/-! ... -/` before any declaration; each
    later one is an item of its own, where the file writes it."""
    found = leansource.declarations(text)
    record = {"module": module_name(path), "file": path, **header(text), "title": "", "doc": "", "items": None}
    if found is None:
        return record
    first_line = min((declaration.line for declaration in found), default=None)
    notes, opened = [], False
    for start, end, kind in leansource.spans(text):
        if kind != "module doc":
            continue
        line = text.count("\n", 0, start) + 1
        doc = leansource.docstring(text[start + 3:end - 2])
        if not opened and (first_line is None or line < first_line):
            opened = True
            title = HEADING.match(doc.split("\n", 1)[0])
            if title and len(title.group(1)) == 1:
                record["title"], doc = title.group(2), doc.split("\n", 1)[1] if "\n" in doc else ""
            record["doc"] = without_plans(doc)
        elif cut := without_plans(doc):
            notes.append({"line": line, "note": cut})
    declarations = [{"name": declaration.name, "kind": declaration.kind, "line": declaration.line,
                     "doc": declaration.doc, "statement": statement_of(text, declaration),
                     "sorry": declaration.proof_sorry if declaration.statement is not None else declaration.sorry}
                    for declaration in found if declaration.name and not declaration.private]
    record["items"] = sorted(notes + declarations, key=lambda item: item["line"])
    return record


def maintainers(governance: str) -> list[dict]:
    """The maintainers GOVERNANCE.md names, by role: the lead maintainer, technical leads and area maintainers,
    each a name as written, without the affiliation and handle after it."""
    roles = []
    for match in re.finditer(r"^### (.+?)\s*\n(.*?)(?=^#{2,3} |\Z)", governance, re.M | re.S):
        names = [re.split(r"\s*\(@|,|\.\s", item, maxsplit=1)[0].strip().rstrip(".")
                 for item in re.findall(r"^- (.+)$", match.group(2), re.M)]
        if names:
            roles.append({"role": match.group(1).strip(), "names": names})
    return roles


def readme_description(readme: str) -> list[str]:
    """The README's paragraphs before its first `#` section after the title, and those of its "What's CSLib?"
    section, without its aims, which say what the library means to offer."""
    sections = re.split(r"^# ", readme, flags=re.M)
    kept = []
    for index, section in enumerate(sections[1:]):
        title, _, body = section.partition("\n")
        if index == 0 or title.strip().lower().startswith("what"):
            body = re.split(r"^##? ", body, maxsplit=1, flags=re.M)[0]
            kept += [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
    return kept


def read(checkout: Path, paths: list[str]) -> tuple[dict, list[str]]:
    """The record of a checkout, with the problems that keep it from being written: a license that is not
    Apache-2.0, a file the commit lists that is not checked out, a module whose scopes don't close."""
    problems = []
    license_file = checkout / "LICENSE"
    if not license_file.is_file() or not is_apache(license_file.read_text(encoding="utf-8")):
        problems.append("not Apache-2.0: its LICENSE is not the Apache License 2.0")
    lean = sorted(path for path in paths if path.startswith(LIBRARY + "/") and path.endswith(".lean"))
    readmes = sorted(path for path in paths if path.startswith(LIBRARY + "/") and path.endswith("/README.md"))
    wanted = lean + readmes + ["README.md", "GOVERNANCE.md"]
    missing = [path for path in wanted if not (checkout / path).is_file()]
    if missing:
        problems.append(f"not checked out: {missing[0]}" + (f" and {len(missing) - 1:,} other files" if len(missing) > 1 else ""))
        return {}, problems
    if not lean:
        return {}, problems + [f"no Lean file under {LIBRARY}/"]
    modules = []
    for path in lean:
        record = read_module((checkout / path).read_text(encoding="utf-8"), path)
        if record["items"] is None:
            problems.append(f"{path}: its scopes do not close as they open")
        modules.append(record)
    folders = {}
    for path in readmes:
        folder = path.removesuffix("/README.md")
        if any(module["file"].startswith(folder + "/") for module in modules):
            folders[folder] = readme_text((checkout / path).read_text(encoding="utf-8"))
    record = {
        "schema": SCHEMA,
        "readme": readme_description((checkout / "README.md").read_text(encoding="utf-8")),
        "maintainers": maintainers((checkout / "GOVERNANCE.md").read_text(encoding="utf-8")),
        "folders": folders,
        "modules": modules,
    }
    return record, problems


def counts(modules: list[dict]) -> Counter:
    tally: Counter = Counter()
    for module in modules:
        for item in module["items"] or []:
            if "name" in item:
                tally["declarations"] += 1
                tally[item["kind"]] += 1
                tally["documented"] += bool(item["doc"])
                tally["sorry"] += item["sorry"]
    return tally


def load(data: Path) -> dict | None:
    """data/cslib/'s source and library, when both are there."""
    source, library = data / "cslib" / "source.json", data / "cslib" / "library.json"
    if not (source.is_file() and library.is_file()):
        return None
    return json.loads(source.read_text(encoding="utf-8")) | json.loads(library.read_text(encoding="utf-8"))
