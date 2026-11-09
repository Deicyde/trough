import json
from pathlib import Path

from trough import analysis, blueprints
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "a" * 40
BLOB = f"https://github.com/teorth/analysis/blob/{REV}"

# Shaped like Analysis/Section_6_1.lean.
SECTION_6_1 = '''import Mathlib.Tactic
import Analysis.Section_5_1
import Analysis.Misc.Tools

/-!
# Analysis I, Section 6.1: Convergence and limit laws

Main constructions and results of this section:

- Definition of $`ε`-closeness, with {name}`Real.Close`.
-/

/- Definition 6.1.1 (Distance). A comment, not a docstring. -/
#check Real.dist_eq

abbrev Real.Close (ε x y : ℝ) : Prop := dist x y ≤ ε

/--
  Definition 6.1.2 (ε-close). Similar to {lean}`ℚ`'s.
-/
theorem Real.close_def (ε x y : ℝ) : ε.Close x y ↔ dist x y ≤ ε := by rfl

namespace Chapter6

/-- Definition 6.1.3 (Sequence). -/
@[ext]
structure Sequence where
  m : ℤ
  seq : ℤ → ℝ

/-- Exercise 6.1.2 -/
theorem Sequence.ex (a : Sequence) : a = a := by
  sorry

/-- {given -show}`n : ℕ` Exercise 6.1.3 : prove it again. -/
theorem Sequence.ex' : True := sorry

/-- Definition 6.1.3 (Cauchy sequence) -/
abbrev Sequence.IsCauchy (a : Sequence) : Prop := sorry

/-- Examples 6.1.6 -/
example : (1 : ℝ) = 1 := by rfl

/-- Theorem 6.1.7(a) / Exercise 6.1.4 -/
theorem tendsTo_add : True := by sorry

/-- Proposition 6.1.8, a private helper -/
private lemma helper : True := trivial

/-- Lemma 6.1.9 -/
postfix:100 "++" => Nat.succ

end Chapter6
'''

FILES = {
    "Analysis/Section_2_epilogue.lean": "import Analysis.Section_5_1\n\n/-!\n# Analysis I, Chapter 2 epilogue: Isomorphism "
                                        "with the Mathlib natural numbers\n-/\n\ntheorem iso : True := trivial\n",
    "Analysis/Section_4_2.lean": "/-!\n# Analysis I, Section 4.2\n\nThe rationals, without a subtitle.\n-/\n",
    "Analysis/Section_5_1.lean": "/-! # Analysis I, Section 5.1: Cauchy sequences -/\n\n"
                                 "/-- Definition 5.1.1 -/\ndef Chapter5.Sequence : Type := ℕ → ℚ\n",
    "Analysis/Section_6_1.lean": SECTION_6_1,
    "Analysis/Appendix_A_1.lean": "/-! # Analysis I, Appendix A.1: Mathematical Statements -/\n\n"
                                  "/-- Exercise A.1.1.  Fill in the first {syntax term}`sorry`. -/\n"
                                  "example {X Y:Prop} : ¬ (X ↔ Y) ↔ sorry := by sorry\n",
    "Analysis/MeasureTheory/Notation.lean": "/-! # Introduction to Measure Theory, Chapter 0: Notation -/\n",
    "Analysis/MeasureTheory/Section_1_1_1.lean": "import Analysis.MeasureTheory.Notation\nimport Analysis.Section_6_1\n\n"
                                                 "/-! # Introduction to Measure Theory, Section 1.1.1: Elementary measure -/\n\n"
                                                 "/-- Lemma 1.1.2(i): boxes. -/\ntheorem box : True := trivial\n\n"
                                                 "/-- Exercise 1.1.23' -/\ntheorem prime : True := sorry\n",
    "Analysis/MeasureTheory/Section_1_2_0.lean": "import Analysis.MeasureTheory.Section_1_1_1\n\n"
                                                 "/-! # Introduction to Measure Theory, Section 1.2: Lebesgue measure -/\n",
    "Analysis/Misc/erdos_1.lean": "/-! A solution to Erdos problem \\#1.  It is convenient to rephrase things. -/\n",
    "Analysis/Tools/ExistsUnique.lean": "/-! # API for ExistsUnique\n\nHere we review some of the API. -/\n",
}
LITERATE = '''exclude = ["Analysis.Misc", "Analysis.MeasureTheory"]

[order_children]
"Analysis" = [
  "Analysis.Section_2_epilogue",
  "Analysis.Section_4_2",
  "Analysis.Section_5_1",
  "Analysis.Section_6_1",
  "Analysis.Appendix_A_1",
]

[modules."Analysis.Section_4_2"]
title = "4.2. The rationals"
'''
README = '''# Lean formalization of _Analysis I_

The files in this directory contain a formalization. The formalization is intended to be as faithful a
paraphrasing as possible to the original text.

Portions of the text that were left as exercises to the reader are rendered in this translation as `sorry`s.

A third paragraph.

## Sections

- _Chapter 1: Introduction (not formalized)_
- Chapter 2: Starting at the beginning: the natural numbers
  - Chapter 2 epilogue: Isomorphism with the Mathlib natural numbers ([Verso page](https://example.org))
- Chapter 4: Integers and rationals
- Chapter 5: The Real numbers
- Chapter 6: Limits of sequences
- Appendix A: The basics of mathematical logic

## Additional content

- Chapter 7: not a chapter of this list
'''
MT_README = '''# Lean formalization of _An introduction to measure theory_

The files in this directory contain a formalization of my text.

Portions of the text are rendered in this translation as `sorry`s.

## Sections (work in progress)

- Notation section
- Chapter 1: Measure Theory
  - Section 1.1: Prologue: the problem of measure
    - Section 1.1.1: Elementary measure
  - Section 1.2: Lebesgue measure
    - Introduction:
  - Section 1.5: Modes of convergence
    - Section 1.5.1: Uniqueness (Documentation) (Lean source)
'''


def checkout(tmp_path: Path) -> Path:
    for path, text in {**FILES, "literate.toml": LITERATE, "README.md": README,
                       "Analysis/MeasureTheory/README.md": MT_README}.items():
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text(text, encoding="utf-8")
    return tmp_path


def record(tmp_path: Path) -> dict:
    read = analysis.read(checkout(tmp_path), sorted(path for path in FILES))
    assert read.pop("missing") == []
    return {"repo": analysis.REPO, "rev": REV, "date": "2026-10-18T00:29:34Z", "toolchain": "v4.29.0-rc8",
            "mathlib": "b" * 40, "schema": analysis.SCHEMA, **read}


def section(data: dict, module: str) -> dict:
    return next(section for section in data["sections"] if section["module"] == module)


def built(tmp_path: Path):
    data = record(tmp_path)
    chapter, links, forward = analysis.chapter(data)
    assign_paths(chapter.root, tmp_path / "vault" / "roadmap" / "analysis")
    blueprints.resolve(chapter, tmp_path / "vault")
    return data, chapter, links, forward


def test_labels_read_as_the_book_writes_them():
    assert analysis.label("Definition 6.1.3 (Sequence). This is similar") == ("Definition 6.1.3", "Definition", False)
    assert analysis.label("Exercise 3.6.2a") == ("Exercise 3.6.2a", "Exercise", True)
    assert analysis.label("Exercise 1.1.23'") == ("Exercise 1.1.23'", "Exercise", True)
    assert analysis.label("Exercise 1.3.8(vi'') (Product)") == ("Exercise 1.3.8(vi'')", "Exercise", True)
    assert analysis.label("Exercise A.1.1.  Fill in") == ("Exercise A.1.1", "Exercise", True)
    assert analysis.label("Axiom 2.1 (0 is a natural number)") == ("Axiom 2.1", "Axiom", False)
    assert analysis.label("Examples 6.1.6") == ("Examples 6.1.6", "Example", False)
    assert analysis.label("Assumption 2.6 (Existence)") == ("Assumption 2.6", "Assumption", False)
    assert analysis.label("Theorem 11.4.1(a) / Exercise 11.4.1") == ("Theorem 11.4.1(a) / Exercise 11.4.1", "Theorem", True)
    assert analysis.label("Proposition A.3.1, alternate proof") == ("Proposition A.3.1", "Proposition", False)
    # A Verso `{given}` role may come first.
    assert analysis.label("{given -show}`n : ℕ` Exercise 7.4.2 : reprove") == ("Exercise 7.4.2", "Exercise", True)
    for text in ("Exercise for Lemma 1.1.2(ii): Interval", "Definition of disjointness", "Example: the measure",
                 "Lemmas that can be helpful for proving 5.5.4", "Helper lemma for Exercise 3.4.7.", ""):
        assert analysis.label(text) is None


def test_verso_markup_reads_as_markdown():
    assert analysis.markdown("Sequences from {lean}`ℤ` to {name (full := Real)}`ℝ`.") == "Sequences from `ℤ` to `ℝ`."
    assert analysis.markdown("{given -show}`n₁, n₀`\n{lean}`a.from n₁` starts it") == "`a.from n₁` starts it"
    assert analysis.markdown("{given}`aᵢ` Exercise") == "`aᵢ` Exercise"
    assert analysis.markdown("Definition of $`ε`-closeness and $$`\\sum_i a_i`") == "Definition of $ε$-closeness and $$\\sum_i a_i$$"
    # Markdown's own code and TeX stay as written.
    assert analysis.markdown("`x` and $L^1$") == "`x` and $L^1$"


def test_a_checkout_reads_into_sections_in_book_order(tmp_path):
    data = record(tmp_path)
    assert [section["module"] for section in data["sections"]] == [
        "Analysis.Section_2_epilogue", "Analysis.Section_4_2", "Analysis.Section_5_1", "Analysis.Section_6_1",
        "Analysis.Appendix_A_1", "Analysis.MeasureTheory.Notation", "Analysis.MeasureTheory.Section_1_1_1",
        "Analysis.MeasureTheory.Section_1_2_0"]
    assert [(section["book"], section["chapter"], section["number"]) for section in data["sections"]] == [
        ("analysis-i", "2", "2 epilogue"), ("analysis-i", "4", "4.2"), ("analysis-i", "5", "5.1"),
        ("analysis-i", "6", "6.1"), ("analysis-i", "A", "A.1"), ("measure-theory", "0", "0"),
        ("measure-theory", "1.1", "1.1.1"), ("measure-theory", "1.2", "1.2")]
    six = section(data, "Analysis.Section_6_1")
    assert six["title"] == "Section 6.1: Convergence and limit laws"
    assert six["doc"].startswith("Main constructions and results of this section:")
    # Only the imports of other sections are kept.
    assert six["imports"] == ["Analysis.Section_5_1"]
    assert section(data, "Analysis.MeasureTheory.Section_1_1_1")["imports"] == [
        "Analysis.MeasureTheory.Notation", "Analysis.Section_6_1"]
    assert section(data, "Analysis.Section_4_2")["literate_title"] == "4.2. The rationals"
    assert [other["module"] for other in data["others"]] == ["Analysis.Misc.erdos_1", "Analysis.Tools.ExistsUnique"]
    assert data["others"][1]["title"] == "API for ExistsUnique" and data["others"][0]["title"] == ""
    assert data["chapters"]["analysis-i"] == {
        "1": "Chapter 1: Introduction (not formalized)", "2": "Chapter 2: Starting at the beginning: the natural numbers",
        "4": "Chapter 4: Integers and rationals", "5": "Chapter 5: The Real numbers", "6": "Chapter 6: Limits of sequences",
        "A": "Appendix A: The basics of mathematical logic"}
    assert data["chapters"]["measure-theory"] == {"1.1": "Section 1.1: Prologue: the problem of measure",
                                                  "1.2": "Section 1.2: Lebesgue measure",
                                                  "1.5": "Section 1.5: Modes of convergence"}
    assert len(data["readme"]["analysis-i"]) == 3 and data["readme"]["analysis-i"][0].startswith("The files in this")
    assert data["readme"]["measure-theory"][1] == "Portions of the text are rendered in this translation as `sorry`s."


def test_a_section_keeps_its_labelled_items_in_file_order(tmp_path):
    six = section(record(tmp_path), "Analysis.Section_6_1")
    assert [item["label"] for item in six["items"]] == [
        "Definition 6.1.2", "Definition 6.1.3", "Exercise 6.1.2", "Exercise 6.1.3", "Examples 6.1.6",
        "Theorem 6.1.7(a) / Exercise 6.1.4"]
    close, sequence, exercise, again, examples, add = six["items"]
    assert close["declarations"] == [{"name": "Real.close_def", "kind": "theorem", "line": 21,
                                      "doc": "Definition 6.1.2 (ε-close). Similar to {lean}`ℚ`'s.",
                                      "statement": "theorem Real.close_def (ε x y : ℝ) : ε.Close x y ↔ dist x y ≤ ε",
                                      "sorry": False}]
    # A label shared by declarations far apart is one item, at its first place.
    assert [(declaration["name"], declaration["kind"], declaration["sorry"]) for declaration in sequence["declarations"]] == [
        ("Chapter6.Sequence", "structure", False), ("Chapter6.Sequence.IsCauchy", "abbrev", True)]
    assert sequence["declarations"][0]["statement"] == "structure Sequence"
    assert exercise["exercise"] and exercise["declarations"][0]["sorry"]
    assert again["declarations"][0]["name"] == "Chapter6.Sequence.ex'"
    assert examples["kind"] == "Example" and examples["declarations"][0]["name"] == ""
    assert examples["declarations"][0]["statement"] == "example : (1 : ℝ) = 1"
    assert add["kind"] == "Theorem" and add["exercise"]
    assert six["unlabelled"] == {"declarations": 1, "examples": 0}
    assert six["unread"] == [
        {"label": "Proposition 6.1.8", "line": 48, "why": "on a private declaration, which the reading leaves out"},
        {"label": "Lemma 6.1.9", "line": 51, "why": "on a `postfix` command, which declares nothing the reading keeps"}]


def test_statuses_follow_the_declaration_kind_its_value_and_its_label(tmp_path):
    six = section(record(tmp_path), "Analysis.Section_6_1")
    outcomes = [analysis.outcome(declaration, item) for item in six["items"] for declaration in item["declarations"]]
    assert outcomes == ["proved", "definition", "definition sorry", "exercise", "exercise", "proved", "exercise"]
    assert analysis.outcome({"kind": "lemma", "sorry": True}, {"exercise": False}) == "stated"
    assert analysis.outcome({"kind": "axiom", "sorry": False}, {"exercise": False}) == "axiom"
    assert [analysis.STATUS[outcome] for outcome in ("proved", "stated", "exercise")] == [
        "Proved here.", "Stated without proof.", "An exercise, stated without proof."]


def test_the_chapter_has_a_part_per_book_and_a_page_for_other_modules(tmp_path):
    data, chapter, links, forward = built(tmp_path)
    root = chapter.root
    assert root.title == "Analysis I and An introduction to measure theory"
    assert [entry.node.title for entry in root.entries] == ["Analysis I", "An introduction to measure theory",
                                                            "Other modules"]
    part_i, measure, others = (entry.node for entry in root.entries)
    assert [chapter.title for chapter in part_i.children] == [
        "Chapter 2: Starting at the beginning: the natural numbers", "Chapter 4: Integers and rationals",
        "Chapter 5: The Real numbers", "Chapter 6: Limits of sequences", "Appendix A: The basics of mathematical logic"]
    assert [leaf.title for leaf in part_i.children[1].children] == ["Section 4.2: The rationals"]
    assert part_i.children[0].children[0].path.name == "section-2-epilogue.md"
    # Notation first, then a page per section of Chapter 1 that has a file; nothing for 1.5.
    assert [node.title for node in measure.children] == ["Chapter 0: Notation",
                                                         "Section 1.1: Prologue: the problem of measure",
                                                         "Section 1.2: Lebesgue measure"]
    assert isinstance(measure.children[0], Leaf) and isinstance(measure.children[1], Container)
    assert others.children == [] and "neither book" in others.prose
    assert "[`Analysis.Tools.ExistsUnique`](" in others.prose and "API for ExistsUnique." in others.prose
    assert "whose module docstring opens “A solution to Erdos problem \\#1. …”" in others.prose
    assert chapter.stats["articles"] == 8 and chapter.stats["items"] == 10
    assert links["Real.close_def"] == f"{BLOB}/Analysis/Section_6_1.lean#L21"
    assert "" not in links


def test_edges_follow_imports_and_forward_imports_are_reported(tmp_path):
    data, chapter, links, forward = built(tmp_path)
    leaves = {leaf.title: leaf for leaf in walk(chapter.root) if isinstance(leaf, Leaf)}
    assert [leaf.title for leaf in leaves["Section 6.1: Convergence and limit laws"].depends] == [
        "Section 5.1: Cauchy sequences"]
    assert [leaf.title for leaf in leaves["Section 1.1.1: Elementary measure"].depends] == [
        "Chapter 0: Notation", "Section 6.1: Convergence and limit laws"]
    # The chapter 2 epilogue comes before Section 5.1 in literate.toml's order; a measure theory section's import
    # of Analysis I is no forward import.
    assert forward == [("Analysis.Section_2_epilogue", "Analysis.Section_5_1")]
    assert chapter.stats["edges"] == 5
    assert "1 import points forward in its book's order: Chapter 2 epilogue" in chapter.root.prose


def test_an_article_quotes_its_docstrings_and_has_a_block_per_label(tmp_path):
    data, chapter, links, forward = built(tmp_path)
    files = render_tree(chapter.root, tmp_path / "vault")
    page = next(text for path, text in files.items() if path.name == "section-6-1.md")
    assert ("lean: Real.close_def, Chapter6.Sequence, Chapter6.Sequence.IsCauchy, Chapter6.Sequence.ex, "
            "Chapter6.Sequence.ex', Chapter6.tendsTo_add\nstatement: formalized\n---") in page
    assert "proof: formalized" not in page
    assert "> - Definition of $ε$-closeness, with `Real.Close`." in page
    assert (f"*Quoted from [Analysis/Section_6_1.lean]({BLOB}/Analysis/Section_6_1.lean) in "
            "[teorth/analysis](https://github.com/teorth/analysis) at commit") in page
    assert ("The file has 6 labelled items, carried by 7 declarations: 2 proved here, 3 stated without proof (3 of them "
            "exercises) and 2 definitions (1 with a value left as `sorry`). It also has 1 declaration with no label, "
            "counted here but not shown. The docstring labelled Proposition 6.1.8 at line 48 is on a private "
            "declaration, which the reading leaves out.") in page
    assert ("## Definition 6.1.2\n\n`Real.close_def` (theorem, [line 21]("
            f"{BLOB}/Analysis/Section_6_1.lean#L21)). Proved here.\n\n"
            "> Definition 6.1.2 (ε-close). Similar to `ℚ`'s.\n\n"
            "```lean\ntheorem Real.close_def (ε x y : ℝ) : ε.Close x y ↔ dist x y ≤ ε\n```") in page
    assert "`Chapter6.Sequence.IsCauchy` (abbrev, [line 39](" in page
    assert "). A definition whose value is left as `sorry`." in page
    assert f"## Examples 6.1.6\n\nAn `example` ([line 42]({BLOB}/Analysis/Section_6_1.lean#L42)). Proved here." in page
    assert "> Exercise 6.1.3 : prove it again." in page
    assert "## Theorem 6.1.7(a) / Exercise 6.1.4" in page
    assert "## Depends on\n\n- [Section 5.1: Cauchy sequences](../chapter-5/section-5-1.md)" in page
    assert "- [Verso page](https://teorth.github.io/analysis/Analysis/Section_6_1/)" in page
    assert "- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_6_1.html)" in page
    appendix = next(text for path, text in files.items() if path.name == "appendix-a-1.md")
    # A section whose labelled items are all examples names no declaration.
    assert appendix.startswith("# Appendix A.1: Mathematical Statements")
    assert "An `example` ([line 4](" in appendix and "An exercise, stated without proof." in appendix
    notation = next(text for path, text in files.items() if path.name == "notation.md")
    assert "Its Lean file imports no other section's file." in notation
    assert "- [Verso page]" not in notation


def test_the_intro_credits_the_repository_and_says_how_statuses_are_read(tmp_path):
    data, chapter, links, forward = built(tmp_path)
    intro = chapter.root.prose
    assert "Terence Tao's Lean companion" in intro and "graphs/contributors" in intro
    assert "> The files in this directory contain a formalization. The formalization is intended to be as faithful" in intro
    assert "A third paragraph." not in intro
    assert "- Lean toolchain v4.29.0-rc8, Mathlib at [bbbbbbbb](" in intro and "- License: Apache-2.0." in intro
    assert "“Proved here.”" in intro and "says nothing of the results the proof uses" in intro
    assert "An edge from one section to another means that the first section's Lean file imports the other's" in intro
    assert "“An axiom.”" not in intro
    for part in walk(chapter.root):
        if isinstance(part, Container) and part is not chapter.root and part.children:
            assert f"at commit [aaaaaaaa](https://github.com/teorth/analysis/tree/{REV})" in part.prose


def test_the_committed_data_build_the_chapter(tmp_path):
    data = analysis.load(ROOT / "data")
    if data is None:
        return
    chapter, links, forward = analysis.chapter(data)
    assign_paths(chapter.root, tmp_path / "vault" / "roadmap" / "analysis")
    blueprints.resolve(chapter, tmp_path / "vault")
    files = render_tree(chapter.root, tmp_path / "vault")
    assert chapter.stats["articles"] == len(data["sections"])
    assert max(len(text.encode()) for text in files.values()) < 100_000
    assert json.loads((ROOT / "data" / "analysis" / "source.json").read_text(encoding="utf-8"))["rev"] == data["rev"]
