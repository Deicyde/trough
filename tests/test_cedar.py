import json
import os
import subprocess
from pathlib import Path

import refresh_library
from trough import blueprints, cedar, library
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent

README = """# Cedar Specification

This repository contains the formalization of Cedar and infrastructure for performing differential randomized
testing (DRT) between the formalization and Rust production implementation available in
[`cedar`](https://github.com/cedar-policy/cedar).

You can learn more about our formalization efforts in the following blog posts:
"""

HEADER = """/-
 Copyright Cedar Contributors

 Licensed under the Apache License, Version 2.0 (the "License");
-/
"""

# Shaped like cedar-lean/Cedar/Spec/Authorizer.lean.
AUTHORIZER = HEADER + """
module

public import Cedar.Spec.Evaluator

/-! This file defines the Cedar authorizer. -/

namespace Cedar.Spec

/-- Whether a policy is satisfied. -/
public def satisfied (n : Nat) : Bool :=
  n == 0

end Cedar.Spec
"""

APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"

FILES = {"cedar-lean/Cedar/Spec/Authorizer.lean": AUTHORIZER,
         "cedar-lean/Cedar/Spec/Evaluator.lean": HEADER + "\nmodule\n\nnamespace Cedar.Spec\n\npublic def evaluate : Nat := 0\n\nend Cedar.Spec\n",
         "cedar-lean/Cedar.lean": HEADER + "\nmodule\n\npublic import Cedar.Spec.Authorizer\n",
         "cedar-lean/UnitTest/Main.lean": "def main : IO Unit := pure ()\n",
         "cedar-lean/README.md": "# Cedar Lean\n\nThis folder contains the Lean formalization of, and proofs about, Cedar.\n",
         "cedar-lean/lean-toolchain": "leanprover/lean4:v4.36.0\n",
         "cedar-lean/lake-manifest.json": json.dumps({"packages": [{"name": "batteries", "rev": "c" * 40}]}),
         "README.md": README, "LICENSE": APACHE}


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-18T14:07:49+00:00",
           "GIT_COMMITTER_DATE": "2026-11-18T14:07:49+00:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path) -> Path:
    for path, text in FILES.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "Initial commit")
    return root


def test_the_readme_description_is_its_first_paragraph():
    assert cedar.readme_description(README) == [
        "This repository contains the formalization of Cedar and infrastructure for performing differential randomized "
        "testing (DRT) between the formalization and Rust production implementation available in "
        "[`cedar`](https://github.com/cedar-policy/cedar)."]
    assert refresh_library.LIBRARIES["cedar"] is cedar.CEDAR


def test_a_lake_project_in_a_subfolder_is_read_from_it_and_linked_with_it(tmp_path):
    out = tmp_path / "data" / "cedar"
    assert library.refresh(cedar.CEDAR, checkout(tmp_path / "cedar-spec"), out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    record = json.loads((out / "library.json").read_text(encoding="utf-8"))
    rev = source["rev"]
    assert source["toolchain"] == "v4.36.0" and source["mathlib"] == ""
    # Modules are named and filed from cedar-lean/; UnitTest is another library and is not read.
    assert [(module["module"], module["file"]) for module in record["modules"]] == [
        ("Cedar.Spec.Authorizer", "Cedar/Spec/Authorizer.lean"), ("Cedar.Spec.Evaluator", "Cedar/Spec/Evaluator.lean")]
    assert record["readme"][0].startswith("This repository contains the formalization of Cedar")
    result, links = cedar.chapter(cedar.load(tmp_path / "data"))
    assert links["Cedar.Spec.satisfied"] == \
        f"https://github.com/cedar-policy/cedar-spec/blob/{rev}/cedar-lean/Cedar/Spec/Authorizer.lean#L16"
    vault = tmp_path / "vault"
    assign_paths(result.root, vault / "roadmap" / "cedar")
    blueprints.resolve(result, vault)
    pages = {path.relative_to(vault / "roadmap" / "cedar").as_posix(): text
             for path, text in render_tree(result.root, vault).items()}
    front = pages["README.md"]
    assert "the 2 modules under `cedar-lean/Cedar/` that declare something public by name" in front
    # The headers name no authors, so the intro does not say an article gives them.
    assert "It gives its docstrings and a block per public declaration" in front and "authors" not in front
    assert "The project's libraries other than `Cedar`, for Protobuf serialization" in front
    ledger = json.loads(result.files["sources/cedar/Cedar.Spec.Authorizer.json"])
    assert ledger["file"] == "cedar-lean/Cedar/Spec/Authorizer.lean"


def test_the_committed_data_build_the_chapter():
    loaded = cedar.load(ROOT / "data")
    assert loaded is not None and loaded["schema"] == cedar.SCHEMA and loaded["repo"] == cedar.REPO
    assert len(loaded["rev"]) == 40 and loaded["license"] == "Apache-2.0" and loaded["modules"]
    result, links = cedar.chapter(loaded)
    leaves = [node for node in walk(result.root) if isinstance(node, Leaf)]
    assert len(leaves) == result.stats["articles"] == len(result.files)
    assert result.stats["articles"] + result.stats.get("listed", 0) + result.stats.get("unbuilt", 0) == len(loaded["modules"])
    assert set(links) >= {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
    titles = [leaf.title for leaf in leaves]
    assert len(titles) == len(set(titles))
    assert loaded["deps"] and "built" in loaded["deps"]
    assert all(url.startswith(f"https://github.com/{cedar.REPO}/blob/{loaded['rev']}/cedar-lean/Cedar/")
               for url in links.values())
