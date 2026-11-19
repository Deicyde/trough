import json
import os
import subprocess
from pathlib import Path

import pytest

import refresh_library
from trough import aesop, blueprints, library
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent

README = """# Aesop

Aesop (Automated Extensible Search for Obvious Proofs) is a proof search tactic
for Lean 4. It is broadly similar to Isabelle's `auto`. In essence, Aesop works
like this:

- As with `simp`, you tag a (large) collection of definitions with the
  `@[aesop]` attribute, registering them as Aesop _rules_.

## Building

Run `lake build`.
"""

# Shaped like Aesop/Rule/Basic.lean.
RULE = """/-
Copyright (c) 2021 Jannis Limperg. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Jannis Limperg
-/
module

public import Aesop.RuleTac.Descr

public section

namespace Aesop

/-- A rule. -/
structure Rule (α : Type) where
  name : Nat
  extra : α

def Rule.compareByName (r s : Rule α) : Ordering :=
  compare r.name s.name

end Aesop
"""

APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"


def module(number: int) -> str:
    return f"module\n\npublic section\n\nnamespace Aesop\n\ndef top{number} : Nat := {number}\n\nend Aesop\n"


# A folder and 22 modules at the top, more than a page lists.
FILES = {"Aesop/Rule/Basic.lean": RULE, "Aesop.lean": "module\n\npublic import Aesop.Rule.Basic\n",
         "AesopTest/Basic.lean": "module\n\ntheorem test : True := trivial\n"}
FILES |= {f"Aesop/Top{number:02d}.lean": module(number) for number in range(22)}


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-18T14:07:49+00:00",
           "GIT_COMMITTER_DATE": "2026-11-18T14:07:49+00:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path) -> Path:
    every = FILES | {"LICENSE": APACHE, "README.md": README, "lean-toolchain": "leanprover/lean4:v4.37.0-rc1\n",
                     "lake-manifest.json": json.dumps({"packages": [{"name": "batteries", "rev": "c" * 40}]})}
    for path, text in every.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "Initial commit")
    return root


def built(tmp_path: Path, deps: dict | None = None, **dump):
    out = tmp_path / "data" / "aesop"
    assert library.refresh(aesop.AESOP, checkout(tmp_path / "aesop"), out) == []
    rev = json.loads((out / "source.json").read_text(encoding="utf-8"))["rev"]
    if deps is not None:
        (out / "deps.json").write_text(json.dumps({"rev": rev, "modules": deps, **dump}), encoding="utf-8")
    loaded = aesop.load(tmp_path / "data")
    result, links = aesop.chapter(loaded)
    vault = tmp_path / "vault"
    assign_paths(result.root, vault / "roadmap" / "aesop")
    blueprints.resolve(result, vault)
    pages = {path.relative_to(vault / "roadmap" / "aesop").as_posix(): text
             for path, text in render_tree(result.root, vault).items()}
    return loaded, result, links, pages


def test_the_readme_description_is_what_aesop_is():
    assert aesop.readme_description(README) == [
        "Aesop (Automated Extensible Search for Obvious Proofs) is a proof search tactic for Lean 4. It is broadly "
        "similar to Isabelle's `auto`."]
    assert refresh_library.LIBRARIES["aesop"] is aesop.AESOP


def test_the_front_page_quotes_the_readme_and_nests_a_long_root(tmp_path):
    loaded, result, links, pages = built(tmp_path)
    root = pages["README.md"]
    assert root.startswith("# Aesop: proof search for Lean\n")
    assert "> Aesop (Automated Extensible Search for Obvious Proofs) is a proof search tactic for Lean 4." in root
    assert "Mathlib requires it." in root and "In essence" not in root
    # 23 modules, 22 of them at the top: no page lists more than 20.
    assert result.stats["articles"] == 23
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
    assert "with Lean toolchain v4.37.0-rc1. It has an article for each of the 23 modules" in root


def test_a_module_that_did_not_build_is_listed_on_the_front_page(tmp_path):
    names = [f"Aesop.Top{number:02d}" for number in range(22)]
    built_modules = ["Aesop.Rule.Basic", *names[1:]]
    deps = {name: {"statement": [], "proof": []} for name in built_modules}
    loaded, result, links, pages = built(tmp_path, deps, built=built_modules)
    rev = loaded["rev"]
    assert result.stats["unbuilt"] == 1 and result.stats["articles"] == 22
    assert not any(key.endswith("Top00") for key in result.targets) and "Aesop.top0" not in links
    assert ("1 module under `Aesop/` did not build in the library's own build, so Lean could not read it and it has no "
            f"article: [`Aesop.Top00`](https://github.com/leanprover-community/aesop/blob/{rev}/Aesop/Top00.lean).") in \
        pages["README.md"]
    assert "sources/aesop/Aesop.Top00.json" not in result.files


def test_a_dump_in_which_over_half_the_modules_did_not_build_is_refused(tmp_path):
    with pytest.raises(ValueError, match="did not build, over half"):
        built(tmp_path, {"Aesop.Rule.Basic": {"statement": [], "proof": []}}, built=["Aesop.Rule.Basic"])


def test_the_generic_dump_records_the_modules_that_built():
    dump = (ROOT / "lean" / "library" / "LibraryDeps.lean").read_text(encoding="utf-8")
    assert '("built",' in dump


def test_the_committed_data_build_the_chapter():
    loaded = aesop.load(ROOT / "data")
    assert loaded is not None and loaded["schema"] == aesop.SCHEMA and loaded["repo"] == aesop.REPO
    assert len(loaded["rev"]) == 40 and loaded["license"] == "Apache-2.0" and loaded["modules"]
    result, links = aesop.chapter(loaded)
    leaves = [node for node in walk(result.root) if isinstance(node, Leaf)]
    assert len(leaves) == result.stats["articles"]
    assert result.stats["articles"] + result.stats.get("listed", 0) + result.stats.get("unbuilt", 0) == len(loaded["modules"])
    assert set(links) >= {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
    titles = [leaf.title for leaf in leaves]
    assert len(titles) == len(set(titles))
    assert loaded["deps"] and "built" in loaded["deps"]
