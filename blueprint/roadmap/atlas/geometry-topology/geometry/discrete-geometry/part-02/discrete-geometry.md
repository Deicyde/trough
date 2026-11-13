---
declaration: section
origin: cited
lean: Submodule.discrete_full_rank_iff_isZLattice, MetaMathlibExt.erdos_anning, MetaMathlibExt.euler_polyhedron_formula, MetaMathlibExt.monsky_theorem, MathlibExt.Geometry.ScottishBook59Wanted.squaringTheSquareDistinctSquares, MathlibExt.Geometry.Euclidean.SylvesterGallaiWanted.sylvester_gallai
statement: formalized
---

# Discrete geometry: its own results

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/index.html).

Finite point configurations and their distances, polytopes and polyhedra, dissections and tilings, lattice points and extremal shape problems.

## A discrete subgroup is a lattice iff it has full rank

Let $E$ be a finite-dimensional
real normed space and let $L \subseteq E$ be a $\mathbb{Z}$-submodule (an additive subgroup) that
is discrete in the subspace topology. Then the $\mathbb{Z}$-rank of $L$ equals $\dim_{\mathbb{R}} E$
if and only if $L$ is a $\mathbb{Z}$-lattice in $E$, that is, $L$ spans $E$ over $\mathbb{R}$.

## Sources

- ATLAS `NumberTheoryI`, Lemma 14.3 (full-rank clause only).

Formalized by `Submodule.discrete_full_rank_iff_isZLattice`, a theorem declared in [MathlibExt/Geometry/DiscreteFullRankZLattice.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/DiscreteFullRankZLattice.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/index.html#discrete-full-rank-iff-is-zlattice).

## Erdős–Anning theorem

An infinite set of points in the plane with pairwise
integer distances is collinear.

## Sources

- N. H. Anning and P. Erdős, "Integral distances," Bull. Amer. Math. Soc. 51 (1945), 598–600; P. Erdős, "Integral distances," Bull. Amer. Math. Soc. 51 (1945), 996. Overview: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Anning_theorem

Formalized by `MetaMathlibExt.erdos_anning`, a theorem declared in [MathlibExt/Geometry/Euclidean/ErdosAnning.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/ErdosAnning.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/index.html#erdos-anning).

## Euler's polyhedron formula

Let $V$, $E$ and $F$ be finite sets, let
$\iota : V \to \mathbb{R}^3$ be an injective map into Euclidean space, and let
$P = \operatorname{conv} \iota(V)$ be the convex hull of its image; assume $P$ has nonempty
interior $\operatorname{int} P$, and write $\partial P$ for its frontier. Each edge $e \in E$ has an
ordered pair of endpoints $(s(e), t(e)) \in V \times V$, with segment
$[e] = [\iota(s(e)), \iota(t(e))]$; each face $f \in F$ has a finite vertex set $V_f \subseteq V$,
with cell $C_f = \operatorname{conv} \iota(V_f)$. Say that the segment between vertices
$u, w \in V$ lies in the face $f$ when $u, w \in V_f$ and $[\iota(u), \iota(w)] \subseteq C_f$, and
that it lies in exactly two faces when it lies in two distinct faces $f_1, f_2$ and every face it
lies in is $f_1$ or $f_2$. Assume the following. For every edge $e$: $[e] \subseteq P$;
$s(e) \ne t(e)$; if $\iota(v) \in [e]$ for a vertex $v$, then $v = s(e)$ or $v = t(e)$; and the
segment between $s(e)$ and $t(e)$ lies in exactly two faces. Distinct edges $e_1, e_2$ never have
the same endpoints, in the same or in the reverse order, and every common point of $[e_1]$ and
$[e_2]$ is $\iota(v)$ for a vertex $v$ that is an endpoint of both. Every vertex is an endpoint of
some edge. For every face $f$: $C_f \subseteq P$; $V_f$ has at least $3$ elements;
$C_f \cap \operatorname{int} P = \emptyset$; the affine span of $C_f$ has dimension $2$; and every
$v \in V_f$ is an endpoint of two distinct edges whose segments are contained in $C_f$. For
distinct faces $f_1, f_2$, $V_{f_1} \not\subseteq V_{f_2}$, and every point of
$C_{f_1} \cap C_{f_2}$ is $\iota(v)$ for some vertex $v$ or lies on $[e]$ for some edge $e$. The
cells cover the frontier: $\partial P \subseteq \bigcup_{f \in F} C_f$. Finally, if $v_1 \ne v_2$
are vertices such that $[\iota(v_1), \iota(v_2)] \subseteq P$, this segment is disjoint from
$\operatorname{int} P$, it contains $\iota(v)$ only for $v \in \{v_1, v_2\}$, and it lies in
exactly two faces, then some edge has endpoints $(v_1, v_2)$ or $(v_2, v_1)$. Then
$|V| - |E| + |F| = 2$.

The vertex set may contain points that are not extreme points of $P$, such as subdivision
vertices on an edge or inside a face of the polyhedron, and the faces may subdivide a face of $P$
(for example by a diagonal); the statement concerns this cellulation, and $E$ and $F$ need not be
the edges and facets of $P$.

## Sources

- https://en.wikipedia.org/wiki/Euler_characteristic.

Stated but not proved: `MetaMathlibExt.euler_polyhedron_formula` is written with `theorem_wanted` in [WantedExt/Geometry/Polyhedra/EulerPolyhedronFormulaWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Polyhedra/EulerPolyhedronFormulaWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/index.html#euler-polyhedron-formula).

## Monsky's theorem

Let $T$ be a finite set of subsets of the Euclidean plane
$\mathbb{R}^2$ such that every member of $T$ is the convex hull of three points $a, b, c$ of the
plane (not necessarily distinct), the union of the members of $T$ is the closed unit square
$[0,1]^2$, any two distinct members of $T$ have disjoint interiors, and all members of $T$ have
the same Lebesgue measure. Then the number of members of $T$ is even.

Proof: A 2-adic valuation on ℝ gives a three-colouring of the plane, and a Sperner-type parity
count supplies a rainbow triangle whose area valuation rules out an odd number of pieces.

## Sources

- Paul Monsky, "On Dividing A Square Into Triangles," *The American Mathematical Monthly* 77(2) (1970), 161–164, DOI 10.1080/00029890.1970.11992441.

Formalized by `MetaMathlibExt.monsky_theorem`, a theorem declared in [MathlibExt/Geometry/Dissections/Monsky.lean, line 2763](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Dissections/Monsky.lean#L2763). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/index.html#monsky-theorem).

## Squaring the square with distinct squares

There are an integer $n > 1$ and real numbers
$x_i$, $y_i$ and $s_i > 0$ for $i = 1, \dots, n$, with the $s_i$ pairwise distinct, such that
the union of the closed squares $[x_i, x_i + s_i] \times [y_i, y_i + s_i]$ is the unit square
$[0, 1] \times [0, 1]$ and any two of these squares with different indices have disjoint
interiors.

## Sources

- S. Ruziewicz, Problem 59 of the Scottish Book, asking whether a square can be decomposed into a finite number of squares all different from one another; the answer is affirmative. The first published solution is R. Sprague's 1939 squaring of the square with distinct squares; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015), and the 2026 survey "90+ years of the Scottish Book" (arXiv:2603.27867).

Stated but not proved: `MathlibExt.Geometry.ScottishBook59Wanted.squaringTheSquareDistinctSquares` is written with `theorem_wanted` in [WantedExt/Geometry/ScottishBook59Wanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/ScottishBook59Wanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-02/index.html#squaring-the-square-distinct-squares).

## Sylvester–Gallai theorem

Every finite non-collinear subset of the real Euclidean plane determines an ordinary line: two
points of the set such that no third point of the set is collinear with them.

## Sources

- J. J. Sylvester, Mathematical Question 11851, Educational Times 59 (1893) 98; L. M. Kelly, A resolution of the Sylvester–Gallai problem, Discrete Comput. Geom. 1 (1986) 101–104 standard real-plane version.

Formalized by `MathlibExt.Geometry.Euclidean.SylvesterGallaiWanted.sylvester_gallai`, a theorem declared in [MathlibExt/Geometry/Euclidean/SylvesterGallai.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/SylvesterGallai.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-02/index.html#sylvester-gallai).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrete geometry](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/discrete-geometry)
