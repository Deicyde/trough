import json
import os
import subprocess
from pathlib import Path

import pytest

import refresh_stacks
from trough import blueprints
from trough import stacks
from trough.vault import Container, Leaf, assign_paths, render_tree, walk

ROOT = Path(__file__).resolve().parent.parent
REV = "b" * 40
PROJECT_REV = "c" * 40
BLOB = f"https://github.com/AxiomMath/Stacks/blob/{REV}"

# Shaped like StacksCore's files: a tagged theorem with an EGA reference, then a registration with an SGA one.
CORE = '''module

public import Mathlib.RingTheory.Ideal.Operations
import StacksCore.Tactic.StacksAttribute

/-! # Prime avoidance -/

namespace Ideal

/-- **Prime avoidance**: an ideal inside a finite union of primes is inside one of them. -/
@[stacks 00DS "the version with two non-prime ideals", ega "0 16.2.4" "more general"]
theorem subset_union_prime' (n : ℕ) : n = n := rfl

end Ideal

add_to_stacks 00DS Ideal.subset_union_prime
add_to_sga "3 V 4.1" "more general" Ideal.subset_union_prime
'''

FRONTIER = '''module

import StacksCore.Tactic.StacksAttribute

namespace Stacks

/-- A docstring with <angle> brackets and $x < y$. -/
@[stacks 00DS]
theorem frontier_avoid : True := by
  trivial

@[stacks 01QN "part (2)", sga "4 IV 4.9.4"]
instance : Inhabited Nat where
  default := 0

@[stacks 01QN]
private lemma helper : True := trivial

def byCases : Nat → Nat
  | 0 => 0
  | n + 1 => n

/-- This docstring mentions a command at the start of a line:
add_to_stacks 0000 Not.a.command -/
def note : String := "a string
add_to_stacks 0000 Not.a.command either"

end Stacks

attribute [stacks 01QO "a tag given after the fact"] Stacks.byCases
attribute [stacks 05E3] Other.declared
'''

OTHER = '''namespace Other

theorem declared : True := trivial

end Other
'''

REGISTRATIONS = '''import StacksCore.Tactic.StacksAttribute

add_to_stacks 00DT "the definition, as Mathlib states it; its comment spans
  two lines" Ideal.IsPrime
add_to_stacks 9999 "a comment with a string gap, \\
which Lean reads as one line" Nowhere.listed
'''

FILES = {"StacksCore/Algebra/Foo.lean": CORE, "StacksFrontier/AlgebraicGeometry/Bar.lean": FRONTIER,
         "StacksFrontier/Other.lean": OTHER, "StacksFrontier/MathlibRegistrations/Ch10.lean": REGISTRATIONS}

TAGS = '''# List of current tags in the stacks project
00AO,algebra-section-phantom
00DQ,algebra-section-miscellany
00DS,algebra-lemma-silly
00DT,algebra-definition-prime
05E3,more-algebra-section-phantom
01QM,schemes-section-phantom
01QN,schemes-section-affine
01QO,schemes-lemma-affine
'''

CHAPTERS = '''\\begin{multicols}{2}[\\section{Other chapters}]
\\noindent
Preliminaries
\\begin{enumerate}
\\item \\hyperref[introduction-section-phantom]{Introduction}
\\item \\hyperref[algebra-section-phantom]{Commutative Algebra}
\\item \\hyperref[more-algebra-section-phantom]{More on Algebra}
\\end{enumerate}
Schemes
\\begin{enumerate}
\\setcounter{enumi}{3}
\\item \\hyperref[schemes-section-phantom]{Schemes}
\\end{enumerate}
\\end{multicols}
'''

ALGEBRA = '''\\input{preamble}
\\begin{document}
\\title{Commutative Algebra}
\\maketitle
\\phantomsection
\\label{section-phantom}

\\section{Introduction}
\\label{section-introduction}
Some text. % a comment with \\label{lemma-commented}

\\section{Miscellany}
\\label{section-miscellany}

\\begin{lemma}
\\label{lemma-silly}
A lemma.
\\end{lemma}

\\begin{definition}
\\label{definition-prime}
A definition.
\\end{definition}
\\end{document}
'''

MORE_ALGEBRA = '''\\phantomsection
\\label{section-phantom}

\\section{Introduction}
\\label{section-introduction}
'''

SCHEMES = '''\\phantomsection
\\label{section-phantom}

\\section{Affine schemes $\\Spec(R)$}
\\label{section-affine}

\\begin{lemma}
\\label{lemma-affine}
\\end{lemma}
'''

PROJECT = {"tags/tags": TAGS, "chapters.tex": CHAPTERS, "preamble.tex": "\\def\\Spec{\\mathop{\\rm Spec}}\n",
           "algebra.tex": ALGEBRA, "more-algebra.tex": MORE_ALGEBRA, "schemes.tex": SCHEMES, "introduction.tex": ""}

YAML = '''version: "v0.4"
project:
  name: "Stacks"
  authors: [A. Author, B. Author]
  description: >
    `Stacks` is a Lean 4 formalization of The Stacks Project. `StacksCore` is the human-reviewed library;
    `StacksFrontier` holds drafted formalizations that are not yet reviewed. Community feedback and
    contributions are welcome!
  responsible_maintainers: [B. Author]
  license: "Apache-2.0"
sources:
  - title: "The Stacks Project"
    id: "https://stacks.math.columbia.edu"
    note: "Statements taken from the Stacks project at commit a5811b23a9bfc23256ca49035d7e121533dd6f29."
automation:
  methods:
    - method: "autonomous"
      models: [AxiomProver]
review:
  status: "self-assessed"
  notes: "StacksCore is human-reviewed."
'''

README = '''# The Stacks Project in Lean

## Structure

`import Stacks` brings in both tiers. Every proof is kernel-checked.

* [StacksCore](StacksCore/): human-reviewed formalizations, checked against the Stacks Project. More words.
* [StacksFrontier](StacksFrontier/): formalizations written by AI agents. This is where coverage grows fastest.

## Finding a tag
'''

MANIFEST = json.dumps({"packages": [{"name": "mathlib", "rev": "d" * 40, "inputRev": "v4.35.0"}]})
APACHE = "\n                                 Apache License\n                           Version 2.0, January 2004\n"


def write(root: Path, files: dict[str, str]) -> Path:
    for path, text in files.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    return root


def read_all(tmp_path: Path, files: dict[str, str] = FILES) -> tuple[list[dict], dict, list[str]]:
    write(tmp_path, files)
    return stacks.read(tmp_path, sorted(files, key=stacks.natural))


def data(tmp_path: Path, site: bool = False) -> dict:
    tags, counts, unread = read_all(tmp_path / "repo")
    assert unread == []
    structure, problems = stacks.read_project(write(tmp_path / "project", PROJECT), {record["tag"] for record in tags})
    assert problems == []
    source = {"repo": stacks.REPO, "rev": REV, "date": "2026-11-06T08:31:32Z", "toolchain": "v4.35.0",
              "mathlib": "d" * 40, "mathlib_version": "v4.35.0", "license": "Apache-2.0",
              "project": {"name": "Stacks", "description": "`Stacks` formalizes it. Contributions are welcome!",
                          "authors": ["A. Author"], "maintainers": ["B. Author"]},
              "review": {"status": "self-assessed", "notes": "StacksCore is human-reviewed.", "reviewers": []},
              "automation": {"methods": [{"method": "autonomous", "models": ["AxiomProver"]}], "notes": ""},
              "readme": refresh_stacks.readme_words(README), "counts": counts,
              "site": {"url": stacks.SITE, "tags": site}}
    return {"source": source, "structure": {"repo": stacks.PROJECT, "rev": PROJECT_REV, **structure}, "tags": tags}


def test_lean_strings_decode_escapes_and_gaps():
    assert stacks.lean_string('"a \\"b\\" \\\\ c\\n"') == 'a "b" \\ c\n'
    assert stacks.lean_string('"one \\\n    two"') == "one two"
    # As an attribute list gives it, its whitespace collapsed.
    assert stacks.lean_string('"one \\ two"') == "one two"
    assert stacks.lean_string('"\\x41\\u00e9"') == "Aé"


def test_quotes_escape_the_underscores_and_braces_of_their_prose_only():
    # The site would read "_cris at u_" as emphasis and the "{X/S}" after it as an attribute list.
    doc = ("The slice of (X/S)_cris at u_{X/S}^{-1}h_{X'}, `(X/S)_cris`, $f_*\\mathcal{O}_X$, an escaped \\_.\n\n"
           "    0 ⟶ h_{X'} ⟶ F\n\n"
           "```\nf_{x}\n\n    g_{y}\n```\nafter_{all}")
    assert stacks.literal(doc) == (
        "The slice of (X/S)\\_cris at u\\_\\{X/S}^\\{-1}h\\_\\{X'}, `(X/S)_cris`, $f_*\\mathcal{O}_X$, an escaped \\_.\n\n"
        "    0 ⟶ h_{X'} ⟶ F\n\n"
        "```\nf_{x}\n\n    g_{y}\n```\nafter\\_\\{all}")
    assert stacks.literal("for i<n over N<X>, <https://example.org/a_b>, `j<p`") == (
        "for i`<`n over N`<`X>, <https://example.org/a_b>, `j<p`")
    # A bracket before parentheses that hold no URL reads as text, not as a link.
    assert stacks.comment("g_C = 1 + Σ mᵢ([κᵢ : k](gᵢ - 1))") == "g\\_C = 1 + Σ mᵢ([κᵢ : k\\](gᵢ - 1))"


def test_ega_and_sga_references_read_as_the_attributes_validate_them():
    assert stacks.ega("IV 7.8.3") == ("IV", "7.8.3") and stacks.ega("0 23.1.1") == ("0", "23.1.1")
    assert stacks.ega("V 1.2") is None and stacks.ega("IV 7") is None
    assert stacks.sga("4 IV 4.9.4") == ("4", "IV", "4.9.4") and stacks.sga("1 I 9.5") == ("1", "I", "9.5")
    assert stacks.sga("4½ Th_finitude 1.2") == ("4½", "Th finitude", "1.2")
    assert stacks.sga("6 0 App.1.1") == ("6", "0", "App.1.1")
    assert stacks.sga("8 I 1.1") is None and stacks.sga("4 iv 1.1") is None


def test_a_file_gives_its_tagged_declarations_registrations_and_attribute_commands():
    record = stacks.read_file(FRONTIER, "StacksFrontier/AlgebraicGeometry/Bar.lean")
    assert record["unread"] == []
    declarations = {(item["name"], item["line"]): item for item in record["declarations"]}
    assert list(declarations) == [("Stacks.frontier_avoid", 9), ("", 13), ("Stacks.helper", 17), ("Stacks.byCases", 19)]
    instance = declarations[("", 13)]
    assert instance["statement"] == "instance : Inhabited Nat" and instance["tags"] == [{"tag": "01QN", "comment": "part (2)"}]
    assert instance["sga"] == [{"ref": "4 IV 4.9.4", "comment": ""}]
    assert declarations[("Stacks.helper", 17)]["private"]
    by_cases = declarations[("Stacks.byCases", 19)]
    # A definition by cases has no `:=` before its value: its statement is its header.
    assert by_cases["statement"] == "def byCases : Nat → Nat"
    assert by_cases["tags"] == [{"tag": "01QO", "comment": "a tag given after the fact", "attribute_line": 30}]
    assert record["commands"] == [{"line": 31, "name": "Other.declared", "tags": [{"tag": "05E3", "comment": ""}],
                                   "ega": [], "sga": []}]
    # Neither the docstring's line nor the string's reads as a registration.
    assert record["registrations"] == []
    assert record["names"] == {"Stacks.frontier_avoid": 9, "Stacks.byCases": 19, "Stacks.note": 25}
    registrations = stacks.read_file(REGISTRATIONS, "StacksFrontier/MathlibRegistrations/Ch10.lean")["registrations"]
    assert registrations == [
        {"what": "stacks", "ref": "00DT", "line": 3, "name": "Ideal.IsPrime",
         "comment": "the definition, as Mathlib states it; its comment spans\n  two lines"},
        {"what": "stacks", "ref": "9999", "line": 5, "name": "Nowhere.listed",
         "comment": "a comment with a string gap, which Lean reads as one line"}]


def test_a_structure_without_where_states_itself_whole():
    text = '@[mk_iff, stacks 0121 "(7)"]\nclass IsFinite (n : Nat) : Prop extends Nonempty Nat\n\nsection\nend\n'
    (item,) = stacks.read_file(text, "StacksCore/F.lean")["declarations"]
    assert item["statement"] == "class IsFinite (n : Nat) : Prop extends Nonempty Nat"


def test_what_does_not_read_is_listed_with_its_line():
    text = ('@[stacks 00D]\ntheorem a : True := trivial\n\n@[ega "V 1.2"]\ntheorem b : True := trivial\n\n'
            '@[stacks 00DS]\nexample : True := trivial\n\nadd_to_stacks lower Foo.bar\n'
            'attribute [stacks 00DS] (Foo.bar)\n')
    assert stacks.read_file(text, "StacksFrontier/Bad.lean")["unread"] == [
        {"line": 2, "why": "an attribute that does not read: stacks 00D"},
        {"line": 5, "why": 'an attribute that does not read: ega "V 1.2"'},
        {"line": 7, "why": "an attribute on no declaration the reading finds: stacks 00DS"},
        {"line": 10, "why": "a registration that does not read: add_to_stacks lower Foo.bar"},
        {"line": 11, "why": "an `attribute` command whose names do not read: (Foo.bar)"}]
    assert stacks.read_file("namespace A\nend B\n", "StacksFrontier/Broken.lean")["unread"] == [
        {"line": 0, "why": "its scopes do not close as they open"}]


def test_the_tags_gather_declarations_registrations_and_references_across_files(tmp_path):
    tags, counts, unread = read_all(tmp_path)
    assert unread == []
    by_tag = {record["tag"]: record for record in tags}
    assert list(by_tag) == ["00DS", "00DT", "01QN", "01QO", "05E3", "9999"]
    core, frontier = by_tag["00DS"]["declarations"]
    assert (core["name"], core["tier"], core["file"], core["line"]) == (
        "Ideal.subset_union_prime'", "StacksCore", "StacksCore/Algebra/Foo.lean", 12)
    assert core["comment"] == "the version with two non-prime ideals" and core["doc"].startswith("**Prime avoidance**")
    assert core["ega"] == [{"ref": "0 16.2.4", "comment": "more general"}] and not core["sorry"]
    assert frontier["name"] == "Stacks.frontier_avoid" and frontier["tier"] == "StacksFrontier"
    (registered,) = by_tag["00DS"]["registrations"]
    # The SGA reference registered on the same name goes with the registration.
    assert registered == {"name": "Ideal.subset_union_prime", "file": "StacksCore/Algebra/Foo.lean", "line": 16,
                          "tier": "StacksCore", "comment": "", "ega": [],
                          "sga": [{"ref": "3 V 4.1", "comment": "more general"}]}
    # An `attribute` command in one file tags a declaration of another.
    (declared,) = by_tag["05E3"]["declarations"]
    assert (declared["name"], declared["file"], declared["line"], declared["attribute_file"], declared["attribute_line"]) == (
        "Other.declared", "StacksFrontier/Other.lean", 3, "StacksFrontier/AlgebraicGeometry/Bar.lean", 31)
    assert counts["declarations_StacksCore"] == 1 and counts["declarations_StacksFrontier"] == 5
    assert counts["registrations_StacksCore"] == 1 and counts["registrations_StacksFrontier"] == 2
    assert counts["sga_registrations_StacksCore"] == 1 and (counts["ega_items"], counts["sga_items"]) == (1, 2)
    assert counts["tags_StacksCore"] == 1 and counts["tags_StacksFrontier"] == 6 and counts["sorry"] == 0
    assert counts["files_StacksCore"] == 1 and counts["files_StacksFrontier"] == 3


def test_the_stacks_project_places_each_tag_in_its_section(tmp_path):
    structure, problems = stacks.read_project(write(tmp_path, PROJECT), {"00DS", "00DT", "01QN", "01QO", "05E3", "00AO"})
    assert problems == []
    assert [part["title"] for part in structure["parts"]] == ["Preliminaries", "Schemes"]
    chapters = [chapter for part in structure["parts"] for chapter in part["chapters"]]
    assert [(chapter["number"], chapter["file"], chapter["tag"]) for chapter in chapters] == [
        (1, "introduction", None), (2, "algebra", "00AO"), (3, "more-algebra", "05E3"), (4, "schemes", "01QM")]
    assert chapters[1]["sections"] == [{"number": 1, "title": "Introduction", "tag": None},
                                       {"number": 2, "title": "Miscellany", "tag": "00DQ"}]
    # The preamble's macros are expanded in titles.
    assert chapters[3]["sections"][0]["title"] == "Affine schemes $\\mathop{\\rm Spec}(R)$"
    assert structure["tags"] == {
        "00AO": {"chapter": "algebra", "section": 0, "order": 1, "kind": "chapter"},
        "00DS": {"chapter": "algebra", "section": 2, "order": 4, "kind": "lemma"},
        "00DT": {"chapter": "algebra", "section": 2, "order": 5, "kind": "definition"},
        "01QN": {"chapter": "schemes", "section": 1, "order": 2, "kind": "section"},
        "01QO": {"chapter": "schemes", "section": 1, "order": 3, "kind": "lemma"},
        "05E3": {"chapter": "more-algebra", "section": 0, "order": 1, "kind": "chapter"}}
    _, problems = stacks.read_project(tmp_path / "missing", set())
    assert problems == ["the Stacks Project's tags/tags lists no tags", "the Stacks Project's chapters.tex lists no parts"]


def build(tmp_path: Path, site: bool = False):
    built, links = stacks.chapter(data(tmp_path, site))
    vault = Path("blueprint")
    assign_paths(built.root, vault / "roadmap" / "stacks")
    blueprints.resolve(built, vault)
    return built, links, render_tree(built.root, vault)


ARTICLE = Path("blueprint/roadmap/stacks/preliminaries/2-commutative-algebra/2-2-miscellany.md")


def test_the_chapter_has_a_part_per_stacks_part_a_page_per_chapter_and_an_article_per_section(tmp_path):
    built, links, files = build(tmp_path)
    assert [entry.node.title for entry in built.root.entries] == ["Preliminaries", "Schemes", "EGA", "SGA"]
    preliminaries = built.root.entries[0].node
    assert [entry.node.title for entry in preliminaries.entries] == ["2 Commutative Algebra", "3 More on Algebra"]
    leaves = [node.title for node in walk(built.root) if isinstance(node, Leaf)]
    assert leaves == ["2.2 Miscellany", "3 More on Algebra: the chapter's own tag", "4.1 Affine schemes $\\mathop{\\rm Spec}(R)$"]
    stats = built.stats
    assert (stats["articles"], stats["chapters"], stats["parts"], stats["tags"]) == (3, 3, 2, 5)
    assert (stats["StacksCore"], stats["StacksFrontier"], stats["registrations"], stats["unplaced"]) == (1, 5, 2, 1)
    assert (stats["ega_indexed"], stats["sga_indexed"]) == (1, 2)
    assert links == {"Ideal.IsPrime": stacks.MATHLIB_DOCS.format("Ideal.IsPrime"),
                     "Ideal.subset_union_prime": stacks.MATHLIB_DOCS.format("Ideal.subset_union_prime"),
                     "Ideal.subset_union_prime'": f"{BLOB}/StacksCore/Algebra/Foo.lean#L12",
                     "Other.declared": f"{BLOB}/StacksFrontier/Other.lean#L3",
                     "Stacks.byCases": f"{BLOB}/StacksFrontier/AlgebraicGeometry/Bar.lean#L19",
                     "Stacks.frontier_avoid": f"{BLOB}/StacksFrontier/AlgebraicGeometry/Bar.lean#L9",
                     "Stacks.helper": f"{BLOB}/StacksFrontier/AlgebraicGeometry/Bar.lean#L17"}
    assert all(len(node.children) <= 20 for node in walk(built.root) if isinstance(node, Container))


def test_an_article_has_one_kind_of_front_matter_and_a_block_per_tag(tmp_path):
    _, _, files = build(tmp_path)
    page = files[ARTICLE]
    assert page.startswith("---\ndeclaration: section\norigin: cited\nlean: Ideal.subset_union_prime', "
                           "Stacks.frontier_avoid, Ideal.subset_union_prime, Ideal.IsPrime\nstatement: formalized\n"
                           "proof: formalized\n---\n\n# 2.2 Miscellany\n\nSection 2.2 of the Stacks Project, "
                           "[Tag 00DQ](https://stacks.math.columbia.edu/tag/00DQ). 2 tags here are carried by 2 "
                           "declarations of the repository (1 in StacksCore and 1 in StacksFrontier) and 2 registered "
                           "declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit")
    assert page.index("## Tag 00DS, a lemma") < page.index("## Tag 00DT, a definition")
    assert "[Tag 00DS](https://stacks.math.columbia.edu/tag/00DS) in the Stacks Project.\n" in page
    assert ("**`Ideal.subset_union_prime'`**, a theorem in StacksCore (human-reviewed), declared in "
            f"[StacksCore/Algebra/Foo.lean, line 12]({BLOB}/StacksCore/Algebra/Foo.lean#L12). The attribute's comment: "
            "“the version with two non-prime ideals”. References: EGA 0 (16.2.4), “more general”.") in page
    assert ("> **Prime avoidance**: an ideal inside a finite union of primes is inside one of them.\n\n"
            "```lean\ntheorem subset_union_prime' (n : ℕ) : n = n\n```") in page
    assert "**`Stacks.frontier_avoid`**, a theorem in StacksFrontier (drafted, not yet reviewed)" in page
    assert "> A docstring with `<`angle> brackets and $x < y$." in page
    assert (f"- [`Ideal.subset_union_prime`]({stacks.MATHLIB_DOCS.format('Ideal.subset_union_prime')}) registered with "
            f"`add_to_stacks` in [StacksCore/Algebra/Foo.lean, line 16]({BLOB}/StacksCore/Algebra/Foo.lean#L16) "
            "(StacksCore). References: SGA 3 V (4.1), “more general”.") in page
    assert ("registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 3]"
            f"({BLOB}/StacksFrontier/MathlibRegistrations/Ch10.lean#L3) (StacksFrontier): “the definition, as Mathlib "
            "states it; its comment spans two lines”.") in page
    assert stacks.NO_DEPENDS in page and "stacks.axiommath.ai" not in page
    schemes = files[Path("blueprint/roadmap/stacks/schemes/4-schemes/4-1-affine-schemes-rm-spec-r.md")]
    assert "## Tag 01QN, the section" in schemes and "## Tag 01QO, a lemma" in schemes
    assert ("**An instance with no name** in StacksFrontier (drafted, not yet reviewed), declared in "
            f"[StacksFrontier/AlgebraicGeometry/Bar.lean, line 13]") in schemes
    assert "**`Stacks.helper`**, a private lemma in StacksFrontier" in schemes
    assert (f"The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Bar.lean, line 30]"
            f"({BLOB}/StacksFrontier/AlgebraicGeometry/Bar.lean#L30).") in schemes
    chapter_tag = files[Path("blueprint/roadmap/stacks/preliminaries/3-more-on-algebra/3-0-chapter.md")]
    assert "The tag of Chapter 3 of the Stacks Project as a whole." in chapter_tag
    assert "## Tag 05E3, the chapter" in chapter_tag


def test_pages_credit_the_repository_and_the_stacks_project(tmp_path):
    _, _, files = build(tmp_path)
    root = files[Path("blueprint/roadmap/stacks/README.md")]
    assert "This chapter maps it as read at commit [bbbbbbbb]" in root and "no continuous integration" in root
    assert "“`Stacks` formalizes it. …”" in root and "welcome" not in root
    assert ("Its README: “`import Stacks` brings in both tiers. Every proof is kernel-checked.” It describes StacksCore "
            "as “human-reviewed formalizations, checked against the Stacks Project.” and StacksFrontier as "
            "“formalizations written by AI agents.”") in root
    assert "- Maintainers: B. Author." in root and "- Review status: “self-assessed”." in root
    assert ("There are 3 articles, one for each section of the Stacks Project with a tag that a declaration carries, in "
            "3 chapters and 2 parts") in root
    assert "GNU Free Documentation License" in root and f"at commit [cccccccc](https://github.com/{stacks.PROJECT}/tree/" in root
    assert "its tag pages answer as missing pages when fetched, so the blocks do not link them" in root
    assert "The articles have no dependencies: edges between declarations need Lean." in root
    assert "[EGA](ega/README.md) (1 items)" not in root and "[EGA](ega/README.md) (1 item" in root
    assert ("Tags that the Stacks Project does not list at commit [cccccccc]"
            f"(https://github.com/{stacks.PROJECT}/tree/{PROJECT_REV}), so with no article: 9999, carried by "
            "`Nowhere.listed` (registered).") in root
    part = files[Path("blueprint/roadmap/stacks/preliminaries/README.md")]
    assert "under its Apache-2.0 license" in part and "[bbbbbbbb]" in part
    chapter = files[Path("blueprint/roadmap/stacks/preliminaries/2-commutative-algebra/README.md")]
    assert ("Chapter 2 of the Stacks Project, *Commutative Algebra*, [Tag 00AO](https://stacks.math.columbia.edu/tag/00AO): "
            "its one section with a tag that a declaration carries.") in chapter


def test_the_indexes_list_each_reference_with_its_articles(tmp_path):
    _, _, files = build(tmp_path)
    ega = files[Path("blueprint/roadmap/stacks/ega/ega-0/README.md")]
    assert "### §16\n\n- (16.2.4): [2.2 Miscellany](../../preliminaries/2-commutative-algebra/2-2-miscellany.md) (“more general”)" in ega
    sga = files[Path("blueprint/roadmap/stacks/sga/sga-4/README.md")]
    assert "### Exposé IV\n\n- (4.9.4): [4.1 Affine schemes $\\mathop{\\rm Spec}(R)$]" in sga
    index = files[Path("blueprint/roadmap/stacks/sga/README.md")]
    assert "2 items, on a page per volume" in index


def test_the_blocks_link_the_site_only_when_it_serves_tag_pages(tmp_path):
    _, _, files = build(tmp_path, site=True)
    assert f"[its page]({stacks.SITE}library?tag=00DS) on the repository's site" in files[ARTICLE]
    assert "each block links the tag's page there" in files[Path("blueprint/roadmap/stacks/README.md")]


def test_the_site_check_reads_its_tag_page_and_its_data():
    base = "https://cdn.example.org/deploy/"
    pages = {stacks.SITE: f'<html data-base="{base}">'.encode(), f"{stacks.SITE}library?tag=00DS": b"<html>",
             f"{base}api/entity/00DS.json": json.dumps({"entity": {"tag": "00DS"}}).encode(),
             f"{base}api/entity/01QN.json": json.dumps({"entity": {"tag": "01QN"}}).encode()}

    def fetch(url: str, method: str) -> bytes | None:
        return pages.get(url)

    assert stacks.site_problem(stacks.SITE, ["00DS", "01QN"], fetch) is None
    assert stacks.site_problem(stacks.SITE, ["00DS", "05E3"], fetch) == "its data has no entry for tag 05E3"
    del pages[f"{stacks.SITE}library?tag=00DS"]
    assert stacks.site_problem(stacks.SITE, ["00DS"], fetch) == f"{stacks.SITE}library?tag=00DS answers that it has no such page"
    assert stacks.sample([f"{n:04d}" for n in range(100)], 4) == ["0000", "0025", "0050", "0075"]


def git(path: Path, *args: str) -> str:
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@example.org", "GIT_AUTHOR_DATE": "2026-11-06T08:31:32+02:00",
           "GIT_COMMITTER_DATE": "2026-11-06T08:31:32+02:00"}
    return subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True, text=True, env=env).stdout


def commit(root: Path, files: dict[str, str]) -> Path:
    write(root, files)
    git(root, "init", "--quiet")
    git(root, "add", "-A")
    git(root, "commit", "--quiet", "-m", "release")
    return root


def checkout(root: Path, files: dict[str, str] = FILES, license_text: str = APACHE, config: str = YAML) -> Path:
    # Shaped like the sparse checkout the workflow makes.
    return commit(root, files | {"LICENSE": license_text, "formalization.yaml": config, "README.md": README,
                                 "lean-toolchain": "leanprover/lean4:v4.35.0\n", "lake-manifest.json": MANIFEST})


def no_site(url: str, method: str) -> bytes | None:
    return None


def test_the_refresh_writes_the_source_the_structure_and_the_tags(tmp_path):
    out = tmp_path / "data" / "stacks"
    repo, project = checkout(tmp_path / "stacks"), commit(tmp_path / "project", PROJECT)
    assert refresh_stacks.refresh(repo, project, out, stacks.SITE, no_site) == []
    source = json.loads((out / "source.json").read_text(encoding="utf-8"))
    rev = git(repo, "rev-parse", "HEAD").strip()
    # The commit date is written in UTC.
    assert (source["repo"], source["rev"], source["date"], source["toolchain"]) == (
        stacks.REPO, rev, "2026-11-06T06:31:32Z", "v4.35.0")
    assert (source["mathlib"], source["mathlib_version"], source["license"]) == ("d" * 40, "v4.35.0", "Apache-2.0")
    assert source["project"]["maintainers"] == ["B. Author"] and source["review"]["status"] == "self-assessed"
    assert source["readme"]["tiers"] == {"StacksCore": "human-reviewed formalizations, checked against the Stacks Project.",
                                         "StacksFrontier": "formalizations written by AI agents."}
    assert source["counts"]["declarations_StacksFrontier"] == 5 and source["site"] == {"url": stacks.SITE, "tags": False}
    structure = json.loads((out / "structure.json").read_text(encoding="utf-8"))
    assert structure["repo"] == stacks.PROJECT and structure["rev"] == git(project, "rev-parse", "HEAD").strip()
    assert "9999" not in structure["tags"] and structure["tags"]["00DS"]["section"] == 2
    assert sorted(path.name for path in (out / "tags").iterdir()) == ["00.json", "01.json", "05.json", "99.json"]
    shard = json.loads((out / "tags" / "00.json").read_text(encoding="utf-8"))
    assert shard["schema"] == stacks.SCHEMA and shard["rev"] == rev
    assert [record["tag"] for record in shard["tags"]] == ["00DS", "00DT"]
    assert len(stacks.load(tmp_path / "data")["tags"]) == 6


def test_the_refresh_writes_nothing_from_a_checkout_it_cannot_read_in_full(tmp_path):
    project = commit(tmp_path / "project", PROJECT)

    def refused(root: Path, against: Path = project) -> list[str]:
        out = tmp_path / "out"
        problems = refresh_stacks.refresh(root, against, out, None, no_site)
        assert not out.exists()
        return problems

    mit = checkout(tmp_path / "mit", license_text="MIT License\n")
    assert refused(mit) == [f"{stacks.REPO} at {git(mit, 'rev-parse', 'HEAD')[:8]}: not Apache-2.0 "
                            "(formalization.yaml says 'Apache-2.0')"]
    gone = checkout(tmp_path / "gone")
    (gone / "StacksFrontier/Other.lean").unlink()
    assert refused(gone) == ["not checked out: StacksFrontier/Other.lean"]
    unread = FILES | {"StacksFrontier/Bad.lean": "@[stacks 00D]\ntheorem a : True := trivial\n",
                      "StacksFrontier/Broken.lean": "namespace A\nend B\n"}
    assert refused(checkout(tmp_path / "unread", unread)) == [
        "StacksFrontier/Bad.lean:2 an attribute that does not read: stacks 00D",
        "StacksFrontier/Broken.lean:0 its scopes do not close as they open"]
    assert refused(checkout(tmp_path / "good"), commit(tmp_path / "empty", {"tags/tags": TAGS})) == [
        "the Stacks Project's chapters.tex lists no parts"]


def test_the_refresh_refuses_a_record_with_under_half_the_last_tags(tmp_path):
    out = tmp_path / "out"
    (out / "tags").mkdir(parents=True)
    last = {"schema": stacks.SCHEMA, "rev": "e" * 40, "tags": [{"tag": f"0A{n:02d}"} for n in range(20)]}
    (out / "tags" / "0A.json").write_text(json.dumps(last), encoding="utf-8")
    problems = refresh_stacks.refresh(checkout(tmp_path / "stacks"), commit(tmp_path / "project", PROJECT), out, None,
                                      no_site)
    assert problems == ["6 tags, under half the 20 of the last record"]
    assert json.loads((out / "tags" / "0A.json").read_text(encoding="utf-8")) == last
    assert not (out / "source.json").exists()


def test_an_unreachable_site_keeps_the_last_value_only_for_the_same_tags(tmp_path):
    def unreachable(url: str, method: str) -> bytes | None:
        raise stacks.Unreachable(url)

    out = tmp_path / "out"
    repo, project = checkout(tmp_path / "stacks"), commit(tmp_path / "project", PROJECT)
    assert refresh_stacks.refresh(repo, project, out, stacks.SITE, no_site) == []
    source = out / "source.json"
    record = json.loads(source.read_text(encoding="utf-8"))
    source.write_text(json.dumps(record | {"site": {"url": stacks.SITE, "tags": True}}), encoding="utf-8")
    assert refresh_stacks.refresh(repo, project, out, stacks.SITE, unreachable) == []
    assert json.loads(source.read_text(encoding="utf-8"))["site"] == {"url": stacks.SITE, "tags": True}
    source.write_text(json.dumps(record | {"site": {"url": stacks.SITE, "tags": True}}), encoding="utf-8")
    fewer = checkout(tmp_path / "fewer", {path: text for path, text in FILES.items() if "Registrations" not in path})
    assert refresh_stacks.refresh(fewer, project, out, stacks.SITE, unreachable) == []
    assert json.loads(source.read_text(encoding="utf-8"))["site"] == {"url": stacks.SITE, "tags": False}


@pytest.mark.skipif(stacks.load(ROOT / "data") is None, reason="no Stacks data committed")
def test_the_committed_data_build_the_chapter():
    loaded = stacks.load(ROOT / "data")
    assert loaded["source"]["repo"] == stacks.REPO and len(loaded["source"]["rev"]) == 40
    assert loaded["structure"]["repo"] == stacks.PROJECT and len(loaded["structure"]["rev"]) == 40
    for record in loaded["tags"]:
        assert stacks.TAG.match(record["tag"])
        for block in record["declarations"]:
            assert block["tier"] in stacks.TIERS and block["statement"]
    built, links = stacks.chapter(loaded)
    leaves = [node for node in walk(built.root) if isinstance(node, Leaf)]
    assert len(leaves) == built.stats["articles"] > 0
    assert set(links) == {name for leaf in leaves for name in dict(leaf.fields).get("lean", "").split(", ") if name}
    assert all(len(dict(leaf.fields).get("lean", "").split(", ")) <= stacks.LEAN_NAMES for leaf in leaves)
    assert all(dict(leaf.fields)["declaration"] == "section" for leaf in leaves)
    assert all(len(node.children) <= 20 for node in walk(built.root) if isinstance(node, Container))
