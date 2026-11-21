"""The Riemann Hypothesis chapter: the Lean source that claims RH and GRH for Dirichlet L-functions.

leanprover-community/riemann-hypothesis mirrors that source, announced by Alpöge on 2026-11-20, with the files
Comparator needs to check it. The source has no license, so the chapter states facts only: names, counts and links
into the repository at the pinned commit. It quotes none of its text: no statement, README or note.

The source is too big for an article per module (175,187 files), so the chapter has a page per top-level folder of
`src/` and a part per second-level folder of at least PART_FILES files, with file, line and declaration counts read
by a line scan, and the import lines between those pages. The five theorems Comparator's configuration names each get
an article whose statement is formalized and whose proof is not, until a passing Comparator run is recorded.

refresh() reads a checkout into data/riemann-hypothesis/: source.json (the commit, toolchain, Mathlib pin, lakefile
libraries, the five theorems' lines and the totals), folders.json (the counts per folder and the import lines
between folders), scan.json (a line scan for constructs that skip checks) and verification.json (the repository's
verification/ folder as file names and blob hashes, the hash of its notes' Results section, and Comparator's status).
The status is "pending" unless a person records a passing run: the file and the commit that hold Comparator's output.
The refresh then checks that file and records what it found; chapter() shows the proof as formalized only when that
check holds.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tomllib
from collections import Counter, defaultdict
from pathlib import Path

from .blueprints import Built
from .vault import Container, Entry, Leaf, slugify, walk

ID = "riemann-hypothesis"
TITLE = "Riemann Hypothesis (Alpöge)"
REPO = "leanprover-community/riemann-hypothesis"
URL = f"https://github.com/{REPO}"
ANNOUNCEMENT = "https://alpo.ge/remark.pdf"
COMPARATOR = "https://github.com/leanprover/comparator"
MATHLIB = "https://github.com/leanprover-community/mathlib4"
MATHLIB_RH = ("https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html"
              "#RiemannHypothesis")
# Formal Conjectures' statement of RH, whose article the RH articles link.
FC_RH = "RiemannHypothesis.riemannHypothesis"
# A second-level folder with at least this many files gets its own page.
PART_FILES = 300
# The line `lake comparator` prints when every checker accepts.
SUCCESS = "Your solution is okay!"
# The source files the repository added for Comparator, which are not the submission's.
ADDED = ("Challenge.lean",)
# What each theorem Comparator's configuration names states, in our words.
CLAIMS = {
    "riemannHypothesis": "Mathlib's [`RiemannHypothesis`]({rh}).",
    "riemannZeta_eq_zero_re": "Mathlib's [`RiemannHypothesis`]({rh}) with its definition unfolded: a zero of "
                              "`riemannZeta` that is neither a trivial zero nor the point 1 has real part 1/2.",
    "LFunction_ne_zero_of_half_lt_re": "No Dirichlet L-function vanishes where the real part exceeds 1/2, for any "
                                       "modulus and any character, leaving out the trivial character at 1.",
    "LFunction_eq_zero_re": "The Generalized Riemann Hypothesis for Dirichlet L-functions: a zero whose real part lies "
                            "strictly between 0 and 1 has real part 1/2, for any modulus and any character.",
    "LFunction_eq_zero_re_of_isPrimitive": "The Generalized Riemann Hypothesis for the L-functions of primitive "
                                           "Dirichlet characters.",
}
# The theorems whose article links Formal Conjectures' page, and what that page states of them.
FC_NOTES = {
    "riemannHypothesis": "states Mathlib's `RiemannHypothesis` as an open problem",
    "riemannZeta_eq_zero_re": "states Mathlib's `RiemannHypothesis` as an open problem",
    "LFunction_eq_zero_re_of_isPrimitive": "states the Generalized Riemann Hypothesis for primitive Dirichlet "
                                           "characters as an open problem",
}

MODIFIERS = r"(?:(?:private|protected|noncomputable|partial|nonrec|unsafe|public|scoped|local|meta)[ \t]+)*"
ATTRIBUTES = r"(?:@\[[^\n]*?\][ \t]*)*"
DECLARATION = re.compile(rf"^[ \t]*{ATTRIBUTES}{MODIFIERS}(theorem|lemma|def|abbrev|structure|class|instance|inductive)\b",
                         re.M)
IMPORT = re.compile(r"^(?:public[ \t]+)?(?:meta[ \t]+)?import[ \t]+(?:all[ \t]+)?(\S+)", re.M)
# The line scan: a label, how the front page names it, and its pattern.
SCAN = (
    ("sorry", "`sorry`", r"\bsorry\b"),
    ("admit", "`admit`", r"\badmit\b"),
    ("axiom", "`axiom` declaration", rf"^[ \t]*{ATTRIBUTES}{MODIFIERS}axiom\b"),
    ("native_decide", "`native_decide`", r"\bnative_decide\b|\bofReduceBool\b|\btrustCompiler\b"),
    ("implemented_by", "`implemented_by`", r"\bimplemented_by\b"),
    ("extern", "`extern`", r"\bextern\b"),
    ("unsafe", "`unsafe`", r"\bunsafe\b"),
    ("opaque", "`opaque`", r"\bopaque\b"),
    ("debug", "`debug` option", r"\bset_option[ \t]+debug\."),
    ("skipKernelTC", "`skipKernelTC`", r"\bskipKernelTC\b"),
    ("addDecl", "`addDecl`", r"\baddDecl\b|\baddAndCompile\b"),
    ("modifyEnv", "`modifyEnv`", r"\bmodifyEnv\b|\bsetEnv\b"),
    ("run_tac", "`run_tac`", r"\brun_tac\b"),
    ("kexactB", "`kexactB`", r"\bkexactB\b"),
    ("kcopy", "`kcopy`", r"\bkcopy\b"),
    ("allowUnsafeReducibility", "`allowUnsafeReducibility`", r"\ballowUnsafeReducibility\b"),
)
# The tactics the source defines that assign a term to the goal without the elaborator checking its type.
UNCHECKED = ("kexactB", "kcopy")


# Reading the checkout.

def git(checkout: Path, *args: str) -> str:
    # Dates in UTC, whatever the committer's zone.
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def blob_hash(data: bytes) -> str:
    """The file's git blob hash."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def unit_of(parts: tuple[str, ...]) -> tuple[str, str]:
    """A file's folder for the counts, from its path below src/: "" for a file of src/ itself, the top-level folder
    for a file directly in it, else the second-level folder; and its third-level folder, "" for a file directly in
    the second-level one."""
    if len(parts) == 1:
        return "", ""
    if len(parts) == 2:
        return parts[0], ""
    return f"{parts[0]}/{parts[1]}", parts[2] if len(parts) > 3 else ""


def tally(text: str) -> Counter:
    lines = text.splitlines()
    counts = Counter(files=1, lines=len(lines), nonblank=sum(1 for line in lines if line.strip()),
                     bytes=len(text.encode("utf-8")))
    for match in DECLARATION.finditer(text):
        counts["theorems" if match.group(1) in ("theorem", "lemma") else "definitions"] += 1
    return counts


def results_section(notes: str) -> str:
    """The notes' Results section, from its heading to the next of its level."""
    match = re.search(r"(?ms)^## Results[ \t]*$.*?(?=^## |\Z)", notes)
    return match.group() if match else ""


def evidence_check(text: str, names: list[str]) -> dict:
    """What a file said to hold Comparator's output shows: its blob hash, whether it has the passing line, and which
    of the theorems it names."""
    data = text.encode("utf-8")
    return {"blob": blob_hash(data), "success": SUCCESS in text,
            "names": [name for name in names if re.search(rf"\b{re.escape(name)}\b", text)]}


def refresh(checkout: Path, out: Path, evidence: Path | None = None) -> tuple[list[str], list[str]]:
    """Write the chapter's data from a checkout; return the problems, if any, and how the verification folder changed
    since the last record. Nothing is written when there is a problem."""
    problems: list[str] = []
    src = checkout / "src"
    lakefile = tomllib.loads((checkout / "lakefile.toml").read_text(encoding="utf-8"))
    comparator = json.loads((checkout / "comparator.json").read_text(encoding="utf-8"))
    manifest = json.loads((checkout / "lake-manifest.json").read_text(encoding="utf-8"))
    names = comparator["theorem_names"]
    if set(names) != set(CLAIMS):
        problems.append(f"comparator.json names {', '.join(names)}, not the five theorems the chapter describes")

    units: dict[str, Counter] = defaultdict(Counter)
    subs: dict[str, dict[str, Counter]] = defaultdict(lambda: defaultdict(Counter))
    files = sorted(path for path in src.rglob("*.lean") if path.relative_to(src).as_posix() not in ADDED)
    modules = {path.relative_to(src).with_suffix("").as_posix().replace("/", ".") for path in files}
    module_unit = {path.relative_to(src).with_suffix("").as_posix().replace("/", "."):
                   unit_of(path.relative_to(src).parts)[0] for path in files}
    imports: dict[str, Counter] = defaultdict(Counter)
    scan_lines, scan_files = Counter(), Counter()
    patterns = [(key, re.compile(pattern, re.M)) for key, _, pattern in SCAN]
    for path in files:
        text = path.read_text(encoding="utf-8")
        unit, sub = unit_of(path.relative_to(src).parts)
        counts = tally(text)
        units[unit].update(counts)
        if "/" in unit:
            subs[unit][sub].update(counts)
        for match in IMPORT.finditer(text):
            target = match.group(1)
            imports[unit][module_unit[target] if target in modules else "@" + target.split(".")[0]] += 1
        for key, pattern in patterns:
            hits = sum(1 for _ in pattern.finditer(text))
            if hits:
                scan_lines[key] += hits
                scan_files[key] += 1
    totals = Counter()
    for counts in units.values():
        totals.update(counts)

    def lines_of(file: str) -> dict[str, int]:
        text = (src / file).read_text(encoding="utf-8")
        found = {}
        for number, line in enumerate(text.splitlines(), 1):
            match = re.match(r"theorem[ \t]+(\S+)", line)
            if match and match.group(1) in names:
                found.setdefault(match.group(1), number)
        return found

    main_lines, challenge_lines = lines_of("Main.lean"), lines_of("Challenge.lean")
    for name in names:
        if name not in main_lines or name not in challenge_lines:
            problems.append(f"{name} is not declared in both src/Main.lean and src/Challenge.lean")

    libraries = []
    defaults = lakefile.get("defaultTargets", [])
    for lib in lakefile.get("lean_lib", []):
        entry = {"name": lib["name"], "comparator": lib["name"] not in defaults}
        for key in ("globs", "roots"):
            if key in lib:
                entry[key] = lib[key]
        libraries.append(entry)
    mathlib = next((package["rev"] for package in manifest.get("packages", []) if package.get("name") == "mathlib"), None)

    verification = checkout / "verification"
    listing = {path.relative_to(verification).as_posix(): blob_hash(path.read_bytes())
               for path in sorted(verification.rglob("*")) if path.is_file()}
    notes = (verification / "NOTES.md").read_text(encoding="utf-8") if (verification / "NOTES.md").is_file() else ""
    results = hashlib.sha256(results_section(notes).encode("utf-8")).hexdigest()
    previous_path = out / "verification.json"
    previous = json.loads(previous_path.read_text(encoding="utf-8")) if previous_path.is_file() else None
    status = dict(previous["comparator"]) if previous else {"status": "pending"}
    changes: list[str] = []
    if previous:
        old = set(previous["files"])
        changes += [f"verification/{name} added" for name in sorted(listing.keys() - old)]
        changes += [f"verification/{name} removed" for name in sorted(old - listing.keys())]
        if previous["results"] != results:
            changes.append("the Results section of verification/NOTES.md changed")
    if status["status"] == "passed":
        missing = [key for key in ("file", "commit") if not status.get(key)]
        if missing:
            problems.append(f"verification.json records a passing run without its {' and '.join(missing)}")
        elif evidence is None:
            problems.append(f"verification.json records a passing run in {status['file']} at {status['commit'][:8]}; "
                            "pass that file as fetched at that commit")
        else:
            check = evidence_check(evidence.read_text(encoding="utf-8"), names)
            status["checked"] = check
            if not check["success"] or set(check["names"]) != set(names):
                problems.append(f"{status['file']} at {status['commit'][:8]} does not hold Comparator's passing line "
                                "and all five theorem names")
    elif status["status"] != "pending":
        problems.append(f"verification.json has the unknown status {status['status']}")

    if problems:
        return problems, changes
    out.mkdir(parents=True, exist_ok=True)
    rev = git(checkout, "rev-parse", "HEAD")
    source = {
        "repo": REPO, "rev": rev,
        "date": git(checkout, "show", "-s", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
        "toolchain": (checkout / "lean-toolchain").read_text(encoding="utf-8").strip(), "mathlib": mathlib,
        "libraries": libraries,
        "theorems": [{"name": name, "main_line": main_lines[name], "challenge_line": challenge_lines[name]}
                     for name in names],
        "permitted_axioms": comparator.get("permitted_axioms", []),
        "totals": dict(sorted(totals.items())),
    }
    folders = {
        "units": {unit: dict(sorted(units[unit].items()))
                  | ({"sub": {sub: dict(sorted(counts.items())) for sub, counts in sorted(subs[unit].items())}}
                     if "/" in unit else {})
                  for unit in sorted(units)},
        "imports": {unit: dict(sorted(imports[unit].items())) for unit in sorted(imports)},
    }
    scan = {"files": len(files), "patterns": [{"key": key, "lines": scan_lines[key], "files": scan_files[key]}
                                              for key, _, _ in SCAN]}
    record = {"files": listing, "results": results, "comparator": status}
    for name, value in (("source", source), ("folders", folders), ("scan", scan), ("verification", record)):
        (out / f"{name}.json").write_text(json.dumps(value, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return [], changes


def load(data: Path) -> dict | None:
    folder = data / ID
    if not (folder / "source.json").is_file():
        return None
    return {name: json.loads((folder / f"{name}.json").read_text(encoding="utf-8"))
            for name in ("source", "folders", "scan", "verification")}


# The chapter.

def plural(count: int, word: str, many: str | None = None) -> str:
    return f"{count:,} {word if count == 1 else many or word + 's'}"


def listing(items: list[str], conjunction: str = "and") -> str:
    if len(items) <= 2:
        return f" {conjunction} ".join(items)
    return ", ".join(items[:-1]) + f" {conjunction} " + items[-1]


def verified(record: dict, names: list[str]) -> bool:
    """Whether the data record a passing Comparator run that the refresh checked: the file and commit a person named,
    with Comparator's passing line and every theorem's name in it."""
    status = record["comparator"]
    if status["status"] != "passed":
        return False
    check = status.get("checked") or {}
    if not (status.get("file") and status.get("commit") and check.get("success") and set(check.get("names", ())) >= set(names)):
        raise ValueError(f"data/{ID}/verification.json records a passing run the refresh has not checked")
    return True


def chapter(data: dict, fc_root: Container | None = None) -> tuple[Built, dict[str, str]]:
    source, folders, scan, record = data["source"], data["folders"], data["scan"], data["verification"]
    rev = source["rev"]
    short = rev[:8]
    names = [theorem["name"] for theorem in source["theorems"]]
    passed = verified(record, names)
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}

    def blob(path: str, line: int | None = None) -> str:
        return f"{URL}/blob/{rev}/{path}" + (f"#L{line}" if line else "")

    def tree(path: str) -> str:
        return f"{URL}/tree/{rev}/{path}"

    fc_page = None
    if fc_root is not None:
        fc_page = next((node for node in walk(fc_root) if isinstance(node, Leaf)
                        and FC_RH in dict(node.fields).get("lean", "").split(", ")), None)
    if fc_page is not None:
        targets["fc-rh"] = fc_page

    # The theorem articles.
    theorem_entries = []
    for number, theorem in enumerate(source["theorems"]):
        name = theorem["name"]
        if name not in CLAIMS:
            raise ValueError(f"data/{ID}/source.json names {name}, which the chapter does not describe")
        main = blob("src/Main.lean", theorem["main_line"])
        links[name] = main
        parts = [f"`{name}`, in [src/Main.lean, line {theorem['main_line']}]({main}): "
                 + CLAIMS[name].format(rh=MATHLIB_RH),
                 f"Comparator's challenge states it over Mathlib alone, in "
                 f"[src/Challenge.lean, line {theorem['challenge_line']}]({blob('src/Challenge.lean', theorem['challenge_line'])})."]
        fields = [("declaration", "theorem"), ("origin", "cited"), ("lean", name), ("statement", "formalized")]
        if passed:
            status = record["comparator"]
            parts.append(f"Comparator accepted the proof in the run recorded in "
                         f"[{status['file']}]({URL}/blob/{status['commit']}/{status['file']}).")
            fields.append(("proof", "formalized"))
        else:
            parts.append("The proof is claimed and not verified: Comparator's check is pending, so this page shows no "
                         f"proof. See the repository's [verification notes]({blob('verification/NOTES.md')}).")
        leaf = Leaf(name, slugify(name), fields, "\n\n".join(parts))
        leaf.no_depends = "Its statement uses no other declaration mapped here."
        if fc_page is not None and name in FC_NOTES:
            leaf.notes.append(("Also stated", f"[Formal Conjectures](trough:fc-rh) {FC_NOTES[name]}."))
        leaf.sources = [(f"src/Main.lean at {short}", main),
                        (f"src/Challenge.lean at {short}", blob("src/Challenge.lean", theorem["challenge_line"])),
                        (f"comparator.json at {short}", blob("comparator.json"))]
        if "RiemannHypothesis" in CLAIMS[name]:
            leaf.sources.append(("Mathlib documentation: `RiemannHypothesis`", MATHLIB_RH))
        targets[f"{ID}-theorem-{name}"] = leaf
        stats["theorems"] += 1
        before = ("## Claimed theorems\n\nThe five theorems Comparator's configuration names, in "
                  f"[src/Main.lean]({blob('src/Main.lean')}).") if number == 0 else ""
        theorem_entries.append(Entry(leaf, before=before))

    # The folder pages.
    units = folders["units"]
    tops = sorted({unit.split("/")[0] for unit in units})
    parts_of = {unit for unit, counts in units.items() if "/" in unit and counts["files"] >= PART_FILES}

    def page_of(unit: str) -> str:
        return unit if unit in parts_of else unit.split("/")[0]

    def key(page: str) -> str:
        return f"{ID}-folder-{page or 'root'}"

    def page_title(page: str) -> str:
        return page if page else "Main and Statements"

    def where(page: str) -> str:
        return f"src/{page}/" if page else "src/"

    def count_line(counts: dict, page: str) -> str:
        here = (f"[`{where(page)}`]({tree('src/' + page)})" if page else
                f"The files directly in [`src/`]({tree('src')}), `Main.lean` and `Statements.lean`,")
        return (f"{here} {'hold' if not page else 'holds'} {plural(counts['files'], 'file')}: "
                f"{plural(counts['lines'], 'line')}, {counts['nonblank']:,} of them non-blank, with "
                f"{plural(counts.get('theorems', 0), '`theorem` or `lemma` declaration')} and "
                f"{plural(counts.get('definitions', 0), 'other declaration')}.")

    def libraries_line(top: str) -> str:
        found = []
        for lib in source["libraries"]:
            if lib["comparator"]:
                continue
            heads = {pattern.split(".")[0] for pattern in lib.get("globs", [])}
            roots = set(lib.get("roots", []))
            if (top and top in heads) or (not top and roots):
                found.append(lib)
        if not found:
            return ""
        if len(found) == 1:
            return f"The lakefile builds it as the library `{found[0]['name']}`."
        described = []
        for lib in found:
            folders_named = sorted({pattern.split(".")[1] for pattern in lib.get("globs", []) if pattern.count(".") >= 2})
            described.append(f"`{lib['name']}` ({listing(folders_named)})" if folders_named else f"`{lib['name']}`")
        return f"The lakefile builds it as {len(found)} libraries: {listing(described)}."

    def row_link(page: str, label: str) -> str:
        return f"[{label}](trough:{key(page)})"

    def table(rows: list[tuple[str, dict]]) -> str:
        lines = ["| Folder | Files | Lines | `theorem` or `lemma` | Other declarations |", "| --- | ---: | ---: | ---: | ---: |"]
        lines += [f"| {label} | {counts['files']:,} | {counts['lines']:,} | {counts.get('theorems', 0):,} | "
                  f"{counts.get('definitions', 0):,} |" for label, counts in rows]
        return "\n".join(lines)

    def external(name: str) -> str:
        return name.removeprefix("@")

    def imports_lines(members: set[str], group, note: str = "") -> str:
        """The pages the members' files import and the pages whose files import them, by import lines; *group* maps
        a unit to the page it counts under, or None to leave it out."""
        out: Counter = Counter()
        into: Counter = Counter()
        for unit, targets_of in folders["imports"].items():
            for target, count in targets_of.items():
                if unit in members and target not in members:
                    page = external(target) if target.startswith("@") else group(target)
                    if page is not None:
                        out[page] += count
                elif target in members and unit not in members:
                    page = group(unit)
                    if page is not None:
                        into[page] += count

        def named(page: str, count: int) -> str:
            label = row_link(page, page_title(page)) if page in pages_known else page
            return f"{label} ({plural(count, 'line')})"

        def ordered(counter: Counter) -> list[str]:
            return [named(page, count) for page, count in sorted(counter.items(), key=lambda item: (-item[1], item[0]))]

        lines = []
        lines.append(f"Its files import modules of {listing(ordered(out))}." if out else
                     "Its files import no module outside it.")
        lines.append(f"Files of {listing(ordered(into))} import its modules." if into else
                     "No file outside it imports its modules.")
        return f"## Imports\n\nCounted in import lines.{note}\n\n" + "\n\n".join(lines)

    pages_known = set(tops) | parts_of

    def part_page(unit: str) -> Container:
        counts = units[unit]
        container = Container(unit, slugify(unit.replace("/", "-")))
        rows = [((f"[{sub}]({tree(f'src/{unit}/{sub}')})" if sub else f"Files directly in `src/{unit}/`"), sub_counts)
                for sub, sub_counts in counts.get("sub", {}).items()]
        prose = [count_line(counts, unit)]
        if rows:
            prose.append(table(rows))
        prose.append(imports_lines({unit}, page_of, " A top-level folder stands for those of its files that have no "
                                                     "page of their own."))
        container.prose = "\n\n".join(prose)
        targets[key(unit)] = container
        stats["parts"] += 1
        return container

    library_entries = []
    for index, top in enumerate(tops):
        members = {unit for unit in units if unit.split("/")[0] == top}
        counts = Counter()
        for unit in members:
            counts.update({name: value for name, value in units[unit].items() if name != "sub"})
        container = Container(page_title(top), slugify(page_title(top)))
        part_entries = []
        rows = []
        if top and top in units:
            rows.append((f"Files directly in `src/{top}/`", units[top]))
        for unit in sorted(member for member in members if "/" in member):
            label = unit.split("/", 1)[1]
            if unit in parts_of:
                part = part_page(unit)
                part_entries.append(Entry(part, before="" if part_entries else "## Parts"))
                rows.append((row_link(unit, label), units[unit]))
            else:
                rows.append((f"[{label}]({tree('src/' + unit)})", units[unit]))
        prose = [count_line(counts, top)]
        if line := libraries_line(top):
            prose.append(line)
        if rows and top:
            prose.append(table(rows))
        # Its imports, by top-level folder, outside it.
        prose.append(imports_lines(members, lambda unit: unit.split("/")[0]))
        container.prose = "\n\n".join(prose)
        container.entries = part_entries
        targets[key(top)] = container
        stats["libraries"] += 1
        before = ("## Folders\n\nA page per top-level folder of `src/`, and a part per second-level folder of "
                  f"{PART_FILES:,} files or more.") if index == 0 else ""
        library_entries.append(Entry(container, before=before))

    # The front page.
    totals = source["totals"]
    hits = {pattern["key"]: pattern for pattern in scan["patterns"]}
    absent = [label for key_, label, _ in SCAN if not hits.get(key_, {}).get("lines")]
    present = [f"{label} on {plural(hits[key_]['lines'], 'line')} in {plural(hits[key_]['files'], 'file')}"
               for key_, label, _ in SCAN if hits.get(key_, {}).get("lines")]
    unchecked = [f"`{name}`" for name in UNCHECKED if hits.get(name, {}).get("lines")]
    scan_text = f"A line scan of every file finds no {listing(absent, 'or')}." if absent else ""
    if present:
        scan_text += f" It finds {listing(present)}."
    if unchecked:
        scan_text += (f" {listing(unchecked)} {'is a tactic' if len(unchecked) == 1 else 'are tactics'} defined in the "
                      "source that close a goal with a term whose type the elaborator does not compare with it, so "
                      "for those proofs only the kernel's check applies.")
    mathlib = source["mathlib"]
    axioms = [f"`{name}`" for name in source["permitted_axioms"]]
    status_sentence = (
        "Comparator accepted the five theorems' proofs in a recorded run, so the theorem pages show them as formalized."
        if passed else
        "The theorem pages show each statement as formalized and no proof, because no passing Comparator run on this "
        f"source has been recorded; the people checking it keep [notes]({blob('verification/NOTES.md')}) in the "
        "repository.")
    front = [
        "Lean source that claims proofs of the Riemann Hypothesis and of the Generalized Riemann Hypothesis for "
        f"Dirichlet L-functions, announced by Alpöge on 2026-11-20 in [a note]({ANNOUNCEMENT}). "
        f"[{REPO}]({URL}) holds the published source under `src/`, unchanged, with the files a "
        f"[Comparator]({COMPARATOR}) check needs. This chapter reads it at commit [{short}]({URL}/tree/{rev}), "
        f"of {source['date'][:10]}.",
        status_sentence,
        "The source has no license, so this chapter gives names, counts and links, and quotes none of its text.",
        f"`src/` holds {plural(totals['files'], '`.lean` file')} of the submission, leaving out Comparator's "
        f"`Challenge.lean`: {plural(totals['lines'], 'line')}, {totals['nonblank']:,} of them non-blank, and "
        f"{totals['bytes']:,} bytes. A line scan counts {totals.get('theorems', 0):,} `theorem` or `lemma` declarations "
        f"and {totals.get('definitions', 0):,} by `def`, `abbrev`, `structure`, `class`, `instance` or `inductive`. "
        f"It builds on Lean `{source['toolchain'].split(':')[-1]}` and Mathlib at "
        f"[{mathlib[:8]}]({MATHLIB}/tree/{mathlib}).",
        scan_text.strip(),
        f"Comparator's configuration names the five theorems below and permits the axioms {listing(axioms)}.",
    ]
    root = Container(TITLE, ID, theorem_entries + library_entries)
    root.prose = "\n\n".join(paragraph for paragraph in front if paragraph)
    targets[ID] = root
    stats.update({"files": totals["files"], "verified": int(passed)})
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items()))
