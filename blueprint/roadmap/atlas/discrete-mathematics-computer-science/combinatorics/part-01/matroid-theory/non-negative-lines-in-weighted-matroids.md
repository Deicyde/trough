---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.IsSimpleMatroid, MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.IsLine, MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.weight, MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.nonnegGraph, MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.conjecture, MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.conjecture_holds
statement: formalized
---

# Non-negative lines in weighted matroids

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids/index.html).

## Simple matroid

A matroid $M$ on elements of $\{0, \dots, n-1\}$ is simple when the set
$\{e, f\}$ is independent in $M$ for all $e, f \in \{0, \dots, n-1\}$, so that every set of at most
two of these elements is independent (no loops, no parallel pairs).

Formalized by `MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.IsSimpleMatroid`, a definition declared in [WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids/index.html#is-simple-matroid).

## Line of a matroid

A set $L$ of points is a line of a matroid $M$ on elements of
$\{0, \dots, n-1\}$ when $L$ is a flat of $M$ of rank $2$.

Formalized by `MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.IsLine`, a definition declared in [WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids/index.html#is-line).

## Weight of a set of points

Given real weights $a_0, \dots, a_{n-1}$ on the points
$0, \dots, n-1$, the weight of a set $S$ of points is $\sum_{i \in S} a_i$.

Formalized by `MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.weight`, a definition declared in [WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids/index.html#weight).

## Graph of non-negative lines

Let $M$ be a matroid on elements of $\{0, \dots, n-1\}$ and
let $a_0, \dots, a_{n-1}$ be real weights, the weight of a set of points being the sum of the
weights of its points. The graph of non-negative lines has as vertices the points $i$ with
$a_i \ge 0$, and two distinct vertices are adjacent when some line of $M$ (a flat of rank $2$)
contains both and has non-negative weight.

Formalized by `MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.nonnegGraph`, a definition declared in [WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids/index.html#nonneg-graph).

## Connectivity question for weighted rank-3 matroids

This is the statement that for every
$n$, every simple matroid $M$ of rank $3$ on the ground set $\{0, \dots, n-1\}$ (every set of at
most two points is independent) and all real weights $a_0, \dots, a_{n-1}$ with
$a_0 + \dots + a_{n-1} \ge 0$, the graph on the points $i$ with $a_i \ge 0$, in which two distinct
points are adjacent when some line of $M$ (a flat of rank $2$) contains both and has non-negative
weight, the weight of a set being the sum of the weights of its points, is connected.

Formalized by `MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids/index.html#conjecture).

## Non-negative points of a weighted rank-3 matroid are connected by non-negative lines

Let $n$
be a natural number, let $M$ be a simple matroid of rank $3$ on the ground set $\{0, \dots, n-1\}$
(every set of at most two points is independent) and let $a_0, \dots, a_{n-1}$ be real weights
with $a_0 + \dots + a_{n-1} \ge 0$. Then the graph on the points $i$ with $a_i \ge 0$, in which two
distinct points are adjacent when some line of $M$ (a flat of rank $2$) contains both and has
non-negative weight, the weight of a set being the sum of the weights of its points, is
connected.

Resolved true: for a matroid of rank $r$, a generic weight and a threshold $t \le \min\{0, w\}$,
where $w$ is the total weight, the proper flats of weight greater than $t$ form an
$(r - 3)$-connected poset (Adiprasito–Björner, Theorem 2.1, settling the Mikhalkin–Ziegler
conjecture); for $r = 3$, a small generic perturbation with $t$ slightly below $0$ gives the
connectivity of the non-negative points through non-negative lines. Shellability in the omitted
rank-$r$ part is open (their Open Problem 3.2).

## Sources

- K. A. Adiprasito, A. Björner, Filtered geometric lattices and Lefschetz section theorems over the tropical semiring, arXiv:1401.7301, https://arxiv.org/abs/1401.7301.

Stated but not proved: `MathlibExt.Combinatorics.WeightedMatroidNonnegativeLinesConnectedWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeightedMatroidNonnegativeLinesConnectedWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Non-negative lines in weighted matroids](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/matroid-theory/non-negative-lines-in-weighted-matroids)
