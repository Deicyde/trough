---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.IsMonochromaticCliquePacking, MathlibExt.Combinatorics.MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.leftoverValue, MathlibExt.Combinatorics.MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.monochromaticCliquePartitionLeftover, MathlibExt.Combinatorics.MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.monochromaticCliquePartitionLeftover_holds
statement: formalized
---

# Monochromatic clique packings

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/monochromatic-clique-packings/index.html).

## Monochromatic clique packings

Let $n$ and $k$ be natural numbers, and view a simple
graph $G$ on the vertex set $\{0, 1, \dots, n - 1\}$ as a two-colouring of the edges of the
complete graph $K_n$: the edges of $G$ are red and the edges of its complement $G^c$ are blue.
A finite family $P$ of sets of vertices is a monochromatic $k$-clique packing for $G$ when the
sets in $P$ are pairwise disjoint and each of them is a $k$-clique of $G$ or a $k$-clique of
$G^c$, that is, a set of exactly $k$ vertices spanning a monochromatic copy of $K_k$.

Formalized by `MathlibExt.Combinatorics.MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.IsMonochromaticCliquePacking`, a definition declared in [WantedExt/Combinatorics/MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/monochromatic-clique-packings/index.html#is-monochromatic-clique-packing).

## Burr–Erdős–Spencer leftover value

For natural numbers $k$ and $n$, let $r = R(k, k - 1)$
be the classical two-colour Ramsey number. The leftover value is
$r - 1 + \big((n + 1 - r) \bmod k\big)$, where subtraction is truncated at $0$ (in particular
$n + 1 - r$ is read as $0$ when $n + 1 \le r$) and $a \bmod 0 = a$.

For $k \ge 2$ and large $n$, Burr, Erdős and Spencer showed that this is the least number of
vertices that vertex-disjoint monochromatic copies of $K_k$ can be guaranteed to leave uncovered
in every two-colouring of the edges of $K_n$.

Formalized by `MathlibExt.Combinatorics.MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.leftoverValue`, a definition declared in [WantedExt/Combinatorics/MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/monochromatic-clique-packings/index.html#leftover-value).

## Erdős Problem 1015 in the Burr–Erdős–Spencer form

This is the statement that for every
natural number $k \ge 2$ there is $n_0$ such that for every $n \ge n_0$ the following holds. Let
$r = R(k, k - 1)$ be the classical two-colour Ramsey number and let
$L = r - 1 + \big((n + 1 - r) \bmod k\big)$, where $n + 1 - r$ is read as $0$ if it is negative.
View a simple graph $G$ on $n$ vertices as a two-colouring of the edges of $K_n$, with the edges
of $G$ red and those of its complement $G^c$ blue. Then every such colouring admits a
monochromatic $k$-clique packing, that is, a finite family of pairwise disjoint sets of vertices,
each a $k$-clique of $G$ or of $G^c$, leaving at most $L$ vertices uncovered; and some colouring
admits no such packing leaving fewer than $L$ vertices uncovered. In other words, for these $n$
the least number $f(n, k)$ such that every two-colouring of $K_n$ admits such a packing leaving at
most $f(n, k)$ vertices uncovered equals $L$.

Formalized by `MathlibExt.Combinatorics.MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.monochromaticCliquePartitionLeftover`, a definition declared in [WantedExt/Combinatorics/MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/monochromatic-clique-packings/index.html#monochromatic-clique-partition-leftover).

## Burr–Erdős–Spencer theorem on monochromatic clique packings

For every natural number
$k \ge 2$ there is $n_0$ such that for every $n \ge n_0$ the following holds. Let
$r = R(k, k - 1)$ be the classical two-colour Ramsey number and let
$L = r - 1 + \big((n + 1 - r) \bmod k\big)$, where $n + 1 - r$ is read as $0$ if it is negative.
View a simple graph $G$ on $n$ vertices as a two-colouring of the edges of $K_n$, with the edges
of $G$ red and those of its complement $G^c$ blue. Then every such colouring admits a finite
family of pairwise disjoint sets of vertices, each a $k$-clique of $G$ or of $G^c$, that leaves at
most $L$ vertices uncovered; and some colouring admits no such family leaving fewer than $L$
vertices uncovered.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1015, https://www.erdosproblems.com/1015 (status SOLVED); resolution: S. A. Burr, P. Erdős and J. H. Spencer, Ramsey theorems for multiple copies of graphs, Trans. Amer. Math. Soc. 209 (1975), 87-99, §5, Theorem 6: if k is given, then for sufficiently large n, f(n, k) = r(k, k - 1) - 1 + rem(n - r(k, k - 1) + 1, k), where f(n, k) is the minimal integer such that any two-coloring of K_n admits vertex-disjoint monochromatic K_k with at most f(n, k) points left over; erdosproblems.com/1015 lists the problem as solved citing this paper, https://users.renyi.hu/~p_erdos/1975-35.pdf.

Stated but not proved: `MathlibExt.Combinatorics.MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.monochromaticCliquePartitionLeftover_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticCliquePartitionLeftoverErdosProblem1015Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/monochromatic-clique-packings/index.html#monochromatic-clique-partition-leftover-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic clique packings](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/monochromatic-clique-packings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-ramsey-theory/monochromatic-clique-packings)
