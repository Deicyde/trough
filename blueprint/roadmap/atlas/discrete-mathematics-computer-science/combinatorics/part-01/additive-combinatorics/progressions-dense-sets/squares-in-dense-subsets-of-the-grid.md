---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.DenseGridSquareErdosProblem658Wanted.denseGridContainsSquare, MathlibExt.Combinatorics.DenseGridSquareErdosProblem658Wanted.denseGridContainsSquare_holds
statement: formalized
---

# Squares in dense subsets of the grid

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/squares-in-dense-subsets-of-the-grid/index.html).

## Erdős Problem 658 (axis-parallel squares in dense subsets of the grid)

The statement that
for every real number $\delta > 0$ there is a natural number $N_0$ such that for every $N \ge N_0$,
every set $A \subseteq \{1, \dots, N\}^2$ of pairs of natural numbers with $|A| \ge \delta N^2$
contains the four vertices $(a, b)$, $(a + d, b)$, $(a, b + d)$ and $(a + d, b + d)$ of an
axis-parallel square, for some natural numbers $a$, $b$ and $d \ge 1$.

Formalized by `MathlibExt.Combinatorics.DenseGridSquareErdosProblem658Wanted.denseGridContainsSquare`, a definition declared in [WantedExt/Combinatorics/DenseGridSquareErdosProblem658Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DenseGridSquareErdosProblem658Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/squares-in-dense-subsets-of-the-grid/index.html#dense-grid-contains-square).

## Erdős Problem 658 is true

For every real number $\delta > 0$ there is a natural number $N_0$
such that for every $N \ge N_0$, every set $A \subseteq \{1, \dots, N\}^2$ of pairs of natural
numbers with $|A| \ge \delta N^2$ contains the four vertices $(a, b)$, $(a + d, b)$, $(a, b + d)$
and $(a + d, b + d)$ of an axis-parallel square, for some natural numbers $a$, $b$ and $d \ge 1$.

This follows from the density Hales–Jewett theorem of Furstenberg and Katznelson; Solymosi gave a
quantitative proof.

## Sources

- T. F. Bloom, Erdős Problems, Problem #658, https://www.erdosproblems.com/658 (status PROVED (LEAN)); resolution: H. Furstenberg and Y. Katznelson, A density version of the Hales-Jewett theorem, J. Anal. Math. (1991), 64-119, erdosproblems.com/658: the qualitative statement follows from the density Hales-Jewett theorem; a quantitative proof was given by Solymosi (Combin. Probab. Comput. 2004), https://www.erdosproblems.com/658.

Stated but not proved: `MathlibExt.Combinatorics.DenseGridSquareErdosProblem658Wanted.denseGridContainsSquare_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/DenseGridSquareErdosProblem658Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DenseGridSquareErdosProblem658Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/squares-in-dense-subsets-of-the-grid/index.html#dense-grid-contains-square-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Squares in dense subsets of the grid](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/squares-in-dense-subsets-of-the-grid/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/squares-in-dense-subsets-of-the-grid)
