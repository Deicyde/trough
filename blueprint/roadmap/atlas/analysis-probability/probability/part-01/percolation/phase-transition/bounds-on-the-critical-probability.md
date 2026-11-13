---
declaration: section
origin: cited
lean: StatMech.Percolation.vertOf, StatMech.Percolation.edgeOf, StatMech.Percolation.wordEvent, StatMech.Percolation.goodWord, StatMech.Percolation.dirOf, StatMech.Percolation.pc_pos, StatMech.Percolation.pcUpperBound, StatMech.Percolation.pcRatio
statement: formalized
proof: formalized
---

# Bounds on the critical probability

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html).

## Vertices of a lattice path encoded by a step sequence

The `k`-th vertex of the lattice path from the origin that takes step `±e_i` given by `g j`
at time `j`.

Formalized by `StatMech.Percolation.vertOf`, a definition declared in [MathlibExt/Probability/Percolation/PcNontrivial.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcNontrivial.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#vert-of).

## Edges of a lattice path encoded by a step sequence

The `k`-th edge `{vertOf g k, vertOf g (k + 1)}` of the path encoded by `g`.

Formalized by `StatMech.Percolation.edgeOf`, a definition declared in [MathlibExt/Probability/Percolation/PcNontrivial.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcNontrivial.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#edge-of).

## Event that an encoded lattice path is open

The event that the first `n` edges of the path encoded by `g` are open.

Formalized by `StatMech.Percolation.wordEvent`, a definition declared in [MathlibExt/Probability/Percolation/PcNontrivial.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcNontrivial.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#word-event).

## Self-avoiding initial segment of an encoded lattice path

The first `n + 1` vertices of the path encoded by `g` are distinct.

Formalized by `StatMech.Percolation.goodWord`, a definition declared in [MathlibExt/Probability/Percolation/PcNontrivial.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcNontrivial.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#good-word).

## Step directions of an open walk from the origin

The direction `(i, ±)` of the `k`-th step of an open walk from the origin (arbitrary past its
end).

Formalized by `StatMech.Percolation.dirOf`, a definition declared in [MathlibExt/Probability/Percolation/PcNontrivial.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcNontrivial.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#dir-of).

## Positivity of the critical probability (Hammersley's bound)

`p_c(d) > 0` for bond percolation on `ℤ^d`, `d ≥ 1` (Hammersley 1957, by counting paths:
`p_c(d) ≥ 1/(2d)`).

Formalized by `StatMech.Percolation.pc_pos`, a theorem declared in [MathlibExt/Probability/Percolation/PcNontrivial.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcNontrivial.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-pos).

## Peierls series bounding closed dual circuits

The Peierls series `∑_ℓ ℓ 4^ℓ (1 - p)^ℓ` bounding the probability of a closed dual circuit
around the origin.

Formalized by `StatMech.Percolation.pcUpperBound`, a definition declared in [MathlibExt/Probability/Percolation/PcUpper.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpper.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-upper-bound).

## Geometric ratio of the Peierls series

The ratio `4(1 - p)` of the geometric part of `pcUpperBound`.

Formalized by `StatMech.Percolation.pcRatio`, a definition declared in [MathlibExt/Probability/Percolation/PcUpper.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpper.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-ratio).

## Peierls contour bound on the percolation probability

The Peierls contour bound `1 - θ_2(p) ≤ pcUpperBound p` at density `p`.

Formalized by `StatMech.Percolation.PcContourBound`, a definition declared in [MathlibExt/Probability/Percolation/PcUpper.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpper.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-contour-bound).

## $p_c(2) < 1$ from the Peierls contour bound

`p_c(2) < 1`, assuming the Peierls contour bound `PcContourBound` for all `p` above some
`p₀ < 1`.

Formalized by `StatMech.Percolation.pc_lt_one`, a theorem declared in [MathlibExt/Probability/Percolation/PcUpper.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpper.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-lt-one).

## Primal edges crossed by a dual walk

The set of primal edges crossed by the darts of a walk `c` in the dual (face) lattice.

Formalized by `StatMech.Percolation.primalEdgeFinset`, a definition declared in [MathlibExt/Probability/Percolation/PcUpperEnclosure.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpperEnclosure.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#primal-edge-finset).

## Event that a dual circuit is closed

The event that every primal edge crossed by the dual walk `c` is closed.

Formalized by `StatMech.Percolation.closedCircuitEvent`, a definition declared in [MathlibExt/Probability/Percolation/PcUpperEnclosure.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpperEnclosure.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#closed-circuit-event).

## Anchor sites for dual circuits

The `2ℓ` anchor sites `(j, 0)` and `(j, -1)`, `0 ≤ j < ℓ`.

Formalized by `StatMech.Percolation.anchorFinset`, a definition declared in [MathlibExt/Probability/Percolation/PcUpperEnclosure.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpperEnclosure.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#anchor-finset).

## Anchored dual cycles of a given length

The finite set of dual cycles of length `ℓ` based at an anchor site of `anchorFinset ℓ`.

Formalized by `StatMech.Percolation.cyclesAtLen`, a definition declared in [MathlibExt/Probability/Percolation/PcUpperEnclosure.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpperEnclosure.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#cycles-at-len).

## Summand of the anchored Peierls series

The summand `2ℓ · 4^ℓ · (1 - p)^ℓ`.

Formalized by `StatMech.Percolation.pcSummandTwo`, a definition declared in [MathlibExt/Probability/Percolation/PcUpperEnclosure.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpperEnclosure.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-summand-two).

## Anchored dual-circuit enclosure property

Every finite cluster of the origin is enclosed by a cycle of its face-boundary graph based at
an anchor site of `anchorFinset ℓ`, where `ℓ` is the cycle length.

Formalized by `StatMech.Percolation.PcAnchoredEnclosure`, a definition declared in [MathlibExt/Probability/Percolation/PcUpperEnclosure.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpperEnclosure.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-anchored-enclosure).

## $p_c(2) < 1$ from anchored dual-circuit enclosure

`p_c(2) < 1`, assuming the anchored enclosure property `PcAnchoredEnclosure`.

Formalized by `StatMech.Percolation.pc_lt_one_of_enclosure`, a theorem declared in [MathlibExt/Probability/Percolation/PcUpperEnclosure.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PcUpperEnclosure.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-lt-one-of-enclosure).

## Bernoulli product pulled back along an injection is Bernoulli

Pulling a Bernoulli product configuration back along an injective map `f : I → E` gives the
Bernoulli product measure on `I`. See also `MeasureTheory.Measure.infinitePi_map_restrict'` for
the case of a subset.

Formalized by `StatMech.FK.bernoulliProduct_map_injective_restrict`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#bernoulli-product-map-injective-restrict).

## $q = 1$ probability of an edge pattern is its Bernoulli weight

The `q = 1` random-cluster probability of a given pattern on the graph edges is its Bernoulli
weight.

Formalized by `StatMech.FK.fkProbOne_pattern`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#fk-prob-one-pattern).

## $q = 1$ measure equals Bernoulli percolation on graph-edge events

The `q = 1` random-cluster measure on a finite graph agrees with Bernoulli percolation on events
that depend only on the graph edges.

Formalized by `StatMech.FK.fkProbOne_event_eq_bernoulli`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#fk-prob-one-event-eq-bernoulli).

## Connection to the boundary depends only on graph edges

The event that `x` is connected to the boundary depends only on the graph edges.

Formalized by `StatMech.FK.connToBdryEvent_dependsOn`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#conn-to-bdry-event-depends-on).

## Bernoulli percolation restricted to a box is Bernoulli on the box

Restricting Bernoulli percolation on `ℤ^d` to the box gives Bernoulli percolation on the box.

Formalized by `StatMech.FK.bernoulliProduct_map_boxRestrict`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#bernoulli-product-map-box-restrict).

## Bernoulli box cylinder probability equals its probability on the box

The Bernoulli probability of a box cylinder event equals its probability on the box.

Formalized by `StatMech.FK.bernoulliProduct_boxRestrict_preimage`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#bernoulli-product-box-restrict-preimage).

## Wired $q = 2$ origin-to-boundary probability at most Bernoulli

The wired `q = 2` box measure of "the origin is connected to the box boundary" is at most its
Bernoulli probability.

Formalized by `StatMech.FK.wiredFinite_boxBdryConnEvent_le_bernoulli`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#wired-finite-box-bdry-conn-event-le-bern).

## Wired $q = 2$ percolation probability at most the Bernoulli one

The wired `q = 2` percolation probability is at most the Bernoulli one: `θ¹(p, 2) ≤ θ(p)`.

Formalized by `StatMech.FK.fkTheta_two_le_bernoulliTheta`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#fk-theta-two-le-bernoulli-theta).

## Plane embedding of $\mathbb{Z}^2$ into $\mathbb{Z}^{2+k}$

The embedding of `ℤ²` into `ℤ^{2+k}` as the plane of the first two coordinates.

Formalized by `StatMech.Percolation.pcv_siteEmbed`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-site-embed).

## First two coordinates of an embedded site are the original ones

The first two coordinates of an embedded site.

Formalized by `StatMech.Percolation.pcv_siteEmbed_castAdd`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-site-embed-cast-add).

## Last $k$ coordinates of an embedded site vanish

The last `k` coordinates of an embedded site vanish.

Formalized by `StatMech.Percolation.pcv_siteEmbed_natAdd`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-site-embed-nat-add).

## Injectivity of the plane embedding

The plane embedding is injective.

Formalized by `StatMech.Percolation.pcv_siteEmbed_injective`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-site-embed-injective).

## Plane embedding preserves and reflects adjacency

The plane embedding preserves and reflects lattice adjacency.

Formalized by `StatMech.Percolation.pcv_siteEmbed_adj_iff`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-site-embed-adj-iff).

## Plane embedding on edges

The plane embedding on edges.

Formalized by `StatMech.Percolation.pcv_edgeEmbed`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-edge-embed).

## Injectivity of the plane embedding on edges

The plane embedding on edges is injective.

Formalized by `StatMech.Percolation.pcv_edgeEmbed_injective`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-edge-embed-injective).

## Restriction of a configuration to the embedded plane

Restrict a configuration on `ℤ^{2+k}` to the embedded plane.

Formalized by `StatMech.Percolation.pcv_planeRestrict`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-plane-restrict).

## Bernoulli percolation restricted to the plane is planar Bernoulli

Restricting Bernoulli percolation on `ℤ^{2+k}` to the plane gives Bernoulli percolation on `ℤ²`.

Formalized by `StatMech.Percolation.bernoulliProduct_map_planeRestrict`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#bernoulli-product-map-plane-restrict).

## Plane embedding fixes the origin

The plane embedding sends the origin to the origin.

Formalized by `StatMech.Percolation.pcv_siteEmbed_origin`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-site-embed-origin).

## Plane open connections are open connections in $\mathbb{Z}^{2+k}$

Open connections in the restricted plane configuration are open connections in `ℤ^{2+k}`.

Formalized by `StatMech.Percolation.pcv_connected_of_planeRestrict`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-connected-of-plane-restrict).

## Percolation in the plane implies percolation in $\mathbb{Z}^{2+k}$

Percolation in the plane implies percolation in `ℤ^{2+k}`.

Formalized by `StatMech.Percolation.pcv_plane_percolation_subset`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pcv-plane-percolation-subset).

## $\theta_2(p) \le \theta_{2+k}(p)$ for Bernoulli percolation

The Bernoulli percolation probability does not decrease with the dimension: `θ_2(p) ≤
θ_{2+k}(p)`.

Formalized by `StatMech.Percolation.theta_two_le_theta_add`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#theta-two-le-theta-add).

## Monotonicity in $p$ of the Bernoulli percolation probability

The Bernoulli percolation probability `θ_d(p)` is monotone in `p`.

Formalized by `StatMech.Percolation.theta_mono_parameter`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#theta-mono-parameter).

## Positive percolation at $p$ gives $p_c(d) \le p$

Positive percolation probability at `p` gives `p_c(d) ≤ p`.

Formalized by `StatMech.Percolation.pc_le_of_theta_pos`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-le-of-theta-pos).

## Positive planar percolation at some $p < 1$ via the Ising model

There is `p < 1` with `θ_2(p) > 0`, from spontaneous magnetization of the two-dimensional Ising
model.

Formalized by `StatMech.Percolation.exists_theta_two_pos_below_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#exists-theta-two-pos-below-one).

## Bernoulli critical probability on $\mathbb{Z}^2$ is below one

The Bernoulli critical probability on `ℤ²` is below `1`.

Formalized by `StatMech.Percolation.pc_two_lt_one_via_fk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-two-lt-one-via-fk).

## Nontrivial Bernoulli critical probability on $\mathbb{Z}^2$

`0 < p_c(2) < 1`.

Formalized by `StatMech.Percolation.pc_two_nontrivial`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 541](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L541). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-two-nontrivial).

## Bernoulli critical probability below one for $d \ge 2$

The Bernoulli critical probability on `ℤ^d` is below `1` for `d ≥ 2`.

Formalized by `StatMech.Percolation.pc_lt_one_of_two_le_via_fk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-lt-one-of-two-le-via-fk).

## Non-triviality of the percolation critical probability

For Bernoulli bond percolation
on `ℤ^d` with `d ≥ 2`, `0 < p_c(d) < 1`.

Reference: S. R. Broadbent and J. M. Hammersley, *Percolation processes I*, Proc. Cambridge
Philos. Soc. 53 (1957); G. Grimmett, *Percolation*, 2nd ed. (1999), Theorem 1.10.

Formalized by `StatMech.Percolation.pc_nontrivial_of_two_le`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/PcUpperViaFK.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html#pc-nontrivial-of-two-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounds on the critical probability](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/phase-transition/bounds-on-the-critical-probability)
