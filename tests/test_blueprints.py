import json
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
    assert "*suppose* **this**, see (wiles, p. 3), [here](https://a.org/x) and Szemerédi." in md
    assert "- (i) first $a$\n- (ii) second" in md
    assert "1. one\n2. two" in md
    assert "$$\n\\begin{aligned} a &= b  \\\\ c &= d \\end{aligned}\n$$" in md
    assert "By [lem:x](trough:lem:x) and [lem:y](trough:lem:y), done." in md


def test_text_that_reads_as_markdown_is_escaped():
    md = writer().statement("1. first, a_b * c [d] < e")
    assert md == r"1\. first, a\_b \* c [d] $<$ e"
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


def test_a_label_across_lines_is_one_line(tmp_path):
    (tmp_path / "web.tex").write_text(
        "\\begin{document}\n\\begin{lemma}\\label{A.one,\n    A.two}\\uses{B,\n  C}\n"
        "Text.\n\\end{lemma}\n\\end{document}\n"
    )
    [node] = leanblueprint.read(tmp_path, "web.tex").graph
    assert node.id == "A.one, A.two" and node.uses == ["B", "C"]


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
    unlabelled = leaves["Lemma: Unlabelled and not ready."]  # a node with no label or title is headed by its text
    assert dict(unlabelled.fields)["not_ready"] == "true"
    assert [leaf.title for leaf in unlabelled.depends] == ["a-proof-label"]
    assert [leaf.title for leaf in leaves["a-proof-label"].proof_depends] == ["Main"]
    assert "[Definition Thing]" not in leaves["a-proof-label"].body
    assert "By [Thing](def-thing.md), things exist." == leaves["a-proof-label"].body
    assert built.lean_links["A.one"] == "https://example.org/docs/find/#doc/A.one"
    first = built.root.entries[0].node
    assert first.title == "First" and first.prose == "Some prose about $\\mathbb{R}$."
    basics = first.entries[0].node
    # The remark and its proof sit between the cards of the nodes around them.
    assert [entry.node.title for entry in basics.entries] == ["Thing", "a-proof-label", "Lemma: Unlabelled and not ready."]
    assert basics.entries[2].before == "**Remark.** A remark.\n\n*Proof.* Proves the remark, not the lemma."


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


@pytest.mark.parametrize("library", sorted(path.name for path in DATA.iterdir() if (path / "source.json").is_file()))
def test_vendored_blueprints_read_as_refreshed(library):
    """Each vendored blueprint reads to the node count its refresh recorded, and every
    reference in its pages resolves."""
    project = blueprints.load_projects(DATA.parent, [{"id": library, "name": library}])[0]
    source = json.loads((project.directory / "source.json").read_text(encoding="utf-8"))
    blueprint = blueprints.load_blueprint(project)
    assert len(blueprint.graph) == source["nodes"] > 0
    assert not [problem for problem in blueprint.problems if leanblueprint.UNREAD.search(problem)]
    built = blueprints.chapter(project, blueprint, {})
    assign_paths(built.root, Path("blueprint/roadmap") / library)
    blueprints.resolve(built, Path("blueprint"))
    assert built.stats["nodes"] == source["nodes"]


def test_formulas_keep_dollars_inside_braces_and_let_copies_a_meaning():
    assert writer().statement(r"If $x = \text{a $y$ b}$ then.") == r"If $x = \text{a $y$ b}$ then."
    assert tex.expand(r"$\phi$", tex.definitions(r"\let\oldphi\phi \renewcommand{\phi}{\oldphi_0}")) == r"$\phi_0$"


def test_titles_keep_their_formulas_and_quotes_close():
    assert writer().plain(r"Reduction to \texorpdfstring{$n\geq5$}{ngeq5} and prime") == r"Reduction to $n\geq5$ and prime"
    assert writer().statement(r"call it `the $x'$ map' and `don't'") == r"call it ‘the $x'$ map’ and ‘don't’"


def test_lists_stay_lists():
    w = writer()
    assert w.statement(r"\begin{itemize}\item \[ x = y \]. \item two \end{itemize}") == "- $$\n    x = y.\n    $$\n\n- two"
    nested = r"\begin{enumerate}\item one \begin{itemize}\item a \item b\end{itemize} \item two\end{enumerate}"
    assert w.statement(nested) == "1. one\n\n    - a\n    - b\n\n2. two"


def test_missing_files_are_problems(tmp_path):
    (tmp_path / "web.tex").write_text("\\begin{document}\\input{gone}\\inputleanmodule{Demo.Gone}\\end{document}\n")
    problems = leanblueprint.read(tmp_path, "web.tex").problems
    assert problems == ["web.tex:1: \\input{gone} names no file", "web.tex:1: \\inputleanmodule{Demo.Gone} names no module"]
    assert all(leanblueprint.UNREAD.search(problem) for problem in problems)  # so a refresh refuses
    with pytest.raises(FileNotFoundError):
        leanblueprint.read(tmp_path, "renamed.tex")


def test_a_proof_inside_a_proof_is_part_of_it(tmp_path):
    (tmp_path / "web.tex").write_text(
        "\\begin{document}\\chapter{C}\\begin{lemma}\\label{a} A. \\end{lemma}\n"
        "\\begin{proof}\\leanok Outer. \\begin{proof} Inner. \\end{proof} \\end{proof}\n"
        "\\begin{lemma}\\label{b}\\leanok B. \\end{lemma}\\begin{proof}\\mathlibok\\end{proof}\\end{document}\n"
    )
    a, b = leanblueprint.read(tmp_path, "web.tex").graph
    assert a.proof.leanok and "Outer." in a.proof.body and "Inner." in a.proof.body
    assert b.proof.leanok  # \mathlibok marks a proof formalized, as in leanblueprint


PAGES = r"""
\documentclass{report}
\newtheorem{lemma}{Lemma}
\newtheorem{theorem}{Theorem}
\newtheorem{remark}{Remark}
\begin{document}
\chapter{Eq}
Consider
\begin{equation}\label{eq:a} a = b \end{equation}
\begin{lemma}\label{lem:e}By \eqref{eq:a}, and
\begin{align} c &= d \label{eq:c} \\ e &= f \end{align}
so \eqref{eq:c} and \ref{eq:c}.
\end{lemma}
\begin{remark}\label{rem:x} Remark text. \end{remark}
\section{Sub}
See \cref{lem:e}, Lemma~\ref{lem:e}, \eqref{eq:c}, \cref{rem:x} and \cite[p.~1]{knuth}.
\subsection{Deeper}
Text here.
\begin{theorem}\label{my thm} T. \end{theorem}
After, by \cref{my thm}.
\section{Words}
Only words, in a section with no nodes.
\bibliography{refs}
\end{document}
"""


def test_pages_read_in_the_blueprints_order(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "web.tex").write_text(PAGES)
    (tmp_path / "src" / "refs.bib").write_text(
        "@book{knuth, author = {Knuth, Donald E.}, title = {Art}, year = 1968, doi = {10.1/x}}\n"
    )
    blueprint = leanblueprint.read(tmp_path / "src", "web.tex")
    assert blueprint.bibliography == ["refs.bib"]
    built = blueprints.chapter(project(tmp_path), blueprint, {})
    assign_paths(built.root, Path("blueprint/roadmap/demo"))
    blueprints.resolve(built, Path("blueprint"))
    eq = built.root.entries[0].node
    assert eq.prose == "Consider\n\n$$\na = b\\qquad\\text{(1)}\n$$"
    lemma = eq.entries[0].node
    assert lemma.body == ("By [(1)](README.md), and\n\n$$\n\\begin{aligned} c &= d\\qquad\\text{(2)}\\\\ e &= f "
                          "\\end{aligned}\n$$\n\nso (2) and 2.")
    sub, words = eq.entries[1].node, eq.entries[2].node
    assert eq.entries[1].before == "**Remark.** Remark text."
    assert sub.prose == ("See [Lemma e](../lem-e.md), Lemma [e](../lem-e.md), [(2)](../lem-e.md), [Remark "
                         "x](../README.md) and ([Knuth 1968](https://doi.org/10.1/x), p. 1).\n\n## Deeper\n\nText here.")
    assert [entry.node.title for entry in sub.entries] == ["my thm"]
    assert sub.tail == "After, by [Theorem my thm](my-thm.md)."
    assert words.prose == "Only words, in a section with no nodes." and not words.entries


def test_leanarchitect_output_reads_where_it_is_placed(tmp_path):
    """LeanArchitect's files, written under .lake/build/blueprint with the build's absolute
    paths, are read from the copy in leanarchitect/ where \\inputleanmodule places them."""
    build = "/home/runner/work/demo/demo/./.lake/build/blueprint"
    files = {
        "web.tex": "\\documentclass{report}\n\\usepackage[thms=lemma]{blueprint}\n\\input{blueprint}\n\\end{document}\n",
        "blueprint.tex": ("\\input{../../.lake/build/blueprint/library/Demo}\n\\newtheorem{lemma}{Lemma}\n"
                          "\\begin{document}\n\\chapter{Demo}\nOpening.\n\\inputleanmodule{Demo.A}\n"),
        "leanarchitect/library/Demo.tex": f"\\input{{{build}/module/Demo/A.tex}}\n",
        "leanarchitect/module/Demo/A.tex": (
            "%%% This file is automatically generated by LeanArchitect. %%%\n\\makeatletter\n"
            "\\providecommand{\\newleannode}[2]{%\n  \\expandafter\\gdef\\csname leannode@#1\\endcsname{#2}}\n"
            "\\makeatother\n\n"
            f"\\newleannode{{lem:a}}{{\\input{{{build}/module/Demo/A.artifacts/lem:a}}}}\n\n"
            "\\newleanmodule{Demo.A}{\nSome module prose.\n\n\\inputleannode{lem:a}\n}"
        ),
        "leanarchitect/module/Demo/A.artifacts/lem:a.tex": (
            "\\begin{lemma}[A lemma]\\label{lem:a}\\lean{Demo.a}\\leanok\nStatement.\n\\end{lemma}\n"
            "\\begin{proof}\\leanok\nProof.\n\\end{proof}\n"
        ),
    }
    for name, text in files.items():
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / name).write_text(text)
    blueprint = leanblueprint.read(tmp_path, "web.tex")
    assert not blueprint.problems
    [node] = blueprint.graph
    assert (node.id, node.lean, node.leanok, node.proof.leanok) == ("lem:a", ["Demo.a"], True, True)
    assert node.where.file == "leanarchitect/module/Demo/A.artifacts/lem:a.tex"
    assert [prose.text for prose in blueprint.prose] == ["Opening.\n\nSome module prose."]
    assert project(tmp_path).source(node.where) == ("Demo/A.lean", "https://github.com/o/p/blob/0123456789abcdef/Demo/A.lean")


ROUND_TWO = r"""
\documentclass{report}
\newtheorem{lemma}{Lemma}
\newtheorem{theorem}{Theorem}
\newtheorem{remark}{Remark}
\begin{document}
Opening words before any chapter.
\chapter{Main}
\begin{theorem}\label{thm:t} The theorem. \end{theorem}
Some lemmas first, as Table~\ref{tab:laws} and \cref{tab:laws} list.
\begin{table}[h]\begin{tabular}{cc} law & order \\ \hline $x = x$ & 1 \end{tabular}\caption{Laws.}\label{tab:laws}\end{table}
\begin{remark}\label{rem:r} A remark. \end{remark}
More words, then \cref{rem:r}.
\begin{proof}[Note for readers] Not a proof. \end{proof}
\begin{itemize}\item first
\begin{lemma}\label{lem:inside} Inside a list. \end{lemma}
\item second \end{itemize}
\begin{proof}[Proof of the theorem]\proves{thm:t}
We first show a claim.
\begin{lemma}\label{lem:claim} A claim. \end{lemma}
\begin{proof}\leanok Proof of the claim. \end{proof}
Then the theorem follows, so
\[ a = b \label{eq:ab} \].
\end{proof}
\begin{verbatim}
n % 2 -- kept
\end{verbatim}
\subsection{Deep}
Deep words.
\bibliography{missing}
\end{document}
"""


def test_round_two_pages(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "web.tex").write_text(ROUND_TWO)
    blueprint = leanblueprint.read(tmp_path / "src", "web.tex")
    assert blueprint.problems == ["web.tex:30: \\bibliography{missing} names no file"]
    nodes = {node.id: node for node in blueprint.nodes}
    # A lemma stated inside a proof keeps its own proof; the outer text points to it.
    assert nodes["lem:claim"].proof.leanok and "Proof of the claim" in nodes["lem:claim"].proof.body
    assert "(\\cref{lem:claim})" in nodes["thm:t"].proof.body and "A claim" not in nodes["thm:t"].proof.body
    built = blueprints.chapter(project(tmp_path), blueprint, {})
    assign_paths(built.root, Path("blueprint/roadmap/demo"))
    blueprints.resolve(built, Path("blueprint"))
    assert "Opening words before any chapter." in built.root.prose
    main = built.root.entries[0].node
    assert [entry.node.title for entry in main.entries] == ["t", "inside", "claim"]
    text = main.entries[1].before
    assert "as Table 1 and Table 1 list." in text
    assert "| law | order |\n| --- | --- |\n| $x = x$ | 1 |\n\n**Table 1.** Laws." in text
    assert "**Remark.** A remark.\n\nMore words, then Remark r.\n\n*Note for readers.* Not a proof." in text
    assert text.endswith("- first")  # the list goes on after the lemma that interrupts it
    after = main.entries[2].before
    assert after.startswith("- second\n\n*Proof of the theorem: shown with [Theorem t](thm-t.md).*")
    assert main.tail.startswith("```\nn % 2 -- kept\n```\n\n## Deep\n\nDeep words.")
    theorem = built.targets["thm:t"]
    proof = dict(theorem.notes)["Proof"]
    assert proof.startswith("*Proof of the theorem.* We first show a claim. ([Lemma claim](lem-claim.md))")
    assert "a = b.\\qquad\\text{(1)}" in proof  # punctuation before the number


def test_bibliography_labels(tmp_path):
    bib = tmp_path / "refs.bib"
    bib.write_text(
        "@article{a1, author = {Mazur, B.}, year = 1977, title = {One}}\n"
        "@article{a2, author = {Mazur, B.}, year = 1977, title = {Two}}\n"
        "@article{b, author = {Charles de la Vall{\\'e}e Poussin and Ann Smith and others}, year = 1896}\n"
    )
    from trough import bibtex
    assert bibtex.bibliography([bib], ["a2", "b"]) == {"a2": ("Mazur 1977", None), "b": ("de la Vallée Poussin et al. 1896", None)}
    assert bibtex.bibliography([bib], ["a2", "a1"])["a1"] == ("Mazur 1977b", None)


def test_round_three_text():
    w = writer()
    # Brackets stay as typed unless they would close a link: an escaped \[ opening a
    # paragraph that ends in \] reads as display math.
    assert w.statement("[Note: true for $L$-functions.]") == "[Note: true for $L$-functions.]"
    assert w.statement("[a](b), [c][d] and [e]: f") == r"[a\](b), [c\][d] and [e\]: f"
    assert w.statement(r"\url{https://a.org/$\sim$jrh/x.html}") == "<https://a.org/~jrh/x.html>"
    numbered = tex.Writer({}, tag={"e": "1", "f": "2"}.get)
    assert numbered.statement(r"Thus \begin{align} a&=b \label{e}\\ c&=d\label{f} \end{align}, next.") == (
        "Thus\n\n$$\n\\begin{aligned} a&=b\\qquad\\text{(1)}\\\\ c&=d,\\qquad\\text{(2)}\\end{aligned}\n$$\n\nnext."
    )
    figure = tex.Writer({}, tag={"fig:a": "Figure 1"}.get)
    assert figure.statement(r"\begin{figure}\caption{A pic.\label{fig:a}}\end{figure}").startswith("**Figure 1.** A pic.")
    listing = tex.Writer({"op": tex.Macro(body="\\diamond")})
    assert "```\nx \\op y\n```" in listing.statement("\\begin{verbatim}\nx \\op y\n\\end{verbatim}")
    # The second half of a list that a lemma cut in two keeps the rest of the item it was in.
    assert w.statement(r"\begin{enumerate} which is useful. \item Last.\end{enumerate} After.") == (
        "which is useful.\n\n1. Last.\n\nAfter."
    )
    assert tex.unlinked(r"[$\zeta$ has no\_zeros](trough:x) and no\_such") == r"$\zeta$ has no_zeros and no_such"


ROUND_THREE = r"""
\documentclass{report}
\newtheorem{lemma}{Lemma}
\newtheorem{theorem}{Theorem}
\newtheorem{remark}{Remark}
\begin{document}
\chapter{S \cite{knuth}}
\begin{lemma}\label{a} A. \end{lemma}
\begin{proof} Outer. \begin{proof} Inner. \begin{lemma}\label{c} Claim C. \end{lemma} done. \end{proof} \end{proof}
\begin{theorem}[Knuth \cite{knuth}]\label{thm:t}\uses{a} The theorem.
\begin{proof} By a claim. \begin{lemma}\label{lem:d}\uses{c} A claim. \end{lemma} \end{proof}
\end{theorem}
\begin{lemma}\label{e} E. \begin{remark} Remark R. \end{remark} \end{lemma}
\begin{proof} P. \end{proof}
\begin{theorem} $R$ is Church-Rosser iff it is confluent. \begin{enumerate}\item one \item two \end{enumerate} \end{theorem}
\bibliography{refs}
\end{document}
"""


def test_round_three_pages(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "web.tex").write_text(ROUND_THREE)
    (tmp_path / "src" / "refs.bib").write_text("@book{knuth, author = {Knuth, Donald E.}, title = {Art}, year = 1968}\n")
    blueprint = leanblueprint.read(tmp_path / "src", "web.tex")
    nodes = {node.id: node for node in blueprint.nodes}
    # A lemma inside a proof is its own node, whether the proof is nested in a proof or in a statement.
    assert {"a", "c", "thm:t", "lem:d", "e"} <= set(nodes) and len(blueprint.graph) == 6
    assert nodes["a"].labels == ["a"] and "(\\cref{c})" in nodes["a"].proof.body
    assert nodes["thm:t"].labels == ["thm:t"] and nodes["thm:t"].uses == ["a"]
    built, leaves = build(blueprint, tmp_path)
    page = built.root.entries[0].node
    assert page.title == "S (Knuth 1968)" and "Knuth (Knuth 1968)" in leaves  # a citation in a title
    assert "Theorem: $R$ is Church-Rosser iff it is confluent." in leaves  # no … after a full stop
    text = " ".join([page.prose, page.tail, *(entry.before for entry in page.entries)])
    assert "Remark R." in text and "shown with its statement" not in text  # the remark is inside lemma e
