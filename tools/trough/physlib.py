"""The Physlib chapter: leanprover-community/physlib, an article per Lean module.

leanprover-community/physlib digitalises results from physics in Lean, on Mathlib. Its repository holds three
libraries, as its README presents them: Physlib, the reviewed core; PhyslibAlpha, downstream of it under a lighter
review; and QuantumInfo, quantum information theory with its own conventions. Its handbook organizes a file around
one definition and names it after it, and every module carries a module docstring, so the chapter has an article
per module, in a part per library, a page per area and per folder below it, and a page for each deeper folder with
an API map, the repository's own account of an area. tools/refresh_physlib.py reads a checkout at a pinned commit
into data/physlib/ without Lean: each module's docstring, its section docstrings and its declarations as
trough.leansource reads them, the API maps, the significant results scripts/lint/exemptions/Theorems.txt lists, and
the README's descriptions. lean/physlib/PhyslibDeps.lean then reads with Lean which modules each module's statements
and proofs use, and which of the names read from the source Lean has.
"""

from __future__ import annotations

import json
import posixpath
import re
from collections import Counter, defaultdict
from pathlib import Path

from . import leansource
from .blueprints import Built, escape
from .cfsg import declaration_text
from .ff import is_apache
from .formal_conjectures import OPAQUE, module_name, natural, plural, quote, title_and_doc
from .mathlib import fence
from .stacks import comment, header, literal
from .vault import Container, Entry, Leaf, chunk, slugify

SCHEMA = "trough-physlib/v1"
REPO = "leanprover-community/physlib"
GITHUB = "https://github.com"
LIBRARIES = ("Physlib", "PhyslibAlpha", "QuantumInfo")
THEOREMS = "scripts/lint/exemptions/Theorems.txt"
API_MAP = "API-map.md"
HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
TODO = re.compile(r"\bTODO\b")
# A Lean reference of an API map: its number, the file and the names it lists, wrapped over lines.
REFERENCE = re.compile(r"^(\d+)\.[ \t]+(\S+\.lean)[ \t]+—[ \t]+(.*?)(?=^\d+\.[ \t]|\Z)", re.M | re.S)
LITERATURE = re.compile(r"^(\d+)\.[ \t]+(.*?)(?=^\d+\.[ \t]|\Z)", re.M | re.S)
LEAN_CITATION = re.compile(r"\[(\d+)\]")
# The kinds whose whole text is their statement: their fields or constructors.
WHOLE = ("structure", "class", "inductive")
LIBRARY_HEAD = re.compile(r"^###\s+\[\*\*(\w+)\*\*\]\(\./\w+\)\s*$")
MAINTAINER = re.compile(r"^- (.+?) \(@[\w-]+\)\s*$")


# Reading the repository.

def doc_spans(text: str) -> list[tuple[int, str]]:
    """Each `/-! ... -/` comment of the text, by the line it starts on, with its text as leansource.docstring gives
    it."""
    return [(text.count("\n", 0, start) + 1, leansource.docstring(text[start + 3:end - 2]))
            for start, end, kind in leansource.spans(text) if kind == "module doc"]


def read_module(text: str, path: str) -> dict | None:
    """A module's record: its title and module docstring, its section docstrings, and its declarations in file order
    with their docstrings and Lean statements, an instance with no name under the name ""; None when its scopes don't
    close as they open. The module docstring is the first `/-!` comment when it comes before the first declaration;
    the others are section docstrings. The reading is leansource's relaxed one, so a statement keeps the indentation
    its lines have in the file. A structure, class or inductive type keeps its whole text, its fields or
    constructors; a declaration whose statement has no `:=` or `where` keeps its header. `private` declarations are
    counted, not kept."""
    found = leansource.declarations(text, relaxed=True)
    if found is None:
        return None
    docs = doc_spans(text)
    first = min((declaration.line for declaration in found), default=None)
    opening = docs[0] if docs and (first is None or docs[0][0] < first) else None
    title, doc = title_and_doc(opening[1]) if opening else ("", "")
    kept = [declaration for declaration in found if not declaration.private]
    return {
        "file": path, "module": module_name(path), "title": title, "doc": doc,
        "sections": [{"line": line, "text": words} for line, words in (docs[1:] if opening else docs)],
        "declarations": [{"name": declaration.name, "kind": declaration.kind, "line": declaration.line,
                          "doc": declaration.doc,
                          "statement": declaration_text(text, declaration.line) if declaration.kind in WHOLE
                          else declaration.statement if declaration.statement is not None
                          else header(text, declaration.line),
                          "sorry": declaration.proof_sorry if declaration.statement is not None else declaration.sorry}
                         for declaration in kept],
        "private": sum(declaration.private for declaration in found),
    }


def read_api_map(text: str, path: str) -> dict:
    """An API map's title, its content sections as written, its numbered Lean references (each one's file and the
    names it lists) and its numbered literature references."""
    title = next((match.group(2) for line in text.split("\n") if (match := HEADING.match(line))
                  and len(match.group(1)) == 1), "")
    sections: list[tuple[str, list[str]]] = []
    for line in text.split("\n"):
        heading = HEADING.match(line)
        if heading and len(heading.group(1)) == 2:
            sections.append((heading.group(2), []))
        elif sections:
            sections[-1][1].append(line)
    bodies = [(heading, "\n".join(lines).strip()) for heading, lines in sections]
    lean = next((body for heading, body in bodies if heading == "Lean References"), "")
    literature = next((body for heading, body in bodies if heading == "References"), "")
    return {
        "file": path, "folder": path.rsplit("/", 1)[0], "title": title,
        "content": [{"heading": heading, "text": body} for heading, body in bodies if heading.startswith("Content")],
        "lean": {number: {"file": file, "names": re.findall(r"`([^`]+)`", rest)}
                 for number, file, rest in REFERENCE.findall(lean)},
        "references": {number: " ".join(rest.split()) for number, rest in LITERATURE.findall(literature)},
    }


def read_theorems(text: str) -> dict[str, list[str]]:
    """The names Theorems.txt lists, by the library whose `[L]` section lists them."""
    out: dict[str, list[str]] = {}
    library = None
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith("--"):
            continue
        if line.startswith("[") and line.endswith("]"):
            library = line[1:-1]
            out.setdefault(library, [])
        elif library:
            out[library].append(line)
    return out


def read_readme(text: str) -> dict:
    """The README's words on the project: the heading that describes it, each library's description in its table,
    the paragraphs of its PhyslibAlpha section, the sentence on how Physlib was formed, and the maintainers it
    names."""
    lines = text.split("\n")
    tagline = next((match.group(2) for line in lines if (match := HEADING.match(line.strip()))
                    and len(match.group(1)) == 2), "")
    libraries: dict[str, str] = {}
    for index, line in enumerate(lines):
        if match := LIBRARY_HEAD.match(line.strip()):
            words = []
            for following in lines[index + 1:]:
                if following.strip().startswith("<"):
                    if words:
                        break
                    continue
                words.append(following.strip())
            libraries[match.group(1)] = " ".join(" ".join(words).split())
    formed = next((re.split(r"(?<=\.)\s", " ".join(block.split()), maxsplit=1)[0] for block in text.split("\n\n")
                   if block.strip().startswith("Physlib was formed")), "")
    maintainers, alpha, section = [], [], ""
    for line in lines:
        if heading := HEADING.match(line):
            section = heading.group(2) if len(heading.group(1)) == 2 else section
        elif section == "Maintainers" and (match := MAINTAINER.match(line.strip())):
            maintainers.append(match.group(1))
        elif section == "PhyslibAlpha":
            alpha.append(line)
    paragraphs = [" ".join(block.split()) for block in "\n".join(alpha).split("\n\n") if block.strip()]
    return {"tagline": tagline, "libraries": libraries, "alpha": paragraphs, "formed": formed,
            "maintainers": maintainers}


def lean_paths(paths: list[str]) -> list[str]:
    """The modules of the three libraries among a commit's files, in path order."""
    return sorted((path for path in paths if path.endswith(".lean") and "/" in path and path.split("/")[0] in LIBRARIES),
                  key=natural)


def read(checkout: Path, paths: list[str]) -> tuple[dict, list[str]]:
    """The record of a checkout, with the problems that keep it from being written: a license that is not Apache-2.0,
    a file not checked out, a module whose scopes don't close, or a README that no longer describes each library."""
    problems = []
    license_file = checkout / "LICENSE"
    if not license_file.is_file() or not is_apache(license_file.read_text(encoding="utf-8")):
        problems.append(f"{REPO}: its LICENSE is not the Apache License 2.0")
    lean = lean_paths(paths)
    maps = sorted((path for path in paths if path.endswith("/" + API_MAP) and path.split("/")[0] in LIBRARIES), key=natural)
    wanted = [*lean, *maps, THEOREMS, "README.md"]
    missing = [path for path in wanted if not (checkout / path).is_file()]
    if missing:
        problems.append(f"not checked out: {missing[0]}" + (f" and {len(missing) - 1:,} other files" if len(missing) > 1 else ""))
    if not lean:
        problems.append(f"{REPO} has no .lean files under {', '.join(LIBRARIES)}")
    if problems:
        return {}, problems
    modules = []
    for path in lean:
        record = read_module((checkout / path).read_text(encoding="utf-8"), path)
        if record is None:
            problems.append(f"{path}: its scopes do not close as they open")
            continue
        modules.append(record)
    readme = read_readme((checkout / "README.md").read_text(encoding="utf-8"))
    problems += [f"README.md: no description of {library} in its table of libraries" for library in LIBRARIES
                 if not readme["libraries"].get(library)]
    if not readme["alpha"]:
        problems.append("README.md: no PhyslibAlpha section")
    record = {
        "license": "Apache-2.0", "readme": readme,
        "theorems": read_theorems((checkout / THEOREMS).read_text(encoding="utf-8")),
        "modules": modules,
        "api_maps": [read_api_map((checkout / path).read_text(encoding="utf-8"), path) for path in maps],
    }
    return record, problems


def mapped(modules: list[dict]) -> int:
    """The declarations a record maps: the named declarations of its modules."""
    return sum(len(module["declarations"]) for module in modules)


def shard(path: str) -> str:
    """The data file a module's record goes in: one per library and area."""
    parts = path.split("/")
    return ".".join(parts[:2]) if len(parts) > 2 else parts[0]


# The chapter, from the data.

TITLE = "Physlib: The Lean Physics Library"
MATHLIB_REPO = "https://github.com/leanprover-community/mathlib4"
LEAN_NAMES = 8  # the names a card's Lean row shows
# The bytes of article Markdown a listing page folds in before its next article starts a page.
PAGE_BUDGET = 250_000
NO_DEPENDS = "Its declarations' statements use no declaration of another module with an article here."
NO_DEPENDS_UNREAD = "No dependencies are recorded: they come from Lean's reading of the modules, which the data lack."
PLANS = re.compile(r"\b(?:underway|under way|planned|plans? to|will be|in the future)\b", re.I)
LIST_ITEM = re.compile(r"^[ \t]*[-*+][ \t]")
FENCE = re.compile(r"^ {0,3}(?:`{3,}|~{3,})")
CITATIONS = re.compile(r"((?:\s*\[(?:\d+|TODO)\])+)")
INLINE_LINK = re.compile(r"(?<!!)\[((?:[^\[\]\n]|\[[^\[\]\n]*\])*)\]\(([^()\s]+)\)")
SCHEME = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|#)")
API_MAP_PATH = re.compile(r"(\S+)/API-map\.md$")


def load(data: Path) -> dict | None:
    """data/physlib/'s source, API maps, module records and, when it is there, Lean's reading of them."""
    directory = data / "physlib"
    shards = sorted((directory / "modules").glob("*.json"))
    if not ((directory / "source.json").is_file() and (directory / "api-maps.json").is_file() and shards):
        return None
    modules = [module for path in shards for module in json.loads(path.read_text(encoding="utf-8"))["modules"]]
    deps = directory / "deps.json"
    return {"source": json.loads((directory / "source.json").read_text(encoding="utf-8")),
            "api_maps": json.loads((directory / "api-maps.json").read_text(encoding="utf-8"))["api_maps"],
            "modules": sorted(modules, key=lambda module: natural(module["file"])),
            "deps": json.loads(deps.read_text(encoding="utf-8")) if deps.is_file() else None}


def blob(source: dict, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{source['repo']}/blob/{source['rev']}/{path}" + (f"#L{line}" if line else "")


def tree(source: dict, path: str = "") -> str:
    return f"{GITHUB}/{source['repo']}/tree/{source['rev']}" + (f"/{path}" if path else "")


def at(source: dict) -> str:
    return f"[{source['rev'][:8]}]({tree(source)})"


def credit(source: dict) -> str:
    return (f"The docstrings, Lean statements and API maps are quoted from [{source['repo']}]({GITHUB}/{source['repo']}) "
            f"at commit {at(source)}, under its Apache-2.0 license.")


def without_plans(text: str) -> str:
    """A description without its clauses on what is planned or under way, the cut marked with …."""
    clauses = re.split(r"(?<=[.;])\s+", " ".join(text.split()))
    kept = [clause for clause in clauses if not PLANS.search(clause)]
    return " ".join(kept) + (" …" if len(kept) < len(clauses) else "")


def without_todos(markdown: str) -> str:
    """Quoted Markdown without what mentions a TODO item: each list item that does, or else the paragraph, the cut
    marked with …. The map records what the library has, not what it plans."""
    out = []
    for block in re.split(r"\n[ \t]*\n", markdown.strip()):
        if not TODO.search(block):
            out.append(block)
            continue
        items: list[list[str]] = []
        for line in block.split("\n"):
            if LIST_ITEM.match(line) or not items:
                items.append([line])
            else:
                items[-1].append(line)
        if len(items) > 1 and all(LIST_ITEM.match(item[0]) for item in items):
            kept = [line for item in items if not TODO.search("\n".join(item)) for line in item]
            out.append("\n".join(kept) + "\n\n…" if kept else "…")
        else:
            out.append("…")
    return re.sub(r"…(?:\n\n…)+", "…", "\n\n".join(out)).strip()


def shown(text: str) -> bool:
    return bool(text) and text != "…"


def quoted_prose(markdown: str, here: str = "", source: dict | None = None, keys: dict[str, str] | None = None) -> str:
    """Prose of the module at *here*, quoted: escaped as literal() escapes it, its inline links kept whole, so an
    underscore in a link's target stays one. A link to one of the repository's files, written relative to the
    module, points at the article of that module here, or else at the file at the pinned commit; a link out of the
    repository is left for quote() to make text."""
    links: list[str] = []
    folder = here.rsplit("/", 1)[0]
    opaque = [match.span() for match in OPAQUE.finditer(markdown)]

    def keep(match: re.Match) -> str:
        label, target = match.groups()
        if any(start <= match.start() < end for start, end in opaque):
            return match.group()
        if not SCHEME.match(target):
            if source is None:
                return match.group()
            path = target.split("#")[0]
            path = posixpath.normpath(path.lstrip("/") if path.startswith("/") else posixpath.join(folder, path))
            if path == ".." or path.startswith("../"):
                return match.group()
            target = f"trough:{keys[path]}" if keys and path in keys else blob(source, path)
        links.append(f"[{literal(label)}]({target})")
        return f"\x00{len(links) - 1}\x00"

    text = literal(INLINE_LINK.sub(keep, markdown))
    return quote(re.sub(r"\x00(\d+)\x00", lambda match: links[int(match.group(1))], text))


def doc_markdown(text: str, quoted=quoted_prose) -> list[str]:
    """A docstring as an article shows it: its headings as the article's, from `##` down, and its prose quoted. A
    table of contents, which the article's own headings give, is left out, and so is a section headed by a TODO and
    what else mentions a TODO item, each such cut marked with …."""
    parts: list[str] = []
    prose: list[str] = []
    skipping, fenced = 0, False

    def flush() -> None:
        kept = without_todos("\n".join(prose))
        if kept:
            parts.append(quoted(kept))
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
        skipping = level if "table of contents" in words.casefold() or TODO.search(words) else 0
        if TODO.search(words):
            parts.append("…")
        elif not skipping:
            parts.append("#" * min(max(level, 2), 6) + " " + comment(words))
    flush()
    return parts


def significant(source: dict) -> set[str]:
    """The names Theorems.txt lists, in any library's section."""
    return {name for names in source["theorems"].values() for name in names}


def declaration_block(declaration: dict, module: dict, source: dict, listed: set[str], keys: dict[str, str]) -> str:
    """A declaration's block: its name, kind and line, whether Theorems.txt lists it, its docstring and its Lean
    statement."""
    where = f"[line {declaration['line']}]({blob(source, module['file'], declaration['line'])})"
    if declaration["name"]:
        kind = declaration["kind"]
        head = f"**`{declaration['name']}`**, {'an' if kind[0] in 'aeiou' else 'a'} {kind}, {where}."
    else:
        head = f"**An instance with no name**, {where}."
    if declaration["name"] in listed:
        head += f" Listed as a significant result in [{THEOREMS.rsplit('/', 1)[-1]}]({blob(source, THEOREMS)})."
    if declaration["sorry"]:
        head += " Its value contains `sorry`."
    parts = [head]
    doc = without_todos(declaration["doc"])
    if shown(doc):
        parts.append(quoted_prose(doc, module["file"], source, keys))
    parts.append(fence(declaration["statement"]))
    return "\n\n".join(parts)


def lean_names(module: dict, listed: set[str]) -> list[str]:
    """The names a card's Lean row shows: the significant results first, then the others in file order."""
    names = [declaration["name"] for declaration in module["declarations"] if declaration["name"]]
    return ([name for name in names if name in listed] + [name for name in names if name not in listed])[:LEAN_NAMES]


def article(module: dict, source: dict, listed: set[str], links: dict[str, str], slug: str,
            keys: dict[str, str]) -> Leaf:
    """A module's article: where it is, its module docstring, then its declarations in file order under its own
    section headings."""
    declarations = module["declarations"]
    anonymous = sum(not declaration["name"] for declaration in declarations)
    named = sum(declaration["name"] in listed for declaration in declarations)
    documented = sum(bool(declaration["doc"]) for declaration in declarations)
    opening = (f"The module `{module['module']}`, [{module['file']}]({blob(source, module['file'])}): "
               f"{plural(len(declarations), 'declaration')}"
               + (f" ({plural(anonymous, 'instance')} with no name)" if anonymous else "")
               + f", {documented:,} with a docstring"
               + (f", {named:,} listed as significant" if named else "")
               + (f"; {module['private']:,} private, not shown" if module["private"] else "") + ".")
    def quoted(text: str) -> str:
        return quoted_prose(text, module["file"], source, keys)

    parts = [opening, *doc_markdown(module["doc"], quoted)]
    index = 0
    for section in module["sections"]:
        before = [declaration for declaration in declarations[index:] if declaration["line"] < section["line"]]
        parts += [declaration_block(declaration, module, source, listed, keys) for declaration in before]
        index += len(before)
        parts += doc_markdown(section["text"], quoted)
    parts += [declaration_block(declaration, module, source, listed, keys) for declaration in declarations[index:]]
    names = lean_names(module, listed)
    fields = [("declaration", "module"), ("origin", "cited")]
    if names:
        fields += [("lean", ", ".join(names)), ("statement", "formalized")]
        if not any(declaration["sorry"] for declaration in declarations):
            fields.append(("proof", "formalized"))
    lines = {declaration["name"]: declaration["line"] for declaration in declarations}
    for name in names:
        links[name] = blob(source, module["file"], lines[name])
    leaf = Leaf(comment(module["title"]) if module["title"] else escape(module["module"]), slug, fields,
                "\n\n".join(parts), no_depends=NO_DEPENDS)
    leaf.sources = [(f"{module['file']} at {source['rev'][:8]}", blob(source, module["file"]))]
    return leaf


def api_map_prose(api_map: dict, source: dict, keys: dict[str, str], pages: set[str] = frozenset()) -> str:
    """An API map's content as a page quotes it: each sentence the map marks [TODO] left out, the cut marked with …,
    and a heading whose paragraphs all go left out with them; a Lean citation [n] links the article of the module the
    map's n-th Lean reference names; its literature references listed after it, one naming another API map whose
    folder has a page linked to that page."""

    def cite(match: re.Match) -> str:
        entry = api_map["lean"].get(match.group(1))
        key = keys.get(entry["file"]) if entry else None
        return f"[\\[{match.group(1)}\\]](trough:{key})" if key else f"\\[{match.group(1)}\\]"

    out = []
    for section in api_map["content"]:
        blocks: list[tuple[str, str]] = []
        for block in re.split(r"\n[ \t]*\n", section["text"]):
            if match := HEADING.match(block.strip()):
                blocks.append(("heading", "#" * max(len(match.group(1)), 3) + " " + comment(match.group(2))))
                continue
            pieces = CITATIONS.split(" ".join(block.split()))
            units = [pieces[index] + (pieces[index + 1] if index + 1 < len(pieces) else "")
                     for index in range(0, len(pieces), 2)]
            kept: list[str] = []
            for unit in units:
                if "[TODO]" in unit:
                    if kept and kept[-1] != "…":
                        kept.append("…")
                    elif not kept:
                        kept.append("…")
                elif unit.strip():
                    kept.append(unit.strip())
            if any(unit != "…" for unit in kept):
                blocks.append(("text", " ".join(kept)))
        blocks = [block for index, block in enumerate(blocks)
                  if block[0] == "text" or (index + 1 < len(blocks) and blocks[index + 1][0] == "text")]
        if blocks:
            text = "\n\n".join(block if kind == "heading" else LEAN_CITATION.sub(cite, literal(block))
                               for kind, block in blocks)
            out.append(f"*{escape(section['heading'])}*\n\n" + quote(text))
    if not out:
        return ""
    lines = [f"The repository's API map for this folder, *{escape(api_map['title'])}* "
             f"([{api_map['file']}]({blob(source, api_map['file'])})), with the sentences it marks as not yet "
             "formalized left out (…). A citation \\[n\\] links the module its n-th Lean reference names.", *out]
    def reference(text: str) -> str:
        named = API_MAP_PATH.search(text)
        if named and named.group(1) in pages:
            return f"{literal(text[:named.start()])}[{literal(named.group())}](trough:physlib-folder-{named.group(1)})"
        return literal(text)

    if api_map["references"]:
        lines.append("Its references:\n\n" + quote("\n".join(
            f"- \\{{{number}\\}} {reference(text)}"
            for number, text in sorted(api_map["references"].items(), key=lambda item: int(item[0])))))
    return "\n\n".join(lines)


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


def edges(deps: dict, articles: set[str]) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Each module's nearest dependencies among the modules with an article: those its statements use, without one
    reached through another's statements, and those only its proofs use, without one reached through any other.
    A module without an article is passed through, its uses taken as the module's own."""
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
            out[module] = sorted(found - {module}, key=natural)
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


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and the links of the names its cards' Lean rows show (for
    hooks/lean-links.json). A part per library, a page per area and per folder below it, an article per module."""
    source, deps = data["source"], data["deps"]
    if deps and deps["rev"] != source["rev"]:
        raise ValueError(f"data/physlib/deps.json reads {deps['rev'][:8]}, but source.json pins {source['rev'][:8]}")
    missing = set(deps["missing"]) if deps else set()
    listed = significant(source)
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    modules = []
    for module in data["modules"]:
        kept = [declaration for declaration in module["declarations"] if declaration["name"] not in missing]
        stats["unresolved"] += len(module["declarations"]) - len(kept)
        if kept:
            modules.append({**module, "declarations": kept})
        else:
            stats["unshown"] += 1

    # A page per area, per folder below it, and per deeper folder with an API map; the modules of other deeper folders
    # join the nearest page above, under a line naming their folder.
    maps = {api_map["folder"]: api_map for api_map in data["api_maps"]}
    pages: set[str] = set()
    for module in modules:
        folder = module["file"].rsplit("/", 1)[0]
        parts = folder.split("/")
        pages.update("/".join(parts[:depth]) for depth in range(2, min(len(parts), 3) + 1))
        while "/" in folder:
            if folder in maps:
                pages.add(folder)
            folder = folder.rsplit("/", 1)[0]

    def page_of(path: str) -> str:
        folder = path.rsplit("/", 1)[0]
        while folder not in pages and "/" in folder:
            folder = folder.rsplit("/", 1)[0]
        return folder

    def order(module: dict) -> list:
        # Basic.lean holds a folder's basic results, as the handbook says, so it comes first in its folder.
        directory, name = module["file"].rsplit("/", 1)
        return [natural(directory), name != "Basic.lean", natural(name)]

    articles: dict[str, Leaf] = {}
    keys = {module["file"]: f"physlib-{module['module']}" for module in modules}  # each article's key, by file
    placed: dict[str, list[dict]] = defaultdict(list)  # the modules on each page, or directly in a library's part
    for module in sorted(modules, key=order):
        home = page_of(module["file"])
        placed[home].append(module)
        slug = slugify(module["file"][len(home) + 1:].removesuffix(".lean").replace("/", " "))
        leaf = article(module, source, listed, links, slug, keys)
        articles[module["module"]] = leaf
        targets[keys[module["file"]]] = leaf
        library = module["file"].split("/")[0]
        stats["articles"] += 1
        stats[f"articles {library}"] += 1
        stats["declarations"] += len(module["declarations"])
        stats["instances"] += sum(not declaration["name"] for declaration in module["declarations"])
        stats["documented"] += sum(bool(declaration["doc"]) for declaration in module["declarations"])
        stats["significant"] += sum(declaration["name"] in listed for declaration in module["declarations"])
        stats["sorry"] += sum(declaration["sorry"] for declaration in module["declarations"])
        stats["private"] += module["private"]
    if deps:
        statement, proof = edges(deps, set(articles))
        for module, leaf in articles.items():
            leaf.depends = [articles[target] for target in statement[module]]
            leaf.proof_depends = [articles[target] for target in proof[module]]
            stats["statement_edges"] += len(leaf.depends)
            stats["proof_edges"] += len(leaf.proof_depends)
    else:
        for leaf in articles.values():
            leaf.no_depends = NO_DEPENDS_UNREAD

    containers: dict[str, Container] = {}
    for folder in sorted(pages, key=natural):
        containers[folder] = page = Container(escape(folder.rsplit("/", 1)[-1]), slugify(folder.rsplit("/", 1)[-1]))
        targets[f"physlib-folder-{folder}"] = page
    # Deepest first, so that a page's count includes the pages below it.
    totals: Counter = Counter()
    for folder in sorted(containers, key=lambda folder: -folder.count("/")):
        page = containers[folder]
        here, current = placed.get(folder, []), folder
        for module in here:
            directory = module["file"].rsplit("/", 1)[0]
            before = ""
            if directory != current:
                before = f"Modules in [{directory[len(folder) + 1:]}/]({tree(source, directory)}):"
                current = directory
            page.entries.append(Entry(articles[module["module"]], before=before))
        below = sorted((other for other in containers if other.rsplit("/", 1)[0] == folder), key=natural)
        page.entries += [Entry(containers[other]) for other in below]
        totals[folder] += len(here) + sum(totals[other] for other in below)
        prose = [f"The folder [{folder}/]({tree(source, folder)}): "
                 + (f"{plural(len(here), 'module')}, an article each, in path order with Basic.lean first in its folder"
                    if here else "")
                 + ("; then " if here and below else "")
                 + (f"{plural(len(below), 'folder')} below it, a page each" if below else "")
                 + (f", {totals[folder]:,} modules in all." if below and totals[folder] > len(here) else ".")]
        if folder in maps and (text := api_map_prose(maps[folder], source, keys, set(containers))):
            prose.append(text)
        page.prose = "\n\n".join(prose)
    for folder in sorted(containers, key=natural):
        chunk(containers[folder], budget=PAGE_BUDGET)

    parts = []
    readme = source["readme"]
    for library in LIBRARIES:
        entries = [Entry(articles[module["module"]]) for module in placed.get(library, [])]
        entries += [Entry(containers[folder]) for folder in sorted(containers, key=natural)
                    if folder.rsplit("/", 1)[0] == library]
        if not entries:
            continue
        part = Container(library, slugify(library), entries)
        where = f"[{library}/]({tree(source, library)})"
        described = quote(literal(without_plans(readme["libraries"][library])))
        words = {
            "Physlib": [f"The repository's core library, {where}. Its README describes it:", described],
            "PhyslibAlpha": [f"{where}, downstream of Physlib in the same repository. Its README describes it:", described,
                             "and gives its review in a section of its own:",
                             quote("\n\n".join(literal(paragraph) for paragraph in readme["alpha"]))],
            "QuantumInfo": [f"{where}, a build target of its own in the repository. Its README describes it:", described],
        }[library]
        part.prose = "\n\n".join([
            *words,
            f"Its {plural(stats[f'articles {library}'], 'module')} with a declaration are mapped here, an article each, "
            "on a page per area and per folder below it.",
            credit(source)])
        chunk(part)
        targets[f"physlib-{library}"] = part
        parts.append(Entry(part))
        stats["parts"] += 1
    stats["pages"] = len(containers)
    root = Container(TITLE, "physlib", parts)
    root.prose = intro(data, stats)
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items()))


def intro(data: dict, stats: Counter) -> str:
    source, deps = data["source"], data["deps"]
    readme = source["readme"]
    sizes = listing([f"{stats[f'articles {library}']:,} in [{library}](trough:physlib-{library})"
                     for library in LIBRARIES if stats[f"articles {library}"]])
    if deps:
        reading = (
            "The dependencies come from Lean. The data workflow fetches the repository's build cache with Mathlib's, "
            "imports every module of the three libraries, and reads which other modules' declarations each module's "
            "declarations use: in a statement, which here takes in a definition's value and a structure's fields, or "
            "in a proof. An article depends on the modules whose declarations its statements use (“Statement uses” on "
            "the site), and its proof depends on those that only its proofs use; a dependency already reached through "
            f"another is left out. That gives {plural(stats['statement_edges'], 'statement edge')} and "
            f"{plural(stats['proof_edges'], 'proof edge')}. An edge says that some declaration of one module uses some "
            "declaration of the other, not which one. The same reading checks the names read from the source: a "
            "declaration whose name Lean does not have, such as one private to its module, is left out"
            + (f", {plural(stats['unresolved'], 'declaration')} at this commit." if stats["unresolved"] else
               ", and none is at this commit."))
    else:
        reading = "No dependencies are recorded here: they come from Lean's reading of the modules, which the data lack."
    unshown = stats["unshown"]
    return "\n\n".join(part for part in [
        f"[Physlib]({GITHUB}/{source['repo']}) is, in its README's words, “{literal(readme['tagline'])}”. "
        + (f"The README adds: “{literal(readme['formed'])}” " if readme.get("formed") else "")
        + "The repository holds three libraries, as the README presents them: Physlib, the core library; PhyslibAlpha, "
        "downstream of it under a lighter review; and QuantumInfo, quantum information theory in a codebase of its "
        f"own. The README names the project's maintainers: {listing(readme['maintainers'])}.",
        f"- Repository: [{source['repo']}]({GITHUB}/{source['repo']}), read at commit {at(source)} "
        f"({source['date'][:10]}), the newest commit of its `master` branch whose build passed.\n"
        f"- Lean toolchain {source['toolchain']}, Mathlib "
        + (f"{source['mathlib_version']}, " if source.get("mathlib_version") else "")
        + f"[{source['mathlib'][:8]}]({MATHLIB_REPO}/tree/{source['mathlib']}).\n"
        f"- License: {source['license']}.",
        f"The repository's handbook asks that a file be organized around a single definition and named after it, so "
        f"the map has an article per module with a declaration: {plural(stats['articles'], 'article')}, {sizes}. A part "
        f"per library has a page per area, per folder below it and per deeper folder with an API map, "
        f"{plural(stats['pages'], 'folder page')} in all; a module in another deeper folder is on the page of the "
        "nearest folder above, under a line naming its folder.",
        f"An article quotes the module's docstring and its section docstrings, their headings shown as the article's "
        f"and a table of contents left out, and shows each declaration in file order: its name, kind and line, its "
        f"docstring and its Lean statement (the text up to the `:=` or `where` that starts its value, or the whole text "
        f"of a structure, class or inductive type). The articles "
        f"hold {plural(stats['declarations'], 'declaration')}, {stats['instances']:,} of them instances with no name, "
        f"and {stats['documented']:,} have a docstring"
        + (f"; {plural(stats['private'], 'private declaration')} {'is' if stats['private'] == 1 else 'are'} counted on "
           "the articles, not shown" if stats["private"] else "") + ". The "
        f"repository keeps the keyword `theorem` for the significant results its [{THEOREMS}]({blob(source, THEOREMS)}) "
        f"lists, “usually one known by name”: {stats['significant']:,} of the declarations here are among them, and "
        "their blocks say so and lead their cards' Lean rows. "
        + ("No declaration's value read here contains `sorry`." if not stats["sorry"] else
           f"{plural(stats['sorry'], 'declaration')} {'has' if stats['sorry'] == 1 else 'have'} a value that contains "
           "`sorry`; each block says so."),
        "The API maps, the repository's own accounts of an area with citations of the declarations that formalize it, "
        "are quoted on the pages of their folders, without the sentences they mark as not yet formalized. Informal "
        "results (`informal_lemma`, `informal_definition`, `semiformal_result`) and TODO items are not mapped, and the "
        "parts of a docstring that mention a TODO item are left out, each cut marked with …: the map records what the "
        "library has, not what it plans."
        + (f" {plural(unshown, 'module')} {'holds' if unshown == 1 else 'hold'} nothing else, only such text or "
           f"private declarations, and {'has' if unshown == 1 else 'have'} no article." if unshown else ""),
        "The text is read from the source without Lean, by the reading trough uses for other libraries: a "
        "declaration's name is read under the namespaces it sits in, and its line is the line its keyword is on. "
        + reading,
        credit(source),
    ] if part)


def listing(parts: list[str]) -> str:
    return ", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else "".join(parts)
