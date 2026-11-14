"""Satellite projects: one-off Lean projects, each a card beside the library it builds on.

data/satellites/projects.toml lists the projects. tools/refresh_satellites.py reads
each at a pinned commit into data/satellites/<slug>.json, from a sparse checkout of
its manifests, README, license, blueprint TeX and the .lean files of the Lean
libraries its lakefile defines, without Lean: the requirements its Lake manifest
names directly, the Mathlib modules it imports, the declarations it makes
(trough.leansource), the Mathlib concepts it names, and its headline
declarations, by the first of three rules that gives any:

1. the Lean names of the blueprint nodes no other node uses, marked \\leanok;
2. the names its README sets in code spans that the project declares;
3. the theorems of a module named Main, MainTheorem(s) or Statement(s).

A project with headlines is a card: its `lean:` names are its headlines, its
statement edges the Mathlib concepts and other chapters' declarations their
signatures name, and its proof edges the Mathlib concepts its files name most
often relative to the other projects. The card lives in a projects/ folder of
its home: the chapter of a live library it requires, else the overview area of
Mathlib it uses most. The host's page lists the folder without owning it, so the
host's generator never reads these pages. A project with no headline is listed by
its facts on its home's projects page. The README's opening is quoted only when
the license at the pinned commit is one this module recognizes from its text.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import tomllib
from collections import Counter
from pathlib import Path

from . import leanblueprint, leansource
from .ff import CODE, FENCE, HEADING, blocks, plural, safe
from .mathlib import title_key
from .vault import Container, Entry, Leaf, chunk, link_text, short

SCHEMA = "trough-satellites/v1"
GITHUB = "https://github.com"
# Lake packages that build, document or test a project rather than add mathematics to it.
INFRASTRUCTURE = {"checkdecls", "doc-gen4", "«doc-gen4»", "verso", "subverso", "cli", "plausible", "aesop",
                  "proofwidgets", "importgraph", "leansearchclient", "tryateachstep", "leansqlite", "lean-tqdm",
                  "md4lean", "batteries", "qq", "lean4checker", "unicodebasic", "bibtexquery", "versoblueprint",
                  "leanarchitect", "verso-blueprint"}
MAX_FILES = 5000  # .lean files read per project
MAX_HEADLINES = 8
MAX_USES = 8
QUOTE_LIMIT = 600
STALE_DAYS = 90  # a pin older than this, by its commit's date, moves to the newest commit
MAIN_MODULES = {"Main", "MainTheorem", "MainTheorems", "Statement", "Statements"}
THEOREMS = ("theorem", "lemma")
RULES = {
    "blueprint": "Lean names of the blueprint nodes that no other node uses, marked \\leanok",
    "readme": "theorems its README names in code",
    "main": "theorems of its module named Main, MainTheorem(s) or Statement(s)",
}
LICENSE_NAME = re.compile(r"^(?:LICEN[CS]E|COPYING)(?:[-._][^/]*)?$", re.I)
README_NAME = re.compile(r"^README(?:\.md|\.markdown)?$", re.I)
OPEN = re.compile(r"^[ \t]*open[ \t]+(?!scoped\b)([^\n]*)", re.M)
NAMESPACE = re.compile(r"^[ \t]*namespace[ \t]+(\S+)", re.M)
IMPORT = re.compile(r"^[ \t]*(?:public[ \t]+|private[ \t]+)?(?:meta[ \t]+)?import[ \t]+(?:all[ \t]+)?([^\n]*)", re.M)
TOKEN = re.compile(r"(?<![\w.'!?])[^\W\d][\w'!?]*(?:\.[^\W\d][\w'!?]*)*")
AXIOM = re.compile(r"^[ \t]*(?:(?:private|protected|noncomputable|unsafe)[ \t]+)*axiom[ \t]", re.M)
SENTENCE_END = re.compile(r"[.!?][\"'”’)\]*_]*(?=\s|$)")
ABBREVIATION = re.compile(r"(?:\b(?:e\.g|i\.e|cf|resp|vs|et al|Fig|Thm|Prop|Sec|Ch|Dr|Prof|No)|\b[A-Z])\.$")


# Hand-kept files.

def load_projects(path: Path) -> list[dict]:
    projects = tomllib.loads(path.read_text(encoding="utf-8")).get("project", []) if path.is_file() else []
    slugs = [project["slug"] for project in projects]
    if len(set(slugs)) != len(slugs):
        raise ValueError(f"{path}: a slug is used twice")
    return projects


def load_packages(path: Path) -> dict[str, dict]:
    """Package URLs, as repo_key() gives them, that stand for a catalog library."""
    packages = tomllib.loads(path.read_text(encoding="utf-8")).get("package", []) if path.is_file() else []
    return {repo_key(package["url"]): package for package in packages}


def load_overrides(path: Path) -> dict[str, dict]:
    overrides = tomllib.loads(path.read_text(encoding="utf-8")).get("override", []) if path.is_file() else []
    for override in overrides:
        if not str(override.get("reason", "")).strip():
            raise ValueError(f"{path}: the override for {override.get('repo')} gives no reason")
    return {override["repo"].lower(): override for override in overrides}


def repo_key(url: str) -> str:
    """A repository URL as owner/name in lower case when it is on GitHub, else the URL."""
    match = re.match(r"(?:https?://|git@)github\.com[/:]([^/]+)/([^/#?]+?)(?:\.git)?/?$", url.strip())
    return f"{match.group(1)}/{match.group(2)}".lower() if match else url.strip()


# Reading a checkout.

def recognize(text: str) -> tuple[str | None, list[str]]:
    """The license a license file's text is, when it is one of those this module quotes under, and its
    copyright lines. The text must open as the license does, after a title and copyright lines."""
    lines = text.replace("\r\n", "\n").split("\n")
    copyright, start = [], 0
    for start, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or re.fullmatch(r"(?:The )?MIT License(?: \(MIT\))?|MIT No Attribution|"
                                        r"BSD [23]-Clause License|(?:The )?BSD License", stripped, re.I):
            continue
        if re.match(r"(?:Copyright\b|\(c\)|©)", stripped, re.I):
            copyright.append(stripped)
            continue
        break
    body = " ".join(" ".join(lines[start:]).split())
    flat = " ".join(text.split())
    if flat.startswith("Apache License Version 2.0, January 2004"):
        return "Apache-2.0", []
    if body.startswith("Permission is hereby granted, free of charge, to any person obtaining a copy"):
        attribution = "The above copyright notice and this permission notice shall be included" in body
        return ("MIT" if attribution else "MIT-0"), copyright
    if body.startswith("Redistribution and use in source and binary forms, with or without modification, are "
                       "permitted provided that the following conditions are met"):
        if "advertising materials" in body:
            return None, copyright
        return ("BSD-3-Clause" if "Neither the name" in body else "BSD-2-Clause"), copyright
    head = flat[:400]
    if re.match(r"(?:Creative Commons Legal Code )?CC0 1\.0 Universal", head):
        return "CC0-1.0", []
    if re.match(r"(?:Creative Commons )?Attribution 4\.0 International", head) and \
            not re.search(r"NonCommercial|ShareAlike|NoDerivatives", head):
        return "CC-BY-4.0", copyright
    return None, copyright


def read_license(checkout: Path, paths: list[str]) -> dict:
    """The license files at the repository's root, and the first whose text recognize() knows. A LICENSES/
    folder (the REUSE layout) is listed but not applied: REUSE licenses only the files that name it."""
    root = sorted(path for path in paths if "/" not in path and LICENSE_NAME.match(path))
    reuse = sorted(path for path in paths if path.startswith("LICENSES/"))
    record = {"files": root + reuse, "spdx": None, "file": None, "copyright": []}
    for path in root:
        spdx, copyright = recognize(read_text(checkout / path))
        if spdx:
            record.update(spdx=spdx, file=path, copyright=copyright)
            break
    return record


def read_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8", errors="replace") if path.is_file() else ""


def plain_title(markdown: str) -> str:
    """A heading's text without its Markdown marks, links or HTML."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", markdown)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_`]+", "", text)
    return " ".join(text.split())


def readme_parts(readme: str) -> tuple[str, str | None]:
    """A README's title, its first heading, and its opening paragraph: the first paragraph of prose that is not
    badges, images or HTML, cut after its last sentence that ends within QUOTE_LIMIT characters (None when
    none does)."""
    lines = readme.replace("\r\n", "\n").split("\n")
    title = ""
    for line in lines:
        if (heading := HEADING.match(line)) and not FENCE.match(line):
            title = plain_title(heading.group(2))
            break
    if not title:
        setext = re.search(r"^([^\n]+)\n=+[ \t]*$", readme, re.M)
        title = plain_title(setext.group(1)) if setext else ""
    for kind, text in blocks(lines):
        if kind != "prose" or text.startswith(("|", "<", "```", "~~~", ">")):
            continue
        visible = re.sub(r"!\[[^\]]*\]\([^)]*\)|<[^>]+>|\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)", "", text)
        if not re.search(r"[A-Za-z]{3}", visible) or "](" in visible and not re.sub(r"\[[^\]]*\]\([^)]*\)", "", visible).strip():
            continue
        if re.match(r"\s*(?:=+|-+)\s*$", text.split("\n")[-1]):
            continue  # a setext heading
        return title, opening_sentences(text)
    return title, None


def opening_sentences(paragraph: str) -> str | None:
    """The paragraph up to its last sentence end within QUOTE_LIMIT characters, outside code spans."""
    flat = " ".join(paragraph.split())
    code = [match.span() for match in CODE.finditer(flat)]
    best = None
    for match in SENTENCE_END.finditer(flat):
        end = match.end()
        if end > QUOTE_LIMIT:
            break
        if any(start < match.start() < stop for start, stop in code):
            continue
        if ABBREVIATION.search(flat[:match.start() + 1]):
            continue
        best = end
    return flat[:best] if best else None


def lean_libraries(project: Path) -> list[dict]:
    """The Lean libraries the project's lakefile defines: each name, its source folder and its root modules."""
    toml = project / "lakefile.toml"
    if toml.is_file():
        try:
            config = tomllib.loads(read_text(toml))
        except tomllib.TOMLDecodeError:
            return []
        base = str(config.get("srcDir", ".")).strip("/") or "."
        libraries = []
        for library in config.get("lean_lib", []):
            name = str(library.get("name", ""))
            roots = [str(root) for root in library.get("roots", [])] or [name]
            roots += [re.sub(r"\.[+*]$", "", str(glob)).rstrip(".") for glob in library.get("globs", [])]
            libraries.append({"name": name, "src": join(base, str(library.get("srcDir", "."))),
                              "roots": sorted(set(filter(None, roots)))})
        return libraries
    original = read_text(project / "lakefile.lean")
    # Matched in the text with comments and strings blanked, and read from the original at the same places.
    text = leansource.blank(original)
    package = re.search(r"^package[ \t]+\S+([^\n]*(?:\n(?:[ \t][^\n]*)?)*)", text, re.M)
    base = re.search(r'srcDir\s*:=\s*"([^"]*)"', original[package.start(1):package.end(1)]) if package else None
    base_dir = base.group(1).strip("/") or "." if base else "."
    libraries = []
    for match in re.finditer(r"^(?:@\[[^\]\n]*\][ \t]*)?lean_lib[ \t]+(«[^»\n]+»|[^\s{]+)([^\n]*(?:\n(?:[ \t][^\n]*)?)*)",
                             text, re.M):
        name = match.group(1).strip("«»")
        body = original[match.start(2):match.end(2)]
        src = re.search(r'srcDir\s*:=\s*"([^"]*)"', body)
        roots = [root.strip("«»").rstrip(".") for key in ("roots", "globs")
                 for listing in re.findall(rf"{key}\s*:=\s*#\[([^\]]*)\]", body)
                 for root in re.findall(r"`(«[^»]+»|[\w.'«»]+)", listing)]
        libraries.append({"name": name, "src": join(base_dir, src.group(1) if src else "."),
                          "roots": sorted(set(roots or [name]))})
    return libraries


def join(*parts: str) -> str:
    joined = "/".join(part.strip("/") for part in parts if part.strip("/") not in ("", "."))
    return joined or "."


def project_dir(paths: list[str]) -> str | None:
    """The folder holding the Lake project: the root, else the shallowest folder with a lakefile, preferring
    one with a manifest. None when there is no lakefile (a Lean 3 project has leanpkg.toml)."""
    lakefiles = sorted({path.rsplit("/", 1)[0] if "/" in path else "" for path in paths
                        if path.rsplit("/", 1)[-1] in ("lakefile.lean", "lakefile.toml")},
                       key=lambda folder: (folder.count("/") + bool(folder), folder))
    if not lakefiles:
        return None
    manifests = {path.rsplit("/", 1)[0] if "/" in path else "" for path in paths
                 if path.rsplit("/", 1)[-1] == "lake-manifest.json"}
    depth = lakefiles[0].count("/") + bool(lakefiles[0])
    shallowest = [folder for folder in lakefiles if folder.count("/") + bool(folder) == depth]
    return next((folder for folder in shallowest if folder in manifests), shallowest[0])


def library_files(paths: list[str], folder: str, libraries: list[dict]) -> dict[str, str]:
    """Each .lean file of the project's libraries, by path in the repository, with its module name."""
    prefix = f"{folder}/" if folder else ""
    out: dict[str, str] = {}
    lean = sorted(path for path in paths if path.endswith(".lean") and path.startswith(prefix))
    if not libraries:
        # No library: every .lean file outside Lake's build and package folders, named from the project folder.
        for path in lean:
            inner = path[len(prefix):]
            if not inner.startswith((".lake/", "lake-packages/")) and "/.lake/" not in inner:
                out[path] = inner.removesuffix(".lean").replace("/", ".")
        return out
    for library in libraries:
        src = "" if library["src"] == "." else library["src"] + "/"
        for root in library["roots"]:
            stem = prefix + src + root.replace(".", "/")
            for path in lean:
                if path == stem + ".lean" or path.startswith(stem + "/"):
                    out.setdefault(path, path[len(prefix + src):].removesuffix(".lean").replace("/", "."))
    return out


def requirements(manifest: dict) -> tuple[list[dict], str]:
    """The packages the manifest names directly, but for Mathlib and infrastructure, and Mathlib's commit."""
    out, mathlib = [], ""
    for package in manifest.get("packages", []):
        name = str(package.get("name", ""))
        if name == "mathlib":
            mathlib = str(package.get("rev", ""))
            continue
        if package.get("inherited", False) or name.lower() in INFRASTRUCTURE:
            continue
        out.append({"name": name, "url": str(package.get("url", "") or package.get("dir", "")),
                    "rev": str(package.get("rev", ""))})
    return sorted(out, key=lambda package: package["name"].lower()), mathlib


def opens(code: str) -> list[str]:
    """The namespaces a file's `open` commands open and those its `namespace` commands enter, with every
    prefix of each."""
    found: set[str] = set()
    for line in OPEN.findall(code):
        line = re.split(r"\(|\bhiding\b|\brenaming\b|\bin\b", line)[0]
        found.update(name for name in line.split() if leansource.is_name(name))
    for name in NAMESPACE.findall(code):
        parts = leansource.split(name)
        found.update(".".join(parts[:end]) for end in range(1, len(parts) + 1))
    return sorted(found)


def resolve(code: str, scopes: list[str], names: set[str], by_last: dict[str, list[str]]) -> set[str]:
    """The names of *names* the code writes: in full, or after one of *scopes*, the file's open namespaces."""
    found = set()
    scope_set = set(scopes)
    for token in set(TOKEN.findall(code)):
        token = token.removeprefix("_root_.")
        last = token.rsplit(".", 1)[-1]
        for name in by_last.get(last, ()):
            if name == token or (name.endswith("." + token) and name[:-len(token) - 1] in scope_set):
                found.add(name)
    return found


def index(names: set[str]) -> dict[str, list[str]]:
    by_last: dict[str, list[str]] = {}
    for name in names:
        by_last.setdefault(name.rsplit(".", 1)[-1], []).append(name)
    return by_last


def blueprint_names(checkout: Path, paths: list[str]) -> list[str] | None:
    """The Lean names of the blueprint's nodes that no other node uses, marked \\leanok and not definitions,
    in document order; None when there is no blueprint."""
    webs = sorted((path for path in paths if re.search(r"(?:^|/)blueprint/src/web\.tex$", path)),
                  key=lambda path: (path.count("/"), path))
    if not webs:
        return None
    blueprint = leanblueprint.read(checkout / webs[0].rsplit("/", 1)[0], "web.tex")
    used = {label for node in blueprint.graph for label in node.uses + node.proof_uses}
    names = []
    for node in blueprint.graph:
        if node.leanok and node.env != "definition" and not used & set(node.labels + [node.id]):
            names += [name for name in node.lean if name not in names]
    return names


def readme_names(readme: str) -> list[str]:
    """The text of the README's inline code spans that reads as one Lean name, in order, outside fenced code."""
    out, fence = [], None
    for line in readme.split("\n"):
        match = FENCE.match(line)
        if fence:
            if match and match.group(1)[0] == fence:
                fence = None
            continue
        if match:
            fence = match.group(1)[0]
            continue
        for span in re.findall(r"(?<!`)`([^`\n]+)`(?!`)", line):
            span = span.strip().removeprefix("@")
            if leansource.is_name(span) and span not in out:
                out.append(span)
    return out


def by_suffix(name: str, declared: dict, by_last: dict[str, list[str]]) -> str | None:
    """The declared name *name* is, in full or as the end of exactly one declared name."""
    if name in declared:
        return name
    matches = [full for full in by_last.get(name.rsplit(".", 1)[-1], ()) if full.endswith("." + name)]
    return matches[0] if len(matches) == 1 else None


def headlines(checkout: Path, paths: list[str], readmes: list[str],
              declared: dict[str, tuple[str, str, leansource.Declaration]]) -> tuple[str | None, list[str], int]:
    """The rule that names the project's headlines, the names (at most MAX_HEADLINES), and how many it names."""
    by_last = index(set(declared))
    candidates = blueprint_names(checkout, paths)
    if candidates:
        names = [name for name in candidates if name in declared and declared[name][2].kind != "instance"]
        if names:
            return "blueprint", names[:MAX_HEADLINES], len(names)
    names = []
    for readme in readmes:
        for span in readme_names(readme):
            # Only theorems: a README names definitions as its vocabulary, not as its results.
            full = by_suffix(span, declared, by_last)
            if full and full not in names and declared[full][2].kind in THEOREMS:
                names.append(full)
    if names:
        return "readme", names[:MAX_HEADLINES], len(names)
    names = [name for name, (_, module, found) in sorted(declared.items(), key=lambda item: (item[1][0], item[1][2].line))
             if module.rsplit(".", 1)[-1] in MAIN_MODULES and found.kind in THEOREMS]
    if names:
        return "main", names[:MAX_HEADLINES], len(names)
    return None, [], 0


def chapter_names(vault: Path) -> set[str]:
    """The `lean:` names of the vault's pages outside projects/ folders, for statement edges."""
    names = set()
    for page in (vault / "roadmap").rglob("*.md"):
        if "projects" in page.relative_to(vault).parts:
            continue
        with page.open(encoding="utf-8") as handle:
            if handle.readline() != "---\n":
                continue
            for line in handle:
                if line == "---\n":
                    break
                if line.startswith("lean: "):
                    names.update(name.strip() for name in line[6:].split(","))
    return names


def concept_heads(links: Path) -> set[str]:
    """The first declaration of each Mathlib article, the name a project's use of the concept is read by."""
    heads = set()
    for line in read_text(links / "mathlib" / "articles.jsonl").splitlines():
        ends = json.loads(line).get("object", [])
        if ends and ends[0].get("location", {}).get("declaration"):
            heads.add(ends[0]["location"]["declaration"])
    return heads


def metadata(checkout: Path, paths: list[str]) -> dict:
    """What a checkout of the metadata files alone gives: the license, README, Lake project folder and
    requirements, and the digest of what moves a pin (the requirements, README opening and license texts)."""
    license_record = read_license(checkout, paths)
    readme_path = next((path for path in sorted(paths) if "/" not in path and README_NAME.match(path)), None)
    readme = read_text(checkout / readme_path) if readme_path else ""
    title, excerpt = readme_parts(readme)
    folder = project_dir(paths)
    manifest_path = checkout / folder / "lake-manifest.json" if folder is not None else None
    try:
        manifest = json.loads(read_text(manifest_path)) if manifest_path and manifest_path.is_file() else {}
    except json.JSONDecodeError:
        manifest = {}
    required, mathlib = requirements(manifest if isinstance(manifest, dict) else {})
    license_texts = [read_text(checkout / path) for path in license_record["files"]]
    digest = hashlib.sha256(json.dumps(
        [[(package["name"], package["url"]) for package in required], excerpt, license_texts]).encode()).hexdigest()
    return {"license": license_record, "readme_path": readme_path, "readme": readme, "title": title,
            "excerpt": excerpt, "folder": folder, "requirements": required, "mathlib": mathlib, "stable": digest}


def read_project(checkout: Path, project: dict, rev: str, date: str, paths: list[str], heads: set[str],
                 names: set[str]) -> dict:
    """A project's record at its checkout's commit. *paths* are every file the commit has; *heads* the Mathlib
    concepts' names and *names* the other chapters' `lean:` names."""
    record: dict = {"schema": SCHEMA, "repo": project["repo"], "slug": project["slug"], "rev": rev, "date": date}
    meta = metadata(checkout, paths)
    license_record, readme_path, readme, title, excerpt, folder, required, mathlib = (
        meta["license"], meta["readme_path"], meta["readme"], meta["title"], meta["excerpt"], meta["folder"],
        meta["requirements"], meta["mathlib"])
    record["stable"] = meta["stable"]
    record["license"] = license_record
    record["readme"] = {"file": readme_path, "title": title,
                        "excerpt": excerpt if license_record["spdx"] else None}
    record["lean_files"] = sum(path.endswith(".lean") and path.rsplit("/", 1)[-1] != "lakefile.lean" for path in paths)
    if folder is None:
        record["admitted"] = False
        record["reason"] = ("a Lean 3 project: leanpkg.toml and no lakefile" if any(
            path.rsplit("/", 1)[-1] == "leanpkg.toml" for path in paths) else "no lakefile")
        return record
    record["admitted"] = True
    toolchain = read_text(checkout / folder / "lean-toolchain").strip()
    libraries = lean_libraries(checkout / folder)
    files = library_files(paths, folder, libraries)
    record.update(folder=folder, toolchain=toolchain.split(":")[-1], mathlib=mathlib, requirements=required,
                  libraries=libraries, library_files=min(len(files), MAX_FILES), capped=len(files) > MAX_FILES)
    declared: dict[str, tuple[str, str, leansource.Declaration]] = {}
    twice: set[str] = set()
    imports: Counter = Counter()
    roots: Counter = Counter()
    uses: Counter = Counter()
    counts: Counter = Counter()
    file_scopes: dict[str, list[str]] = {}
    file_imports: dict[str, set[str]] = {}
    sorry_paths: set[str] = set()
    axioms: dict[str, int] = {}
    head_index = index(heads)
    for path in sorted(files)[:MAX_FILES]:
        text = read_text(checkout / path)
        code = leansource.blank(text)
        imported = {module for line in IMPORT.findall(code) for module in line.split() if leansource.is_name(module)}
        imports.update(module for module in imported if module.startswith("Mathlib."))
        roots.update({module.split(".")[0] for module in imported})
        file_imports[path] = imported
        if leansource.SORRY.search(code):
            sorry_paths.add(path)
        axioms[path] = len(AXIOM.findall(code))
        scopes = opens(code)
        file_scopes[path] = scopes
        uses.update(resolve(code, scopes, heads, head_index))
        found = leansource.scan(text)
        if found is None:
            counts["unclosed_files"] += 1
            continue
        for name, declaration in found.items():
            if name in declared:
                twice.add(name)
            declared.setdefault(name, (path, files[path], declaration))
    for name in twice:
        del declared[name]
    readmes = [readme] + ([read_text(checkout / folder / "README.md")] if folder else [])
    rule, chosen, total = headlines(checkout, paths, readmes, declared)
    targets = heads | names
    target_index = index(targets)
    heads_out = []
    for name in chosen:
        path, module, declaration = declared[name]
        statement = declaration.statement or ""
        parts = leansource.split(name)
        scopes = sorted(set(file_scopes[path]) | {".".join(parts[:end]) for end in range(1, len(parts))})
        named = resolve(leansource.blank(statement), scopes, targets, target_index) - {name}
        heads_out.append({"name": name, "module": module, "file": path, "line": declaration.line,
                          "kind": declaration.kind, "sorry": declaration.sorry, "names": sorted(named)})
    # The files the headlines' files import, directly or not, through the project's own modules.
    by_module = {module: path for path, module in files.items() if path in file_imports}
    closure, todo = set(), sorted({declared[name][0] for name in chosen})
    while todo:
        path = todo.pop()
        if path not in closure:
            closure.add(path)
            todo += [by_module[module] for module in file_imports.get(path, ()) if module in by_module]
    record.update(declarations=len(declared), sorry_files=len(sorry_paths), axioms=sum(axioms.values()),
                  closure_files=len(closure), closure_sorry=sorted(closure & sorry_paths)[:20],
                  closure_axioms=sum(axioms[path] for path in closure),
                  unclosed_files=counts["unclosed_files"], headline_rule=rule, headline_count=total,
                  headlines=heads_out, mathlib_imports=dict(sorted(imports.items())),
                  import_roots=dict(sorted(roots.items())), uses=dict(sorted(uses.items())))
    return record


# The chapter, from the records.

NO_DEPENDS = "Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site."
MATHLIB_REPO = "https://github.com/leanprover-community/mathlib4"
OVERVIEW = "mathlib:overview"  # the home of a Mathlib project no area claims
CI_WORDS = {"SUCCESS": "passing", "FAILURE": "failing", "ERROR": "failing", "PENDING": "pending",
            "EXPECTED": "pending"}


def load(data: Path) -> tuple[list[dict], dict, dict]:
    """The records under data/satellites/, in the order of projects.toml, with the packages and overrides."""
    folder = data / "satellites"
    records = []
    for project in load_projects(folder / "projects.toml"):
        path = folder / f"{project['slug']}.json"
        if path.is_file():
            records.append(json.loads(path.read_text(encoding="utf-8")) | {"kind": project["kind"]})
    return records, load_packages(folder / "packages.toml"), load_overrides(folder / "overrides.toml")


def module_of(leaf: Leaf) -> str | None:
    file = dict(leaf.fields).get("mathlib_file")
    return file.removesuffix(".lean").replace("/", ".") if file else None


class Areas:
    """Mathlib's overview areas: the area of each concept, and of each module by its longest prefix that the
    modules of an area's concepts share."""

    def __init__(self, areas: dict[str, Container]):
        self.order = list(areas)
        self.titles = {slug: container.title for slug, container in areas.items()}
        self.of_leaf: dict[int, str] = {}
        self.prefixes: dict[str, Counter] = {}
        for slug, container in areas.items():
            for node in walk_leaves(container):
                self.of_leaf[id(node)] = slug
                if module := module_of(node):
                    parts = module.split(".")
                    for end in range(2, len(parts) + 1):
                        self.prefixes.setdefault(".".join(parts[:end]), Counter())[slug] += 1

    def module(self, module: str) -> str | None:
        parts = module.split(".")
        for end in range(len(parts), 1, -1):
            if counts := self.prefixes.get(".".join(parts[:end])):
                return min(self.order, key=lambda slug: (-counts[slug], self.order.index(slug)))
        return None

    def leaf(self, leaf: Leaf) -> str | None:
        if id(leaf) in self.of_leaf:
            return self.of_leaf[id(leaf)]
        return self.module(module) if (module := module_of(leaf)) else None

    def shares(self, record: dict) -> tuple[Counter, int]:
        """The files importing each area's modules, and the imports mapped to an area."""
        counts: Counter = Counter()
        for module, files in record.get("mathlib_imports", {}).items():
            if area := self.module(module):
                counts[area] += files
        return counts, sum(counts.values())


def walk_leaves(container: Container):
    for child in container.children:
        if isinstance(child, Container):
            yield from walk_leaves(child)
        else:
            yield child


def plurality(areas: list[str], order: list[str]) -> str | None:
    counts = Counter(area for area in areas if area)
    return min(counts, key=lambda area: (-counts[area], order.index(area))) if counts else None


def area_lifts(record: dict, areas: Areas, baseline: dict[str, float]) -> list[tuple[str, float, int, int]]:
    """Each area holding at least a tenth of the project's mapped Mathlib imports, with its lift over the
    average project's share, its imports and the project's mapped total, by lift."""
    counts, total = areas.shares(record)
    rows = [(area, (counts[area] / total) / baseline[area], counts[area], total) for area in areas.order
            if total and counts[area] * 10 >= total and baseline.get(area)]
    return sorted(rows, key=lambda row: (-row[1], areas.order.index(row[0])))


def baselines(records: list[dict], areas: Areas) -> dict[str, float]:
    shares = []
    for record in records:
        counts, total = areas.shares(record)
        if total:
            shares.append({area: counts[area] / total for area in areas.order})
    return {area: sum(share[area] for share in shares) / len(shares) for area in areas.order} if shares else {}


def use_lifts(record: dict, records: list[dict]) -> list[tuple[str, float]]:
    """The Mathlib concepts the project's files name, by lift: the share of its files naming one over the
    average share across the projects."""
    def share(item: dict, name: str) -> float:
        return item.get("uses", {}).get(name, 0) / item["library_files"] if item.get("library_files") else 0.0

    readers = [item for item in records if item.get("library_files")]
    out = []
    for name in record.get("uses", {}):
        average = sum(share(item, name) for item in readers) / len(readers)
        out.append((name, share(record, name) / average if average else 0.0))
    return sorted(out, key=lambda pair: (-pair[1], -record["uses"][pair[0]], pair[0]))


def live_requirements(record: dict, live: dict[str, tuple[str, str]], hosts: dict) -> list[tuple[str, dict, str]]:
    """The requirements that are a live chapter's library with a page here: its id, the package and how the
    package stands for it."""
    out = []
    for package in record.get("requirements", []):
        if (found := live.get(repo_key(package["url"]))) and found[0] in hosts:
            out.append((found[0], package, found[1]))
    return out


def home(record: dict, live: dict[str, tuple[str, str]], hosts: dict, overrides: dict, areas: Areas,
         baseline: dict[str, float], statement_areas: list[str], use_areas: list[str],
         order: list[str]) -> tuple[str | None, str]:
    """Where the project's card goes, a key of *hosts*, and the evidence for it in a sentence; None when it
    builds on neither Mathlib nor a mapped library."""
    if override := overrides.get(record["repo"].lower()):
        if override["home"] not in hosts:
            raise ValueError(f"overrides.toml: {record['repo']} has home {override['home']!r}, which is no page here")
        return override["home"], f"Placed by hand. {override['reason']}"
    chapters = live_requirements(record, live, hosts)
    if chapters:
        roots = record.get("import_roots", {})
        chosen, package, how = min(chapters, key=lambda item: (-roots.get(item[1]["name"], 0), order.index(item[0])))
        files = roots.get(package["name"], 0)
        return chosen, (f"Its Lake manifest requires `{package['name']}`" + (f", {how}" if how else "")
                        + (f", whose modules {plural(files, 'file')} of the project import." if files else "."))
    if not record.get("mathlib") and not record.get("mathlib_imports"):
        return None, "It requires neither Mathlib nor a library mapped here."
    counts = Counter(statement_areas)
    if len(statement_areas) >= 3 and (area := plurality(statement_areas, areas.order)) and counts[area] * 2 > len(statement_areas):
        return f"mathlib:{area}", (f"{counts[area]} of the {plural(len(statement_areas), 'Mathlib concept')} its "
                                   f"headline statements name are in {areas.titles[area]}.")
    if lifts := area_lifts(record, areas, baseline):
        area, lift, files, total = lifts[0]
        return f"mathlib:{area}", (f"Of its imports of Mathlib modules in an overview area, {files} of {total} are in "
                                   f"{areas.titles[area]}, {lift:.1f} times the average project's share, the most "
                                   "of the areas holding a tenth of its imports.")
    if area := plurality(use_areas, areas.order):
        return f"mathlib:{area}", (f"{Counter(use_areas)[area]} of the {len(use_areas)} Mathlib concepts its files "
                                   f"name are in {areas.titles[area]}.")
    return OVERVIEW, "It builds on Mathlib, but neither its statements, imports nor names point to one overview area."


def blob(record: dict, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{record['repo']}/blob/{record['rev']}/{path}" + (f"#L{line}" if line else "")


def tree(record: dict) -> str:
    return f"{GITHUB}/{record['repo']}/tree/{record['rev']}"


def at(record: dict) -> str:
    return f"[{record['rev'][:8]}]({tree(record)})"


def proof_formalized(record: dict) -> bool:
    return bool(record["headlines"]) and not (record["closure_sorry"] or record["closure_axioms"] or record["capped"])


def notice(record: dict) -> str:
    license_record = record["license"]
    return ", ".join([license_record["spdx"], *license_record["copyright"]])


def title(record: dict) -> str:
    return short(record["readme"]["title"], 80) if record["readme"].get("title") else record["repo"].split("/")[1]


def heading_text(text: str) -> str:
    return re.sub(r"([\\`*_\[\]<])", r"\\\1", text)


def card(record: dict, depends: list[Leaf], uses: list[Leaf], named: int, placement: str,
         builds_on: list[str], lifts: list[tuple[str, float, int, int]], areas: Areas) -> tuple[Leaf, dict[str, str]]:
    """A project's card, and the source links of its headline names."""
    heads = record["headlines"]
    fields = [("declaration", heads[0]["kind"]), ("origin", "cited"),
              ("lean", ", ".join(head["name"] for head in heads)), ("statement", "formalized")]
    if proof_formalized(record):
        fields.append(("proof", "formalized"))
    body = f"[{record['repo']}]({GITHUB}/{record['repo']}) at commit {at(record)}, {record['date'][:10]}."
    excerpt = record["readme"].get("excerpt")
    if excerpt and record["license"]["spdx"]:
        body += (f"\n\n> {safe(excerpt)}\n\n*Quoted from [{record['readme']['file']}]"
                 f"({blob(record, record['readme']['file'])}), {notice(record)}.*")
    count = (f"{len(heads)} of the {record['headline_count']}" if record["headline_count"] > len(heads)
             else "the")
    proof = (f"No file its headlines import, directly or not ({plural(record['closure_files'], 'file')}), holds "
             "`sorry`, `admit` or an axiom." if proof_formalized(record) else
             f"Of the files its headlines import, directly or not, {', '.join(f'`{path}`' for path in record['closure_sorry'])} "
             "hold `sorry` or `admit`." if record["closure_sorry"] else "")
    rows = [f"- [`{head['name']}`]({blob(record, head['file'], head['line'])}) ({head['kind']}"
            + (", its text holds `sorry`" if head["sorry"] else "") + ")" for head in heads]
    notes = [("Main results", f"Its Lean names are {count} {RULES[record['headline_rule']]}:\n\n" + "\n".join(rows)
              + (f"\n\n{proof}" if proof else ""))]
    facts = [f"- Lean {record['toolchain'] or 'toolchain not given'}"
             + (f", Mathlib at [{record['mathlib'][:8]}]({MATHLIB_REPO}/tree/{record['mathlib']})"
                if re.fullmatch(r"[0-9a-f]{40}", record.get("mathlib") or "") else "") + ".",
             f"- {record['lean_files']:,} .lean files; "
             + (f"its Lean libraries {', '.join(f'`{library['name']}`' for library in record['libraries'])} hold "
                if record["libraries"] else "the project folder holds ")
             + f"{record['library_files']:,}{' (the first read)' if record['capped'] else ''}, declaring "
             f"{record['declarations']:,} names, with `sorry` in {plural(record['sorry_files'], 'file')} and "
             f"{plural(record['axioms'], 'axiom')}, read without Lean."]
    if record.get("ci"):
        facts.append(f"- Its own CI at this commit: {CI_WORDS.get(record['ci'], record['ci'].lower())}.")
    license_record = record["license"]
    if license_record["spdx"]:
        facts.append(f"- License: {license_record['spdx']} ([{license_record['file']}]"
                     f"({blob(record, license_record['file'])})).")
    elif license_record["files"]:
        facts.append(f"- License files: {', '.join(f'`{path}`' for path in license_record['files'])}; facts only.")
    else:
        facts.append("- No license file; facts only.")
    notes.append(("Project", "\n".join(facts)))
    if builds_on:
        notes.append(("Builds on", "\n".join(builds_on)))
    notes.append(("Placement", placement))
    if lifts or record.get("uses"):
        lines = [f"{areas.titles[area]} ({files} of {total} imports, {lift:.1f}×)" for area, lift, files, total in lifts[:3]]
        text = (f"Areas of its Mathlib imports by lift over the average project: {', '.join(lines)}." if lines else "")
        if record.get("uses"):
            text += (" " if text else "") + (
                f"*Proof depends on* names {len(uses)} of the {plural(named, 'Mathlib concept')} its files name, "
                "those named most often relative to the other projects.")
        notes.append(("Mathlib use", text))
    leaf = Leaf(heading_text(title(record)), record["slug"], fields, body, depends=depends, proof_depends=uses,
                notes=notes, no_depends=NO_DEPENDS)
    leaf.sources = [(f"{record['repo']} at {record['rev'][:8]}", tree(record))]
    return leaf, {head["name"]: blob(record, head["file"], head["line"]) for head in heads}


def listed(record: dict) -> str:
    """A project without a card, as its home's page lists it."""
    return (f"- [{record['repo']}]({GITHUB}/{record['repo']}) at {at(record)}: {record['lean_files']:,} .lean files, "
            f"{record['declarations']:,} declarations.")


def chapter(records: list[dict], packages: dict, overrides: dict, libraries: list[dict], hosts: dict[str, Container],
            heads: dict[str, Leaf], names: dict[str, Leaf]) -> tuple[list[tuple[Container, Container, dict[str, str]]],
                                                                   Counter, dict[str, Leaf | Container]]:
    """The projects pages: each with its host, the page that lists it, and its cards' source links; the counts;
    and the link targets of the cards' notes (for blueprints.resolve). *hosts* has a page per home: each live
    chapter's by its catalog id, and Mathlib's overview areas as "mathlib:<slug>", with the overview as OVERVIEW."""
    order = [library["id"] for library in libraries]
    live = {repo_key(library["repo"]): (library["id"], "") for library in libraries if library["map_status"] == "live"}
    live |= {key: (package["chapter"], package.get("reason", "")) for key, package in packages.items()}
    areas = Areas({key.removeprefix("mathlib:"): host for key, host in hosts.items()
                   if key.startswith("mathlib:") and key != OVERVIEW})
    admitted = [record for record in records if record.get("admitted")]
    baseline = baselines(admitted, areas)
    by_repo = {record["repo"].lower(): record for record in admitted}
    by_slug = {record["slug"]: record for record in admitted}
    stats: Counter = Counter(projects=len(records), admitted=len(admitted))
    placed: dict[str, list[tuple[dict, list[Leaf], list[Leaf], int, str, list, list]]] = {}
    for record in admitted:
        statement = []
        for head in record["headlines"]:
            for name in head["names"]:
                target = heads.get(name) or names.get(name)
                if target is not None and target not in statement:
                    statement.append(target)
        statement_areas = [areas.leaf(leaf) for leaf in statement if leaf in heads.values()]
        statement_areas = [area for area in statement_areas if area]
        ranked = [(heads[name], lift) for name, lift in use_lifts(record, admitted) if name in heads]
        uses = [leaf for leaf, _ in ranked if leaf not in statement][:MAX_USES]
        use_areas = [area for leaf, _ in ranked if (area := areas.leaf(leaf))]
        key, placement = home(record, live, hosts, overrides, areas, baseline, statement_areas, use_areas, order)
        if key is None:
            stats["held_back"] += 1
            continue
        builds_on = []
        if record.get("mathlib"):
            builds_on.append(f"- Mathlib, at [{record['mathlib'][:8]}]({MATHLIB_REPO}/tree/{record['mathlib']})."
                             if re.fullmatch(r"[0-9a-f]{40}", record["mathlib"]) else f"- Mathlib, at `{record['mathlib']}`.")
        for package in record.get("requirements", []):
            target = live.get(repo_key(package["url"]))
            other = by_repo.get(repo_key(package["url"]))
            rev = f" at `{package['rev'][:8]}`" if package["rev"] else ""
            if target and target[0] in hosts:
                builds_on.append(f"- [{link_text(package['name'])}](trough:{target[0]}){rev}"
                                 + (f", {target[1]}" if target[1] else "") + ".")
            elif other is not None:
                builds_on.append(f"- [{link_text(package['name'])}](trough:satellite:{other['slug']}){rev}.")
            else:
                url = package["url"]
                builds_on.append(f"- `{package['name']}`" + (f" ({url})" if url.startswith("https://") else "") + f"{rev}.")
        placed.setdefault(key, []).append((record, statement, uses, len(record.get("uses", {})), placement, builds_on,
                                           area_lifts(record, areas, baseline)))
    out = []
    targets: dict[str, Leaf | Container] = {}
    for key, host in hosts.items():
        members = placed.get(key)
        if not members:
            continue
        cards, links, without = [], {}, []
        for record, statement, uses, named, placement, builds_on, lifts in members:
            # A corpus collects many problems or theorems: none is its main result.
            if not record["headlines"] or record["kind"] == "corpus":
                without.append(record)
                stats["without_headline"] += 1
                continue
            leaf, names_here = card(record, statement, uses, named, placement, builds_on, lifts, areas)
            cards.append(leaf)
            links.update(names_here)
            targets[f"satellite:{record['slug']}"] = leaf
            stats["cards"] += 1
            stats[f"rule_{record['headline_rule']}"] += 1
            stats["statement_edges"] += len(statement)
            stats["proof_edges"] += len(uses)
            stats["mathlib_edges"] += any(leaf in heads.values() for leaf in statement + uses)
        cards.sort(key=lambda leaf: title_key(leaf.title))
        where = "across Mathlib" if key == OVERVIEW else f"building on {host.title}"
        projects = Container(f"Projects {where} ({len(cards) + len(without)})", "projects", [Entry(leaf) for leaf in cards])
        projects.prose = ("Lean projects outside the libraries mapped here that build on "
                          + ("Mathlib" if key == OVERVIEW else f"Mathlib, placed by their use of its {host.title.lower()}"
                             if key.startswith("mathlib:") else host.title)
                          + ", read at a pinned commit without Lean" + (", one card each." if cards else "."))
        if without:
            listing = "\n".join(["## Projects without a named main result", ""] + [listed(record) for record in without])
            if cards:
                projects.tail = listing
            else:
                projects.prose += "\n\n" + listing
        chunk(projects, budget=300_000)
        out.append((host, projects, links))
        stats["homes"] += 1
    # Requirements between projects become edges once every card exists.
    for _, projects, _ in out:
        for leaf in walk_leaves(projects):
            for package in by_slug[leaf.slug].get("requirements", []):
                other = by_repo.get(repo_key(package["url"]))
                if other is not None and (target := targets.get(f"satellite:{other['slug']}")) and target not in leaf.depends:
                    leaf.depends.append(target)
                    stats["satellite_edges"] += 1
    targets |= {key: host for key, host in hosts.items() if not key.startswith("mathlib:")}
    return out, stats, targets


def attach(host: Container, projects: Container) -> None:
    """List the projects page on its host's page, without the host owning it."""
    host.entries.append(Entry(projects, owned=False))
