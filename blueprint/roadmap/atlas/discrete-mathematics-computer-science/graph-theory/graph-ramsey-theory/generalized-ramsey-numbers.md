---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.FourCliqueFiveColoursErdosProblem136Wanted.HasFourFiveColouring, MathlibExt.Combinatorics.FourCliqueFiveColoursErdosProblem136Wanted.fourFiveColourNumber, MathlibExt.Combinatorics.FourCliqueFiveColoursErdosProblem136Wanted.fourFiveColourNumberAsymptotic, MathlibExt.Combinatorics.FourCliqueFiveColoursErdosProblem136Wanted.fourFiveColourNumberAsymptotic_holds
statement: formalized
---

# Generalized Ramsey numbers

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/generalized-ramsey-numbers/index.html).

## $(4, 5)$-colourings of $K_n$

For natural numbers $n$ and $k$, the complete graph $K_n$ on
the vertices $0, 1, \dots, n - 1$ has a $(4, 5)$-colouring with $k$ colours if there is a map $c$
assigning to every ordered pair $(x, y)$ of vertices one of $k$ colours, with $c(x, y) = c(y, x)$
for all $x, y$, such that for any four distinct vertices the six edges between them receive at
least five distinct colours.

Formalized by `MathlibExt.Combinatorics.FourCliqueFiveColoursErdosProblem136Wanted.HasFourFiveColouring`, a definition declared in [WantedExt/Combinatorics/FourCliqueFiveColoursErdosProblem136Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FourCliqueFiveColoursErdosProblem136Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/generalized-ramsey-numbers/index.html#has-four-five-colouring).

## The $(4, 5)$-colouring number $f(n)$

For a natural number $n$, $f(n)$ is the least
natural number $k$ such that $K_n$ has a $(4, 5)$-colouring with $k$ colours; such a $k$
always exists.

Formalized by `MathlibExt.Combinatorics.FourCliqueFiveColoursErdosProblem136Wanted.fourFiveColourNumber`, a definition declared in [WantedExt/Combinatorics/FourCliqueFiveColoursErdosProblem136Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FourCliqueFiveColoursErdosProblem136Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/generalized-ramsey-numbers/index.html#four-five-colour-number).

## The asymptotic of the $(4, 5)$-colouring number (Erdős Problem 136)

Let $f(n)$ be the
least number of colours in a $(4, 5)$-colouring of $K_n$. This is the proposition that $f(n)/n$
tends to $5/6$ as $n \to \infty$; equivalently, $f(n) = (5/6 + o(1))\, n$.

Formalized by `MathlibExt.Combinatorics.FourCliqueFiveColoursErdosProblem136Wanted.fourFiveColourNumberAsymptotic`, a definition declared in [WantedExt/Combinatorics/FourCliqueFiveColoursErdosProblem136Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FourCliqueFiveColoursErdosProblem136Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/generalized-ramsey-numbers/index.html#four-five-colour-number-asymptotic).

## Erdős Problem 136: the $(4, 5)$-colouring number of $K_n$ is asymptotically $5n/6$

Let
$f(n)$ be the least number of colours in a $(4, 5)$-colouring of $K_n$, that is, a symmetric
colouring of the pairs of vertices of $K_n$ in which the six edges of every $K_4$ receive at
least five distinct colours. Then $f(n)/n \to 5/6$ as $n \to \infty$.

Erdős and Gyárfás proved $f(n) > 5(n - 1)/6$, and Bennett, Cushman, Dudek and Prałat constructed
$(4, 5)$-colourings of $K_n$ with $5n/6 + o(n)$ colours (Joos and Mubayi gave a shorter proof).

## Sources

- T. F. Bloom, Erdős Problems, Problem #136, https://www.erdosproblems.com/136 (status SOLVED); resolution: P. Bennett, R. Cushman, A. Dudek and P. Prałat, The Erdős-Gyárfás function f(n, 4, 5) = 5n/6 + o(n) - so Gyárfás was right, arXiv:2207.02920 (2022); F. Joos and D. Mubayi, Ramsey theory constructions from hypergraph matchings, arXiv:2208.12563 (2022), abstract: (4, 5)-colourings of K_n with 5n/6 + o(n) colours; with the Erdős-Gyárfás lower bound f(n) > 5(n - 1)/6 this gives f(n) ~ 5n/6 (erdosproblems.com/136), https://arxiv.org/abs/2207.02920.

Stated but not proved: `MathlibExt.Combinatorics.FourCliqueFiveColoursErdosProblem136Wanted.fourFiveColourNumberAsymptotic_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/FourCliqueFiveColoursErdosProblem136Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FourCliqueFiveColoursErdosProblem136Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/generalized-ramsey-numbers/index.html#four-five-colour-number-asymptotic-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Ramsey numbers](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/generalized-ramsey-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-ramsey-theory/generalized-ramsey-numbers)
