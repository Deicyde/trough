import json
import os
import subprocess
from collections import Counter
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

/-! TODO: the damped oscillator. -/

/-! TODO: the driven oscillator. -/

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

alias ⟨configuration_mp, configuration_mpr⟩ := Iff.rfl

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

# From QuantumInfo/Capacity/Capacity.lean's module docstring at the pin: a wish list, and a TODO note whose list and
# following paragraph go with it.
CAPACITY = """## ii. Key results

The most basic facts:
 * `emulates_self`: Every channel emulates itself.
 * `emulates_trans`: If A emulates B and B emulates C, then A emulates C. (That is, emulation
   is an ordering.)
 * `εApproximates A B ε` is equivalent to the existence of some δ (depending on ε and dims(A))
   so that |A-B| has diamond norm at most δ, and δ→0 as ε→0.
 * `achievesRate_0`: Every channel out of a nonempty space achievesRate 0. So, in that case,
   the set of achievable rates is Nonempty.
 * If a channel achievesRate R₁, it also achievesRate every R₂ ≤ R₁, i.e. it is an interval
   extending left towards -∞. Achievable rates are `¬BddBelow`.
 * `bddAbove_achievesRate`: A channel C : dimX → dimY cannot achievesRate R with
   `R > log2(min(dimX, dimY))`. Thus, the interval is `BddAbove`.

The nice lemmas we would want:
 * Capacity of a replacement channel is zero.
 * Capacity of an identity channel is `log2(D)`.
 * Capacity is superadditive under tensor products. (That is, at least additive. Showing that
   it isn't _exactly_ additive, unlike classical capacity which is additive, is a much harder
   task.)
 * Capacity of a kth tensor power is exactly k times the capacity of the original channel.
 * Capacity does not decrease under tensor sums.
 * Capacity does not increase under composition.

Then, we should show that our definition is equivalent to some above. Most, except (3), should
be not too hard to prove.

Then the LSD theorem establishes that the single-copy coherent information is a lower bound.
This is stated in `coherentInfo_le_quantumCapacity`. The corollary, that the n-copy coherent
information converges to the capacity, is `quantumCapacity_eq_piProd_coherentInfo`.

TODO: The only notion of "capacity" here currently is "quantum capacity" in the usual sense.
But there are several non-equal capacities relevant to quantum channels, see e.g. [Watrous's
notes](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf) for a list:
 * Quantum capacity (`quantumCapacity`)
 * Quantum 1-shot capacity
 * Entanglement-assisted classical capacity
 * Qss, the quantum side-channel capacity
 * Holevo capacity, aka Holevo χ. The Holevo–Schumacher–Westmoreland theorem as a major theorem
 * Entanglement-assisted Holevo capacity
 * Entanglement-assisted quantum capacity
 * One- and two-way distillable entanglement

And other important theorems like superdense coding, nonadditivity, superactivation.

## iii. Table of contents

- A. Basic definitions
- B. Emulation between channels
- C. Approximation between channels
- D. Achievable rates
- E. The quantum capacity"""

# From Physlib/Units/Basic.lean's module docstring: a mid-paragraph `TODO` that keeps the next paragraph.
UNITS_DOC = """The fundamental choices one has in physics are related to:
- Time
- Length
- Mass
- Charge
- Temperature

(In fact temperature is not really a fundamental choice, however we leave this as a `TODO`.)

From these fundamental choices one can construct all other units and dimensions."""

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
        (line_of(OSCILLATOR, "/-!\n\n## A."), "## A. The input data"), (line_of(OSCILLATOR, "/-!\n\n## B."), "## B. Energy"),
        (line_of(OSCILLATOR, "/-! TODO: the damped"), "TODO: the damped oscillator."),
        (line_of(OSCILLATOR, "/-! TODO: the driven"), "TODO: the driven oscillator.")]
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
    # The copyright line says whose code the file is; `TODO "..."` commands and informal results are counted.
    assert record["copyright"] == "2025 Joseph Tooby-Smith" and record["informal"] == 1
    # An `alias ⟨mp, mpr⟩` is not read, only counted.
    geometric = physlib.read_module(GEOMETRIC, "Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean")
    assert record["aliases"] == 0 and geometric["aliases"] == 1
    assert [item["name"] for item in geometric["declarations"]] == ["ClassicalMechanics.ConfigurationSpace"]
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
    # A paragraph that starts with a TODO note takes what follows it up to the next heading.
    assert physlib.without_todos("Keep this.\n\n- one\n- TODO two\n- three\n\nTODO para\n\nAnd more.\n\n## Next\n\nEnd.") == (
        "Keep this.\n\n- one\n- three\n\n…\n\n## Next\n\nEnd.")
    assert physlib.without_todos("TODO: everything.") == "…"
    # From PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean: TODOs count as a TODO.
    assert physlib.without_todos("The spectral statements are the TODOs of `Hydrogen.Basic`.") == "…"
    # A TODO cuts its sentence and the rest of its paragraph, and keeps the sentences before it
    # (Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean).
    assert physlib.without_todos(
        "The period is defined here, and the\n`TODO` after the definition lists the milestones. The rest follows.\n\n"
        "Next paragraph.") == "…\n\nNext paragraph."
    assert physlib.without_todos("Substitution of a term.\nTODO: substitution of a context. More.") == (
        "Substitution of a term.\n…")
    # After a semicolon, the cut starts at the clause (PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean).
    assert physlib.without_todos(
        "It holds away from the nucleus. It does not say that these are all eigenfunctions;\nthe spectral statements "
        "are the TODOs of `Hydrogen.Basic`.") == (
        "It holds away from the nucleus. It does not say that these are all eigenfunctions; …")
    # A sentence does not end at e.g.
    assert physlib.without_todos("Kept. See e.g. the TODO below.") == "Kept. …"


def test_sentences_about_plans_go_and_what_bounds_the_library_stays():
    # Physlib/Mathematics/ForMathlib/Trigonometry/SinSq.lean and Physlib/Optics/Polarization/Basic.lean.
    assert physlib.without_todos(
        "This file may eventually be upstreamed to Mathlib.\n\n## i. Overview\n\nThis file records the strict bound. "
        "It is used for the pendulum.") == (
        "…\n\n## i. Overview\n\nThis file records the strict bound. It is used for the pendulum.")
    assert physlib.without_todos(
        "The material moved to `HarmonicWave`.\nThis file is kept because there is still some material to be added "
        "here in the future. Contributions would be welcome.") == "The material moved to `HarmonicWave`.\n…"
    assert physlib.without_todos("- `a` : one.\n- `b` : planned for later.\n- `c` : three.") == (
        "- `a` : one.\n- `c` : three.\n\n…")
    # What says what the library does not have, or uses words of time, stays.
    for kept in ["Support in the future of one compact set is included in the full past-compact class.",
                 "The time of a solution of the nonlinear equation of motion is not yet formalized.",
                 "We state the constraints and leave the proof and derivation of these constraints to future work.",
                 "This file is a temporary copy of results intended for Mathlib.",
                 "Gauge fields live here, upstream of `MatterField`."]:
        assert physlib.without_todos(kept) == kept
    # A section on future work goes, under a numbered heading too (Physlib/ClassicalMechanics/Basic.lean); a section
    # on limitations stays.
    assert physlib.doc_markdown("## A.3. Future work\n\nShared declarations should be added here.\n\n"
                                "## A.4. Limitations\n\nOnly finite systems.") == [
        "…", "## A.4. Limitations", "> Only finite systems."]
    assert physlib.doc_markdown("## Roadmap\n\nNext.\n\n### Later\n\nMore.\n\n## Done\n\nDone.") == [
        "…", "## Done", "> Done."]


def test_a_wish_list_and_a_todo_note_go_with_what_follows_them_to_the_next_heading():
    kept = physlib.without_todos(CAPACITY)
    for gone in ["we would want", "Capacity of a replacement channel", "we should show", "not too hard to prove",
                 "coherentInfo_le_quantumCapacity", "The only notion", "Entanglement-assisted",
                 "And other important theorems"]:
        assert gone not in kept
    assert "The most basic facts:\n * `emulates_self`: Every channel emulates itself." in kept
    assert "Thus, the interval is `BddAbove`.\n\n…\n\n## iii. Table of contents\n\n- A. Basic definitions" in kept
    # A TODO in the middle of a paragraph cuts that paragraph only.
    kept = physlib.without_todos(UNITS_DOC)
    assert "(In fact temperature" not in kept and kept.endswith(
        "- Temperature\n\n…\n\nFrom these fundamental choices one can construct all other units and dimensions.")


def test_invitations_and_plans_for_files_go():
    # QuantumInfo/ForMathlib/HermitianMat/Inner.lean, OneDimension/PlaneWaves.lean, ClassicalMechanics/Force.lean,
    # HarmonicOscillator/Solution/Basic.lean and Operators/OneDimension/Unbounded.lean.
    assert physlib.without_todos(
        "Theorems about `HermitianMat`s that have to do with the topological structure. Pretty much everything here "
        "will\nassume these are matrices over ℂ, but changes to upgrade this to other types are welcome.") == (
        "Theorems about `HermitianMat`s that have to do with the topological structure. …")
    assert physlib.without_todos(
        "The plane waves.\n\nThis module has been generalized to d-dimensions in\n"
        "`QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean` and will be removed in the near future.") == (
        "The plane waves.\n\n…")
    assert physlib.without_todos(
        "Newtonian mechanics is\nnot limited to point particles, so this force representation is kept independent\n"
        "of any particular model of matter, with the intention it may get generalized for\nrigid body mechanics.") == "…"
    assert physlib.without_todos(
        "To each initial condition we association a trajectory.\n\nEventually we will show that these trajectories "
        "satisfy the equation of motion.") == "To each initial condition we association a trajectory.\n\n…"
    assert physlib.without_todos("It is likely one day the material in this file will be moved to Mathlib.") == "…"
    # A sentence on what the library does not have stays.
    kept = "The FLRW metric is not yet an object of Physlib."
    assert physlib.without_todos(kept) == kept


def test_a_docstring_cut_whole_shows_its_mark_and_physlibs_tooling_keeps_its_todo_words():
    source = {"repo": physlib.REPO, "rev": REV}
    declaration = {"name": "A.count", "kind": "def", "line": 3, "doc": "The number of TODO items.",
                   "statement": "def count : ℕ", "sorry": False}
    tooling = physlib.declaration_block(declaration, {"file": "Physlib/Meta/TODO/Basic.lean"}, source, set(), {})
    assert "> The number of TODO items." in tooling
    elsewhere = physlib.declaration_block({**declaration, "doc": "TODO: See above."}, {"file": "Physlib/A.lean"},
                                          source, set(), {})
    assert "\n\n> …\n\n```lean\ndef count : ℕ\n```" in elsewhere


def test_a_class_abbrev_is_read_under_its_own_name():
    record = physlib.read_module("namespace A\n\n/-- Both. -/\nclass abbrev Both (M : Type) := Inhabited M, Nonempty M\n\n"
                                 "end A\n", "Physlib/A.lean")
    assert [(item["name"], item["kind"], item["statement"]) for item in record["declarations"]] == [
        ("A.Both", "class", "class abbrev Both (M : Type) := Inhabited M, Nonempty M")]


def test_links_into_the_repository_follow_the_pin():
    source = {"repo": physlib.REPO, "rev": REV}
    assert physlib.pinned("See [here](https://github.com/leanprover-community/physlib/blob/master/scripts/a.md).",
                          source) == f"See [here]({BLOB}/scripts/a.md)."
    # A link to a path that is no module of the commit keeps its label; a module's links its article.
    keys = {"Physlib/A/Basic.lean": "physlib-Physlib.A.Basic"}
    text = physlib.quoted_prose("See [the old file](../Missing/Basic.lean) and [the basics](Basic.lean).",
                                "Physlib/A/Covariant.lean", source, keys)
    assert text == "> See the old file and [the basics](trough:physlib-Physlib.A.Basic)."


def test_a_structure_class_or_inductive_type_keeps_its_whole_command_and_no_more():
    text = """namespace A

/-- Colors. -/
inductive Color
| red
| green
deriving DecidableEq, Repr

/-- Red is not green. -/
@[simp] theorem red_ne_green : Color.red ≠ Color.green := by
  decide

class HasStar (α : Type) where
  star : α → α
  -- a comment between fields
  twice : α → α
@[inherit_doc] scoped infixr:70 " ⋆ " => HasStar.star

@[ext] structure P where
  x : ℕ
  y : ℕ
  -- the next declaration's comment

/-- The origin. -/
def origin : P := ⟨0, 0⟩

  structure Indented where
    z : ℕ
  /-- After it. -/
  @[simp] theorem indented : True := trivial

deriving instance Repr for P

end A
"""
    record = physlib.read_module(text, "Physlib/A.lean")
    statements = {item["name"]: item["statement"] for item in record["declarations"]}
    assert statements["A.Color"] == "inductive Color\n| red\n| green\nderiving DecidableEq, Repr"
    assert statements["A.HasStar"] == (
        "class HasStar (α : Type) where\n  star : α → α\n  -- a comment between fields\n  twice : α → α")
    # The statement starts at the keyword, as others do, and the fields keep their indentation.
    assert statements["A.P"] == "structure P where\n  x : ℕ\n  y : ℕ"
    assert statements["A.Indented"] == "structure Indented where\n  z : ℕ"
    assert statements["A.red_ne_green"] == "theorem red_ne_green : Color.red ≠ Color.green"


def test_a_statement_keeps_its_indentation_when_an_attribute_shares_its_keyword_line():
    text = "namespace A\n\n@[simp] theorem long (x : ℕ)\n    (h : x = x) :\n    x + 0 = x := by\n  simp\n\nend A\n"
    record = physlib.read_module(text, "Physlib/A.lean")
    assert record["declarations"][0]["statement"] == "theorem long (x : ℕ)\n    (h : x = x) :\n    x + 0 = x"


def test_modules_that_share_a_title_are_told_apart():
    def module(file: str, title: str) -> dict:
        return {"file": file, "module": file.removesuffix(".lean").replace("/", "."), "title": title}

    modules = [module("Physlib/ProbabilisticTheory/Weight/Basic.lean", "Weights"),
               module("PhyslibAlpha/ProbabilisticTheory/Weight/Basic.lean", "Weights"),
               module("Physlib/QuantumMechanics/OneDimension/PositionStates.lean", "Position states"),
               module("Physlib/QuantumMechanics/SpaceD/PositionStates.lean", "Position states"),
               module("Physlib/Electromagnetism/Distributional/Basic.lean", "The potential"),
               module("Physlib/Electromagnetism/TemperedDistributional/Basic.lean", "The potential"),
               module("PhyslibAlpha/Electromagnetism/Potential.lean", "The potential"),
               module("Physlib/Optics/Basic.lean", ""),
               module("Physlib/Optics/Lens.lean", "Lenses")]
    assert list(physlib.titles(modules).values()) == [
        "Weights (Physlib)", "Weights (PhyslibAlpha)",
        "Position states (OneDimension/PositionStates)", "Position states (SpaceD/PositionStates)",
        "The potential (Physlib, Distributional/Basic)", "The potential (Physlib, TemperedDistributional/Basic)",
        "The potential (PhyslibAlpha)", "Physlib.Optics.Basic", "Lenses"]


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
    manifestless = checkout(tmp_path / "manifest")
    (manifestless / "lake-manifest.json").unlink()
    assert refused(manifestless) == ["not checked out: lake-manifest.json"]
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
    # The two TODO-only section docstrings after it show one cut mark.
    assert body.endswith("```\n\n> …") and "> …\n\n> …" not in body
    assert "```lean\ntheorem energy_conservation (t : ℝ) : S.m = S.m\n```" in body
    assert "```lean\nstructure HarmonicOscillator where\n  /-- The mass. -/\n  m : ℝ\n  k : ℝ\n```" in body
    assert links["ClassicalMechanics.HarmonicOscillator"] == f"{BLOB}/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L49"


def test_a_docstrings_links_to_the_repository_point_at_articles_or_the_pin(tmp_path):
    result, links, pages = built(tmp_path)
    body = pages["physlib/spaceandtime/time/basic.md"]
    assert "[`Units.lean`](deep-units.md)" in body
    # A path that is no module of the commit keeps only its label.
    assert "see also\n> the README and" in body and f"{BLOB}/README.md" not in body
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


def test_a_module_the_dump_has_no_record_of_is_said_to_have_unknown_dependencies(tmp_path):
    partial = {**DEPS, "modules": {module: uses for module, uses in DEPS["modules"].items()
                                   if module != "Physlib.SpaceAndTime.Time.Deep.Units"}}
    result, links, pages = built(tmp_path, partial)
    leaf = result.targets["physlib-Physlib.SpaceAndTime.Time.Deep.Units"]
    assert leaf.depends == [] and leaf.no_depends == physlib.NO_RECORD
    assert result.stats["unrecorded"] == 1 and "The dump has no record of 1 module" in result.root.prose
    assert "The dump has no record" not in built(tmp_path / "full")[0].root.prose


def test_a_dump_that_has_under_half_the_names_read_is_refused(tmp_path):
    loaded = data(tmp_path, DEPS)
    names = [item["name"] for module in loaded["modules"] for item in module["declarations"] if item["name"]]
    loaded["deps"]["missing"] = names[: len(names) // 2 + 1]
    with pytest.raises(ValueError, match="names read from the source missing, over half"):
        physlib.chapter(loaded)


def test_the_front_page_counts_why_a_module_has_no_article(tmp_path):
    loaded = data(tmp_path, DEPS)
    result, _ = physlib.chapter(loaded)
    stats = Counter(result.stats) + Counter({"unshown": 34, "unshown informal": 10, "unshown unread": 1,
                                             "unshown other": 23})
    assert ("35 modules have no declaration to show and so no article: 24 declare nothing, holding only imports, a "
            "module docstring or other commands; 10 hold informal results or TODO items but no declaration to show; "
            "1 holds only declarations that are private or that Lean does not have.") in physlib.intro(loaded, stats)


def test_a_folder_of_tau_cetis_code_says_so_and_links_its_chapter(tmp_path):
    loaded = data(tmp_path, DEPS)
    for module in loaded["modules"]:
        if module["file"].startswith("Physlib/SpaceAndTime/Time/"):
            module["copyright"] = "2026 The Tau Ceti contributors"
    result, _ = physlib.chapter(loaded, Container("Tau Ceti", "tauceti"))
    time = result.targets["physlib-folder-Physlib/SpaceAndTime/Time"]
    assert ("Its files' headers read “Copyright (c) 2026 The Tau Ceti contributors”: the folder holds code of "
            "[Tau Ceti](trough:tauceti), which has a chapter of its own here.") in time.prose
    # Where some files have another holder, the page says how many have Tau Ceti's.
    loaded["modules"][[module["file"] for module in loaded["modules"]].index("Physlib/SpaceAndTime/Time/Basic.lean")][
        "copyright"] = "2026 Kitware, Inc"
    with_units = [module for module in loaded["modules"] if module["file"].startswith("Physlib/SpaceAndTime/Time/")]
    assert len(with_units) == 2
    result, _ = physlib.chapter(loaded, Container("Tau Ceti", "tauceti"))
    assert "Tau Ceti" not in result.targets["physlib-folder-Physlib/SpaceAndTime/Time"].prose
    assert "Tau Ceti" not in physlib.chapter(data(tmp_path / "plain", DEPS))[0].targets[
        "physlib-folder-Physlib/SpaceAndTime/Time"].prose


def test_folder_pages_and_articles_word_one_and_none(tmp_path):
    result, links, pages = built(tmp_path)
    geometric = result.targets["physlib-folder-Physlib/ClassicalMechanics/HarmonicOscillator/Geometric"]
    assert geometric.prose.startswith(f"The folder [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/]"
                                      f"(https://github.com/{physlib.REPO}/tree/{REV}/Physlib/ClassicalMechanics/"
                                      "HarmonicOscillator/Geometric): 1 module, with an article.")
    braket = result.targets["physlib-QuantumInfo.States.Pure.Braket"]
    assert "1 declaration, none with a docstring, 1 listed as significant." in braket.body


def test_a_dump_of_another_commit_is_refused(tmp_path):
    loaded = data(tmp_path, DEPS)
    loaded["deps"]["rev"] = "c" * 40
    with pytest.raises(ValueError, match="deps.json reads cccccccc"):
        physlib.chapter(loaded)


def test_the_front_page_quotes_the_repository_and_says_how_the_map_is_read(tmp_path):
    result, links, pages = built(tmp_path)
    front = result.root.prose
    assert front.startswith(f"[Physlib](https://github.com/{physlib.REPO}) is, in the words of its [README]({BLOB}/README.md),"
                            " “An open-source, community, project to digitalize results from physics into Lean 4”.")
    assert "maintainers: Léo Lessa and Joseph Tooby-Smith." in front
    assert ("6 articles, 4 in [Physlib](physlib/README.md), 1 in [PhyslibAlpha](physlibalpha/README.md) and 1 in "
            "[QuantumInfo](quantuminfo/README.md).") in front
    assert "1 module has no declaration to show and so no article." in front
    assert "without the sentences they mark as not yet formalized: 2 of the 2." in front
    assert "Lean toolchain v4.35.0, Mathlib v4.35.0, [bbbbbbbb]" in front
    assert "—" not in front
    # The pin is named, not described as the newest of anything: that stops being true.
    assert "newest" not in front and f"read at commit [{REV[:8]}]" in front
    assert "names the two directions of an equivalence: 1 such command is not shown." in front


def test_the_committed_data_build_the_chapter():
    loaded = physlib.load(ROOT / "data")
    assert loaded is not None and loaded["source"]["repo"] == physlib.REPO and len(loaded["source"]["rev"]) == 40
    assert loaded["deps"] is not None and loaded["deps"]["rev"] == loaded["source"]["rev"]
    result, links = physlib.chapter(loaded)
    leaves = [node for node in walk(result.root) if isinstance(node, Leaf)]
    assert len(leaves) == result.stats["articles"] > 1000
    assert set(links) >= {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(dict(leaf.fields)["declaration"] == "module" for leaf in leaves)
    assert len({leaf.title for leaf in leaves}) == len(leaves)
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
