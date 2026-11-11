---
declaration: section
origin: cited
lean: StatMech.Lattice.ffc_offSupportLattice, StatMech.Lattice.ffc_lift_walk, StatMech.Lattice.ffc_floodFill, StatMech.Lattice.offSupport, StatMech.Lattice.offSupportComponent, StatMech.Lattice.EvenDegree.exists_cycle_through_edge_of_even, StatMech.Lattice.sharedPrimalEdge, StatMech.Lattice.bdEdge
statement: formalized
proof: formalized
---

# Discrete Jordan curve theorem for the square lattice

107 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html).

## Square lattice with a set of vertices removed

The square lattice with every vertex of `B` removed (edges with an endpoint in `B` deleted).

Formalized by `StatMech.Lattice.ffc_offSupportLattice`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FloodFillConnected.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/FloodFillConnected.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#ffc-off-support-lattice).

## Lattice walk avoiding a set, lifted to the reduced lattice

A lattice walk avoiding `B`, viewed as a walk in `ffc_offSupportLattice B`.

Formalized by `StatMech.Lattice.ffc_lift_walk`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FloodFillConnected.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/FloodFillConnected.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#ffc-lift-walk).

## Flood fill avoiding a set of sites

The flood fill of `seed` avoiding `B`: the sites reachable from `seed` in the lattice with
`B` removed.

Formalized by `StatMech.Lattice.ffc_floodFill`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FloodFillConnected.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/FloodFillConnected.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#ffc-flood-fill).

## Square lattice with a closed walk's vertices removed

The square lattice with the vertices of the closed walk `Vc` removed. It is the same graph as
`StatMech.Lattice.ffc_offSupportLattice {z | z ∈ Vc.support}`.

Formalized by `StatMech.Lattice.offSupport`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InsideConnected.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InsideConnected.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#off-support).

## Component off a closed walk containing a seed

The sites reachable from `seed` in the lattice with the vertices of `Vc` removed.

Formalized by `StatMech.Lattice.offSupportComponent`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InsideConnected.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InsideConnected.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#off-support-component).

## Every edge of a finite even-degree graph lies on a cycle

In a finite graph in which every vertex has even degree, every edge lies on a cycle. See also
Mathlib's `SimpleGraph.adj_and_reachable_delete_edges_iff_exists_cycle`, which this combines
with `StatMech.Lattice.reachable_deleteEdges_of_even`.

Formalized by `StatMech.Lattice.EvenDegree.exists_cycle_through_edge_of_even`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#exists-cycle-through-edge-of-even).

## Primal edge shared by adjacent faces

The primal edge of `ℤ²` separating the adjacent unit faces with lower left corners `f` and
`g`.

Formalized by `StatMech.Lattice.sharedPrimalEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#shared-primal-edge).

## Boundary edge of a set

The edge `e` has exactly one endpoint in `S`.

Formalized by `StatMech.Lattice.bdEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#bd-edge).

## Face-boundary graph of a set

The face-boundary graph of `S`: two adjacent faces are joined when the primal edge between
them has exactly one endpoint in `S`. Its edges are the dual edges crossing the boundary of
`S`.

Formalized by `StatMech.Lattice.faceBoundaryGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#face-boundary-graph).

## Four unit faces at a lattice site

The four unit faces having the site `c` as a corner.

Formalized by `StatMech.Lattice.cornerFaces`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosure.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#corner-faces).

## Number of boundary crossings of a walk

The number of edges of the walk `w` with exactly one endpoint in `S`.

Formalized by `StatMech.Lattice.crossCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CrossingParity.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CrossingParity.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#cross-count).

## Square lattice with the boundary edges of a set removed

The square lattice with every edge having exactly one endpoint in `S` removed.

Formalized by `StatMech.Lattice.latticeMinusBarrier`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CrossingParity.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CrossingParity.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#lattice-minus-barrier).

## Exterior of a box maps into the face-region graph

For `H` and `f0g0` inside `[-R, R]²`, the lattice on the exterior of `[-(R + 1), R + 1]²`
maps into the face-region graph of `H` with `f0g0` deleted.

Formalized by `StatMech.Lattice.jfd_extToDeletedHom`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ExteriorReconnect.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/ExteriorReconnect.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jfd-ext-to-deleted-hom).

## Jordan curve theorem for cycles: face count two

A cycle, as a graph on its own vertices, has face count two: the combinatorial form of the
**Jordan curve theorem** for cycles (C. Jordan, *Cours d'analyse*, 1887).

Formalized by `StatMech.Lattice.jcs_cycle_faceCount_eq_two`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCycleSpace.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCycleSpace.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcs-cycle-face-count-eq-two).

## Jordan region of the cut lattice

`S` and its complement are nonempty, and any two sites on the same side of `S` are connected
in the lattice with the boundary edges of `S` removed.

Formalized by `StatMech.Lattice.jcs_JordanRegion`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCycleSpace.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCycleSpace.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcs-jordan-region).

## Bounded region count as cycle rank

The number of bounded regions of a finite graph, defined as its cycle rank `nullity G`.

Formalized by `StatMech.Lattice.jes_boundedRegionCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEulerSeparation.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEulerSeparation.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jes-bounded-region-count).

## Quadrant below and left of a site

The quadrant of sites `p` with `p 0 ≤ z 0 - 1` and `p 1 ≤ z 1 - 1`.

Formalized by `StatMech.Lattice.jec_quad`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-quad).

## Ray edges left of a site

The vertical lattice edges in a column left of `z` joining rows `z 1 - 1` and `z 1`: the
edges crossed by a horizontal ray going left from the face corner of `z`.

Formalized by `StatMech.Lattice.jec_rayEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-ray-edge).

## Wall edges below a site

The horizontal lattice edges in a row below `z` joining columns `z 0 - 1` and `z 0`: the
edges crossed by a vertical ray going down from the face corner of `z`.

Formalized by `StatMech.Lattice.jec_wallEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-wall-edge).

## Ray-crossing count of a walk

The number of ray edges of `z` traversed by the walk `w`.

Formalized by `StatMech.Lattice.jec_rayCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-ray-count).

## Wall-crossing count of a walk

The number of wall edges of `z` traversed by the walk `w`.

Formalized by `StatMech.Lattice.jec_wallCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-wall-count).

## Inside of a closed walk by the even-odd rule

The inside of a closed walk `Vc` by the even–odd rule: sites whose ray count with respect to
`Vc` is odd.

Formalized by `StatMech.Lattice.jec_leftRegion`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-left-region).

## Vertical lattice path upward

The vertical lattice path from `(col, r)` up to `(col, r + k)`.

Formalized by `StatMech.Lattice.jec_vsegUp`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-vseg-up).

## Horizontal lattice path rightward

The horizontal lattice path from `(t, row)` right to `(t + k, row)`.

Formalized by `StatMech.Lattice.jec_hsegRight`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-hseg-right).

## Return path around a rectangle

A lattice path from `(b0, d)` back to `(a0, c)` running outside the rectangle `[α, β] × [c,
d]`: up, left to column `α - 1`, down to row `c - 1`, right, and up.

Formalized by `StatMech.Lattice.jec_retPath`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-ret-path).

## Half-plane below a row

The half-plane of sites in rows below `y`.

Formalized by `StatMech.Lattice.jec_belowSet`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-below-set).

## Open vertical crossings separate the sides of a rectangle

For every configuration, every overlap rectangle, and every `α < β`, `c ≤ d`, the arc-side
property `StatMech.Universality.CrossingArcSides` holds: an open vertical crossing of the
overlap separates the left side of `[α, β] × [c, d]` from its right side.

Formalized by `StatMech.Lattice.jec_crossingArcSides`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean, line 643](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanExteriorClosure.lean#L643). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jec-crossing-arc-sides).

## Set of sites is the inside of a closed lattice walk

Some closed lattice walk has odd ray count exactly at the sites of `K`, so `K` is the inside
of that walk.

Formalized by `StatMech.Lattice.ccs_OrbitIsLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ClosedContourSeparation.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/ClosedContourSeparation.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#ccs-orbit-is-loop).

## Inside and outside of a closed walk are connected

The inside and the outside of `Vc` are nonempty and each is connected in the lattice with the
boundary edges of the inside removed. This is `StatMech.Lattice.jcs_JordanRegion
(jec_leftRegion Vc)`.

Formalized by `StatMech.Lattice.egf_LoopFloodFill`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerGeometricFaces.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/EulerGeometricFaces.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#egf-loop-flood-fill).

## Lattice off a closed walk

The subgraph of the square lattice induced on the sites not visited by `Vc`.

Formalized by `StatMech.Lattice.fcb_offComplGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceComponentBijection.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceComponentBijection.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#fcb-off-compl-graph).

## Jordan region property off a closed walk

Both sides of `Vc` contain sites off `Vc`, and any two sites off `Vc` on the same side are
joined by a lattice path avoiding `Vc`.

Formalized by `StatMech.Lattice.fcb_OffComplJordanRegion`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceComponentBijection.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceComponentBijection.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#fcb-off-compl-jordan-region).

## Veblen's theorem step for unions of cycles

One step of **Veblen's theorem** (O. Veblen, 1912) for graphs whose vertices all have degree
zero or two: a nonempty such graph has a subgraph of the same kind with fewer edges and face count
one less (obtained by deleting a cycle).

Formalized by `StatMech.Lattice.jvp_isCycles_veblenStep`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanVeblenStep.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanVeblenStep.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jvp-is-cycles-veblen-step).

## Adjacency relation of the cut horizontal axis

Both sites lie on the horizontal axis and the pair is not `{(0, 0), (1, 0)}`.

Formalized by `StatMech.Lattice.jkr_lineRel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepReconnectCounterexample.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepReconnectCounterexample.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkr-line-rel).

## Horizontal axis with one edge removed

The horizontal axis of `ℤ²` with the edge from `(0, 0)` to `(1, 0)` removed.

Formalized by `StatMech.Lattice.jkr_lineH`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepReconnectCounterexample.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepReconnectCounterexample.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkr-line-h).

## Keep-reconnect residue for finite graphs

For every graph `H` of `ℤ²` with finitely many edges and every lattice edge `pq` outside `H`
with dual edge `f0g0`: if `p` and `q` are disconnected in `H`, then `f0` and `g0` are
connected in the face-region graph of `H` with `f0g0` deleted.

Formalized by `StatMech.Lattice.jkr_FiniteKeepReconnectResidue`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepReconnectCounterexample.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepReconnectCounterexample.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkr-finite-keep-reconnect-residue).

## Rotated region graph of a lattice subgraph

The square lattice with the edge `crossEdge e` removed for every edge `e` of `G`. Since
`crossEdge` is a global rotation, this is not the faithful dual complement; see
`StatMech.Lattice.whb_faceRegion` for the version using `sharedPrimalEdge`.

Formalized by `StatMech.Lattice.regionGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#region-graph).

## Planar lattice subgraph of the square lattice

A finite graph together with an injective map into `ℤ²` that sends edges to lattice edges.

Formalized by `StatMech.Lattice.PlanarZ2Subgraph`, a structure declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#planar-z2-subgraph).

## Image of a planar lattice subgraph in the square lattice

The image of a `PlanarZ2Subgraph` as a subgraph of the square lattice.

Formalized by `StatMech.Lattice.imageGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#image-graph).

## Geometric count of bounded regions

The number of finite connected components of the region graph of `P`.

Formalized by `StatMech.Lattice.geometricRegionCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#geometric-region-count).

## Box exterior embeds in the region graph

Outside a box containing the image of `P`, the lattice embeds in the region graph.

Formalized by `StatMech.Lattice.exteriorToRegionHom`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarFaceGeometric.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#exterior-to-region-hom).

## Even-degree condition on a subgraph

Every vertex of `K` has even degree.

Formalized by `StatMech.Lattice.jcx_IsEven`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-is-even).

## Even-peelable graph

`K` reduces to the empty graph by repeatedly deleting a cycle through a base vertex `v` such
that, after the deletion, the other vertices of the cycle are isolated.

Formalized by `StatMech.Lattice.jcx_IsEvenPeelable`, an inductive type declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-is-even-peelable).

## Vertices of two unit squares sharing a corner

The vertices of two unit squares `[0, 1]²` and `[1, 2]²` sharing the corner `(1, 1)`.

Formalized by `StatMech.Lattice.jcx_cross_emb`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-cross-emb).

## Adjacency relation of two corner-sharing squares

Adjacency of the two squares sharing a corner, as a Boolean relation.

Formalized by `StatMech.Lattice.jcx_cross_rel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-cross-rel).

## Two 4-cycles sharing a vertex

Two 4-cycles sharing the vertex `2`, on `Fin 7`.

Formalized by `StatMech.Lattice.jcx_cross_G`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-cross-g).

## Two corner-sharing unit squares as a planar lattice subgraph

Two unit squares sharing a corner as a `PlanarZ2Subgraph`.

Formalized by `StatMech.Lattice.jcx_cross_P`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-cross-p).

## Upper 4-cycle based at the shared vertex

The 4-cycle of the upper square, based at the shared vertex.

Formalized by `StatMech.Lattice.jcx_cross_cycB`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-cross-cyc-b).

## Adjacency relation of the lower 4-cycle

Adjacency of the lower 4-cycle, as a Boolean relation.

Formalized by `StatMech.Lattice.jcx_cross_A_rel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-cross-a-rel).

## Lower 4-cycle left after deleting the upper one

The lower 4-cycle, which remains after deleting the upper one.

Formalized by `StatMech.Lattice.jcx_cross_A`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean, line 570](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanCrossingCount.lean#L570). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-cross-a).

## Pushforward of a subgraph into the square lattice

The image in `ℤ²` of a subgraph `K` of a `PlanarZ2Subgraph` `P`.

Formalized by `StatMech.Lattice.jei_pushGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEulerInduction.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEulerInduction.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jei-push-graph).

## Even-degree subgraphs have as many regions as their face count

Every subgraph `K` of `P` whose image has all degrees even has exactly `faceCount K`
face-region components.

Formalized by `StatMech.Lattice.jcx_EvenCountResidue`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FaithfulEvenPeel.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/FaithfulEvenPeel.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-even-count-residue).

## Peeling a cycle from an even-degree subgraph

Every nonempty subgraph `K` of `P` whose image has all degrees even contains a subgraph of
the same kind with fewer edges, face count one less, and one fewer face-region component.

Formalized by `StatMech.Lattice.jcx_EvenPeel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FaithfulEvenPeel.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/FaithfulEvenPeel.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcx-even-peel).

## Square lattice minus the edges of a graph

The square lattice with the edges of `H` deleted.

Formalized by `StatMech.Lattice.jbc_latticeMinusEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-lattice-minus-edges).

## Quarter-turn isomorphism onto the region graph

The quarter-turn rotation is an isomorphism from the lattice minus the edges of `H` onto the
region graph of `H`.

Formalized by `StatMech.Lattice.jbc_rotIso`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-rot-iso).

## Disconnected sites are joined in the lattice minus a bridged graph

If `x` and `y` are not connected in `K`, they are connected in the lattice minus the image of
`K ⊔ edge x y`.

Formalized by `StatMech.Lattice.jbc_BridgeDirection`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-bridge-direction).

## Corners of the unit square in cyclic order

The four corners `(0, 0), (1, 0), (1, 1), (0, 1)` of the unit square, in cyclic order.

Formalized by `StatMech.Lattice.jbc_csq`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-csq).

## Adjacency relation of the 4-cycle

Adjacency of the 4-cycle `0 – 1 – 2 – 3 – 0`, as a Boolean relation.

Formalized by `StatMech.Lattice.jbc_cyc4Rel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-cyc4-rel).

## The 4-cycle graph

The 4-cycle on `Fin 4`.

Formalized by `StatMech.Lattice.jbc_cyc4`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-cyc4).

## Vertex 0 of the 4-cycle

The vertex `0` of the 4-cycle.

Formalized by `StatMech.Lattice.jbc_v0`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-v0).

## Vertex 1 of the 4-cycle

The vertex `1` of the 4-cycle.

Formalized by `StatMech.Lattice.jbc_v1`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-v1).

## Unit square as a planar lattice subgraph

The unit square: the 4-cycle embedded on the corners of `[0, 1]²`.

Formalized by `StatMech.Lattice.jbc_Pce`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanBridgeCycle.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jbc-pce).

## Cactus graph, defined by peeling leaves and cycles

`K` reduces to the empty graph by repeatedly deleting a leaf edge or, when `K` is a union of
cycles, one of its cycles.

Formalized by `StatMech.Lattice.jgc_IsCactus`, an inductive type declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jgc-is-cactus).

## Unit square corners with a pendant site

The corners of the unit square together with the site `(-1, 0)`.

Formalized by `StatMech.Lattice.jgc_pend_emb`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jgc-pend-emb).

## Adjacency relation of a 4-cycle with a pendant edge

Adjacency of the 4-cycle on `0, 1, 2, 3` with the pendant edge `{0, 4}`, as a Boolean
relation.

Formalized by `StatMech.Lattice.jgc_pend_rel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jgc-pend-rel).

## 4-cycle with a pendant edge

The 4-cycle with a pendant edge, on `Fin 5`.

Formalized by `StatMech.Lattice.jgc_pend_G`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jgc-pend-g).

## Unit square with a pendant edge as a planar lattice subgraph

The unit square with a pendant edge as a `PlanarZ2Subgraph`.

Formalized by `StatMech.Lattice.jgc_pend_P`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jgc-pend-p).

## 4-cycle core of the pendant example

The 4-cycle on `0, 1, 2, 3` inside `Fin 5`.

Formalized by `StatMech.Lattice.jgc_pend_core`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanGeneralCount.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jgc-pend-core).

## Number of face regions of a subgraph's image

The number of connected components of the face-region graph of the image of `K`.

Formalized by `StatMech.Lattice.jic_tc`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jic-tc).

## Corners of two distant unit squares

The corners of the unit squares at `(0, 0)` and `(10, 0)`.

Formalized by `StatMech.Lattice.jic_twoSq_emb`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jic-two-sq-emb).

## Adjacency relation of two disjoint 4-cycles

Adjacency of two disjoint 4-cycles on `Fin 8`, as a Boolean relation.

Formalized by `StatMech.Lattice.jic_twoSq_rel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jic-two-sq-rel).

## Two disjoint 4-cycles

Two disjoint 4-cycles on `Fin 8`.

Formalized by `StatMech.Lattice.jic_twoSq_G`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean, line 611](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean#L611). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jic-two-sq-g).

## Two disjoint unit squares as a planar lattice subgraph

Two disjoint unit squares as a `PlanarZ2Subgraph`.

Formalized by `StatMech.Lattice.jic_twoSq_P`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean, line 626](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanIsCyclesCount.lean#L626). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jic-two-sq-p).

## Radius of a box containing a planar lattice subgraph

A radius `R` such that the image of `P` lies in `box 2 R`.

Formalized by `StatMech.Lattice.outerBoxRadius`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanOuterFaceUnique.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanOuterFaceUnique.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#outer-box-radius).

## Outer region of the rotated region graph

The outer region: the component of the region graph containing the far site `beacon 2 R`.

Formalized by `StatMech.Lattice.outerRegion`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanOuterFaceUnique.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanOuterFaceUnique.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#outer-region).

## Bounded regions are the components other than the outer one

The finite components of the region graph are exactly the components other than the outer
region.

Formalized by `StatMech.Lattice.boundedRegionEquivNeOuter`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanOuterFaceUnique.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanOuterFaceUnique.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#bounded-region-equiv-ne-outer).

## Whitney cut-cycle duality for a planar lattice subgraph

Whitney's cut–cycle duality for `P`: for every subgraph `K` of `P` and edge `xy` of `P` not
in `K`, with `f0g0` the dual edge across it, `x` and `y` are connected in `K` iff `f0` and
`g0` are disconnected in the face-region graph of `K` with `f0g0` deleted.

Formalized by `StatMech.Lattice.jfc_WhbSync`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jfc-whb-sync).

## Outer face region of a planar lattice subgraph

The outer region: the component of the face-region graph of `P` containing a face far from
`P`.

Formalized by `StatMech.Lattice.jfc_whb_outerRegion`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jfc-whb-outer-region).

## Pushed-forward subgraphs are locally finite

The image of a subgraph of a `PlanarZ2Subgraph` is locally finite.

Formalized by `StatMech.Lattice.jfc_pushGraph_locallyFinite`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jfc-push-graph-locally-finite).

## Whitney duality for even-degree planar lattice subgraphs

Every `PlanarZ2Subgraph` whose image has all degrees even satisfies `jfc_WhbSync`.

Formalized by `StatMech.Lattice.jfc_EvenDegreeThreading`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jfc-even-degree-threading).

## Interior region of the unit square

The component of the face `(0, 0)` in the face-region graph of the unit square.

Formalized by `StatMech.Lattice.jfc_sq_interior`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanFaithfulCount.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jfc-sq-interior).

## Veblen step property for even-degree subgraphs

Every nonempty subgraph `K` of `P` with even-degree image contains an even-degree subgraph
with fewer edges and face count one less.

Formalized by `StatMech.Lattice.jvp_VeblenStep`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanVeblenPeel.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanVeblenPeel.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jvp-veblen-step).

## Region step property for even-degree subgraphs

Whenever `K' ≤ K` are even-degree subgraphs of `P` with fewer edges and face count one less,
the face-region graph of `K` has one more component than that of `K'`.

Formalized by `StatMech.Lattice.jvp_RegionStep`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanVeblenPeel.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanVeblenPeel.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jvp-region-step).

## Nine sites of a 3 by 3 grid

The nine sites of `[0, 2]²`, indexed row by row.

Formalized by `StatMech.Lattice.jkd_gr9emb`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkd-gr9emb).

## Adjacency relation of the 3 by 3 grid

Adjacency of the `3 × 3` grid on `Fin 9`, as a Boolean relation.

Formalized by `StatMech.Lattice.jkd_gr9rel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkd-gr9rel).

## The 3 by 3 grid graph

The `3 × 3` grid graph on `Fin 9`.

Formalized by `StatMech.Lattice.jkd_gr9G`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkd-gr9-g).

## 3 by 3 grid as a planar lattice subgraph

The `3 × 3` grid as a `PlanarZ2Subgraph`.

Formalized by `StatMech.Lattice.jkd_ringP`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkd-ring-p).

## Grid vertex $(0, 0)$

The vertex `(0, 0)` of the grid.

Formalized by `StatMech.Lattice.jkd_r0`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkd-r0).

## Grid vertex $(1, 0)$

The vertex `(1, 0)` of the grid.

Formalized by `StatMech.Lattice.jkd_r1`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/KeepResidueExamples.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jkd-r1).

## Adding an edge between two components merges them

Adding an edge between two components merges them. This assumes only finitely many
components; see also `StatMech.Lattice.card_components_sup_edge_of_not_reachable` for finite
vertex types.

Formalized by `StatMech.Lattice.jsf_card_components_sup_edge_merge`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/RegionGraphAddEdge.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/RegionGraphAddEdge.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jsf-card-components-sup-edge-merge).

## Cut set of a face coloring

The primal edges `sharedPrimalEdge a b` between adjacent faces `a`, `b` on which `T` takes
different values.

Formalized by `StatMech.Lattice.jed_cutSet`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jed-cut-set).

## Lattice graph spanned by an edge set

The graph on `ℤ²` whose edges are the lattice edges in `E`.

Formalized by `StatMech.Lattice.jed_primalGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jed-primal-graph).

## Bounded faces of a finite lattice graph are counted by its cycle rank

For a
`PlanarZ2Subgraph` `P`, the finite components of the face-region graph `whb_faceRegion` of its
image (faces of `ℤ²`, two adjacent faces joined unless the primal edge between them lies in `P`)
are equinumerous with `Fin (nullity P.G)`, so the number of bounded faces is `|E| - |V| + c`.
This is a count: it does not identify each bounded face with the interior of a particular cycle
of `P`. References: H. Whitney, *Planar graphs* (1933); C. Thomassen, *The Jordan–Schönflies
theorem and the classification of surfaces* (1992).

Formalized by `StatMech.Lattice.jed_faithfulDiscreteJordan`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jed-faithful-discrete-jordan).

## Twelve boundary edges of a 3 by 3 rectangle

The twelve lattice edges of the boundary of the rectangle `[-1, 2] × [-2, 1]`.

Formalized by `StatMech.Lattice.jed_boxEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jed-box-edges).

## Boundary of a 3 by 3 rectangle as a graph

The boundary of the rectangle `[-1, 2] × [-2, 1]` as a graph.

Formalized by `StatMech.Lattice.jed_boxH`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEnclosureDuality.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jed-box-h).

## Bounded regions of a planar lattice subgraph

The bounded (finite) connected components of the face-region graph of `P`.

Formalized by `StatMech.Lattice.jcb_BoundedRegion`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-bounded-region).

## Bounded regions indexed by the cycle rank

The bijection between bounded regions of `P` and `Fin (nullity P.G)` given by the discrete
Jordan–Euler theorem.

Formalized by `StatMech.Lattice.jcb_boundedRegionEquiv`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-bounded-region-equiv).

## Cycle rank one gives a unique bounded region

A `PlanarZ2Subgraph` of cycle rank one has exactly one bounded region.

Formalized by `StatMech.Lattice.jcb_uniqueBoundedRegion_of_nullity_one`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-unique-bounded-region-of-nullity-one).

## Jordan curve theorem

**Jordan curve theorem** for lattice cycles: a connected `PlanarZ2Subgraph` with as many
edges as vertices has exactly one bounded region. Reference: C. Jordan, *Cours d'analyse*
(1887); for the discrete form, C. Thomassen, *The Jordan–Schönflies theorem and the
classification of surfaces* (1992).

Formalized by `StatMech.Lattice.jcb_uniqueBoundedRegion_of_connected_cycle`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-unique-bounded-region-of-connected-c).

## Lattice points around the L-shaped tromino

The eight lattice points around the L-shaped tromino, in cyclic order.

Formalized by `StatMech.Lattice.jcb_Lemb`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-lemb).

## Adjacency relation of the 8-cycle

Adjacency of the 8-cycle on `Fin 8`, as a Boolean relation.

Formalized by `StatMech.Lattice.jcb_LcycRel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-lcyc-rel).

## The 8-cycle graph

The 8-cycle on `Fin 8`.

Formalized by `StatMech.Lattice.jcb_Lcyc`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-lcyc).

## 8-cycle around the L-tromino as a planar lattice subgraph

The 8-cycle around the L-shaped tromino as a `PlanarZ2Subgraph`.

Formalized by `StatMech.Lattice.jcb_LPce`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-lpce).

## Two diagonally touching sites

The two-site set `{(0, 0), (1, 1)}`, which touches diagonally.

Formalized by `StatMech.Lattice.jcb_diagK`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanClusterBridge.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcb-diag-k).

## Facial orbit of a boundary dart

The orbit of a boundary dart of `C`, as a connected component of the successor graph on
boundary darts.

Formalized by `StatMech.Lattice.rsf_facialOrbit`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/RotationSystemFaces.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/RotationSystemFaces.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#rsf-facial-orbit).

## Boundary darts of a component off a closed walk

The set of boundary darts of a connected component of the sites off the support of `Vc`.

Formalized by `StatMech.Lattice.rsf_componentDarts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/RotationSystemFaces.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/RotationSystemFaces.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#rsf-component-darts).

## Facial orbits cover the components of the complement

The boundary dart sets of the components of the complement of `Vc` are exactly the members of
`𝓕`.

Formalized by `StatMech.Lattice.rsf_FacialOrbitsCoverComponents`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/RotationSystemFaces.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/RotationSystemFaces.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#rsf-facial-orbits-cover-components).

## Separating side between inside and outside sites

Some set `S` contains `inside`, misses `outside`, and every lattice edge between sites of `D`
that leaves `S` has an endpoint in `B`.

Formalized by `StatMech.Lattice.jcu_HasSeparatingSide`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/SeparatingSide.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/SeparatingSide.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html#jcu-has-separating-side).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrete Jordan curve theorem for the square lattice](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/discrete-jordan-curve-theorem-for-the-square-lat)
