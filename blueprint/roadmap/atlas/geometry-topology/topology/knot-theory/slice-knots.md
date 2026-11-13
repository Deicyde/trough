---
declaration: section
origin: cited
lean: MathlibExt.Topology.ConwayTopologicallySliceWanted.KnotTheory.conway_knot_topologically_slice, MathlibExt.Topology.PiccirilloWanted.KnotTheory.conwayKnot_isSimple, MathlibExt.Topology.PiccirilloWanted.KnotTheory.conway_knot_not_smoothly_slice, MathlibExt.Topology.SliceDichotomyWanted.KnotTheory.exists_topologically_slice_not_smoothly_slice
statement: formalized
---

# Slice knots

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/slice-knots/index.html).

## The Conway knot is topologically slice

Let $K$ be the PL knot traced by the braid closure
on $4$ strands of the braid word
$\sigma_1^{-2} \sigma_2 \sigma_1^{-1} \sigma_2 \sigma_1^{-1} \sigma_3 \sigma_2^{-2} \sigma_3^2$
for the Conway knot 11n34. Then $K$ is topologically slice: there is a smooth knot $J$ whose
image is unoriented topologically ambient isotopic in $\mathbb{R}^3$ to the image of $K$, and $J$
is topologically slice.

This follows from Freedman's theorem that every knot with trivial Alexander polynomial is
topologically slice, since the Conway knot has $\Delta_K(t) = 1$.

## Sources

- Freedman, *The topology of four-dimensional manifolds*, J. Diff. Geom. 17 (1982). See also Freedman-Quinn, *Topology of 4-Manifolds*, Princeton 1990. Problem `conway_knot_topologically_slice` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.ConwayTopologicallySliceWanted.KnotTheory.conway_knot_topologically_slice` is written with `theorem_wanted` in [WantedExt/Topology/ConwayTopologicallySliceWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ConwayTopologicallySliceWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/slice-knots/index.html#conway-knot-topologically-slice).

## The Conway knot polyline is a simple closed curve

Let $K$ be the Conway knot $11n34$,
realized as a closed polyline in $\mathbb{R}^3$ (the braid closure of a 4-strand braid word for
it), and let $N$ be its number of vertices. The periodic piecewise-linear parametrization of $K$,
which traverses each edge in unit time, is injective on the interval $[0, N)$.

Equivalently, the vertices of $K$ are distinct, non-adjacent edges are disjoint, and adjacent
edges meet only at their shared vertex.

## Sources

- https://arxiv.org/abs/1808.02923. Problem `conway_knot_not_smoothly_slice` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.PiccirilloWanted.KnotTheory.conwayKnot_isSimple` is written with `theorem_wanted` in [WantedExt/Topology/PiccirilloWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PiccirilloWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/slice-knots/index.html#conway-knot-is-simple).

## The Conway knot is not smoothly slice (Piccirillo)

Let $K$ be the Conway knot $11n34$,
realized as a closed polyline in $\mathbb{R}^3$. There is no smooth knot $J$, that is, a smooth
$2\pi$-periodic map $\mathbb{R} \to \mathbb{R}^3$ with nowhere vanishing derivative that is
injective on $[0, 2\pi)$, with both of the following properties: some topological ambient isotopy
of $\mathbb{R}^3$ carries the image of $J$ onto the image of $K$; and there is a smooth map
$D \colon \mathbb{R}^2 \to \mathbb{R}^3 \times \mathbb{R}$ that is injective with injective
derivative on the closed unit disk $\overline{\mathbb{D}}$, takes $\overline{\mathbb{D}}$ into the
half-space $\mathbb{R}^3 \times [0, \infty)$, takes a point of $\overline{\mathbb{D}}$ to height
$0$ exactly when it lies on the unit circle, and whose $\mathbb{R}^3$-component maps the unit
circle onto the image of $J$.

## Sources

- https://arxiv.org/abs/1808.02923. Problem `conway_knot_not_smoothly_slice` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.PiccirilloWanted.KnotTheory.conway_knot_not_smoothly_slice` is written with `theorem_wanted` in [WantedExt/Topology/PiccirilloWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/PiccirilloWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/slice-knots/index.html#conway-knot-not-smoothly-slice).

## A topologically slice knot that is not smoothly slice

There is a PL knot $K$ (a closed
polyline in $\mathbb{R}^3$ with at least three vertices, not required to be simple) that is
topologically slice but not smoothly slice. Here $K$ is smoothly (respectively topologically)
slice when some smooth knot whose image is topologically ambient isotopic to the image of $K$
bounds a smooth (respectively locally flat) properly embedded $2$-disk in
$\mathbb{R}^3 \times [0, \infty)$.

## Sources

- Casson, 1980s (unpublished); Akbulut-Matveyev, *A convex decomposition theorem for 4-manifolds*, IMRN 1998. See also Hedden-Kirk-Livingston, *Non-slice linear combinations of algebraic knots*, J. Eur. Math. Soc. 14 (2012). Problem `exists_topologically_slice_not_smoothly_slice` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.SliceDichotomyWanted.KnotTheory.exists_topologically_slice_not_smoothly_slice` is written with `theorem_wanted` in [WantedExt/Topology/SliceDichotomyWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/SliceDichotomyWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/slice-knots/index.html#exists-topologically-slice-not-smoothly).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Slice knots](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/slice-knots/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/knot-theory/slice-knots)
