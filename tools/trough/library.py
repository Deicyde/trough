"""A Lean library's chapter, an article per module, read from the source without Lean and checked by a Lean run.

A library is configured by a Library value: its repository, the folder its modules live under, its intro and the
files it reads besides its modules. The reader takes each module's title, docstrings, the authors its header names
and its declarations, as trough.leansource reads them, and the chapter quotes the docstrings without their TODO notes
and their text about plans (doc_text, doc_markdown); a Lean run
over the built library (lean/library/LibraryDeps.lean) says which names are public and which modules each
module's statements and proofs use. The chapter has a part per folder under the library's root, a page per folder
below and an article per module, with a block per public declaration in file order.

Physlib's chapter (trough.physlib) keeps its own record, pages and blocks, and takes from here its links at the pin,
its guards, the docstring filter, the quoting of docstrings and its edges. The filter cuts when the chapter is built,
not when the source is read: the data keep the docstrings as the source writes them, so a change to the filter needs
no new reading of the library, and its tests and the data check one another.
"""

from __future__ import annotations

import json
import os
import posixpath
import re
import subprocess
import sys
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from . import leansource
from .blueprints import VAULT_FILE, Built, escape
from .ff import is_apache
from .formal_conjectures import OPAQUE, module_name, quote
from .mathlib import fence
from .stacks import comment, literal
from .vault import Container, Entry, Leaf, chunk, slugify

GITHUB = "https://github.com"
# A header's copyright holders and its optional list of authors, which AUTHORS.md says name a file's authors.
COPYRIGHT = re.compile(r"^Copyright \(c\) \d{4}(?:[-–]\d{4})? (?P<holders>.+?)\.? All rights reserved\.?$", re.M)
AUTHORS = re.compile(r"^Authors?:[ \t]*(?P<authors>.+(?:\n(?![A-Z][a-z]+:)[ \t]*\S.*)*)", re.M)
# A sentence about what is planned, wanted or welcome, not about what the library has. Not "not yet", "remains to be",
# "in the future" or "upstream", which say what the library has or are its subject (temporal logic, physics), nor
# "has to be added", which says what a construction needs.
PLANS = re.compile(r"\b(?:underway|under way|planned|we plan|plans? to|welcome|reserved for future work|future work on|"
                   r"future design work|be upstreamed|accepted upstream|will follow|(?<!has )(?<!have )(?<!needs )to be added|"
                   r"we would want|we should show|"
                   r"will eventually|near future|one day|be deprecated|with the intention|eventually we will|"
                   r"long term aim|leave this as future work|would be appreciated|contributors can|may want to focus|"
                   r"feel free to)\b", re.I)
# A README opening that speaks of plans, as a placeholder for later work does.
PLANNED = re.compile(r"\b(?:plan(?:s|ned)?|placeholder|upstream(?:ing)?)\b", re.I)
HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
# Definitions whose whole text is shown: their fields or constructors say what they are.
WHOLE = ("structure", "class", "inductive")
KIND_WORDS = {"theorem": "theorem", "lemma": "lemma", "def": "definition", "abbrev": "abbreviation",
              "instance": "instance", "structure": "structure", "class": "class", "inductive": "inductive type",
              "opaque": "opaque constant", "axiom": "axiom", "alias": "alias"}


@dataclass(frozen=True)
class Library:
    """What a library's chapter is made from."""
    id: str  # its data folder under data/, its roadmap folder and the prefix of its target keys
    name: str  # as the chapter's text names it
    title: str  # the chapter's title
    repo: str  # owner/name on GitHub
    root: str  # the folder its modules live under, the root of their names
    schema: str  # library.json's schema
    intro: Callable[[dict, Counter], str]  # the front page's prose, from the data and the counts
    # The files it reads besides its modules and its folders' READMEs, and what it records from them, in order.
    required: tuple[str, ...] = ("README.md",)
    extras: Callable[[Path], dict] = lambda checkout: {}
    # The bytes of article Markdown a folder's page folds in before its next article starts a page.
    page_budget: int = 200_000
    # The sentences the docstring filter cuts, about what is planned or invited rather than what the library has.
    plans: re.Pattern = PLANS
    # The folders its modules live under when there are several; else its root alone.
    roots: tuple[str, ...] = ()
    # What its credit line says is quoted.
    quotes: str = "The docstrings, Lean statements and README text"
    # The folders whose docstrings keep their TODO notes, as they describe a TODO command.
    todo_exempt: tuple[str, ...] = ()
    # Whether a module that declares nothing public by name is listed on its folder's page rather than given an
    # article; a folder left with no article has no page, and its modules are listed on the page above.
    list_empty: bool = False

    def notes(self, file: str) -> bool:
        """Whether the filter cuts the TODO notes of the module at *file*: not in the folders the library exempts."""
        return not file.startswith(self.todo_exempt) if file else True

    def without_todos(self, markdown: str, file: str = "") -> str:
        """without_todos() with the library's plan phrases, keeping TODO notes in the folders it exempts."""
        return without_todos(markdown, self.plans, notes=self.notes(file))


def header(text: str) -> dict:
    """The copyright holders and the authors the file's opening comment names."""
    spans = leansource.spans(text)
    first = spans[0] if spans and spans[0][2] == "comment" and not text[:spans[0][0]].strip() else None
    comment = text[first[0] + 2:first[1] - 2] if first else ""
    holders, authors = COPYRIGHT.search(comment), AUTHORS.search(comment)
    return {"copyright": holders["holders"].strip() if holders else "",
            "authors": " ".join(authors["authors"].split()) if authors else ""}


def readme_text(text: str) -> str:
    """A README's opening paragraph after its copyright block and title, which says what the folder holds; nothing
    when it speaks of plans, as a placeholder for later work does. Its other sections give principles for
    contributors and plans, and are left out."""
    text = re.sub(r"(?s)\A\s*<pre>.*?</pre>\s*", "", text)
    text = re.sub(r"\A\s*#[ \t]+[^\n]*\n", "", text).strip()
    opening = re.split(r"\n\s*\n", text, maxsplit=1)[0].strip()
    return "" if HEADING.match(opening) or PLANNED.search(opening) else opening


def statement_of(text: str, declaration: leansource.Declaration) -> str:
    """What a block shows of a declaration: a structure's, class's or inductive type's whole text, with its fields
    or constructors; any other's statement, the text up to the `:=` or `where` that starts its value, or its header
    when neither ends it, as for a definition by cases."""
    if declaration.kind in WHOLE or declaration.statement is None:
        return whole(text, declaration.line, declaration.kind not in WHOLE)
    return declaration.statement


def whole(text: str, line: int, header_only: bool = False) -> str:
    """A declaration's text from its keyword's line while lines are indented past the command's start, blank or a
    `deriving` clause; with *header_only*, it also stops at a line that starts a `|` case. The command starts at its
    attribute list when one shares the keyword's line, so a next command that opens with one ends it too."""
    plain = leansource.blank(text).split("\n")
    keyword = leansource.blank_attributes("\n".join(plain)).split("\n")
    source = text.split("\n")
    start = len(plain[line - 1]) - len(plain[line - 1].lstrip())
    column = len(keyword[line - 1]) - len(keyword[line - 1].lstrip())
    end = line
    for number in range(line, len(plain)):
        code = plain[number]
        stripped = code.strip()
        if header_only and (not stripped or stripped.startswith("|")):
            break
        clause = stripped.startswith("deriving") and not stripped.startswith("deriving instance")
        if stripped and len(code) - len(code.lstrip()) <= start and not clause:
            break
        if stripped:
            end = number + 1
    # It ends at its last line of code: a comment or docstring after it belongs to what follows.
    return leansource.dedent("\n".join([source[line - 1][column:]] + source[line:end]).rstrip(), start)


def read_module(text: str, path: str, library: Library | None = None) -> dict:
    """A module's record: its title, docstrings and public declarations in file order; `items` is None when its
    scopes don't close as they open. The module docstring is the first `/-! ... -/` before any declaration; each
    later one is an item of its own, where the file writes it. Docstrings are kept as the source writes them, and a
    `class abbrev` keeps its own name, where leansource reads `abbrev`."""
    found = leansource.declarations(text, relaxed=True)
    source = text.split("\n")
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
            record["doc"] = doc.strip()
        elif doc:
            notes.append({"line": line, "note": doc})
    declarations = [{"name": declared_name(declaration, source), "kind": declaration.kind, "line": declaration.line,
                     "doc": declaration.doc, "statement": statement_of(text, declaration),
                     "sorry": declaration.proof_sorry if declaration.statement is not None else declaration.sorry}
                    for declaration in found if declaration.name and not declaration.private]
    record["items"] = sorted(notes + declarations, key=lambda item: item["line"])
    return record


def read(library: Library, checkout: Path, paths: list[str]) -> tuple[dict, list[str]]:
    """The record of a checkout, with the problems that keep it from being written: a license that is not
    Apache-2.0, a file the commit lists that is not checked out, a module whose scopes don't close."""
    problems = []
    license_file = checkout / "LICENSE"
    if not license_file.is_file() or not is_apache(license_file.read_text(encoding="utf-8")):
        problems.append("not Apache-2.0: its LICENSE is not the Apache License 2.0")
    lean = sorted(path for path in paths if path.startswith(library.root + "/") and path.endswith(".lean"))
    readmes = sorted(path for path in paths if path.startswith(library.root + "/") and path.endswith("/README.md"))
    wanted = lean + readmes + list(library.required)
    if problem := checked_out(checkout, wanted):
        problems.append(problem)
        return {}, problems
    if not lean:
        return {}, problems + [f"no Lean file under {library.root}/"]
    modules = []
    for path in lean:
        record = read_module((checkout / path).read_text(encoding="utf-8"), path, library)
        if record["items"] is None:
            problems.append(f"{path}: its scopes do not close as they open")
        modules.append(record)
    folders = {}
    for path in readmes:
        folder = path.removesuffix("/README.md")
        if any(module["file"].startswith(folder + "/") for module in modules):
            if text := readme_text((checkout / path).read_text(encoding="utf-8")):
                folders[folder] = text
    record = {
        "schema": library.schema,
        **library.extras(checkout),
        "folders": folders,
        "modules": modules,
    }
    return record, problems


def checked_out(checkout: Path, wanted: list[str]) -> str:
    """The problem when a file the record needs is not in the checkout, naming the first."""
    missing = [path for path in wanted if not (checkout / path).is_file()]
    if not missing:
        return ""
    return f"not checked out: {missing[0]}" + (f" and {len(missing) - 1:,} other files" if len(missing) > 1 else "")


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def refresh(library: Library, checkout: Path, out: Path) -> list[str]:
    """Write source.json and library.json under *out* from a checkout of the library at the commit to pin, or neither
    when there is a problem: a license that is not Apache-2.0, a file not checked out, a module whose scopes don't
    close, or a reading of under half the declarations the last record has. Return the problems."""
    rev = git(checkout, "rev-parse", "HEAD")
    paths = git(checkout, "ls-tree", "-r", "--name-only", "HEAD").splitlines()
    record, problems = read(library, checkout, paths)
    previous = out / "library.json"
    last = json.loads(previous.read_text(encoding="utf-8")) if previous.is_file() else None
    if record and last:
        now, before = counts(record["modules"])["declarations"], counts(last["modules"])["declarations"]
        if now * 2 < before:
            problems.append(f"reads {now} declarations, under half the {before} the last record read")
    if problems:
        return problems
    manifest = json.loads((checkout / "lake-manifest.json").read_text(encoding="utf-8"))
    mathlib = next((package.get("rev", "") for package in manifest.get("packages", []) if package.get("name") == "mathlib"), "")
    source = {"repo": library.repo, "rev": rev,
              # In UTC, as git versions print %cI differently.
              "date": git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
              "toolchain": (checkout / "lean-toolchain").read_text(encoding="utf-8").strip().split(":")[-1],
              "mathlib": mathlib, "license": "Apache-2.0"}
    record = {"schema": record.pop("schema"), "rev": rev, **record}
    out.mkdir(parents=True, exist_ok=True)
    (out / "source.json").write_text(json.dumps(source, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    previous.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    tally = counts(record["modules"])
    print(f"{library.repo} {rev[:8]}: {len(record['modules'])} modules, {tally['declarations']} declarations read "
          f"({tally['documented']} documented, {tally['sorry']} holding sorry), "
          f"{sum(1 for module in record['modules'] if module['title'])} modules titled by their docstrings, "
          f"{len(record['folders'])} folder READMEs", file=sys.stderr)
    return []


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


def load(library: Library, data: Path) -> dict | None:
    """The library's source and library records under *data*, when both are there, with the Lean dump's edges when
    they are of the same commit."""
    source, record, deps = (data / library.id / name for name in ("source.json", "library.json", "deps.json"))
    if not (source.is_file() and record.is_file()):
        return None
    loaded = json.loads(source.read_text(encoding="utf-8")) | json.loads(record.read_text(encoding="utf-8"))
    dump = json.loads(deps.read_text(encoding="utf-8")) if deps.is_file() else None
    return loaded | {"deps": dump if dump and dump.get("rev") == loaded["rev"] else None}


# The chapter, from the data.


def blob(library: Library, rev: str, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{library.repo}/blob/{rev}/{path}" + (f"#L{line}" if line else "")


def folder_url(library: Library, rev: str, path: str = "") -> str:
    return f"{GITHUB}/{library.repo}/tree/{rev}" + (f"/{path}" if path else "")


def at(library: Library, rev: str) -> str:
    return f"[{rev[:8]}]({folder_url(library, rev)})"


def pinned(library: Library, text: str, rev: str, base: str | None = None) -> str:
    """Quoted text whose links into the repository's master branch point at the pinned commit. With *base*, the
    folder the text was read from, a relative Markdown link points at its target in the repository at that commit,
    as it would not resolve on the site."""
    text = re.sub(rf"{GITHUB}/{re.escape(library.repo)}/(blob|tree)/master/",
                  lambda match: f"{GITHUB}/{library.repo}/{match.group(1)}/{rev}/", text)
    if base is None:
        return text
    return re.sub(r"\]\((?![a-zA-Z][a-zA-Z0-9+.-]*:|#)([^)\s]+)\)",
                  lambda match: f"]({blob(library, rev, posixpath.normpath(posixpath.join(base, match.group(1))).lstrip('/'))})",
                  text)


def plural(count: int, word: str, words: str | None = None) -> str:
    return f"{count:,} {word if count == 1 else words or word + 's'}"


def listing(parts: list[str]) -> str:
    return ", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else "".join(parts)


def title_text(title: str) -> str:
    """A docstring's title as a page title: Markdown escaped outside its code spans and formulas."""
    parts, last = [], 0
    for match in OPAQUE.finditer(title):
        parts += [escape(title[last:match.start()]), match.group()]
        last = match.end()
    return "".join(parts) + escape(title[last:])


def stem(module: dict) -> str:
    return module["file"].rsplit("/", 1)[-1].removesuffix(".lean")


def titles(modules: list[dict]) -> dict[str, str]:
    """Each module's title: its docstring's, or its file name when the docstring has none. Where modules share one,
    each takes the shortest end of its file's path that no other of them shares, in brackets after a docstring's
    title or in place of a file name."""
    # A title is a heading, so a full stop that ends it as a sentence goes.
    plain = {module["module"]: re.sub(r"(?<!\.)\.$", "", module["title"]) for module in modules}
    groups: dict[str, list[dict]] = {}
    for module in modules:
        groups.setdefault(plain[module["module"]] or stem(module), []).append(module)
    named = {}
    for base, members in groups.items():
        for module in members:
            if len(members) == 1:
                named[module["module"]] = base
                continue
            parts = module["file"].removesuffix(".lean").split("/")
            others = [other["file"].removesuffix(".lean").split("/") for other in members if other is not module]
            depth = next(depth for depth in range(1, len(parts) + 1) if all(other[-depth:] != parts[-depth:] for other in others))
            piece = "/".join(parts[-depth:])
            named[module["module"]] = f"{base} ({piece})" if plain[module["module"]] else piece
    shared = [title for title, count in Counter(named.values()).items() if count > 1]
    if shared:
        raise ValueError(f"modules still share the titles {', '.join(shared)}")
    return named


def declarations(module: dict) -> list[dict]:
    return [item for item in module["items"] if "name" in item]


def quoted_doc(library: Library, text: str, file: str, keys: dict[str, str]) -> str:
    """A docstring of the module at *file* as a block quotes it: filtered by doc_text(), a link to another module
    pointing at its article, as quoted_prose() keeps links; nothing when nothing is left."""
    kept = doc_text(text, library.plans, library.notes(file))
    return quoted_prose(kept, file, keys, escape=False) if kept else ""


def block(library: Library, item: dict, file: str, rev: str, keys: dict[str, str]) -> str:
    """A declaration's name, kind and line, its docstring and its Lean statement; or a note the module writes there."""
    if "note" in item:
        return quoted_doc(library, item["note"], file, keys)
    where = f"[line {item['line']}]({blob(library, rev, file, item['line'])})"
    head = f"`{item['name']}` ({KIND_WORDS.get(item['kind'], item['kind'])}, {where})"
    if item["sorry"]:
        head += ". Its value holds `sorry`."
    doc = quoted_doc(library, item["doc"], file, keys)
    return "\n\n".join([head] + ([doc] if doc else []) + [fence(item["statement"])])


def article(library: Library, module: dict, title: str, rev: str, links: dict[str, str], keys: dict[str, str]) -> Leaf:
    """A module's article: where it is and who wrote it, its docstring, and a block per public declaration and per
    later note, in file order; notes cut whole one after another show one cut mark."""
    names = [item["name"] for item in declarations(module)]
    authors = module["authors"] or module["copyright"]
    opening = f"`{module['module']}`, in [{module['file']}]({blob(library, rev, module['file'])})" + (f", by {authors}." if authors else ".")
    if not names:
        opening += " It declares nothing public by name."
    doc = quoted_doc(library, module["doc"], module["file"], keys)
    parts = [opening] + ([doc] if doc else [])
    parts += [part for item in module["items"] if (part := block(library, item, module["file"], rev, keys))]
    parts = one_cut(parts)
    fields = [("catalog", "module")]
    if names:
        fields += [("lean", ", ".join(names)), ("statement", "formalized")]
        if not any(item["sorry"] for item in declarations(module)):
            fields.append(("proof", "formalized"))
    for item in declarations(module):
        links.setdefault(item["name"], blob(library, rev, module["file"], item["line"]))
    leaf = Leaf(title_text(title), slugify(stem(module)), fields, "\n\n".join(parts))
    leaf.sources = [(f"{module['file']} at {rev[:8]}", blob(library, rev, module["file"])),
                    ("Declaration ledger", VAULT_FILE + ledger_path(library, module))]
    return leaf


def tree(modules: list[dict]) -> dict:
    """The folders under the library's root as nested {"modules", "folders"}, by name."""
    root: dict = {"modules": [], "folders": {}}
    for module in modules:
        node = root
        for part in module["file"].split("/")[1:-1]:
            node = node["folders"].setdefault(part, {"modules": [], "folders": {}})
        node["modules"].append(module)
    return root


def every(node: dict) -> list[dict]:
    return node["modules"] + [module for child in node["folders"].values() for module in every(child)]


def credit(library: Library, rev: str) -> str:
    return (f"{library.quotes} are quoted from [{library.repo}]({GITHUB}/{library.repo}) "
            f"at commit {at(library, rev)}, under its Apache-2.0 license.")


LEDGER_SCHEMA = "trough-ledger/v1"
# What the source reading does not read, which a ledger therefore cannot list.
UNREAD = ("Unnamed instances, the names an `alias ⟨…⟩` command gives, and the names Lean generates for a declaration "
          "(constructors, recursors, derived instances) are not read from the source, so they are not listed.")


def ledger_path(library: Library, module: dict) -> str:
    """Where a module catalog's declaration ledger is, below the vault: a JSON file, which the site does not publish
    and links in the repository instead."""
    return f"sources/{library.id}/{module['module']}.json"


def ledger(library: Library, module: dict, rev: str, private: set[str], missing: set[str]) -> str:
    """A module catalog's declaration ledger: every declaration read from the module's source, with its kind and line,
    under `public` when Lean has it as a public declaration (these are the article's `lean:` names), `private` when
    Lean has it only as a declaration private to the module, and `missing` when Lean does not have it."""
    entries: dict[str, list[dict]] = {"public": [], "private": [], "missing": []}
    for item in declarations(module):
        group = "private" if item["name"] in private else "missing" if item["name"] in missing else "public"
        entries[group].append({"name": item["name"], "kind": item["kind"], "line": item["line"]})
    head = {"schema": LEDGER_SCHEMA, "library": library.name, "repo": library.repo, "rev": rev,
            "module": module["module"], "file": module["file"]}
    # An entry a line, so that a change to the module shows as a change to its lines.
    parts = [f" {json.dumps(key)}: {json.dumps(value, ensure_ascii=False)}" for key, value in head.items()]
    parts += [f' "{group}": [' + ",".join(f"\n  {json.dumps(entry, ensure_ascii=False)}" for entry in items)
              + ("\n ]" if items else "]") for group, items in entries.items()]
    parts.append(f' "unread": {json.dumps(UNREAD, ensure_ascii=False)}')
    return "{\n" + ",\n".join(parts) + "\n}\n"


def module_intro(library: Library, data: dict, stats: Counter, about: list[str], empty: str | None = None) -> str:
    """The front page of a library whose modules that declare nothing public are listed (Library.list_empty): *about*,
    the paragraphs that say what the library is, then the commit and the counts, how an article reads, where the edges
    come from, and the credit. *empty* says what the listed modules are, when the library's own words fit better."""
    rev = data["rev"]
    theorems = stats["theorem"] + stats["lemma"]
    definitions = sum(stats[kind] for kind in ("def", "abbrev", "structure", "class", "inductive", "opaque"))
    others = stats["declarations"] - theorems - definitions
    if data.get("deps"):
        lean = (
            f"Edges come from Lean: a GitHub Actions run builds {library.name} at this commit and reads, for each module, "
            "which other modules' declarations its own use. “Depends on” lists the modules its statements use, the "
            "types of its declarations and the values of its definitions, and “Proof depends on” those only its proofs "
            f"use; a dependency reached through another is left out. That gives "
            f"{plural(stats['statement_edges'], 'statement edge')} and {plural(stats['proof_edges'], 'proof edge')}."
            + (f" The run has no record of {plural(stats['unrecorded'], 'module')}, whose dependencies are unknown."
               if stats["unrecorded"] else "")
            + " The same run checks the names read from the source"
            + (f": Lean marks {stats['private']:,} of them as private to their modules (in a `module` file, a "
               "declaration outside a `public section` and not marked `public` is private), and these are left out"
               + (f", as {'is' if stats['unresolved'] == 1 else 'are'} {plural(stats['unresolved'], 'name')} Lean does "
                  "not have" if stats["unresolved"] else "")
               + "." if stats["private"] or stats["unresolved"] else ", and Lean has each as a public declaration."))
    else:
        lean = ("The articles have no edges, and the names read from the source are not checked against Lean: both come "
                f"from a Lean run over {library.name} at this commit, which the data lack.")
    if empty is None:
        empty = (f" The other {plural(stats['empty'], 'module')} declare nothing public by name; they are listed on "
                 "their folders' pages.")
    mathlib = f" and Mathlib {data['mathlib'][:8]}" if data.get("mathlib") else ""
    return "\n\n".join(part for part in [
        *about,
        f"This chapter maps {library.name} at commit {at(library, rev)} ({data['date'][:10]}), with Lean toolchain "
        f"{data['toolchain']}{mathlib}. It has an article for each of the {plural(stats['articles'], 'module')} under "
        f"`{library.root}/` that declare something public by name, in a part per folder of `{library.root}/` and a page "
        f"per folder below. They hold {plural(stats['declarations'], 'public declaration')}, "
        + listing([plural(count, word, words) for count, word, words in (
            (theorems, "theorem", None), (definitions, "definition", None),
            (others, "instance or alias", "instances and aliases")) if count])
        + f", {stats['documented']:,} of them with a docstring."
        + (empty if stats["empty"] else ""),
        "An article is titled by its module docstring, or by its file name when the docstring has no title; where "
        "modules share a title, each adds the shortest end of its path that tells them apart. It gives the module's "
        "authors as its header names them, its docstrings, and a block per public declaration in file order with its "
        "Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, "
        "class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names "
        "an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future "
        "work; an ellipsis marks each cut."
        + ("" if stats["sorry"] else " No declaration's value holds `sorry`."),
        lean,
        credit(library, rev),
    ] if part)


def unbuilt_line(library: Library, unbuilt: list[dict], rev: str) -> str:
    """The front page's line naming the modules the library's build did not compile, which Lean could not read."""
    names = listing([f"[`{module['module']}`]({blob(library, rev, module['file'])})" for module in unbuilt])
    return (f"{plural(len(unbuilt), 'module')} under `{library.root}/` did not build in the library's own build, so Lean "
            f"could not read {'it' if len(unbuilt) == 1 else 'them'} and {'it has' if len(unbuilt) == 1 else 'they have'} "
            f"no article: {names}.")


def chapter(library: Library, data: dict) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and each declaration's source line (for
    hooks/lean-links.json). A part per area, a page per folder below it and an article per module."""
    rev, deps = data["rev"], data.get("deps")
    stats: Counter = Counter()
    # Lean decides which of the names read from the source are public: one private to its module, or one Lean does not
    # have, is left out.
    private, missing = (set(deps.get("private", [])), set(deps.get("missing", []))) if deps else (set(), set())
    # A dump that says which modules the library's build compiled (lean/library/LibraryDeps.lean, which imports each
    # one) leaves the others unread: they are listed on the front page, not mapped. Over half unbuilt is refused, as the
    # reading, not the library, has gone wrong.
    built = set(deps["built"]) if deps and "built" in deps else None
    unbuilt = [module for module in data["modules"] if built is not None and module["module"] not in built]
    if len(unbuilt) * 2 > len(data["modules"]):
        raise ValueError(f"data/{library.id}/deps.json says {len(unbuilt):,} of the {len(data['modules']):,} modules "
                         "did not build, over half")
    read = [module for module in data["modules"] if module not in unbuilt]
    check_names(library, {item["name"] for module in read for item in module["items"] or [] if "name" in item},
                missing)
    modules = []
    for module in read:
        stats["private"] += sum(item.get("name") in private for item in module["items"])
        stats["unresolved"] += sum(item.get("name") in missing for item in module["items"])
        modules.append({**module, "items": [item for item in module["items"]
                                            if item.get("name") not in private | missing or "name" not in item]})
    # The modules with an article, and those listed instead.
    shown = [module for module in modules if declarations(module) or not library.list_empty]
    named = titles(shown)
    keys = {module["file"]: f"{library.id}-{module['module']}" for module in shown}  # each article's key, by file
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    leaves: dict[str, Leaf] = {}

    def unshown(module: dict) -> bool:
        return library.list_empty and not declarations(module)

    def listed_line(listed: list[dict]) -> str:
        """The line naming the modules a page lists, which declare nothing public by name."""
        names = listing([f"[`{module['module']}`]({blob(library, rev, module['file'])})" for module in listed])
        return (f"{'This module declares' if len(listed) == 1 else 'These modules declare'} nothing public by name, "
                f"so {'it has' if len(listed) == 1 else 'they have'} no article: {names}.")

    def build(name: str, node: dict, path: str, part: bool) -> tuple[Container | None, list[dict]]:
        """The folder's page, or None when it would hold no article, with the modules a page above must list."""
        entries, listed = [], []
        # By name, as the root module imports them, a module before the folder of the same name.
        children = sorted([(stem(module), 0, module) for module in node["modules"]]
                          + [(folder, 1, child) for folder, child in node["folders"].items()], key=lambda row: row[:2])
        for child_name, is_folder, child in children:
            if is_folder:
                page, below = build(child_name, child, f"{path}/{child_name}", False)
                entries += [Entry(page)] if page else []
                listed += below
            elif unshown(child):
                listed.append(child)
            else:
                leaf = article(library, child, named[child["module"]], rev, links, keys)
                leaves[child["module"]] = leaf
                targets[f"{library.id}-{child['module']}"] = leaf
                stats["articles"] += 1
                entries.append(Entry(leaf))
        if not entries:
            return None, listed
        container = Container(escape(name), slugify(name), entries)
        inside = every(node)
        tally = counts(inside)
        held = (f", with {plural(tally['declarations'], 'public declaration')}." if tally["declarations"] else
                ", none of which declares anything public by name." if len(inside) > 1 else
                ", which declares nothing public by name.")
        lines = [f"{plural(len(inside), 'module')} under `{path}/`{held}"]
        if listed:
            lines.append(listed_line(listed))
            stats["listed"] += len(listed)
        if path in data["folders"]:
            lines.append(f"Its [README]({blob(library, rev, path + '/README.md')}) opens:\n\n{quote(pinned(library, data['folders'][path], rev, path))}")
        if part:
            lines.append(credit(library, rev))
        container.prose = "\n\n".join(lines)
        targets[f"{library.id}-{path}"] = container
        stats["folders"] += 1
        return chunk(container, budget=library.page_budget), []

    top = tree(modules)
    parts, listed = [], []
    for name, child in sorted(top["folders"].items()):
        page, below = build(name, child, f"{library.root}/{name}", True)
        parts += [Entry(page)] if page else []
        listed += below
    stats["parts"] = len(parts)
    for module in top["modules"]:
        if unshown(module):
            listed.append(module)
            continue
        leaf = article(library, module, named[module["module"]], rev, links, keys)
        leaves[module["module"]] = leaf
        targets[f"{library.id}-{module['module']}"] = leaf
        stats["articles"] += 1
        parts.append(Entry(leaf))
    edges(library, data, leaves, stats)
    stats.update(counts(modules))
    stats["empty"] = sum(1 for module in modules if not declarations(module))
    if listed:
        stats["listed"] += len(listed)
    if unbuilt:
        stats["unbuilt"] = len(unbuilt)
    # A root with more parts and articles than a page lists is nested, as a folder's page is.
    root = chunk(Container(library.title, library.id, parts))
    root.prose = (library.intro(data, stats) + (f"\n\n{listed_line(listed)}" if listed else "")
                  + (f"\n\n{unbuilt_line(library, unbuilt, rev)}" if unbuilt else ""))
    # A declaration ledger for each article, a module catalog; a listed module has no article, so no ledger.
    ledgers = {ledger_path(library, module): ledger(library, module, rev, private, missing)
               for module in data["modules"] if module["module"] in leaves}
    return Built(root, targets, {}, dict(stats), Counter(), ledgers), dict(sorted(links.items()))


def edges(library: Library, data: dict, leaves: dict[str, Leaf], stats: Counter) -> None:
    """Each article's edges from the Lean dump, when there is one: the modules whose declarations its statements use
    under "Depends on", and those only its proofs use under "Proof depends on". A statement dependency already
    reached through another statement dependency, or a proof dependency reached through any other dependency, is
    left out."""
    if data.get("deps") is None:
        for leaf in leaves.values():
            leaf.no_depends = "No dependencies are recorded: the Lean dump that gives them has not been read."
        return
    deps = data["deps"].get("modules", {})
    stmt = {module: set(deps.get(module, {}).get("statement", [])) & leaves.keys() - {module} for module in leaves}
    proof = {module: set(deps.get(module, {}).get("proof", [])) & leaves.keys() - {module} - stmt[module]
             for module in leaves}
    reach_stmt: dict[str, set[str]] = {}
    reach_all: dict[str, set[str]] = {}

    def walk_from(module: str) -> None:
        # Modules import one another without cycles, so a depth-first walk ends; each set is its node's closure. A
        # node met again before its closure is done is on a cycle, which a dump that reads imports cannot give.
        stack = [(module, False)]
        open_nodes: set[str] = set()
        while stack:
            node, done = stack.pop()
            if node in reach_all:
                continue
            if not done and node in open_nodes:
                raise ValueError(f"data/{library.id}/deps.json has a cycle of module dependencies through {node}")
            open_nodes.add(node)
            if done:
                reach_stmt[node] = set().union(*(reach_stmt[child] | {child} for child in stmt[node]))
                reach_all[node] = set().union(*(reach_all[child] | {child} for child in stmt[node] | proof[node]))
                continue
            stack.append((node, True))
            stack.extend((child, False) for child in stmt[node] | proof[node] if child not in reach_all)

    for module in sorted(leaves):
        walk_from(module)
    for module, leaf in leaves.items():
        kept_stmt = {child for child in stmt[module]
                     if not any(child in reach_stmt[other] for other in stmt[module] - {child})}
        kept_proof = {child for child in proof[module]
                      if not any(child in reach_all[other] for other in (stmt[module] | proof[module]) - {child})}
        leaf.depends = [leaves[child] for child in sorted(kept_stmt)]
        leaf.proof_depends = [leaves[child] for child in sorted(kept_proof)]
        if module in deps:
            leaf.no_depends = f"Its statements use no other {library.name} module's declarations."
        else:
            leaf.no_depends = "The Lean dump has no record of this module, so its dependencies are unknown."
            stats["unrecorded"] += 1
        stats["statement_edges"] += len(leaf.depends)
        stats["proof_edges"] += len(leaf.proof_depends)


# What Physlib's chapter reads and renders, shared for the libraries that take it up.

# `class abbrev X := A, B`, which leansource reads as a class named `abbrev`.
CLASS_ABBREV = re.compile(rf"\bclass[ \t]+abbrev[ \t]+({leansource.NAME})")
TODOS = re.compile(r"\bTODOs?\b")
# A TODO note: a block that starts with one.
TODO_NOTE = re.compile(r"TODOs?\b")
# A heading over plans, after its section number if it has one.
PLAN_HEADING = re.compile(r"^(?:[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*\.[ \t]+)?(?:plans?|future work|todos?|roadmap)\b", re.I)
HEADING_START = re.compile(r"#{1,6}[ \t]")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
ABBREVIATION = re.compile(r"\b(?:e\.g|i\.e|cf|resp|vs)\.$")
BULLET = re.compile(r"^[ \t]*[-*+][ \t]")
FENCE = re.compile(r"^ {0,3}(?:`{3,}|~{3,})")
FENCED = re.compile(r"^ {0,3}(`{3,}|~{3,}).*?(?:^ {0,3}\1[ \t]*$|\Z)", re.M | re.S)
INLINE_LINK = re.compile(r"(?<!!)\[((?:[^\[\]\n]|\[[^\[\]\n]*\])*)\]\(([^()\s]+)\)")
SCHEME = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|#)")
CUT_MARKS = ("…", "> …")  # a cut mark, as a paragraph and quoted


def declared_name(declaration: leansource.Declaration, source: list[str]) -> str:
    """A declaration's name, a `class abbrev`'s own where leansource reads `abbrev`; *source* is the text's lines."""
    if declaration.kind == "class" and declaration.name.rsplit(".", 1)[-1] == "abbrev":
        if match := CLASS_ABBREV.search(source[declaration.line - 1]):
            return declaration.name.removesuffix("abbrev") + match.group(1)
    return declaration.name


def check_names(library: Library, read_names: set[str], missing: set[str]) -> None:
    """Refuse a Lean dump that marks over half the names read from the source missing: as the refresh refuses a record
    that reads under half the last one, the reading, not the library, has gone wrong."""
    if len(missing & read_names) * 2 > len(read_names):
        raise ValueError(f"data/{library.id}/deps.json marks {len(missing & read_names):,} of the {len(read_names):,} "
                         "names read from the source missing, over half")


def sentences(paragraph: str) -> list[str]:
    """A paragraph's sentences, each with the space after it, so that they join to the paragraph; a sentence does not
    end at an abbreviation such as e.g."""
    pieces, start = [], 0
    for match in SENTENCE_END.finditer(paragraph):
        if not ABBREVIATION.search(paragraph[start:match.start()]):
            pieces.append(paragraph[start:match.end()])
            start = match.end()
    return pieces + ([paragraph[start:]] if start < len(paragraph) else [])


def without_cut_sentences(paragraph: str, plans: re.Pattern, todos: re.Pattern = TODOS) -> str:
    """A paragraph without its sentences about plans, and without what follows the start of the sentence, or of the
    clause after a semicolon, that mentions a TODO item, each cut marked with …."""
    kept, marked = "", False
    for sentence in sentences(paragraph):
        todo = todos.search(sentence)
        clauses = [match.start() for match in re.finditer(r";\s", sentence[:todo.start()])] if todo else []
        if clauses:
            return kept + sentence[:clauses[-1] + 1] + " …"
        if todo or plans.search(sentence):
            if not marked:
                kept, marked = kept + "… ", True
            if todo:
                break
            continue
        kept, marked = kept + sentence, False
    return kept.strip()


def without_todos(markdown: str, plans: re.Pattern, notes: bool = True) -> str:
    """Quoted Markdown without its TODO notes and its sentences about plans (those *plans* matches), each cut marked
    with …. A paragraph that starts with a TODO note, or whose first sentence is about plans, goes with the list it
    introduces and every paragraph after it up to the next heading. Otherwise a list item that mentions a TODO item or
    plans goes whole, the line that introduces the list staying, and in a paragraph a sentence about plans goes, and so
    does a sentence that mentions a TODO item with the rest of its paragraph. Code in a fenced block is not read for
    TODOs or plans. The map records what the library has, not what it plans. Without *notes*, TODO items are not cut,
    for text that describes a TODO command."""
    todos = TODOS if notes else re.compile(r"(?!)")
    out, cutting = [], False
    for block in re.split(r"\n[ \t]*\n", markdown.strip()):
        prose = FENCED.sub("", block)
        if HEADING_START.match(block):
            cutting = False
        elif cutting:
            continue
        else:
            # The paragraph's first sentence, before any list it introduces.
            lines = block.strip().split("\n")
            opening = lines[:next((index for index, line in enumerate(lines) if index and BULLET.match(line)), len(lines))]
            lead = (sentences("\n".join(opening)) or [""])[0]
            if (notes and TODO_NOTE.match(block.lstrip())) or plans.search(lead):
                out.append("…")
                cutting = True
                continue
        if not (todos.search(prose) or plans.search(prose)):
            out.append(block)
            continue
        items: list[list[str]] = []
        for line in block.split("\n"):
            if BULLET.match(line) or not items:
                items.append([line])
            else:
                items[-1].append(line)
        # A list, after the line that introduces it when that line neither plans nor mentions a TODO.
        intro = [] if BULLET.match(items[0][0]) else items[0]
        listed = items[1:] if intro else items
        if (len(listed) > (0 if intro else 1) and all(BULLET.match(item[0]) for item in listed)
                and not (todos.search(text := FENCED.sub("", "\n".join(intro))) or plans.search(text))):
            kept = [line for item in listed
                    if not (todos.search(text := FENCED.sub("", "\n".join(item))) or plans.search(text))
                    for line in item]
            out.append("\n".join(intro + kept) + "\n\n…" if intro or kept else "…")
        else:
            out.append(without_cut_sentences(block, plans, todos))
    return re.sub(r"…(?:\n\n…)+", "…", "\n\n".join(out)).strip()


def quoted_prose(markdown: str, here: str = "", keys: dict[str, str] | None = None, escape: bool = True) -> str:
    """Prose of the module at *here*, quoted: with *escape*, escaped as literal() escapes it, its inline links kept
    whole, so an underscore in a link's target stays one. With *keys*, each article's key by file, a link to one of the
    repository's files, written relative to the module, points at the article of that module here; a link to another
    path, which is no module of the commit, keeps only its label. A link out of the repository is left for quote() to
    make text."""
    links: list[str] = []
    folder = here.rsplit("/", 1)[0]
    opaque = [match.span() for match in OPAQUE.finditer(markdown)]

    def keep(match: re.Match) -> str:
        label, target = match.groups()
        if any(start <= match.start() < end for start, end in opaque):
            return match.group()
        if not SCHEME.match(target):
            if keys is None:
                return match.group()
            path = target.split("#")[0]
            path = posixpath.normpath(path.lstrip("/") if path.startswith("/") else posixpath.join(folder, path))
            if path == ".." or path.startswith("../"):
                return match.group()
            if path not in keys:
                return label
            target = f"trough:{keys[path]}"
        links.append(f"[{literal(label) if escape else label}]({target})")
        return f"\x00{len(links) - 1}\x00"

    text = INLINE_LINK.sub(keep, markdown)
    text = literal(text) if escape else text
    return quote(re.sub(r"\x00(\d+)\x00", lambda match: links[int(match.group(1))], text))


def doc_sections(text: str, plans: re.Pattern, notes: bool = True) -> list[tuple]:
    """A docstring's headings and prose, filtered: ("heading", level, words, line) for a heading it keeps, ("cut",)
    for a section headed by a TODO or by plans (Future work, Roadmap), left out with the headings under it, and
    ("prose", kept, written) for the text between headings, with the TODO notes and sentences about plans
    without_todos cuts and the text as written. A table of contents, which an article's own headings give, is left out
    unmarked, as ("contents",)."""
    out: list[tuple] = []
    prose: list[str] = []
    skipping, fenced = 0, False

    def flush() -> None:
        written = "\n".join(prose)
        out.append(("prose", without_todos(written, plans, notes), written))
        prose.clear()

    for line in text.split("\n"):
        if FENCE.match(line):
            fenced = not fenced
        match = None if fenced else HEADING.match(line)
        if match is None:
            if not skipping:
                prose.append(line)
            continue
        level, words = len(match.group(1)), match.group(2)
        if skipping and level > skipping:
            continue
        flush()
        planned = bool(TODOS.search(words) or PLAN_HEADING.match(words))
        skipping = level if "table of contents" in words.casefold() or planned else 0
        if planned:
            out.append(("cut",))
        elif skipping:
            out.append(("contents",))
        else:
            out.append(("heading", level, words, line))
    flush()
    return out


def doc_markdown(text: str, quoted: Callable[[str], str], plans: re.Pattern) -> list[str]:
    """A docstring as an article shows it, from doc_sections(): its headings as the article's, from `##` down, its
    prose quoted, and each section cut marked with …."""
    parts: list[str] = []
    for section in doc_sections(text, plans):
        if section[0] == "heading":
            parts.append("#" * min(max(section[1], 2), 6) + " " + comment(section[2]))
        elif section[0] == "cut":
            parts.append("…")
        elif section[0] == "prose" and section[1]:
            parts.append(quoted(section[1]))
    return parts


def doc_text(text: str, plans: re.Pattern, notes: bool = True) -> str:
    """A docstring as one block quotes it, from doc_sections(): as written where nothing is cut; else its headings as
    written, each section cut and each run of cuts marked with one …, and its paragraphs a blank line apart."""
    sections = doc_sections(text, plans, notes)
    if all(section[0] == "heading" or (section[0] == "prose" and section[1].split() == section[2].split())
           for section in sections):
        return text.strip()
    blocks = [section[3] if section[0] == "heading" else "…" if section[0] == "cut" else
              section[1] if section[0] == "prose" else "" for section in sections]
    return re.sub(r"…(?:\n\n…)+", "…", "\n\n".join(block for block in blocks if block)).strip()


def one_cut(parts: list[str]) -> list[str]:
    """An article's parts with each run of cut marks, as from docstrings cut whole one after another, made one."""
    return [part for index, part in enumerate(parts) if not (part in CUT_MARKS and parts[index - 1] in CUT_MARKS)]


def closures(graph: dict[str, list[str]]) -> dict[str, set[str]]:
    """What each node of an acyclic graph reaches through one or more edges."""
    out: dict[str, set[str]] = {}

    def visit(node: str) -> set[str]:
        if node not in out:
            out[node] = set()
            out[node] = set().union(*({target} | visit(target) for target in graph.get(node, [])))
        return out[node]

    for node in graph:
        visit(node)
    return out


def nearest_edges(deps: dict, articles: set[str], order: Callable[[str], object] = str) \
        -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Each module's nearest dependencies among the modules with an article: those its statements use, without one
    reached through another's statements, and those only its proofs use, without one reached through any other.
    A module without an article is passed through, its uses taken as the module's own. *order* sorts each list."""
    uses = deps["modules"]

    def through(kind: str) -> dict[str, list[str]]:
        memo: dict[str, set[str]] = {}

        def reached(module: str) -> set[str]:
            if module not in memo:
                memo[module] = set()
                found: set[str] = set()
                direct = uses.get(module, {}).get(kind, [])
                if kind == "proof":
                    direct = [*direct, *uses.get(module, {}).get("statement", [])]
                for target in direct:
                    found |= {target} if target in articles else reached(target)
                memo[module] = found
            return memo[module]

        out = {}
        for module in articles:
            found: set[str] = set()
            for target in uses.get(module, {}).get(kind, []):
                found |= {target} if target in articles else reached(target)
            out[module] = sorted(found - {module}, key=order)
        return out

    statement = through("statement")
    proof = {module: [target for target in targets if target not in set(statement[module])]
             for module, targets in through("proof").items()}
    by_statement = closures(statement)
    either = {module: statement[module] + proof[module] for module in articles}
    by_either = closures(either)
    nearest = {module: [target for target in targets
                        if not any(target in by_statement[other] for other in targets if other != target)]
               for module, targets in statement.items()}
    proof_nearest = {module: [target for target in targets
                              if not any(target in by_either[other] for other in either[module] if other != target)]
                     for module, targets in proof.items()}
    return nearest, proof_nearest
