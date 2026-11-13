---
declaration: section
origin: cited
lean: StatMech.Onsager.BaseCase.stepOf, StatMech.Onsager.BaseCase.pos, StatMech.Onsager.BaseCase.cc, StatMech.Onsager.BaseCase.sum_turns_zero, StatMech.Onsager.BaseCase.four_dvd_cc, StatMech.Onsager.BaseCase.cc_pos, StatMech.Onsager.BaseCase.four_le_cc, StatMech.Onsager.BaseCase.base_cc_eq_four
statement: formalized
proof: formalized
---

# Hopf's Umlaufsatz for lattice polygons

212 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/index.html).

## Unit lattice step in a given direction

The unit step of `ℤ²` in direction `w`: `0 ↦ (1, 0)` (east), `1 ↦ (0, 1)` (north), `2 ↦ (-1, 0)`
 (west), `3 ↦ (0, -1)` (south).

Formalized by `StatMech.Onsager.BaseCase.stepOf`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#step-of).

## Vertices of a lattice walk from its step directions

The `k`-th vertex of the lattice walk with step directions `d`: the sum of the steps `stepOf (d
 i)` for `i < k`, so that `pos d 0 = 0`.

Formalized by `StatMech.Onsager.BaseCase.pos`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#pos).

## Number of left turns of a direction sequence

The number of counterclockwise (left) quarter turns of the cyclic direction sequence `d`, i.e.
 of indices `i` with `d (i + 1) - d i = 1`.

Formalized by `StatMech.Onsager.BaseCase.cc`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#cc).

## Turns of a cyclic direction sequence sum to zero

The turns of a cyclic direction sequence sum to zero in `Fin 4`.

Formalized by `StatMech.Onsager.BaseCase.sum_turns_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#sum-turns-zero).

## Without right turns, the number of left turns is divisible by four

If every turn is straight or left, the number of left turns is divisible by `4`.

Formalized by `StatMech.Onsager.BaseCase.four_dvd_cc`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#four-dvd-cc).

## A closed walk without right turns turns at least once

A closed walk with only straight steps and left turns turns at least once.

Formalized by `StatMech.Onsager.BaseCase.cc_pos`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#cc-pos).

## A closed walk without right turns has at least four left turns

A closed walk with only straight steps and left turns has at least four left turns.

Formalized by `StatMech.Onsager.BaseCase.four_le_cc`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#four-le-cc).

## Exactly four left turns when simplicity rules out eight

A closed walk with only straight steps and left turns has exactly four left turns, provided
 simplicity rules out eight or more.

Formalized by `StatMech.Onsager.BaseCase.base_cc_eq_four`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/DirectionWalk.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#base-cc-eq-four).

## Reverse of a dart

The reverse of a dart: it starts at the head of `d` and points in the opposite direction.

Formalized by `StatMech.Onsager.ons_dartRev`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurningTelescope.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurningTelescope.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#ons-dart-rev).

## Turn between two directions as an element of $\mathbb{Z}/4$

The turn from direction `μ` to `ν` as an element of `ZMod 4`.

Formalized by `StatMech.Onsager.ons_turnZ`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurningTelescope.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurningTelescope.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#ons-turn-z).

## Integer turn exponent between two directions

The integer turn exponent from `μ` to `ν`: `1` for a left turn, `-1` for a right turn, `0` for
going straight (and, by convention, for a U-turn).

Formalized by `StatMech.Onsager.ons_turnPow`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurningTelescope.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurningTelescope.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#ons-turn-pow).

## Closed lattice walk starts at the origin

The walk starts at the origin.

Formalized by `StatMech.Onsager.NoDoubleWind.pos_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#pos-zero).

## Forward vertex recursion of a closed lattice walk

Vertex recursion of a closed walk: the next vertex is the current one plus the current step
 (indices taken cyclically).

Formalized by `StatMech.Onsager.NoDoubleWind.pos_succ`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#pos-succ).

## Backward vertex recursion of a closed lattice walk

Vertex recursion of a closed walk read backwards from vertex `M`.

Formalized by `StatMech.Onsager.NoDoubleWind.pos_pred`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#pos-pred).

## Coordinates of the four lattice steps

The four lattice steps, case by case.

Formalized by `StatMech.Onsager.NoDoubleWind.stepOf_coords`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#step-of-coords).

## North step followed by west step at the top corner of a walk

A closed walk with only straight steps and left turns has a north step immediately followed by a
 west step (at its lexicographically largest vertex).

Formalized by `StatMech.Onsager.NoDoubleWind.lexmax_corner`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkVertices.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#lexmax-corner).

## North-then-west corner at the highest vertices

A closed walk without right turns has a north-then-west corner at the rightmost of its highest
 vertices.

Formalized by `StatMech.Onsager.UmlaufsatzStrip.ymax_NW_corner`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#ymax-nw-corner).

## South-then-east corner at the lowest vertices

A closed walk without right turns has a south-then-east corner at one of its lowest vertices.

Formalized by `StatMech.Onsager.UmlaufsatzStrip.ymin_SE_corner`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#ymin-se-corner).

## Previous and next vertices of a north-then-west corner

At a north-then-west corner `M`, the previous vertex is just below and the next vertex just to
 the left.

Formalized by `StatMech.Onsager.UmlaufsatzStrip.nw_corner_neighbours`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#nw-corner-neighbours).

## Distinct north-then-west corners sit at distinct vertices

In a simple walk, distinct north-then-west corners sit at distinct vertices.

Formalized by `StatMech.Onsager.UmlaufsatzStrip.nw_corners_distinct_pos`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-01/index.html#nw-corners-distinct-pos).

## Contiguous top row of a walk

The vertices of the walk at its maximal height cover every lattice point between any two of
 them, i.e. the top row of the walk is a contiguous horizontal segment.

Formalized by `StatMech.Onsager.UmlaufsatzStrip.TopRowContiguous`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/ExtremeCorners.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#top-row-contiguous).

## Recursion for the x-coordinate of a closed walk

The `x`-coordinate recursion of a closed walk. See also
 `StatMech.Onsager.WalkCrossing.fst_step`.

Formalized by `StatMech.Onsager.NoDoubleWind2.xco_succ`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#xco-succ).

## Recursion for the y-coordinate of a closed walk

The `y`-coordinate recursion of a closed walk. See also
 `StatMech.Onsager.WalkCrossing.snd_step`.

Formalized by `StatMech.Onsager.NoDoubleWind2.yco_succ`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#yco-succ).

## No east step leaves a rightmost vertex

No east step leaves a vertex of maximal `x`-coordinate.

Formalized by `StatMech.Onsager.NoDoubleWind2.maxx_no_E_out`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#maxx-no-e-out).

## No west step arrives at a rightmost vertex

No west step arrives at a vertex of maximal `x`-coordinate.

Formalized by `StatMech.Onsager.NoDoubleWind2.maxx_no_W_in`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#maxx-no-w-in).

## No south step leaves a lowest vertex

No south step leaves a vertex of minimal `y`-coordinate.

Formalized by `StatMech.Onsager.NoDoubleWind2.miny_no_S_out`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#miny-no-s-out).

## No north step arrives at a lowest vertex

No north step arrives at a vertex of minimal `y`-coordinate.

Formalized by `StatMech.Onsager.NoDoubleWind2.miny_no_N_in`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#miny-no-n-in).

## Number of left turns out of a given direction

The number of left turns of `d` from direction `c` to direction `c + 1`.

Formalized by `StatMech.Onsager.NoDoubleWind2.tcount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#tcount).

## Number of straight continuations in a given direction

The number of straight continuations of `d` in direction `c`.

Formalized by `StatMech.Onsager.NoDoubleWind2.scount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#scount).

## Every direction is left by equally many left turns

In a direction sequence without right turns, every direction is left by the same number of left
 turns.

Formalized by `StatMech.Onsager.NoDoubleWind2.tcount_shift`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#tcount-shift).

## Left turns are four times the north-to-west turns

In a direction sequence without right turns, the number of left turns is four times the number
 of north-to-west turns.

Formalized by `StatMech.Onsager.NoDoubleWind2.cc_eq_four_mul_tcount`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#cc-eq-four-mul-tcount).

## Eight left turns give two north-then-west corners

Eight or more left turns, without right turns, give two distinct north-then-west corners.

Formalized by `StatMech.Onsager.NoDoubleWind2.exists_two_top_corners`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#exists-two-top-corners).

## A unique top corner forces fewer than eight left turns

If the north-then-west corner is unique, a direction sequence without right turns has fewer than
 eight left turns.

Formalized by `StatMech.Onsager.NoDoubleWind2.cc_lt_eight_of_uniqueTopCorner`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TurnCount.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#cc-lt-eight-of-unique-top-corner).

## Vertical lattice direction

The direction `w` is vertical (north or south).

Formalized by `StatMech.Onsager.WalkCrossing.isVertEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#is-vert-edge).

## Horizontal lattice direction

The direction `w` is horizontal (east or west).

Formalized by `StatMech.Onsager.WalkCrossing.isHorizEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#is-horiz-edge).

## Recursion for the y-coordinate of a walk step

The `y`-coordinate recursion of a closed walk. See also
 `StatMech.Onsager.NoDoubleWind2.yco_succ`.

Formalized by `StatMech.Onsager.WalkCrossing.snd_step`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#snd-step).

## Recursion for the x-coordinate of a walk step

The `x`-coordinate recursion of a closed walk. See also
 `StatMech.Onsager.NoDoubleWind2.xco_succ`.

Formalized by `StatMech.Onsager.WalkCrossing.fst_step`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#fst-step).

## Number of crossings of a horizontal line

The number of vertical steps of the walk crossing the horizontal line `y = m + 1/2`, i.e.
 vertical steps between heights `m` and `m + 1`.

Formalized by `StatMech.Onsager.WalkCrossing.fullLineCross`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#full-line-cross).

## A closed walk crosses a horizontal line equally often up and down

A closed walk crosses the line `y = m + 1/2` upwards as often as downwards.

Formalized by `StatMech.Onsager.WalkCrossing.upDown_card_eq`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#up-down-card-eq).

## A closed walk crosses each horizontal line an even number of times

A closed walk crosses each horizontal line `y = m + 1/2` an even number of times.

Formalized by `StatMech.Onsager.WalkCrossing.fullLineCross_even`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-02/index.html#full-line-cross-even).

## A lattice point lies on a walk step

The lattice point `p` lies on the closed segment traversed by step `k`.

Formalized by `StatMech.Onsager.WalkCrossing.onEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#on-edge).

## Crossing steps force a repeated vertex

If a horizontal and a vertical step that share no index endpoint meet at a point, the walk
 visits some vertex twice.

Formalized by `StatMech.Onsager.WalkCrossing.edges_cross_not_injective`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#edges-cross-not-injective).

## Number of crossings of a horizontal ray

The number of vertical steps crossing the line `y = m + 1/2` strictly to the right of `x =
 qx`.

Formalized by `StatMech.Onsager.WalkCrossing.rayCross`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossing.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#ray-cross).

## Upward ray crossings above a cell

The number of horizontal steps of the walk on the column `[a, a + 1]` strictly above the cell
 `(a, b)`: the crossings of the upward vertical ray from the center of that cell.

Formalized by `StatMech.Onsager.JordanParity.upCross`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#up-cross).

## Ray-crossing parity of a lattice cell

The parity of the number of crossings of the upward ray from the center of cell `(a, b)` with
 the walk; cells with parity `1` are inside the walk.

Formalized by `StatMech.Onsager.JordanParity.rayParity`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#ray-parity).

## Upward crossing count is unchanged across a vertical move

The upward crossing count is the same for cells `(a, b)` and `(a, b + 1)` when no horizontal
 step lies between them.

Formalized by `StatMech.Onsager.JordanParity.upCross_vstep`, a lemma declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#up-cross-vstep).

## Ray parity is unchanged across a vertical move

The ray parity is the same for cells `(a, b)` and `(a, b + 1)` when no horizontal step lies
 between them.

Formalized by `StatMech.Onsager.JordanParity.rayParity_vstep`, a lemma declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#ray-parity-vstep).

## No upward crossings for cells above a walk

Cells at or above the top height of the walk have no upward crossings.

Formalized by `StatMech.Onsager.JordanParity.upCross_topOutside`, a lemma declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#up-cross-top-outside).

## Cells above a walk are outside

Cells at or above the top height of the walk are outside.

Formalized by `StatMech.Onsager.JordanParity.rayParity_topOutside`, a lemma declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#ray-parity-top-outside).

## Upward crossing counts of horizontal neighbours sum to an even number

When no vertical step separates the cells `(a, b)` and `(a + 1, b)`, their upward crossing
 counts add up to an even number.

Formalized by `StatMech.Onsager.JordanParity.upCross_hstep`, a lemma declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#up-cross-hstep).

## Ray parity is unchanged across a horizontal move

The ray parity is the same for cells `(a, b)` and `(a + 1, b)` when no vertical step lies
 between them.

Formalized by `StatMech.Onsager.JordanParity.rayParity_hstep`, a lemma declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/JordanParity.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#ray-parity-hstep).

## Moving horizontally inside a closed walk

If cell `(a, b)` is inside and no vertical step separates it from `(a + 1, b)`, then `(a + 1,
 b)` is inside.

Formalized by `StatMech.Onsager.InsideClimb.inside_climb_x`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#inside-climb-x).

## Moving vertically inside a closed walk

If cell `(a, b)` is inside and no horizontal step separates it from `(a, b + 1)`, then `(a, b +
 1)` is inside.

Formalized by `StatMech.Onsager.InsideClimb.inside_climb_y`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#inside-climb-y).

## Coordinates of the vertices around a north-then-west corner

The vertices before and after a north-then-west corner.

Formalized by `StatMech.Onsager.InsideClimb.nw_corner_coords`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#nw-corner-coords).

## The north step at a corner blocks horizontal movement

At a north-then-west corner, the north step separates the cell below-left of the corner from its
 right neighbour.

Formalized by `StatMech.Onsager.InsideClimb.nw_corner_not_climbable_x`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#nw-corner-not-climbable-x).

## The west step at a corner blocks vertical movement

At a north-then-west corner, the west step separates the cell below-left of the corner from its
 top neighbour.

Formalized by `StatMech.Onsager.InsideClimb.nw_corner_not_climbable_y`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#nw-corner-not-climbable-y).

## Uniqueness of the lexicographically largest vertex

In a simple walk the lexicographically largest vertex is attained at a unique index.

Formalized by `StatMech.Onsager.InsideClimb.lexmax_unique`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#lexmax-unique).

## Existence of a north-then-west corner

A closed walk without right turns has a north-then-west corner.

Formalized by `StatMech.Onsager.InsideClimb.exists_lexmax_nw_corner`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#exists-lexmax-nw-corner).

## Two north-then-west corners force a self-intersection

Any two distinct north-then-west corners of `d` force `pos d` to be non-injective.

Formalized by `StatMech.Onsager.InsideClimb.two_nw_corners_not_injective`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#two-nw-corners-not-injective).

## Four left turns, given that two corners force a self-intersection

A simple closed walk without right turns has four left turns, assuming that two distinct
 north-then-west corners force a self-intersection.

Formalized by `StatMech.Onsager.InsideClimb.cc_eq_four_of_selfAvoidanceWall`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InsidePropagation.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-03/index.html#cc-eq-four-of-self-avoidance-wall).

## Unit cell to the left of a lattice step

The unit cell to the left of the step in direction `w` starting at `p` (cells are named by their
 lower-left corners).

Formalized by `StatMech.Onsager.Orientation.leftCell`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#left-cell).

## Steps around a left turn share their left cell

At a left turn, the steps before and after the turn have the same left cell.

Formalized by `StatMech.Onsager.Orientation.leftCell_eq_of_leftTurn`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#left-cell-eq-of-left-turn).

## No vertical step through a non-vertex point

A vertical step through the point `(c, h)` has `(c, h)` as a vertex; if `(c, h)` is not a walk
 vertex, no vertical step straddles height `h` on the line `x = c`.

Formalized by `StatMech.Onsager.Orientation.no_vEdge_of_not_vertex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#no-v-edge-of-not-vertex).

## No horizontal step starts at a non-vertex point

If `(c, h)` is not a walk vertex, no horizontal step starts at `x = c` on height `h`.

Formalized by `StatMech.Onsager.Orientation.no_hEdge_of_not_vertex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#no-h-edge-of-not-vertex).

## Index of a vertical step above a walk vertex

In a simple walk, a vertical step on the segment above the vertex `pos d m` is step `m` or step
 `m - 1`.

Formalized by `StatMech.Onsager.Orientation.vEdge_lower_index`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#v-edge-lower-index).

## Index of a horizontal step right of a walk vertex

In a simple walk, a horizontal step on the segment to the right of the vertex `pos d m` is step
 `m` or step `m - 1`.

Formalized by `StatMech.Onsager.Orientation.hEdge_left_index`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#h-edge-left-index).

## Index of a vertical step below a walk vertex

In a simple walk, a vertical step on the segment below the vertex `pos d m` is step `m` or step
 `m - 1`.

Formalized by `StatMech.Onsager.Orientation.vEdge_upper_index`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#v-edge-upper-index).

## Index of a horizontal step left of a walk vertex

In a simple walk, a horizontal step on the segment to the left of the vertex `pos d m` is step
 `m` or step `m - 1`.

Formalized by `StatMech.Onsager.Orientation.hEdge_right_index`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#h-edge-right-index).

## Left cells keep their ray parity on a straight step

Going straight, consecutive left cells have the same ray parity.

Formalized by `StatMech.Onsager.Orientation.leftCell_parity_eq_of_straight`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#left-cell-parity-eq-of-straight).

## Ray parity of the cell left of a step

The ray parity of the cell to the left of step `k`.

Formalized by `StatMech.Onsager.Orientation.leftParity`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#left-parity).

## Consecutive steps have the same left parity

For a simple closed walk without right turns, consecutive steps have the same left parity.

Formalized by `StatMech.Onsager.Orientation.leftParity_step`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#left-parity-step).

## Left parity is constant along a walk without right turns

For a simple closed walk without right turns, the left parity is the same for every step.

Formalized by `StatMech.Onsager.Orientation.leftParity_const`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Orientation.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#left-parity-const).

## Vertical steps separating two horizontal neighbour cells

The vertical steps of the walk on the segment `{a + 1} × [b, b + 1]` separating the cells `(a,
 b)` and `(a + 1, b)`.

Formalized by `StatMech.Onsager.RayFlipH.straddleSet`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipH.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipH.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#straddle-set).

## Parity of upward crossings across a vertical segment

The upward crossing counts of cells `(a, b)` and `(a + 1, b)` plus the number of steps between
 them is even.

Formalized by `StatMech.Onsager.RayFlipH.upCross_hstep_gen`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipH.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipH.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#up-cross-hstep-gen).

## Ray parity across a vertical segment counts separating steps

The ray parities of cells `(a, b)` and `(a + 1, b)` add up to the number of separating vertical
 steps mod `2`.

Formalized by `StatMech.Onsager.RayFlipH.rayParity_hstep_gen`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipH.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipH.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#ray-parity-hstep-gen).

## An odd number of vertical steps flips the ray parity

An odd number of vertical steps between cells `(a, b)` and `(a + 1, b)` flips the ray parity.

Formalized by `StatMech.Onsager.RayFlipH.rayParity_hflip`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipH.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipH.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#ray-parity-hflip).

## Horizontal steps on a unit segment

The horizontal steps of the walk on the segment `[a, a + 1] × {b}`.

Formalized by `StatMech.Onsager.RayFlipV.midSet`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipV.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipV.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#mid-set).

## Upward crossings of vertically adjacent cells differ by separating steps

The upward crossings from cell `(a, b)` are those from `(a, b + 1)` plus the horizontal steps
 between the two cells.

Formalized by `StatMech.Onsager.RayFlipV.upCross_vsplit`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipV.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipV.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#up-cross-vsplit).

## An odd number of horizontal steps flips the ray parity

An odd number of horizontal steps between cells `(a, b)` and `(a, b + 1)` flips the ray
 parity.

Formalized by `StatMech.Onsager.RayFlipV.rayParity_vflip`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipV.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/RayFlipV.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#ray-parity-vflip).

## $k + 2 \ne k$ in $\mathrm{Fin}\, n$ for $n \ge 3$

In `Fin n` with `n ≥ 3`, `k + 2 ≠ k`.

Formalized by `StatMech.Onsager.EdgeUnique.not_add_two_self`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-04/index.html#not-add-two-self).

## Steps on a horizontal unit segment join its endpoints

A step on the horizontal segment `[a, a + 1] × {b}` goes from one endpoint to the other.

Formalized by `StatMech.Onsager.EdgeUnique.midSet_endpoints`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#mid-set-endpoints).

## Steps on a vertical unit segment join its endpoints

A step on the vertical segment `{a + 1} × [b, b + 1]` goes from one endpoint to the other.

Formalized by `StatMech.Onsager.EdgeUnique.straddleSet_endpoints`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#straddle-set-endpoints).

## A simple closed walk traverses each horizontal segment at most once

A simple closed walk traverses each horizontal unit segment at most once.

Formalized by `StatMech.Onsager.EdgeUnique.midSet_card_le_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#mid-set-card-le-one).

## A simple closed walk traverses each vertical segment at most once

A simple closed walk traverses each vertical unit segment at most once.

Formalized by `StatMech.Onsager.EdgeUnique.straddleSet_card_le_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/EdgeUnique.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#straddle-set-card-le-one).

## Some north-then-west corner has its below-left cell inside

A simple closed walk without right turns has a north-then-west corner `M` whose below-left cell
 `((pos d M).1 - 1, (pos d M).2 - 1)` has ray parity `1`.

Formalized by `StatMech.Onsager.InsideConnected.lexmax_corner_cell_inside`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopCornerCellInside.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopCornerCellInside.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#lexmax-corner-cell-inside).

## No north step leaves a highest vertex

No north step leaves a vertex of maximal height.

Formalized by `StatMech.Onsager.TopRow.top_out_ne_N`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#top-out-ne-n).

## No south step arrives at a highest vertex

No south step arrives at a vertex of maximal height.

Formalized by `StatMech.Onsager.TopRow.top_in_ne_S`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#top-in-ne-s).

## Position after a run of west steps

After `j` consecutive west steps from vertex `M`, the walk is `j` units to the left of `M` at
 the same height.

Formalized by `StatMech.Onsager.TopRow.forward_west_run`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#forward-west-run).

## Single west run covering the top row

Every vertex of the walk at the height of `M` is reached from `M` by a run of consecutive west
 steps.

Formalized by `StatMech.Onsager.TopRow.SingleTopRun`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#single-top-run).

## A single top run makes the top row contiguous

If the top row is covered by a single west run from a highest vertex, it is contiguous.

Formalized by `StatMech.Onsager.TopRow.topRowContiguous_of_singleTopRun`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#top-row-contiguous-of-single-top-run).

## Top row is contiguous when every top corner starts a single run

If every highest north-then-west corner starts a single top run, the top row is contiguous.

Formalized by `StatMech.Onsager.TopRow.topRowContiguous_of_residue`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRow.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#top-row-contiguous-of-residue).

## A north step into a highest vertex is followed by a west step

In a closed walk without right turns, a north step arriving at a highest vertex is followed by a
 west step.

Formalized by `StatMech.Onsager.SingleTopRunProof.top_arrival_west`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#top-arrival-west).

## A west step on the top row is followed by west or south

A west step on the top row is followed by a west or a south step, and stays on the top row.

Formalized by `StatMech.Onsager.SingleTopRunProof.top_west_next`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#top-west-next).

## A closed walk is not all west steps

A closed walk does not consist of west steps only.

Formalized by `StatMech.Onsager.SingleTopRunProof.exists_step_ne_west`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#exists-step-ne-west).

## A west run from a highest vertex ends in a south step

From a highest vertex where the walk turns west, it makes `J ≥ 1` west steps and then a south
 step.

Formalized by `StatMech.Onsager.SingleTopRunProof.exists_west_run_end`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#exists-west-run-end).

## A west run covering the top row is a single top run

A west run from `M` whose vertices cover the top row is a single top run.

Formalized by `StatMech.Onsager.SingleTopRunProof.singleTopRun_of_runCoversTop`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/TopRowWestRun.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#single-top-run-of-run-covers-top).

## A step changes the x-coordinate by at most one

A step changes the `x`-coordinate by `0` or `±1`.

Formalized by `StatMech.Onsager.WalkCrossingV.fst_step_bound`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossingV.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossingV.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#fst-step-bound).

## Number of crossings of a vertical line

The number of horizontal steps of the walk crossing the vertical line `x = m + 1/2`.

Formalized by `StatMech.Onsager.WalkCrossingV.vertColCross`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossingV.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossingV.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#vert-col-cross).

## A closed walk crosses a vertical line equally often left and right

A walk crosses the line `x = m + 1/2` to the right as often as to the left.

Formalized by `StatMech.Onsager.WalkCrossingV.leftRight_card_eq`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossingV.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossingV.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#left-right-card-eq).

## A closed walk crosses each vertical line an even number of times

A closed walk crosses each vertical line `x = m + 1/2` an even number of times.

Formalized by `StatMech.Onsager.WalkCrossingV.vertColCross_even`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossingV.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCrossingV.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-05/index.html#vert-col-cross-even).

## Interior cells by the even-odd rule

The cells inside the walk by the even-odd rule: those with ray parity `1`.

Formalized by `StatMech.Onsager.InteriorCells.interiorSet`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#interior-set).

## Minimal height of a walk

The minimal height of a vertex of the walk.

Formalized by `StatMech.Onsager.InteriorCells.yInf`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#y-inf).

## Maximal height of a walk

The maximal height of a vertex of the walk.

Formalized by `StatMech.Onsager.InteriorCells.ySup`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#y-sup).

## An inside cell lies below a horizontal step

An inside cell lies directly below some horizontal step of the walk.

Formalized by `StatMech.Onsager.InteriorCells.exists_edge_of_rayParity`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#exists-edge-of-ray-parity).

## Cells below a walk are outside

Cells below the walk are outside.

Formalized by `StatMech.Onsager.InteriorCells.rayParity_zero_of_lt_yInf`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#ray-parity-zero-of-lt-y-inf).

## Finiteness of the interior of a closed walk

A closed walk has finitely many inside cells.

Formalized by `StatMech.Onsager.InteriorCells.interiorSet_finite`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#interior-set-finite).

## Finite set of interior cells of a closed walk

The finite set of cells inside a closed walk (ray parity `1`). See also
 `StatMech.Onsager.WalkCellRegion.interiorCells`, the bounded face of the walk; the two agree for
 simple walks without right turns (`StatMech.Onsager.UmlaufsatzFinal.interiorCells_bridge`).

Formalized by `StatMech.Onsager.InteriorCells.interiorCells`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorCells.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#interior-cells).

## Corner count of the interior counts inside cells around a point

The corner count of the interior at `(vx, vy)` counts the inside cells among the four cells
 around that point.

Formalized by `StatMech.Onsager.WalkCellBridge.cornerCount_interior_eq`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBridge.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBridge.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-count-interior-eq).

## Ray parity is constant around a non-vertex point

At a lattice point that is not a vertex of the walk, the four cells around it have the same ray
 parity.

Formalized by `StatMech.Onsager.WalkCellBridge.rayParity_const_of_not_vertex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBridge.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBridge.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#ray-parity-const-of-not-vertex).

## Corner weight at a left turn into the east direction

At a left turn made of a south step followed by an east step, the corner weight of the interior
 is `1` if the cell to the left of the walk is inside and `-1` otherwise.

Formalized by `StatMech.Onsager.LeftCornerE.cornerWeight_leftTurn_E`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LeftCornerE.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LeftCornerE.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-weight-left-turn-e).

## Corner weight at a left turn into the north direction

At a left turn made of an east step followed by a north step, the corner weight of the interior
 is `1` if the cell to the left of the walk is inside and `-1` otherwise.

Formalized by `StatMech.Onsager.LeftCornerN.cornerWeight_leftTurn_N`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LeftCornerN.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LeftCornerN.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-weight-left-turn-n).

## Corner weight at a left turn into the south direction

At a left turn made of a west step followed by a south step, the corner weight of the interior
 is `1` if the cell to the left of the walk is inside and `-1` otherwise.

Formalized by `StatMech.Onsager.LeftCornerS.cornerWeight_leftTurn_S`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LeftCornerS.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LeftCornerS.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-weight-left-turn-s).

## Corner weight at a left turn into the west direction

At a left turn made of a north step followed by a west step, the corner weight of the interior
 is `1` if the cell to the left of the walk is inside and `-1` otherwise.

Formalized by `StatMech.Onsager.LeftCornerW.cornerWeight_leftTurn_W`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LeftCornerW.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LeftCornerW.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-weight-left-turn-w).

## A horizontal direction is not vertical

A horizontal direction is not vertical.

Formalized by `StatMech.Onsager.StraightCorner.not_isVert_of_isHoriz`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#not-is-vert-of-is-horiz).

## A vertical direction is not horizontal

A vertical direction is not horizontal.

Formalized by `StatMech.Onsager.StraightCorner.not_isHoriz_of_isVert`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#not-is-horiz-of-is-vert).

## Even corner counts have zero corner weight

An even corner count has weight `0`.

Formalized by `StatMech.Onsager.StraightCorner.cornerWeight_eq_zero_of_two_dvd`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-weight-eq-zero-of-two-dvd).

## Zero corner weight where the walk continues horizontally

A vertex where the walk continues horizontally has weight `0`.

Formalized by `StatMech.Onsager.StraightCorner.cornerWeight_straight_horiz`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-weight-straight-horiz).

## Zero corner weight where the walk continues vertically

A vertex where the walk continues vertically has weight `0`.

Formalized by `StatMech.Onsager.StraightCorner.cornerWeight_straight_vert`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-weight-straight-vert).

## Straight steps of a simple closed walk carry no corner weight

A vertex where a simple closed walk goes straight has corner weight `0` for the interior.

Formalized by `StatMech.Onsager.StraightCorner.cornerWeight_straight`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/StraightCorner.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#corner-weight-straight).

## Horizontal neighbours of different parity are separated by a vertical step

If cells `(a, b)` and `(a + 1, b)` have different ray parities, a vertical step separates
 them.

Formalized by `StatMech.Onsager.PinchFree.straddle_nonempty_of_ne`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/PinchFree.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/PinchFree.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-06/index.html#straddle-nonempty-of-ne).

## Vertical neighbours of different parity are separated by a horizontal step

If cells `(a, b)` and `(a, b + 1)` have different ray parities, a horizontal step separates
 them.

Formalized by `StatMech.Onsager.PinchFree.mid_nonempty_of_ne`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/PinchFree.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/PinchFree.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#mid-nonempty-of-ne).

## Interior of a simple closed walk has no pinch points

The interior of a simple closed walk has no pinch points.

Formalized by `StatMech.Onsager.PinchFree.pinch_free`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/PinchFree.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/PinchFree.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#pinch-free).

## Pinch count of the ray-parity interior is zero

The interior of a simple closed walk has pinch count `0`. See also
 `StatMech.Onsager.WalkCellLocal.pinchCount_interiorCells_eq_zero`.

Formalized by `StatMech.Onsager.PinchFree.pinchCount_eq_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/PinchFree.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/PinchFree.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#pinch-count-eq-zero).

## Zero corner weight of the interior off the walk

A lattice point off the walk has corner weight `0` for the interior.

Formalized by `StatMech.Onsager.WalkCornerSum.cornerWeight_zero_of_notMem_image`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCornerSum.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCornerSum.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#corner-weight-zero-of-not-mem-image).

## Corner defect of the interior as a sum over walk vertices

For a simple closed walk, the corner defect of the interior is the sum of the corner weights at
 the walk vertices.

Formalized by `StatMech.Onsager.WalkCornerSum.cornerDiff_interior_eq_walk_sum`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCornerSum.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCornerSum.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#corner-diff-interior-eq-walk-sum).

## Corner weights at the turns of a walk without right turns

The corner weight of the interior at the vertex after step `i` is `±1` (sign given by the
 orientation) at a left turn and `0` at a straight step.

Formalized by `StatMech.Onsager.MasterCorner.cornerWeight_master`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CornerWeights.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CornerWeights.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#corner-weight-master).

## Corner defect of the interior is the number of left turns up to sign

The corner defect of the interior equals `±cc d`, the sign given by the orientation of the
 walk.

Formalized by `StatMech.Onsager.MasterCorner.cornerDiff_eq_weight_mul_cc`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CornerWeights.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CornerWeights.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#corner-diff-eq-weight-mul-cc).

## Four left turns from a pinch-free interior of Euler characteristic 1

A simple closed walk without right turns whose interior is pinch-free with Euler characteristic
 `1` has four left turns.

Formalized by `StatMech.Onsager.MasterCorner.cc_eq_four`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CornerWeights.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CornerWeights.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#cc-eq-four).

## Vertex of a walk as a lattice site

The `i`-th vertex of the walk as a site of `ℤ²`.

Formalized by `StatMech.Onsager.JedBridge.posSite`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#pos-site).

## Vertices of a simple walk are distinct sites

The vertices of a simple walk are distinct sites.

Formalized by `StatMech.Onsager.JedBridge.posSite_injective`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#pos-site-injective).

## Each lattice step has $\ell^1$-length one

Each step has `ℓ¹`-length `1`.

Formalized by `StatMech.Onsager.JedBridge.stepOf_natAbs_sum`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#step-of-nat-abs-sum).

## Consecutive walk vertices are adjacent in the square lattice

Consecutive vertices of the walk are adjacent in the square lattice.

Formalized by `StatMech.Onsager.JedBridge.walk_isSub`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#walk-is-sub).

## Simple closed walk as an embedded cycle graph

A simple closed walk as a planar subgraph of `ℤ²`: the cycle graph `cycleGraph (m + 3)` embedded
 by its vertex positions.

Formalized by `StatMech.Onsager.JedBridge.walkSubgraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#walk-subgraph).

## A cycle graph has one connected component

A cycle graph has one connected component. A specialization of
 `SimpleGraph.Preconnected.subsingleton_connectedComponent`.

Formalized by `StatMech.Onsager.JedBridge.cycleGraph_card_components_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#cycle-graph-card-components-one).

## Number of edges of a cycle graph

The cycle graph on `m + 3` vertices has `m + 3` edges.

Formalized by `StatMech.Onsager.JedBridge.cycleGraph_card_edges`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#cycle-graph-card-edges).

## Cycle graph has cycle rank one

The cycle graph has nullity (cycle rank) `1`.

Formalized by `StatMech.Onsager.JedBridge.cycle_nullity_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#cycle-nullity-one).

## Subgraph of a simple closed lattice walk has cycle rank one

The planar subgraph of a simple closed walk has nullity `1`.

Formalized by `StatMech.Onsager.JedBridge.walkSubgraph_nullity_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#walk-subgraph-nullity-one).

## Lattice Jordan curve theorem for simple closed walks

Lattice Jordan curve theorem for a simple closed walk: its complement in the face graph of `ℤ²`
 has exactly one bounded connected component.

Formalized by `StatMech.Onsager.JedBridge.walk_one_bounded_region`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#walk-one-bounded-region).

## Ray-parity interior equals the bounded face components

The ray-parity interior of the walk coincides with the union of bounded face components.

Formalized by `StatMech.Onsager.JedBridge.BridgeParityMembership`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#bridge-parity-membership).

## Face-graph adjacency as absence of a walk step between cells

Adjacency in the face graph of the walk is the absence of a walk step on the common side of two
 cells.

Formalized by `StatMech.Onsager.JedBridge.BridgeAdjacencyClimb`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkPlanarSubgraph.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-07/index.html#bridge-adjacency-climb).

## Unit cell as a face of the square lattice

The unit cell with lower-left corner `p`, viewed as a face of the square lattice, i.e. as the
 site `![p.1, p.2]` of the dual lattice.

Formalized by `StatMech.Onsager.WalkCellRegion.cellFace`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#cell-face).

## Simple closed walk as a planar subgraph

A simple closed walk as a planar subgraph of `ℤ²`.

Formalized by `StatMech.Onsager.WalkCellRegion.walkP`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#walk-p).

## Face graph of a closed walk

The face graph of the walk: adjacent faces of the square lattice whose common side is not an
 edge of the walk.

Formalized by `StatMech.Onsager.WalkCellRegion.walkRegionGraph`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#walk-region-graph).

## Each walk step is an edge of the image graph

Each step of the walk is an edge of its image graph.

Formalized by `StatMech.Onsager.WalkCellRegion.walkEdge_mem_imageGraph`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#walk-edge-mem-image-graph).

## Neighbours in the image graph are walk predecessor and successor

In the image graph of a simple closed walk, the neighbours of a vertex are its predecessor and
 successor on the walk.

Formalized by `StatMech.Onsager.WalkCellRegion.imageGraph_adj_pos_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#image-graph-adj-pos-iff).

## Horizontally face-adjacent cells have the same ray parity

Horizontally adjacent cells joined in the face graph have the same ray parity.

Formalized by `StatMech.Onsager.WalkCellRegion.rayParity_eq_of_faceAdj_right`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#ray-parity-eq-of-face-adj-right).

## Vertically face-adjacent cells have the same ray parity

Vertically adjacent cells joined in the face graph have the same ray parity.

Formalized by `StatMech.Onsager.WalkCellRegion.rayParity_eq_of_faceAdj_top`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#ray-parity-eq-of-face-adj-top).

## Face-adjacent cells have the same ray parity

Cells adjacent in the face graph have the same ray parity.

Formalized by `StatMech.Onsager.WalkCellRegion.rayParity_eq_of_faceAdj`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#ray-parity-eq-of-face-adj).

## Ray parity is constant on face-graph components

Ray parity is constant on connected components of the face graph.

Formalized by `StatMech.Onsager.WalkCellRegion.rayParity_eq_of_reachable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#ray-parity-eq-of-reachable).

## Top corner with an inside cell below it

A vertex `M` at which the walk turns from north to west and whose below-left cell is inside
 (chosen from `StatMech.Onsager.InsideConnected.lexmax_corner_cell_inside`).

Formalized by `StatMech.Onsager.WalkCellRegion.lexInteriorIndex`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#lex-interior-index).

## Defining property of the inside top corner

The defining property of `lexInteriorIndex`.

Formalized by `StatMech.Onsager.WalkCellRegion.lexInteriorIndex_spec`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#lex-interior-index-spec).

## Face below-left of the inside top corner

The face of the cell below-left of the corner `lexInteriorIndex`.

Formalized by `StatMech.Onsager.WalkCellRegion.lexInteriorFace`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#lex-interior-face).

## The face below the inside top corner is inside

The face `lexInteriorFace` is inside the walk.

Formalized by `StatMech.Onsager.WalkCellRegion.lexInteriorFace_parity`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#lex-interior-face-parity).

## Inner component of the face graph

The connected component of the face graph containing `lexInteriorFace`.

Formalized by `StatMech.Onsager.WalkCellRegion.innerComponent`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#inner-component).

## A face far outside the walk has ray parity zero

A face far outside the bounding box of the walk has ray parity `0`.

Formalized by `StatMech.Onsager.WalkCellRegion.outerBeacon_parity`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#outer-beacon-parity).

## The inner face component is finite

The component `innerComponent` is bounded.

Formalized by `StatMech.Onsager.WalkCellRegion.innerComponent_finite`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#inner-component-finite).

## Cells of the inner face component

The cells whose faces lie in `innerComponent`.

Formalized by `StatMech.Onsager.WalkCellRegion.componentCellSet`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#component-cell-set).

## The inner component has finitely many cells

There are finitely many such cells.

Formalized by `StatMech.Onsager.WalkCellRegion.componentCellSet_finite`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#component-cell-set-finite).

## Cells of the bounded face of a simple closed walk

The cells of the bounded face of a simple closed walk without right turns. See also
 `StatMech.Onsager.InteriorCells.interiorCells`, the ray-parity interior; they agree by
 `mem_interiorCells_iff_rayParity`.

Formalized by `StatMech.Onsager.WalkCellRegion.interiorCells`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#interior-cells).

## Membership in the bounded face

Membership in the bounded face.

Formalized by `StatMech.Onsager.WalkCellRegion.mem_interiorCells`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-08/index.html#mem-interior-cells).

## Lattice Jordan curve theorem, even-odd form

Lattice Jordan curve theorem, even-odd form: a cell lies in the bounded face of a simple closed
 walk without right turns iff its ray parity is `1`.

Formalized by `StatMech.Onsager.WalkCellRegion.mem_interiorCells_iff_rayParity`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellRegion.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#mem-interior-cells-iff-ray-parity).

## Face-graph component of an interior cell

The connected component of the walk's face graph containing an interior cell.

Formalized by `StatMech.Onsager.GeneralInterior.oddComponent`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LatticePolygonInterior.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LatticePolygonInterior.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#odd-component).

## A side between interior and exterior cells is a walk edge

A side shared by an interior and an exterior cell is an edge of the walk.

Formalized by `StatMech.Onsager.WalkCellLocal.sharedPrimalEdge_mem_of_membership_diff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellLocal.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellLocal.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#shared-primal-edge-mem-of-membership-dif).

## Three walk edges cannot meet at a vertex

Three walk edges cannot meet at one vertex of a simple closed walk.

Formalized by `StatMech.Onsager.WalkCellLocal.pinch_four_edges_impossible`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellLocal.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellLocal.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#pinch-four-edges-impossible).

## Bounded face of a simple closed walk has no pinch points

The bounded face of the walk has no pinch points.

Formalized by `StatMech.Onsager.WalkCellLocal.not_pinchAt_interiorCells`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellLocal.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellLocal.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#not-pinch-at-interior-cells).

## Pinch count of the bounded face is zero

The bounded face of the walk has pinch count `0`. See also
 `StatMech.Onsager.PinchFree.pinchCount_eq_zero`.

Formalized by `StatMech.Onsager.WalkCellLocal.pinchCount_interiorCells_eq_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellLocal.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellLocal.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#pinch-count-interior-cells-eq-zero).

## Cell to the left of a walk step

The cell to the left of step `k` of the walk. See also `StatMech.Onsager.Orientation.leftCell`;
 they agree by `StatMech.Onsager.UmlaufsatzFinal.leftCell_bridge`.

Formalized by `StatMech.Onsager.WalkCellBoundary.leftCell`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#left-cell).

## Cell to the right of a walk step

The cell to the right of step `k` of the walk.

Formalized by `StatMech.Onsager.WalkCellBoundary.rightCell`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#right-cell).

## Vertices of a walk's image graph are adjacent only to walk neighbours

In the image graph of a simple closed walk, a vertex is adjacent only to its walk neighbours.

Formalized by `StatMech.Onsager.WalkCellBoundary.imageGraph_not_adj_of_neighbours`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#image-graph-not-adj-of-neighbours).

## Consecutive left cells on a straight step are face-adjacent

Going straight, consecutive left cells are adjacent in the face graph of the walk.

Formalized by `StatMech.Onsager.WalkCellBoundary.leftCell_faceAdj_of_straight`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#left-cell-face-adj-of-straight).

## Consecutive left cells have the same ray parity

Consecutive left cells of a simple closed walk without right turns have the same ray parity.

Formalized by `StatMech.Onsager.WalkCellBoundary.leftCell_parity_succ`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#left-cell-parity-succ).

## All left cells have the same ray parity

All left cells of a simple closed walk without right turns have the same ray parity.

Formalized by `StatMech.Onsager.WalkCellBoundary.leftCell_parity_eq_of_reachable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#left-cell-parity-eq-of-reachable).

## Every left cell has ray parity one

Every left cell of a simple closed walk without right turns is inside.

Formalized by `StatMech.Onsager.WalkCellBoundary.leftCell_parity_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#left-cell-parity-one).

## Every left cell lies in the bounded face

Every left cell of a simple closed walk without right turns lies in the bounded face.

Formalized by `StatMech.Onsager.WalkCellBoundary.leftCell_mem_interiorCells`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#left-cell-mem-interior-cells).

## Cells on either side of a step lie in different faces

The two cells on either side of a walk step are in different face components.

Formalized by `StatMech.Onsager.WalkCellBoundary.walkRegion_flanking_not_reachable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#walk-region-flanking-not-reachable).

## Left and right cells of a step share that step

The left and right cells of a step are adjacent faces sharing that step.

Formalized by `StatMech.Onsager.WalkCellBoundary.left_right_flanking`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#left-right-flanking).

## No right cell lies in the bounded face

No right cell of a simple closed walk without right turns lies in the bounded face.

Formalized by `StatMech.Onsager.WalkCellBoundary.rightCell_not_mem_interiorCells`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#right-cell-not-mem-interior-cells).

## Corner count as a sum of four indicators

The corner count at `v` as a sum of four indicators. See also
 `StatMech.Onsager.CellEuler.cornerCount_eq_inter`.

Formalized by `StatMech.Onsager.WalkCellBoundary.cornerCount_eq_indicators`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#corner-count-eq-indicators).

## Corner count of the bounded face at a walk vertex

At the vertex after step `k`, the bounded face has one cell after a left turn and two after a
 straight step.

Formalized by `StatMech.Onsager.WalkCellBoundary.cornerCount_at_walkVertex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#corner-count-at-walk-vertex).

## Zero corner weight of the bounded face off the walk

Points off the walk have corner weight `0` for the bounded face.

Formalized by `StatMech.Onsager.WalkCellBoundary.cornerWeight_zero_of_not_walkVertex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-09/index.html#corner-weight-zero-of-not-walk-vertex).

## Corner weight of the bounded face at a walk vertex

The corner weight of the bounded face at the vertex after step `k` is `1` after a left turn and
 `0` after a straight step.

Formalized by `StatMech.Onsager.WalkCellBoundary.cornerWeight_at_walkVertex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#corner-weight-at-walk-vertex).

## Corner defect of the bounded face equals the number of left turns

The corner defect of the bounded face of a simple closed walk without right turns equals its
 number of left turns.

Formalized by `StatMech.Onsager.WalkCellBoundary.cornerDiff_interiorCells_eq_cc`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/WalkCellBoundary.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#corner-diff-interior-cells-eq-cc).

## 1-skeleton of a cell complex

The 1-skeleton of the cell complex `S`: vertices are the corners of cells, edges the sides of
 cells.

Formalized by `StatMech.Onsager.CellEulerFaithful.cellSkeleton`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#cell-skeleton).

## 1-skeleton of a cell complex as a planar subgraph

The 1-skeleton of `S` as a planar subgraph of `ℤ²`.

Formalized by `StatMech.Onsager.CellEulerFaithful.cellSkeletonP`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#cell-skeleton-p).

## Cell complex edges lie in the embedded skeleton

An edge of the cell complex is an edge of the embedded skeleton.

Formalized by `StatMech.Onsager.CellEulerFaithful.regEdge_mem_imageGraph`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#reg-edge-mem-image-graph).

## Shared side of a cell and an adjacent face is an edge

The side shared by a cell of `S` and an adjacent face is an edge of `S`.

Formalized by `StatMech.Onsager.CellEulerFaithful.sharedPrimalEdge_mem_regEdges`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#shared-primal-edge-mem-reg-edges).

## The face of a cell is enclosed on all four sides

The face of a cell of `S` is enclosed by the skeleton on all four sides.

Formalized by `StatMech.Onsager.CellEulerFaithful.occupiedFace_isolated`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#occupied-face-isolated).

## Face component containing a cell

The face component of the skeleton containing the cell `c`.

Formalized by `StatMech.Onsager.CellEulerFaithful.occupiedComponent`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#occupied-component).

## The face of a cell is alone in its component

The face of a cell of `S` is alone in its face component.

Formalized by `StatMech.Onsager.CellEulerFaithful.occupiedFace_reachable_eq`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#occupied-face-reachable-eq).

## The face component of a cell is bounded

The face component of a cell of `S` is bounded.

Formalized by `StatMech.Onsager.CellEulerFaithful.occupiedComponent_finite`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#occupied-component-finite).

## Bounded face formed by a cell

The bounded face of the skeleton formed by a cell of `S`.

Formalized by `StatMech.Onsager.CellEulerFaithful.occupiedBoundedFace`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#occupied-bounded-face).

## Distinct cells form distinct bounded faces

Distinct cells form distinct bounded faces.

Formalized by `StatMech.Onsager.CellEulerFaithful.occupiedBoundedFace_injective`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#occupied-bounded-face-injective).

## Number of cells is at most the nullity of the skeleton

The number of cells is at most the nullity of the skeleton.

Formalized by `StatMech.Onsager.CellEulerFaithful.card_le_cellSkeleton_nullity`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#card-le-cell-skeleton-nullity).

## Edges of the skeleton are the edges of the cell complex

The edges of `cellSkeleton S` are the edges of the cell complex `S`.

Formalized by `StatMech.Onsager.CellEulerFaithful.cellSkeletonEdgeEquiv`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#cell-skeleton-edge-equiv).

## Vertex count of the skeleton

The skeleton has `(regVerts S).card` vertices.

Formalized by `StatMech.Onsager.CellEulerFaithful.card_cellSkeleton_vertices`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#card-cell-skeleton-vertices).

## Euler characteristic at most 1 for a connected skeleton

If the 1-skeleton of `S` is connected, then `eulerChar S ≤ 1`. See also
 `StatMech.Onsager.CellEulerBound.eulerChar_le_one`.

Formalized by `StatMech.Onsager.CellEulerFaithful.eulerChar_le_one_of_skeleton_connected`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#euler-char-le-one-of-skeleton-connected).

## Corner of a cell as a skeleton vertex

A corner of a cell of `S`, as a vertex of the skeleton.

Formalized by `StatMech.Onsager.CellEulerFaithful.skeletonVertexOfCorner`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#skeleton-vertex-of-corner).

## Cell corners are connected to the lower-left corner

Every corner of a cell is connected in the skeleton to its lower-left corner.

Formalized by `StatMech.Onsager.CellEulerFaithful.corner_reachable_lowerLeft`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#corner-reachable-lower-left).

## Adjacent cells have connected lower-left corners

The lower-left corners of two adjacent cells of `S` are connected in the skeleton.

Formalized by `StatMech.Onsager.CellEulerFaithful.cell_representatives_reachable_of_adj`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#cell-representatives-reachable-of-adj).

## Lower-left corner of a cell as a skeleton vertex

The lower-left corner of a cell of `S`, as a vertex of the skeleton.

Formalized by `StatMech.Onsager.CellEulerFaithful.skeletonRepresentative`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-10/index.html#skeleton-representative).

## Interior cells have connected lower-left corners

Any two interior cells of a simple closed walk without right turns have skeleton-connected
 lower-left corners.

Formalized by `StatMech.Onsager.CellEulerFaithful.interior_representatives_reachable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#interior-representatives-reachable).

## Connectedness of the skeleton of the interior

The skeleton of the interior of a simple closed walk without right turns is connected.

Formalized by `StatMech.Onsager.CellEulerFaithful.interior_cellSkeleton_connected`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#interior-cell-skeleton-connected).

## Interior of a simple closed walk has Euler characteristic at most 1

The interior of a simple closed walk without right turns has Euler characteristic at most
 `1`.

Formalized by `StatMech.Onsager.CellEulerFaithful.eulerChar_interiorCells_le_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/InteriorEulerBound.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#euler-char-interior-cells-le-one).

## Hopf's Umlaufsatz

**Hopf's Umlaufsatz** for lattice polygons. A simple closed walk in `ℤ²` with at least three
steps and no U-turns has total turning `±4` quarter turns, that is rotation index `±1` (H. Hopf,
*Über die Drehung der Tangenten und Sehnen ebener Kurven*, 1935).

Formalized by `StatMech.Onsager.GeneralUmlaufsatz.turnSum_eq_four_or_neg_four`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LatticeUmlaufsatz.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/LatticeUmlaufsatz.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#turn-sum-eq-four-or-neg-four).

## Agreement of the two definitions of the left cell

The two descriptions of the cell to the left of a step agree.

Formalized by `StatMech.Onsager.UmlaufsatzFinal.leftCell_bridge`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#left-cell-bridge).

## A walk without right turns is positively oriented

The cell to the left of the first step is inside: the walk is positively oriented.

Formalized by `StatMech.Onsager.UmlaufsatzFinal.leftParity_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#left-parity-zero).

## Ray-parity interior equals the bounded face

The ray-parity interior of a simple closed walk without right turns equals its bounded face.

Formalized by `StatMech.Onsager.UmlaufsatzFinal.interiorCells_bridge`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#interior-cells-bridge).

## Discrete Umlaufsatz for walks of length at least three, shifted form

The discrete Umlaufsatz for walks of length `m + 3` without right turns.

Formalized by `StatMech.Onsager.UmlaufsatzFinal.cc_eq_four'`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#cc-eq-four).

## Discrete Umlaufsatz for walks of length at least three

The discrete Umlaufsatz for walks of length at least `3` without right turns.

Formalized by `StatMech.Onsager.UmlaufsatzFinal.cc_eq_four`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#cc-eq-four-2).

## A closed walk without right turns has length at least three

A closed walk without right turns or reversals has length at least `3`.

Formalized by `StatMech.Onsager.UmlaufsatzFinal.three_le_n`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#three-le-n).

## Discrete Umlaufsatz for lattice walks without right turns

Discrete Umlaufsatz (theorem of turning tangents) for lattice walks without right turns: a
 simple closed walk on `ℤ²` whose every turn is straight or a left quarter turn has exactly four
 left turns, i.e. its direction makes one full counterclockwise revolution. Right turns and
 reversals are excluded by hypothesis, so the walks covered are exactly counterclockwise
 boundaries of lattice rectangles (no reflex corner); the general signed statement is
 `StatMech.Onsager.GeneralUmlaufsatz.turnSum_eq_four_or_neg_four`. Compare H. Hopf, *Über die
 Drehung der Tangenten und Sehnen ebener Kurven*, Compositio Math. 2 (1935), for smooth curves.

Formalized by `StatMech.Onsager.UmlaufsatzFinal.cc_eq_four_of_no_right_turn`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#cc-eq-four-of-no-right-turn).

## A simple closed walk without right turns has under eight left turns

The hypothesis of `StatMech.Onsager.BaseCase.base_cc_eq_four` holds: a simple closed walk
 without right turns has fewer than eight left turns.

Formalized by `StatMech.Onsager.UmlaufsatzFinal.hnodbl_discharged`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/Umlaufsatz.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/part-11/index.html#hnodbl-discharged).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hopf's Umlaufsatz for lattice polygons](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/hopf-s-umlaufsatz-for-lattice-polygons)
