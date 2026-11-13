---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_pathDisplacement, StatMech.Onsager.ons_pathVertices, StatMech.Onsager.ons_openTurnSum, StatMech.Onsager.ons_cyclicTurnSum, StatMech.Onsager.ons_outsideConnector, StatMech.Onsager.ons_outsideConnectorVertexList, StatMech.Onsager.ons_periodStateList, StatMech.Onsager.ons_allPeriodStates
statement: formalized
proof: formalized
---

# Homology and turning of loops on the square-lattice torus

63 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html).

## Total displacement of a list of lattice directions

The total displacement in `ℤ²` of a list of lattice directions.

Formalized by `StatMech.Onsager.ons_pathDisplacement`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-path-displacement).

## Lattice points visited by a path from the origin

The lattice points visited by a path from the origin with the given directions.

Formalized by `StatMech.Onsager.ons_pathVertices`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-path-vertices).

## Open turning sum of a direction list

The total turning (in quarter turns) between consecutive directions of a list.

Formalized by `StatMech.Onsager.ons_openTurnSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-open-turn-sum).

## Cyclic turning sum of a direction list

The total turning of a direction list read cyclically, including the turn from the last
direction back to the first.

Formalized by `StatMech.Onsager.ons_cyclicTurnSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-cyclic-turn-sum).

## Outside connector around the bounding box of a periodic arc

A path east, north, west, south and east again that runs around the bounding box of a periodic
arc with displacement `(dx, dy)` and height `top`.

Formalized by `StatMech.Onsager.ons_outsideConnector`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-outside-connector).

## Lattice points visited by the outside connector

The lattice points visited by the outside connector.

Formalized by `StatMech.Onsager.ons_outsideConnectorVertexList`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-outside-connector-vertex-list).

## States of one period of a periodic walk

The states `(r, i)` (period index `r`, position `i`) of one period of a periodic walk.

Formalized by `StatMech.Onsager.ons_periodStateList`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 936](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L936). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-period-state-list).

## States of the first $N + 1$ periods of a periodic walk

The states of the first `N` periods of a periodic walk followed by the initial state of the next
period.

Formalized by `StatMech.Onsager.ons_allPeriodStates`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 941](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L941). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-all-period-states).

## States of a periodic arc across $N$ periods

The states of the periodic arc from position `imin` in the first period to position `imax` in
period `N`.

Formalized by `StatMech.Onsager.ons_periodicArcStates`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 946](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L946). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-periodic-arc-states).

## Lattice point of a period state

The lattice point of the state `(r, i)`: the `i`-th point of the lift shifted by `r` periods.

Formalized by `StatMech.Onsager.ons_periodStateCoord`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 1023](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L1023). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-period-state-coord).

## Last element of $\{0, \ldots, n - 1\}$

The last element of `Fin n`.

Formalized by `StatMech.Onsager.ons_lastFin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 1063](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L1063). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-last-fin).

## Directions along a periodic arc

The directions along the periodic arc.

Formalized by `StatMech.Onsager.ons_periodicArcDirections`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 1165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L1165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-periodic-arc-directions).

## $N$ repetitions of a direction sequence

`N` repetitions of the direction sequence.

Formalized by `StatMech.Onsager.ons_directionPeriods`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 1362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L1362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-direction-periods).

## Rotation of a lattice point by quarter turns

Rotation of a lattice point by `c` quarter turns.

Formalized by `StatMech.Onsager.ons_rotatePoint`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean, line 1708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/PeriodicTurnClosure.lean#L1708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-rotate-point).

## Reduction of a lattice site to the torus

Reduction of a site of `ℤ²` to the torus `ℤ_L × ℤ_L`.

Formalized by `StatMech.Onsager.ons_reduceSite`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusContractibleLoop.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusContractibleLoop.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-reduce-site).

## Direction sequence of the lift of a closed torus walk

The direction sequence of a closed torus walk, read in the order of the lift to `ℤ²`.

Formalized by `StatMech.Onsager.ons_liftDir`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusContractibleLoop.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusContractibleLoop.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-lift-dir).

## Sites of a closed torus walk in lift order

The sites of a closed torus walk, in the order of the lift.

Formalized by `StatMech.Onsager.ons_liftSite`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusContractibleLoop.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusContractibleLoop.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-lift-site).

## Indicator bit of an edge in an edge set

The indicator of `e ∈ F` in `Fin 2`.

Formalized by `StatMech.Onsager.ons_edgeBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-edge-bit).

## Horizontal edge bit of an edge set at a site

Whether `F` contains the horizontal edge from `p` eastward.

Formalized by `StatMech.Onsager.ons_horizontalBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-horizontal-bit).

## Vertical edge bit of an edge set at a site

Whether `F` contains the vertical edge from `p` northward.

Formalized by `StatMech.Onsager.ons_verticalBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-vertical-bit).

## Mod 2 intersection number of two torus edge sets

The mod-2 intersection number of edge sets `F` and `G` on the torus.

Formalized by `StatMech.Onsager.ons_edgeCycleIntersection`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-edge-cycle-intersection).

## Horizontal edge bit as an element of $\mathbb{Z}/2$

The horizontal edge bit as an element of `ZMod 2`.

Formalized by `StatMech.Onsager.ons_horizontalZBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-horizontal-zbit).

## Vertical edge bit as an element of $\mathbb{Z}/2$

The vertical edge bit as an element of `ZMod 2`.

Formalized by `StatMech.Onsager.ons_verticalZBit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-vertical-zbit).

## Horizontal flux of an edge set through a column

The number mod 2 of horizontal edges of `F` leaving column `x` eastward.

Formalized by `StatMech.Onsager.ons_xFlux`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-x-flux).

## Vertical flux of an edge set through a row

The number mod 2 of vertical edges of `F` leaving row `y` northward.

Formalized by `StatMech.Onsager.ons_yFlux`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-y-flux).

## Vertical-seam edge in a given row

The edge of the vertical seam in row `y`.

Formalized by `StatMech.Onsager.ons_xSeamPortEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-x-seam-port-edge).

## Horizontal-seam edge in a given column

The edge of the horizontal seam in column `x`.

Formalized by `StatMech.Onsager.ons_ySeamPortEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-y-seam-port-edge).

## Prefix sum of a function on $\mathbb{Z}/L$

The prefix sum `∑_{k < x} f k` along `ZMod L`, using the representatives `0, …, L - 1`.

Formalized by `StatMech.Onsager.ons_zmodPrefix`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 519](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L519). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-zmod-prefix).

## Horizontal part of the zero-flux potential construction

The horizontal part of the potential construction for an edge set of zero flux.

Formalized by `StatMech.Onsager.ons_zeroFluxHorizontal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-zero-flux-horizontal).

## Vertical part of the zero-flux potential construction

The vertical part of the potential construction for an edge set of zero flux.

Formalized by `StatMech.Onsager.ons_zeroFluxVertical`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-zero-flux-vertical).

## Face potential of an even subgraph of zero homology

A face potential `P` whose boundary is a given even subgraph of zero homology.

Formalized by `StatMech.Onsager.ons_zeroFluxPotential`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-zero-flux-potential).

## Intersection number of torus edge sets in the field $\mathbb{Z}/2$

The intersection number of two edge sets, valued in `ZMod 2`.

Formalized by `StatMech.Onsager.ons_edgeCycleZIntersection`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean, line 941](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusIntersection.lean#L941). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-edge-cycle-zintersection).

## Parity of an integer as a bit

The parity of an integer as an element of `Fin 2`.

Formalized by `StatMech.Onsager.ons_intParity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopCharacter.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopCharacter.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-int-parity).

## Mod 2 homology class of a winding

The homology class mod 2 of the winding `(m₁, m₂)`.

Formalized by `StatMech.Onsager.ons_windingParity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopCharacter.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopCharacter.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-winding-parity).

## Linear character of the boundary phases

The linear character `(-1)^{a h₁ + b h₂}` of the boundary phases on homology classes mod 2.

Formalized by `StatMech.Onsager.ons_spinLinearCharacter`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopCharacter.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopCharacter.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-spin-linear-character).

## Crossing of the vertical seam by a dart

A dart crosses the vertical seam between the columns `x = -1` and `x = 0`.

Formalized by `StatMech.Onsager.ons_xWrap`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-x-wrap).

## Crossing of the horizontal seam by a dart

A dart crosses the horizontal seam between the rows `y = -1` and `y = 0`.

Formalized by `StatMech.Onsager.ons_yWrap`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-y-wrap).

## Signed crossing of the vertical seam by a dart

The signed crossing of the vertical seam by a dart: `1` eastward, `-1` westward, `0` otherwise.

Formalized by `StatMech.Onsager.ons_xWrapSign`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-x-wrap-sign).

## Signed crossing of the horizontal seam by a dart

The signed crossing of the horizontal seam by a dart: `1` northward, `-1` southward, `0`
otherwise.

Formalized by `StatMech.Onsager.ons_yWrapSign`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-y-wrap-sign).

## Edge set of a closed walk of darts

The set of torus edges traversed by a closed walk of darts.

Formalized by `StatMech.Onsager.ons_dartEdgeSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusLoopHomology.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-dart-edge-set).

## Translation of $\mathbb{Z}^2$ for a winding around the torus

The translation `(L m₁, L m₂)` of `ℤ²` corresponding to winding `(m₁, m₂)` around the torus.

Formalized by `StatMech.Onsager.ons_windingTranslation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPeriodicLift.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPeriodicLift.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-winding-translation).

## Points of the periodic lift of a torus loop

The `i`-th point of the `r`-th period of the lift of a torus loop with winding `(m₁, m₂)`,
relative to the starting point.

Formalized by `StatMech.Onsager.ons_periodicLiftVertex`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPeriodicLift.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPeriodicLift.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-periodic-lift-vertex).

## Base point in $\mathbb{Z}^2$ over the start of a torus loop

A base point in `ℤ²` over the starting site of a torus loop.

Formalized by `StatMech.Onsager.ons_liftBase`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPeriodicLift.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPeriodicLift.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-lift-base).

## Periodic lift anchored at the base point

The periodic lift translated to start at the base point over the starting site.

Formalized by `StatMech.Onsager.ons_anchoredPeriodicLiftVertex`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPeriodicLift.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPeriodicLift.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-anchored-periodic-lift-vertex).

## Signed potential difference across a horizontal edge

The signed difference of a face potential across the horizontal edge at `p`.

Formalized by `StatMech.Onsager.ons_signedHorizontalBoundary`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPrimitiveWinding.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPrimitiveWinding.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-signed-horizontal-boundary).

## Signed potential difference across a vertical edge

The signed difference of a face potential across the vertical edge at `p`.

Formalized by `StatMech.Onsager.ons_signedVerticalBoundary`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPrimitiveWinding.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPrimitiveWinding.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-signed-vertical-boundary).

## Signed boundary coefficient on an outgoing edge

The signed boundary coefficient of a potential on the edge leaving `p` in direction `μ`.

Formalized by `StatMech.Onsager.ons_outgoingBoundaryCoeff`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPrimitiveWinding.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPrimitiveWinding.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-outgoing-boundary-coeff).

## Signed boundary coefficient along a torus loop

The signed boundary coefficient on the `k`-th step of a torus loop.

Formalized by `StatMech.Onsager.ons_loopBoundaryCoeff`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPrimitiveWinding.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusPrimitiveWinding.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-loop-boundary-coeff).

## Edges crossing the vertical seam of the torus

Edges of the torus crossing the vertical seam between the columns `x = -1` and `x = 0`.

Formalized by `StatMech.Onsager.ons_xSeamEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-x-seam-edge).

## Edges crossing the horizontal seam of the torus

Edges of the torus crossing the horizontal seam between the rows `y = -1` and `y = 0`.

Formalized by `StatMech.Onsager.ons_ySeamEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-y-seam-edge).

## Mod 2 homology class of an edge set

The homology class mod 2 of an edge set: the parities of its numbers of edges crossing the
vertical and the horizontal seam.

Formalized by `StatMech.Onsager.ons_evenHomology`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-even-homology).

## Sector weight of a homology class

The sector weight `Z_h(x) = ∑ x^|F|` over even subgraphs `F` of the torus with homology class
`h`.

Formalized by `StatMech.Onsager.ons_sectorWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-sector-weight).

## Sector weight of the trivial homology class

The sector weight of the trivial homology class.

Formalized by `StatMech.Onsager.ons_sector00`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-sector00).

## Sector weight of the homology class $(1, 0)$

The sector weight of the homology class `(1, 0)`.

Formalized by `StatMech.Onsager.ons_sector10`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-sector10).

## Sector weight of the homology class $(0, 1)$

The sector weight of the homology class `(0, 1)`.

Formalized by `StatMech.Onsager.ons_sector01`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-sector01).

## Sector weight of the homology class $(1, 1)$

The sector weight of the homology class `(1, 1)`.

Formalized by `StatMech.Onsager.ons_sector11`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-sector11).

## Signed sector sum $Z_{00} + Z_{10} + Z_{01} - Z_{11}$

The signed sector sum `Z₀₀ + Z₁₀ + Z₀₁ - Z₁₁`.

Formalized by `StatMech.Onsager.ons_spin00`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-spin00).

## Signed sector sum $Z_{00} - Z_{10} + Z_{01} + Z_{11}$

The signed sector sum `Z₀₀ - Z₁₀ + Z₀₁ + Z₁₁`.

Formalized by `StatMech.Onsager.ons_spin10`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-spin10).

## Signed sector sum $Z_{00} + Z_{10} - Z_{01} + Z_{11}$

The signed sector sum `Z₀₀ + Z₁₀ - Z₀₁ + Z₁₁`.

Formalized by `StatMech.Onsager.ons_spin01`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-spin01).

## Signed sector sum $Z_{00} - Z_{10} - Z_{01} - Z_{11}$

The signed sector sum `Z₀₀ - Z₁₀ - Z₀₁ - Z₁₁`.

Formalized by `StatMech.Onsager.ons_spin11`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/TorusSpinSectors.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-spin11).

## Spin-structure character of a mod 2 homology class

The spin-structure character `(-1)^{(1 + a) h₁ + (1 + b) h₂ + h₁ h₂}` of a homology class `h`
mod 2, for boundary phases `a, b`.

Formalized by `StatMech.Onsager.ons_spinCharacter`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCharacter.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCharacter.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-spin-character).

## Intersection form on the mod 2 homology of the torus

The intersection form `h₁ k₂ + h₂ k₁` on `H₁(T², ℤ/2) = (ℤ/2)²`.

Formalized by `StatMech.Onsager.ons_homologyIntersection`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCharacter.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCharacter.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-homology-intersection).

## Spin-character sum over even subgraphs of the torus

The even-subgraph sum of the torus with each subgraph weighted by the spin character of its
homology class.

Formalized by `StatMech.Onsager.ons_spinCharacterSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCharacter.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCharacter.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html#ons-spin-character-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Homology and turning of loops on the square-lattice torus](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/homology-and-turning-of-loops-on-the-square-latt)
