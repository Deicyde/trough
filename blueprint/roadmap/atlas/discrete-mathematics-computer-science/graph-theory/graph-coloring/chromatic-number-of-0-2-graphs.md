---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ThreeChromaticZeroTwoGraphWanted.IsZeroTwo, MathlibExt.Combinatorics.ThreeChromaticZeroTwoGraphWanted.conjecture, MathlibExt.Combinatorics.ThreeChromaticZeroTwoGraphWanted.conjecture_refuted
statement: formalized
---

# Chromatic number of (0,2)-graphs

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-0-2-graphs/index.html).

## $(0,2)$-graphs

For a natural number $n$, a simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ is a $(0,2)$-graph when every two distinct vertices of $G$ have either
exactly zero or exactly two common neighbors.

Formalized by `MathlibExt.Combinatorics.ThreeChromaticZeroTwoGraphWanted.IsZeroTwo`, a definition declared in [WantedExt/Combinatorics/ThreeChromaticZeroTwoGraphWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ThreeChromaticZeroTwoGraphWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-0-2-graphs/index.html#is-zero-two).

## The three-chromatic $(0,2)$-graph conjecture

It asserts that there are a natural number
$n$ and a simple graph $G$ on the vertex set $\{0, \dots, n-1\}$ in which every two distinct
vertices have either zero or two common neighbors, such that the chromatic number of $G$ is $3$.

Formalized by `MathlibExt.Combinatorics.ThreeChromaticZeroTwoGraphWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ThreeChromaticZeroTwoGraphWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ThreeChromaticZeroTwoGraphWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-0-2-graphs/index.html#conjecture).

## No finite $(0,2)$-graph has chromatic number three

For every natural number $n$ and
every simple graph $G$ on the vertex set $\{0, \dots, n-1\}$ in which every two distinct vertices
have either zero or two common neighbors, the chromatic number of $G$ is not $3$. In particular,
the three-chromatic $(0,2)$-graph conjecture is false.

Williamson proves the stronger statement that every finite three-colourable $(0,2)$-graph is
bipartite (Theorem 2 of the source below).

## Sources

- Christopher Williamson, Finite Three-Colourable (0,2)-Graphs Are Bipartite, arXiv preprint (2026), arXiv:2607.10125, https://arxiv.org/abs/2607.10125.

Stated but not proved: `MathlibExt.Combinatorics.ThreeChromaticZeroTwoGraphWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ThreeChromaticZeroTwoGraphWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ThreeChromaticZeroTwoGraphWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-0-2-graphs/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chromatic number of (0,2)-graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-0-2-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-0-2-graphs)
