import json
import os
import subprocess
import urllib.error
import urllib.request
from pathlib import Path

import pytest

import refresh_anthropic_flt
from trough import anthropic_flt, blueprints, catalog
from trough.vault import Container, Entry, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "a" * 40
BLOB = f"https://github.com/anthropics/fermats-last-theorem/blob/{REV}"

# Five theorems: root_thm cites C.first, which cites A.helper, which cites A.step and B.deep; A.step cites
# B.deep. A.helper is not a landmark.
META = "window.FLT_META=" + json.dumps({
    "v": 1,
    "aliases": {"root_thm": "Root; R", "A.step": "Step", "A.helper": "Not a landmark"},
    "names": ["A.step", "A.helper", "B.deep", "root_thm", "C.first"],
    "stemx": {},
    "stage": [2, 2, 2, 0, 1],
    "lm": [1, 0, 1, 1, 1],
    "defs": ["Def_One"],
    "stages": {"0": "The statement", "1": "First", "2": "Second", "3": "Exact strength"},
}) + ";\n"
EDGES = "window.FLT_EDGES={off:[0,1,3,3,4,5],dst:[2,0,2,4,1]};\n"

PROOF_PATH = """# The route

Intro with E_P and `X.y`.

**1. First step.** `root_thm` follows from `C.first`.

**2. Second step ≥ 2.** `A.step`, adapted from the Imperial College London FLT project, proves it from:
- `B.deep (h : q ≠ 2) : q = q`, with F_p;
- nothing else.

## Exact strength

- **Named.** Proved: `B.deep`, in the strength needed. Not proved: more.
- **Left.** Not proved: anything else.
- **Other.** `C.first` holds as stated.
"""

YAML = """version: "v0.4"
project:
  name: "FLT"
  description: "A proof, built on Mathlib."
  authors: ["Anthropic"]
  license: "Apache-2.0"
sources:
  - title: "Modular elliptic curves and Fermat's Last Theorem"
    authors: ["Andrew Wiles"]
    id: "doi:10.2307/2118559"
    type: "article"
    location: "Annals of Mathematics 141 (1995), 443-551"
    relationship: "adapts"
status:
  scope: "The full statement."
  main_results:
    - declaration: "A.step"
      file: "Theorems/Thm_A_step.lean"
      sorry_count: 0
      axioms: ["propext", "Classical.choice", "Quot.sound"]
    - declaration: "flt_mathlib"
      file: "FinalCheck.lean"
    - file: "Unnamed.lean"
automation:
  methods:
    - method: "agent"
review:
  status: "self-assessed"
  notes: "Machine-checked."
acknowledgements: "Portions derive from the Imperial College London FLT project."
"""

STATEMENTS = {
    "Theorems/Thm_A_step.lean": (
        "import Mathlib\nimport P2M.Sol.S_A_step\nattribute [-instance] Foo.bar Foo.baz\nattribute [-simp] Baz.qux\n\n"
        "open Foo\ntheorem A.step (P : T) : f (K := x) P = y := by p2m_exact_reverting @_root_.P2MW.S_A_step.solution\n"),
    "Theorems/Thm_B_deep.lean": (
        "import P2M.Sol.S_B_deep\nattribute [-instance] Foo.bar\n"
        "local notation \"Γ:=\" => (G := 1)\nnamespace B\ntheorem deep {q : ℕ}\n    (h : q ≠ 2) : q = q := by\n"
        "  exact rfl\nend B\n"),
    "Theorems/Thm_root_thm.lean": "import P2M.Sol.S_root_thm\ntheorem\nroot_thm (n : ℕ) : n = n := by p2m_exact_reverting @x\n",
    "Theorems/Thm_C_first.lean": "import P2M.Sol.S_C_first\ntheorem C.first : True := by trivial\ntheorem Imp.shared : True := trivial\n",
}
APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"
MANIFEST = {"packages": [{"name": "mathlib", "url": "https://github.com/leanprover-community/mathlib4", "rev": "c" * 40}]}


def checkout(tmp_path: Path, **changes: str) -> Path:
    root = tmp_path / "flt"
    files = {"PROOF-PATH.md": PROOF_PATH, "formalization.yaml": YAML, "html/data/meta.js": META,
             "html/data/edges.js": EDGES, "lean-toolchain": "leanprover/lean4:v4.33.1\n",
             "lake-manifest.json": json.dumps(MANIFEST), "LICENSE": APACHE,
             "FinalCheck.lean": "import Theorems.Thm_root_thm\ntheorem flt_mathlib : True := trivial\n", **STATEMENTS}
    files.update(changes)
    for path, text in files.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    return root


def paths_of(root: Path) -> set[str]:
    # The proof modules are not checked out, but the commit has them, as `git ls-tree` would say.
    return {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()} | {
        "P2M/Sol/S_A_step.lean", "P2M/Sol/S_B_deep.lean"}


def records(tmp_path, **changes):
    root = checkout(tmp_path, **changes)
    return anthropic_flt.read_repository(root, REV, "2026-09-24T14:06:36Z", paths_of(root))


def test_both_data_scripts_are_read():
    assert anthropic_flt.read_js(META)["names"][3] == "root_thm"
    assert anthropic_flt.read_js(EDGES) == {"off": [0, 1, 3, 3, 4, 5], "dst": [2, 0, 2, 4, 1]}


def test_a_statement_runs_from_the_preamble_to_the_top_level_colon_equals():
    stated = anthropic_flt.statement(STATEMENTS["Theorems/Thm_A_step.lean"])
    # The `:=` of a named argument is inside parentheses, so the statement goes on past it.
    assert stated == {"name": "A.step", "line": 7, "statement": "open Foo\ntheorem A.step (P : T) : f (K := x) P = y"}
    deep = anthropic_flt.statement(STATEMENTS["Theorems/Thm_B_deep.lean"])
    assert deep["name"] == "B.deep" and deep["line"] == 5
    assert deep["statement"] == ('local notation "Γ:=" => (G := 1)\nnamespace B\ntheorem deep {q : ℕ}\n'
                                 "    (h : q ≠ 2) : q = q")
    # A name on the line after the keyword is read too.
    assert anthropic_flt.statement(STATEMENTS["Theorems/Thm_root_thm.lean"]) == {
        "name": "root_thm", "line": 2, "statement": "theorem\nroot_thm (n : ℕ) : n = n"}
    assert anthropic_flt.statement("import Mathlib\nattribute [-simp] x\ndef f : ℕ := 1\n") is None
    assert anthropic_flt.statement("theorem t : True\n") is None
    # A `let` in the statement has a top-level `:=` too: what follows the cut opens no proof, so it is refused.
    with pytest.raises(ValueError, match="of t does not open a tactic proof"):
        anthropic_flt.statement("theorem t : let x := 1; x = x := by rfl\n")


def test_a_landmark_reaches_the_nearest_landmarks_through_other_theorems():
    edges = anthropic_flt.read_js(EDGES)
    landmarks = {0, 2, 3, 4}
    reach = {index: anthropic_flt.nearest(index, edges["off"], edges["dst"], landmarks) for index in landmarks}
    # C.first reaches A.step and B.deep through A.helper; root_thm stops at C.first.
    assert reach == {0: {2}, 2: set(), 3: {4}, 4: {0, 2}}


def test_proof_path_gives_the_intro_steps_and_later_sections():
    route = anthropic_flt.proof_path(PROOF_PATH)
    assert route["title"] == "The route" and route["intro"] == "Intro with E_P and `X.y`."
    assert [(step["number"], step["title"]) for step in route["steps"]] == [(1, "First step"), (2, "Second step ≥ 2")]
    assert route["steps"][1]["text"].startswith("**2. Second step ≥ 2.** `A.step`, adapted")
    assert route["steps"][1]["text"].endswith("- nothing else.")
    assert [section["title"] for section in route["sections"]] == ["Exact strength"]
    assert route["sections"][0]["text"].endswith("- **Other.** `C.first` holds as stated.")


def test_a_code_span_names_a_landmark_alone_or_with_its_signature():
    names = {"A.step", "B.deep"}
    assert anthropic_flt.mentions("`B.deep (h : q ≠ 2) : q = q`, `A.step`, `B.deeper`, `A.step.x`, `B.deep`", names) == [
        "B.deep", "A.step"]


def test_a_section_keeps_each_proved_clause_and_cuts_what_follows():
    assert anthropic_flt.proved_only(anthropic_flt.proof_path(PROOF_PATH)["sections"][0]["text"]) == (
        "- **Named.** Proved: `B.deep`, in the strength needed. …\n- **Other.** `C.first` holds as stated.")
    # A sentence ends at a period outside code.
    assert anthropic_flt.proved_only("- **X.** Proved: `a.b` and\n  `c.d`. Rest.\n") == "- **X.** Proved: `a.b` and\n  `c.d`. …\n"


def test_the_records_hold_the_facts_steps_and_landmarks(tmp_path):
    source, landmarks = records(tmp_path)
    assert source["schema"] == anthropic_flt.SOURCE_SCHEMA and source["rev"] == REV
    assert source["toolchain"] == "v4.33.1" and source["mathlib"] == "c" * 40 and source["license"] == "Apache-2.0"
    assert source["review"] == {"status": "self-assessed", "notes": "Machine-checked.", "reviewers": []}
    assert source["automation"]["methods"] == [{"method": "agent"}] and source["scope"] == "The full statement."
    assert source["acknowledgements"].startswith("Portions derive")
    assert source["main_results"] == [
        {"name": "A.step", "file": "Theorems/Thm_A_step.lean", "found": {"line": 7, "kind": "theorem", "stated": False},
         "sorry_count": 0, "axioms": ["propext", "Classical.choice", "Quot.sound"]},
        {"name": "flt_mathlib", "file": "FinalCheck.lean", "found": {"line": 2, "kind": "theorem", "stated": False}}]
    assert landmarks["counts"] == {"theorems": 5, "landmarks": 4, "edges": 5, "landmark_edges": 4,
                                   "definition_modules": 1}
    by_name = {record["name"]: record for record in landmarks["landmarks"]}
    assert list(by_name) == ["A.step", "B.deep", "root_thm", "C.first"]
    assert by_name["A.step"] == {
        "name": "A.step", "aliases": ["Step"], "stage": 2, "file": "Theorems/Thm_A_step.lean", "line": 7,
        "statement": "open Foo\ntheorem A.step (P : T) : f (K := x) P = y", "proof_file": "P2M/Sol/S_A_step.lean",
        "reaches": ["B.deep"]}
    assert by_name["root_thm"]["aliases"] == ["Root", "R"] and by_name["root_thm"]["reaches"] == ["C.first"]
    # The proof module a statement file imports is kept only when the commit has it.
    assert "proof_file" not in by_name["C.first"]
    assert by_name["C.first"]["also_declares"] == ["Imp.shared"]
    assert by_name["C.first"]["reaches"] == ["A.step", "B.deep"]


def test_records_are_refused_when_the_source_does_not_hold(tmp_path):
    with pytest.raises(ValueError, match="not Apache-2.0"):
        records(tmp_path / "1", **{"LICENSE": "MIT License\n"})
    with pytest.raises(ValueError, match="'MIT'"):
        records(tmp_path / "2", **{"formalization.yaml": YAML.replace('license: "Apache-2.0"', 'license: "MIT"')})
    with pytest.raises(ValueError, match="states C.first, not B.deep"):
        records(tmp_path / "3", **{"Theorems/Thm_B_deep.lean": STATEMENTS["Theorems/Thm_C_first.lean"]})
    with pytest.raises(ValueError, match="edges.js has 5 offsets and 5 edges for 5 theorems"):
        records(tmp_path / "7", **{"html/data/edges.js": "window.FLT_EDGES={off:[0,1,3,3,5],dst:[2,0,2,4,1]};\n"})
    with pytest.raises(ValueError, match="Thm_root_thm.lean: the text after the top-level `:=` of root_thm"):
        records(tmp_path / "8", **{"Theorems/Thm_root_thm.lean": "theorem root_thm : let x := 1; x = x := by rfl\n"})
    with pytest.raises(ValueError, match="numbered \\[1, 3\\]"):
        records(tmp_path / "4", **{"PROOF-PATH.md": PROOF_PATH.replace("**2. Second", "**3. Second")})
    with pytest.raises(ValueError, match="B.deep is in stage 3"):
        records(tmp_path / "5", **{"html/data/meta.js": META.replace('"stage": [2, 2, 2', '"stage": [2, 2, 3')})
    root = checkout(tmp_path / "6")
    with pytest.raises(ValueError, match="Thm_B_deep.lean is missing"):
        anthropic_flt.read_repository(root, REV, "", paths_of(root) - {"Theorems/Thm_B_deep.lean"})
    # A sparse checkout that leaves out a main result's file must not read as the file not declaring it.
    (root / "FinalCheck.lean").unlink()
    with pytest.raises(ValueError, match="flt_mathlib: FinalCheck.lean is in the commit but not in the checkout"):
        anthropic_flt.read_repository(root, REV, "", paths_of(root) | {"FinalCheck.lean"})


def test_files_lists_the_statement_and_main_result_files(tmp_path, monkeypatch, capsys):
    # meta.js gives B.deep's file a stem of its own.
    meta = META.replace('"stemx": {}', '"stemx": {"2": "B_deep_1"}')
    root = checkout(tmp_path, **{"html/data/meta.js": meta})
    monkeypatch.setattr("sys.argv", ["refresh_anthropic_flt.py", str(root), "--files"])
    assert refresh_anthropic_flt.main() == 0
    assert capsys.readouterr().out.split() == ["Theorems/Thm_A_step.lean", "Theorems/Thm_B_deep_1.lean",
                                               "Theorems/Thm_root_thm.lean", "Theorems/Thm_C_first.lean",
                                               "FinalCheck.lean"]


def git(path: Path, *args: str) -> None:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-09-24T16:06:36+02:00",
           "GIT_COMMITTER_DATE": "2026-09-24T16:06:36+02:00"}
    subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, env=env)


def repository(root: Path) -> Path:
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "release")
    return root


def site(served: dict[str, bytes | None]):
    def fetch(url: str, method: str) -> bytes | None:
        return served.get(url.removeprefix("https://docs.example/"))
    return fetch


def test_the_refresh_writes_both_records_or_none(tmp_path):
    root, out = repository(checkout(tmp_path)), tmp_path / "out"
    assert refresh_anthropic_flt.refresh(root, out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    assert source["date"] == "2026-09-24T14:06:36Z" and len(source["rev"]) == 40 and "docs" not in source
    assert len(json.loads((out / "landmarks.json").read_text(encoding="utf-8"))["landmarks"]) == 4
    # A last record with more than twice the landmarks stops the refresh, and both records stay as they were.
    (out / "landmarks.json").write_text(json.dumps({"landmarks": [{}] * 9}), encoding="utf-8")
    (out / "source.json").write_text("{}", encoding="utf-8")
    assert refresh_anthropic_flt.refresh(root, out) == ["4 landmarks, under half the 9 of the last record"]
    assert (out / "source.json").read_text(encoding="utf-8") == "{}"
    (root / "LICENSE").write_text("MIT License\n", encoding="utf-8")
    git(root, "commit", "--quiet", "-am", "relicense")
    assert refresh_anthropic_flt.refresh(root, tmp_path / "none")[0].startswith("not Apache-2.0")
    assert not (tmp_path / "none").exists()


def test_the_documentation_site_is_linked_only_when_it_serves_the_landmarks_pages(tmp_path):
    _, landmarks = records(tmp_path)
    shards = {f"data/shard/{anthropic_flt.shard(name)}.js": b"" for name in ("A.step", "B.deep", "root_thm", "C.first")}
    served = {"thm.html": b'<div id="thm-main"></div>', "data/meta.js": META.encode(), **shards}
    assert anthropic_flt.docs_problem("https://docs.example/", landmarks, site(served)) is None
    assert "thm.html" in anthropic_flt.docs_problem("https://docs.example/", landmarks, site(served | {"thm.html": None}))
    fewer = META.replace('"lm": [1, 0, 1, 1, 1]', '"lm": [1, 0, 1, 1, 0]').encode()
    assert "marks 3 landmarks, not the 4" in anthropic_flt.docs_problem(
        "https://docs.example/", landmarks, site(served | {"data/meta.js": fewer}))
    missing = next(iter(shards))
    assert missing in anthropic_flt.docs_problem("https://docs.example/", landmarks, site(served | {missing: None}))
    # The pages' script puts a theorem in shard FNV-1a(name) mod 256; FNV-1a("a") is 0xe40c292c.
    assert anthropic_flt.shard("a") == f"{0xE40C292C % 256:03d}" == "044"
    root, out = repository(checkout(tmp_path / "repo")), tmp_path / "out"
    assert refresh_anthropic_flt.refresh(root, out, "https://docs.example/", site(served)) == []
    assert json.loads((out / "source.json").read_text(encoding="utf-8"))["docs"] == "https://docs.example/"

    def down(url: str, method: str) -> bytes | None:
        raise anthropic_flt.Unreachable(url)

    # A site that does not answer at all keeps the last record's link, so an outage changes nothing.
    assert refresh_anthropic_flt.refresh(root, out, "https://docs.example/", down) == []
    assert json.loads((out / "source.json").read_text(encoding="utf-8"))["docs"] == "https://docs.example/"
    # A site that answers without the pages loses it.
    assert refresh_anthropic_flt.refresh(root, out, "https://docs.example/", site({})) == []
    assert "docs" not in json.loads((out / "source.json").read_text(encoding="utf-8"))
    assert refresh_anthropic_flt.refresh(root, out, "https://docs.example/", down) == []
    assert "docs" not in json.loads((out / "source.json").read_text(encoding="utf-8"))


def test_a_request_is_retried_and_only_a_missing_page_is_an_answer(monkeypatch):
    calls = []

    def unanswered(request, timeout):
        calls.append(request.full_url)
        raise urllib.error.URLError("no route")

    monkeypatch.setattr(urllib.request, "urlopen", unanswered)
    with pytest.raises(anthropic_flt.Unreachable):
        refresh_anthropic_flt.fetch("https://docs.example/thm.html", "GET", attempts=3, wait=0)
    assert len(calls) == 3

    def missing(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 404, "Not Found", None, None)

    monkeypatch.setattr(urllib.request, "urlopen", missing)
    assert refresh_anthropic_flt.fetch("https://docs.example/thm.html", "HEAD", wait=0) is None


def imperial_chapter() -> Container:
    shared = Leaf("A shared name", "shared", [("lean", "Imp.shared")], "")
    named = Leaf("The root", "root", [("lean", "Other.name, root_thm")], "")
    plain = Leaf("No Lean", "plain", [("declaration", "theorem")], "")
    frey = Leaf("The Frey package", "frey", [("lean", "FreyPackage")], "")
    return Container("Fermat's Last Theorem (Imperial)", "flt", [Entry(shared), Entry(named), Entry(plain), Entry(frey)])


def build(tmp_path, docs: str | None = None, imperial: Container | None = None):
    source, landmarks = records(tmp_path)
    if docs:
        source["docs"] = docs
    vault = Path("blueprint")
    if imperial:
        assign_paths(imperial, vault / "roadmap" / "flt")
    built, links = anthropic_flt.chapter(source, landmarks, imperial)
    assign_paths(built.root, vault / "roadmap" / "anthropic-flt")
    blueprints.resolve(built, vault)
    return built, links, render_tree(built.root, vault)


def test_a_part_per_step_holds_the_landmarks_of_its_stage(tmp_path):
    built, links, files = build(tmp_path)
    parts = [entry.node for entry in built.root.entries]
    assert [part.title for part in parts] == ["1. First step", "2. Second step ≥ 2", "Exact strength"]
    # The theorem itself, in the stage before the first step, opens the first step.
    assert [(entry.node.title, entry.owned) for entry in parts[0].entries] == [("root_thm", True), ("C.first", True)]
    # A.step opens its step in backticks, so it takes the step's name.
    assert [(entry.node.title, entry.owned) for entry in parts[1].entries] == [("Second step ≥ 2", True), ("B.deep", True)]
    # The section after the steps places nothing and links what its quoted text names.
    assert [(entry.node.title, entry.owned) for entry in parts[2].entries] == [("B.deep", False), ("C.first", False)]
    assert built.stats == {"imperial_matches": 0, "articles": 4, "landmark_edges": 4, "parts": 3, "theorems": 5,
                           "edges": 5}
    assert links == {"A.step": f"{BLOB}/Theorems/Thm_A_step.lean#L7", "B.deep": f"{BLOB}/Theorems/Thm_B_deep.lean#L5",
                     "root_thm": f"{BLOB}/Theorems/Thm_root_thm.lean#L2", "C.first": f"{BLOB}/Theorems/Thm_C_first.lean#L2"}
    page = files[Path("blueprint/roadmap/anthropic-flt/2-second-step-2/README.md")]
    # Quoted as GitHub reads it: underscores outside code escaped, a blank line before the list.
    assert ("> **2. Second step ≥ 2.** `A.step`, adapted from the Imperial College London FLT project, proves it from:\n"
            ">\n> - `B.deep (h : q ≠ 2) : q = q`, with F\\_p;\n> - nothing else.") in page
    assert f"*Quoted from the route of the proof in [PROOF-PATH.md]({BLOB}/PROOF-PATH.md) of " in page
    # B.deep's span carries its signature, and still counts as naming it.
    assert "in the order this step names them:\n\n- [Second step ≥ 2](a-step.md)\n- [B.deep](b-deep.md)" in page
    first = files[Path("blueprint/roadmap/anthropic-flt/1-first-step/README.md")]
    assert ("The theorem itself, which the repository's web pages place before this step, then the landmarks they "
            "place in it, in the order this step names them:\n\n- [root_thm](root-thm.md)\n- [C.first](c-first.md)") in first
    section = files[Path("blueprint/roadmap/anthropic-flt/exact-strength/README.md")]
    assert "> - **Named.** Proved: `B.deep`, in the strength needed. …\n> - **Other.** `C.first` holds as stated." in section
    assert "Not proved" not in section and "Left" not in section
    assert (f"*Quoted from the section “Exact strength” of [PROOF-PATH.md]({BLOB}/PROOF-PATH.md) of "
            "[anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit "
            f"[aaaaaaaa](https://github.com/anthropics/fermats-last-theorem/tree/{REV}), Apache-2.0: each “Proved:” "
            "clause, cut with … where the text goes on.*") in section
    assert "No landmark is placed in this section. The landmarks it names" in section
    assert "- [B.deep](../2-second-step-2/b-deep.md)\n- [C.first](../1-first-step/c-first.md)" in section


def test_an_article_quotes_its_statement_aliases_and_dependencies(tmp_path):
    _, _, files = build(tmp_path, docs="https://docs.example/")
    page = files[Path("blueprint/roadmap/anthropic-flt/2-second-step-2/a-step.md")]
    assert page.startswith("---\ndeclaration: theorem\norigin: cited\nlean: A.step\nstatement: formalized\n"
                           "proof: formalized\n---\n\n# Second step ≥ 2\n\n```lean\nopen Foo\n"
                           "theorem A.step (P : T) : f (K := x) P = y\n```\n")
    assert f"*Quoted from [Theorems/Thm_A_step.lean, line 7]({BLOB}/Theorems/Thm_A_step.lean#L7) of " in page
    assert "Aliases on the repository's web pages: “Step”." in page
    assert "PROOF-PATH.md names it in [2. Second step ≥ 2](README.md), as the theorem that carries step 2." in page
    deep = files[Path("blueprint/roadmap/anthropic-flt/2-second-step-2/b-deep.md")]
    assert "PROOF-PATH.md names it in [2. Second step ≥ 2](README.md) and [Exact strength](../exact-strength/README.md)." in deep
    assert f"## Depends on\n\n{anthropic_flt.NO_STATEMENT_EDGES}\n\n## Proof depends on\n\n- [B.deep](b-deep.md)" in page
    assert f"and proved in [P2M/Sol/S_A_step.lean]({BLOB}/P2M/Sol/S_A_step.lean)." in page
    assert "- [The repository's documentation page for `A.step`](https://docs.example/thm.html#A.step)" in page
    first = files[Path("blueprint/roadmap/anthropic-flt/1-first-step/c-first.md")]
    assert "## Proof depends on\n\n- [Second step ≥ 2](../2-second-step-2/a-step.md)\n- [B.deep](../2-second-step-2/b-deep.md)" in first
    assert "Aliases" not in first and "Imperial FLT" not in first


def test_the_intro_attributes_what_it_quotes_and_counts_the_rest(tmp_path):
    _, _, files = build(tmp_path)
    page = files[Path("blueprint/roadmap/anthropic-flt/README.md")]
    assert "by Anthropic, read at commit [aaaaaaaa](" in page and " (2026-09-24)." in page
    assert "> A proof, built on Mathlib.\n\n*Quoted from the project description in [formalization.yaml]" in page
    assert "> Intro with E\\_P and `X.y`.\n\n*Quoted from [PROOF-PATH.md]" in page
    assert "> Portions derive from the Imperial College London FLT project." in page
    assert "list 5 theorems and mark 4 of them as landmarks" in page and "the other theorem is counted" in page
    assert "The web pages put `root_thm` in a stage before the first step, so it opens part 1." in page
    assert "4 edges in all" in page and "Imperial FLT chapter" not in page
    assert "Articles link the repository's files at the commit above." in page
    assert "## The route\n\n- [1. First step](1-first-step/README.md)" in page
    assert "- Review status: “self-assessed”." in page and "- Scope, as its status states: “The full statement.”" in page
    assert (f"- `A.step`, stated in [Theorems/Thm_A_step.lean, line 7]({BLOB}/Theorems/Thm_A_step.lean#L7); its article: "
            "[A.step](2-second-step-2/a-step.md); sorry count 0; axioms `propext`, `Classical.choice`, `Quot.sound`.") in page
    assert f"- `flt_mathlib`, stated in [FinalCheck.lean, line 2]({BLOB}/FinalCheck.lean#L2)." in page
    assert "Annals of Mathematics 141 (1995), 443-551 (article; adapts)." in page


def test_a_name_the_imperial_chapter_shares_is_linked(tmp_path):
    built, _, files = build(tmp_path, imperial=imperial_chapter())
    assert built.stats["imperial_matches"] == 2
    root = files[Path("blueprint/roadmap/anthropic-flt/1-first-step/root-thm.md")]
    assert "- `root_thm`, its name, is also the Lean name of [root_thm](../../flt/root.md) in the Imperial FLT chapter." in root
    first = files[Path("blueprint/roadmap/anthropic-flt/1-first-step/c-first.md")]
    assert ("- `Imp.shared`, which its statement file also declares, is also the Lean name of "
            "[Imp.shared](../../flt/shared.md) in the Imperial FLT chapter.") in first
    page = files[Path("blueprint/roadmap/anthropic-flt/README.md")]
    assert "[Imperial FLT chapter](../flt/README.md)" in page and "At this commit 2 names do." in page
    # PROOF-PATH.md says the Frey package is adapted from the Imperial project, which has an article on its own.
    assert ("The repository's `FreyPackage` is adapted from the Imperial College London FLT project, as PROOF-PATH.md "
            "says, and the Imperial FLT chapter has an article on its [`FreyPackage`](../flt/frey.md).") in page
    assert built.stats["imperial_matches"] == 2


def test_the_committed_data_build_the_chapter():
    loaded = anthropic_flt.load(ROOT / "data")
    assert loaded is not None
    source, landmarks = loaded
    assert source["schema"] == anthropic_flt.SOURCE_SCHEMA and landmarks["schema"] == anthropic_flt.LANDMARKS_SCHEMA
    assert len(source["rev"]) == 40 and landmarks["rev"] == source["rev"] and source["license"] == "Apache-2.0"
    built, links = anthropic_flt.chapter(source, landmarks)
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert len(leaves) == built.stats["articles"] == landmarks["counts"]["landmarks"] > 0
    assert set(links) == {dict(leaf.fields)["lean"] for leaf in leaves}
    assert built.stats["landmark_edges"] == landmarks["counts"]["landmark_edges"]
    entry = next(library for library in catalog.load(ROOT / "catalog" / "libraries.toml") if library["id"] == "anthropic-flt")
    assert entry["map_status"] == "live" and "head" not in entry
    page = catalog.sources_readme([entry], "m" * 40, None, anthropic_flt=source)
    assert f"at {source['rev'][:12]}: " in page and "## Fermat's Last Theorem (Anthropic)" in page
