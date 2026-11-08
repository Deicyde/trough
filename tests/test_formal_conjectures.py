import json
from pathlib import Path

from trough import blueprints
from trough import formal_conjectures as fc
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "a" * 40
BLOB = f"https://github.com/google-deepmind/formal-conjectures/blob/{REV}"

# Shaped like FormalConjectures/ErdosProblems/1.lean.
ERDOS = '''/-
Copyright 2025 The Formal Conjectures Authors.
-/
module

public import FormalConjecturesUtil

/-!
# Erdős Problem 1

*Reference:* [erdosproblems.com/1](https://www.erdosproblems.com/1)
-/

namespace Erdos1

/-- A helper definition, with no category. -/
abbrev IsSumDistinctSet (A : Finset ℕ) (N : ℕ) : Prop := True

set_option linter.style.formal_proof_palomar false in
/--
If $A\\subseteq\\{1, ..., N\\}$ then $N \\gg 2 ^ n$.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at
  "https://github.com/someone/erdos1/blob/0123/Erdos1.lean#L1"]
theorem erdos_1 : ¬ ∃ C > (0 : ℝ), ∀ (N : ℕ) (A : Finset ℕ),
    IsSumDistinctSet A N → C * 2 ^ A.card < N := by
  sorry

/-- The trivial lower bound. -/
@[category textbook, AMS 5 11]
theorem erdos_1.variants.weaker : True := by
  trivial

/-- An open case <with a bracket>. -/
@[category research open, AMS 5]
theorem erdos_1.variants.open_case : 1 + 1 = 2 := by
  sorry

/-- A conditional proof. -/
@[category research solved, AMS 11,
  conditional formal_proof using formal_conjectures at "https://example.org/proof" assuming erdos_1.variants.open_case]
theorem erdos_1.variants.conditional : True := by
  sorry

/-- Proved from a statement stated without proof. -/
@[category research solved, AMS 5]
theorem erdos_1.variants.proved : True := by
  trivial

@[category test, AMS 5]
theorem erdos_1.test_one : True := trivial

@[category test, AMS 5]
example : True := trivial

@[category API, AMS 5]
theorem erdos_1.api_one : True := trivial

@[category research sovled]
theorem erdos_1.variants.typo : True := by
  sorry

end Erdos1
'''

WIKI = '''/-!
# A conjecture on Wikipedia

Some prose about it.

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Conjecture_(mathematics))
-/

/-- It is open. -/
@[category research open, AMS 11]
theorem Wiki.conjecture : ∀ n : ℕ, n = n := by
  sorry
'''

ONLY_TESTS = '''/-!
# Tests only
-/

@[category test, AMS 5]
theorem OnlyTests.t : True := trivial
'''

SUBSET = '''/-!
# FC100OpenSet1

A random subset.
-/

namespace Subsets.FC100OpenSet1

def problems : List Name := [
  decl_name% Erdos1.erdos_1.variants.open_case,
  decl_name% Wiki.conjecture,
  decl_name% OnlyTests.t,
  decl_name% Gone.missing]

end Subsets.FC100OpenSet1
'''

AMS = '''inductive AMS
  /-- Combinatorics -/
  | «5»
  /-- Number theory -/
  | «11»
  deriving Inhabited
'''

FILES = {"FormalConjectures/ErdosProblems/1.lean": ERDOS, "FormalConjectures/Wikipedia/Conjecture.lean": WIKI,
         "FormalConjectures/Other/OnlyTests.lean": ONLY_TESTS, "FormalConjectures/Subsets/FC100OpenSet1.lean": SUBSET}


def data(tmp_path: Path) -> dict:
    for path, text in FILES.items():
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text(text, encoding="utf-8")
    problems, subsets = fc.read(tmp_path, sorted(FILES, key=fc.natural))
    return {"schema": fc.SCHEMA, "repo": fc.REPO, "rev": REV, "date": "2026-11-06T12:35:01Z", "toolchain": "v4.33.1",
            "subjects": fc.subjects(AMS), "problems": problems, "subsets": subsets}


def test_a_problem_file_keeps_its_research_and_textbook_statements(tmp_path):
    record = fc.read_module(ERDOS, "FormalConjectures/ErdosProblems/1.lean")
    assert record["module"] == "FormalConjectures.ErdosProblems.«1»" and record["folder"] == "ErdosProblems"
    assert record["title"] == "Erdős Problem 1"
    assert record["reference"] == {"text": "erdosproblems.com/1", "url": "https://www.erdosproblems.com/1"}
    names = [statement["name"] for statement in record["statements"]]
    assert names == ["Erdos1.erdos_1", "Erdos1.erdos_1.variants.weaker", "Erdos1.erdos_1.variants.open_case",
                     "Erdos1.erdos_1.variants.conditional", "Erdos1.erdos_1.variants.proved"]
    main = record["statements"][0]
    assert main["category"] == "research solved" and main["ams"] == [5, 11] and main["sorry"]
    assert main["formal_proofs"] == [{"system": "lean4", "url": "https://github.com/someone/erdos1/blob/0123/Erdos1.lean#L1"}]
    assert main["doc"] == "If $A\\subseteq\\{1, ..., N\\}$ then $N \\gg 2 ^ n$."
    assert main["statement"] == ("theorem erdos_1 : ¬ ∃ C > (0 : ℝ), ∀ (N : ℕ) (A : Finset ℕ),\n"
                                 "    IsSumDistinctSet A N → C * 2 ^ A.card < N")
    assert record["statements"][3]["formal_proofs"] == [
        {"system": "formal_conjectures", "url": "https://example.org/proof", "assuming": ["erdos_1.variants.open_case"]}]
    assert not record["statements"][1]["sorry"] and not record["statements"][4]["sorry"]
    # The test example has no name, so only the named test statement counts.
    assert record["folded"] == {"test": 1, "api": 1}
    assert record["unread"] == [{"name": "Erdos1.erdos_1.variants.typo", "line": 60,
                                 "why": "an attribute that does not read: category research sovled"}]


def test_titles_references_and_subjects_come_from_the_docstrings():
    assert fc.title_and_doc("# T\n\nRest.") == ("T", "Rest.")
    assert fc.title_and_doc("Title: Degree sequences\nAuthors: A.") == ("Degree sequences", "Authors: A.")
    assert fc.title_and_doc("No title here.") == ("", "No title here.")
    assert fc.reference("*References:*\n- [AR75] A book.\n- [B](https://b.org)") == {"text": "B", "url": "https://b.org"}
    assert fc.reference("*Reference:* https://www.erdosproblems.com/1104") == {
        "text": "https://www.erdosproblems.com/1104", "url": "https://www.erdosproblems.com/1104"}
    assert fc.reference("No references.") is None
    assert fc.subjects(AMS) == {"5": "Combinatorics", "11": "Number theory"}


def test_the_fc100_lists_name_statements_by_file_and_category(tmp_path):
    [subset] = data(tmp_path)["subsets"]
    assert subset["title"] == "FC100OpenSet1" and subset["doc"] == "A random subset."
    assert subset["names"] == [
        {"name": "Erdos1.erdos_1.variants.open_case", "file": "FormalConjectures/ErdosProblems/1.lean",
         "category": "research open"},
        {"name": "Wiki.conjecture", "file": "FormalConjectures/Wikipedia/Conjecture.lean", "category": "research open"},
        {"name": "OnlyTests.t", "file": "FormalConjectures/Other/OnlyTests.lean", "category": "test"},
        {"name": "Gone.missing", "file": None, "category": None}]


def test_status_lines_follow_category_proof_links_and_sorry():
    def line(category, sorry, proofs=(), kind="theorem"):
        return fc.status({"category": category, "sorry": sorry, "formal_proofs": list(proofs), "kind": kind})

    lean = {"system": "lean4", "url": "https://example.org/p"}
    assert line("research open", True) == "Open: stated without proof."
    assert line("research solved", True, [lean]) == (
        "Solved: stated here; a Lean proof is at [https://example.org/p](https://example.org/p).")
    assert line("research solved", True) == "Solved: stated here without proof."
    assert line("research solved", False) == "Proved here."
    assert line("research open", False) == "Proved here."
    assert line("textbook", True) == "Textbook result, stated without proof."
    assert line("textbook", False) == "Textbook result, proved here."
    assert line("research solved", True, [{"system": "other_system", "url": "https://x.org/a(b)"}]) == (
        "Solved: stated here; a proof in another system is at [https://x.org/a(b)](https://x.org/a%28b%29).")
    assert line("research solved", True, [lean | {"assuming": ["grh"]}]).startswith(
        "Solved: stated here; a Lean proof assuming `grh` is at")
    assert line("research solved", False, kind="def").startswith("A definition (`def`), not a statement")


def build(tmp_path):
    built, links = fc.chapter(data(tmp_path))
    vault = Path("blueprint")
    assign_paths(built.root, vault / "roadmap" / "formal-conjectures")
    blueprints.resolve(built, vault)
    return built, links, render_tree(built.root, vault)


def test_the_chapter_has_a_part_per_folder_and_an_article_per_problem_file(tmp_path):
    built, links, files = build(tmp_path)
    assert [entry.node.title for entry in built.root.entries] == [
        "Erdős problems", "Wikipedia", "By subject", "FC100 subsets"]
    leaves = {node.title: node for node in walk(built.root) if isinstance(node, Leaf)}
    assert set(leaves) == {"Erdős Problem 1", "A conjecture on Wikipedia"}
    stats = built.stats
    assert stats["articles"] == 2 and stats["statements"] == 6 and stats["without_statements"] == 1
    assert (stats["open"], stats["solved with proof"], stats["proved"], stats["textbook proved"]) == (2, 2, 1, 1)
    assert stats["test"] == 2 and stats["api"] == 1 and stats["unread"] == 1
    erdos = built.root.entries[0].node
    assert [entry.node.title for entry in erdos.entries] == ["Problems 1 to 99"]
    assert links["Erdos1.erdos_1"] == f"{BLOB}/FormalConjectures/ErdosProblems/1.lean#L25"
    assert set(links) == {name for leaf in leaves.values() for name in dict(leaf.fields)["lean"].split(", ")}


def test_an_article_quotes_its_module_docstring_and_has_a_card_per_statement(tmp_path):
    _, _, files = build(tmp_path)
    page = files[Path("blueprint/roadmap/formal-conjectures/erdos-problems/1-99/erdos-problem-1.md")]
    assert page.startswith("---\ndeclaration: theorem\norigin: cited\nlean: Erdos1.erdos_1, ")
    assert "proof: formalized" not in page
    assert "# Erdős Problem 1\n\n> *Reference:* [erdosproblems.com/1](https://www.erdosproblems.com/1)\n\n*Quoted from" in page
    assert ("The problem's page on erdosproblems.com: "
            "[https://www.erdosproblems.com/1](https://www.erdosproblems.com/1).") in page
    assert ("The file states 5 research or textbook statements: 1 open, 3 solved and 1 textbook result. "
            "It also has 1 test statement and 1 API statement, counted here but not shown.") in page
    assert ("## `Erdos1.erdos_1`\n\nSolved: stated here; a Lean proof is at "
            "[https://github.com/someone/erdos1/blob/0123/Erdos1.lean#L1]") in page
    assert "> If $A\\subseteq\\{1, ..., N\\}$ then $N \\gg 2 ^ n$.\n\n```lean\ntheorem erdos_1 : ¬ ∃ C" in page
    assert ("Category `research solved`; AMS [05 Combinatorics](../../by-subject/05-combinatorics/README.md), "
            "[11 Number theory](../../by-subject/11-number-theory/README.md). Declared in "
            f"[FormalConjectures/ErdosProblems/1.lean, line 25]({BLOB}/FormalConjectures/ErdosProblems/1.lean#L25).") in page
    assert "> An open case &lt;with a bracket>." in page
    assert "## `Erdos1.erdos_1.variants.proved`\n\nProved here." in page
    assert "typo" not in page and "test_one" not in page
    assert fc.NO_DEPENDS in page
    wiki = files[Path("blueprint/roadmap/formal-conjectures/wikipedia/a-conjecture-on-wikipedia.md")]
    assert "> Some prose about it.\n>\n> *References:*" in wiki and "erdosproblems.com" not in wiki
    assert "- [Wikipedia](https://en.wikipedia.org/wiki/Conjecture_%28mathematics%29)" in wiki


def test_part_pages_credit_formal_conjectures_and_list_files_without_an_article(tmp_path):
    _, _, files = build(tmp_path)
    erdos = files[Path("blueprint/roadmap/formal-conjectures/erdos-problems/README.md")]
    assert "quoted from [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind)" in erdos
    assert f"[README for this folder]({BLOB}/FormalConjectures/ErdosProblems/README.md)" in erdos
    root = files[Path("blueprint/roadmap/formal-conjectures/README.md")]
    assert "6 statements in 2 articles" in root and "under its Apache-2.0 license" in root
    assert f"No article: 1 file in a folder with no article states no research or textbook statement: [Tests only]" in root
    subject = files[Path("blueprint/roadmap/formal-conjectures/by-subject/05-combinatorics/README.md")]
    assert "- [Erdős Problem 1](../../erdos-problems/1-99/erdos-problem-1.md)" in subject
    subset = files[Path("blueprint/roadmap/formal-conjectures/fc100-subsets/fc100openset1/README.md")]
    assert ("- [`Wiki.conjecture` (research open), in A conjecture on Wikipedia]"
            "(../../wikipedia/a-conjecture-on-wikipedia.md)") in subset
    assert "`OnlyTests.t` (test, in [FormalConjectures/Other/OnlyTests.lean]" in subset
    assert "`Gone.missing`, which the reading does not find" in subset


def test_the_committed_data_build_the_chapter():
    loaded = fc.load(ROOT / "data")
    assert loaded is not None and loaded["schema"] == fc.SCHEMA and loaded["repo"] == fc.REPO and len(loaded["rev"]) == 40
    for problem in loaded["problems"]:
        for statement in problem["statements"]:
            assert statement["category"] in fc.KEPT and statement["statement"]
    built, links = fc.chapter(loaded)
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert len(leaves) == built.stats["articles"] > 0
    assert set(links) == {name for leaf in leaves for name in dict(leaf.fields)["lean"].split(", ")}
    assert all(len(node.children) <= 20 for node in walk(built.root) if isinstance(node, Container))
