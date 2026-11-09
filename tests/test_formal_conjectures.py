import json
import os
import subprocess
from pathlib import Path

import pytest

import refresh_formal_conjectures
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

/-- A definition, though its category is a statement's. -/
@[category research solved, AMS 5]
noncomputable def erdos_1.variants.F : ℕ := 0

end Erdos1
'''

# A category that does not read, to put at the end of ERDOS.
TYPO = '''@[category research sovled]
theorem erdos_1.variants.typo : True := by
  sorry

end Erdos1
'''

WIKI = '''/-!
# A conjecture on Wikipedia

Some prose about it, <https://example.org/autolink>.

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Conjecture_(mathematics))
- [Er56](Erdős, P., Problems (1956).) and $[0,1](x)$
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


def data(tmp_path: Path, files: dict[str, str] = FILES) -> dict:
    for path, text in files.items():
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text(text, encoding="utf-8")
    problems, subsets = fc.read(tmp_path, sorted(files, key=fc.natural))
    return {"schema": fc.SCHEMA, "repo": fc.REPO, "rev": REV, "date": "2026-11-06T12:35:01Z", "toolchain": "v4.33.1",
            "subjects": fc.subjects(AMS), "problems": problems, "subsets": subsets}


def test_a_problem_file_keeps_its_research_and_textbook_statements(tmp_path):
    record = fc.read_module(ERDOS.replace("end Erdos1\n", TYPO), "FormalConjectures/ErdosProblems/1.lean")
    assert record["module"] == "FormalConjectures.ErdosProblems.«1»" and record["folder"] == "ErdosProblems"
    assert record["title"] == "Erdős Problem 1"
    assert record["reference"] == {"text": "erdosproblems.com/1", "url": "https://www.erdosproblems.com/1"}
    names = [statement["name"] for statement in record["statements"]]
    assert names == ["Erdos1.erdos_1", "Erdos1.erdos_1.variants.weaker", "Erdos1.erdos_1.variants.open_case",
                     "Erdos1.erdos_1.variants.conditional", "Erdos1.erdos_1.variants.proved",
                     "Erdos1.erdos_1.variants.F"]
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
    assert record["statements"][5]["kind"] == "def"
    assert record["unread"] == [{"name": "Erdos1.erdos_1.variants.typo", "line": 64,
                                 "why": "an attribute that does not read: category research sovled"}]


def test_a_declaration_that_does_not_read_is_listed_with_its_reason():
    path = "FormalConjectures/Other/X.lean"
    record = fc.read_module("namespace A\n@[category research open]\ntheorem x : True := sorry\nend B\n", path)
    assert record["statements"] == [] and record["unread"] == [
        {"name": "", "line": 0, "why": "its scopes do not close as they open"}]
    two = fc.read_module("@[category research open, category test]\ntheorem two : True := by\n  sorry\n", path)
    assert two["statements"] == [] and two["folded"] == {"test": 0, "api": 0}
    assert two["unread"] == [{"name": "two", "line": 2, "why": "more than one category"}]
    cases = "@[category research open]\ntheorem cases : ∀ n : ℕ, n = n\n  | 0 => rfl\n  | n + 1 => rfl\n"
    assert fc.read_module(cases, path)["unread"] == [
        {"name": "cases", "line": 2, "why": "no `:=` or `where` found to end its statement"}]
    # A test statement is only counted, so it needs no Lean statement.
    assert fc.read_module(cases.replace("research open", "test"), path)["folded"] == {"test": 1, "api": 0}


def test_titles_references_and_subjects_come_from_the_docstrings():
    assert fc.title_and_doc("# T\n\nRest.") == ("T", "Rest.")
    assert fc.title_and_doc("Title: Degree sequences\nAuthors: A.") == ("Degree sequences", "Authors: A.")
    assert fc.title_and_doc("No title here.") == ("", "No title here.")
    assert fc.reference("*References:*\n- [AR75] A book.\n- [B](https://b.org)") == {"text": "B", "url": "https://b.org"}
    assert fc.reference("*Reference:* https://www.erdosproblems.com/1104") == {
        "text": "https://www.erdosproblems.com/1104", "url": "https://www.erdosproblems.com/1104"}
    assert fc.reference("No references.") is None
    assert fc.reference("Prose.\n\n## References\n\n- [A paper](https://a.org/p)") == {
        "text": "A paper", "url": "https://a.org/p"}
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


def test_a_quote_puts_each_display_formula_in_a_block_of_its_own():
    # The site reads `$$...$$` as a formula only as a block of its own.
    assert fc.displays("such that\n$$\n  N \\gg 2^n.\n$$\nthen more") == "such that\n\n$$\n  N \\gg 2^n.\n$$\n\nthen more"
    assert fc.displays("and\n$$a(n) = 8$$ for $n$.") == "and\n\n$$a(n) = 8$$\n\nfor $n$."
    assert fc.displays("x `$$a$$` y") == "x `$$a$$` y"
    assert fc.displays("such that\n$$a$$\nthen\n$$b$$\nas") == "such that\n\n$$a$$\n\nthen\n\n$$b$$\n\nas"
    assert fc.displays("No formula.") == "No formula."
    # A character reference reads as its character, which a formula then shows.
    assert fc.quote("then$$x&#60; 1,$$where") == "> then\n>\n> $$x< 1,$$\n>\n> where"


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
    assert (stats["open"], stats["solved with proof"], stats["solved proved"], stats["textbook proved"]) == (2, 2, 1, 1)
    assert stats["definition"] == 1 and stats["test"] == 2 and stats["api"] == 1
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
    assert ("The file states 5 research or textbook statements: 1 open, 3 solved and 1 textbook result. A definition "
            "with a category attribute is not counted among them. It also has 1 test statement and 1 API statement, "
            "counted here but not shown.") in page
    assert "## `Erdos1.erdos_1.variants.F`\n\nA definition (`def`), not a statement" in page
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
    assert "> Some prose about it, <https://example.org/autolink>.\n>\n> *References:*" in wiki
    assert "erdosproblems.com" not in wiki
    assert "- [Wikipedia](https://en.wikipedia.org/wiki/Conjecture_%28mathematics%29)" in wiki
    # A citation written as a link reads as text, so the site looks for no page at its target.
    assert "> - [Er56\\](Erdős, P., Problems (1956).) and $[0,1](x)$" in wiki


def test_part_pages_credit_formal_conjectures_and_list_files_without_an_article(tmp_path):
    _, _, files = build(tmp_path)
    erdos = files[Path("blueprint/roadmap/formal-conjectures/erdos-problems/README.md")]
    assert "quoted from [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind)" in erdos
    assert f"[README for this folder]({BLOB}/FormalConjectures/ErdosProblems/README.md)" in erdos
    root = files[Path("blueprint/roadmap/formal-conjectures/README.md")]
    assert ("6 statements in 2 articles: 2 open and stated without proof; 3 research solved, 1 of them proved here and 2 "
            "of the rest with a `formal_proof` link to a proof elsewhere; 1 textbook result, 1 of them proved here. "
            "Besides these, 1 definition carries a category attribute; its card says it is not a statement.") in root
    assert "under its Apache-2.0 license" in root
    assert "The articles have no dependencies: edges between statements need Lean." in root and "flat" not in root
    wiki = files[Path("blueprint/roadmap/formal-conjectures/wikipedia/README.md")]
    assert ("The 1 problem file in [FormalConjectures/Wikipedia](https://github.com/google-deepmind/formal-conjectures/"
            f"tree/{REV}/FormalConjectures/Wikipedia) that states a research or textbook statement, at commit") in wiki
    assert "Its docstrings and Lean statements are quoted from" in wiki
    assert "one article each" not in wiki and "Their docstrings" not in wiki
    assert f"No article: 1 file in a folder with no article states no research or textbook statement: [Tests only]" in root
    subject = files[Path("blueprint/roadmap/formal-conjectures/by-subject/05-combinatorics/README.md")]
    assert "- [Erdős Problem 1](../../erdos-problems/1-99/erdos-problem-1.md)" in subject
    subset = files[Path("blueprint/roadmap/formal-conjectures/fc100-subsets/fc100openset1/README.md")]
    assert ("The 4 statements the list names, numbered as it lists them, 2 of them linked to their problem's article; "
            "the 2 others, without an article here, are listed at the end.") in subset
    assert ("- [2. `Wiki.conjecture` (research open), in A conjecture on Wikipedia]"
            "(../../wikipedia/a-conjecture-on-wikipedia.md)") in subset
    assert "3. `OnlyTests.t` (test, in [FormalConjectures/Other/OnlyTests.lean]" in subset
    assert "4. `Gone.missing`, which the reading does not find" in subset


def test_a_declaration_that_does_not_read_stops_the_chapter(tmp_path):
    # Its file would otherwise read as one that states no research or textbook statement.
    typo = FILES | {"FormalConjectures/ErdosProblems/1.lean": ERDOS.replace("end Erdos1\n", TYPO)}
    with pytest.raises(ValueError, match="1.lean:64 Erdos1.erdos_1.variants.typo: an attribute that does not read"):
        fc.chapter(data(tmp_path, typo))


def problem_file(title: str, name: str, extra: str = "") -> str:
    return f"/-!\n# {title}\n{extra}-/\n\n@[category research open, AMS 11]\ntheorem {name} : True := by\n  sorry\n"


def test_an_erdos_article_links_its_file_number_when_the_title_names_it():
    def number(file, title):
        return fc.erdos_number({"file": f"FormalConjectures/{file}", "folder": file.split("/")[0], "title": title})

    assert number("ErdosProblems/67.lean", "Erdős Problem 67") == 67
    assert number("ErdosProblems/67.lean", "Erdős Problem 68") is None
    assert number("ErdosProblems/Misc.lean", "Erdős Problem 3") is None
    assert number("Wikipedia/67.lean", "Problem 67") is None


def test_unusual_files_folders_and_long_lists_keep_their_places(tmp_path):
    names = [f"P{n}.t" for n in range(1, 11)] + ["Gone.missing"] + [f"P{n}.t" for n in range(11, 23)]
    files = {
        # Its reference names another problem; the article links its own.
        "FormalConjectures/ErdosProblems/67.lean": problem_file(
            "Erdős Problem 67", "Erdos67.e", "\n*References:*\n- [erdosproblems.com/67](https://www.erdosproblems.com/66)\n"),
        "FormalConjectures/ErdosProblems/Misc.lean": problem_file("Erdős miscellany", "ErdosMisc.e"),
        "FormalConjectures/NewFolder/Thing.lean": problem_file("A thing", "Thing.t"),
        "FormalConjectures/Wikipedia/Empty.lean": ONLY_TESTS,
        "FormalConjectures/Subsets/FC100Big.lean": "/-!\n# FC100Big\n-/\n\ndef problems : List Name := [\n"
        + ",\n".join(f"  decl_name% {name}" for name in names) + "]\n",
    } | {f"FormalConjectures/Wikipedia/P{n}.lean": problem_file(f"Problem {n}", f"P{n}.t") for n in range(1, 23)}
    built, _ = fc.chapter(data(tmp_path, files))
    vault = Path("blueprint")
    chapter = vault / "roadmap" / "formal-conjectures"
    assign_paths(built.root, chapter)
    blueprints.resolve(built, vault)
    pages = render_tree(built.root, vault)
    # A folder FOLDERS does not name comes after those it does, titled from its name.
    assert [entry.node.title for entry in built.root.entries] == [
        "Erdős problems", "Wikipedia", "New Folder", "By subject", "FC100 subsets"]
    erdos = pages[chapter / "erdos-problems" / "1-99" / "erdos-problem-67.md"]
    assert "[https://www.erdosproblems.com/67](https://www.erdosproblems.com/67)" in erdos
    assert "- [erdosproblems.com/67](https://www.erdosproblems.com/67)" in erdos.split("*Quoted from")[1]
    other = pages[chapter / "erdos-problems" / "other" / "erdos-miscellany.md"]
    assert "erdosproblems.com" not in other
    # The files without an article are listed on their folder's page, not on its last part's.
    assert ("No article: 1 file here states no research or textbook statement: [Tests only]"
            in pages[chapter / "wikipedia" / "README.md"])
    assert "No article" not in pages[chapter / "wikipedia" / "part-02" / "README.md"]
    # An FC100 list numbers its entries as it lists them, and lists those without an article on its own page.
    big = chapter / "fc100-subsets" / "fc100big"
    assert ("The 23 statements the list names, numbered as it lists them, 22 of them linked to their problem's article; "
            "the 1 other, without an article here, is listed at the end.") in pages[big / "README.md"]
    assert "Without an article here: 11. `Gone.missing`, which the reading does not find." in pages[big / "README.md"]
    assert [entry.node.title for entry in built.root.entries[-1].node.entries[0].node.entries] == [
        "Entries 1 to 21", "Entries 22 to 23"]
    assert "- [12. `P11.t` (research open), in Problem 11]" in pages[big / "part-01" / "README.md"]
    assert "Without an article" not in pages[big / "part-02" / "README.md"]


APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-05T12:00:00+02:00",
           "GIT_COMMITTER_DATE": "2026-11-05T12:00:00+02:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path, files: dict[str, str] = FILES, license_text: str = APACHE, ams: str = AMS) -> Path:
    # Shaped like the sparse checkout the workflow makes.
    every = files | {"LICENSE": license_text, refresh_formal_conjectures.AMS_FILE: ams,
                     "lean-toolchain": "leanprover/lean4:v4.33.1\n"}
    for path, text in every.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "release")
    return root


def test_the_refresh_writes_the_source_and_the_problems(tmp_path):
    out = tmp_path / "out"
    assert refresh_formal_conjectures.refresh(checkout(tmp_path / "fc"), out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    # The commit date is written in UTC.
    assert source == {"repo": fc.REPO, "rev": git(tmp_path / "fc", "rev-parse", "HEAD").strip(),
                      "date": "2026-11-05T10:00:00Z", "toolchain": "v4.33.1"}
    record = json.loads((out / "problems.json").read_text(encoding="utf-8"))
    assert record["schema"] == fc.SCHEMA and record["rev"] == source["rev"] and record["subjects"] == fc.subjects(AMS)
    assert [problem["file"] for problem in record["problems"]] == [
        "FormalConjectures/ErdosProblems/1.lean", "FormalConjectures/Other/OnlyTests.lean",
        "FormalConjectures/Wikipedia/Conjecture.lean"]
    assert [subset["file"] for subset in record["subsets"]] == ["FormalConjectures/Subsets/FC100OpenSet1.lean"]


def test_the_refresh_writes_nothing_from_a_checkout_it_cannot_read_in_full(tmp_path):
    def refused(root: Path) -> list[str]:
        out = tmp_path / "out"
        problems = refresh_formal_conjectures.refresh(root, out)
        assert not out.exists()
        return problems

    mit = checkout(tmp_path / "mit", license_text="MIT License\n")
    assert refused(mit) == [f"{fc.REPO} at {git(mit, 'rev-parse', 'HEAD')[:8]}: its LICENSE is not Apache-2.0"]
    assert refused(checkout(tmp_path / "ams", ams="inductive AMS\n")) == [
        "FormalConjecturesUtil/Attributes/AMS.lean gives no subject names"]
    gone = checkout(tmp_path / "gone")
    (gone / "FormalConjectures/Wikipedia/Conjecture.lean").unlink()
    assert refused(gone) == ["not checked out: FormalConjectures/Wikipedia/Conjecture.lean"]
    unread = FILES | {"FormalConjectures/ErdosProblems/1.lean": ERDOS.replace("end Erdos1\n", TYPO),
                      "FormalConjectures/Other/Broken.lean": "namespace A\nend B\n"}
    assert refused(checkout(tmp_path / "unread", unread)) == [
        "FormalConjectures/ErdosProblems/1.lean:64 Erdos1.erdos_1.variants.typo: an attribute that does not read: "
        "category research sovled",
        "FormalConjectures/Other/Broken.lean:0 (the file): its scopes do not close as they open"]


def test_the_refresh_refuses_a_record_that_keeps_under_half_the_last(tmp_path):
    out = tmp_path / "out"
    out.mkdir()
    last = {"problems": [{"statements": [{}] * 15}]}
    (out / "problems.json").write_text(json.dumps(last), encoding="utf-8")
    assert refresh_formal_conjectures.refresh(checkout(tmp_path / "fc"), out) == [
        "keeps 7 statements, under half the 15 the last record kept"]
    assert json.loads((out / "problems.json").read_text(encoding="utf-8")) == last
    assert not (out / "source.json").exists()


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
