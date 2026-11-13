import json
import os
import subprocess
from pathlib import Path

import refresh_cslib
from trough import blueprints
from trough import cslib
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "a" * 40
BLOB = f"https://github.com/leanprover/cslib/blob/{REV}"

# Shaped like Cslib/Foundations/Semantics/LTS/Basic.lean.
LTS = """/-
Copyright (c) 2025 Fabrizio Montesi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Fabrizio Montesi, Thomas Waring,
  Chris Henson
-/

module

public import Cslib.Init

/-!
# Labelled Transition System (LTS)

A Labelled Transition System (`LTS`) models the observable behaviour of a system.
TODO: add image-finite LTSs.

## Main definitions

- `LTS` is a structure for labelled transition systems.

## TODO

- Weak bisimulation up to.
-/

@[expose] public section

namespace Cslib

/-- A Labelled Transition System. -/
@[ext]
structure LTS (State : Type u) (Label : Type v) where
  /-- The transition relation. -/
  Tr : State → Label → State → Prop

namespace LTS

/-- A state is terminal if it has no outgoing transitions. -/
def IsTerminal (lts : LTS State Label) (s : State) : Prop :=
  ∀ μ s', ¬lts.Tr s μ s'

/-! ## Multistep transitions

This section treats executions with finitely many steps.
-/

theorem terminal_iff (lts : LTS State Label) (s : State) :
    lts.IsTerminal s ↔ ∀ μ s', ¬lts.Tr s μ s' := Iff.rfl

private theorem helper : True := trivial

instance : Inhabited Nat := ⟨0⟩

/-- The number of steps, by cases. -/
def steps : List Label → Nat
  | [] => 0
  | _ :: l => steps l + 1

end LTS

end Cslib

public meta section

/-- An elaborator. -/
def elabLts : Nat := 0

end
"""

BISIMULATION = """/-
Copyright (c) 2025 Fabrizio Montesi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

module

public import Cslib.Foundations.Semantics.LTS.Basic

/-! # Bisimulation -/

namespace Cslib.LTS

theorem bisim_refl : True := by
  sorry

end Cslib.LTS
"""

LAMBDA = """/-
Copyright (c) 2025 Chris Henson. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Chris Henson
-/

module

/-! # λ-calculus

The untyped λ-calculus.
-/

namespace Cslib.LambdaCalculus

/-- Terms. -/
inductive Term where
  | var : Nat → Term
  | app : Term → Term → Term
  deriving DecidableEq
/-- Application. -/
def app : Term → Term → Term := Term.app

end Cslib.LambdaCalculus
"""

INIT = """/-
Copyright (c) 2025 Fabrizio Montesi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

module

public import Mathlib.Init
"""

FOUNDATIONS_README = """<pre>
Copyright (c) 2026 Fabrizio Montesi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
</pre>

# Foundations

This directory covers **common foundations** for the rest of CSLib.

## Principles

Please reuse these abstractions.

### Plans

- Many modules are still missing.
"""

MECH_README = """# Mech

This directory is a placeholder for the upstreaming of Mech.

Mech is a framework.
"""

README = """# CSLib

The Lean library for Computer Science.

# What's CSLib?

CSLib aims at formalising Computer Science theories and tools, broadly construed, in the Lean programming language.

## Aims

- Offer APIs and languages.

# Using CSLib in your project

Add it to your lakefile.
"""

GOVERNANCE = """# Governance model for cslib

## Steering committee

- Clark Barrett (@barrettcw), Stanford University and Amazon.

## Maintainers

The maintainer team is responsible for the code.

### Lead maintainer

The Lead Maintainer is CSLib's chief architect.

- Fabrizio Montesi (@fmontesi), FORM, University of Southern Denmark.

### Area maintainers

- Ching-Tsun Chou (@ctchou). Areas: automata theory.
- Chris Henson (@chenson2018), Drexel University. Areas: Lambda calculus.

## Reviewers

- Eric Wieser (@eric-wieser), Google DeepMind.
"""

MANIFEST = {"packages": [{"name": "mathlib", "rev": "b" * 40}, {"name": "batteries", "rev": "c" * 40}]}
APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"
FILES = {
    "Cslib/Foundations/Semantics/LTS/Basic.lean": LTS,
    "Cslib/Foundations/Semantics/LTS/Bisimulation.lean": BISIMULATION,
    "Cslib/Languages/LambdaCalculus/Named.lean": LAMBDA,
    "Cslib/Languages/LambdaCalculus/LocallyNameless.lean": LAMBDA.replace("The untyped", "The locally nameless").replace(
        "Cslib.LambdaCalculus", "Cslib.LambdaCalculus.LocallyNameless"),
    "Cslib/Languages/Mech/Basic.lean": LAMBDA.replace("# λ-calculus", "# Mech").replace("LambdaCalculus", "Mech"),
    "Cslib/Init.lean": INIT,
    "Cslib/Foundations/README.md": FOUNDATIONS_README,
    "Cslib/Languages/Mech/README.md": MECH_README,
    "Cslib/Languages/Boole/README.md": "# Boole\n\nA language.\n",
    "CslibTests/LTS.lean": "module\n\ntheorem test : True := trivial\n",
}


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-12T04:33:36+01:00",
           "GIT_COMMITTER_DATE": "2026-11-12T04:33:36+01:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path, files: dict[str, str] = FILES, license_text: str = APACHE) -> Path:
    every = files | {"LICENSE": license_text, "README.md": README, "GOVERNANCE.md": GOVERNANCE,
                     "lean-toolchain": "leanprover/lean4:v4.36.0-rc2\n", "lake-manifest.json": json.dumps(MANIFEST)}
    for path, text in every.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "Initial commit")
    return root


def test_plans_sections_and_todo_lines_are_cut_and_marked():
    # A TODO runs to the end of its paragraph; a plans section to the next heading of its level; cuts in a row are one.
    text = "Intro.\nTODO: more.\nStill here.\n\n## Plans\n\n- One.\n\n### Detail\n\nMore plans.\n\n## Kept\n\nYes."
    assert cslib.without_plans(text) == "Intro.\n…\n## Kept\n\nYes."
    # A TODO in a code block or a code span stays; a list item ends a TODO's paragraph.
    assert cslib.without_plans("```\nTODO x\n```\n- TODO a\n- `TODO` b\nEnd.") == "```\nTODO x\n```\n…\n- `TODO` b\nEnd."
    # The ellipsis a text writes itself is not a cut.
    assert cslib.without_plans("For i ∈ {0, …, n}.") == "For i ∈ {0, …, n}."


# Docstrings at CSLib 86d560b6: SingleTape/Deterministic.lean's module docstring, Derivation.subs, VendingMachine.lean,
# Operators.lean's note on dynamic modalities, LocalComputation.lean, PMF.lean, StatefulProcesses/Basic.lean's
# limitations and BTL/Basic.lean.
DETERMINISTIC = """We also provide ways of constructing polynomial-runtime TMs

* `PolyTimeComputable.id`: computes the identity function

## TODOs

- Encoding of types in lists to represent computations on arbitrary types.
- Add `∘` notation for `compComputer`."""
SUBS = """Substitution of a family of derivations `D` for hypotheses in the context `Γ` of `E`. TODO:
this implementation is not capture avoiding."""
VENDING = """We then prove the classical example that the two are not bisimilar.

Future work on proving that the two vending machines are trace equivalent would be welcome."""
OPERATORS = """Here we need to use the prefix `d` to distinguish our notation from the normal `[·]` and `⟨·⟩`.
A refactoring that makes this unnecessary would be welcome."""
LOCAL = """The module is currently developed with minimality in mind. In the future, we plan on adding
facilities for typing expressions and easy integration with Lean and other IRs/FFIs."""
PMF = """## NB: This module is temporary

The bind/pure and posterior lemmas here have no dependence on any domain-specific
structure. They should be upstreamed to Mathlib
(likely `Mathlib.Probability.ProbabilityMassFunction.Monad` or a new
`Mathlib.Probability.ProbabilityMassFunction.Prod`). Once accepted upstream,
these lemmas should be removed and their consumers should import the Mathlib module instead.

The uniform samplers retain the PMF interface removed in
[mathlib#42909](https://github.com/leanprover-community/mathlib4/pull/42909),
pending a decision on CSLib's probability API. Their definitions and proofs are adapted from
`Mathlib.Probability.Distributions.Uniform` before that PR, by Josha Dekker, Devon Tuma,
and Kexing Ying, under the Apache 2.0 license.
Original sampler copyright (c) 2024 Josha Dekker. All rights reserved.

## Main results

- `Cslib.Probability.PMF.bind_pair_apply`: the "pairing" bind at `(a, b)` equals `p a * f a b`"""
LIMITATIONS = """## Limitations

The current formalisation does not cover process polymorphism (procedures do not take process
parameters) nor general recursion (this is the tail-recursive fragment of Stateful Processes).
For recursion, only the syntax is currently implemented. Its semantics will follow a similar
approach to that for `CCS`."""
BTL = """The basic temporal language has two unary modalities: `F` (sometime in the future) and
`P` (sometime in the past)."""


def test_todo_notes_and_plans_in_cslibs_docstrings_are_cut():
    assert cslib.without_plans(DETERMINISTIC) == DETERMINISTIC.split("\n\n## TODOs")[0] + "\n\n…"
    # A TODO in the middle of a line keeps the text before it.
    assert cslib.without_plans(SUBS) == ("Substitution of a family of derivations `D` for hypotheses in the context `Γ` "
                                         "of `E`. …")
    assert cslib.without_plans(VENDING) == "We then prove the classical example that the two are not bisimilar.\n\n…"
    assert cslib.without_plans(OPERATORS) == OPERATORS.split("\n")[0] + "\n…"
    assert cslib.without_plans(LOCAL) == "The module is currently developed with minimality in mind. …"
    # The paragraph on upstreaming goes; the attribution under the same heading stays.
    pmf = cslib.without_plans(PMF)
    assert pmf.startswith("## NB: This module is temporary\n\n…\n\nThe uniform samplers retain")
    assert "under the Apache 2.0 license.\nOriginal sampler copyright (c) 2024 Josha Dekker." in pmf
    assert "upstream" not in pmf.split("The uniform samplers")[0]
    # A section on limitations stays, without its sentence on what will follow.
    assert cslib.without_plans(LIMITATIONS) == LIMITATIONS.split(" Its semantics")[0] + " …"
    # "In the future" alone is vocabulary, as in temporal logic.
    assert cslib.without_plans(BTL) == BTL
    # A heading with nothing left under it goes.
    assert cslib.without_plans("Kept.\n\n## Note\n\nWe plan to add more.\n\n## Next\n\nText.") == (
        "Kept.\n\n…\n\n## Next\n\nText.")


def test_the_header_names_the_copyright_holders_and_the_authors():
    assert cslib.header(LTS) == {"copyright": "Fabrizio Montesi",
                                 "authors": "Fabrizio Montesi, Thomas Waring, Chris Henson"}
    assert cslib.header(BISIMULATION) == {"copyright": "Fabrizio Montesi", "authors": ""}
    assert cslib.header("module\n\ntheorem x : True := trivial\n") == {"copyright": "", "authors": ""}


def test_a_readme_gives_its_opening_paragraph_unless_it_speaks_of_plans():
    assert cslib.readme_text(FOUNDATIONS_README) == "This directory covers **common foundations** for the rest of CSLib."
    assert cslib.readme_text(MECH_README) == ""


def test_the_readme_description_and_the_maintainers():
    assert cslib.readme_description(README) == [
        "The Lean library for Computer Science.", "…",
        "CSLib aims at formalising Computer Science theories and tools, broadly construed, in the Lean programming "
        "language."]
    assert cslib.maintainers(GOVERNANCE) == [{"role": "Lead maintainer", "names": ["Fabrizio Montesi"]},
                                             {"role": "Area maintainers", "names": ["Ching-Tsun Chou", "Chris Henson"]}]


def test_a_module_keeps_its_title_docstrings_and_public_declarations_in_file_order():
    record = cslib.read_module(LTS, "Cslib/Foundations/Semantics/LTS/Basic.lean")
    assert record["module"] == "Cslib.Foundations.Semantics.LTS.Basic"
    assert record["title"] == "Labelled Transition System (LTS)"
    # The TODO line and the TODO section are cut.
    assert record["doc"] == ("A Labelled Transition System (`LTS`) models the observable behaviour of a system.\n…\n\n"
                             "## Main definitions\n\n- `LTS` is a structure for labelled transition systems.\n\n…")
    items = record["items"]
    assert [item.get("name") or item["note"].split("\n")[0] for item in items] == [
        "Cslib.LTS", "Cslib.LTS.IsTerminal", "## Multistep transitions", "Cslib.LTS.terminal_iff", "Cslib.LTS.steps",
        "elabLts"]
    lts, terminal, note, iff, steps, elab = items
    # A structure shows its fields; a definition and a theorem their statements; a definition by cases its header.
    assert lts == {"name": "Cslib.LTS", "kind": "structure", "line": 33, "doc": "A Labelled Transition System.",
                   "statement": "structure LTS (State : Type u) (Label : Type v) where\n  /-- The transition relation. -/\n"
                                "  Tr : State → Label → State → Prop", "sorry": False}
    assert terminal["statement"] == "def IsTerminal (lts : LTS State Label) (s : State) : Prop"
    assert note == {"line": 43, "note": "## Multistep transitions\n\nThis section treats executions with finitely many steps."}
    assert iff["statement"] == ("theorem terminal_iff (lts : LTS State Label) (s : State) :\n"
                                "    lts.IsTerminal s ↔ ∀ μ s', ¬lts.Tr s μ s'")
    assert steps["statement"] == "def steps : List Label → Nat" and steps["kind"] == "def"
    assert elab["kind"] == "def"


# The shapes of Circuit/Boolean/Basic.lean's Op, Operators.lean's classes and their notation, and an `@[ext]`
# structure, each followed by a command opening with an attribute; and a statement with an attribute on its line.
WHOLES = """module

namespace A

inductive Op where
  | and | or
  deriving DecidableEq

/-- The number of operations. -/
@[simp] theorem Op.card : Nat.succ 1 = 2 := rfl

/-- Conjunction. -/
class HasAnd (α : Type) where
  /-- The operation. -/
  and : α → α → α

@[inherit_doc] scoped infixr:35 " ∧∧ " => HasAnd.and

@[ext] structure P where
  x : Nat
  y : Nat

@[simp] theorem long_statement :
    (1 :
      Nat) = 1 := rfl

end A
"""


def test_a_whole_definition_ends_before_a_command_that_opens_with_an_attribute():
    items = {item["name"]: item for item in cslib.read_module(WHOLES, "Cslib/A.lean")["items"]}
    assert list(items) == ["A.Op", "A.Op.card", "A.HasAnd", "A.P", "A.long_statement"]
    assert items["A.Op"]["statement"] == "inductive Op where\n  | and | or\n  deriving DecidableEq"
    assert items["A.HasAnd"]["statement"] == "class HasAnd (α : Type) where\n  /-- The operation. -/\n  and : α → α → α"
    # The attribute is not shown, and the fields keep their indentation.
    assert items["A.P"]["statement"] == "structure P where\n  x : Nat\n  y : Nat"
    # A continuation keeps its indentation when an attribute shares the keyword's line.
    assert items["A.long_statement"]["statement"] == "theorem long_statement :\n    (1 :\n      Nat) = 1"


def test_an_inductive_type_shows_its_constructors_and_deriving_clause():
    record = cslib.read_module(LAMBDA, "Cslib/Languages/LambdaCalculus/Named.lean")
    assert record["items"][0]["statement"] == (
        "inductive Term where\n  | var : Nat → Term\n  | app : Term → Term → Term\n  deriving DecidableEq")


def test_a_module_whose_scopes_do_not_close_has_no_items():
    assert cslib.read_module("namespace A\nend B\n", "Cslib/Broken.lean")["items"] is None


def test_the_refresh_writes_the_source_and_the_library(tmp_path):
    out = tmp_path / "out"
    repo = checkout(tmp_path / "cslib")
    assert refresh_cslib.refresh(repo, out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    # The commit date is written in UTC.
    assert source == {"repo": cslib.REPO, "rev": git(repo, "rev-parse", "HEAD").strip(), "date": "2026-11-12T03:33:36Z",
                      "toolchain": "v4.36.0-rc2", "mathlib": "b" * 40, "license": "Apache-2.0"}
    record = json.loads((out / "library.json").read_text(encoding="utf-8"))
    assert record["schema"] == cslib.SCHEMA and record["rev"] == source["rev"]
    # The tests are not the library; a folder whose README speaks of plans, or that holds no module, is left out.
    assert [module["file"] for module in record["modules"]] == [
        "Cslib/Foundations/Semantics/LTS/Basic.lean", "Cslib/Foundations/Semantics/LTS/Bisimulation.lean",
        "Cslib/Init.lean", "Cslib/Languages/LambdaCalculus/LocallyNameless.lean",
        "Cslib/Languages/LambdaCalculus/Named.lean", "Cslib/Languages/Mech/Basic.lean"]
    assert record["folders"] == {"Cslib/Foundations": "This directory covers **common foundations** for the rest of CSLib."}
    assert record["readme"][0] == "The Lean library for Computer Science."
    assert record["maintainers"][0] == {"role": "Lead maintainer", "names": ["Fabrizio Montesi"]}
    assert cslib.counts(record["modules"]) == {"declarations": 12, "structure": 1, "def": 6, "theorem": 2, "inductive": 3,
                                               "documented": 10, "sorry": 1}


def test_the_refresh_writes_nothing_from_a_checkout_it_cannot_read_in_full(tmp_path):
    def refused(root: Path) -> list[str]:
        out = tmp_path / "out"
        problems = refresh_cslib.refresh(root, out)
        assert not out.exists()
        return problems

    assert refused(checkout(tmp_path / "mit", license_text="MIT License\n")) == [
        "not Apache-2.0: its LICENSE is not the Apache License 2.0"]
    broken = FILES | {"Cslib/Broken.lean": "namespace A\nend B\n"}
    assert refused(checkout(tmp_path / "broken", broken)) == ["Cslib/Broken.lean: its scopes do not close as they open"]
    gone = checkout(tmp_path / "gone")
    (gone / "Cslib/Init.lean").unlink()
    assert refused(gone) == ["not checked out: Cslib/Init.lean"]


def test_the_refresh_refuses_a_record_that_reads_under_half_the_last_declarations(tmp_path):
    out = tmp_path / "out"
    out.mkdir()
    last = {"modules": [{"items": [{"name": f"x{index}", "kind": "theorem", "doc": "", "sorry": False}
                                   for index in range(25)]}]}
    (out / "library.json").write_text(json.dumps(last), encoding="utf-8")
    assert refresh_cslib.refresh(checkout(tmp_path / "cslib"), out) == [
        "reads 12 declarations, under half the 25 the last record read"]
    assert json.loads((out / "library.json").read_text(encoding="utf-8")) == last
    assert not (out / "source.json").exists()


def data(tmp_path: Path, deps: dict | None = None, **dump: list[str]) -> dict:
    out = tmp_path / "data" / "cslib"
    assert refresh_cslib.refresh(checkout(tmp_path / "cslib"), out) == []
    rev = json.loads((out / "source.json").read_text(encoding="utf-8"))["rev"]
    if deps is not None:
        (out / "deps.json").write_text(json.dumps({"rev": rev, "modules": deps, **dump}), encoding="utf-8")
    return cslib.load(tmp_path / "data")


def built(tmp_path: Path, deps: dict | None = None, **dump: list[str]):
    loaded = data(tmp_path, deps, **dump)
    result, links = cslib.chapter(loaded)
    vault = tmp_path / "vault"
    assign_paths(result.root, vault / "roadmap" / "cslib")
    blueprints.resolve(result, vault)
    pages = {path.relative_to(vault / "roadmap" / "cslib").as_posix(): text
             for path, text in render_tree(result.root, vault).items()}
    return loaded, result, links, pages


def test_the_chapter_has_a_part_per_area_a_page_per_folder_and_an_article_per_module(tmp_path):
    loaded, result, links, pages = built(tmp_path)
    assert [entry.text for entry in result.root.entries] == ["Foundations", "Languages", "Init"]
    assert sorted(pages) == [
        "README.md", "foundations/README.md", "foundations/semantics/README.md", "foundations/semantics/lts/README.md",
        "foundations/semantics/lts/basic.md", "foundations/semantics/lts/bisimulation.md", "init.md",
        "languages/README.md", "languages/lambdacalculus/README.md", "languages/lambdacalculus/locallynameless.md",
        "languages/lambdacalculus/named.md", "languages/mech/README.md", "languages/mech/basic.md"]
    rev = loaded["rev"]
    foundations = pages["foundations/README.md"]
    assert "2 modules under `Cslib/Foundations/`, with 6 public declarations." in foundations
    assert (f"Its [README](https://github.com/leanprover/cslib/blob/{rev}/Cslib/Foundations/README.md) opens:\n\n"
            "> This directory covers **common foundations** for the rest of CSLib.") in foundations
    # A part page credits the repository and commit; a folder page below it does not.
    assert f"at commit [{rev[:8]}](https://github.com/leanprover/cslib/tree/{rev})" in foundations
    assert "commit" not in pages["foundations/semantics/README.md"]
    assert links["Cslib.LTS.terminal_iff"] == f"https://github.com/leanprover/cslib/blob/{rev}/Cslib/Foundations/Semantics/LTS/Basic.lean#L48"
    assert len(links) == 12


def test_an_article_shows_its_module_its_authors_its_docstring_and_a_block_per_declaration(tmp_path):
    loaded, result, links, pages = built(tmp_path)
    rev = loaded["rev"]
    page = pages["foundations/semantics/lts/basic.md"]
    names = ("Cslib.LTS, Cslib.LTS.IsTerminal, Cslib.LTS.terminal_iff, Cslib.LTS.steps, elabLts")
    assert page.startswith(f"---\ncatalog: module\nlean: {names}\nstatement: formalized\nproof: formalized\n---\n\n"
                           "# Labelled Transition System (LTS)\n\n")
    blob = f"https://github.com/leanprover/cslib/blob/{rev}/Cslib/Foundations/Semantics/LTS/Basic.lean"
    assert (f"`Cslib.Foundations.Semantics.LTS.Basic`, in [Cslib/Foundations/Semantics/LTS/Basic.lean]({blob}), by "
            "Fabrizio Montesi, Thomas Waring, Chris Henson.") in page
    assert "> A Labelled Transition System (`LTS`) models the observable behaviour of a system.\n> …" in page
    assert (f"`Cslib.LTS.IsTerminal` (definition, [line 40]({blob}#L40))\n\n> A state is terminal if it has no outgoing "
            "transitions.\n\n```lean\ndef IsTerminal (lts : LTS State Label) (s : State) : Prop\n```") in page
    assert "> ## Multistep transitions" in page
    # A module without its own Authors line names its copyright holder; a proof with sorry says so.
    bisimulation = pages["foundations/semantics/lts/bisimulation.md"]
    assert "proof: formalized" not in bisimulation and ", by Fabrizio Montesi." in bisimulation
    assert "`Cslib.LTS.bisim_refl` (theorem, [line 14](" in bisimulation and "). Its value holds `sorry`." in bisimulation
    # A module that declares nothing public has no Lean row and says so; its title is its file name.
    init = pages["init.md"]
    assert init.startswith("---\ncatalog: module\n---\n\n# Init\n\n") and "It declares nothing public by name." in init


def test_titles_shared_by_modules_take_their_file_names(tmp_path):
    loaded, result, links, pages = built(tmp_path)
    assert "# λ-calculus (Named)\n" in pages["languages/lambdacalculus/named.md"]
    assert "# λ-calculus (LocallyNameless)\n" in pages["languages/lambdacalculus/locallynameless.md"]
    assert "# Mech\n" in pages["languages/mech/basic.md"]
    # Where title and file name are both shared, the shortest end of the path that tells the modules apart; a full
    # stop that ends a title goes, an ellipsis stays.
    modules = [("A", "λ-calculus", "Cslib/L/Stlc/Basic.lean"), ("B", "λ-calculus", "Cslib/L/Fsub/Basic.lean"),
               ("C", "λ-calculus", "Cslib/L/LocallyNameless/Untyped/Basic.lean"),
               ("D", "λ-calculus", "Cslib/L/Named/Untyped/Basic.lean"), ("E", "λ-calculus", "Cslib/L/Named/FullBeta.lean"),
               ("F", "", "Cslib/L/Stlc/StrongNorm.lean"), ("G", "", "Cslib/L/Untyped/StrongNorm.lean"),
               ("H", "Total LTS.", "Cslib/A.lean"), ("I", "And so on...", "Cslib/B.lean")]
    assert cslib.titles([{"module": module, "title": title, "file": file} for module, title, file in modules]) == {
        "A": "λ-calculus (Stlc/Basic)", "B": "λ-calculus (Fsub/Basic)", "C": "λ-calculus (LocallyNameless/Untyped/Basic)",
        "D": "λ-calculus (Named/Untyped/Basic)", "E": "λ-calculus (FullBeta)", "F": "Stlc/StrongNorm",
        "G": "Untyped/StrongNorm", "H": "Total LTS", "I": "And so on..."}
    titles = [leaf.title for leaf in walk(result.root) if isinstance(leaf, Leaf)]
    assert len(titles) == len(set(titles))


def test_edges_come_from_the_dump_reduced(tmp_path):
    lts, bisim = "Cslib.Foundations.Semantics.LTS.Basic", "Cslib.Foundations.Semantics.LTS.Bisimulation"
    named, nameless = "Cslib.Languages.LambdaCalculus.Named", "Cslib.Languages.LambdaCalculus.LocallyNameless"
    mech = "Cslib.Languages.Mech.Basic"
    deps = {bisim: {"statement": [lts], "proof": []},
            # Mech's statements use Bisimulation, which uses Basic, so Basic is no edge of its own; Named, which only
            # its proofs use, is reached through no other dependency.
            mech: {"statement": [bisim, lts], "proof": [named, "Mathlib.Order.Basic"]},
            # Its proofs use Basic, which its statements reach through Named.
            nameless: {"statement": [named], "proof": [lts]},
            named: {"statement": [lts], "proof": []}, lts: {"statement": [], "proof": []}}
    loaded, result, links, pages = built(tmp_path, deps)
    assert result.stats["statement_edges"] == 4 and result.stats["proof_edges"] == 1
    page = pages["languages/mech/basic.md"]
    depends = page.split("## Depends on\n\n")[1].split("\n\n")[0]
    assert depends == "- [Bisimulation](../../foundations/semantics/lts/bisimulation.md)"
    assert "## Proof depends on\n\n- [λ-calculus (Named)](../lambdacalculus/named.md)" in page
    assert "## Proof depends on" not in pages["languages/lambdacalculus/locallynameless.md"]
    assert "Its statements use no other CSLib module's declarations." in pages["foundations/semantics/lts/basic.md"]
    # The dump has no record of Init: its dependencies are unknown, not none.
    assert "The Lean dump has no record of this module, so its dependencies are unknown." in pages["init.md"]
    assert "4 statement edges and 1 proof edge. The run has no record of 1 module" in pages["README.md"]


def test_lean_decides_which_declarations_are_public(tmp_path):
    # Lean marks a declaration private to its module, as in Combinators/Id.lean and Order/Huntington.lean, where a
    # declaration outside a public section and not marked public is private; and both of Mech's.
    loaded, result, links, pages = built(tmp_path, {}, private=["Cslib.LTS.IsTerminal", "Cslib.Mech.Term", "Cslib.Mech.app"],
                                         missing=["elabLts"])
    assert result.stats["private"] == 3 and result.stats["unresolved"] == 1 and result.stats["declarations"] == 8
    basic = pages["foundations/semantics/lts/basic.md"]
    assert "`Cslib.LTS.IsTerminal`" not in basic and "`elabLts`" not in basic and "Cslib.LTS.IsTerminal" not in links
    assert "lean: Cslib.LTS, Cslib.LTS.terminal_iff, Cslib.LTS.steps\n" in basic
    assert "1 module under `Cslib/Languages/Mech/`, which declares nothing public by name." in pages["languages/mech/README.md"]
    assert "It declares nothing public by name." in pages["languages/mech/basic.md"]
    assert ("Lean marks 3 of them as private to their modules (in a `module` file, a declaration outside a `public "
            "section` and not marked `public` is private), and these are left out, as is 1 name Lean does not have."
            ) in pages["README.md"]


def test_a_dump_of_another_commit_gives_no_edges(tmp_path):
    out = tmp_path / "data" / "cslib"
    assert refresh_cslib.refresh(checkout(tmp_path / "cslib"), out) == []
    (out / "deps.json").write_text(json.dumps({"rev": "f" * 40, "modules": {}}), encoding="utf-8")
    loaded = cslib.load(tmp_path / "data")
    assert loaded["deps"] is None
    result, _ = cslib.chapter(loaded)
    assert result.stats.get("statement_edges", 0) == 0
    assert "The articles have no edges, and the names read from the source are not checked against Lean" in \
        result.root.prose


def test_the_front_page_quotes_the_readme_names_the_maintainers_and_gives_the_counts(tmp_path):
    loaded, result, links, pages = built(tmp_path, {})
    root = pages["README.md"]
    # The heading between the README's opening and its "What's CSLib?" is marked as a cut.
    assert "> The Lean library for Computer Science.\n>\n> …\n>\n> CSLib aims at formalising" in root
    assert "newest" not in root
    assert "Its GOVERNANCE.md names Fabrizio Montesi as lead maintainer and Ching-Tsun Chou and Chris Henson as area " \
           "maintainers." in root
    assert ("It has an article for each of the 6 modules under `Cslib/`, in a part per folder of `Cslib/` and a page "
            "per folder below. They hold 12 public declarations, 2 theorems and 10 definitions, 10 of them with a "
            "docstring; 1 module declares nothing public by name.") in root
    assert "Aims" not in root and "Offer APIs" not in root


def test_the_committed_data_build_the_chapter():
    loaded = cslib.load(ROOT / "data")
    assert loaded is not None and loaded["schema"] == cslib.SCHEMA and loaded["repo"] == cslib.REPO and len(loaded["rev"]) == 40
    assert loaded["license"] == "Apache-2.0" and loaded["modules"]
    result, links = cslib.chapter(loaded)
    leaves = [node for node in walk(result.root) if isinstance(node, Leaf)]
    assert len(leaves) == result.stats["articles"] == len(loaded["modules"])
    assert set(links) >= {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
    titles = [leaf.title for leaf in leaves]
    assert len(titles) == len(set(titles))
    # The dump of the same commit has a record of every module and every name it was given.
    assert loaded["deps"] and not result.stats.get("unrecorded") and not result.stats.get("unresolved")
