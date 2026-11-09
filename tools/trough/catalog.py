"""The book's front page, coverage contract and source catalog, from catalog/libraries.toml."""

from __future__ import annotations

import tomllib
from pathlib import Path

from .vault import frontmatter

GROUPS = (
    ("core-library", "Core library"),
    ("ai-library", "AI-written libraries"),
    ("research-project", "Research projects with blueprints"),
    ("library", "Libraries"),
    ("corpus", "Large corpora"),
    ("formal-frontier", "Formal Frontier libraries"),
)
# The parts of the Formal Frontier chapter, in order; each Formal Frontier library names one as its subject.
SUBJECTS = (
    "Commutative algebra",
    "Ring theory",
    "Algebraic geometry",
    "Number theory",
    "Group theory",
    "Homological algebra and category theory",
    "Topology",
    "Analysis",
)


def load(path: Path) -> list[dict]:
    libraries = tomllib.loads(path.read_text(encoding="utf-8"))["library"]
    known = {group for group, _ in GROUPS}
    for library in libraries:
        missing = {"id", "name", "repo", "group", "map_status", "map_unit", "map_plan"} - library.keys()
        if missing:
            raise ValueError(f"{path}: library {library.get('id', '?')} lacks {', '.join(sorted(missing))}")
        if library["group"] not in known:
            raise ValueError(f"{path}: library {library['id']} has unknown group {library['group']}")
        if library["map_status"] not in ("live", "elsewhere", "planned"):
            raise ValueError(f"{path}: library {library['id']} has unknown map_status {library['map_status']}")
        if library["group"] == "formal-frontier" and library.get("subject") not in SUBJECTS:
            raise ValueError(f"{path}: library {library['id']} has unknown subject {library.get('subject')}")
    ids = [library["id"] for library in libraries]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{path}: duplicate library ids")
    return libraries


def repo_url(library: dict) -> str:
    return f"https://github.com/{library['repo']}"


def files_note(library: dict) -> str:
    count = library.get("lean_files")
    return f" ({count:,} Lean files)" if isinstance(count, int) else ""


def roadmap_root(libraries: list[dict], chapters: dict[str, str], previous: str | None) -> str:
    """The book's preface: the chapters, here or elsewhere, then every library still to map."""
    lines = [
        "# Trough",
        "",
        "Trough maps Lean formalization libraries: what each one formalizes and how its results depend "
        "on one another, not what the library may add. Each library gets the article unit that suits it, "
        "such as curated concepts for Mathlib, the declarations its roadmaps name and the results its docstrings "
        "name for Tau Ceti, blueprint nodes for the research projects and headline results for Formal Frontier. "
        "The maps are rendered with "
        "[AutoformBot](https://github.com/facebookresearch/autoform-bot).",
        "",
        "## Chapters",
        "",
    ]
    listed = set()
    for library in libraries:
        if library["map_status"] == "live" and library["group"] == "formal-frontier":
            # The Formal Frontier libraries share one chapter, listed where the first of them stands.
            if library["group"] in chapters and library["group"] not in listed:
                listed.add(library["group"])
                live = sum(other["group"] == library["group"] and other["map_status"] == "live" for other in libraries)
                lines.append(f"- [Formal Frontier]({chapters[library['group']]}): {live} libraries, a part per "
                             f"subject. {library['map_plan']}")
        elif library["map_status"] == "live" and library["id"] in chapters:
            lines.append(f"- [{library['name']}]({chapters[library['id']]}): {library['map_plan']}")
        elif library["map_status"] == "elsewhere":
            lines.append(f"- [{library['name']}]({repo_url(library)}){files_note(library)}: {library['map_plan']}")
    lines += ["", "## Libraries still to map", ""]
    for group, heading in GROUPS:
        members = [library for library in libraries if library["group"] == group and library["map_status"] == "planned"]
        if not members:
            continue
        lines += [f"### {heading}", ""]
        if group == "formal-frontier":
            lines += [
                f"Formal Frontier, a Mathlib Initiative program, publishes {len(members)} agent-written "
                "libraries that fill gaps around Mathlib. Each will be mapped by its headline results: "
                + ", ".join(f"[{library['name']}]({repo_url(library)})" for library in members)
                + ".",
                "",
            ]
            continue
        for library in members:
            plan = library["map_plan"]
            lines.append(f"- [{library['name']}]({repo_url(library)}){files_note(library)}: {plan}")
        lines.append("")
    # A map records what each library has, not its progress, so the book shows no Lean progress.
    return frontmatter([("tracks_lean", "false")], previous) + "\n".join(lines).rstrip() + "\n"


def coverage(libraries: list[dict], rows: list[tuple[str, str, str]]) -> str:
    lines = [
        "# Coverage",
        "",
        "Each library is a row. A mapped library has one row per source it is mapped from; a library "
        "not mapped yet says what its map will be made of.",
        "",
        "| Area | Coverage | Evidence |",
        "| --- | --- | --- |",
    ]
    lines += [f"| {area} | `{disposition}` | {evidence} |" for area, disposition, evidence in rows]
    for library in libraries:
        if library["map_status"] == "planned":
            lines.append(f"| {library['name']} | `DEFERRED` | Planned map, by {library['map_unit']}: {library['map_plan']} |")
        elif library["map_status"] == "elsewhere":
            lines.append(f"| {library['name']} | `OUT` | {library['map_plan']} |")
    return "\n".join(lines) + "\n"


def sources_readme(libraries: list[dict], mathlib_rev: str, thousand_plus: dict | None,
                   blueprints: list[tuple[str, str, str, str | None, bool]] = (),
                   tauceti: tuple[str, str] | None = None, formal_frontier: dict[str, str] | None = None,
                   formal_conjectures: str | None = None) -> str:
    """The sources page. *blueprints* has (id, name, repo, license, text) for each blueprint library;
    *tauceti* has the Tau Ceti and roadmap commits, once the chapter is built; *formal_frontier* has the
    commit each Formal Frontier library's record pins, by library id; *formal_conjectures* is the Formal
    Conjectures commit read."""
    formal_frontier = formal_frontier or {}
    lines = [
        "# Sources",
        "",
        "Trough reads these sources. The catalog of libraries is `catalog/libraries.toml`.",
        "",
        "## Mathlib's curated lists",
        "",
        f"- `data/mathlib/yaml/`: docs/overview.yaml, docs/undergrad.yaml, docs/100.yaml and docs/1000.yaml "
        f"from [leanprover-community/mathlib4 at {mathlib_rev[:8]}]"
        f"(https://github.com/leanprover-community/mathlib4/tree/{mathlib_rev}/docs), Apache-2.0.",
        "- `data/mathlib/concept-deps.json`: each listed declaration's kind, docstring, signature and "
        "nearest listed dependencies, written by `lean/ConceptDeps.lean` in GitHub Actions.",
    ]
    if thousand_plus:
        source = thousand_plus.get("source", {})
        lines.append(
            f"- `data/thousand-plus.json`: subject classification and Wikipedia pages of the 1000+ theorems, "
            f"from [{source.get('repo', '1000-plus')}](https://github.com/{source.get('repo', '')}) at "
            f"{str(source.get('rev', ''))[:8]}, released into the public domain."
        )
    if blueprints:
        lines += ["", "## Blueprints", ""]
        for project_id, name, repo, license_name, text in blueprints:
            if text:
                lines.append(f"- `data/blueprints/{project_id}/`: the TeX of [{name}'s blueprint](https://github.com/{repo}), "
                             f"pinned in its source.json, {license_name}; the license is copied beside it.")
            else:
                lines.append(f"- `data/blueprints/{project_id}/structure.json`: the titles, labels, Lean names, marks and "
                             f"places of [{name}'s blueprint](https://github.com/{repo}); it gives no license, so its text "
                             "is not copied.")
    if tauceti:
        rev, roadmap_rev = tauceti
        lines += [
            "",
            "## Tau Ceti",
            "",
            f"- `data/tauceti/roadmaps.json`: each roadmap's title and the declarations its STATUS.md names under "
            f"its named results and notable definitions, from [TauCetiProject/TauCetiRoadmap at {roadmap_rev[:8]}]"
            f"(https://github.com/TauCetiProject/TauCetiRoadmap/tree/{roadmap_rev}), Apache-2.0.",
            f"- `data/tauceti/deps.json`: each named declaration's kind, docstring, signature and nearest named "
            f"dependencies in [TauCetiProject/TauCeti at {rev[:8]}](https://github.com/TauCetiProject/TauCeti/tree/{rev}), "
            "Apache-2.0, written by `lean/tauceti/TauCetiDeps.lean` in GitHub Actions.",
        ]
    if formal_frontier:
        lines += [
            "",
            "## Formal Frontier",
            "",
            f"- `data/ff/<name>.json`: for each of the {len(formal_frontier)} Formal Frontier libraries, the facts, highlights "
            "and main results of its formalization.yaml and the headline results of its README, read at the commit the "
            "file records, with the line and kind of each named declaration its file declares, from "
            "[FormalFrontier](https://github.com/FormalFrontier), Apache-2.0. The declarations are read from the source "
            "text, without Lean.",
        ]
    if formal_conjectures:
        lines += [
            "",
            "## Formal Conjectures",
            "",
            f"- `data/formal-conjectures/problems.json`: each problem file's title and module docstring, its research "
            "and textbook statements with their categories, subjects, proof links, docstrings and Lean statements, and "
            "its counts of test and API statements, with the FC100 lists, from "
            f"[google-deepmind/formal-conjectures at {formal_conjectures[:8]}]"
            f"(https://github.com/google-deepmind/formal-conjectures/tree/{formal_conjectures}), Apache-2.0. They are "
            "read from the source text, without Lean.",
        ]
    lines += ["", "## Libraries", ""]
    pinned = {**formal_frontier, **({"formal-conjectures": formal_conjectures} if formal_conjectures else {})}
    for group, heading in GROUPS:
        members = [library for library in libraries if library["group"] == group]
        if members:
            lines.append(f"### {heading}")
            lines.append("")
            for library in members:
                head = pinned[library["id"]][:12] if library["id"] in pinned else library.get("head")
                snapshot = f" at {head}" if head else ""
                lines.append(f"- [{library['name']}]({repo_url(library)}){snapshot}: {library.get('what', '')}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"
