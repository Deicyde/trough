"""The CFSG chapter: Axiom Math's Lean proof of the classification of finite simple groups.

AxiomMath/CFSG states the classification as CFSG.classification_finite_simple_groups in CFSG/Statement.lean,
whose proof applies CFSG.Assembly.classification (CFSG/Assembly/Reduction.lean) to the catalog of simple groups
and to one theorem for each case of the proof's case division, each case a proposition Reduction.lean defines.
Beside it, CFSG/Milestones.lean imports the milestone modules, the major results the authors single out, each
a module directly under CFSG/Milestones/. The code has no docstrings, so the chapter titles its articles by Lean
names. The repository cannot be built in CI (its README says a build takes most of a day with changes to Lake),
so tools/refresh_cfsg.py reads a checkout at a pinned commit into data/cfsg/ without Lean: the top theorem, the
reduction and the case theorems; each milestone module's declarations; the import graph of every Lean file,
from which it records which case and milestone files each such file imports, directly or not, through no other;
and the facts of formalization.yaml. The chapter has a part for the case division and a part for the milestones.
"""

from __future__ import annotations

import json
import re
from collections import Counter, deque
from pathlib import Path

from . import formalization, leansource
from .blueprints import Built, escape
from .ff import facts, facts_of, is_apache
from .formal_conjectures import module_name, quote
from .mathlib import fence
from .vault import Container, Entry, Leaf, chunk, slugify, walk

SCHEMA = "trough-cfsg/v2"
REPO = "AxiomMath/CFSG"
GITHUB = "https://github.com"
TOP_FILE, TOP = "CFSG/Statement.lean", "CFSG.classification_finite_simple_groups"
MILESTONES = "CFSG/Milestones"
MILESTONE_INDEX = "CFSG/Milestones.lean"
# The certificate files, which hold no milestone or case and are imported in bulk: counted, not read.
CERTIFICATES = ("Certificates/", "CFSG/Certificates/")
IMPORT = re.compile(r"^(?:public[ \t]+)?(?:meta[ \t]+)?import[ \t]+(?:all[ \t]+)?(\S+)", re.M)
THEOREM = re.compile(r"^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:(?:private|protected|noncomputable|public)[ \t]+)*(?:theorem|lemma)\b",
                     re.M)
DOTTED = re.compile(r"(?<![\w.'])[A-Za-z_][\w']*(?:\.[A-Za-z_][\w']*)+")
# An explicit hypothesis of the reduction, as `(hlow : LowTwoRankStatement C)`.
BINDER = re.compile(r"\((h[\w']*)\s*:\s*([A-Za-z_][\w'.]*)[^()]*\)")
TAUCETI_NAME = re.compile(r"(?<![\w.'])TauCeti(?:\.[A-Za-z_][\w']*)+")


def stem(path: str) -> str:
    return path.rsplit("/", 1)[-1].removesuffix(".lean")


def milestone_paths(paths: list[str]) -> list[str]:
    """The milestone modules among a commit's files: the .lean files directly under CFSG/Milestones/."""
    return sorted(path for path in paths if path.startswith(MILESTONES + "/") and path.endswith(".lean")
                  and "/" not in path[len(MILESTONES) + 1:])


def declaration_record(declaration: leansource.Declaration) -> dict:
    """What the data keep of a declaration. Its value holds `sorry` when the text after its statement does,
    or, when no `:=` or `where` ends a statement, when any of its text does."""
    sorry = declaration.proof_sorry if declaration.statement is not None else declaration.sorry
    return {"name": declaration.name, "kind": declaration.kind, "line": declaration.line, "doc": declaration.doc,
            "statement": declaration.statement, "sorry": sorry}


def read_milestone(text: str, path: str) -> dict:
    """A milestone module's record: its declarations in file order, None when its scopes don't close, and the
    modules it imports."""
    found = leansource.scan(text)
    return {"module": module_name(path), "file": path, "id": stem(path),
            "imports": IMPORT.findall(leansource.blank(text)),
            "declarations": None if found is None else
            [declaration_record(declaration) for declaration in sorted(found.values(), key=lambda item: item.line)]}


def declaration_text(text: str, line: int) -> str:
    """A declaration's whole text, from its line to the next line that starts a command at column 0."""
    lines = text.split("\n")
    end = line
    while end < len(lines) and (not lines[end].strip() or lines[end][:1].isspace()):
        end += 1
    return "\n".join(lines[line - 1:end]).rstrip()


def value_of(text: str, declaration: leansource.Declaration) -> str:
    """The text of a declaration's value, after the `:=` that ends its statement, with comments blanked."""
    code = leansource.blank(text)
    offset = sum(len(row) + 1 for row in text.split("\n")[:declaration.line - 1])
    start = text.index(declaration.statement, offset) + len(declaration.statement)
    whole = declaration_text(code, declaration.line)
    return code[start:offset + len(whole)].strip().removeprefix(":=").strip()


def arguments(code: str) -> list[str]:
    """A term's function and arguments: its parts separated by spaces outside brackets."""
    parts, depth, current = [], 0, []
    for char in code:
        if char in "([{⟨":
            depth += 1
        elif char in ")]}⟩":
            depth -= 1
        if char.isspace() and depth == 0:
            if current:
                parts.append("".join(current))
                current = []
        else:
            current.append(char)
    return parts + (["".join(current)] if current else [])


def candidates(term: str, namespace: str) -> list[str]:
    """The full names a term may cite: each dotted name in it, under the namespace and as written."""
    return [full for name in DOTTED.findall(term) for full in (f"{namespace}.{name}", name)]


def reduce(reach: dict[str, set[str]]) -> dict[str, list[str]]:
    """The transitive reduction of a reachability relation: each node's targets that it reaches through no other."""
    return {node: sorted(targets - set().union(*(reach[other] for other in targets))) for node, targets in reach.items()}


def closure(start: str, graph: dict[str, list[str]]) -> set[str]:
    seen, queue = {start}, deque([start])
    while queue:
        for target in graph.get(queue.popleft(), []):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def readme_paragraphs(readme: str) -> list[str]:
    """The README's paragraphs between its title and its first section, without its list of links."""
    head = re.split(r"^#{1,2} ", re.sub(r"\A\s*# [^\n]*\n", "", readme), maxsplit=1, flags=re.M)[0]
    return [part.strip() for part in re.split(r"\n\s*\n", head)
            if part.strip() and not re.match(r"^[*-] \[", part.strip())]


def read(checkout: Path, paths: list[str]) -> tuple[dict, list[str]]:
    """The record of a checkout, with the problems that keep it from being written: a license that is not
    Apache-2.0, a file not checked out, a module whose scopes don't close, a top theorem, reduction, case or main
    result not found where it should be."""
    problems = []
    config = formalization.load((checkout / "formalization.yaml").read_text(encoding="utf-8"))
    license_name = formalization.text_of(config.project.get("license"))
    license_file = checkout / "LICENSE"
    if license_name != "Apache-2.0" or not license_file.is_file() or not is_apache(license_file.read_text(encoding="utf-8")):
        problems.append(f"not Apache-2.0 (formalization.yaml says {license_name!r})")
    lean = [path for path in paths if path.endswith(".lean") and not path.startswith(CERTIFICATES)]
    certificates = sum(path.endswith(".lean") and path.startswith(CERTIFICATES) for path in paths)
    missing = [path for path in lean if not (checkout / path).is_file()]
    if missing:
        problems.append(f"not checked out: {missing[0]}" + (f" and {len(missing) - 1:,} other files" if len(missing) > 1 else ""))
    if TOP_FILE not in lean or missing:
        return {}, problems + ([f"{TOP_FILE} is not in the commit"] if TOP_FILE not in lean else [])

    # The top theorem's proof names the reduction, the catalog and a theorem per case; every file is searched for them.
    top_text = (checkout / TOP_FILE).read_text(encoding="utf-8")
    top = (leansource.scan(top_text) or {}).get(TOP)
    if top is None or top.statement is None:
        return {}, problems + [f"{TOP} is not found declared in {TOP_FILE}"]
    namespace = TOP.rsplit(".", 1)[0]
    terms = arguments(value_of(top_text, top))
    wanted = {full for term in terms for full in candidates(term, namespace)}
    last = sorted({name.rsplit(".", 1)[-1] for name in wanted})
    declares = re.compile(rf"\b(?:theorem|lemma|def|abbrev)\s+(?:_root_\.)?(?:[\w'.]+\.)?(?:{'|'.join(map(re.escape, last))})\b")
    found: dict[str, tuple[str, str, leansource.Declaration]] = {}
    graph: dict[str, list[str]] = {}
    folders: dict[str, Counter] = {}
    texts: dict[str, str] = {}
    for path in lean:
        text = (checkout / path).read_text(encoding="utf-8", errors="replace")
        graph[module_name(path)] = IMPORT.findall(text)
        parts = path.split("/")
        folder = "/".join(parts[:2]) if parts[0] == "CFSG" and len(parts) > 2 else parts[0] if len(parts) > 1 else "(top)"
        tally = folders.setdefault(folder, Counter())
        tally["files"] += 1
        tally["theorems"] += len(THEOREM.findall(text))
        tally["documented"] += "/--" in text or "/-!" in text
        if declares.search(text):
            for name, declaration in (leansource.scan(text) or {}).items():
                if name in wanted:
                    found[name] = (path, text, declaration)
        if path.startswith(MILESTONES + "/") or path == MILESTONE_INDEX:
            texts[path] = text
    known = set(graph)
    graph = {module: [target for target in targets if target in known] for module, targets in graph.items()}

    def cited(term: str) -> list[str]:
        return list(dict.fromkeys(name for name in candidates(term, namespace) if name in found))

    function = cited(terms[0]) if terms else []
    if len(function) != 1:
        return {}, problems + [f"{TOP}: its proof does not apply one theorem found in the repository"]
    reduction_file, reduction_text, reduction = found[function[0]]
    hypotheses = BINDER.findall(reduction.statement or "")
    cases_terms = terms[2:2 + len(hypotheses)]
    catalog_names = cited(terms[1]) if len(terms) > 1 else []
    # The reduction is applied to the catalog, a theorem per hypothesis, then the group.
    if len(terms) != len(hypotheses) + 3 or len(catalog_names) != 1:
        return {}, problems + [f"{TOP}: its proof does not give {function[0]} a catalog and {len(hypotheses)} cases"]
    reduction_scan = leansource.scan(reduction_text) or {}
    reduction_namespace = reduction.name.rsplit(".", 1)[0]
    cases = []
    for (hypothesis, kind), term in zip(hypotheses, cases_terms):
        names = [name for name in cited(term) if found[name][2].kind in ("theorem", "lemma")]
        definition = reduction_scan.get(f"{reduction_namespace}.{kind}")
        if len(names) != 1 or definition is None:
            problems.append(f"{TOP}: the case {hypothesis} : {kind} does not cite one theorem, or {kind} is not "
                            f"defined in {reduction_file}")
            continue
        path, _, theorem = found[names[0]]
        cases.append({"hypothesis": hypothesis, "type": kind,
                      "definition": {"name": definition.name, "line": definition.line,
                                     "text": declaration_text(reduction_text, definition.line)},
                      "theorem": {"file": path, "module": module_name(path), **declaration_record(theorem)}})
    catalog_file, catalog_text, catalog = found[catalog_names[0]]

    milestones = []
    for path in milestone_paths(lean):
        record = read_milestone(texts[path], path)
        if record["declarations"] is None:
            problems.append(f"{path}: its scopes do not close as they open")
        milestones.append(record)
    indexed = set(IMPORT.findall(leansource.blank(texts.get(MILESTONE_INDEX, ""))))
    milestone_modules = {record["module"] for record in milestones}
    nodes = milestone_modules | {case["theorem"]["module"] for case in cases}
    # Every case's file imports the catalog's, so an import of that file is no edge, even where a case's theorem is
    # declared beside it.
    catalog_module = module_name(catalog_file)
    reaches = {node: closure(node, graph) - {node} for node in nodes}
    depends = reduce({node: reached & (nodes - {catalog_module}) for node, reached in reaches.items()})
    for case in cases:
        module = case["theorem"]["module"]
        case["reaches"] = sorted(reaches[module] & milestone_modules)
        case["depends"] = depends[module]
    catalog_importers = sum(case["theorem"]["module"] != catalog_module and catalog_module in reaches[case["theorem"]["module"]]
                            for case in cases)
    for record in milestones:
        record["indexed"] = record["module"] in indexed
        record["depends"] = depends[record["module"]]
        record["cases"] = [case["theorem"]["name"] for case in cases if record["module"] in case["reaches"]]
        del record["imports"]

    results = []
    for result in config.main_results:
        name, file = formalization.text_of(result.get("declaration")), str(result.get("file") or "")
        hit = None
        if file in lean:
            hit = (leansource.scan((checkout / file).read_text(encoding="utf-8")) or {}).get(name)
        if hit is None:
            problems.append(f"main result {name} is not found declared in {file}")
            continue
        results.append({"file": file, **declaration_record(hit)})
    readme = checkout / "README.md"
    record = {
        "schema": SCHEMA, "license": license_name, **facts_of(config), "main_results": results,
        "readme": readme_paragraphs(readme.read_text(encoding="utf-8")) if readme.is_file() else [],
        "top": {"file": TOP_FILE, **declaration_record(top), "reduction": reduction.name,
                "catalog": {"name": catalog.name, "file": catalog_file, "line": catalog.line,
                            "text": declaration_text(catalog_text, catalog.line), "imported_by_cases": catalog_importers}},
        "reduction": {"file": reduction_file, "module": module_name(reduction_file), "name": reduction.name,
                      "declarations": [declaration_record(declaration) | (
                          {"text": declaration_text(reduction_text, declaration.line)} if declaration.kind in ("def", "abbrev") else {})
                          for declaration in sorted(reduction_scan.values(), key=lambda item: item.line)]},
        "cases": cases, "milestones": milestones,
        "files": len(lean), "certificates": certificates,
        "folders": sorted(({"folder": folder, **tally} for folder, tally in folders.items()),
                          key=lambda row: (-row["files"], row["folder"])),
    }
    return record, problems


def mathlib_and_tauceti(manifest: dict) -> tuple[str, str]:
    revs = {package.get("name"): package.get("rev", "") for package in manifest.get("packages", [])}
    return revs.get("mathlib", ""), revs.get("TauCeti", revs.get("tauceti", ""))


# The chapter, from the data.

TITLE = "Classification of Finite Simple Groups (Axiom)"
MATHLIB_REPO = "https://github.com/leanprover-community/mathlib4"
TAUCETI_REPO = "https://github.com/TauCetiProject/TauCeti"
FOLDERS_SHOWN = 12
NO_DEPENDS = "Its Lean file imports no case or milestone file, directly or through other files."


def load(data: Path) -> dict | None:
    """data/cfsg/'s source and proof, when both are there."""
    source, proof = data / "cfsg" / "source.json", data / "cfsg" / "proof.json"
    if not (source.is_file() and proof.is_file()):
        return None
    return json.loads(source.read_text(encoding="utf-8")) | json.loads(proof.read_text(encoding="utf-8"))


def blob(rev: str, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{REPO}/blob/{rev}/{path}" + (f"#L{line}" if line else "")


def at(rev: str) -> str:
    return f"[{rev[:8]}]({GITHUB}/{REPO}/tree/{rev})"


def plural(count: int, word: str, words: str | None = None) -> str:
    return f"{count:,} {word if count == 1 else words or word + 's'}"


def listing(parts: list[str]) -> str:
    return ", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else "".join(parts)


def tauceti_names(root: Container | None) -> dict[str, Leaf]:
    """Each Lean name of an article in the Tau Ceti chapter, with its article."""
    names: dict[str, Leaf] = {}
    for node in walk(root) if root is not None else []:
        if isinstance(node, Leaf):
            for name in dict(node.fields).get("lean", "").split(", "):
                if name:
                    names.setdefault(name, node)
    return names


def mentioned(declarations: list[dict], names: dict[str, Leaf]) -> list[str]:
    """The Tau Ceti names with an article that the declarations' statements write out in full, in order."""
    out: list[str] = []
    for declaration in declarations:
        for name in TAUCETI_NAME.findall(declaration.get("statement") or declaration.get("text") or ""):
            if name in names and name not in out:
                out.append(name)
    return out


def status(declaration: dict) -> str:
    if declaration["kind"] in ("theorem", "lemma"):
        return "Stated without proof: its proof holds `sorry`." if declaration["sorry"] else "Proved here."
    return "A definition whose value holds `sorry`." if declaration["sorry"] else "A definition."


def block(declaration: dict, file: str, rev: str) -> str:
    """A declaration with its line and status, and its Lean statement, or a definition's whole text."""
    where = f"[line {declaration['line']}]({blob(rev, file, declaration['line'])})"
    lines = [f"`{declaration['name']}` ({declaration['kind']}, {where}). {status(declaration)}"]
    if declaration.get("text"):
        lines += ["", fence(declaration["text"])]
    elif declaration["statement"] is None:
        lines += ["", "Its statement is not shown: no `:=` or `where` ends it."]
    else:
        lines += ["", fence(declaration["statement"])]
    return "\n".join(lines)


def quoted(file: str, rev: str) -> str:
    return f"quoted from [{file}]({blob(rev, file)}) in [{REPO}]({GITHUB}/{REPO}) at commit {at(rev)}, Apache-2.0"


def theorem_fields(names: list[str], proved: bool) -> list[tuple[str, str]]:
    # Each article states a theorem, whatever its module declares first.
    return [("declaration", "theorem"), ("origin", "cited"), ("lean", ", ".join(names)), ("statement", "formalized")] + (
        [("proof", "formalized")] if proved else [])


def tauceti_note(leaf: Leaf, declarations: list[dict], tau: dict[str, Leaf], targets: dict) -> None:
    names = mentioned(declarations, tau)
    for name in names:
        targets[f"tauceti:{name}"] = tau[name]
    if names:
        leaf.notes.append(("Tau Ceti", "\n".join(
            f"- A statement here names `{name}`, which has [an article](trough:tauceti:{name}) in the Tau Ceti chapter."
            for name in names)))


def milestone_link(module: str) -> str:
    return f"[{escape(module.rsplit('.', 1)[-1])}](trough:cfsg-{module})"


def top_article(data: dict, cases: list[dict]) -> Leaf:
    rev, top = data["rev"], data["top"]
    catalog = top["catalog"]
    reduction = data["reduction"]
    lines = [f"The proof's top theorem, {quoted(top['file'], rev)}:", block(top, top["file"], rev),
             f"Its proof applies [`{reduction['name']}`](trough:cfsg-reduction) to the catalog `{catalog['name']}` and to "
             f"a theorem for each of the reduction's {plural(len(cases), 'hypothesis', 'hypotheses')}, in its order:",
             "\n".join(f"- `{case['hypothesis']} : {case['type']}`: [`{case['theorem']['name']}`](trough:cfsg-case-{case['hypothesis']})"
                       for case in cases),
             f"The catalog, declared in [{catalog['file']}, line {catalog['line']}]({blob(rev, catalog['file'], catalog['line'])}):",
             fence(catalog["text"])]
    leaf = Leaf(escape(top["name"]), "top-theorem", theorem_fields([top["name"]], not top["sorry"]), "\n\n".join(lines),
                no_depends="Its statement uses no other result mapped here.")
    leaf.sources = [(f"{top['file']} at {rev[:8]}", blob(rev, top["file"], top["line"]))]
    return leaf


def reduction_article(data: dict) -> Leaf:
    rev, reduction = data["rev"], data["reduction"]
    declarations = reduction["declarations"]
    lines = [f"The module `{reduction['module']}` defines each case of the proof's case division as a proposition and "
             f"derives the classification from them. Its {plural(len(declarations), 'declaration')}, in file order, "
             f"{quoted(reduction['file'], rev)}; each definition is shown whole:"]
    lines += [block(declaration, reduction["file"], rev) for declaration in declarations]
    theorems = [declaration for declaration in declarations if declaration["kind"] in ("theorem", "lemma")]
    leaf = Leaf(escape(reduction["module"]), "reduction",
                theorem_fields([declaration["name"] for declaration in declarations],
                               not any(declaration["sorry"] for declaration in theorems)),
                "\n\n".join(lines), no_depends="It uses no other result mapped here.")
    leaf.sources = [(f"{reduction['file']} at {rev[:8]}", blob(rev, reduction["file"]))]
    return leaf


def case_article(case: dict, data: dict) -> Leaf:
    rev, reduction = data["rev"], data["reduction"]
    theorem, definition = case["theorem"], case["definition"]
    reaches = case["reaches"]
    lines = [f"The case `{case['hypothesis']} : {case['type']}` of [`{reduction['name']}`](trough:cfsg-reduction). "
             f"What it asserts, defined in [{reduction['file']}, line {definition['line']}]"
             f"({blob(rev, reduction['file'], definition['line'])}):",
             fence(definition["text"]),
             f"The theorem the top theorem's proof gives for it, {quoted(theorem['file'], rev)}:",
             block(theorem, theorem["file"], rev),
             (f"Its file imports, directly or through other files, {plural(len(reaches), 'milestone module')}: "
              + ", ".join(milestone_link(module) for module in reaches) + "."
              if reaches else "Its file imports none of the milestone modules, directly or through other files.")]
    leaf = Leaf(escape(theorem["name"]), slugify(f"case {case['hypothesis']} {case['type']}"),
                theorem_fields([theorem["name"]], not theorem["sorry"]), "\n\n".join(lines), no_depends=NO_DEPENDS)
    leaf.sources = [(f"{theorem['file']} at {rev[:8]}", blob(rev, theorem["file"], theorem["line"]))]
    return leaf


def milestone_article(milestone: dict, data: dict, case_titles: dict[str, str]) -> Leaf:
    rev, file, declarations = data["rev"], milestone["file"], milestone["declarations"]
    lines = [f"The milestone module `{milestone['module']}`"
             + (", one of those CFSG/Milestones.lean imports." if milestone["indexed"]
                else ", which CFSG/Milestones.lean does not import."),
             f"It declares {plural(len(declarations), 'result')}, {quoted(file, rev)}:" if declarations
             else "It declares nothing the reading keeps."]
    lines += [block(declaration, file, rev) for declaration in declarations]
    cases = milestone["cases"]
    lines.append(f"The files of {plural(len(cases), 'case theorem')} import it, directly or through other files: "
                 + ", ".join(f"[`{name}`](trough:{case_titles[name]})" for name in cases) + "."
                 if cases else "No case theorem's file imports it, directly or through other files.")
    leaf = Leaf(escape(milestone["id"]), slugify(milestone["id"]),
                theorem_fields([declaration["name"] for declaration in declarations],
                               not any(declaration["sorry"] for declaration in declarations)) if declarations else [],
                "\n\n".join(lines), no_depends=NO_DEPENDS)
    leaf.sources = [(f"{file} at {rev[:8]}", blob(rev, file))]
    return leaf


def chapter(data: dict, tauceti: Container | None = None) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and each mapped declaration's source line (for
    hooks/lean-links.json). A part for the case division, then one for the milestones."""
    rev, cases, milestones = data["rev"], data["cases"], data["milestones"]
    tau = tauceti_names(tauceti)
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    stats: Counter = Counter()
    top, reduction = top_article(data, cases), reduction_article(data)
    targets["cfsg-top"], targets["cfsg-reduction"] = top, reduction
    case_leaves = {}
    for case in cases:
        leaf = case_article(case, data)
        case_leaves[case["theorem"]["module"]] = leaf
        targets[f"cfsg-case-{case['hypothesis']}"] = leaf
    case_titles = {case["theorem"]["name"]: f"cfsg-case-{case['hypothesis']}" for case in cases}
    milestone_leaves = {}
    for milestone in milestones:
        leaf = milestone_article(milestone, data, case_titles)
        milestone_leaves[milestone["module"]] = leaf
        targets[f"cfsg-{milestone['module']}"] = leaf
    by_module = case_leaves | milestone_leaves
    top.proof_depends = [reduction, *(case_leaves[case["theorem"]["module"]] for case in cases)]
    for case in cases:
        leaf = case_leaves[case["theorem"]["module"]]
        leaf.depends = [by_module[module] for module in case["depends"]]
        stats["edges"] += len(leaf.depends)
    for milestone in milestones:
        leaf = milestone_leaves[milestone["module"]]
        leaf.depends = [by_module[module] for module in milestone["depends"]]
        stats["edges"] += len(leaf.depends)
        stats["unreached"] += not milestone["cases"]
        stats["indexed"] += milestone["indexed"]
    every = [(data["top"]["file"], [data["top"]]), (data["reduction"]["file"], data["reduction"]["declarations"]),
             *((case["theorem"]["file"], [case["theorem"]]) for case in cases),
             *((milestone["file"], milestone["declarations"]) for milestone in milestones)]
    for file, declarations in every:
        for declaration in declarations:
            links.setdefault(declaration["name"], blob(rev, file, declaration["line"]))
            stats["sorry"] += declaration["sorry"]
    stats["milestone_declarations"] = sum(len(milestone["declarations"]) for milestone in milestones)
    for result in data["main_results"]:
        links.setdefault(result["name"], blob(rev, result["file"], result["line"]))
    for leaf, declarations in [(top, [data["top"]]), (reduction, data["reduction"]["declarations"]),
                               *((case_leaves[case["theorem"]["module"]], [case["theorem"]]) for case in cases),
                               *((milestone_leaves[milestone["module"]], milestone["declarations"]) for milestone in milestones)]:
        tauceti_note(leaf, declarations, tau, targets)
        stats["tauceti"] += bool(leaf.notes)

    division = Container("The case division", "case-division",
                         [Entry(top), Entry(reduction),
                          *(Entry(case_leaves[case["theorem"]["module"]], label=f"{case['type']}: {escape(case['theorem']['name'])}")
                            for case in cases)])
    division.prose = (f"The top theorem, the module that reduces it to {plural(len(cases), 'case')}, and the theorem "
                      "the top theorem's proof gives for each case, in the order of the reduction's hypotheses. Each "
                      "entry for a case names the proposition it proves.")
    part = Container("Milestones", "milestones", [Entry(milestone_leaves[milestone["module"]]) for milestone in milestones])
    part.prose = (f"The {plural(len(milestones), 'module')} directly under `{MILESTONES}/`, by file name, one article "
                  f"each; CFSG/Milestones.lean imports {stats['indexed']:,} of them. "
                  f"{plural(stats['unreached'], 'milestone is', 'milestones are')} imported by no case theorem's file, "
                  "directly or through other files.")
    targets["cfsg-division"], targets["cfsg-milestones"] = division, part
    root = Container(TITLE, "cfsg", [Entry(division), Entry(chunk(part))])
    stats["articles"] = 2 + len(cases) + len(milestones)
    stats["cases"], stats["milestones"] = len(cases), len(milestones)
    root.prose = intro(data, stats, tau, targets)
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items()))


def main_results(data: dict, tau: dict[str, Leaf], targets: dict, stats: Counter) -> str:
    rev = data["rev"]
    by_name = {declaration["name"]: milestone for milestone in data["milestones"]
               for declaration in milestone["declarations"]}
    parts = [f"Its formalization.yaml names {plural(len(data['main_results']), 'main result')}."]
    for result in data["main_results"]:
        where = f"[{result['file']}, line {result['line']}]({blob(rev, result['file'], result['line'])})"
        line = f"`{result['name']}` ({result['kind']}), in {where}."
        if result["name"] in by_name:
            parts.append(line + f" Its milestone has [an article](trough:cfsg-{by_name[result['name']]['module']}).")
            continue
        parts.append(line + (" Its statement:" if result["statement"] else ""))
        if result["statement"]:
            parts.append(fence(result["statement"]))
        names = mentioned([result], tau)
        for name in names:
            targets[f"tauceti:{name}"] = tau[name]
        stats["tauceti_main"] += bool(names)
        if names:
            parts.append(" ".join(f"It names `{name}`, which has [an article](trough:tauceti:{name}) in the Tau Ceti "
                                  "chapter." for name in names))
    return "\n\n".join(parts)


def composition(data: dict) -> str:
    folders = data["folders"]
    documented = [row for row in folders if row["documented"]]
    rows = [f"- `{row['folder']}/`: {plural(row['files'], 'file')}, {plural(row['theorems'], 'theorem or lemma', 'theorems and lemmas')}"
            for row in folders[:FOLDERS_SHOWN]]
    doc_line = ("No file has a docstring or module docstring" if not documented else
                "Docstrings and module docstrings appear only in "
                + plural(sum(row["documented"] for row in documented), "file") + ", under "
                + listing([f"`{row['folder']}/`" for row in documented]))
    return "\n\n".join([
        f"The commit has {plural(data['files'], 'Lean file')} besides {plural(data['certificates'], 'certificate file')} "
        "under `Certificates/` and `CFSG/Certificates/`, which are counted, not read. Its largest folders, by the number "
        "of files, with the theorems and lemmas their text declares:",
        "\n".join(rows),
        f"{doc_line}, so the titles here are Lean names: a case's article is titled by its theorem, and a milestone's "
        "by its file name."])


def intro(data: dict, stats: Counter, tau: dict[str, Leaf], targets: dict) -> str:
    rev = data["rev"]
    rows = facts({**data, "repo": REPO})
    if data.get("tauceti"):
        rows += (f"\n- Tau Ceti at [{data['tauceti'][:8]}]({TAUCETI_REPO}/tree/{data['tauceti']}), a Lake dependency; "
                 "the README says the proof uses Tau Ceti's statement of the classification.")
    clean = stats["sorry"] == 0
    catalog_case = next((case for case in data["cases"] if case["theorem"]["file"] == data["top"]["catalog"]["file"]), None)
    return "\n\n".join(part for part in [
        f"[{REPO}]({GITHUB}/{REPO}) is a Lean proof of the classification of finite simple groups, by Axiom Math. "
        "Its README says:",
        quote("\n\n".join(data["readme"])) if data["readme"] else "",
        rows,
        "## Main results",
        main_results(data, tau, targets, stats),
        "## This map",
        f"The chapter follows the proof as the repository writes it. [`{data['top']['name']}`](trough:cfsg-top), in "
        f"{data['top']['file']}, states the classification. Its proof applies `{data['reduction']['name']}` to "
        f"{plural(stats['cases'], 'theorem')}, one for each case of a case division that "
        f"[{data['reduction']['file']}](trough:cfsg-reduction) defines; [the case division](trough:cfsg-division) "
        f"has an article for each of these. [The milestones](trough:cfsg-milestones) are the "
        f"{plural(stats['milestones'], 'module')} directly under `{MILESTONES}/`, the results the authors single out: "
        f"{plural(stats['milestone_declarations'], 'declaration')} in all. An article shows each declaration's Lean "
        "statement, or a definition's whole text, its line in the source and its status.",
        composition(data),
        "No Lean is run for this chapter. The repository's README says it builds in under 24 hours only with changes "
        "to Lake, so its declarations are read from the source text: a declaration's Lean statement is its text up "
        "to the `:=` or `where` that starts its value, and “Proved here.” means that value holds no `sorry`. "
        + ("None does, as the repository's formalization.yaml states." if clean else
           f"{plural(stats['sorry'], 'declaration holds', 'declarations hold')} `sorry`."),
        "The top theorem's article lists the reduction and the case theorems under what its proof depends on, as its "
        "proof names them. Every other edge comes from imports: an edge from one case or milestone to another means "
        "that the first one's Lean file imports the other's, directly or through other files, and imports no other "
        "case or milestone file that does; an edge implied by two others is left out. There are "
        f"{plural(stats['edges'], 'such edge')}, shown as what an article depends on (“Statement uses” on the site). "
        f"{plural(data['top']['catalog']['imported_by_cases'], 'case file imports', 'case files import')} "
        f"{data['top']['catalog']['file']}, directly or through other files, for the catalog it declares"
        + (f" beside the theorem for the case `{catalog_case['hypothesis']} : {catalog_case['type']}`" if catalog_case else "")
        + "; imports of that file are not edges. An import makes the other file's results available; it does not say "
        "which of them a proof uses.",
        ("Where a statement writes out the full name of a declaration that has an article in the Tau Ceti chapter, "
         "the page that shows the statement links that article: "
         + listing([text for count, text in (
             (stats["tauceti"], plural(stats["tauceti"], "article here")),
             (stats["tauceti_main"], plural(stats["tauceti_main"], "main result above"))) if count] or ["none here"])
         + (" does so." if stats["tauceti"] + stats["tauceti_main"] == 1 else " do so.")) if tau else "",
        f"The README text and Lean source are quoted from [{REPO}]({GITHUB}/{REPO}) at commit {at(rev)}, under its "
        "Apache-2.0 license.",
    ] if part)
