import json
import re
import subprocess
from pathlib import Path

import pytest

import refresh_riemann_hypothesis
from trough import riemann_hypothesis as rh
from trough.blueprints import LINK
from trough.vault import Container, Entry, Leaf, walk

ROOT = Path(__file__).resolve().parent.parent
NAMES = list(rh.CLAIMS)

LAKEFILE = """name = "tree"
srcDir = "src"
defaultTargets = ["Alpha", "Beta", "BetaFields", "Main"]

[[lean_lib]]
name = "Alpha"
globs = ["Alpha.+"]

[[lean_lib]]
name = "Beta"
globs = ["Beta.One.+"]

[[lean_lib]]
name = "BetaFields"
globs = ["Beta.Two.+"]

[[lean_lib]]
name = "Main"
roots = ["Statements", "Main"]

[[lean_lib]]
name = "Challenge"
roots = ["Challenge"]
"""


def theorems(prefix: str) -> str:
    return "".join(f"{prefix}theorem {name} : True := trivial\n" for name in NAMES)


def make_checkout(path: Path, results: str = "In progress.") -> Path:
    files = {
        "lakefile.toml": LAKEFILE,
        "lean-toolchain": "leanprover/lean4:v4.33.1\n",
        "lake-manifest.json": json.dumps({"packages": [{"name": "mathlib", "rev": "0df444a3" + "0" * 32}]}),
        "comparator.json": json.dumps({"theorem_names": NAMES, "permitted_axioms": ["propext", "Quot.sound"]}),
        "src/Main.lean": "import Statements\nimport Alpha.Core.Top\n\n" + theorems(""),
        "src/Statements.lean": "import Mathlib\n\ndef P : Prop := True\n",
        "src/Challenge.lean": "import Mathlib\n\n" + theorems("\n"),
        "src/Alpha/Core/Top.lean": "import Alpha.Core.Deep.Low\nimport Beta.One.X\nimport Mathlib.Tactic\n\n"
                                   "@[simp] theorem a : True := trivial\nlemma b : True := trivial\n\n"
                                   "noncomputable def c : Nat := 0\n",
        "src/Alpha/Core/Deep/Low.lean": "import Mathlib\n\nprivate theorem d : True := by sorry\n"
                                        "structure S where\n  x : Nat\n",
        "src/Alpha/Side/S.lean": "import Alpha.Core.Top\n\ninstance : Inhabited Nat := ⟨0⟩\n",
        "src/Alpha/Loose.lean": "import Lean\n\nabbrev e := 1\n",
        "src/Beta/One/X.lean": "import Mathlib\n\nclass inductive K\n  | k\n-- kexactB here\n",
        "src/Beta/Two/Y.lean": "import Beta.One.X\n\ninductive T\n  | t\n",
        "verification/NOTES.md": f"# Notes\n\nIt printed {rh.SUCCESS} on a smoke test.\n\n## Results\n\n{results}\n",
        "verification/static-scan.txt": "counts\n",
    }
    for name, text in files.items():
        (path / name).parent.mkdir(parents=True, exist_ok=True)
        (path / name).write_text(text, encoding="utf-8")
    git(path, "init", "--quiet")
    commit(path)
    return path


def git(path: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True)


def commit(path: Path) -> None:
    git(path, "add", "-A")
    git(path, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "--quiet", "-m", "c", "--allow-empty")


def read(out: Path) -> dict:
    return rh.load(out.parent)


def test_the_refresh_counts_folders_imports_and_the_scan(tmp_path):
    checkout = make_checkout(tmp_path / "repo")
    out = tmp_path / "data" / rh.ID
    assert rh.refresh(checkout, out) == ([], [])
    data = read(out)
    source, units = data["source"], data["folders"]["units"]
    # Comparator's Challenge.lean is not the submission's.
    assert source["totals"]["files"] == 8
    assert source["totals"]["theorems"] == 5 + 3 and source["totals"]["definitions"] == 7
    assert [lib["name"] for lib in source["libraries"] if lib["comparator"]] == ["Challenge"]
    assert source["theorems"][0] == {"name": "riemannHypothesis", "main_line": 4, "challenge_line": 4}
    assert source["theorems"][1]["challenge_line"] == 6
    assert source["mathlib"].startswith("0df444a3") and source["toolchain"] == "leanprover/lean4:v4.33.1"
    assert set(units) == {"", "Alpha", "Alpha/Core", "Alpha/Side", "Beta/One", "Beta/Two"}
    assert units["Alpha/Core"]["files"] == 2 and units["Alpha/Core"]["theorems"] == 3
    assert units["Alpha/Core"]["sub"] == {"": {"bytes": units["Alpha/Core"]["sub"][""]["bytes"], "definitions": 1,
                                                "files": 1, "lines": 8, "nonblank": 6, "theorems": 2},
                                          "Deep": {"bytes": units["Alpha/Core"]["sub"]["Deep"]["bytes"],
                                                   "definitions": 1, "files": 1, "lines": 5, "nonblank": 4,
                                                   "theorems": 1}}
    assert data["folders"]["imports"]["Alpha/Core"] == {"@Mathlib": 2, "Alpha/Core": 1, "Beta/One": 1}
    assert data["folders"]["imports"][""] == {"": 1, "@Mathlib": 1, "Alpha/Core": 1}
    scan = {pattern["key"]: pattern for pattern in data["scan"]["patterns"]}
    assert scan["sorry"] == {"key": "sorry", "lines": 1, "files": 1}
    assert scan["kexactB"]["files"] == 1 and scan["axiom"]["lines"] == 0
    record = data["verification"]
    assert set(record["files"]) == {"NOTES.md", "static-scan.txt"} and record["comparator"] == {"status": "pending"}


def test_a_changed_verification_folder_is_reported_and_the_data_still_written(tmp_path):
    checkout = make_checkout(tmp_path / "repo")
    out = tmp_path / "data" / rh.ID
    rh.refresh(checkout, out)
    (checkout / "verification" / "comparator-output.txt").write_text("output\n", encoding="utf-8")
    (checkout / "verification" / "NOTES.md").write_text("# Notes\n\n## Results\n\nDone.\n", encoding="utf-8")
    (checkout / "src" / "Alpha" / "More.lean").write_text("theorem f : True := trivial\n", encoding="utf-8")
    commit(checkout)
    problems, changes = rh.refresh(checkout, out)
    assert problems == []
    assert changes == ["verification/comparator-output.txt added", "the Results section of verification/NOTES.md changed"]
    data = read(out)
    assert data["source"]["totals"]["files"] == 9 and data["verification"]["comparator"] == {"status": "pending"}
    # Edits elsewhere in the notes are not a change.
    notes = checkout / "verification" / "NOTES.md"
    notes.write_text("# Notes, edited\n\n## Results\n\nDone.\n", encoding="utf-8")
    assert rh.refresh(checkout, out) == ([], [])


def test_the_script_writes_the_changes_file(tmp_path, monkeypatch):
    checkout = make_checkout(tmp_path / "repo")
    monkeypatch.setattr(refresh_riemann_hypothesis, "ROOT", tmp_path)
    monkeypatch.setattr("sys.argv", ["refresh", str(checkout)])
    assert refresh_riemann_hypothesis.main() == 0
    (checkout / "verification" / "RESULT.md").write_text("x\n", encoding="utf-8")
    changes = tmp_path / "changes.txt"
    monkeypatch.setattr("sys.argv", ["refresh", str(checkout), "--changes", str(changes)])
    assert refresh_riemann_hypothesis.main() == 0
    assert changes.read_text(encoding="utf-8") == "verification/RESULT.md added\n"


def test_a_passing_run_counts_only_once_the_refresh_checked_its_file(tmp_path):
    checkout = make_checkout(tmp_path / "repo")
    out = tmp_path / "data" / rh.ID
    rh.refresh(checkout, out)
    record_path = out / "verification.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    record["comparator"] = {"status": "passed", "file": "verification/run.txt", "commit": "c" * 40}
    record_path.write_text(json.dumps(record), encoding="utf-8")
    # Without the file, or with the notes' smoke test, nothing is written.
    problems, _ = rh.refresh(checkout, out)
    assert problems and "pass that file" in problems[0]
    notes = checkout / "verification" / "NOTES.md"
    problems, _ = rh.refresh(checkout, out, notes)
    assert problems and "does not hold" in problems[0]
    assert "checked" not in json.loads(record_path.read_text(encoding="utf-8"))["comparator"]
    # The chapter refuses a passing status the refresh has not checked.
    with pytest.raises(ValueError, match="has not checked"):
        rh.chapter(read(out))
    evidence = tmp_path / "run.txt"
    evidence.write_text("".join(f"{name}: ok\n" for name in NAMES) + rh.SUCCESS + "\n", encoding="utf-8")
    assert rh.refresh(checkout, out, evidence)[0] == []
    data = read(out)
    assert data["verification"]["comparator"]["checked"]["success"] is True
    built, _ = rh.chapter(data)
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert all(dict(leaf.fields).get("proof") == "formalized" for leaf in leaves)
    assert "Comparator accepted" in leaves[0].body


def test_the_chapter_shows_claims_without_proofs_and_folders_with_parts(tmp_path, monkeypatch):
    checkout = make_checkout(tmp_path / "repo")
    out = tmp_path / "data" / rh.ID
    rh.refresh(checkout, out)
    monkeypatch.setattr(rh, "PART_FILES", 2)
    fc_page = Leaf("Riemann Hypothesis and its generalizations", "rh", [("lean", f"{rh.FC_RH}, GRH.g")], "")
    fc_root = Container("FC", "fc", [])
    fc_root.entries = [Entry(fc_page)]
    built, links = rh.chapter(read(out), fc_root)
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert [leaf.title for leaf in leaves] == NAMES and set(links) == set(NAMES)
    for leaf in leaves:
        fields = dict(leaf.fields)
        assert fields["statement"] == "formalized" and "proof" not in fields and fields["lean"] == leaf.title
        assert "Comparator's check is pending" in leaf.body
    assert built.targets["fc-rh"] is fc_page
    assert [leaf.title for leaf in leaves if leaf.notes] == ["riemannHypothesis", "riemannZeta_eq_zero_re",
                                                             "LFunction_eq_zero_re_of_isPrimitive"]
    containers = [node for node in walk(built.root) if isinstance(node, Container)]
    assert [node.title for node in containers] == [rh.TITLE, "Main and Statements", "Alpha", "Alpha/Core", "Beta"]
    assert "quotes none of its text" in built.root.prose and "no passing Comparator run" in built.root.prose
    assert "no `sorry`" not in built.root.prose and "`sorry` on 1 line in 1 file" in built.root.prose
    beta = containers[-1]
    assert "2 libraries: `Beta` (One) and `BetaFields` (Two)" in beta.prose
    alpha = containers[2]
    assert "| [Core](trough:riemann-hypothesis-folder-Alpha/Core) | 2 |" in alpha.prose
    assert "import modules of Mathlib (2 lines), [Beta](trough:riemann-hypothesis-folder-Beta) (1 line) and Lean (1 line)" in alpha.prose
    assert "Files of [Main and Statements](trough:riemann-hypothesis-folder-root) (1 line) import its modules" in alpha.prose
    core = containers[3]
    assert "[Alpha](trough:riemann-hypothesis-folder-Alpha) (1 line)" in core.prose
    # Every placeholder names a target.
    texts = [node.prose for node in containers] + [leaf.body for leaf in leaves] + [
        text for leaf in leaves for _, text in leaf.notes]
    assert all(match.group(1) in built.targets for text in texts for match in LINK.finditer(text))


def test_the_committed_data_build_the_chapter():
    loaded = rh.load(ROOT / "data")
    assert loaded is not None and loaded["source"]["repo"] == rh.REPO and len(loaded["source"]["rev"]) == 40
    built, links = rh.chapter(loaded)
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert [leaf.title for leaf in leaves] == [theorem["name"] for theorem in loaded["source"]["theorems"]]
    assert all(len(node.children) <= 20 for node in walk(built.root) if isinstance(node, Container))
    assert loaded["verification"]["comparator"]["status"] in ("pending", "passed")
    # No statement text: the pages show no Lean code from the source.
    assert not any(re.search(r"```", leaf.body) for leaf in leaves)
