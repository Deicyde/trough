---
declaration: section
origin: cited
lean: StatMech.Lattice.Dart, StatMech.Lattice.Dart.rev, StatMech.Lattice.Dart.dir, StatMech.Lattice.Dart.equivSimpleGraphDart, StatMech.Lattice.Dart.equivSimpleGraphDart_rev, StatMech.Lattice.unitWt, StatMech.Lattice.mkDart, StatMech.Lattice.IsBoundaryDart
statement: formalized
proof: formalized
---

# Boundary contours in the square lattice

89 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html).

## Dart of the square lattice

An oriented edge of the square lattice: a pair of nearest-neighbour sites. This is the same data
as Mathlib's `SimpleGraph.Dart` of `hypercubicLattice 2`; see
`StatMech.Lattice.Dart.equivSimpleGraphDart`.

Formalized by `StatMech.Lattice.Dart`, a structure declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dart).

## Reversal of a lattice dart

The dart with tail and head exchanged.

Formalized by `StatMech.Lattice.Dart.rev`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#rev).

## Direction of a lattice dart

The direction `head - tail` of a dart, one of the four unit vectors of `ℤ²`.

Formalized by `StatMech.Lattice.Dart.dir`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dir).

## Lattice darts agree with graph darts of the square lattice

Lattice darts are exactly Mathlib's darts of the square lattice.

Formalized by `StatMech.Lattice.Dart.equivSimpleGraphDart`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#equiv-simple-graph-dart).

## Dart correspondence respects reversal

Reversing a lattice dart corresponds to `SimpleGraph.Dart.symm`.

Formalized by `StatMech.Lattice.Dart.equivSimpleGraphDart_rev`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartDef.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#equiv-simple-graph-dart-rev).

## $\ell^1$ norm of a vector in $\mathbb{Z}^2$

The `ℓ¹` norm `|z 0| + |z 1|` of a vector of `ℤ²`.

Formalized by `StatMech.Lattice.unitWt`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartNext.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartNext.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#unit-wt).

## Dart from a site in a unit direction

The dart from `p` to `p + g`, for a unit vector `g`.

Formalized by `StatMech.Lattice.mkDart`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartNext.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartNext.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#mk-dart).

## Boundary dart of a set of sites

`e` is a boundary dart of `K`: it points from a site of `K` to a site outside `K`.

Formalized by `StatMech.Lattice.IsBoundaryDart`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartNext.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartNext.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#is-boundary-dart).

## Successor of a boundary dart

The successor of the dart `e` along the boundary of `K`. Write `r` for `e.dir` rotated
clockwise by a quarter turn. If `e.head + r ∈ K` (a reflex corner of `K`), the successor shares the
head of `e`; if only `e.tail + r ∈ K`, it is the translate of `e` by `r`; otherwise (a convex corner
of `K`) it starts at `e.tail` in direction `r`.

Formalized by `StatMech.Lattice.dartNext`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartNext.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartNext.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dart-next).

## Successor map on boundary darts

The successor map restricted to boundary darts of `K`.

Formalized by `StatMech.Lattice.dartNextSub`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dart-next-sub).

## Successor graph on boundary darts

The graph on boundary darts of `K` in which each dart is adjacent to its successor.

Formalized by `StatMech.Lattice.dartSuccGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dart-succ-graph).

## Walk along the first iterates of a boundary dart

The walk `a, next a, …, next^[n] a` in `dartSuccGraph K`.

Formalized by `StatMech.Lattice.orbitWalkAux`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#orbit-walk-aux).

## Minimal period of a boundary dart

The minimal period of the boundary dart `a` under the successor map.

Formalized by `StatMech.Lattice.dartOrbitPeriod`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dart-orbit-period).

## Closed walk around a boundary dart orbit

The closed walk in `dartSuccGraph K` that runs once around the orbit of `a`.

Formalized by `StatMech.Lattice.dartOrbitWalk`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dart-orbit-walk).

## Iterates up to the minimal period are distinct

The iterates `f^[j] x` for `1 ≤ j ≤ minimalPeriod f x` are distinct. See also Mathlib's
`Function.iterate_injOn_Iio_minimalPeriod`, the same statement for `0 ≤ j < minimalPeriod f x`.

Formalized by `StatMech.Lattice.iterate_inj_on_Icc_minimalPeriod`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/DartOrbit.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#iterate-inj-on-icc-minimal-period).

## Inner corner of a boundary dart

The site `e.head + r`, with `r` the clockwise rotation of `e.dir`, lies in `K`; then the
successor of `e` has the same head.

Formalized by `StatMech.Lattice.IsInnerCorner`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#is-inner-corner).

## Two darts in the same boundary orbit

The dart `f` is obtained from `e` by iterating the boundary successor map of `K`.

Formalized by `StatMech.Lattice.SameOrbit`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#same-orbit).

## Orbit saturation by heads connected in the complement

Boundary darts whose heads are connected in `Kᶜ` lie in the same orbit; a reformulation of
`StatMech.Lattice.InterfaceConnected`.

Formalized by `StatMech.Lattice.OrbitHeadsSaturate`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#orbit-heads-saturate).

## King adjacency on the square lattice

King adjacency on `ℤ²`: distinct sites that differ by at most one in each coordinate.

Formalized by `StatMech.Lattice.KingAdj`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#king-adj).

## King-move graph on the complement of a set

The graph of king moves on the complement of `K`.

Formalized by `StatMech.Lattice.boundaryKingGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#boundary-king-graph).

## Site reached by a boundary orbit

Some boundary dart in the orbit of `e` has head `v`.

Formalized by `StatMech.Lattice.OrbitReached`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#orbit-reached).

## Boundary orbits spread along king moves

If the orbit of `e` reaches a site outside `K`, it reaches every king neighbour of that site
outside `K`.

Formalized by `StatMech.Lattice.OrbitKingTransport`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#orbit-king-transport).

## Orbit saturation at reached sites

Every boundary dart whose head is reached by the orbit of `e` lies in that orbit.

Formalized by `StatMech.Lattice.OrbitVertexSaturate`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#orbit-vertex-saturate).

## Lattice connectivity in the complement implies king connectivity

Sites connected by a lattice path in `Kᶜ` are connected by king moves in `Kᶜ`.

Formalized by `StatMech.Lattice.BoundaryKingConnected`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceConnected.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#boundary-king-connected).

## Boundary darts with heads in one component share an orbit

Boundary darts of `K` whose heads lie in the same connected component of `Kᶜ` lie in the same
boundary orbit.

Formalized by `StatMech.Lattice.InterfaceConnected`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceOrbit.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/InterfaceOrbit.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#interface-connected).

## Lower left corner of the unit face at $(a, b)$

The lower left corner `(a, b)` of the unit face `[a, a + 1] × [b, b + 1]`.

Formalized by `StatMech.Lattice.faceCorner00`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#face-corner00).

## Lower right corner of the unit face at $(a, b)$

The lower right corner `(a + 1, b)` of the unit face `[a, a + 1] × [b, b + 1]`.

Formalized by `StatMech.Lattice.faceCorner10`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#face-corner10).

## Upper right corner of the unit face at $(a, b)$

The upper right corner `(a + 1, b + 1)` of the unit face `[a, a + 1] × [b, b + 1]`.

Formalized by `StatMech.Lattice.faceCorner11`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#face-corner11).

## Upper left corner of the unit face at $(a, b)$

The upper left corner `(a, b + 1)` of the unit face `[a, a + 1] × [b, b + 1]`.

Formalized by `StatMech.Lattice.faceCorner01`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#face-corner01).

## Boundary indicator of an edge

`1` if exactly one of `x` and `y` lies in `S`, and `0` otherwise.

Formalized by `StatMech.Lattice.bdInd`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#bd-ind).

## Boundary degree of a unit face

The number of the four edges of the unit face at `(a, b)` that have exactly one
endpoint
in `S`.

Formalized by `StatMech.Lattice.faceBoundaryDegree`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanZ2.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#face-boundary-degree).

## Face loop left of one period of a boundary orbit

The closed walk of faces to the left of the darts in one period of the boundary orbit of `a`.

Formalized by `StatMech.Lattice.mpl_orbitFaceLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/MinimalPeriodLoop.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/MinimalPeriodLoop.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#mpl-orbit-face-loop).

## Minimal-period orbit loop as a lattice walk

The closed face walk of one period of the orbit of `a`, as a walk in the square lattice.

Formalized by `StatMech.Lattice.mpl_orbitLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/MinimalPeriodLoop.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/MinimalPeriodLoop.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#mpl-orbit-loop).

## Lower left corner of a face $f$

The lower left corner of the face `f`. This is `StatMech.Lattice.faceCorner00 (f 0) (f 1)`.

Formalized by `StatMech.Lattice.npd_P00`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#npd-p00).

## Lower right corner of a face $f$

The lower right corner of the face `f`.

Formalized by `StatMech.Lattice.npd_P10`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#npd-p10).

## Upper right corner of a face $f$

The upper right corner of the face `f`.

Formalized by `StatMech.Lattice.npd_P11`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#npd-p11).

## Upper left corner of a face $f$

The upper left corner of the face `f`.

Formalized by `StatMech.Lattice.npd_P01`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#npd-p01).

## Diagonal touch at a face

`K` contains exactly two opposite corners of the face `f`.

Formalized by `StatMech.Lattice.npd_DiagTouch`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#npd-diag-touch).

## No diagonal touch along a boundary orbit

No face visited in one period of the orbit of `a` is a diagonal touch of `K`.

Formalized by `StatMech.Lattice.npd_NoDiagTouchAlongOrbit`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#npd-no-diag-touch-along-orbit).

## Set with no diagonal touches

`K` has no diagonal touch at any face.

Formalized by `StatMech.Lattice.npd_NoDiagTouch`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchDual.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#npd-no-diag-touch).

## King-saturated set

Whenever `K` contains two opposite corners of a face, it contains one of the other two
corners.

Formalized by `StatMech.Lattice.npm_KingSaturated`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchMatching.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/NoPinchMatching.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#npm-king-saturated).

## Boundary orbit face loop as a lattice walk

The face loop of the boundary orbit of `e`, as a closed walk in the square lattice.

Formalized by `StatMech.Lattice.olb_orbitLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitLoopBridge.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitLoopBridge.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#olb-orbit-loop).

## Product set of two coordinate sets in the plane

The product set `{x | x 0 ∈ A ∧ x 1 ∈ B}`.

Formalized by `StatMech.Lattice.ndt_product`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#ndt-product).

## Sublevel set of a separable function

The sublevel set `{x | φ (x 0) + ψ (x 1) ≤ c}` of a separable function.

Formalized by `StatMech.Lattice.ndt_sublevel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#ndt-sublevel).

## Membership in the star hull

Membership in the star hull of `K`: sites of `K`, closed under filling the lower right corner
of a face whose lower left and upper right corners are members, and the lower left corner of
a face whose lower right and upper left corners are members.

Formalized by `StatMech.Lattice.ndt_StarHullMem`, an inductive type declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#ndt-star-hull-mem).

## Star hull of a set of lattice sites

The star hull of `K`: the smallest superset of `K` closed under the diagonal fill rules.

Formalized by `StatMech.Lattice.ndt_StarHull`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#ndt-star-hull).

## Closure under the diagonal fill rules

`S` is closed under the two diagonal fill rules of `StatMech.Lattice.ndt_StarHullMem`.

Formalized by `StatMech.Lattice.ndt_FillClosed`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/StarHull.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#ndt-fill-closed).

## Four quarter turns of the square lattice are the identity

Four counterclockwise quarter turns are the identity, i.e. every site is a periodic point of
 `rot90Fun` of period `4`.

Formalized by `StatMech.Lattice.rot90Fun_iterate_four_eq`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#rot90-fun-iterate-four-eq).

## Rotation of $\mathbb{Z}^2$ by a number of quarter turns

Rotation of `ℤ²` by `s` counterclockwise quarter turns, `s : ZMod 4`.

Formalized by `StatMech.Lattice.rotPow`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#rot-pow).

## Quarter-turn rotations form an action of $\mathbb{Z}/4$

`rotPow` is an action of the additive group `ZMod 4`.

Formalized by `StatMech.Lattice.rotPow_add`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#rot-pow-add).

## Nontrivial quarter-turn rotations fix no lattice direction

A nontrivial rotation moves every lattice direction: `rotPow s` fixes the direction of a dart
 only for `s = 0`.

Formalized by `StatMech.Lattice.rotPow_dir_eq_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#rot-pow-dir-eq-iff).

## Quarter turn between consecutive boundary darts modulo 4

The quarter turn, as an element of `ZMod 4`, from the boundary dart `e` of `K` to its successor
 `dartNext K e`: `1` for a counterclockwise (left) turn, `0` for going straight, `3` for a
 clockwise (right) turn.

Formalized by `StatMech.Lattice.turn`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#turn).

## Signed quarter turn between consecutive boundary darts

The signed quarter turn from `e` to `dartNext K e`: `1` counterclockwise, `0` straight, `-1`
 clockwise. Its reduction mod `4` is `turn K e`.

Formalized by `StatMech.Lattice.turnZ`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#turn-z).

## Next boundary dart direction is rotated by the turn

The direction of `dartNext K e` is the direction of `e` rotated by `turn K e` quarter turns.

Formalized by `StatMech.Lattice.dartNext_dir_eq_rotPow_turn`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dart-next-dir-eq-rot-pow-turn).

## Cumulative turn along a boundary-tracing orbit

The cumulative turn, in `ZMod 4`, over the first `k` steps of the `dartNext K`-orbit of `e`.

Formalized by `StatMech.Lattice.cumTurn`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#cum-turn).

## Dart direction after k steps is rotated by the cumulative turn

After `k` boundary-tracing steps the direction of a dart is its initial direction rotated by the
 cumulative turn `cumTurn K e k`.

Formalized by `StatMech.Lattice.dir_iterate_eq_rotPow_cumTurn`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dir-iterate-eq-rot-pow-cum-turn).

## Total signed turning along a boundary orbit

The total signed turning (in quarter turns) over the first `p` steps of the `dartNext K`-orbit
 of `e`.

Formalized by `StatMech.Lattice.totalTurnZ`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#total-turn-z).

## Total turning of a closed orbit segment is divisible by four

If the orbit of `e` closes after `p` steps, the total signed turning over these steps is
 divisible by `4`.

Formalized by `StatMech.Lattice.four_dvd_totalTurnZ_of_iterate_eq`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#four-dvd-total-turn-z-of-iterate-eq).

## Total turning over the minimal period is divisible by four

The total signed turning around a boundary orbit, taken over its minimal period, is divisible by
 `4`.

Formalized by `StatMech.Lattice.four_dvd_orbit_totalTurnZ`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#four-dvd-orbit-total-turn-z).

## Total turning of a boundary orbit is bounded by its length

The total signed turning around a boundary orbit is at most the orbit length in absolute
 value.

Formalized by `StatMech.Lattice.abs_orbit_totalTurnZ_le`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#abs-orbit-total-turn-z-le).

## Boundary orbit making exactly one full revolution

The boundary orbit through `a` turns by exactly one full revolution, i.e. its total signed
 turning is `4` or `-4` quarter turns.

Formalized by `StatMech.Lattice.TurningIsFullRevolution`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#turning-is-full-revolution).

## Boundary orbit with a full revolution has length at least four

A boundary orbit that makes a full revolution has length at least `4`.

Formalized by `StatMech.Lattice.orbitPeriod_ge_four_of_fullRevolution`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#orbit-period-ge-four-of-full-revolution).

## Number of reflex corners in a boundary orbit

The number of steps `i < p` in the boundary orbit of `e` with turn `turnZ = 1` (reflex
corners of `K`).

Formalized by `StatMech.Lattice.rightCornerCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#right-corner-count).

## Number of convex corners in a boundary orbit

The number of steps `i < p` in the boundary orbit of `e` with turn `turnZ = -1` (convex
corners of `K`).

Formalized by `StatMech.Lattice.leftCornerCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#left-corner-count).

## Unit cell as a one-site set

The one-site set `{(0, 0)}`.

Formalized by `StatMech.Lattice.unitCell`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#unit-cell).

## Rightward boundary dart of the unit cell

The boundary dart of the unit cell pointing right.

Formalized by `StatMech.Lattice.ucDart0`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#uc-dart0).

## Downward boundary dart of the unit cell

The boundary dart of the unit cell pointing down.

Formalized by `StatMech.Lattice.ucDart1`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#uc-dart1).

## Leftward boundary dart of the unit cell

The boundary dart of the unit cell pointing left.

Formalized by `StatMech.Lattice.ucDart2`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#uc-dart2).

## Upward boundary dart of the unit cell

The boundary dart of the unit cell pointing up.

Formalized by `StatMech.Lattice.ucDart3`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#uc-dart3).

## Base boundary dart of the unit cell

The rightward boundary dart of the unit cell, as an element of the subtype of boundary darts.

Formalized by `StatMech.Lattice.ucBase`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalance.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#uc-base).

## Number of straight steps in a boundary orbit

The number of steps `i < p` in the boundary orbit of `e` with turn `0`.

Formalized by `StatMech.Lattice.straightStepCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#straight-step-count).

## Corner balance of a simple lattice polygon

The numbers of reflex and convex corners along the orbit of `a` differ by `4` or `-4`, the
corner count of a simple lattice polygon.

Formalized by `StatMech.Lattice.SimplePolygonCornerBalance`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#simple-polygon-corner-balance).

## Domino as a two-site set

The two-site set `{(0, 0), (1, 0)}`.

Formalized by `StatMech.Lattice.domino`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#domino).

## Downward domino dart at the left site

The boundary dart of the domino from `(0, 0)` downwards.

Formalized by `StatMech.Lattice.dmD0`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dm-d0).

## Leftward domino dart at the left site

The boundary dart of the domino from `(0, 0)` to the left.

Formalized by `StatMech.Lattice.dmD1`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dm-d1).

## Upward domino dart at the left site

The boundary dart of the domino from `(0, 0)` upwards.

Formalized by `StatMech.Lattice.dmD2`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dm-d2).

## Upward domino dart at the right site

The boundary dart of the domino from `(1, 0)` upwards.

Formalized by `StatMech.Lattice.dmD3`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dm-d3).

## Rightward domino dart at the right site

The boundary dart of the domino from `(1, 0)` to the right.

Formalized by `StatMech.Lattice.dmD4`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dm-d4).

## Downward domino dart at the right site

The boundary dart of the domino from `(1, 0)` downwards.

Formalized by `StatMech.Lattice.dmD5`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dm-d5).

## Base boundary dart of the domino

The boundary dart `dmD0` of the domino, as an element of the subtype of boundary darts.

Formalized by `StatMech.Lattice.dmBase`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/CornerBalanceDomino.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#dm-base).

## No-pinch condition for a boundary orbit

Darts in one period of the orbit of `a` that have the same face also have the same direction.

Formalized by `StatMech.Lattice.OrbitFaceNoPinch`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Umlaufsatz.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Umlaufsatz.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#orbit-face-no-pinch).

## Face loop around the unit cell

The closed walk of faces around the unit cell, of length four.

Formalized by `StatMech.Lattice.unitCellFaceLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Umlaufsatz.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Umlaufsatz.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#unit-cell-face-loop).

## Face loop around the domino

The closed walk of faces around the domino, of length six.

Formalized by `StatMech.Lattice.dominoFaceLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Umlaufsatz.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Umlaufsatz.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#domino-face-loop).

## Four unit vectors of $\mathbb{Z}^2$

The four unit vectors of `ℤ²`.

Formalized by `StatMech.Lattice.usc_fourDirs`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#usc-four-dirs).

## Visit times of a boundary orbit to a face

The times `i` in one period of the orbit of `a` at which the dart has face `f`.

Formalized by `StatMech.Lattice.usc_visitSet`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#usc-visit-set).

## Each face visited once per period by a boundary orbit

Every face visited by the orbit of `a` is visited exactly once per period.

Formalized by `StatMech.Lattice.usc_FaceMultiplicityOne`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#usc-face-multiplicity-one).

## Local turn of a boundary orbit at a face

The sum of the turns `turnZ` at the visits of the orbit of `a` to the face `f`.

Formalized by `StatMech.Lattice.usc_localTurn`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#usc-local-turn).

## Faces visited by a boundary orbit in one period

The set of faces visited in one period of the orbit of `a`.

Formalized by `StatMech.Lattice.usc_orbitFaces`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#usc-orbit-faces).

## $p_c(\mathbb{Z}^2) < 1$ under a no-pinch hypothesis

`p_c(ℤ²) < 1`, under the hypothesis that for every configuration with a finite origin cluster
the boundary orbit of the exit dart has period at least three, has no pinch, and contains the
left exit dart.

Formalized by `StatMech.Lattice.usc_pc_lt_one_of_noPinch`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UmlaufsatzSingleCycle.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html#usc-pc-lt-one-of-no-pinch).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Boundary contours in the square lattice](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/boundary-contours-in-the-square-lattice)
