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
    text = "Intro.\nTODO: more.\nStill here.\n\n## Plans\n\n- One.\n\n### Detail\n\nMore plans.\n\n## Kept\n\nYes."
    assert cslib.without_plans(text) == "Intro.\n…\nStill here.\n\n…\n## Kept\n\nYes."
    # A TODO in a code block stays, and two cuts in a row are one.
    assert cslib.without_plans("```\nTODO x\n```\n- TODO a\n- TODO b\nEnd.") == "```\nTODO x\n```\n…\nEnd."
    # The ellipsis a text writes itself is not a cut.
    assert cslib.without_plans("For i ∈ {0, …, n}.") == "For i ∈ {0, …, n}."


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
        "The Lean library for Computer Science.",
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


def data(tmp_path: Path, deps: dict | None = None) -> dict:
    out = tmp_path / "data" / "cslib"
    assert refresh_cslib.refresh(checkout(tmp_path / "cslib"), out) == []
    rev = json.loads((out / "source.json").read_text(encoding="utf-8"))["rev"]
    if deps is not None:
        (out / "deps.json").write_text(json.dumps({"rev": rev, "modules": deps}), encoding="utf-8")
    return cslib.load(tmp_path / "data")


def built(tmp_path: Path, deps: dict | None = None):
    loaded = data(tmp_path, deps)
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
    assert "Its README opens:\n\n> This directory covers **common foundations** for the rest of CSLib." in foundations
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
    # A full stop that ends a title goes; an ellipsis stays.
    assert cslib.titles([{"module": "A", "title": "Total LTS.", "file": "Cslib/A.lean"},
                         {"module": "B", "title": "And so on...", "file": "Cslib/B.lean"}]) == {
        "A": "Total LTS", "B": "And so on..."}


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
            named: {"statement": [lts], "proof": []}}
    loaded, result, links, pages = built(tmp_path, deps)
    assert result.stats["statement_edges"] == 4 and result.stats["proof_edges"] == 1
    page = pages["languages/mech/basic.md"]
    depends = page.split("## Depends on\n\n")[1].split("\n\n")[0]
    assert depends == "- [Bisimulation](../../foundations/semantics/lts/bisimulation.md)"
    assert "## Proof depends on\n\n- [λ-calculus (Named)](../lambdacalculus/named.md)" in page
    assert "## Proof depends on" not in pages["languages/lambdacalculus/locallynameless.md"]
    assert "Its statements use no other CSLib module's declarations." in pages["init.md"]
    assert "4 statement edges and 1 proof edge" in pages["README.md"]


def test_a_dump_of_another_commit_gives_no_edges(tmp_path):
    out = tmp_path / "data" / "cslib"
    assert refresh_cslib.refresh(checkout(tmp_path / "cslib"), out) == []
    (out / "deps.json").write_text(json.dumps({"rev": "f" * 40, "modules": {}}), encoding="utf-8")
    loaded = cslib.load(tmp_path / "data")
    assert loaded["deps"] is None
    result, _ = cslib.chapter(loaded)
    assert result.stats.get("statement_edges", 0) == 0
    assert "The articles have no edges yet" in result.root.prose


def test_the_front_page_quotes_the_readme_names_the_maintainers_and_gives_the_counts(tmp_path):
    loaded, result, links, pages = built(tmp_path, {})
    root = pages["README.md"]
    assert "> The Lean library for Computer Science.\n>\n> CSLib aims at formalising" in root
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
