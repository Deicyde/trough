import json
import os
import subprocess
from pathlib import Path

import refresh_cfsg
from trough import blueprints
from trough import cfsg
from trough import leansource
from trough.vault import Container, Entry, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "a" * 40
BLOB = f"https://github.com/AxiomMath/CFSG/blob/{REV}"

# Shaped like CFSG/Statement.lean: the top theorem applies the reduction to the catalog and a theorem per case.
STATEMENT = """module

public import CFSG.Assembly.Reduction
public import CFSG.Assembly.LowTwoRank
public import CFSG.FeitThompson.OddOrder

public section

namespace CFSG

theorem classification_finite_simple_groups
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G] :
    ∃ i : TauCeti.CFSGIndex, Nonempty (G ≃* i.Group) :=
  Assembly.classification Assembly.InCatalog
    (fun _ _ _ h => CFSG.FeitThompson.isSolvable_of_odd_natCard _ h)
    Assembly.abelian_simple
    Assembly.low_two_rank
    G

end CFSG
"""

# Shaped like CFSG/Assembly/Reduction.lean, with two cases.
REDUCTION = """module

public section

namespace CFSG.Assembly

abbrev GroupProp : Type 1 := ∀ (G : Type) [Group G], Prop

variable (C : GroupProp)

@[expose] def OddOrderStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G], Odd (Nat.card G) → Group.IsSolvable G

@[expose] def AbelianStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∀ a b : G, a * b = b * a) → C G

@[expose] def LowTwoRankStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], twoRank G ≤ 2 → C G

theorem classification (hodd : OddOrderStatement) (hab : AbelianStatement C) (hlow : LowTwoRankStatement C)
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G] : C G := by
  exact hlow G (by omega)

end CFSG.Assembly
"""

IN_CATALOG = """module

public import CFSG.Assembly.Reduction

namespace CFSG.Assembly

def InCatalog : GroupProp := fun G _ =>
  True

theorem abelian_simple (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hcomm : ∀ a b : G, a * b = b * a) : InCatalog G :=
  trivial

end CFSG.Assembly
"""

LOW_TWO_RANK = """module

public import CFSG.Assembly.InCatalog
public import CFSG.Milestones.LR_rank_two
public import CFSG.Support.Bridge

namespace CFSG.Assembly

theorem low_two_rank
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hrank : twoRank G ≤ 2) : InCatalog G := by
  trivial

end CFSG.Assembly
"""

ODD_ORDER_CASE = """module

public import CFSG.Milestones.OO_odd_order_solvable

namespace CFSG.FeitThompson

theorem isSolvable_of_odd_natCard (G : Type) [Group G] [Finite G] (h : Odd (Nat.card G)) :
    Group.IsSolvable G :=
  odd_order G h

end CFSG.FeitThompson
"""

# Shaped like CFSG/Milestones/OO_odd_order_solvable.lean.
ODD_ORDER = """module

public import CFSG.FeitThompson.OddOrderTheorem

public section

namespace CFSG.OddOrder

theorem _root_.CFSG.Milestones.odd_order_solvable {G : Type*} [Group G] [Finite G]
    (_h : Odd (Nat.card G)) : Group.IsSolvable G :=
  CFSG.FeitThompson.isSolvable_of_odd_natCard _ _h

end CFSG.OddOrder
"""

RANK_TWO = """module

public import CFSG.Milestones.OO_odd_order_solvable

namespace CFSG.Open

@[expose] def RankTwo (G : Type) [Group G] : Prop := True

theorem _root_.CFSG.Milestones.lr_rank_two (G : Type) [Group G] : RankTwo G := by
  trivial

end CFSG.Open
"""

TOOL = """module

namespace CFSG.Open

theorem _root_.CFSG.Milestones.zj_glauberman (n : ℕ) : n = n := by
  sorry

end CFSG.Open
"""

SOLUTION = """module

public import TauCeti.GroupTheory.SpecificGroups.CFSG.Classification

public section

universe u

theorem CFSGComparator.classification : TauCeti.ClassificationStatement.{u} :=
  TauCeti.classificationStatement_of_zero CFSG.Certified.classification_finite_simple_groups
"""

FORMALIZATION = """version: "v0.4"
project:
  name: "The Classification of Finite Simple Groups"
  description: >-
    A Lean 4 formalization of the Classification of Finite Simple Groups.
  authors: ["Dean Cureton", "Vasily Ilin"]
  license: "Apache-2.0"
sources:
  - title: "CFSG Sources"
status:
  sorry_count: 0
  main_results:
    - declaration: "CFSGComparator.classification"
      file: "Comparator/Solution.lean"
    - declaration: "CFSG.Milestones.odd_order_solvable"
      file: "CFSG/Milestones/OO_odd_order_solvable.lean"
automation:
  methods:
    - method: autonomous
      framework: "AxiomProver"
review:
  status: self-assessed
  reviewers: ["Axiom Math"]
"""

README = """# Classification of Finite Simple Groups in Lean
* [Website](https://cfsg.axiommath.ai/)

A sorry-free Lean4 proof of the Classification of Finite Simple Groups (CFSG).

## Checking the proof

`lake build` builds the entire project.
"""

MANIFEST = {"packages": [{"name": "mathlib", "rev": "b" * 40}, {"name": "TauCeti", "rev": "c" * 40}]}
APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"
FILES = {
    "CFSG/Statement.lean": STATEMENT,
    "CFSG/Assembly/Reduction.lean": REDUCTION,
    "CFSG/Assembly/InCatalog.lean": IN_CATALOG,
    "CFSG/Assembly/LowTwoRank.lean": LOW_TWO_RANK,
    "CFSG/FeitThompson/OddOrder.lean": ODD_ORDER_CASE,
    "CFSG/Support/Bridge.lean": "module\n\npublic import CFSG.Milestones.OO_odd_order_solvable\n",
    "CFSG/Milestones.lean": "module\n\npublic import CFSG.Milestones.LR_rank_two\npublic import CFSG.Milestones.OO_odd_order_solvable\n",
    "CFSG/Milestones/OO_odd_order_solvable.lean": ODD_ORDER,
    "CFSG/Milestones/LR_rank_two.lean": RANK_TWO,
    "CFSG/Milestones/ZJ_glauberman.lean": TOOL,
    "CFSG/Milestones/ASVolI/Background.lean": "module\n\ntheorem support : True := trivial\n",
    "CFSG/ThirdParty/Adapted.lean": "module\n\n/-- An adapted lemma. -/\ntheorem adapted : True := trivial\n",
    "CFSG/Certificates/Kernel.lean": "module\n\ntheorem kernel : True := trivial\n",
    "Certificates/Certificate1.lean": "module\n\ntheorem certificate : True := trivial\n",
    "Comparator/Solution.lean": SOLUTION,
}


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-10-27T17:07:38+02:00",
           "GIT_COMMITTER_DATE": "2026-10-27T17:07:38+02:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def checkout(root: Path, files: dict[str, str] = FILES, license_text: str = APACHE,
             formalization: str = FORMALIZATION) -> Path:
    every = files | {"LICENSE": license_text, "formalization.yaml": formalization, "README.md": README,
                     "lean-toolchain": "leanprover/lean4:v4.35.0-rc3\n", "lake-manifest.json": json.dumps(MANIFEST)}
    for path, text in every.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "Initial commit")
    return root


def test_a_milestone_keeps_its_declarations_in_order_with_their_statements():
    record = cfsg.read_milestone(RANK_TWO, "CFSG/Milestones/LR_rank_two.lean")
    assert record["module"] == "CFSG.Milestones.LR_rank_two" and record["id"] == "LR_rank_two"
    assert record["imports"] == ["CFSG.Milestones.OO_odd_order_solvable"]
    assert [(item["name"], item["kind"], item["line"], item["sorry"]) for item in record["declarations"]] == [
        ("CFSG.Open.RankTwo", "def", 7, False), ("CFSG.Milestones.lr_rank_two", "theorem", 9, False)]
    assert record["declarations"][1]["statement"] == "theorem _root_.CFSG.Milestones.lr_rank_two (G : Type) [Group G] : RankTwo G"
    assert cfsg.read_milestone(TOOL, "CFSG/Milestones/ZJ_glauberman.lean")["declarations"][0]["sorry"]
    assert cfsg.read_milestone("namespace A\nend B\n", "CFSG/Milestones/X.lean")["declarations"] is None


def test_the_milestones_are_the_files_directly_under_their_folder():
    assert cfsg.milestone_paths(list(FILES)) == [
        "CFSG/Milestones/LR_rank_two.lean", "CFSG/Milestones/OO_odd_order_solvable.lean",
        "CFSG/Milestones/ZJ_glauberman.lean"]


def test_the_top_theorems_proof_reads_as_a_function_and_its_arguments():
    top = leansource.scan(STATEMENT)["CFSG.classification_finite_simple_groups"]
    value = cfsg.value_of(STATEMENT, top)
    assert cfsg.arguments(value) == ["Assembly.classification", "Assembly.InCatalog",
                                     "(fun _ _ _ h => CFSG.FeitThompson.isSolvable_of_odd_natCard _ h)",
                                     "Assembly.abelian_simple", "Assembly.low_two_rank", "G"]
    assert cfsg.candidates("(fun _ _ _ h => CFSG.FeitThompson.isSolvable_of_odd_natCard _ h)", "CFSG") == [
        "CFSG.CFSG.FeitThompson.isSolvable_of_odd_natCard", "CFSG.FeitThompson.isSolvable_of_odd_natCard"]


def test_a_definition_is_its_text_up_to_the_next_command():
    assert cfsg.declaration_text(REDUCTION, 11) == (
        "@[expose] def OddOrderStatement : Prop :=\n"
        "  ∀ (G : Type) [Group G] [Finite G], Odd (Nat.card G) → Group.IsSolvable G")
    assert cfsg.declaration_text(IN_CATALOG, 7) == "def InCatalog : GroupProp := fun G _ =>\n  True"


def test_edges_are_the_transitive_reduction_of_what_each_file_reaches():
    graph = {"A": ["B", "X"], "X": ["C", "Y"], "Y": ["B"], "B": ["C"], "C": []}
    assert cfsg.closure("X", graph) == {"X", "C", "Y", "B"}
    # A reaches C through B, so the edge from A to C is left out.
    assert cfsg.reduce({"A": {"B", "C"}, "B": {"C"}, "C": set()}) == {"A": ["B"], "B": ["C"], "C": []}


def test_the_readme_opening_leaves_out_its_links_and_stops_at_its_first_section():
    assert cfsg.readme_paragraphs(README) == ["A sorry-free Lean4 proof of the Classification of Finite Simple Groups (CFSG)."]


def test_the_refresh_writes_the_source_and_the_proof(tmp_path):
    out = tmp_path / "out"
    repo = checkout(tmp_path / "cfsg")
    assert refresh_cfsg.refresh(repo, out) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    # The commit date is written in UTC.
    assert source == {"repo": cfsg.REPO, "rev": git(repo, "rev-parse", "HEAD").strip(), "date": "2026-10-27T15:07:38Z",
                      "toolchain": "v4.35.0-rc3", "mathlib": "b" * 40, "tauceti": "c" * 40}
    record = json.loads((out / "proof.json").read_text(encoding="utf-8"))
    assert record["schema"] == cfsg.SCHEMA and record["rev"] == source["rev"] and record["license"] == "Apache-2.0"
    top = record["top"]
    assert (top["name"], top["file"], top["line"], top["reduction"]) == (
        "CFSG.classification_finite_simple_groups", "CFSG/Statement.lean", 11, "CFSG.Assembly.classification")
    assert top["catalog"] == {"name": "CFSG.Assembly.InCatalog", "file": "CFSG/Assembly/InCatalog.lean", "line": 7,
                              "text": "def InCatalog : GroupProp := fun G _ =>\n  True", "imported_by_cases": 1}
    assert [declaration["name"] for declaration in record["reduction"]["declarations"]] == [
        "CFSG.Assembly.GroupProp", "CFSG.Assembly.OddOrderStatement", "CFSG.Assembly.AbelianStatement",
        "CFSG.Assembly.LowTwoRankStatement", "CFSG.Assembly.classification"]
    assert record["reduction"]["declarations"][1]["text"].startswith("@[expose] def OddOrderStatement : Prop :=\n")
    # An abbreviation is shown whole too; a theorem by its statement.
    assert record["reduction"]["declarations"][0]["text"] == "abbrev GroupProp : Type 1 := ∀ (G : Type) [Group G], Prop"
    assert "text" not in record["reduction"]["declarations"][-1]
    odd, abelian, low = record["cases"]
    assert (odd["hypothesis"], odd["type"], odd["theorem"]["name"], odd["theorem"]["module"]) == (
        "hodd", "OddOrderStatement", "CFSG.FeitThompson.isSolvable_of_odd_natCard", "CFSG.FeitThompson.OddOrder")
    assert odd["definition"]["line"] == 11 and odd["reaches"] == odd["depends"] == ["CFSG.Milestones.OO_odd_order_solvable"]
    assert (abelian["theorem"]["name"], abelian["theorem"]["file"], abelian["depends"]) == (
        "CFSG.Assembly.abelian_simple", "CFSG/Assembly/InCatalog.lean", [])
    assert (low["hypothesis"], low["type"], low["theorem"]["name"], low["theorem"]["line"]) == (
        "hlow", "LowTwoRankStatement", "CFSG.Assembly.low_two_rank", 9)
    # It reaches the odd order milestone through CFSG.Support.Bridge too, but LR_rank_two imports that milestone, so
    # its only edge goes to LR_rank_two; and it imports the catalog's file, the abelian case's, which is no edge.
    assert low["reaches"] == ["CFSG.Milestones.LR_rank_two", "CFSG.Milestones.OO_odd_order_solvable"]
    assert low["depends"] == ["CFSG.Milestones.LR_rank_two"]
    milestones = {milestone["id"]: milestone for milestone in record["milestones"]}
    assert list(milestones) == ["LR_rank_two", "OO_odd_order_solvable", "ZJ_glauberman"]
    assert [milestones[key]["indexed"] for key in milestones] == [True, True, False]
    assert milestones["LR_rank_two"]["depends"] == ["CFSG.Milestones.OO_odd_order_solvable"]
    assert milestones["OO_odd_order_solvable"]["cases"] == ["CFSG.FeitThompson.isSolvable_of_odd_natCard",
                                                            "CFSG.Assembly.low_two_rank"]
    assert milestones["ZJ_glauberman"]["cases"] == [] and "imports" not in milestones["ZJ_glauberman"]
    # The certificates are counted, not read.
    assert record["files"] == 13 and record["certificates"] == 2
    folders = {row["folder"]: row for row in record["folders"]}
    assert "CFSG/Certificates" not in folders and "Certificates" not in folders
    assert folders["CFSG/Milestones"] == {"folder": "CFSG/Milestones", "files": 4, "theorems": 4, "documented": 0}
    assert folders["CFSG/ThirdParty"]["documented"] == 1
    assert [(result["name"], result["line"]) for result in record["main_results"]] == [
        ("CFSGComparator.classification", 9), ("CFSG.Milestones.odd_order_solvable", 9)]


def test_the_refresh_writes_nothing_from_a_checkout_it_cannot_read_in_full(tmp_path):
    def refused(root: Path) -> list[str]:
        out = tmp_path / "out"
        problems = refresh_cfsg.refresh(root, out)
        assert not out.exists()
        return problems

    assert refused(checkout(tmp_path / "mit", license_text="MIT License\n")) == [
        "not Apache-2.0 (formalization.yaml says 'Apache-2.0')"]
    broken = FILES | {"CFSG/Milestones/Broken.lean": "namespace A\nend B\n"}
    assert refused(checkout(tmp_path / "broken", broken)) == [
        "CFSG/Milestones/Broken.lean: its scopes do not close as they open"]
    gone = checkout(tmp_path / "gone")
    (gone / "CFSG/Support/Bridge.lean").unlink()
    assert refused(gone) == ["not checked out: CFSG/Support/Bridge.lean"]
    renamed = FORMALIZATION.replace('"CFSGComparator.classification"', '"CFSGComparator.classify"')
    assert refused(checkout(tmp_path / "renamed", formalization=renamed)) == [
        "main result CFSGComparator.classify is not found declared in Comparator/Solution.lean"]
    no_top = FILES | {"CFSG/Statement.lean": STATEMENT.replace("classification_finite_simple_groups", "classify")}
    assert refused(checkout(tmp_path / "no-top", no_top)) == [
        "CFSG.classification_finite_simple_groups is not found declared in CFSG/Statement.lean"]
    short = FILES | {"CFSG/Assembly/Reduction.lean": REDUCTION.replace(
        "(hlow : LowTwoRankStatement C)", "(hlow : LowTwoRankStatement C) (hmore : LowTwoRankStatement C)")}
    assert refused(checkout(tmp_path / "short", short)) == [
        "CFSG.classification_finite_simple_groups: its proof does not give CFSG.Assembly.classification a catalog and "
        "4 cases"]
    undefined = FILES | {"CFSG/Assembly/Reduction.lean": REDUCTION.replace("def LowTwoRankStatement", "def LowRank")}
    assert refused(checkout(tmp_path / "undefined", undefined)) == [
        "CFSG.classification_finite_simple_groups: the case hlow : LowTwoRankStatement does not cite one theorem, or "
        "LowTwoRankStatement is not defined in CFSG/Assembly/Reduction.lean"]


def test_the_refresh_refuses_a_record_that_reads_under_half_the_last_milestones(tmp_path):
    out = tmp_path / "out"
    out.mkdir()
    last = {"milestones": [{}] * 7}
    (out / "proof.json").write_text(json.dumps(last), encoding="utf-8")
    assert refresh_cfsg.refresh(checkout(tmp_path / "cfsg"), out) == [
        "reads 3 milestones, under half the 7 the last record read"]
    assert json.loads((out / "proof.json").read_text(encoding="utf-8")) == last
    assert not (out / "source.json").exists()


def data(tmp_path: Path) -> dict:
    out = tmp_path / "data" / "cfsg"
    assert refresh_cfsg.refresh(checkout(tmp_path / "cfsg"), out) == []
    return cfsg.load(tmp_path / "data") | {"rev": REV}


def built(tmp_path: Path, tau: Container | None = None):
    result, links = cfsg.chapter(data(tmp_path), tau)
    vault = tmp_path / "vault"
    if tau is not None:
        assign_paths(tau, vault / "roadmap" / "tauceti")
    assign_paths(result.root, vault / "roadmap" / "cfsg")
    blueprints.resolve(result, vault)
    pages = {path.relative_to(vault / "roadmap" / "cfsg"): text for path, text in render_tree(result.root, vault).items()}
    return result, links, pages


def test_the_chapter_has_the_case_division_then_the_milestones(tmp_path):
    result, links, pages = built(tmp_path)
    division, milestones = (entry.node for entry in result.root.entries)
    assert [entry.text for entry in division.entries] == [
        "CFSG.classification_finite_simple_groups", "CFSG.Assembly.Reduction",
        "OddOrderStatement: CFSG.FeitThompson.isSolvable_of_odd_natCard", "AbelianStatement: CFSG.Assembly.abelian_simple",
        "LowTwoRankStatement: CFSG.Assembly.low_two_rank"]
    assert [entry.text for entry in milestones.entries] == ["LR_rank_two", "OO_odd_order_solvable", "ZJ_glauberman"]
    assert ("The 3 modules directly under `CFSG/Milestones/`, by file name, one article each; CFSG/Milestones.lean imports "
            "2 of them. 1 milestone is imported by no case theorem's file, directly or through other files.") in pages[
        Path("milestones/README.md")]
    assert links["CFSG.Assembly.low_two_rank"] == f"{BLOB}/CFSG/Assembly/LowTwoRank.lean#L9"
    assert links["CFSG.Assembly.OddOrderStatement"] == f"{BLOB}/CFSG/Assembly/Reduction.lean#L11"
    assert links["CFSGComparator.classification"] == f"{BLOB}/Comparator/Solution.lean#L9"
    assert result.stats["articles"] == 8 and result.stats["edges"] == 3 and result.stats["sorry"] == 1
    # Every article is captioned as a theorem, whatever its module declares first.
    assert all(text.startswith("---\ndeclaration: theorem\n") for path, text in pages.items() if path.name != "README.md")


def test_the_top_article_lists_the_cases_its_proof_applies_the_reduction_to(tmp_path):
    result, links, pages = built(tmp_path)
    top = pages[Path("case-division/top-theorem.md")]
    assert ("Its proof applies [`CFSG.Assembly.classification`](reduction.md) to the catalog `CFSG.Assembly.InCatalog` "
            "and to a theorem for each of the reduction's 3 hypotheses, in its order:") in top
    assert "- `hlow : LowTwoRankStatement`: [`CFSG.Assembly.low_two_rank`](case-hlow-lowtworankstatement.md)" in top
    assert "```lean\ndef InCatalog : GroupProp := fun G _ =>\n  True\n```" in top
    assert "## Depends on\n\nIts statement uses no other result mapped here.\n\n## Proof depends on" in top
    assert ("## Proof depends on\n\n- [CFSG.Assembly.Reduction](reduction.md)\n"
            "- [CFSG.FeitThompson.isSolvable_of_odd_natCard](case-hodd-oddorderstatement.md)\n"
            "- [CFSG.Assembly.abelian_simple](case-hab-abelianstatement.md)\n"
            "- [CFSG.Assembly.low_two_rank](case-hlow-lowtworankstatement.md)") in top
    reduction = pages[Path("case-division/reduction.md")]
    assert "```lean\n@[expose] def LowTwoRankStatement : Prop :=\n" in reduction
    assert "`CFSG.Assembly.classification` (theorem, [line 20]" in reduction


def test_a_case_shows_what_it_asserts_its_theorem_and_the_milestones_its_file_reaches(tmp_path):
    result, links, pages = built(tmp_path)
    case = pages[Path("case-division/case-hlow-lowtworankstatement.md")]
    assert ("The case `hlow : LowTwoRankStatement` of [`CFSG.Assembly.classification`](reduction.md). What it asserts, "
            f"defined in [CFSG/Assembly/Reduction.lean, line 17]({BLOB}/CFSG/Assembly/Reduction.lean#L17):") in case
    assert f"`CFSG.Assembly.low_two_rank` (theorem, [line 9]({BLOB}/CFSG/Assembly/LowTwoRank.lean#L9)). Proved here." in case
    assert ("Its file imports, directly or through other files, 2 milestone modules: "
            "[LR_rank_two](../milestones/lr-rank-two.md), [OO_odd_order_solvable](../milestones/oo-odd-order-solvable.md).") in case
    assert "## Depends on\n\n- [LR_rank_two](../milestones/lr-rank-two.md)\n\n## Sources" in case


def test_a_milestone_shows_its_statements_and_the_cases_whose_files_import_it(tmp_path):
    result, links, pages = built(tmp_path)
    page = pages[Path("milestones/oo-odd-order-solvable.md")]
    assert "The milestone module `CFSG.Milestones.OO_odd_order_solvable`, one of those CFSG/Milestones.lean imports." in page
    assert ("The files of 2 case theorems import it, directly or through other files: "
            "[`CFSG.FeitThompson.isSolvable_of_odd_natCard`](../case-division/case-hodd-oddorderstatement.md), "
            "[`CFSG.Assembly.low_two_rank`](../case-division/case-hlow-lowtworankstatement.md).") in page
    rank_two = pages[Path("milestones/lr-rank-two.md")]
    assert "lean: CFSG.Open.RankTwo, CFSG.Milestones.lr_rank_two" in rank_two and "proof: formalized" in rank_two
    assert "```lean\ndef RankTwo (G : Type) [Group G] : Prop\n```" in rank_two
    assert "## Depends on\n\n- [OO_odd_order_solvable](oo-odd-order-solvable.md)" in rank_two
    tool = pages[Path("milestones/zj-glauberman.md")]
    assert "which CFSG/Milestones.lean does not import." in tool and "No case theorem's file imports it" in tool
    assert "Stated without proof: its proof holds `sorry`." in tool and "proof: formalized" not in tool
    assert "Its Lean file imports no case or milestone file, directly or through other files." in tool


def test_the_front_page_has_the_facts_the_main_results_and_how_the_map_is_read(tmp_path):
    result, links, pages = built(tmp_path)
    front = pages[Path("README.md")]
    assert "> A sorry-free Lean4 proof of the Classification of Finite Simple Groups (CFSG)." in front
    assert "- Review status: “self-assessed”." in front
    assert (f"`CFSGComparator.classification` (theorem), in [Comparator/Solution.lean, line 9]({BLOB}/Comparator/Solution.lean#L9). "
            "Its statement:\n\n```lean\ntheorem CFSGComparator.classification : TauCeti.ClassificationStatement.{u}\n```") in front
    assert "Its milestone has [an article](milestones/oo-odd-order-solvable.md)." in front
    assert ("The commit has 13 Lean files besides 2 certificate files under `Certificates/` and `CFSG/Certificates/`, "
            "which are counted, not read.") in front
    assert "- `CFSG/Milestones/`: 4 files, 4 theorems and lemmas" in front
    assert "Docstrings and module docstrings appear only in 1 file, under `CFSG/ThirdParty/`, so the titles here are Lean names" in front
    assert "1 declaration holds `sorry`." in front
    assert "and imports no other case or milestone file that does; an edge implied by two others is left out. There are 3 such edges" in front
    assert ("1 case file imports CFSG/Assembly/InCatalog.lean, directly or through other files, for the catalog it declares "
            "beside the theorem for the case `hab : AbelianStatement`; imports of that file are not edges.") in front
    assert "cfsg.axiommath.ai/" not in "".join(text for path, text in pages.items() if path != Path("README.md"))


def test_a_statement_naming_a_tau_ceti_article_links_it(tmp_path):
    leaf = Leaf("Classification of finite simple groups, statement", "statement",
                [("declaration", "def"), ("lean", "TauCeti.ClassificationStatement")], "")
    tau = Container("Tau Ceti", "tauceti", [Entry(leaf)])
    result, links, pages = built(tmp_path, tau)
    front = pages[Path("README.md")]
    assert ("It names `TauCeti.ClassificationStatement`, which has [an article](../tauceti/statement.md) in the Tau Ceti "
            "chapter.") in front
    assert "the page that shows the statement links that article: 1 main result above does so." in front


def test_the_committed_data_build_the_chapter():
    loaded = cfsg.load(ROOT / "data")
    assert loaded is not None and loaded["schema"] == cfsg.SCHEMA and loaded["repo"] == cfsg.REPO and len(loaded["rev"]) == 40
    assert loaded["license"] == "Apache-2.0" and len(loaded["main_results"]) == 2 and loaded["cases"]
    result, links = cfsg.chapter(loaded)
    leaves = [node for node in walk(result.root) if isinstance(node, Leaf)]
    assert len(leaves) == result.stats["articles"] == 2 + len(loaded["cases"]) + len(loaded["milestones"])
    assert set(links) >= {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(len(node.children) <= 20 for node in walk(result.root) if isinstance(node, Container))
