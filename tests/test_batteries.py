import json
import os
import subprocess
from pathlib import Path

import refresh_library
from trough import batteries, blueprints, library
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent

# Shaped like Batteries/Data/Char/Basic.lean.
CHAR_BASIC = """/-
Copyright (c) 2022 Jannis Limperg. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Jannis Limperg, François G. Dorais
-/
module

public import Batteries.Classes.Order

public section

namespace Char

theorem le_antisymm_iff {x y : Char} : x = y ↔ x ≤ y ∧ y ≤ x :=
  Char.ext_iff.trans UInt32.le_antisymm_iff

instance : Std.LawfulOrd Char :=
  .compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm
    (fun _ => Nat.lt_irrefl _) Nat.lt_trans Nat.not_lt Char.le_antisymm

/--
Maximum character code point.
(See [unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value).)
-/
protected abbrev max := 0x10FFFF

end Char
"""

# Batteries/Data/Char.lean: only imports.
CHAR = """module

public import Batteries.Data.Char.Basic
"""

# Shaped like Batteries/Tactic/NoMatch.lean: syntax and elaborators, no declaration by name.
NOMATCH = """/-
Copyright (c) 2021 Mario Carneiro. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Mario Carneiro
-/
module

public meta import Lean.Elab.Tactic.Basic

public meta section

/-!
Deprecation warnings for `match ⋯ with.`, `fun.`, `λ.`, and `intro.`.
-/
namespace Batteries.Tactic
open Lean Elab Term Tactic Parser.Term

/-- The syntax `fun.` has been deprecated in favor of `nofun`. -/
elab (name := funDot) (priority := low) tk:"fun" "." : term <= expectedType? => do
  elabTerm (← `(nofun)) expectedType?

end Batteries.Tactic
"""

# A tactic module with a public definition.
TACTIC_BASIC = """/-
Copyright (c) 2024 Kim Morrison. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Kim Morrison
-/
module

public meta import Lean.Elab.Tactic.Basic

/-! # Tactic basics -/

public meta section

namespace Batteries.Tactic

/-- The tactics this file defines. -/
def basics : List String := ["trivial"]

end Batteries.Tactic
"""

# A linter whose definition is not public: in a `module` file, a `meta section` not marked `public` is private.
LINTER = """/-
Copyright (c) 2023 Mario Carneiro. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Mario Carneiro
-/
module

public meta import Lean.Linter.Util

meta section

namespace Batteries.Linter

/-- The linter. -/
def unreachableTacticLinter : Nat := 0

end Batteries.Linter
"""

README = """# Batteries

The "batteries included" extended library for Lean 4. This is a collection of data structures and tactics intended for use by both computer-science applications and mathematics applications of Lean 4.

# Using `batteries`

To use `batteries` in your project, add it to your `lakefile.lean`.
"""

APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"
FILES = {
    "Batteries/Data/Char/Basic.lean": CHAR_BASIC,
    "Batteries/Data/Char.lean": CHAR,
    "Batteries/Tactic/NoMatch.lean": NOMATCH,
    "Batteries/Tactic/Basic.lean": TACTIC_BASIC,
    "Batteries/Linter/UnreachableTactic.lean": LINTER,
    "Batteries.lean": "module\n\npublic import Batteries.Data.Char\n",
    "BatteriesTest/char.lean": "module\n\ntheorem test : True := trivial\n",
}
CHAR_LEMMAS, TACTICS = "Batteries.Data.Char.Basic", "Batteries.Tactic.Basic"


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-16T17:41:33+01:00",
           "GIT_COMMITTER_DATE": "2026-11-16T17:41:33+01:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path, files: dict[str, str] = FILES, license_text: str = APACHE) -> Path:
    every = files | {"LICENSE": license_text, "README.md": README, "lean-toolchain": "leanprover/lean4:v4.36.0\n",
                     "lake-manifest.json": json.dumps({"packages": []})}
    for path, text in every.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "Initial commit")
    return root


def test_the_readme_description_is_its_opening_section():
    assert batteries.readme_description(README) == [
        "The \"batteries included\" extended library for Lean 4. This is a collection of data structures and tactics "
        "intended for use by both computer-science applications and mathematics applications of Lean 4."]


def test_the_refresh_writes_the_source_and_the_library(tmp_path):
    out = tmp_path / "out"
    repo = checkout(tmp_path / "batteries")
    assert library.refresh(batteries.BATTERIES, repo, out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    # Batteries needs no Mathlib.
    assert source == {"repo": batteries.REPO, "rev": git(repo, "rev-parse", "HEAD").strip(),
                      "date": "2026-11-16T16:41:33Z", "toolchain": "v4.36.0", "mathlib": "", "license": "Apache-2.0"}
    record = json.loads((out / "library.json").read_text(encoding="utf-8"))
    assert record["schema"] == batteries.SCHEMA and record["rev"] == source["rev"]
    # The tests and the root module, which only imports, are not read.
    assert [module["file"] for module in record["modules"]] == [
        "Batteries/Data/Char.lean", "Batteries/Data/Char/Basic.lean", "Batteries/Linter/UnreachableTactic.lean",
        "Batteries/Tactic/Basic.lean", "Batteries/Tactic/NoMatch.lean"]
    assert record["readme"][0].startswith("The \"batteries included\" extended library for Lean 4.")
    assert library.counts(record["modules"]) == {"declarations": 4, "theorem": 1, "abbrev": 1, "def": 2,
                                                 "documented": 3, "sorry": 0}
    # The command line names the library.
    assert refresh_library.LIBRARIES["batteries"] is batteries.BATTERIES


def test_the_refresh_writes_nothing_from_a_checkout_it_cannot_read_in_full(tmp_path):
    out = tmp_path / "out"
    assert library.refresh(batteries.BATTERIES, checkout(tmp_path / "mit", license_text="MIT License\n"), out) == [
        "not Apache-2.0: its LICENSE is not the Apache License 2.0"]
    gone = checkout(tmp_path / "gone")
    (gone / "lake-manifest.json").unlink()
    assert library.refresh(batteries.BATTERIES, gone, out) == ["not checked out: lake-manifest.json"]
    assert not out.exists()


def built(tmp_path: Path, deps: dict | None = None, **dump: list[str]):
    out = tmp_path / "data" / "batteries"
    assert library.refresh(batteries.BATTERIES, checkout(tmp_path / "batteries"), out) == []
    rev = json.loads((out / "source.json").read_text(encoding="utf-8"))["rev"]
    if deps is not None:
        (out / "deps.json").write_text(json.dumps({"rev": rev, "modules": deps, **dump}), encoding="utf-8")
    loaded = batteries.load(tmp_path / "data")
    result, links = batteries.chapter(loaded)
    vault = tmp_path / "vault"
    assign_paths(result.root, vault / "roadmap" / "batteries")
    blueprints.resolve(result, vault)
    pages = {path.relative_to(vault / "roadmap" / "batteries").as_posix(): text
             for path, text in render_tree(result.root, vault).items()}
    return loaded, result, links, pages


def test_a_module_that_declares_nothing_public_is_listed_on_its_folders_page(tmp_path):
    # Lean has the linter's definition only as a private one.
    deps = {CHAR_LEMMAS: {"statement": [], "proof": []}, TACTICS: {"statement": [], "proof": []}}
    loaded, result, links, pages = built(tmp_path, deps, private=["Batteries.Linter.unreachableTacticLinter"])
    rev = loaded["rev"]
    blob = f"https://github.com/leanprover-community/batteries/blob/{rev}"
    # Articles only for the modules with a public declaration; the Linter folder, left with none, has no page.
    assert sorted(pages) == ["README.md", "data/README.md", "data/char/README.md", "data/char/basic.md",
                             "tactic/README.md", "tactic/basic.md"]
    assert [entry.text for entry in result.root.entries] == ["Data", "Tactic"]
    assert result.stats["articles"] == 2 and result.stats["listed"] == 3 and result.stats["empty"] == 3
    data = pages["data/README.md"]
    # The instance with no name is not counted.
    assert "2 modules under `Batteries/Data/`, with 2 public declarations." in data
    assert f"This module declares nothing public by name, so it has no article: [`Batteries.Data.Char`]({blob}/Batteries/Data/Char.lean)." in data
    tactic = pages["tactic/README.md"]
    assert "2 modules under `Batteries/Tactic/`, with 1 public declaration." in tactic
    assert f"[`Batteries.Tactic.NoMatch`]({blob}/Batteries/Tactic/NoMatch.lean)" in tactic
    # A folder without a page lists its modules on the page above, here the front page.
    root = pages["README.md"]
    assert f"so it has no article: [`Batteries.Linter.UnreachableTactic`]({blob}/Batteries/Linter/UnreachableTactic.lean)." in root
    assert "unreachableTacticLinter" not in links and len(links) == 3


def test_an_article_shows_its_authors_its_docstrings_and_a_block_per_public_declaration(tmp_path):
    loaded, result, links, pages = built(tmp_path, {CHAR_LEMMAS: {"statement": [], "proof": []},
                                                    TACTICS: {"statement": [], "proof": []}})
    rev = loaded["rev"]
    blob = f"https://github.com/leanprover-community/batteries/blob/{rev}/Batteries/Data/Char/Basic.lean"
    page = pages["data/char/basic.md"]
    assert page.startswith("---\ncatalog: module\nlean: Char.le_antisymm_iff, Char.max\nstatement: formalized\n"
                           "proof: formalized\n---\n\n# Basic\n\n")
    assert f"`Batteries.Data.Char.Basic`, in [Batteries/Data/Char/Basic.lean]({blob}), by Jannis Limperg, François G. Dorais." in page
    assert (f"`Char.max` (abbreviation, [line 25]({blob}#L25))\n\n> Maximum character code point.\n> (See [unicode scalar "
            "value](https://www.unicode.org/glossary/#unicode_scalar_value).)\n\n```lean\nprotected abbrev max\n```") in page
    assert "Its statements use no other Batteries module's declarations." in page
    # A tactic module maps like any other: its public definition has a block.
    assert "`Batteries.Tactic.basics` (definition, [line 17](" in pages["tactic/basic.md"]


def test_the_front_page_quotes_the_readme_and_gives_the_counts(tmp_path):
    loaded, result, links, pages = built(tmp_path, {}, private=["Batteries.Linter.unreachableTacticLinter"])
    root = pages["README.md"]
    assert root.startswith("# Batteries: the extended library for Lean\n")
    assert "> The \"batteries included\" extended library for Lean 4." in root
    assert "Mathlib requires it, so every project built on Mathlib builds on it too." in root
    assert ("It has an article for each of the 2 modules under `Batteries/` that declare something public by name, in "
            "a part per folder of `Batteries/` and a page per folder below. They hold 3 public declarations, 1 theorem "
            "and 2 definitions, 2 of them with a docstring. The other 3 modules, which add syntax, elaborators, linters "
            "and other tools without a public declaration, are listed on their folders' pages.") in root
    assert "Lean marks 1 of them as private to their modules" in root
    # No Mathlib commit: Batteries needs none.
    assert "Mathlib" not in root.split("builds on it too.")[1]


def test_the_generic_dump_reads_the_roots_from_the_environment():
    dump = (ROOT / "lean" / "library" / "LibraryDeps.lean").read_text(encoding="utf-8")
    code = dump.split("-/", 1)[1]
    assert "TROUGH_ROOTS" in code and "Cslib" not in code and not dump.startswith("import")


def test_the_committed_data_build_the_chapter():
    loaded = batteries.load(ROOT / "data")
    assert loaded is not None and loaded["schema"] == batteries.SCHEMA and loaded["repo"] == batteries.REPO
    assert len(loaded["rev"]) == 40 and loaded["license"] == "Apache-2.0" and loaded["modules"]
    result, links = batteries.chapter(loaded)
    leaves = [node for node in walk(result.root) if isinstance(node, Leaf)]
    assert len(leaves) == result.stats["articles"]
    assert result.stats["articles"] + result.stats["listed"] == len(loaded["modules"])
    assert set(links) >= {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
    titles = [leaf.title for leaf in leaves]
    assert len(titles) == len(set(titles))
    # The dump of the same commit has a record of every module.
    assert loaded["deps"] and not result.stats.get("unrecorded")
