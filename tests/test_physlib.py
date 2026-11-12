import json
import os
import subprocess
from pathlib import Path

import pytest

import refresh_physlib
from trough import blueprints
from trough import physlib
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "a" * 40
BLOB = f"https://github.com/leanprover-community/physlib/blob/{REV}"

# Shaped like Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean.
OSCILLATOR = """/-
Copyright (c) 2025 Joseph Tooby-Smith. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Joseph Tooby-Smith
-/
module

public import Physlib.SpaceAndTime.Time.Basic
/-!

# The Classical Harmonic Oscillator

## i. Overview

The classical harmonic oscillator is a mass `m` under a force `- k x`.

A TODO below discusses the geometric model.

## ii. Key results

- `HarmonicOscillator` contains the input data.
- `energy_conservation` proves that energy is conserved.

## iii. Table of contents

- A. The input data
- B. Energy

## iv. References

* Landau & Lifshitz, Mechanics, page 58.
-/

@[expose] public section

namespace ClassicalMechanics

TODO "Model the configuration space as a manifold."

/-!

## A. The input data

The input data are the mass and the spring constant.

-/

/-- The harmonic oscillator, given by a mass `m` and a spring constant `k`. -/
structure HarmonicOscillator where
  /-- The mass. -/
  m : ℝ
  k : ℝ

namespace HarmonicOscillator

variable (S : HarmonicOscillator)

@[simp]
lemma k_ne_zero (h : S.k ≠ 0) : S.k ≠ 0 := h

instance : Inhabited HarmonicOscillator := ⟨⟨1, 1⟩⟩

private lemma helper : True := trivial

/-!

## B. Energy

### B.1. Conservation

-/

/-- Energy is conserved.

TODO: extend this to the damped oscillator. -/
theorem energy_conservation (t : ℝ) : S.m = S.m := by
  rfl

end HarmonicOscillator

end ClassicalMechanics
"""

TIME = """module

/-!
# Time

An instant of time is a real number. Its units are in [`Units.lean`](Deep/Units.lean); see also
[the README](../../../README.md) and [a_b](https://example.org/a_b).
-/

@[expose] public section

/-- An instant of time. -/
structure Time where
  val : ℝ

namespace Time

lemma vadd_val (r : ℝ) (t : Time) : r + t.val = t.val + r := by
  ring

end Time
"""

UNITS = """module

public import Physlib.SpaceAndTime.Time.Basic

/-!
# Units of time
-/

@[expose] public section

/-- A choice of time unit. -/
def TimeUnit : Type := { x : ℝ // 0 < x }
"""

GEOMETRIC = """module

public import Physlib.ClassicalMechanics.HarmonicOscillator.Basic

/-!
# The geometric oscillator
-/

@[expose] public section

namespace ClassicalMechanics

/-- The configuration space. -/
abbrev ConfigurationSpace : Type := ℝ

end ClassicalMechanics
"""

# A placeholder, as Physlib/Cosmology/Basic.lean is: no declaration, so no article.
PLACEHOLDER = """module

/-!

# Cosmology

This directory is currently a place holder.

-/
"""

# Shaped like QuantumInfo/States/Pure/Braket.lean, whose `end section` closes a section and opens another.
BRAKET = """module

@[expose] public section

noncomputable section

section
variable (d : Type*)
end section

namespace Braket

theorem dot_self_eq_one : (1 : ℕ) = 1 := rfl

end Braket
"""

ALPHA = """module

/-!
# PhyslibAlpha

The root of PhyslibAlpha.
-/

/-- A placeholder definition. -/
def PhyslibAlpha.version : ℕ := 1
"""

API_MAP = """# Time

## Abstract (Alpha)

An instant of time is a real number, and time carries a translation action.

## Content (Alpha)

### Instants

An instant of time is a single real number. [1] Instants form an affine space. [2] Time carries an action
of the translation group. [TODO]

### Distributions

Distributions from time are differentiable. [TODO]

### Units

A choice of time unit is a positive real number, see {1}. [3]

## Lean References

1. Physlib/SpaceAndTime/Time/Basic.lean — `Time`
2. Physlib/SpaceAndTime/Time/Basic.lean — `VAdd ℝ Time`,
   `vadd_val`
3. Physlib/SpaceAndTime/Time/Deep/Units.lean — `TimeUnit`

## References

1. Lorentz tensors API map — Physlib/Relativity/Tensors/API-map.md
"""

GEOMETRIC_MAP = """# Geometric oscillator

## Abstract (Alpha)

The oscillator on a manifold.

## Content (Alpha)

The configuration space is the real line. [1]

## Lean References

1. Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean — `ConfigurationSpace`

## References

1. Time API map — Physlib/SpaceAndTime/Time/API-map.md
"""

THEOREMS = """-- WARNING: only add a result to this file if it is a significant result in physics.

[Physlib]
ClassicalMechanics.HarmonicOscillator.energy_conservation

[QuantumInfo]
Braket.dot_self_eq_one
Ket.not_declared

[PhyslibAlpha]
"""

README = """
<div align="center">

## An open-source, community, project to digitalize results from physics into Lean 4

</div>

<table>
<tr>
<td width="33%" valign="top">

### [**Physlib**](./Physlib)

The core library — physics digitalizations reviewed and curated to a high standard.

</td>
<td width="33%" valign="top">

###  [**PhyslibAlpha**](./PhyslibAlpha)

PhyslibAlpha exists for the rapid development of physics digitalizations,
enabled by a lighter review process.

</td>
<td width="33%" valign="top">

### [**QuantumInfo**](./QuantumInfo)

Quantum information theory. Currently a distinct codebase with its own conventions and review norms; work is
underway to bring it closer to Physlib.

</td>
</tr>
</table>

## PhyslibAlpha

PhyslibAlpha sits downstream of `./Physlib` (within the same repository). The core idea is that PhyslibAlpha has
lower review-standards than Physlib.

Because of the lower-review bar for PhyslibAlpha we cannot promise to maintain contributions when they break.

## Maintainers

Below are the maintainers of the project.

- Léo Lessa (@Megaleo)
- Joseph Tooby-Smith (@jstoobysmith)

## Citing the project

Physlib was formed by merging the general physics Lean library PhysLean (formerly called HepLean)
with the quantum-information library Lean-QuantumInfo. Where appropriate please also consider
citing the papers associated with the origin of these projects. For the former please use:
```bibtex
@article{Tooby-Smith:2024vqu,
}
```
"""

MANIFEST = {"packages": [{"name": "mathlib", "rev": "b" * 40, "inputRev": "v4.35.0"}]}
APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"
FILES = {
    "Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean": OSCILLATOR,
    "Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean": GEOMETRIC,
    "Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/API-map.md": GEOMETRIC_MAP,
    "Physlib/SpaceAndTime/Time/Basic.lean": TIME,
    "Physlib/SpaceAndTime/Time/Deep/Units.lean": UNITS,
    "Physlib/SpaceAndTime/Time/API-map.md": API_MAP,
    "Physlib/Cosmology/Basic.lean": PLACEHOLDER,
    "PhyslibAlpha/Basic.lean": ALPHA,
    "QuantumInfo/States/Pure/Braket.lean": BRAKET,
    "scripts/lint/exemptions/Theorems.txt": THEOREMS,
    "Physlib.lean": "module\n\npublic import Physlib.SpaceAndTime.Time.Basic\n",
}


def line_of(text: str, words: str) -> int:
    return text[:text.index(words)].count("\n") + 1


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-11T17:08:33+01:00",
           "GIT_COMMITTER_DATE": "2026-11-11T17:08:33+01:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path, files: dict[str, str] = FILES, license_text: str = APACHE, readme: str = README) -> Path:
    every = files | {"LICENSE": license_text, "README.md": readme, "lean-toolchain": "leanprover/lean4:v4.35.0\n",
                     "lake-manifest.json": json.dumps(MANIFEST)}
    for path, text in every.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "Initial commit")
    return root


def test_a_module_keeps_its_docstrings_and_its_declarations_in_file_order():
    record = physlib.read_module(OSCILLATOR, "Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean")
    assert record["module"] == "Physlib.ClassicalMechanics.HarmonicOscillator.Basic"
    assert record["title"] == "The Classical Harmonic Oscillator"
    assert record["doc"].startswith("## i. Overview\n\nThe classical harmonic oscillator is a mass `m`")
    assert [(section["line"], section["text"].split("\n")[0]) for section in record["sections"]] == [
        (line_of(OSCILLATOR, "/-!\n\n## A."), "## A. The input data"), (line_of(OSCILLATOR, "/-!\n\n## B."), "## B. Energy")]
    rows = [(item["name"], item["kind"], item["line"], item["sorry"]) for item in record["declarations"]]
    assert rows == [
        ("ClassicalMechanics.HarmonicOscillator", "structure", line_of(OSCILLATOR, "structure Harmonic"), False),
        ("ClassicalMechanics.HarmonicOscillator.k_ne_zero", "lemma", line_of(OSCILLATOR, "lemma k_ne_zero"), False),
        ("", "instance", line_of(OSCILLATOR, "instance : Inhabited"), False),
        ("ClassicalMechanics.HarmonicOscillator.energy_conservation", "theorem",
         line_of(OSCILLATOR, "theorem energy_conservation"), False)]
    structure, lemma, instance, theorem = record["declarations"]
    assert structure["doc"] == "The harmonic oscillator, given by a mass `m` and a spring constant `k`."
    # A structure keeps its whole text, its fields.
    assert structure["statement"] == "structure HarmonicOscillator where\n  /-- The mass. -/\n  m : ℝ\n  k : ℝ"
    assert lemma["doc"] == "" and lemma["statement"] == "lemma k_ne_zero (h : S.k ≠ 0) : S.k ≠ 0"
    assert instance["statement"] == "instance : Inhabited HarmonicOscillator"
    assert theorem["doc"] == "Energy is conserved.\n\nTODO: extend this to the damped oscillator."
    # The private lemma is counted, not kept.
    assert record["private"] == 1
    assert physlib.read_module("namespace A\nend B\n", "Physlib/X.lean") is None


def test_end_section_closes_a_section_and_opens_another():
    record = physlib.read_module(BRAKET, "QuantumInfo/States/Pure/Braket.lean")
    assert [item["name"] for item in record["declarations"]] == ["Braket.dot_self_eq_one"]


def test_a_docstring_shows_its_headings_and_quotes_its_prose_without_its_contents_or_todos():
    record = physlib.read_module(OSCILLATOR, "Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean")
    assert physlib.doc_markdown(record["doc"]) == [
        "## i. Overview",
        "> The classical harmonic oscillator is a mass `m` under a force `- k x`.\n>\n> …",
        "## ii. Key results",
        "> - `HarmonicOscillator` contains the input data.\n> - `energy_conservation` proves that energy is conserved.",
        "## iv. References",
        "> * Landau & Lifshitz, Mechanics, page 58.",
    ]
    assert physlib.doc_markdown("## TODO\n\nWrite more.\n\n## Done\n\nDone.") == ["…", "## Done", "> Done."]


def test_what_mentions_a_todo_is_cut_and_marked():
    assert physlib.without_todos("Keep this.\n\n- one\n- TODO two\n- three\n\nTODO para\n\nTODO again\n\nEnd.") == (
        "Keep this.\n\n- one\n- three\n\n…\n\nEnd.")
    assert physlib.without_todos("TODO: everything.") == "…"


def test_an_api_map_reads_its_content_and_its_references():
    record = physlib.read_api_map(API_MAP, "Physlib/SpaceAndTime/Time/API-map.md")
    assert record["title"] == "Time" and record["folder"] == "Physlib/SpaceAndTime/Time"
    assert [section["heading"] for section in record["content"]] == ["Content (Alpha)"]
    assert record["lean"] == {
        "1": {"file": "Physlib/SpaceAndTime/Time/Basic.lean", "names": ["Time"]},
        "2": {"file": "Physlib/SpaceAndTime/Time/Basic.lean", "names": ["VAdd ℝ Time", "vadd_val"]},
        "3": {"file": "Physlib/SpaceAndTime/Time/Deep/Units.lean", "names": ["TimeUnit"]}}
    assert record["references"] == {"1": "Lorentz tensors API map — Physlib/Relativity/Tensors/API-map.md"}


def test_an_api_map_is_quoted_without_what_it_marks_todo():
    record = physlib.read_api_map(API_MAP, "Physlib/SpaceAndTime/Time/API-map.md")
    keys = {"Physlib/SpaceAndTime/Time/Basic.lean": "physlib-T"}
    prose = physlib.api_map_prose(record, {"repo": physlib.REPO, "rev": REV}, keys)
    assert "translation group" not in prose and "Distributions" not in prose and "Abstract" not in prose
    assert ("> An instant of time is a single real number. [\\[1\\]](trough:physlib-T) Instants form an affine space. "
            "[\\[2\\]](trough:physlib-T) …") in prose
    # A reference to a module with no article stays text.
    assert "> A choice of time unit is a positive real number, see \\{1}. \\[3\\]" in prose
    assert "> ### Instants" in prose and "> ### Units" in prose
    assert prose.endswith("> - \\{1\\} Lorentz tensors API map — Physlib/Relativity/Tensors/API-map.md")


def test_the_theorems_file_and_the_readme_read():
    assert physlib.read_theorems(THEOREMS) == {
        "Physlib": ["ClassicalMechanics.HarmonicOscillator.energy_conservation"],
        "QuantumInfo": ["Braket.dot_self_eq_one", "Ket.not_declared"], "PhyslibAlpha": []}
    readme = physlib.read_readme(README)
    assert readme["tagline"] == "An open-source, community, project to digitalize results from physics into Lean 4"
    assert readme["libraries"] == {
        "Physlib": "The core library — physics digitalizations reviewed and curated to a high standard.",
        "PhyslibAlpha": "PhyslibAlpha exists for the rapid development of physics digitalizations, enabled by a "
                        "lighter review process.",
        "QuantumInfo": "Quantum information theory. Currently a distinct codebase with its own conventions and review "
                       "norms; work is underway to bring it closer to Physlib."}
    assert readme["alpha"] == [
        "PhyslibAlpha sits downstream of `./Physlib` (within the same repository). The core idea is that PhyslibAlpha "
        "has lower review-standards than Physlib.",
        "Because of the lower-review bar for PhyslibAlpha we cannot promise to maintain contributions when they break."]
    assert readme["maintainers"] == ["Léo Lessa", "Joseph Tooby-Smith"]
    assert readme["formed"] == ("Physlib was formed by merging the general physics Lean library PhysLean (formerly "
                                "called HepLean) with the quantum-information library Lean-QuantumInfo.")


def test_edges_are_the_nearest_modules_with_an_article():
    deps = {"modules": {
        "A": {"statement": [], "proof": []},
        "B": {"statement": ["A"], "proof": []},
        # H has no article: what it uses counts as C's own.
        "H": {"statement": ["B"], "proof": []},
        "C": {"statement": ["A", "H"], "proof": ["B"]},
        "D": {"statement": [], "proof": ["C", "A"]},
    }}
    statement, proof = physlib.edges(deps, {"A", "B", "C", "D"})
    # C reaches A through B, so its only statement edge goes to B.
    assert statement == {"A": [], "B": ["A"], "C": ["B"], "D": []}
    # D's proof reaches A through C.
    assert proof == {"A": [], "B": [], "C": [], "D": ["C"]}


def test_the_refresh_writes_the_source_the_api_maps_and_the_modules(tmp_path):
    out = tmp_path / "out"
    repo = checkout(tmp_path / "physlib")
    assert refresh_physlib.refresh(repo, out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    # The commit date is written in UTC.
    assert {key: source[key] for key in ("repo", "rev", "date", "toolchain", "mathlib", "mathlib_version", "license")} == {
        "repo": physlib.REPO, "rev": git(repo, "rev-parse", "HEAD").strip(), "date": "2026-11-11T16:08:33Z",
        "toolchain": "v4.35.0", "mathlib": "b" * 40, "mathlib_version": "v4.35.0", "license": "Apache-2.0"}
    assert source["readme"]["maintainers"] == ["Léo Lessa", "Joseph Tooby-Smith"]
    assert source["theorems"]["Physlib"] == ["ClassicalMechanics.HarmonicOscillator.energy_conservation"]
    assert source["counts"]["files_Physlib"] == 5 and source["counts"]["private_Physlib"] == 1
    assert sorted(path.name for path in (out / "modules").iterdir()) == [
        "Physlib.ClassicalMechanics.json", "Physlib.Cosmology.json", "Physlib.SpaceAndTime.json", "PhyslibAlpha.json",
        "QuantumInfo.States.json"]
    shard = json.loads((out / "modules" / "Physlib.SpaceAndTime.json").read_text(encoding="utf-8"))
    assert shard["schema"] == physlib.SCHEMA and shard["rev"] == source["rev"]
    assert [module["file"] for module in shard["modules"]] == [
        "Physlib/SpaceAndTime/Time/Basic.lean", "Physlib/SpaceAndTime/Time/Deep/Units.lean"]
    maps = json.loads((out / "api-maps.json").read_text(encoding="utf-8"))["api_maps"]
    assert [item["file"] for item in maps] == ["Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/API-map.md",
                                               "Physlib/SpaceAndTime/Time/API-map.md"]
    # A later run drops the shard of an area that is gone.
    (out / "modules" / "Physlib.Gone.json").write_text(json.dumps({"modules": []}), encoding="utf-8")
    assert refresh_physlib.refresh(repo, out) == []
    assert not (out / "modules" / "Physlib.Gone.json").exists()


def test_the_refresh_writes_nothing_from_a_checkout_it_cannot_read_in_full(tmp_path):
    def refused(root: Path) -> list[str]:
        out = tmp_path / "out"
        problems = refresh_physlib.refresh(root, out)
        assert not out.exists()
        return problems

    assert refused(checkout(tmp_path / "mit", license_text="MIT License\n")) == [
        f"{physlib.REPO}: its LICENSE is not the Apache License 2.0"]
    broken = FILES | {"Physlib/Broken.lean": "namespace A\nend B\n"}
    assert refused(checkout(tmp_path / "broken", broken)) == ["Physlib/Broken.lean: its scopes do not close as they open"]
    gone = checkout(tmp_path / "gone")
    (gone / "Physlib/SpaceAndTime/Time/Basic.lean").unlink()
    assert refused(gone) == ["not checked out: Physlib/SpaceAndTime/Time/Basic.lean"]
    without = README.replace("### [**QuantumInfo**](./QuantumInfo)", "### QuantumInfo")
    assert refused(checkout(tmp_path / "readme", readme=without)) == [
        "README.md: no description of QuantumInfo in its table of libraries"]
    no_alpha = README.replace("## PhyslibAlpha\n", "## Alpha\n")
    assert refused(checkout(tmp_path / "alpha", readme=no_alpha)) == ["README.md: no PhyslibAlpha section"]


def test_the_refresh_refuses_a_record_that_reads_under_half_the_last_declarations(tmp_path):
    out = tmp_path / "out"
    (out / "modules").mkdir(parents=True)
    last = {"modules": [{"declarations": [{}] * 25}]}
    (out / "modules" / "Physlib.Old.json").write_text(json.dumps(last), encoding="utf-8")
    assert refresh_physlib.refresh(checkout(tmp_path / "physlib"), out) == [
        "reads 10 declarations, under half the 25 the last record read"]
    assert json.loads((out / "modules" / "Physlib.Old.json").read_text(encoding="utf-8")) == last
    assert not (out / "source.json").exists()


def data(tmp_path: Path, deps: dict | None = None) -> dict:
    out = tmp_path / "data" / "physlib"
    repo = checkout(tmp_path / "physlib")
    assert refresh_physlib.refresh(repo, out) == []
    if deps is not None:
        (out / "deps.json").write_text(json.dumps({"rev": git(repo, "rev-parse", "HEAD").strip(), **deps}), encoding="utf-8")
    loaded = physlib.load(tmp_path / "data")
    loaded["source"]["rev"] = REV
    if loaded["deps"]:
        loaded["deps"]["rev"] = REV
    return loaded


DEPS = {"modules": {
    "Physlib.SpaceAndTime.Time.Basic": {"statement": [], "proof": []},
    "Physlib.SpaceAndTime.Time.Deep.Units": {"statement": ["Physlib.SpaceAndTime.Time.Basic"], "proof": []},
    "Physlib.ClassicalMechanics.HarmonicOscillator.Basic": {
        "statement": ["Physlib.SpaceAndTime.Time.Basic", "Physlib.SpaceAndTime.Time.Deep.Units"], "proof": []},
    "Physlib.ClassicalMechanics.HarmonicOscillator.Geometric.Basic": {
        "statement": [], "proof": ["Physlib.ClassicalMechanics.HarmonicOscillator.Basic"]},
    "PhyslibAlpha.Basic": {"statement": [], "proof": []},
    "QuantumInfo.States.Pure.Braket": {"statement": [], "proof": []},
}, "missing": ["ClassicalMechanics.HarmonicOscillator.k_ne_zero"]}


def built(tmp_path: Path, deps: dict | None = DEPS):
    result, links = physlib.chapter(data(tmp_path, deps))
    vault = tmp_path / "vault"
    assign_paths(result.root, vault / "roadmap" / "physlib")
    blueprints.resolve(result, vault)
    pages = {path.relative_to(vault / "roadmap" / "physlib").as_posix(): text
             for path, text in render_tree(result.root, vault).items()}
    return result, links, pages


def test_the_chapter_has_a_part_per_library_and_a_page_per_folder(tmp_path):
    result, links, pages = built(tmp_path)
    assert [entry.node.title for entry in result.root.entries] == ["Physlib", "PhyslibAlpha", "QuantumInfo"]
    core = result.root.entries[0].node
    # Cosmology holds only a placeholder, so it has no page.
    assert [entry.node.title for entry in core.entries] == ["ClassicalMechanics", "SpaceAndTime"]
    mechanics = core.entries[0].node
    oscillator = mechanics.entries[0].node
    assert oscillator.title == "HarmonicOscillator"
    # The deeper folder with an API map has a page of its own.
    assert [entry.node.title for entry in oscillator.entries] == ["The Classical Harmonic Oscillator", "Geometric"]
    time = core.entries[1].node.entries[0].node
    # A deeper folder without one joins the page above, under a line naming it.
    assert [(entry.node.title, entry.before) for entry in time.entries] == [
        ("Time", ""), ("Units of time", f"Modules in [Deep/](https://github.com/{physlib.REPO}/tree/{REV}/"
                                         "Physlib/SpaceAndTime/Time/Deep):")]
    assert "The repository's API map for this folder, *Time*" in time.prose
    assert "[\\[1\\]](basic.md)" in time.prose
    assert result.stats["articles"] == 6 and result.stats["unshown"] == 1 and result.stats["pages"] == 7
    alpha = result.root.entries[1].node
    assert [entry.node.title for entry in alpha.entries] == ["PhyslibAlpha"]
    assert "The core library — physics digitalizations" in core.prose and f"commit [{REV[:8]}]" in core.prose
    # PhyslibAlpha's lighter review is quoted in the README's own words.
    assert "downstream of Physlib in the same repository" in alpha.prose
    assert "> Because of the lower-review bar for PhyslibAlpha we cannot promise" in alpha.prose
    quantum = result.root.entries[2].node
    assert "> Quantum information theory. Currently a distinct codebase with its own conventions and review norms; …" \
        in quantum.prose and "underway" not in quantum.prose
    assert "README.md" in pages and "physlib/README.md" in pages and "physlib/spaceandtime/time/basic.md" in pages


def test_an_article_shows_the_module_docstring_and_each_declaration_under_its_sections(tmp_path):
    result, links, pages = built(tmp_path)
    leaf = result.targets["physlib-Physlib.ClassicalMechanics.HarmonicOscillator.Basic"]
    assert isinstance(leaf, Leaf)
    # Every article has the same kind of front matter, whatever its module declares first.
    assert dict(leaf.fields) == {"declaration": "module", "origin": "cited", "statement": "formalized",
                                 "proof": "formalized",
                                 "lean": "ClassicalMechanics.HarmonicOscillator.energy_conservation, "
                                         "ClassicalMechanics.HarmonicOscillator"}
    body = leaf.body
    # k_ne_zero is read from the source but Lean does not have it, so it is left out.
    assert "k_ne_zero" not in body
    assert body.startswith(f"The module `Physlib.ClassicalMechanics.HarmonicOscillator.Basic`, "
                           f"[Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean]({BLOB}/Physlib/ClassicalMechanics/"
                           "HarmonicOscillator/Basic.lean): 3 declarations (1 instance with no name), 2 with a docstring, "
                           "1 listed as significant; 1 private, not shown.")
    assert "Table of contents" not in body and "TODO" not in body and "manifold" not in body
    order = ["## i. Overview", "## A. The input data", "**`ClassicalMechanics.HarmonicOscillator`**, a structure",
             "**An instance with no name**", "## B. Energy", "### B.1. Conservation",
             "**`ClassicalMechanics.HarmonicOscillator.energy_conservation`**, a theorem"]
    assert [body.index(text) for text in order] == sorted(body.index(text) for text in order)
    line = body[body.index("**`ClassicalMechanics.HarmonicOscillator.energy_conservation`**"):].split("\n")[0]
    assert line == (f"**`ClassicalMechanics.HarmonicOscillator.energy_conservation`**, a theorem, [line 76]({BLOB}/Physlib/"
                    "ClassicalMechanics/HarmonicOscillator/Basic.lean#L76). Listed as a significant result in "
                    f"[Theorems.txt]({BLOB}/scripts/lint/exemptions/Theorems.txt).")
    assert "> Energy is conserved.\n>\n> …" in body
    assert "```lean\ntheorem energy_conservation (t : ℝ) : S.m = S.m\n```" in body
    assert "```lean\nstructure HarmonicOscillator where\n  /-- The mass. -/\n  m : ℝ\n  k : ℝ\n```" in body
    assert links["ClassicalMechanics.HarmonicOscillator"] == f"{BLOB}/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L49"


def test_a_docstrings_links_to_the_repository_point_at_articles_or_the_pin(tmp_path):
    result, links, pages = built(tmp_path)
    body = pages["physlib/spaceandtime/time/basic.md"]
    assert "[`Units.lean`](deep-units.md)" in body
    assert f"[the README]({BLOB}/README.md)" in body
    # A link keeps its target whole, underscores and all.
    assert "[a\\_b](https://example.org/a_b)" in body
    geometric = pages["physlib/classicalmechanics/harmonicoscillator/geometric/README.md"]
    assert "> - \\{1\\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../../../spaceandtime/time/README.md)" in geometric


def test_edges_come_from_lean_and_without_it_there_are_none(tmp_path):
    result, links, pages = built(tmp_path)
    leaf = result.targets["physlib-Physlib.ClassicalMechanics.HarmonicOscillator.Basic"]
    assert [node.title for node in leaf.depends] == ["Units of time"]
    geometric = result.targets["physlib-Physlib.ClassicalMechanics.HarmonicOscillator.Geometric.Basic"]
    assert geometric.depends == [] and [node.title for node in geometric.proof_depends] == ["The Classical Harmonic Oscillator"]
    assert result.stats["statement_edges"] == 2 and result.stats["proof_edges"] == 1 and result.stats["unresolved"] == 1
    front = result.root.prose
    assert "That gives 2 statement edges and 1 proof edge." in front
    assert "is left out, 1 declaration at this commit." in front
    bare, _, _ = built(tmp_path / "bare", None)
    leaf = bare.targets["physlib-Physlib.ClassicalMechanics.HarmonicOscillator.Basic"]
    assert leaf.depends == [] and leaf.no_depends == physlib.NO_DEPENDS_UNREAD
    assert "No dependencies are recorded here" in bare.root.prose


def test_a_dump_of_another_commit_is_refused(tmp_path):
    loaded = data(tmp_path, DEPS)
    loaded["deps"]["rev"] = "c" * 40
    with pytest.raises(ValueError, match="deps.json reads cccccccc"):
        physlib.chapter(loaded)


def test_the_front_page_quotes_the_repository_and_says_how_the_map_is_read(tmp_path):
    result, links, pages = built(tmp_path)
    front = result.root.prose
    assert front.startswith(f"[Physlib](https://github.com/{physlib.REPO}) is, in its README's words, “An open-source, "
                            "community, project to digitalize results from physics into Lean 4”.")
    assert "maintainers: Léo Lessa and Joseph Tooby-Smith." in front
    assert ("6 articles, 4 in [Physlib](physlib/README.md), 1 in [PhyslibAlpha](physlibalpha/README.md) and 1 in "
            "[QuantumInfo](quantuminfo/README.md).") in front
    assert "1 module holds nothing else" in front
    assert "Lean toolchain v4.35.0, Mathlib v4.35.0, [bbbbbbbb]" in front
    assert "—" not in front


def test_the_committed_data_build_the_chapter():
    loaded = physlib.load(ROOT / "data")
    assert loaded is not None and loaded["source"]["repo"] == physlib.REPO and len(loaded["source"]["rev"]) == 40
    assert loaded["deps"] is not None and loaded["deps"]["rev"] == loaded["source"]["rev"]
    result, links = physlib.chapter(loaded)
    leaves = [node for node in walk(result.root) if isinstance(node, Leaf)]
    assert len(leaves) == result.stats["articles"] > 1000
    assert set(links) >= {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(dict(leaf.fields)["declaration"] == "module" for leaf in leaves)
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
