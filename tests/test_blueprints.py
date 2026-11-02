from pathlib import Path

import pytest

from trough import blueprints, leanblueprint, tex
from trough.vault import assign_paths, walk

DATA = Path(__file__).resolve().parent.parent / "data" / "blueprints"


def test_macros_expand_with_arguments_defaults_and_operators():
    macros = tex.definitions(
        r"\newcommand{\abs}[1]{\left|#1\right|}\newcommand\pair[2][x]{(#1,#2)}"
        r"\DeclareMathOperator{\dist}{dist}\renewcommand{\phi}{\varphi}\def\op{\diamond}"
    )
    assert tex.expand(r"\abs{a} \pair{b} \pair[c]{d} \dist \phi", macros) == r"\left|a\right| (x,b) (c,d) \operatorname{dist} \varphi"
    assert tex.expand(r"x \op y", macros) == r"x \diamond y"
    assert tex.expand(r"\op{}x", macros) == r"\diamond{}x"


def test_a_macro_can_define_macros_as_it_goes():
    macros = tex.definitions(
        r"\newcommand{\Equadef}[2]{\expandafter\gdef\csname Equa#1\endcsname{\ensuremath{#2}}}"
        r"\newcommand{\Equaref}[1]{E#1 $(\csname Equa#1\endcsname)$}"
    )
    assert tex.expand(r"\Equadef{14}{x = y}", macros) == ""
    assert tex.expand(r"\Equaref{14}", macros) == r"E14 $(\ensuremath{x = y})$"


def writer(**kwargs):
    return tex.Writer({}, ref=lambda label, command: f"[{label}](trough:{label})", **kwargs)


def test_text_lists_and_formulas_become_markdown():
    md = writer().statement(
        r"""Let $x<y$ and \emph{suppose} \textbf{this}, see \cite[p.~3]{wiles}, \href{https://a.org/x}{here}
        and Szemer\'edi.
        \begin{itemize}\item[(i)] first $a$
        \item[(ii)] second\end{itemize}
        \begin{enumerate}\item one \item two\end{enumerate}
        \begin{align*} a &= b \label{eq} \\ c &= d \end{align*}
        By \Cref{lem:x, lem:y}, done."""
    )
    assert r"$x\lt y$" in md
    assert "*suppose* **this**, see \\[wiles, p. 3\\], [here](https://a.org/x) and Szemerédi." in md
    assert "- (i) first $a$\n- (ii) second" in md
    assert "1. one\n2. two" in md
    assert "$$\n\\begin{aligned} a &= b  \\\\ c &= d \\end{aligned}\n$$" in md
    assert "By [lem:x](trough:lem:x) and [lem:y](trough:lem:y), done." in md


def test_text_that_reads_as_markdown_is_escaped():
    md = writer().statement("1. first, a_b * c [d] < e")
    assert md == r"1\. first, a\_b \* c \[d\] $<$ e"
    assert writer().plain(r"Balog--Szemer\'edi--Gowers for $\tau$") == r"Balog–Szemerédi–Gowers for $\tau$"


def test_unknown_commands_keep_their_text_and_are_counted():
    w = writer()
    assert w.statement(r"\mystery{kept} and \blah done") == "kept and done"
    assert w.unknown == {"mystery": 1, "blah": 1}


BLUEPRINT = r"""
\documentclass{report}
\usepackage[showmore, dep_graph]{blueprint}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\R}{\mathbb{R}}
\dochome{https://example.org/docs}
\github{https://github.com/o/p}
\begin{document}
\input{chapter/one}
\end{document}
"""

CHAPTER = r"""
\chapter{First}\label{ch:first}
Some prose about $\R$.
\section{Basics}
\begin{definition}[Thing]\label{def:thing}\lean{Thing}\leanok
A thing is a map to $\R$.
\end{definition}
\begin{lemma}\label{lem:a}\label{lem:a-alias}\lean{Old}\lean{A.one, A.two}\uses{def:thing}\leanok
By \cref{def:thing}, things exist.
\end{lemma}
\begin{proof}\leanok\uses{def:thing}\label{lem:a-proof-label} Clear. \end{proof}
\begin{remark} A remark. \end{remark}
\begin{proof} Proves the remark, not the lemma. \end{proof}
\begin{lemma}\uses{lem:a}\notready
Unlabelled and not ready.
\end{lemma}
\section{More}
\begin{proof} An orphan proof. \end{proof}
\begin{theorem}[Main]\label{thm:main}\uses{lem:a}\mathlibok\lean{Mathlib.main}
Main.
\end{theorem}
\begin{theorem}\label{thm:noname}\mathlibok
In Mathlib, unnamed.
\end{theorem}
\begin{lemma}\label{lem:late}\proves{lem:a}\leanok
\end{lemma}
\begin{proof}\proves{lem:a}\uses{thm:main} A later proof of lem:a replaces the first. \end{proof}
"""


@pytest.fixture
def blueprint(tmp_path):
    (tmp_path / "chapter").mkdir()
    (tmp_path / "web.tex").write_text(BLUEPRINT)
    (tmp_path / "chapter" / "one.tex").write_text(CHAPTER)
    return leanblueprint.read(tmp_path, "web.tex")


def test_blueprint_nodes_follow_leanblueprint(blueprint):
    nodes = {node.id: node for node in blueprint.nodes}
    assert blueprint.files == ["web.tex", "chapter/one.tex"]
    assert [node.id for node in blueprint.graph] == ["def:thing", "lem:a-proof-label", "lemma-one-1", "thm:main", "thm:noname", "lem:late"]
    lemma = nodes["lem:a-proof-label"]  # the last label, from its proof, is the id
    assert lemma.labels == ["lem:a", "lem:a-alias", "lem:a-proof-label"]
    assert lemma.lean == ["A.one", "A.two"]  # the last \lean wins
    assert lemma.proof.uses == ["thm:main"] and not lemma.proof.leanok  # the later proof replaced the first
    assert not nodes["remark-one-1"].graph and nodes["remark-one-1"].proof is not None
    assert nodes["lemma-one-1"].notready
    assert nodes["thm:main"].mathlibok and nodes["thm:main"].leanok
    assert blueprint.links == {"dochome": "https://example.org/docs", "github": "https://github.com/o/p"}
    assert any("orphan" in problem or "no theorem" in problem for problem in blueprint.problems)
    assert blueprint.labels["ch:first"].title == "First"


def project(tmp_path: Path, text: bool = True) -> blueprints.Project:
    return blueprints.Project("demo", "Demo", "o/p", "0123456789abcdef", "2026-11-02T00:00:00Z", "blueprint/src/web.tex",
                              "Apache-2.0", text, tmp_path)


def build(blueprint, tmp_path, heads=None):
    built = blueprints.chapter(project(tmp_path), blueprint, heads or {})
    assign_paths(built.root, Path("blueprint/roadmap/demo"))
    blueprints.resolve(built, Path("blueprint"))
    return built, {node.title: node for node in walk(built.root) if not hasattr(node, "entries")}


def test_articles_carry_the_blueprints_marks(blueprint, tmp_path):
    built, leaves = build(blueprint, tmp_path)
    assert dict(leaves["Thing"].fields) == {"declaration": "definition", "origin": "cited", "lean": "Thing", "statement": "formalized"}
    lemma = dict(leaves["a-proof-label"].fields)
    assert lemma["lean"] == "A.one, A.two" and lemma["statement"] == "formalized" and "proof" not in lemma
    assert dict(leaves["Main"].fields)["mathlib_declaration"] == "Mathlib.main"
    assert "mathlib" not in dict(leaves["noname"].fields)
    assert dict(leaves["lemma-one-1"].fields)["not_ready"] == "true"
    assert [leaf.title for leaf in leaves["lemma-one-1"].depends] == ["a-proof-label"]
    assert [leaf.title for leaf in leaves["a-proof-label"].proof_depends] == ["Main"]
    assert "[Definition Thing]" not in leaves["a-proof-label"].body
    assert "By [Thing](def-thing.md), things exist." == leaves["a-proof-label"].body
    assert built.lean_links["A.one"] == "https://example.org/docs/find/#doc/A.one"
    assert built.root.entries[0].node.title == "First"
    assert "Some prose about $\\mathbb{R}$." in built.root.entries[0].node.prose


def test_a_node_in_mathlib_is_the_mathlib_article_it_names(blueprint, tmp_path):
    from trough.vault import Leaf

    mathlib_leaf = Leaf("Main theorem", "main", [("mathlib", "true")], "x")
    mathlib_leaf.path = Path("blueprint/roadmap/mathlib/main.md")
    built, leaves = build(blueprint, tmp_path, {"Mathlib.main": mathlib_leaf})
    assert "Main" not in leaves
    assert leaves["a-proof-label"].proof_depends == [mathlib_leaf]


def test_a_library_without_a_license_shows_structure_only(blueprint, tmp_path):
    data = blueprints.structure(blueprint)
    assert "body" not in str(data["nodes"][0].keys())
    again = blueprints.from_structure(data)
    built = blueprints.chapter(project(tmp_path, text=False), again, {})
    assign_paths(built.root, Path("blueprint/roadmap/demo"))
    leaves = [node for node in walk(built.root) if not hasattr(node, "entries")]
    assert len(leaves) == 6
    assert all("does not reproduce its text" in leaf.body for leaf in leaves)


@pytest.mark.parametrize("library, nodes", [("pfr", 219), ("equational-theories", 214), ("flt", 241), ("strongpnt", 621)])
def test_vendored_blueprints_read_whole(library, nodes):
    project = blueprints.load_projects(DATA.parent, [{"id": library, "name": library}])[0]
    blueprint = blueprints.load_blueprint(project)
    assert len(blueprint.graph) == nodes
    built = blueprints.chapter(project, blueprint, {})
    assert built.stats["nodes"] == nodes and not built.unknown
