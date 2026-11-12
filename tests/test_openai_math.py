import json
import os
import subprocess
from pathlib import Path

import refresh_openai_math
from trough import blueprints, openai_math
from trough.vault import Container, Leaf, assign_paths, render_tree, walk


def cell(text: str) -> str:
    return f"<tbody><tr>\n<td>\n\n{text}\n\n</td>\n</tr></tbody>\n"


CONTENTS = ("# Mathematics manuscript collection\n\n<table>\n<thead><tr><th>Result</th></tr></thead>\n"
            + cell("**001. A prime bound.** Proves that every prime <i>p</i> &gt; 2 is odd and $`p^2`$ is odd, with "
                   "<i>x</i><sup>2</sup> and ℤ<sub><i>p</i></sub>.")
            + cell("&emsp;[Odd primes](preprints/Odd-primes-October-1-2026/paper.pdf)\n\nWe prove that primes above 2 "
                   "are odd.")
            + cell("**002. A ring theorem.** Every ring is a ring. ([Lean](lean/docs/002.md))")
            + cell("&emsp;[Rings (and more)](preprints/Rings-(and-more)-October-2-2026/paper.pdf)\n\nRings are rings.")
            + cell("&emsp;[Rings again](preprints/Rings-again-October-3-2026/main.pdf) — secondary writeup\n\nAgain.")
            + cell("**003. Zeta bounds.** The zeta function has no zeros in $`\\Re s > 7/8`$. ([Lean](lean/docs/003.md))")
            + cell("&emsp;[Zeta](preprints/Zeta-October-4-2026/paper.pdf)\n\nA zero-free region.")
            + "</table>\n")
OVERVIEW = ("\\cataloguesection{Number theory}{1}\n\\resultentry{001}{A prime bound}{Proves {it}.}{links}\n"
            "\\resultentry{003}{Zeta}{No zeros.}{links}\n\\cataloguesection{Algebra}{2}\n"
            "\\resultentry{002}{Rings}{Rings.}{links}\n")
DOC_002 = ("# A ring theorem\n\nThe following describes the scope of the Lean formalization related to the following "
           "accompanying paper(s):\n\n- [Rings (and more)](../../preprints/Rings-(and-more)-October-2-2026/paper.pdf)\n\n"
           "## Scope\n\nEvery ring is a ring; see [the statement](../ComparatorChallenges/Ring.lean).\n\n"
           "## Comparator links\n\n| Result | Comparator statement |\n| --- | --- |\n"
           "| Rings are rings | [Ring.lean](../ComparatorChallenges/Ring.lean) |\n")
DOC_003 = ("# Zeta bounds\n\nThe following describes the scope:\n\n- [Zeta](../../preprints/Zeta-October-4-2026/paper.pdf)\n\n"
           "## Scope\n\nA zero-free half-plane $\\Re s > 7/8$.\n\n## Comparator links\n\n"
           "| Result | Comparator statement |\n| --- | --- |\n"
           "| Zeta $7/8$ bound | [Zeta.lean](../ComparatorChallenges/Zeta.lean) |\n"
           "| Hecke bound | [Challenge.lean](../ComparatorChallenges/Hecke/Challenge.lean) |\n")


def config(challenge: str, solution: str, theorems: list[str], definitions: list[str] = ()) -> str:
    return json.dumps({"challenge_module": challenge, "solution_module": solution, "theorem_names": theorems,
                       "definition_names": list(definitions), "permitted_axioms": ["propext"]})


FILES = {
    "CONTENTS.md": CONTENTS,
    "overview.tex": OVERVIEW,
    "lean/docs/002.md": DOC_002,
    "lean/docs/003.md": DOC_003,
    "lean/ComparatorChallenges/Ring.lean": (
        "import Mathlib\n\nnamespace OAI\n\ntheorem ring_is_ring (R : Type) [Ring R] :\n    True := by\n  sorry\n\nend OAI\n"),
    "lean/ComparatorChallenges/Ring.json": config("ComparatorChallenges.Ring", "OAI.Algebra.Ring.Main", ["OAI.ring_is_ring"]),
    "lean/ComparatorChallenges/Zeta.lean": (
        "import Mathlib\n\nnamespace OAI.Zeta\n\ndef region : Set ℂ := sorry\n\n"
        "theorem bound : ∀ s ∈ region, s ≠ 0 := by\n  sorry\n\nend OAI.Zeta\n"),
    "lean/ComparatorChallenges/Zeta.json": config("ComparatorChallenges.Zeta", "OAI.NumberTheory.Zeta.Main",
                                                  ["OAI.Zeta.bound"], ["OAI.Zeta.region"]),
    "lean/ComparatorChallenges/Hecke/Challenge.lean": "namespace OAI.Hecke\n\ntheorem bound : True := by\n  sorry\n\nend OAI.Hecke\n",
    "lean/ComparatorChallenges/Hecke.json": config("ComparatorChallenges.Hecke.Challenge", "OAI.NumberTheory.Hecke.Main",
                                                   ["OAI.Hecke.bound"]),
    "lean/OAI/Algebra/Ring/Main.lean": "namespace OAI\n\ntheorem ring_is_ring (R : Type) [Ring R] : True := trivial\n\nend OAI\n",
    "lean/OAI/NumberTheory/Zeta/Main.lean": (
        "import OAI.NumberTheory.Zeta.Region\n\nnamespace OAI.Zeta\n\ntheorem bound : ∀ s ∈ region, s ≠ 0 := by\n"
        "  sorry\n\nend OAI.Zeta\n"),
    "lean/OAI/NumberTheory/Zeta/Region.lean": "namespace OAI.Zeta\n\ndef region : Set ℂ := ∅\n\nend OAI.Zeta\n",
    "lean/formalization.yaml": (
        'version: "v0.4"\nstatus:\n  main_results:\n    - comparator_config: ComparatorChallenges/Ring.json\n'
        "      declaration: OAI.ring_is_ring\n      file: OAI/Algebra/Ring/Main.lean\n"
        "    - comparator_config: ComparatorChallenges/Gone.json\n      declaration: OAI.gone\n      file: OAI/Gone.lean\n"),
    "lean/lean-toolchain": "leanprover/lean4:v4.34.1\n",
    "lean/lake-manifest.json": json.dumps({"packages": [{"name": "mathlib", "rev": "d" * 40, "inputRev": "v4.34.1"}]}),
}
LICENSE = "                                 Apache License\n                           Version 2.0, January 2004\n"


def write(root: Path, files: dict[str, str]) -> Path:
    for name, text in files.items():
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(text, encoding="utf-8")
    return root


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-10-30T02:35:38+02:00",
           "GIT_COMMITTER_DATE": "2026-10-30T02:35:38+02:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path, files: dict[str, str] = FILES, license_text: str = LICENSE) -> Path:
    write(root, files | {"LICENSE": license_text})
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "collection")
    return root


def build(tmp_path: Path):
    out = tmp_path / "data" / "openai-math"
    assert refresh_openai_math.refresh(checkout(tmp_path / "math"), out) == []
    built, lean_links = openai_math.chapter(openai_math.load(tmp_path / "data"))
    vault = Path("blueprint")
    assign_paths(built.root, vault / "roadmap" / "openai-math")
    blueprints.resolve(built, vault)
    return built, lean_links, render_tree(built.root, vault)


ROOT = Path("blueprint/roadmap/openai-math")


def test_the_collections_html_becomes_the_sites_markdown():
    assert openai_math.markdown("a <i>p</i> &gt; 2 and $`p^2`$") == "a *p* > 2 and $p^2$"
    assert openai_math.markdown("<i>x</i><sup>2</sup>, ℤ<sub><i>p</i></sub>, ℂ<sup><i>n</i></sup>") == (
        "$x^{2}$, ℤ$_{p}$, ℂ$^{n}$")
    assert openai_math.markdown("<i>H</i><sup>1</sup><sub>0</sub> and &#8211;") == "$H^{1}_{0}$ and –"


def test_contents_and_the_overview_give_the_families_in_order(tmp_path):
    families, problems = openai_math.read_contents(CONTENTS)
    assert problems == []
    assert [family["number"] for family in families] == ["001", "002", "003"]
    first = families[0]
    assert first["title"] == "A prime bound" and first["doc"] is None
    assert first["description"] == "Proves that every prime *p* > 2 is odd and $p^2$ is odd, with $x^{2}$ and ℤ$_{p}$."
    assert families[1]["doc"] == "lean/docs/002.md" and families[1]["description"] == "Every ring is a ring."
    assert families[1]["manuscripts"] == [
        {"title": "Rings (and more)", "path": "preprints/Rings-(and-more)-October-2-2026/paper.pdf", "note": "",
         "abstract": "Rings are rings."},
        {"title": "Rings again", "path": "preprints/Rings-again-October-3-2026/main.pdf", "note": "secondary writeup",
         "abstract": "Again."}]
    assert openai_math.read_overview(OVERVIEW) == [{"title": "Number theory", "families": ["001", "003"]},
                                                    {"title": "Algebra", "families": ["002"]}]


def test_a_family_with_lean_gets_its_statements_and_where_the_lean_proves_them(tmp_path):
    structure, families, counts, problems = openai_math.read(checkout(tmp_path / "math"))
    assert problems == []
    assert list(families) == ["Number theory", "Algebra"]
    assert [family["number"] for family in families["Number theory"]] == ["001", "003"]
    ring = families["Algebra"][0]["lean"]
    assert ring["papers"] == ["preprints/Rings-(and-more)-October-2-2026/paper.pdf"]
    [result] = ring["results"]
    assert (result["label"], result["challenge"], result["config"], result["main"]) == (
        "Rings are rings", "lean/ComparatorChallenges/Ring.lean", "lean/ComparatorChallenges/Ring.json", True)
    [statement] = result["statements"]
    assert statement["statement"] == "theorem ring_is_ring (R : Type) [Ring R] :\n    True"
    assert statement["proof"] == {"file": "lean/OAI/Algebra/Ring/Main.lean", "line": 3, "kind": "theorem", "sorry": False}
    zeta, hecke = families["Number theory"][1]["lean"]["results"]
    assert [(entry["name"], entry["role"]) for entry in zeta["statements"]] == [
        ("OAI.Zeta.bound", "theorem"), ("OAI.Zeta.region", "definition")]
    # The theorem's proof is in the solution module, the definition in a module it imports.
    bound, region = (entry["proof"] for entry in zeta["statements"])
    assert (bound["file"], bound["sorry"]) == ("lean/OAI/NumberTheory/Zeta/Main.lean", True)
    assert region["file"] == "lean/OAI/NumberTheory/Zeta/Region.lean"
    # A statement file in a folder of its own, whose solution module is not checked out.
    assert hecke["challenge"] == "lean/ComparatorChallenges/Hecke/Challenge.lean"
    assert hecke["statements"][0]["proof"] is None
    assert {key: counts[key] for key in ("families", "manuscripts", "families_with_lean", "results", "results_main",
                                         "statements", "proofs_found", "proofs_not_found", "proofs_with_sorry",
                                         "main_results", "main_results_unlinked", "subjects")} == {
        "families": 3, "manuscripts": 4, "families_with_lean": 2, "results": 3, "results_main": 1, "statements": 4,
        "proofs_found": 3, "proofs_not_found": 1, "proofs_with_sorry": 1, "main_results": 2,
        "main_results_unlinked": 1, "subjects": 2}


def test_what_does_not_read_or_match_is_listed(tmp_path):
    files = FILES | {"overview.tex": OVERVIEW.replace("\\resultentry{003}", "\\resultentry{004}"),
                     "lean/docs/002.md": DOC_002.replace("Ring.lean)", "Gone.lean)")}
    del files["lean/docs/003.md"]
    _, _, _, problems = openai_math.read(checkout(tmp_path / "math", files))
    assert sorted(problems) == sorted([
        "overview.tex files family 004, which CONTENTS.md does not list",
        "overview.tex does not file family 003",
        "lean/docs/002.md links lean/ComparatorChallenges/Gone.lean, which has no configuration",
        "family 003 links lean/docs/003.md, which is missing"])


def test_the_sparse_checkout_adds_solution_modules_then_their_imports(tmp_path):
    bare = {name: text for name, text in FILES.items() if not name.startswith("lean/OAI/")}
    assert openai_math.solution_files(checkout(tmp_path / "bare", bare)) == [
        "lean/OAI/Algebra/Ring/Main.lean", "lean/OAI/NumberTheory/Hecke/Main.lean", "lean/OAI/NumberTheory/Zeta/Main.lean"]
    assert "lean/OAI/NumberTheory/Zeta/Region.lean" in openai_math.solution_files(checkout(tmp_path / "full"))


def test_the_chapter_has_a_part_per_subject_and_an_article_per_family(tmp_path):
    built, lean_links, files = build(tmp_path)
    root = built.root
    assert [entry.node.title for entry in root.entries] == ["Number theory", "Algebra"]
    assert [entry.node.title for entry in root.entries[0].node.entries] == ["001. A prime bound", "003. Zeta bounds"]
    assert built.stats["families"] == 3 and built.stats["formalized"] == 2 and built.stats["statements"] == 4
    assert all(isinstance(node, (Container, Leaf)) for node in walk(root))
    assert lean_links == {
        "OAI.Zeta.bound": f"https://github.com/openai/math/blob/{built.root.prose.split('/tree/')[1][:40]}/lean/OAI/NumberTheory/Zeta/Main.lean#L5",
        "OAI.Zeta.region": lean_links["OAI.Zeta.region"], "OAI.ring_is_ring": lean_links["OAI.ring_is_ring"]}
    assert lean_links["OAI.Zeta.region"].endswith("/lean/OAI/NumberTheory/Zeta/Region.lean#L3")


def test_an_article_has_its_manuscripts_and_a_block_per_result(tmp_path):
    _, _, files = build(tmp_path)
    zeta = files[ROOT / "number-theory/003-zeta-bounds.md"]
    assert "1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math)" in zeta
    assert "The zeta function has no zeros in $\\Re s > 7/8$." in zeta
    assert "## Zeta\n\nA zero-free region.\n\n[The manuscript](https://github.com/openai/math/blob/" in zeta
    assert "paper.pdf); the Lean below formalizes results from it." in zeta
    assert "## The Lean formalization\n\nA zero-free half-plane $\\Re s > 7/8$." in zeta
    assert "## Lean: Zeta $7/8$ bound" in zeta
    assert "```lean\ntheorem bound : ∀ s ∈ region, s ≠ 0\n```" in zeta
    assert "Main.lean, line 5](" in zeta and "where its value contains `sorry`." in zeta
    assert "Defined in [lean/OAI/NumberTheory/Zeta/Region.lean, line 3](" in zeta
    assert "or a file it imports further down, which this chapter does not read." in zeta
    # Not every statement is proved in a file read, so the card does not say the proof is formalized.
    assert "statement: formalized" in zeta and "proof: formalized" not in zeta
    ring = files[ROOT / "algebra/002-a-ring-theorem.md"]
    assert "/lean/ComparatorChallenges/Ring.lean); one of the main results in the repository's formalization.yaml." in ring
    assert "proof: formalized" in ring
    # A link's parentheses are percent-encoded, and a relative link points to the file at the pin.
    assert "/preprints/Rings-%28and-more%29-October-2-2026/paper.pdf)" in ring
    assert "[the statement](https://github.com/openai/math/blob/" in ring and "/lean/ComparatorChallenges/Ring.lean)" in ring
    assert "[The manuscript](" in ring and "main.pdf), secondary writeup." in ring
    prime = files[ROOT / "number-theory/001-a-prime-bound.md"]
    assert "1 manuscript, with no Lean, quoted from" in prime and "lean:" not in prime


def test_the_root_credits_the_collection_and_counts_what_is_unlinked(tmp_path):
    built, _, files = build(tmp_path)
    root = files[ROOT / "README.md"]
    assert "Its 4 manuscripts form 3 result families, an article each, under the 2 subjects of its overview; 2 with Lean: 4 statements, 2 of them proved in a file this chapter reads." in root
    assert "1 main result of the repository's formalization.yaml is not linked from any family's Lean page." in root
    assert "under its Apache-2.0 license." in root


def test_the_refresh_writes_the_source_the_structure_and_the_families(tmp_path):
    out = tmp_path / "data" / "openai-math"
    repo = checkout(tmp_path / "math")
    assert refresh_openai_math.refresh(repo, out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    assert (source["repo"], source["rev"], source["date"], source["toolchain"], source["mathlib_version"]) == (
        "openai/math", git(repo, "rev-parse", "HEAD").strip(), "2026-10-30T00:35:38Z", "v4.34.1", "v4.34.1")
    assert sorted(path.name for path in (out / "families").iterdir()) == ["algebra.json", "number-theory.json"]
    structure = json.loads((out / "structure.json").read_text(encoding="utf-8"))
    assert structure["schema"] == openai_math.SCHEMA and [subject["title"] for subject in structure["subjects"]] == [
        "Number theory", "Algebra"]


def test_the_refresh_writes_nothing_from_a_checkout_it_cannot_read(tmp_path):
    out = tmp_path / "out"
    mit = checkout(tmp_path / "mit", license_text="MIT License\n")
    assert refresh_openai_math.refresh(mit, out) == [f"openai/math at {git(mit, 'rev-parse', 'HEAD')[:8]}: its LICENSE is not Apache-2.0"]
    assert not out.exists()
    (out / "families").mkdir(parents=True)
    (out / "families" / "old.json").write_text(json.dumps({"families": [{"number": f"{n:03d}"} for n in range(7)]}),
                                               encoding="utf-8")
    assert refresh_openai_math.refresh(checkout(tmp_path / "math"), out) == ["3 families, under half the 7 of the last record"]
    assert not (out / "source.json").exists()


def test_braces_outside_formulas_are_escaped():
    assert openai_math.braces("a {b} and $\\{x\\}$ and `{c}`") == "a \\{b} and $\\{x\\}$ and `{c}`"


def test_a_row_that_links_a_line_states_the_declaration_there_or_the_next(tmp_path):
    rows = ("| Region | [Zeta.lean](../ComparatorChallenges/Zeta.lean#L5) |\n"
            "| Bound | [Zeta.lean](../ComparatorChallenges/Zeta.lean#L6) |\n")
    files = FILES | {"lean/docs/003.md": DOC_003.split("| Zeta $7/8$")[0] + rows}
    _, families, _, problems = openai_math.read(checkout(tmp_path / "math", files))
    assert problems == []
    region, bound = families["Number theory"][1]["lean"]["results"]
    assert (region["line"], [entry["name"] for entry in region["statements"]]) == (5, ["OAI.Zeta.region"])
    assert (bound["line"], [entry["name"] for entry in bound["statements"]]) == (6, ["OAI.Zeta.bound"])
