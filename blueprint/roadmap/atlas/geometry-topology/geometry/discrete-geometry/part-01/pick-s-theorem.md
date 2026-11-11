---
declaration: section
origin: cited
lean: MeasureTheory.toReal_volume_convexHull_lattice_triangle, MetaMathlibExt.pick_convex_lattice_polygon, MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.toPlane, MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.latPoly, MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.inside, MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.area, MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.Adjacent, MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.IsSimple
statement: formalized
---

# Pick's theorem

11 results, 10 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html).

## Pick's theorem for lattice triangles with a vertex at the origin

Let
$u, v \in \mathbb{Z}^2$ with $u_0 v_1 - u_1 v_0 \neq 0$, and let $T \subset \mathbb{R}^2$ be
the convex hull of $0$, $u$ and $v$. Let $I$ be the number of points of $\mathbb{Z}^2$ in the
interior of $T$ and $B$ the number of points of $\mathbb{Z}^2$ on the boundary of $T$. Then
the area (two-dimensional Lebesgue measure) of $T$ equals $I + B/2 - 1$.

Formalized by `MeasureTheory.toReal_volume_convexHull_lattice_triangle`, a theorem declared in [MathlibExt/Geometry/Convex/PickTheorem.lean, line 841](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Convex/PickTheorem.lean#L841). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#to-real-volume-convex-hull-lattice-trian).

## Pick's theorem for convex lattice polygons

Let $V \subset \mathbb{Z}^2$ be a finite
set of lattice points, let $P \subset \mathbb{R}^2$ be the convex hull of $V$, and suppose that
$P$ has nonempty interior. Let $I$ be the number of points of $\mathbb{Z}^2$ in the interior of
$P$ and $B$ the number of points of $\mathbb{Z}^2$ on the boundary of $P$. Then the area
(two-dimensional Lebesgue measure) of $P$ equals $I + B/2 - 1$.

Proof: The triangle case counts lattice points in a half-open fundamental
parallelogram. A crossing diagonal then cuts larger polygons into two smaller
full-dimensional lattice polygons, allowing strong induction on the vertex set.

## Sources

- Eugen J. Ionascu, "A Parametrization of Equilateral Triangles Having Integer Coordinates", Journal of Integer Sequences 10 (2007), Article 07.6.7, standard formula `Area = #b / 2 + #i - 1`, lines 87–100, <https://cs.uwaterloo.ca/journals/JIS/VOL10/Ionascu/ionascu2.tex>; Kevin A. Broughan, "The gcd-sum function", Journal of Integer Sequences 4 (2001), Article 01.2.2, trapezium application, lines 699–715 (the prose there prints "+1" but the paper's own derived formula uses the minus-one form), <https://cs.uwaterloo.ca/journals/JIS/VOL4/BROUGHAN/gcdsum.tex>; Gil Alon and Pete L. Clark, "On the Number of Representations of an Integer by a Linear Form", Journal of Integer Sequences 8 (2005), Article 05.5.2, generalized lattice version `A(P) = δ * (h + b / 2 - 1)`, lines 633–638 (this article is the `δ = 1` standard-lattice case), <https://cs.uwaterloo.ca/journals/JIS/VOL8/Clark/clark80.tex>.

Formalized by `MetaMathlibExt.pick_convex_lattice_polygon`, a theorem declared in [MathlibExt/Geometry/Convex/PickTheorem.lean, line 2017](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Convex/PickTheorem.lean#L2017). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#pick-convex-lattice-polygon).

## Lattice points in the plane

The map $\mathbb{Z}^2 \to \mathbb{R}^2$ sending a lattice
point $(a, b)$ to the point $(a, b)$ of the real plane.

Formalized by `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.toPlane`, a definition declared in [WantedExt/Geometry/PicksTheoremWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#to-plane).

## Lattice polygon

Given integer points $v_0, \dots, v_{n-1} \in \mathbb{Z}^2$, the lattice
polygon on $v$ is the polygon in $\mathbb{R}^2$ with $n$ vertices whose $i$-th vertex is $v_i$,
viewed as a point of $\mathbb{R}^2$.

Formalized by `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.latPoly`, a definition declared in [WantedExt/Geometry/PicksTheoremWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#lat-poly).

## Region enclosed by a planar set

For a set $S \subseteq \mathbb{R}^2$, the region enclosed
by $S$ is the set of points $x \notin S$ whose connected component in the complement
$\mathbb{R}^2 \setminus S$ is bounded. For a simple closed curve $S$ this is the Jordan interior.

Formalized by `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.inside`, a definition declared in [WantedExt/Geometry/PicksTheoremWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#inside).

## Enclosed area

The area enclosed by a set $S \subseteq \mathbb{R}^2$ is the Lebesgue
measure, as a real number, of the region enclosed by $S$ (the points $x \notin S$ whose connected
component in $\mathbb{R}^2 \setminus S$ is bounded); it is taken to be $0$ when that measure is
infinite.

Formalized by `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.area`, a definition declared in [WantedExt/Geometry/PicksTheoremWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#area).

## Cyclically adjacent indices

Two indices $i, j \in \{0, \dots, n-1\}$ are adjacent when
$j \equiv i + 1 \pmod n$ or $i \equiv j + 1 \pmod n$.

Formalized by `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.Adjacent`, a definition declared in [WantedExt/Geometry/PicksTheoremWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#adjacent).

## Simple polygon

A polygon in $\mathbb{R}^2$ with vertices $p_0, \dots, p_{n-1}$ (indices
taken mod $n$) and edges the segments $e_i = [p_i, p_{i+1}]$ is simple when consecutive vertices
are distinct ($p_i \ne p_{i+1}$ for all $i$), any two edges $e_i$ and $e_j$ with $i \ne j$,
$j \not\equiv i + 1$ and $i \not\equiv j + 1 \pmod n$ are disjoint, and every two consecutive
edges meet only in their common vertex: $e_i \cap e_{i+1} = \{p_{i+1}\}$ for all $i$.

Formalized by `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.IsSimple`, a definition declared in [WantedExt/Geometry/PicksTheoremWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#is-simple).

## Number of boundary lattice points

For integer points
$v_0, \dots, v_{n-1} \in \mathbb{Z}^2$, the number of lattice points $z \in \mathbb{Z}^2$ that lie
on the boundary (the union of the edges) of the lattice polygon on $v$.

Formalized by `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.boundaryPts`, a definition declared in [WantedExt/Geometry/PicksTheoremWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#boundary-pts).

## Number of interior lattice points

For integer points
$v_0, \dots, v_{n-1} \in \mathbb{Z}^2$, the number of lattice points $z \in \mathbb{Z}^2$ that lie
in the region enclosed by the boundary of the lattice polygon on $v$, that is, the points off the
boundary whose connected component in its complement is bounded.

Formalized by `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.interiorPts`, a definition declared in [WantedExt/Geometry/PicksTheoremWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#interior-pts).

## Pick's theorem

Let $n \ge 3$ and let $v_0, \dots, v_{n-1} \in \mathbb{Z}^2$ be integer
points such that the lattice polygon $P$ in $\mathbb{R}^2$ with vertices $v_0, \dots, v_{n-1}$ is
simple. Then the area of the region enclosed by the boundary of $P$ equals $I + B/2 - 1$, where
$I$ is the number of lattice points in that region and $B$ is the number of lattice points on the
boundary of $P$.

## Sources

- G. Pick, *Geometrisches zur Zahlenlehre* (1899). Knill, *Some fundamental theorems in mathematics*, §154. Problem `pick` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.PicksTheoremWanted.Geometry.PicksTheorem.pick` is written with `theorem_wanted` in [WantedExt/Geometry/PicksTheoremWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PicksTheoremWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html#pick).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pick's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/pick-s-theorem)
