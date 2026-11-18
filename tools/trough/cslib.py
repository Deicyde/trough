"""The CSLib chapter: the Lean Computer Science Library, a module per article.

leanprover/cslib organizes its Lean in folders under Cslib/, one area each (Foundations, Computability,
Languages, Logics, Algorithms, Crypto and smaller ones), and documents each module the way Mathlib does: a module
docstring with a `#` title, its main definitions and statements, and a docstring on each definition.
tools/refresh_cslib.py reads a checkout at a pinned commit into data/cslib/ without Lean: each module's title,
docstrings, the authors its header names and its public declarations, as trough.leansource reads them, with the
area READMEs' descriptions. lean/cslib/CslibDeps.lean then reads, with Lean, the modules each module's statements
and proofs use, and which of those names Lean has only as private declarations: in a `module` file, a declaration
outside a `public section` and not marked `public` is private, which the source reading does not follow. The chapter
has a part per area, a page per folder and an article per module, with a block per public declaration in file order.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from . import leansource
from .blueprints import Built, escape
from .ff import is_apache
from .formal_conjectures import OPAQUE, module_name, quote
from .mathlib import fence
from .vault import Container, Entry, Leaf, chunk, slugify

SCHEMA = "trough-cslib/v1"
REPO = "leanprover/cslib"
GITHUB = "https://github.com"
LIBRARY = "Cslib"
# A header's copyright holders and its optional list of authors, which AUTHORS.md says name a file's authors.
COPYRIGHT = re.compile(r"^Copyright \(c\) \d{4}(?:[-–]\d{4})? (?P<holders>.+?)\.? All rights reserved\.?$", re.M)
AUTHORS = re.compile(r"^Authors?:[ \t]*(?P<authors>.+(?:\n(?![A-Z][a-z]+:)[ \t]*\S.*)*)", re.M)
# A section of a README or docstring that says what the library plans, not what it has.
PLANS = re.compile(r"^(?:plans?|future work|todos?|roadmap)\b", re.I)
PLANNED = re.compile(r"\b(?:plan(?:s|ned)?|placeholder|upstream(?:ing)?)\b", re.I)
HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
TODO = re.compile(r"\bTODO\b")
CODE_SPAN = re.compile(r"`[^`\n]*`")
# A line that starts a list item, which ends the paragraph a TODO cut runs to.
LIST_ITEM = re.compile(r"^[ \t]*(?:[-*+]|\d+[.)])[ \t]")
# A sentence that plans or invites future work, and a paragraph about moving code elsewhere; kept narrow, as words such
# as "in the future" or "not yet" also describe what a module has (BTL's temporal modalities).
PLAN_SENTENCE = re.compile(r"would be welcome|\bwe plan\b|reserved for future work|future work on|future design work|"
                           r"\bwill follow\b", re.I)
UPSTREAMING = re.compile(r"should be upstreamed", re.I)
# Where a sentence ends: after its full stop, or before a list item, so that a list whose items have no full stops is
# not one sentence.
SENTENCE = re.compile(r"(?<=[.!?])\s+|\n(?=[ \t]*(?:[-*+]|\d+[.)])[ \t])")
CUT = "\x00"  # where without_plans() cut, until it writes …
# Definitions whose whole text is shown: their fields or constructors say what they are.
WHOLE = ("structure", "class", "inductive")


def without_plans(markdown: str) -> str:
    """The Markdown without what it says of plans and TODOs, each cut marked with …: a section headed plans, future
    work, TODO(s) or roadmap, up to the next heading of its level or above; a TODO, from where it stands to the end of
    its paragraph (a blank line, a heading or the next list item); a sentence or list item that plans or invites future
    work, with the list it introduces when it ends in a colon; a paragraph saying code should be upstreamed; and a
    heading left with nothing but cuts under it."""
    out: list[str] = []
    skipping: int | None = None
    cutting = fence = False
    for line in markdown.split("\n"):
        is_fence = line.lstrip().startswith(("```", "~~~"))
        if is_fence:
            fence = not fence
        heading = None if fence or is_fence else HEADING.match(line)
        if heading and skipping is not None and len(heading.group(1)) <= skipping:
            skipping = None
        if skipping is not None:
            continue
        if cutting and (not line.strip() or heading or is_fence or LIST_ITEM.match(line)):
            cutting = False
        if cutting:
            continue
        if heading and PLANS.match(heading.group(2).strip("*_ ")):
            skipping = len(heading.group(1))
            out.append(CUT)
            continue
        todo = None if fence or is_fence else next(
            (match for match in TODO.finditer(line)
             if not any(span.start() < match.start() < span.end() for span in CODE_SPAN.finditer(line))), None)
        if todo:
            before = line[:todo.start()].rstrip()
            out.append(f"{before} {CUT}" if before and not LIST_ITEM.match(before + " ") else CUT)
            cutting = True
            continue
        out.append(line)
    paragraphs = re.split(r"(\n[ \t]*\n)", "\n".join(out))
    fence = False
    for index in range(0, len(paragraphs), 2):
        paragraph = paragraphs[index]
        inside = fence or paragraph.lstrip().startswith(("```", "~~~"))
        fence ^= paragraph.count("```") % 2 == 1
        if inside or HEADING.match(paragraph.strip()):
            continue
        if UPSTREAMING.search(paragraph):
            paragraphs[index] = CUT
        elif PLAN_SENTENCE.search(paragraph):
            pieces = SENTENCE.split(paragraph)
            separators = SENTENCE.findall(paragraph)
            kept, lead_in = [], False
            for piece in pieces:
                # A cut lead-in, a sentence ending in a colon, takes the list it introduces with it.
                if lead_in or PLAN_SENTENCE.search(piece):
                    kept.append(CUT)
                    lead_in = lead_in or (not LIST_ITEM.match(piece) and piece.rstrip().endswith(":"))
                else:
                    kept.append(piece)
            paragraphs[index] = "".join(piece + (separators[number] if number < len(separators) else "")
                                        for number, piece in enumerate(kept))
    text = drop_empty_headings("".join(paragraphs))
    # Consecutive cuts are one.
    return re.sub(rf"{CUT}(?:\s*{CUT})+", CUT, text).strip().replace(CUT, "…")


def drop_empty_headings(text: str) -> str:
    """The text without a heading whose section, up to the next heading of its level or above, holds only cuts."""
    lines = text.split("\n")
    kept: list[str] = []
    dropped = False
    for index, line in enumerate(lines):
        if dropped and not line.strip():
            continue
        dropped = False
        heading = HEADING.match(line)
        if heading:
            section = []
            for later in lines[index + 1:]:
                inner = HEADING.match(later)
                if inner and len(inner.group(1)) <= len(heading.group(1)):
                    break
                if not inner:
                    section.append(later)
            if CUT in "".join(section) and not "".join(section).replace(CUT, "").strip():
                dropped = True
                continue
        kept.append(line)
    return "\n".join(kept)


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


def read_module(text: str, path: str) -> dict:
    """A module's record: its title, docstrings and public declarations in file order; `items` is None when its
    scopes don't close as they open. The module docstring is the first `/-! ... -/` before any declaration; each
    later one is an item of its own, where the file writes it."""
    found = leansource.declarations(text, relaxed=True)
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
                     "doc": without_plans(declaration.doc), "statement": statement_of(text, declaration),
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
    section, without its aims, which say what the library means to offer; a paragraph "…" stands for the heading
    between them."""
    sections = re.split(r"^# ", readme, flags=re.M)
    kept = []
    for index, section in enumerate(sections[1:]):
        title, _, body = section.partition("\n")
        if index == 0 or title.strip().lower().startswith("what"):
            body = re.split(r"^##? ", body, maxsplit=1, flags=re.M)[0]
            kept += (["…"] if index else []) + [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
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
            if text := readme_text((checkout / path).read_text(encoding="utf-8")):
                folders[folder] = text
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
    """data/cslib/'s source and library, when both are there, with the Lean dump's edges when they are of the same
    commit."""
    source, library, deps = (data / "cslib" / name for name in ("source.json", "library.json", "deps.json"))
    if not (source.is_file() and library.is_file()):
        return None
    loaded = json.loads(source.read_text(encoding="utf-8")) | json.loads(library.read_text(encoding="utf-8"))
    dump = json.loads(deps.read_text(encoding="utf-8")) if deps.is_file() else None
    return loaded | {"deps": dump if dump and dump.get("rev") == loaded["rev"] else None}


# The chapter, from the data.

TITLE = "CSLib: the Lean Computer Science Library"
# The bytes of article Markdown a folder's page folds in before its next article starts a page.
PAGE_BUDGET = 200_000
KIND_WORDS = {"theorem": "theorem", "lemma": "lemma", "def": "definition", "abbrev": "abbreviation",
              "instance": "instance", "structure": "structure", "class": "class", "inductive": "inductive type",
              "opaque": "opaque constant", "axiom": "axiom", "alias": "alias"}


def blob(rev: str, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{REPO}/blob/{rev}/{path}" + (f"#L{line}" if line else "")


def at(rev: str) -> str:
    return f"[{rev[:8]}]({GITHUB}/{REPO}/tree/{rev})"


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


def block(item: dict, file: str, rev: str) -> str:
    """A declaration's name, kind and line, its docstring and its Lean statement; or a note the module writes there."""
    if "note" in item:
        return quote(item["note"])
    where = f"[line {item['line']}]({blob(rev, file, item['line'])})"
    head = f"`{item['name']}` ({KIND_WORDS.get(item['kind'], item['kind'])}, {where})"
    if item["sorry"]:
        head += ". Its value holds `sorry`."
    return "\n\n".join([head] + ([quote(item["doc"])] if item["doc"] else []) + [fence(item["statement"])])


def article(module: dict, title: str, rev: str, links: dict[str, str]) -> Leaf:
    """A module's article: where it is and who wrote it, its docstring, and a block per public declaration and per
    later note, in file order."""
    names = [item["name"] for item in declarations(module)]
    authors = module["authors"] or module["copyright"]
    opening = f"`{module['module']}`, in [{module['file']}]({blob(rev, module['file'])})" + (f", by {authors}." if authors else ".")
    if not names:
        opening += " It declares nothing public by name."
    parts = [opening] + ([quote(module["doc"])] if module["doc"] else [])
    parts += [block(item, module["file"], rev) for item in module["items"]]
    fields = [("catalog", "module")]
    if names:
        fields += [("lean", ", ".join(names)), ("statement", "formalized")]
        if not any(item["sorry"] for item in declarations(module)):
            fields.append(("proof", "formalized"))
    for item in declarations(module):
        links.setdefault(item["name"], blob(rev, module["file"], item["line"]))
    leaf = Leaf(title_text(title), slugify(stem(module)), fields, "\n\n".join(parts))
    leaf.sources = [(f"{module['file']} at {rev[:8]}", blob(rev, module["file"]))]
    return leaf


def tree(modules: list[dict]) -> dict:
    """The folders under Cslib/ as nested {"modules", "folders"}, by name."""
    root: dict = {"modules": [], "folders": {}}
    for module in modules:
        node = root
        for part in module["file"].split("/")[1:-1]:
            node = node["folders"].setdefault(part, {"modules": [], "folders": {}})
        node["modules"].append(module)
    return root


def every(node: dict) -> list[dict]:
    return node["modules"] + [module for child in node["folders"].values() for module in every(child)]


def credit(rev: str) -> str:
    return (f"The docstrings, Lean statements and README text are quoted from [{REPO}]({GITHUB}/{REPO}) at commit "
            f"{at(rev)}, under its Apache-2.0 license.")


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and each declaration's source line (for
    hooks/lean-links.json). A part per area, a page per folder below it and an article per module."""
    rev, deps = data["rev"], data.get("deps")
    stats: Counter = Counter()
    # Lean decides which of the names read from the source are public: one private to its module, or one Lean does not
    # have, is left out.
    private, missing = (set(deps.get("private", [])), set(deps.get("missing", []))) if deps else (set(), set())
    modules = []
    for module in data["modules"]:
        stats["private"] += sum(item.get("name") in private for item in module["items"])
        stats["unresolved"] += sum(item.get("name") in missing for item in module["items"])
        modules.append({**module, "items": [item for item in module["items"]
                                            if item.get("name") not in private | missing or "name" not in item]})
    named = titles(modules)
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    leaves: dict[str, Leaf] = {}

    def build(name: str, node: dict, path: str, part: bool) -> Container:
        entries = []
        # By name, as Cslib.lean imports them, a module before the folder of the same name.
        children = sorted([(stem(module), 0, module) for module in node["modules"]]
                          + [(folder, 1, child) for folder, child in node["folders"].items()], key=lambda row: row[:2])
        for child_name, is_folder, child in children:
            if is_folder:
                entries.append(Entry(build(child_name, child, f"{path}/{child_name}", False)))
            else:
                leaf = article(child, named[child["module"]], rev, links)
                leaves[child["module"]] = leaf
                targets[f"cslib-{child['module']}"] = leaf
                stats["articles"] += 1
                entries.append(Entry(leaf))
        container = Container(escape(name), slugify(name), entries)
        inside = every(node)
        tally = counts(inside)
        held = (f", with {plural(tally['declarations'], 'public declaration')}." if tally["declarations"] else
                ", none of which declares anything public by name." if len(inside) > 1 else
                ", which declares nothing public by name.")
        lines = [f"{plural(len(inside), 'module')} under `{path}/`{held}"]
        if path in data["folders"]:
            lines.append(f"Its [README]({blob(rev, path + '/README.md')}) opens:\n\n{quote(data['folders'][path])}")
        if part:
            lines.append(credit(rev))
        container.prose = "\n\n".join(lines)
        targets[f"cslib-{path}"] = container
        stats["folders"] += 1
        return chunk(container, budget=PAGE_BUDGET)

    top = tree(modules)
    parts = [Entry(build(name, child, f"{LIBRARY}/{name}", True)) for name, child in sorted(top["folders"].items())]
    stats["parts"] = len(parts)
    for module in top["modules"]:
        leaf = article(module, named[module["module"]], rev, links)
        leaves[module["module"]] = leaf
        targets[f"cslib-{module['module']}"] = leaf
        stats["articles"] += 1
        parts.append(Entry(leaf))
    edges(data, leaves, stats)
    stats.update(counts(modules))
    stats["empty"] = sum(1 for module in modules if not declarations(module))
    root = Container(TITLE, "cslib", parts)
    root.prose = intro(data, stats)
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items()))


def edges(data: dict, leaves: dict[str, Leaf], stats: Counter) -> None:
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
        # Modules import one another without cycles, so a depth-first walk ends; each set is its node's closure.
        stack = [(module, False)]
        while stack:
            node, done = stack.pop()
            if node in reach_all:
                continue
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
            leaf.no_depends = "Its statements use no other CSLib module's declarations."
        else:
            leaf.no_depends = "The Lean dump has no record of this module, so its dependencies are unknown."
            stats["unrecorded"] += 1
        stats["statement_edges"] += len(leaf.depends)
        stats["proof_edges"] += len(leaf.proof_depends)


def intro(data: dict, stats: Counter) -> str:
    rev = data["rev"]
    roles = [f"{listing(role['names'])} as {role['role'][0].lower() + role['role'][1:]}" for role in data["maintainers"]]
    theorems = stats["theorem"] + stats["lemma"]
    definitions = sum(stats[kind] for kind in ("def", "abbrev", "structure", "class", "inductive", "opaque"))
    others = stats["declarations"] - theorems - definitions
    if data.get("deps"):
        lean = (
            "Edges come from Lean: a GitHub Actions run builds CSLib at this commit and reads, for each module, which "
            "other modules' declarations its own use. “Depends on” lists the modules its statements use, the types of "
            "its declarations and the values of its definitions, and “Proof depends on” those only its proofs use; a "
            f"dependency reached through another is left out. That gives "
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
                "from a Lean run over CSLib at this commit, which the data lack.")
    return "\n\n".join(part for part in [
        f"[{REPO}]({GITHUB}/{REPO}), the Lean Computer Science Library, says in its README:",
        quote("\n\n".join(data["readme"])),
        f"Its GOVERNANCE.md names {listing(roles)}." if roles else "",
        f"This chapter maps CSLib at commit {at(rev)} ({data['date'][:10]}), with Lean toolchain {data['toolchain']} and "
        f"Mathlib {data['mathlib'][:8]}. It has an article for each of the {plural(stats['articles'], 'module')} under "
        f"`{LIBRARY}/`, in a part per folder of `{LIBRARY}/` and a page per folder below. They hold "
        f"{plural(stats['declarations'], 'public declaration')}, "
        + listing([plural(count, word, words) for count, word, words in (
            (theorems, "theorem", None), (definitions, "definition", None),
            (others, "instance or alias", "instances and aliases")) if count])
        + f", {stats['documented']:,} of them with a docstring"
        + (f"; {plural(stats['empty'], 'module declares', 'modules declare')} nothing public by name."
           if stats["empty"] else "."),
        "An article is titled by its module docstring, or by its file name when the docstring has no title; where "
        "modules share a title, each adds the shortest end of its path that tells them apart. It gives the module's "
        "authors as its header names them, its docstrings, and a block per public declaration in file order with its "
        "Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, "
        "class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names "
        "an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future "
        "work; an ellipsis marks each cut."
        + ("" if stats["sorry"] else " No declaration's value holds `sorry`."),
        lean,
        credit(rev),
    ] if part)
