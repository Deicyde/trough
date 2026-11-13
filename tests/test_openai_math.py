import json
import os
import subprocess
from pathlib import Path

import pytest

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
        'version: "v0.4"\nproject:\n  name: "OpenAI math repository"\n'
        '  description: "Lean formalizations accompanying a mathematics manuscript collection."\n'
        '  authors: ["OpenAI"]\n  license: "Apache-2.0"\nsources:\n  - title: "Rings (and more)"\n'
        "    id: ../preprints/Rings-(and-more)-October-2-2026/paper.pdf\nautomation:\n  methods:\n    - method: agent\n"
        "review:\n  status: unchecked\nstatus:\n  main_results:\n    - comparator_config: ComparatorChallenges/Ring.json\n"
        "      declaration: OAI.ring_is_ring\n      file: OAI/Algebra/Ring/Main.lean\n"
        "    - comparator_config: ComparatorChallenges/Gone.json\n      declaration: OAI.gone\n      file: OAI/Gone.lean\n"),
    "README.md": (
        "# Readme\n\nThis repository contains manuscripts produced by a model. \n\nNot all have Lean.\n\n"
        "Some of the unformalized results could have issues. We will fix them.\n\nIn our view, these manuscripts are "
        "raw research data, rather than polished academic papers.\n\n## How the results were produced\n\n"
        "The vast majority of results were obtained with one procedure. Each took three hours.\n\n"
        "Exceptions to this fixed procedure include the zeta work. Additionally, its writeup was human\nedited.\n"),
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


def build(tmp_path: Path, files: dict[str, str] = FILES):
    out = tmp_path / "data" / "openai-math"
    assert refresh_openai_math.refresh(checkout(tmp_path / "math", files), out) == []
    built, lean_links = openai_math.chapter(openai_math.load(tmp_path / "data"))
    vault = Path("blueprint")
    assign_paths(built.root, vault / "roadmap" / "openai-math")
    blueprints.resolve(built, vault)
    return built, lean_links, render_tree(built.root, vault)


ROOT = Path("blueprint/roadmap/openai-math")
REPO_ROOT = Path(__file__).resolve().parent.parent


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
    assert statement["statement"] == "theorem ring_is_ring (R : Type) [Ring R] :\n    True" and statement["main"]
    assert statement["proof"] == {"file": "lean/OAI/Algebra/Ring/Main.lean", "line": 3, "kind": "theorem", "sorry": False}
    zeta, hecke = families["Number theory"][1]["lean"]["results"]
    assert [(entry["name"], entry["role"]) for entry in zeta["statements"]] == [
        ("OAI.Zeta.bound", "theorem"), ("OAI.Zeta.region", "definition")]
    # The theorem's proof is in the solution module, the definition in a module it imports.
    bound, region = (entry["proof"] for entry in zeta["statements"])
    assert (bound["file"], bound["sorry"]) == ("lean/OAI/NumberTheory/Zeta/Main.lean", True)
    assert region["file"] == "lean/OAI/NumberTheory/Zeta/Region.lean"
    # A statement file in a folder of its own, whose solution module is absent at the commit.
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
    # The files formalization.yaml names for its main results are read too.
    assert openai_math.solution_files(checkout(tmp_path / "bare", bare)) == [
        "lean/OAI/Algebra/Ring/Main.lean", "lean/OAI/Gone.lean", "lean/OAI/NumberTheory/Hecke/Main.lean",
        "lean/OAI/NumberTheory/Zeta/Main.lean"]
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
        "OAI.Zeta.region": lean_links["OAI.Zeta.region"], "OAI.ring_is_ring": lean_links["OAI.ring_is_ring"],
        "OAI.Hecke.bound": lean_links["OAI.Hecke.bound"]}
    assert lean_links["OAI.Zeta.region"].endswith("/lean/OAI/NumberTheory/Zeta/Region.lean#L3")
    # A statement with no proof found links its own line.
    assert lean_links["OAI.Hecke.bound"].endswith("/lean/ComparatorChallenges/Hecke/Challenge.lean#L3")


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
    assert "Stated in [Zeta.lean, line 7](https://github.com/openai/math/blob/" in zeta
    assert "/lean/ComparatorChallenges/Zeta.lean#L7). Declared in [" in zeta
    assert "main results" not in zeta
    ring = files[ROOT / "algebra/002-a-ring-theorem.md"]
    assert ("/lean/ComparatorChallenges/Ring.lean#L5). Proved in [lean/OAI/Algebra/Ring/Main.lean, line 3](" in ring
            and "#L3). formalization.yaml lists it as one of the repository's main results." in ring)
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
    assert "under its Apache-2.0 license." in root and "The articles have no edges." in root
    # The README and formalization.yaml are quoted, not paraphrased, and the facts listed.
    assert "/README.md) opens: “This repository contains manuscripts produced by a model.”" in root
    assert ("It adds: “Some of the unformalized results could have issues.” “In our view, these manuscripts are raw "
            "research data, rather than polished academic papers.”") in root
    assert ("On how the results were produced: “The vast majority of results were obtained with one procedure.” "
            "“Exceptions to this fixed procedure include the zeta work. Additionally, its writeup was human edited.”") in root
    assert "describes the Lean: “Lean formalizations accompanying a mathematics manuscript collection.”" in root
    assert "## Facts" in root and "- Authors: OpenAI." in root and "- Review status: “unchecked”." in root
    assert "- Automation: agent" in root and "- Lean toolchain v4.34.1" in root


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


def test_rows_that_link_one_statement_file_count_its_statements_once(tmp_path):
    again = "| Zeta again | [Zeta.lean](../ComparatorChallenges/Zeta.lean) |\n"
    files = FILES | {"lean/docs/003.md": DOC_003 + again}
    _, _, counts, problems = openai_math.read(checkout(tmp_path / "math", files))
    assert problems == [] and (counts["results"], counts["statements"], counts["proofs_found"]) == (4, 4, 3)
    built, _, pages = build(tmp_path / "built", files)
    assert built.stats["statements"] == 4
    zeta = pages[ROOT / "number-theory/003-zeta-bounds.md"]
    assert "1 manuscript and 3 Lean statements, quoted from" in zeta
    # The second row names what the first quotes, with its line.
    assert zeta.count("```lean\ntheorem bound : ∀ s") == 1
    assert "## Lean: Zeta again\n\nStates the `OAI.Zeta.bound` quoted above. Stated in [Zeta.lean, line 7](" in zeta
    assert "States the `OAI.Zeta.region` quoted above. Stated in [Zeta.lean, line 5](" in zeta


def test_a_title_keeps_its_emphasis():
    families, problems = openai_math.read_contents(
        cell("**017. The irrationality exponent of <i>π</i> is 2.** It is 2.")
        + cell("&emsp;[Pi](preprints/Pi/paper.pdf)\n\nPi."))
    assert problems == [] and families[0]["title"] == "The irrationality exponent of *π* is 2"
    leaf = openai_math.article(families[0] | {"lean": None}, {"source": {"repo": "openai/math", "rev": "a" * 40}}, {})
    assert leaf.title == "017. The irrationality exponent of *π* is 2" and "\\*" not in leaf.title
    assert leaf.slug == "017-the-irrationality-exponent-of-is-2"


def test_only_the_statements_formalization_yaml_lists_are_marked_main(tmp_path):
    main = ("    - comparator_config: ComparatorChallenges/Zeta.json\n      declaration: OAI.Zeta.bound\n"
            "      file: OAI/NumberTheory/Zeta/Main.lean\n")
    files = FILES | {"lean/formalization.yaml": FILES["lean/formalization.yaml"] + main}
    _, families, counts, problems = openai_math.read(checkout(tmp_path / "math", files))
    assert problems == []
    zeta = families["Number theory"][1]["lean"]["results"][0]
    assert zeta["main"] and [(entry["name"], entry["main"]) for entry in zeta["statements"]] == [
        ("OAI.Zeta.bound", True), ("OAI.Zeta.region", False)]
    # The counts stay per configuration.
    assert (counts["main_results"], counts["results_main"], counts["main_results_unlinked"]) == (3, 2, 1)
    _, _, pages = build(tmp_path / "built", files)
    page = pages[ROOT / "number-theory/003-zeta-bounds.md"]
    assert page.count("formalization.yaml lists it as one of the repository's main results.") == 1
    assert "where its value contains `sorry`. formalization.yaml lists it as one" in page


def test_a_proof_is_also_read_from_the_file_formalization_yaml_names(tmp_path):
    main = ("    - comparator_config: ComparatorChallenges/Hecke.json\n      declaration: OAI.Hecke.bound\n"
            "      file: OAI/NumberTheory/Hecke/Deep.lean\n")
    files = FILES | {"lean/formalization.yaml": FILES["lean/formalization.yaml"] + main,
                     "lean/OAI/NumberTheory/Hecke/Deep.lean": "namespace OAI.Hecke\n\ntheorem bound : True := trivial\n\nend OAI.Hecke\n"}
    assert "lean/OAI/NumberTheory/Hecke/Deep.lean" in openai_math.solution_files(checkout(tmp_path / "math", files))
    _, families, counts, problems = openai_math.read(tmp_path / "math")
    assert problems == [] and counts["proofs_found"] == 4 and "proofs_not_found" not in counts
    hecke = families["Number theory"][1]["lean"]["results"][1]["statements"][0]
    assert hecke["proof"] == {"file": "lean/OAI/NumberTheory/Hecke/Deep.lean", "line": 3, "kind": "theorem", "sorry": False}


def test_a_family_whose_statements_have_no_proof_found_is_still_formalized(tmp_path):
    hecke = DOC_003.split("| Zeta $7/8$")[0] + "| Hecke bound | [Challenge.lean](../ComparatorChallenges/Hecke/Challenge.lean) |\n"
    _, lean_links, pages = build(tmp_path, FILES | {"lean/docs/003.md": hecke})
    page = pages[ROOT / "number-theory/003-zeta-bounds.md"]
    assert "lean: OAI.Hecke.bound" in page and "statement: formalized" in page and "proof: formalized" not in page
    # The name links its statement's line, as no proof is found.
    assert lean_links["OAI.Hecke.bound"].endswith("/lean/ComparatorChallenges/Hecke/Challenge.lean#L3")


def test_a_label_keeps_a_bar_in_its_formula_and_a_relative_link_its_fragment():
    doc, problems = openai_math.read_doc(
        DOC_002.replace("| Rings are rings |", "| Bound $|x| \\le 1$ |"), "lean/docs/002.md")
    assert problems == [] and doc["results"][0]["label"] == "Bound $|x| \\le 1$"
    source = {"repo": "openai/math", "rev": "r" * 40}
    assert openai_math.relink("[x](../ComparatorChallenges/Zeta.lean#L5)", "lean/docs", source) == (
        f"[x](https://github.com/openai/math/blob/{'r' * 40}/lean/ComparatorChallenges/Zeta.lean#L5)")


def test_html_and_character_references_are_found_outside_formulas():
    assert openai_math.markup("a <b>bold</b> and &hellip;") == ["<b>", "</b>", "&hellip;"]
    assert openai_math.markup("$k<n$ and $m>2$, `<b>`, <https://example.org> and x < y > z") == []
    assert openai_math.markup(openai_math.markdown("$`k<n`$ and <i>p</i> &gt; 2")) == []


def with_cell(after: str, text: str) -> str:
    """CONTENTS with a cell added after the cell that holds *after*."""
    start = CONTENTS.index(after)
    end = CONTENTS.index("</tr></tbody>\n", start) + len("</tr></tbody>\n")
    return CONTENTS[:end] + cell(text) + CONTENTS[end:]


BROKEN = {
    "stray-cell": ({"CONTENTS.md": with_cell("Again.", "Just text.")},
                   "CONTENTS.md has a cell that is neither a family nor a manuscript: 'Just text.'"),
    "duplicate-family": ({"CONTENTS.md": with_cell("Again.", "**001. Twice.** Again.")},
                         "CONTENTS.md lists family 001 2 times"),
    "no-manuscripts": ({"CONTENTS.md": CONTENTS.replace("</table>", cell("**004. Alone.** None.") + "</table>")},
                       "CONTENTS.md: family 004 has no manuscripts"),
    "manuscript-first": ({"CONTENTS.md": CONTENTS.replace("</th></tr></thead>\n", "</th></tr></thead>\n"
                                                          + cell("&emsp;[Stray](preprints/Stray/paper.pdf)\n\nStray."))},
                         "CONTENTS.md lists a manuscript before any family"),
    "html": ({"CONTENTS.md": CONTENTS.replace("is odd, with", "is <b>odd</b>, with")},
             "CONTENTS.md: family 001 keeps HTML or a character reference: '<b>'"),
    "reference": ({"CONTENTS.md": CONTENTS.replace("Again.", "Again&hellip;")},
                  "CONTENTS.md: family 002 keeps HTML or a character reference: '&hellip;'"),
    "lean-link-form": ({"CONTENTS.md": CONTENTS.replace("(lean/docs/002.md))", "(lean/docs/002.md)).")},
                       "CONTENTS.md: family 002 links its Lean page in a form this chapter does not read"),
    "doc-unlinked": ({"CONTENTS.md": CONTENTS.replace(" ([Lean](lean/docs/002.md))", "")},
                     "lean/docs/002.md is linked by no family of CONTENTS.md"),
    "filed-twice": ({"overview.tex": OVERVIEW + "\\resultentry{001}{Again}{Again.}{links}\n"},
                    "overview.tex files family 001 more than once"),
    "subject-slugs": ({"overview.tex": OVERVIEW.replace("{Algebra}", "{Number Theory}")},
                      "overview.tex has 2 subjects that slugify to 'number-theory'"),
    "config": ({"lean/ComparatorChallenges/Ring.json": json.dumps({"solution_module": "OAI.Algebra.Ring.Main"})},
               "lean/ComparatorChallenges/Ring.json does not read: KeyError('challenge_module')"),
    "no-main-results": ({"lean/formalization.yaml": FILES["lean/formalization.yaml"].split("\nstatus:")[0] + "\n"},
                        "lean/formalization.yaml lists no main results"),
    "yaml": ({"lean/formalization.yaml": 'version: "v0.3"\n'}, "lean/formalization.yaml does not read: "),
    "no-scope": ({"lean/docs/002.md": DOC_002.replace("## Scope", "## Range")},
                 "lean/docs/002.md lacks its title, its Scope section or its Comparator links section"),
    "scope-html": ({"lean/docs/002.md": DOC_002.replace("Every ring is a ring;", "Every ring<br>is a ring;")},
                   "lean/docs/002.md keeps HTML or a character reference: '<br>'"),
    "two-links": ({"lean/docs/002.md": DOC_002.replace("(../ComparatorChallenges/Ring.lean) |\n",
                                                       "(../ComparatorChallenges/Ring.lean) [Zeta.lean](../ComparatorChallenges/Zeta.lean) |\n")},
                  "lean/docs/002.md: a Comparator links row does not link one statement file: "),
    "no-rows": ({"lean/docs/002.md": DOC_002.split("| Rings are rings")[0]}, "lean/docs/002.md links no statement file"),
    "line-after-all": ({"lean/docs/003.md": DOC_003.replace("Zeta.lean) |", "Zeta.lean#L99) |")},
                       "lean/docs/003.md links line 99 of lean/ComparatorChallenges/Zeta.lean, after every declaration "
                       "its configuration names"),
    "not-stated": ({"lean/ComparatorChallenges/Ring.json": config("ComparatorChallenges.Ring", "OAI.Algebra.Ring.Main",
                                                                  ["OAI.ring_is_ring", "OAI.missing"])},
                   "lean/ComparatorChallenges/Ring.lean does not state OAI.missing, which "
                   "lean/ComparatorChallenges/Ring.json names"),
    "statement-scopes": ({"lean/ComparatorChallenges/Ring.lean": FILES["lean/ComparatorChallenges/Ring.lean"]
                          .replace("end OAI", "end Wrong")},
                         "lean/ComparatorChallenges/Ring.lean is missing or its scopes don't close"),
    "solution-scopes": ({"lean/OAI/Algebra/Ring/Main.lean": FILES["lean/OAI/Algebra/Ring/Main.lean"]
                         .replace("end OAI", "end Wrong")},
                        "lean/OAI/Algebra/Ring/Main.lean: its scopes don't close"),
}


@pytest.mark.parametrize("name", BROKEN)
def test_each_guard_lists_what_does_not_read_or_match(tmp_path, name):
    files, expected = BROKEN[name]
    _, _, _, problems = openai_math.read(checkout(tmp_path / "math", FILES | files))
    assert any(problem.startswith(expected) for problem in problems), problems


def test_a_problem_writes_nothing(tmp_path):
    out = tmp_path / "out"
    repo = checkout(tmp_path / "math", FILES | BROKEN["solution-scopes"][0])
    assert refresh_openai_math.refresh(repo, out) == ["lean/OAI/Algebra/Ring/Main.lean: its scopes don't close"]
    assert not out.exists()
    empty = {name: text for name, text in FILES.items() if not name.startswith("lean/docs/")}
    empty |= {"CONTENTS.md": "# Mathematics manuscript collection\n", "overview.tex": "\\cataloguesection{Algebra}{1}\n"}
    repo = checkout(tmp_path / "empty", empty)
    assert refresh_openai_math.refresh(repo, out) == [
        f"openai/math at {git(repo, 'rev-parse', 'HEAD')[:8]}: CONTENTS.md lists no families"]
    readme = {name: text for name, text in FILES.items() if name != "README.md"}
    repo = checkout(tmp_path / "readme", readme)
    assert refresh_openai_math.refresh(repo, out) == [
        f"openai/math at {git(repo, 'rev-parse', 'HEAD')[:8]}: README.md does not read"]
    assert not out.exists()


def test_a_listed_file_in_the_commit_but_not_checked_out_writes_nothing(tmp_path):
    out = tmp_path / "out"
    repo = checkout(tmp_path / "math")
    (repo / "lean/OAI/NumberTheory/Zeta/Region.lean").unlink()
    assert refresh_openai_math.refresh(repo, out) == ["not checked out: lean/OAI/NumberTheory/Zeta/Region.lean"]
    assert not out.exists()


def test_a_license_with_text_before_apaches_writes_nothing(tmp_path):
    out = tmp_path / "out"
    repo = checkout(tmp_path / "math", license_text="Manuscripts are CC BY-NC 4.0.\n" + LICENSE)
    assert refresh_openai_math.refresh(repo, out) == [
        f"openai/math at {git(repo, 'rev-parse', 'HEAD')[:8]}: its LICENSE is not Apache-2.0"]
    assert not out.exists()


def test_the_families_with_lean_dropping_under_half_writes_nothing(tmp_path):
    out = tmp_path / "out"
    out.mkdir()
    (out / "source.json").write_text(json.dumps({"counts": {"families_with_lean": 5}}), encoding="utf-8")
    assert refresh_openai_math.refresh(checkout(tmp_path / "math"), out) == [
        "2 families with Lean, under half the 5 of the last record"]
    assert sorted(path.name for path in out.iterdir()) == ["source.json"]


def test_a_subject_renamed_leaves_no_stale_shard(tmp_path):
    out = tmp_path / "out"
    repo = checkout(tmp_path / "math")
    assert refresh_openai_math.refresh(repo, out) == []
    write(repo, {"overview.tex": OVERVIEW.replace("{Algebra}", "{Rings and fields}")})
    git(repo, "commit", "--quiet", "-am", "rename")
    assert refresh_openai_math.refresh(repo, out) == []
    assert sorted(path.name for path in (out / "families").iterdir()) == ["number-theory.json", "rings-and-fields.json"]


def test_the_committed_data_build_the_chapter():
    loaded = openai_math.load(REPO_ROOT / "data")
    source, counts = loaded["source"], loaded["source"]["counts"]
    assert source["repo"] == openai_math.REPO and len(source["rev"]) == 40
    assert loaded["structure"]["schema"] == openai_math.SCHEMA and loaded["structure"]["rev"] == source["rev"]
    built, links = openai_math.chapter(loaded)
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert len(leaves) == built.stats["families"] == counts["families"]
    assert built.stats["statements"] == counts["statements"]
    assert built.stats["proved"] == counts["proofs_found"] - counts["proofs_with_sorry"]
    assert set(links) == {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(len(dict(leaf.fields).get("lean", "").split(", ")) <= openai_math.LEAN_NAMES for leaf in leaves)
    assert all(dict(leaf.fields)["declaration"] == "section" for leaf in leaves)
    assert all(len(node.children) <= 20 for node in walk(built.root) if isinstance(node, Container))
