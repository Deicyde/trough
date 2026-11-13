---
declaration: section
origin: cited
lean: Set.Triplewise, EuclideanGeometry.NonTrilinear, EuclideanGeometry.NonCollinearFor, EuclideanGeometry.HasConvexNGon, EuclideanGeometry.IsCcwConvexPolygon, EuclideanGeometry.IsConvexPolygon, EuclideanGeometry.isConvexPolygon_three_of_affineIndependent, EuclideanGeometry.orientedTriangleArea
statement: formalized
---

# Convex and general position of point sets

22 results, 21 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html).

## Relation holding triplewise on a set

Let $r$ be a ternary relation on a type $\alpha$ and let
$s \subseteq \alpha$. The relation $r$ holds triplewise on $s$ if $r(x, y, z)$ holds for all
pairwise distinct $x, y, z \in s$.

Formalized by `Set.Triplewise`, a definition declared in [MathlibExt/Data/Set/Triplewise.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Set/Triplewise.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#triplewise).

## Sets with no three collinear points

A set $A$ of points in the plane is non-trilinear
if no three distinct points of $A$ lie on a common line.

Formalized by `EuclideanGeometry.NonTrilinear`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#non-trilinear).

## Sets with no $n$ collinear points

A set $S$ of points in a Euclidean affine space has no
$n$ collinear points if no subset of $S$ consisting of exactly $n$ points is collinear.

Formalized by `EuclideanGeometry.NonCollinearFor`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#non-collinear-for).

## Sets containing a convex $n$-gon

A set $P \subseteq \mathbb{R}^2$ contains a convex
$n$-gon if there is a set $S \subseteq P$ of exactly $n$ points that is convex independent: no
point of $S$ lies in the convex hull of the other points of $S$.

Formalized by `EuclideanGeometry.HasConvexNGon`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#has-convex-ngon).

## Counterclockwise convex polygons

Let $P$ be an oriented two-dimensional Euclidean affine
space. Points $p_0, \dots, p_{n-1} \in P$ form a counterclockwise convex polygon if for all
indices $i < j < k$ the oriented angle $\measuredangle p_i p_j p_k$ at $p_j$ has sign $-1$, that
is, $p_i, p_j, p_k$ are not collinear and lie in counterclockwise order with respect to the
orientation of $P$. Every list of at most two points qualifies.

Formalized by `EuclideanGeometry.IsCcwConvexPolygon`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-ccw-convex-polygon).

## Convex polygons

Points $p_0, \dots, p_{n-1}$ of an oriented two-dimensional Euclidean
affine space form a convex polygon if one of the lists $p_0, p_1, \dots, p_{n-1}$ and
$p_0, p_{n-1}, p_{n-2}, \dots, p_1$ is a counterclockwise convex polygon: for any three of its
entries $q, r, s$, in the order in which they occur in that list, the oriented angle
$\measuredangle q r s$ at $r$ has sign $-1$. Thus for $n \ge 3$ the points are the vertices of a
strictly convex polygon, listed counterclockwise or clockwise starting from $p_0$; every list of
at most two points qualifies.

Formalized by `EuclideanGeometry.IsConvexPolygon`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-convex-polygon).

## Affinely independent triples are convex polygons

If three points $A, B, C$ of an oriented
two-dimensional Euclidean affine space are affinely independent, then $A, B, C$ form a convex
polygon.

Formalized by `EuclideanGeometry.isConvexPolygon_three_of_affineIndependent`, a theorem declared in [MathlibExt/Geometry/TwoD.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-convex-polygon-three-of-affine-indepe).

## Oriented triangle area

Let $\omega$ be the area form of the given orientation of the
Euclidean plane, so that $\omega(u, v)$ is the signed area of the parallelogram spanned by the
vectors $u$ and $v$. For points $a$, $b$, $c$ of the plane, the oriented area of the triangle
with vertices $a$, $b$, $c$ is the real number $\omega(a - c, b - c) / 2$.

It changes sign when two vertices are swapped, and it is positive when $a$, $b$, $c$ are in
counterclockwise order and negative when they are in clockwise order.

Formalized by `EuclideanGeometry.orientedTriangleArea`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#oriented-triangle-area).

## Maximum number of distinct distance counts

For a finite set $X \subseteq \mathbb{R}^2$
and a point $x \in X$, let $R_X(x)$ be the number of distinct distances $\lvert y - x \rvert$
from $x$ to the points $y \in X$ other than $x$. For $n \in \mathbb{N}$, $g(n)$ is the maximum,
over all sets $X \subseteq \mathbb{R}^2$ of exactly $n$ points, of the number of distinct values
among the numbers $R_X(x)$ with $x \in X$.

Formalized by `EuclideanGeometry.maximalDistinctDistancesFrom`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#maximal-distinct-distances-from).

## Points in general position

A set $X \subseteq \mathbb{R}^2$, finite or infinite, is in
_general position_ if no three distinct points of $X$ are collinear and no four distinct points
of $X$ lie on a common circle.

Formalized by `EuclideanGeometry.InGeneralPosition`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#in-general-position).

## Right-angled triangles

Points $a, b, c$ of a Euclidean affine space are the vertices of a
right-angled triangle if they are pairwise distinct and the unoriented angle at one of the three
vertices equals $\pi / 2$: $\angle bac = \pi / 2$, $\angle abc = \pi / 2$ or
$\angle bca = \pi / 2$.

The distinctness hypothesis rules out degenerate triples, whose angles can coincide with
$\pi / 2$.

Formalized by `EuclideanGeometry.IsRightAngled`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-right-angled).

## Isosceles trapezoids

Points $a, b, c, d \in \mathbb{R}^2$ are the vertices, in
counterclockwise order, of an isosceles trapezoid if they are in strictly convex position and
listed counterclockwise (for any three of them $p, q, r$, in the order in which they occur in the
list $a, b, c, d$, the oriented angle $\measuredangle p q r$ at $q$ has sign $-1$), the line
through $a$ and $b$ is parallel to the line through $c$ and $d$ (the two bases), and the
diagonals have equal length: $\operatorname{dist}(a, c) = \operatorname{dist}(b, d)$.

One pair of parallel sides together with equal diagonals is the classical characterization of an
isosceles trapezoid; in particular it rules out non-rectangular parallelograms.

Formalized by `EuclideanGeometry.IsIsoscelesTrapezoid`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-isosceles-trapezoid).

## Isosceles-free sets

A set $A$ in a space with a distance function $d$ is isosceles-free if
there are no three distinct points $x, y, z \in A$ such that two of the distances $d(x, y)$,
$d(y, z)$, $d(z, x)$ are equal.

Formalized by `Set.IsIsoscelesFree`, a definition declared in [MathlibExt/Geometry/TwoD.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/TwoD.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-isosceles-free).

## General position of affine points

Let $k$ be a division ring and $P$ an affine space over
$k$. A family $(p_i)_{i \in \iota}$ of points of $P$ is in general position through dimension
$d \in \mathbb{N}$ if for every finite set $S \subseteq \iota$ of at most $d + 1$ indices, the
subfamily $(p_i)_{i \in S}$ is affinely independent over $k$.

Formalized by `IsGeneralPosition`, a definition declared in [MathlibExt/LinearAlgebra/GeneralPosition.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/GeneralPosition.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-general-position).

## Affinely independent families are in general position

If a family $(p_i)_{i \in \iota}$ of
points of an affine space over a division ring $k$ is affinely independent over $k$, then it is in
general position through dimension $d$ for every $d \in \mathbb{N}$.

Formalized by `AffineIndependent.isGeneralPosition`, a theorem declared in [MathlibExt/LinearAlgebra/GeneralPosition.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/GeneralPosition.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-general-position-2).

## General position in affine space is monotone in the dimension

Let $d \le e$ be natural
numbers. If a family of points of an affine space over a division ring $k$ is in general position
through dimension $e$, then it is in general position through dimension $d$.

Formalized by `IsGeneralPosition.mono`, a theorem declared in [MathlibExt/LinearAlgebra/GeneralPosition.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/GeneralPosition.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#mono).

## General position of projective points

Let $k$ be a division ring and $V$ a vector space
over $k$, with projective space $\mathbb{P}(V)$. A family $(p_i)_{i \in \iota}$ of points of
$\mathbb{P}(V)$ is in general position through dimension $d \in \mathbb{N}$ if for every finite set
$S \subseteq \iota$ of at most $d + 1$ indices, the subfamily $(p_i)_{i \in S}$ is projectively
independent.

Formalized by `Projectivization.IsGeneralPosition`, a definition declared in [MathlibExt/LinearAlgebra/GeneralPosition.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/GeneralPosition.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-general-position-3).

## Projectively independent families are in general position

If a family
$(p_i)_{i \in \iota}$ of points of the projective space $\mathbb{P}(V)$ of a vector space $V$ over a
division ring $k$ is projectively independent, then it is in general position through dimension $d$
for every $d \in \mathbb{N}$.

Formalized by `Projectivization.Independent.isGeneralPosition`, a theorem declared in [MathlibExt/LinearAlgebra/GeneralPosition.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/GeneralPosition.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#is-general-position-4).

## General position in projective space is monotone in the dimension

Let $d \le e$ be
natural numbers. If a family of points of the projective space $\mathbb{P}(V)$ of a vector space
$V$ over a division ring $k$ is in general position through dimension $e$, then it is in general
position through dimension $d$.

Formalized by `Projectivization.IsGeneralPosition.mono`, a theorem declared in [MathlibExt/LinearAlgebra/GeneralPosition.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/GeneralPosition.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#mono-2).

## Convex position threshold

For natural numbers $k$ and $n$, $f_k(n)$ is the least natural
number $m$ such that every set of $m$ points of $\mathbb{R}^k$ in general position (any at most
$k + 1$ of them affinely independent) contains $n$ points in convex position (none of them in the
convex hull of the others). If there is no such $m$, then $f_k(n) = 0$.

For $k \ge 2$ such an $m$ exists by the Erdős-Szekeres theorem.

Formalized by `MathlibExt.Combinatorics.ConvexPositionHigherDimensionsErdosProblem651Wanted.convexPositionThreshold`, a definition declared in [WantedExt/Combinatorics/ConvexPositionHigherDimensionsErdosProblem651Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ConvexPositionHigherDimensionsErdosProblem651Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#convex-position-threshold).

## Erdős Problem 651: exponential growth of convex position thresholds

For natural numbers
$k$ and $n$ let $f_k(n)$ be the least $m$ such that every set of $m$ points of $\mathbb{R}^k$ in
general position (any at most $k + 1$ of them affinely independent) contains $n$ points in convex
position (none of them in the convex hull of the others), with $f_k(n) = 0$ if there is no such
$m$. The claim is that for every $k \ge 2$ there is a real $c > 0$ with $(1 + c)^n < f_k(n)$ for
all sufficiently large $n$.

Erdős asked for a constant $c_k > 0$ with $f_k(n) > (1 + c_k)^n$; requiring this only for all
large $n$ makes the claim weaker and its refutation stronger.

Formalized by `MathlibExt.Combinatorics.ConvexPositionHigherDimensionsErdosProblem651Wanted.convexPositionThresholdExponential`, a definition declared in [WantedExt/Combinatorics/ConvexPositionHigherDimensionsErdosProblem651Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ConvexPositionHigherDimensionsErdosProblem651Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#convex-position-threshold-exponential).

## Erdős Problem 651 has a negative answer

For natural numbers $k$ and $n$ let $f_k(n)$ be the
least $m$ such that every set of $m$ points of $\mathbb{R}^k$ in general position (any at most
$k + 1$ of them affinely independent) contains $n$ points in convex position (none of them in the
convex hull of the others), with $f_k(n) = 0$ if there is no such $m$. It is not the case that for
every $k \ge 2$ there is a real $c > 0$ with $(1 + c)^n < f_k(n)$ for all sufficiently large $n$.

Pohoata and Zakharov proved $f_d(n) = 2^{o(n)}$ for every $d \ge 3$, so for $k = 3$ and every
$c > 0$ the bound $f_3(n) \le (1 + c)^n$ holds for all large $n$; erdosproblems.com/651 lists the
problem as disproved.

## Sources

- T. F. Bloom, Erdős Problems, Problem #651, https://www.erdosproblems.com/651 (status DISPROVED (LEAN)); resolution: C. Pohoata and D. Zakharov, Convex polytopes from fewer points, arXiv:2208.04878 (2022), abstract: ES_d(n) = 2^{o(n)} for all d ≥ 3, ES_d(n) being the least number such that any ES_d(n) points in general position in ℝ^d contain n points in convex position; erdosproblems.com/651: the answer is no, even for k = 3, https://arxiv.org/abs/2208.04878.

Stated but not proved: `MathlibExt.Combinatorics.ConvexPositionHigherDimensionsErdosProblem651Wanted.convexPositionThresholdExponential_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ConvexPositionHigherDimensionsErdosProblem651Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ConvexPositionHigherDimensionsErdosProblem651Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html#convex-position-threshold-exponential-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convex and general position of point sets](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/discrete-geometry/part-01/convex-and-general-position-of-point-sets)
