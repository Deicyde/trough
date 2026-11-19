import json
from collections import Counter
from pathlib import Path

import pytest

from trough import links, satellites
from trough.vault import Container, Entry, Leaf, assign_paths, render_container, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "b" * 40
MATHLIB_REV = "c" * 40

APACHE = "                                 Apache License\n                           Version 2.0, January 2004\n" \
         "                        http://www.apache.org/licenses/\n\n   TERMS AND CONDITIONS FOR USE"
MIT = """MIT License

Copyright (c) 2025 Ada Lovelace

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""
MIT0 = """MIT No Attribution

Copyright 2025 Ada Lovelace

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction.
"""
BSD = """BSD {n}-Clause License

Copyright (c) 2024, Thomas Example

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice.
{third}"""
CC0 = "Creative Commons Legal Code\n\nCC0 1.0 Universal\n\n    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM"
CC_BY = "Attribution 4.0 International\n\n=======================================================================\n\n" \
        "Creative Commons Corporation (\"Creative Commons\") is not a law firm"
CC_BY_SA = "Attribution-ShareAlike 4.0 International\n\nCreative Commons Corporation"
SPLIT = """This repository is under two licenses.

The paper, blueprint and home page are under CC BY 4.0. The code is under a separate license, below.

MIT License
"""


@pytest.mark.parametrize("text, expected", [
    (APACHE, ("Apache-2.0", [])),
    (MIT, ("MIT", ["Copyright (c) 2025 Ada Lovelace"])),
    (MIT0, ("MIT-0", ["Copyright 2025 Ada Lovelace"])),
    (BSD.format(n=2, third=""), ("BSD-2-Clause", ["Copyright (c) 2024, Thomas Example"])),
    (BSD.format(n=3, third="3. Neither the name of the copyright holder may be used.\n"),
     ("BSD-3-Clause", ["Copyright (c) 2024, Thomas Example"])),
    (CC0, ("CC0-1.0", [])),
    (CC_BY, ("CC-BY-4.0", [])),
    (CC_BY_SA, (None, [])),
    (SPLIT, (None, [])),
    ("", (None, [])),
])
def test_the_license_is_recognized_from_its_text(text, expected):
    assert satellites.recognize(text) == expected


def test_a_reuse_licenses_folder_alone_is_listed_but_not_applied(tmp_path):
    (tmp_path / "LICENSES").mkdir()
    (tmp_path / "LICENSES" / "BSD-2-Clause").write_text(BSD.format(n=2, third=""))
    record = satellites.read_license(tmp_path, ["LICENSES/BSD-2-Clause", "README.md"])
    assert record == {"files": ["LICENSES/BSD-2-Clause"], "spdx": None, "file": None, "copyright": []}
    (tmp_path / "LICENSE").write_text(MIT)
    record = satellites.read_license(tmp_path, ["LICENSE", "LICENSES/BSD-2-Clause"])
    assert (record["spdx"], record["file"]) == ("MIT", "LICENSE")


def test_the_readme_opening_is_its_first_prose_paragraph_cut_at_a_sentence_end():
    readme = ("# A *Lean* proof of BB(5)\n\n[![CI](https://x/badge.svg)](https://x)\n\n"
              "This repository proves `BB(5) = 47,176,870`. It follows e.g. the Coq proof. Then more text that is "
              + "long " * 150 + "and ends.\n\n## Building\n")
    title, excerpt = satellites.readme_parts(readme)
    assert title == "A Lean proof of BB(5)"
    assert excerpt == "This repository proves `BB(5) = 47,176,870`. It follows e.g. the Coq proof."
    # A paragraph with no sentence end within the limit gives no quote.
    assert satellites.readme_parts("# T\n\nThis contains a formalization of the result:\n\n> X\n") == ("T", None)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


LAKEFILE = """import Lake
open Lake DSL

package «demo» where
  srcDir := "src"

lean_lib Demo where
  roots := #[`Demo]

lean_lib «Extra» where
  globs := #[.submodules `Extra]

lean_exe tool where
  root := `Tool
"""
MANIFEST = {"version": "1.1.0", "packages": [
    {"name": "mathlib", "url": "https://github.com/leanprover-community/mathlib4", "rev": MATHLIB_REV, "inherited": False},
    {"name": "checkdecls", "url": "https://github.com/PatrickMassot/checkdecls.git", "rev": "1" * 40, "inherited": False},
    {"name": "PrimeNumberTheoremAnd", "url": "https://github.com/kimihiro64/PrimeNumberTheoremAnd.git", "rev": "2" * 40,
     "inherited": False},
    {"name": "batteries", "url": "https://github.com/leanprover-community/batteries", "rev": "3" * 40, "inherited": True},
]}
MAIN = """import Mathlib.Analysis.Fourier.AddCircle
import Mathlib.MeasureTheory.Integral.Bochner
import PrimeNumberTheoremAnd.Mathlib

open Real MeasureTheory

namespace Demo

/-- The main theorem; `Demo.helper` is not a declaration here. -/
theorem main_theorem (x : ℝ) : Real.cos x ≤ 1 ∧ volume (Set.univ : Set ℝ) = ⊤ := by
  exact ⟨cos_le_one x, sorry⟩

lemma helper : True := trivial

end Demo
"""
OTHER = """import Mathlib.Combinatorics.SimpleGraph.Basic
import Demo.Main

open SimpleGraph

-- `Real.pi` in a comment is not a use
def Extra.count (G : SimpleGraph ℕ) : ℕ := 0

axiom Extra.choice : True
"""


def demo(tmp_path: Path, readme: str = "# Demo\n\nThe project proves `main_theorem`.\n", web: str | None = None,
         license_text: str = MIT) -> tuple[Path, list[str]]:
    write(tmp_path / "README.md", readme)
    write(tmp_path / "LICENSE", license_text)
    write(tmp_path / "lakefile.lean", LAKEFILE)
    write(tmp_path / "lean-toolchain", "leanprover/lean4:v4.25.0\n")
    write(tmp_path / "lake-manifest.json", json.dumps(MANIFEST))
    write(tmp_path / "src" / "Demo" / "Main.lean", MAIN)
    write(tmp_path / "src" / "Extra" / "Other.lean", OTHER)
    write(tmp_path / "Tool.lean", "def main : IO Unit := pure ()\n")
    if web is not None:
        write(tmp_path / "blueprint" / "src" / "web.tex", web)
    paths = sorted(path.relative_to(tmp_path).as_posix() for path in tmp_path.rglob("*") if path.is_file())
    return tmp_path, paths


HEADS = {"Real.cos", "MeasureTheory.volume", "Set.univ", "SimpleGraph", "Real.pi", "Real.cos_le_one", "Finset.sum"}


def test_a_project_record_reads_its_libraries_requirements_and_uses(tmp_path):
    checkout, paths = demo(tmp_path)
    project = {"repo": "ada/demo", "slug": "ada--demo", "kind": "research-project"}
    record = satellites.read_project(checkout, project, REV, "2026-11-01T00:00:00Z", paths, HEADS, {"Other.thing"})
    assert record["admitted"] and record["folder"] == ""
    assert record["libraries"] == [{"name": "Demo", "src": "src"}, {"name": "Extra", "src": "src"}]
    assert record["library_files"] == 2 and record["lean_files"] == 3
    assert record["mathlib"] == MATHLIB_REV
    assert [package["name"] for package in record["requirements"]] == ["PrimeNumberTheoremAnd"]
    assert record["mathlib_imports"] == {"Mathlib.Analysis.Fourier.AddCircle": 1, "Mathlib.Combinatorics.SimpleGraph.Basic": 1,
                                         "Mathlib.MeasureTheory.Integral.Bochner": 1}
    # Its own modules are not counted among the packages it imports.
    assert record["import_roots"] == {"Mathlib": 2, "PrimeNumberTheoremAnd": 1}
    assert (record["sorry_files"], record["axioms"]) == (1, 1)
    # The headline's file imports no file of the project; the axiom is in another file.
    assert (record["closure_files"], record["closure_sorry"], record["closure_axioms"]) == (1, ["src/Demo/Main.lean"], 0)
    # Names written in full or after an open namespace; not in comments or docstrings.
    assert record["uses"] == {"MeasureTheory.volume": 1, "Real.cos": 1, "Real.cos_le_one": 1, "Set.univ": 1,
                              "SimpleGraph": 1}
    assert record["headline_rule"] == "readme"
    head = record["headlines"][0]
    assert (head["name"], head["module"], head["line"], head["kind"], head["sorry"]) == (
        "Demo.main_theorem", "Demo.Main", 10, "theorem", True)
    assert head["names"] == ["MeasureTheory.volume", "Real.cos", "Set.univ"]
    assert record["readme"] == {"file": "README.md", "title": "Demo", "excerpt": "The project proves `main_theorem`."}
    assert record["license"]["spdx"] == "MIT"


def test_two_reads_at_the_same_commit_give_the_same_record(tmp_path):
    checkout, paths = demo(tmp_path)
    project = {"repo": "ada/demo", "slug": "ada--demo", "kind": "research-project"}
    first = satellites.read_project(checkout, project, REV, "2026-11-01T00:00:00Z", list(reversed(paths)), HEADS, set())
    second = satellites.read_project(checkout, project, REV, "2026-11-01T00:00:00Z", paths, HEADS, set())
    assert json.dumps(first, indent=1, ensure_ascii=False) == json.dumps(second, indent=1, ensure_ascii=False)


def test_an_unrecognized_license_keeps_the_readme_out_of_the_record(tmp_path):
    checkout, paths = demo(tmp_path, license_text=SPLIT)
    record = satellites.read_project(checkout, {"repo": "ada/demo", "slug": "ada--demo"}, REV, "2026-11-01T00:00:00Z",
                                     paths, HEADS, set())
    assert record["readme"]["excerpt"] is None and record["license"]["spdx"] is None


WEB = r"""\documentclass{report}
\usepackage{blueprint}
\begin{document}
\chapter{Main}
\begin{definition}\label{def:count}\lean{Extra.count}\leanok
A count.
\end{definition}
\begin{lemma}\label{lem:helper}\lean{Demo.helper}\leanok
A helper.
\end{lemma}
\begin{theorem}\label{thm:main}\lean{Demo.main_theorem, Mathlib.Not.Here}\leanok\uses{def:count}
The main theorem.
\end{theorem}
\begin{proof}\uses{lem:helper}\leanok Easy.\end{proof}
\begin{theorem}\label{thm:open}\lean{Demo.unfinished}
Not formalized.
\end{theorem}
\end{document}
"""


def test_headlines_come_from_the_blueprint_then_the_readme_then_a_main_module(tmp_path):
    checkout, paths = demo(tmp_path / "a", web=WEB)
    record = satellites.read_project(checkout, {"repo": "a/a", "slug": "a"}, REV, "2026-11-01T00:00:00Z", paths, HEADS, set())
    # Nothing uses thm:main; the helper and the definition are used, the open theorem not \leanok.
    assert (record["headline_rule"], [head["name"] for head in record["headlines"]]) == ("blueprint", ["Demo.main_theorem"])
    checkout, paths = demo(tmp_path / "b")
    record = satellites.read_project(checkout, {"repo": "b/b", "slug": "b"}, REV, "2026-11-01T00:00:00Z", paths, HEADS, set())
    assert record["headline_rule"] == "readme"
    checkout, paths = demo(tmp_path / "c", readme="# C\n\nSee `lake build`.\n")
    record = satellites.read_project(checkout, {"repo": "c/c", "slug": "c"}, REV, "2026-11-01T00:00:00Z", paths, HEADS, set())
    # Demo/Main.lean is a module named Main: its theorems and lemmas, in order.
    assert (record["headline_rule"], [head["name"] for head in record["headlines"]]) == (
        "main", ["Demo.main_theorem", "Demo.helper"])


def test_a_project_without_a_lakefile_is_not_admitted(tmp_path):
    write(tmp_path / "leanpkg.toml", "[package]\n")
    write(tmp_path / "src" / "a.lean", "theorem x : true := trivial\n")
    record = satellites.read_project(tmp_path, {"repo": "o/r", "slug": "o--r"}, REV, "2026-11-01T00:00:00Z",
                                     ["leanpkg.toml", "src/a.lean"], set(), set())
    assert (record["admitted"], record["reason"]) == (False, "a Lean 3 project: leanpkg.toml and no lakefile")


def test_a_nested_lake_project_is_found_with_its_manifest():
    paths = ["README.md", "lean/lakefile.toml", "lean/lake-manifest.json", "tools/x/lakefile.lean", "deep/a/lakefile.lean"]
    assert satellites.project_dir(paths) == "lean"
    assert satellites.project_dir(["lakefile.toml", "lean/lakefile.toml"]) == ""
    assert satellites.project_dir(["README.md"]) is None


# The chapter.

def concept(title: str, slug: str, module: str) -> Leaf:
    return Leaf(title, slug, [("declaration", "theorem"), ("mathlib_declaration", title), ("mathlib_file",
                module.replace(".", "/") + ".lean")], "body")


def mathlib_fixture(vault: Path) -> tuple[Container, dict[str, Container], dict[str, Leaf]]:
    cos = concept("Real.cos", "cos", "Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic")
    volume = concept("MeasureTheory.volume", "volume", "Mathlib.MeasureTheory.Measure.Lebesgue.Basic")
    graph = concept("SimpleGraph", "simple-graph", "Mathlib.Combinatorics.SimpleGraph.Basic")
    fourier = concept("fourierCoeff", "fourier", "Mathlib.Analysis.Fourier.AddCircle")
    sub = Container("Special functions", "special-functions", [Entry(cos), Entry(fourier)])
    analysis = Container("Analysis", "analysis", [Entry(sub), Entry(volume)])
    combinatorics = Container("Combinatorics", "combinatorics", [Entry(graph)])
    overview = Container("Overview", "overview", [Entry(analysis), Entry(combinatorics)])
    root = Container("Mathlib", "mathlib", [Entry(overview)], prose="One article per concept.")
    assign_paths(root, vault / "roadmap" / "mathlib")
    heads = {leaf.title: leaf for leaf in (cos, volume, graph, fourier)}
    hosts = {"mathlib:analysis": analysis, "mathlib:combinatorics": combinatorics, satellites.OVERVIEW: overview}
    return root, hosts, heads


def record(slug: str, **changes) -> dict:
    base = {"schema": satellites.SCHEMA, "repo": f"o/{slug}", "slug": slug, "rev": REV, "date": "2026-11-01T00:00:00Z",
            "admitted": True, "kind": "research-project", "folder": "", "toolchain": "v4.25.0", "mathlib": MATHLIB_REV,
            "requirements": [], "libraries": [{"name": "X", "src": "."}], "library_files": 10,
            "capped": False, "lean_files": 10, "declarations": 50, "sorry_files": 0, "axioms": 0, "unclosed_files": 0,
            "closure_files": 3, "closure_sorry": [], "closure_axioms": 0,
            "root_modules": [], "root_closure_files": 0, "root_closure_sorry": [], "root_closure_axioms": 0,
            "license": {"files": ["LICENSE"], "spdx": "Apache-2.0", "file": "LICENSE", "copyright": []},
            "readme": {"file": "README.md", "title": slug.title(), "excerpt": "It proves a theorem."},
            "headline_rule": "readme", "headline_count": 1,
            "headlines": [{"name": f"{slug}.main", "module": "X.Main", "file": "X/Main.lean", "line": 3,
                           "kind": "theorem", "sorry": False, "names": []}],
            "mathlib_imports": {}, "import_roots": {"Mathlib": 3}, "uses": {}, "ci": "SUCCESS"}
    return base | changes


LIBRARIES = [{"id": "mathlib", "repo": "leanprover-community/mathlib4", "map_status": "live"},
             {"id": "pnt-plus", "repo": "AlexKontorovich/PrimeNumberTheoremAnd", "map_status": "live"},
             {"id": "cslib", "repo": "leanprover/cslib", "map_status": "planned"}]


def placements(records, vault, overrides=None, packages=None, hosts_extra=None):
    root, hosts, heads = mathlib_fixture(vault)
    hosts |= hosts_extra or {}
    pages, stats, _ = satellites.chapter(records, packages or {}, overrides or {}, LIBRARIES, hosts, heads, {})
    placed = {}
    for host, projects, _ in pages:
        for node in walk(projects):
            if isinstance(node, Leaf):
                placed[node.slug] = (host.title, node)
        for line in projects.tail.split("\n"):
            if line.startswith("- ["):
                placed[line.split("[")[1].split("]")[0].split("/")[1]] = (host.title, None)
    return placed, stats


def test_home_takes_an_override_then_a_live_chapter_then_mathlibs_areas(tmp_path):
    pnt = Container("PNT+", "pnt-plus")
    pnt.path = tmp_path / "roadmap" / "pnt-plus" / "README.md"
    fork = {"name": "PrimeNumberTheoremAnd", "url": "https://github.com/kimihiro64/PrimeNumberTheoremAnd.git", "rev": "2" * 40}
    planned = {"name": "cslib", "url": "https://github.com/leanprover/cslib", "rev": "4" * 40}
    records = [
        record("override", requirements=[fork]),
        record("live", requirements=[fork, planned], import_roots={"Mathlib": 3, "PrimeNumberTheoremAnd": 2}),
        # (a) the areas of the concepts its headline statements name
        record("statement", headlines=[record("x")["headlines"][0] | {"names": ["SimpleGraph", "Real.cos", "fourierCoeff"]}],
               mathlib_imports={"Mathlib.Combinatorics.SimpleGraph.Basic": 9}),
        # (b) the area of its imports with the highest lift
        record("imports", mathlib_imports={"Mathlib.Combinatorics.SimpleGraph.Basic": 2,
                                           "Mathlib.Analysis.Fourier.AddCircle": 8}),
        record("imports-2", mathlib_imports={"Mathlib.Combinatorics.SimpleGraph.Basic": 7,
                                             "Mathlib.Analysis.Fourier.AddCircle": 3}),
        # (c) the areas of the concepts its files name
        record("uses", uses={"SimpleGraph": 4}),
        record("nothing"),
        record("core", mathlib="", import_roots={"Batteries": 4}),
    ]
    overrides = {"o/override": {"repo": "o/override", "home": "mathlib:combinatorics", "reason": "Graphs."}}
    packages = {"kimihiro64/primenumbertheoremand": {"chapter": "pnt-plus", "reason": "a GitHub fork of PNT+"}}
    placed, stats = placements(records, tmp_path, overrides, packages, {"pnt-plus": pnt})
    assert {slug: host for slug, (host, _) in placed.items()} == {
        "override": "Combinatorics", "live": "PNT+", "statement": "Analysis", "imports": "Analysis",
        "imports-2": "Combinatorics", "uses": "Combinatorics", "nothing": "Overview"}
    assert stats["held_back"] == 1
    notes = {slug: dict(leaf.notes)["Placement"] for slug, (_, leaf) in placed.items()}
    assert notes["override"] == "Placed by hand. Graphs."
    assert notes["live"] == ("Its Lake manifest requires `PrimeNumberTheoremAnd`, a GitHub fork of PNT+, whose modules "
                             "2 files of the project import.")
    assert notes["statement"] == "2 of the 3 Mathlib concepts its headline statements name are in Analysis."
    assert notes["imports"].startswith("Of its imports of Mathlib modules in an overview area, 8 of 10 are in Analysis")


def test_proof_edges_are_the_concepts_named_most_relative_to_the_other_projects_at_most_eight(tmp_path):
    names = [f"Concept{i}" for i in range(12)]
    root, hosts, heads = mathlib_fixture(tmp_path)
    for i, name in enumerate(names):
        leaf = concept(name, name.lower(), "Mathlib.Analysis.Fourier.AddCircle")
        hosts["mathlib:analysis"].entries.append(Entry(leaf))
        heads[name] = leaf
    assign_paths(root, tmp_path / "roadmap" / "mathlib")
    # Concept0 is named by every file of every project: the lowest lift. Concept11 only here: the highest.
    mine = {name: 10 - min(i, 9) for i, name in enumerate(names)} | {"Concept11": 2}
    others = [record(f"other{i}", uses={"Concept0": 10, "Concept1": 10}) for i in range(3)]
    ranked = satellites.use_lifts(record("mine", uses=mine), [record("mine", uses=mine), *others])
    assert ranked[0][0] in ("Concept2", "Concept11") and ranked[-1][0] in ("Concept0", "Concept1")
    pages, _, _ = satellites.chapter([record("mine", uses=mine), *others], {}, {}, LIBRARIES, hosts, heads, {})
    card = next(node for _, projects, _ in pages for node in walk(projects) if isinstance(node, Leaf) and node.slug == "mine")
    assert len(card.proof_depends) == satellites.MAX_USES
    assert heads["Concept0"] not in card.proof_depends
    note = dict(card.notes)["Mathlib use"]
    assert "lists 8 of the 12 Mathlib overview articles whose Lean names its files write" in note
    assert "a name match, not an import" in note and "requires no Mathlib" not in note


def test_a_project_without_mathlib_keeps_only_the_concepts_lean_core_or_std_declares(tmp_path):
    root, hosts, heads = mathlib_fixture(tmp_path)
    modules = {"List": "Init.Prelude", "Std.HashMap": "Std.Data.HashMap.Basic", "Set": "Mathlib.Data.Set.Defs"}
    for name in modules:
        leaf = concept(name, name.lower().replace(".", "-"), "Mathlib.Analysis.Fourier.AddCircle")
        hosts["mathlib:analysis"].entries.append(Entry(leaf))
        heads[name] = leaf
    batteries = Container("Batteries", "batteries")
    batteries.path = tmp_path / "roadmap" / "batteries" / "README.md"
    hosts[satellites.CORE_HOME] = batteries
    assign_paths(root, tmp_path / "roadmap" / "mathlib")
    uses = {"List": 4, "Std.HashMap": 2, "Set": 1, "Unknown": 1}
    core = record("core", mathlib="", import_roots={"Lean": 2}, uses=uses)
    # A project on Mathlib keeps every concept it names, whatever declares it.
    on = record("on", uses=dict(uses))
    pages, stats, _ = satellites.chapter([core, on], {}, {}, LIBRARIES, hosts, heads, {}, modules)
    cards = {node.slug: node for _, projects, _ in pages for node in walk(projects) if isinstance(node, Leaf)}
    assert set(cards["core"].proof_depends) == {heads["List"], heads["Std.HashMap"]}
    assert heads["Set"] in cards["on"].proof_depends
    assert "It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept." in (
        dict(cards["core"].notes)["Mathlib use"])
    assert (stats["uses_dropped"], stats["uses_dropped_projects"]) == (2, 1)


def test_a_card_quotes_its_readme_only_under_a_recognized_license(tmp_path):
    unlicensed = record("closed", license={"files": [], "spdx": None, "file": None, "copyright": []},
                        readme={"file": "README.md", "title": "Closed", "excerpt": "Words."})
    placed, _ = placements([record("open"), unlicensed], tmp_path)
    assert "> It proves a theorem." in placed["open"][1].body
    assert "Apache-2.0" in placed["open"][1].body
    assert ">" not in placed["closed"][1].body and "Words" not in placed["closed"][1].body
    assert dict(placed["open"][1].fields)["proof"] == "formalized"
    stated = record("stated", sorry_files=2, closure_sorry=["X/Main.lean"])
    placed, _ = placements([stated], tmp_path)
    assert "proof" not in dict(placed["stated"][1].fields)


def test_a_project_without_a_headline_is_listed_on_its_homes_page(tmp_path):
    placed, stats = placements([record("card"), record("bare", headlines=[], headline_rule=None, headline_count=0)], tmp_path)
    assert placed["bare"] == ("Overview", None) and stats["without_headline"] == 1


def test_the_host_lists_its_projects_page_without_owning_it_so_links_never_see_it(tmp_path):
    root, hosts, heads = mathlib_fixture(tmp_path)
    vault = tmp_path
    before = render_tree(root, vault, annotated=True)
    rows_before = links.files(root, vault / "links" / "mathlib", MATHLIB_REV)
    statement = record("graphs", mathlib_imports={"Mathlib.Combinatorics.SimpleGraph.Basic": 3})
    pages, _, _ = satellites.chapter([statement], {}, {}, LIBRARIES, hosts, heads, {})
    for host, projects, _ in pages:
        assign_paths(projects, host.path.parent / "projects")
        satellites.attach(host, projects)
    after = render_tree(root, vault, annotated=True)
    assert links.files(root, vault / "links" / "mathlib", MATHLIB_REV) == rows_before
    assert set(after) == set(before)
    changed = [path for path in before if before[path] != after[path]]
    assert [path.relative_to(vault).as_posix() for path in changed] == ["roadmap/mathlib/overview/combinatorics/README.md"]
    old, new = before[changed[0]].split("\n"), after[changed[0]].split("\n")
    assert [line for line in new if line not in old] == ["- [Projects building on Combinatorics (1)](projects/README.md)"]
    assert [line for line in old if line not in new] == []
    page = render_container(pages[0][1], vault, None)
    assert "graphs.md" in "\n".join(path.name for path in render_tree(pages[0][1], vault))
    assert page.startswith("# Projects building on Combinatorics (1)")


def test_the_committed_records_build_the_chapter():
    records, packages, overrides = satellites.load(ROOT / "data")
    if not records:
        pytest.skip("no satellite records committed yet")
    for item in records:
        assert item["schema"] == satellites.SCHEMA
        assert item["slug"] in {project["slug"] for project in satellites.load_projects(ROOT / "data" / "satellites" / "projects.toml")}
        if item["readme"].get("excerpt"):
            assert item["license"]["spdx"]
    assert Counter(override["home"].split(":")[0] for override in overrides.values())


def test_only_a_top_level_main_module_names_headlines(tmp_path):
    def declared(module: str, kind: str = "theorem") -> tuple:
        return (module.replace(".", "/") + ".lean", module, satellites.leansource.Declaration("x", kind, 1, False))
    nested = {"A.Sub.Main.t": declared("A.Sub.Main")}
    assert satellites.headlines(tmp_path, [], [""], nested) == (None, [], 0)
    top = nested | {"A.Main.t": declared("A.Main"), "A.Main.d": declared("A.Main", "def")}
    assert satellites.headlines(tmp_path, [], [""], top) == ("main", ["A.Main.t"], 1)


def test_a_project_with_a_chapter_of_its_own_is_left_out(tmp_path):
    placed, stats = placements([record("card"), record("chapter", repo="AlexKontorovich/PrimeNumberTheoremAnd")], tmp_path)
    assert "chapter" not in placed and stats["covered"] == 1


def test_a_requirement_on_another_project_links_its_card_or_its_listing_or_names_it(tmp_path):
    def needs(*repos):
        return [{"name": repo.split("/")[1], "url": f"https://github.com/{repo}", "rev": REV} for repo in repos]
    records = [record("user", requirements=needs("o/carded", "o/bare", "o/lean3", "o/alone")), record("carded"),
               record("alone", mathlib=None, import_roots={}),
               record("bare", headlines=[], headline_rule=None, headline_count=0),
               record("lean3", admitted=False, reason="no lakefile")]
    root, hosts, heads = mathlib_fixture(tmp_path)
    pages, _, targets = satellites.chapter(records, {}, {}, LIBRARIES, hosts, heads, {})
    user = next(node for _, projects, _ in pages for node in walk(projects) if node.slug == "user")
    builds = dict(user.notes)["Builds on"]
    assert "(trough:satellite:carded)" in builds and "(trough:satellite:bare)" in builds
    assert "`lean3`" in builds and "satellite:lean3" not in builds
    assert "`alone`" in builds and "satellite:alone" not in builds and "satellite:alone" not in targets
    assert isinstance(targets["satellite:carded"], Leaf) and isinstance(targets["satellite:bare"], Container)
    assert targets["satellite:carded"] in user.depends


def test_a_quoted_readme_links_relative_paths_and_its_own_headings_to_the_repository_at_its_commit():
    item = record("q", readme={"file": "docs/README.md", "title": "Q", "excerpt": ""})
    text = 'See [the paper](../paper/p.pdf), [site](https://x.org), [here](#use) and <img src="fig.png">.'
    assert satellites.absolute(item, text) == (
        f"See [the paper](https://github.com/o/q/blob/{REV}/paper/p.pdf), [site](https://x.org), "
        f"[here](https://github.com/o/q/blob/{REV}/docs/README.md#use) and "
        f'<img src="https://github.com/o/q/blob/{REV}/docs/fig.png">.')


def test_a_record_reads_its_libraries_root_modules_and_what_they_import(tmp_path):
    checkout, _ = demo(tmp_path)
    write(tmp_path / "src" / "Demo.lean", "import Demo.Main\n")
    paths = sorted(path.relative_to(tmp_path).as_posix() for path in tmp_path.rglob("*") if path.is_file())
    project = {"repo": "ada/demo", "slug": "ada--demo", "kind": "research-project"}
    record_ = satellites.read_project(checkout, project, REV, "2026-11-01T00:00:00Z", paths, HEADS, set())
    # Extra's glob root names no file of its own, so only Demo is a root module read here.
    assert record_["root_modules"] == [{"name": "Demo", "file": "src/Demo.lean"}]
    assert (record_["root_closure_files"], record_["root_closure_sorry"], record_["root_closure_axioms"]) == (
        2, ["src/Demo/Main.lean"], 0)


def roots(*names: str) -> list[dict]:
    return [{"name": name, "file": f"{name}.lean"} for name in names]


def test_a_project_without_a_headline_gets_a_card_for_its_own_root_modules(tmp_path):
    bare = dict(headlines=[], headline_rule=None, headline_count=0, root_closure_files=4)
    records = [record("card"),
               record("node", root_modules=roots("Challenge", "Node", "Node2", "Node3", "Node4"), **bare),
               record("shared", root_modules=roots("Challenge"), **bare),
               record("stated", root_modules=roots("Stated"), **bare | {"root_closure_sorry": ["Stated/A.lean"]})]
    placed, stats = placements(records, tmp_path)
    node = placed["node"][1]
    fields = dict(node.fields)
    # Challenge is a root of two projects, so it names neither; at most three roots are named.
    assert (fields["declaration"], fields["lean"], fields["statement"], fields["proof"]) == (
        "module", "Node, Node2, Node3", "formalized", "formalized")
    note = dict(node.notes)["Root modules"]
    assert "stands for its root modules" in note and "not a theorem" in note and "(4 files)" in note
    assert placed["shared"] == ("Overview", None)
    assert "proof" not in dict(placed["stated"][1].fields)
    assert "`Stated/A.lean` holds `sorry`" in dict(placed["stated"][1].notes)["Root modules"]
    assert (stats["module_nodes"], stats["module_proved"], stats["listed"], stats["without_headline"]) == (2, 1, 1, 3)


def test_a_long_or_generic_readme_title_gives_way_to_the_repository_name(tmp_path):
    long = "A computer-assisted counterexample to the planar Pompeiu and Schiffer conjectures"
    records = [record("long", readme={"file": "README.md", "title": long, "excerpt": None}),
               record("generic", readme={"file": "README.md", "title": "License", "excerpt": None}),
               record("plain", readme={"file": "README.md", "title": "Plain words", "excerpt": None})]
    placed, _ = placements(records, tmp_path)
    assert placed["long"][1].title == "long" and placed["long"][1].body.startswith(f"*{long}*\n\n")
    assert placed["generic"][1].title == "generic" and not placed["generic"][1].body.startswith("*")
    assert placed["plain"][1].title == "Plain words"


def test_a_project_on_neither_mathlib_nor_a_mapped_library_goes_to_the_batteries_chapter(tmp_path):
    batteries = Container("Batteries", "batteries")
    batteries.path = tmp_path / "roadmap" / "batteries" / "README.md"
    records = [record("std", mathlib="", import_roots={"Batteries": 4, "Lean": 2}),
               record("core", mathlib="", import_roots={"Lean": 2}),
               record("packages", mathlib="", import_roots={"Iris": 3},
                      requirements=[{"name": "iris", "url": "https://github.com/x/iris", "rev": ""}])]
    placed, stats = placements(records, tmp_path, hosts_extra={"batteries": batteries})
    notes = {slug: dict(leaf.notes)["Placement"] for slug, (host, leaf) in placed.items() if host == "Batteries"}
    assert notes["std"] == ("It requires neither Mathlib nor another library mapped here; 4 files of the project "
                            "import Batteries modules.")
    assert notes["core"].endswith("imports no Batteries module: it builds on Lean core alone.")
    assert notes["packages"].endswith("it builds on Lean core and packages not mapped here.")
    assert stats["held_back"] == 0
