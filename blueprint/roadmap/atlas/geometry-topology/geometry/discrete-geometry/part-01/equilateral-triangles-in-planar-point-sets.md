---
declaration: section
origin: cited
lean: MathlibExt.Geometry.ErdosProblem755Wanted.IsEquilateralTriangle, MathlibExt.Geometry.ErdosProblem755Wanted.IsUnitEquilateralTriangle, MathlibExt.Geometry.ErdosProblem755Wanted.IsAnySizeEquilateralTriangle, MathlibExt.Geometry.ErdosProblem755Wanted.unitEquilateralTriangleCount, MathlibExt.Geometry.ErdosProblem755Wanted.anySizeEquilateralTriangleCount, MathlibExt.Geometry.ErdosProblem755Wanted.TUnit, MathlibExt.Geometry.ErdosProblem755Wanted.TAnySize, MathlibExt.Geometry.ErdosProblem755Wanted.conjecture
statement: formalized
---

# Equilateral triangles in planar point sets

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html).

## Equilateral triangle with given side

For a real number $s$, a finite set $T$ of
points in the Euclidean space $\mathbb{R}^d$ is an equilateral triangle of side $s$ when $T$ has
exactly three elements and any two distinct points of $T$ are at distance $s$.

Formalized by `MathlibExt.Geometry.ErdosProblem755Wanted.IsEquilateralTriangle`, a definition declared in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#is-equilateral-triangle).

## Unit equilateral triangle

A finite set $T$ of points in the Euclidean space $\mathbb{R}^d$
is a unit equilateral triangle when it is an equilateral triangle of side $1$: $T$ has exactly
three elements and any two distinct points of $T$ are at distance $1$.

Formalized by `MathlibExt.Geometry.ErdosProblem755Wanted.IsUnitEquilateralTriangle`, a definition declared in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#is-unit-equilateral-triangle).

## Equilateral triangle of any size

A finite set $T$ of points in the Euclidean space
$\mathbb{R}^d$ is an equilateral triangle of any size when there is a real number $s > 0$ such
that $T$ is an equilateral triangle of side $s$: $T$ has exactly three elements and any two
distinct points of $T$ are at distance $s$.

Formalized by `MathlibExt.Geometry.ErdosProblem755Wanted.IsAnySizeEquilateralTriangle`, a definition declared in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#is-any-size-equilateral-triangle).

## Number of unit equilateral triangles in a point set

For a finite set $P$ of points in
the Euclidean space $\mathbb{R}^d$, this is the number of three-element subsets of $P$ that are
unit equilateral triangles, that is, whose three points are pairwise at distance $1$.

Formalized by `MathlibExt.Geometry.ErdosProblem755Wanted.unitEquilateralTriangleCount`, a definition declared in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#unit-equilateral-triangle-count).

## Number of equilateral triangles in a point set

For a finite set $P$ of points in the
Euclidean space $\mathbb{R}^d$, this is the number of three-element subsets of $P$ that are
equilateral triangles of some positive side length $s$, that is, whose three points are pairwise
at distance $s$.

Formalized by `MathlibExt.Geometry.ErdosProblem755Wanted.anySizeEquilateralTriangleCount`, a definition declared in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#any-size-equilateral-triangle-count).

## Maximum number of unit equilateral triangles

For natural numbers $d$ and $n$, $T_1(d, n)$
is the supremum in $\mathbb{N}$, over all sets $P$ of exactly $n$ points in the Euclidean space
$\mathbb{R}^d$, of the number of unit equilateral triangles spanned by $P$ (the three-element
subsets of $P$ whose points are pairwise at distance $1$). When such sets exist this is the
largest such number; when none exist (only for $d = 0$ and $n \ge 2$) it is $0$.

Formalized by `MathlibExt.Geometry.ErdosProblem755Wanted.TUnit`, a definition declared in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#tunit).

## Maximum number of equilateral triangles

For natural numbers $d$ and $n$, $T(d, n)$ is the
supremum in $\mathbb{N}$, over all sets $P$ of exactly $n$ points in the Euclidean space
$\mathbb{R}^d$, of the number of equilateral triangles of positive side length spanned by $P$
(the three-element subsets of $P$ whose points are pairwise at the same positive distance). When
such sets exist this is the largest such number; when none exist (only for $d = 0$ and $n \ge 2$)
it is $0$.

Formalized by `MathlibExt.Geometry.ErdosProblem755Wanted.TAnySize`, a definition declared in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#tany-size).

## Statement of Erdős Problem 755

Let $T_1(n)$ be the largest number of unit equilateral
triangles spanned by a set of $n$ points in $\mathbb{R}^6$, and let $T(n)$ be the largest number
of equilateral triangles of positive side length spanned by a set of $n$ points in
$\mathbb{R}^6$; a triangle spanned by a set is a three-element subset of it whose points are
pairwise at the same distance. The statement asserts both of the following: there is a function
$o : \mathbb{N} \to \mathbb{R}$ with $o(n) \to 0$ as $n \to \infty$ such that
$T_1(n) \le (1/27 + o(n))\, n^3$ for all sufficiently large $n$; and $T(n)$ is asymptotically
equivalent to $n^3/27$ as $n \to \infty$.

Formalized by `MathlibExt.Geometry.ErdosProblem755Wanted.conjecture`, a definition declared in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#conjecture).

## Erdős Problem 755 holds (Clemen–Dumitrescu–Liu)

Let $T_1(n)$ be the largest number of unit
equilateral triangles spanned by a set of $n$ points in $\mathbb{R}^6$, and let $T(n)$ be the
largest number of equilateral triangles of positive side length spanned by a set of $n$ points in
$\mathbb{R}^6$; a triangle spanned by a set is a three-element subset of it whose points are
pairwise at the same distance. Then there is a function $o : \mathbb{N} \to \mathbb{R}$ with
$o(n) \to 0$ as $n \to \infty$ such that $T_1(n) \le (1/27 + o(n))\, n^3$ for all sufficiently
large $n$, and $T(n)$ is asymptotically equivalent to $n^3/27$ as $n \to \infty$.

## Sources

- Felix Christian Clemen, Adrian Dumitrescu, and Dingyuan Liu, The number of regular simplices in higher dimensions, arXiv:2507.19841 (2025), https://arxiv.org/abs/2507.19841. Resolved true: Resolved externally by Clemen, Dumitrescu, and Liu. This repository records the statement, not an internal proof; a separate pinned Lean proof is cited in the registry.

Stated but not proved: `MathlibExt.Geometry.ErdosProblem755Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Geometry/ErdosProblem755Wanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem755Wanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equilateral triangles in planar point sets](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/equilateral-triangles-in-planar-point-sets)
