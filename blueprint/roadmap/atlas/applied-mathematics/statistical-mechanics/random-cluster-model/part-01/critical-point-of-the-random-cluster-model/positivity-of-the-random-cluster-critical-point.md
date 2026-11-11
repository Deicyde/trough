---
declaration: section
origin: cited
lean: StatMech.FK.openGraph_mono, StatMech.FK.wiredGraph_mono, StatMech.FK.numClustersWired_antitone, StatMech.FK.wiredFkWeight_edgeProduct_cross, StatMech.FK.wiredFkProb_fkProbOne_cross, StatMech.FK.wiredFkProb_le_fkProbOne_increasing, StatMech.FK.sum_prod_factor, StatMech.FK.fkProbOne_cylinder
statement: formalized
proof: formalized
---

# Positivity of the random-cluster critical point

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html).

## A. Domination of the wired measure by Bernoulli percolation

## Monotonicity of the open subgraph

The open subgraph is monotone in the configuration.

Formalized by `StatMech.FK.openGraph_mono`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#open-graph-mono).

## Monotonicity of the wired graph

The wired graph (open edges plus the boundary clique) is monotone in the configuration.

Formalized by `StatMech.FK.wiredGraph_mono`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#wired-graph-mono).

## Wired cluster count is antitone

The wired cluster count `k¹(ω)` is antitone in `ω`.

Formalized by `StatMech.FK.numClustersWired_antitone`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#num-clusters-wired-antitone).

## Holley cross inequality for wired and Bernoulli weights, $q \ge 1$

Holley cross inequality between the wired random-cluster weight and the Bernoulli product
weight, for `q ≥ 1`.

Formalized by `StatMech.FK.wiredFkWeight_edgeProduct_cross`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#wired-fk-weight-edge-product-cross).

## Holley cross inequality for wired and $q = 1$ laws, $q \ge 1$

Holley cross inequality between the ambient wired probability and the ambient `q = 1`
law, for `q ≥ 1`. The latter is Bernoulli-`p` only on the graph-edge marginal.

Formalized by `StatMech.FK.wiredFkProb_fkProbOne_cross`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#wired-fk-prob-fk-prob-one-cross).

## Wired law at most the $q = 1$ law on increasing events, $q \ge 1$

For `q ≥ 1`, the ambient wired law is dominated by `fkProb G p 1` on increasing events.
The latter is Bernoulli-`p` on graph edges and uniform on loops and nonedges; the comparison
with ordinary Bernoulli percolation therefore applies to graph-edge events.

Formalized by `StatMech.FK.wiredFkProb_le_fkProbOne_increasing`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#wired-fk-prob-le-fk-prob-one-increasing).

## Boolean-configuration sum of a coordinatewise product factorizes

Summing a product of single-coordinate factors over all Boolean configurations: coordinates
outside `s` contribute a factor `2` each.

Formalized by `StatMech.FK.sum_prod_factor`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#sum-prod-factor).

## Bernoulli probability that edges $F$ are all open is $p^{|F|}$

Under Bernoulli percolation on a finite graph, a set `F` of edges is open with probability
`p^|F|`.

Formalized by `StatMech.FK.fkProbOne_cylinder`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#fk-prob-one-cylinder).

## Padding a finite lattice word to an infinite word

Extend a word of `m` lattice steps to an infinite word by a fixed padding step.

Formalized by `StatMech.FK.fkExtWord`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#fk-ext-word).

## Event of an open self-avoiding walk of $m$ steps

The event that some self-avoiding walk of `m` steps from the origin is open.

Formalized by `StatMech.FK.fkExistsOpenWalk`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#fk-exists-open-walk).

## Single-edge open event is clopen

The event that a given edge is open is clopen.

Formalized by `StatMech.FK.isClopen_singleOpen`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#is-clopen-single-open).

## Event that a given walk is open is clopen

The event that a given walk is open is clopen.

Formalized by `StatMech.FK.isClopen_wordEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#is-clopen-word-event).

## Event that a given walk is open is increasing

The event that a given walk is open is increasing.

Formalized by `StatMech.FK.isIncreasing_wordEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#is-increasing-word-event).

## Event of some open self-avoiding walk is clopen

The open-walk event is clopen.

Formalized by `StatMech.FK.isClopen_fkExistsOpenWalk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#is-clopen-fk-exists-open-walk).

## Event of some open self-avoiding walk is increasing

The open-walk event is increasing.

Formalized by `StatMech.FK.isIncreasing_fkExistsOpenWalk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#is-increasing-fk-exists-open-walk).

## Percolation gives open self-avoiding walks of every length

Percolation from the origin implies an open self-avoiding walk of every length `m`.

Formalized by `StatMech.FK.percolationEvent_subset_fkExistsOpenWalk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#percolation-event-subset-fk-exists-open).

## Extended box configuration keeps box edge states

Extending a box configuration to `ℤ^d` keeps the state of box edges.

Formalized by `StatMech.FK.extendEdge_eq_of_range`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#extend-edge-eq-of-range).

## Open edges of an extended box configuration are box edges

An edge that is open in an extended box configuration is a box edge.

Formalized by `StatMech.FK.range_of_extendEdge_true`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#range-of-extend-edge-true).

## Box edge with a lattice-edge image is a box-graph edge

A box edge whose image is a lattice edge is an edge of the box graph.

Formalized by `StatMech.FK.boxEdge_mem`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#box-edge-mem).

## Open self-avoiding walk in a box gives $m$ distinct open box edges

An open self-avoiding walk of `m` steps that lies in the box gives `m` distinct box edges that
are all open.

Formalized by `StatMech.FK.exists_boxF`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#exists-box-f).

## Bernoulli bound $p^m$ for a fixed self-avoiding walk in the box

Under Bernoulli percolation on the box, a fixed self-avoiding walk of `m` steps is open with
probability at most `p^m`.

Formalized by `StatMech.FK.perWord_box_bound`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#per-word-box-bound).

## Wired box measure as a finite sum over box configurations

The wired box measure of an event, as a finite sum over box configurations.

Formalized by `StatMech.FK.wiredFiniteMeasure_real_eq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#wired-finite-measure-real-eq).

## Wired box bound $(2dp)^m$ on the open-walk event for $q \ge 1$

For `q ≥ 1`, the wired box measure of the open-walk event is at most `(2dp)^m`.

Formalized by `StatMech.FK.wiredFiniteMeasure_fkExistsOpenWalk_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#wired-finite-measure-fk-exists-open-walk).

## Wired percolation bound $\theta^1(p, q) \le (2dp)^m$ for $q \ge 1$

For `q ≥ 1`, the wired percolation probability satisfies `θ¹(p, q) ≤ (2dp)^m` for every `m`.

Formalized by `StatMech.FK.fkTheta_le_pow`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#fk-theta-le-pow).

## No wired percolation for $2dp < 1$ and $q \ge 1$

For `q ≥ 1` and `2dp < 1`, there is no percolation in the wired measure: `θ¹(p, q) = 0`.

Formalized by `StatMech.FK.fkTheta_eq_zero_of_lt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#fk-theta-eq-zero-of-lt).

## Subcritical set is bounded above by one

The set of `p` with `θ¹(p, q) = 0` is bounded above by `1`.

Formalized by `StatMech.FK.fkSubcriticalSet_bddAbove`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#fk-subcritical-set-bdd-above).

## Subcritical parameters are at most the critical point

Every subcritical `p` is at most `p_c(q, d)`.

Formalized by `StatMech.FK.le_fkPc_of_mem`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#le-fk-pc-of-mem).

## Positivity of the random-cluster critical point

For `d ≥ 1` and `q ≥ 1`,
`0 < p_c(q, d)`; in fact `p_c(q, d) ≥ 1 / (4d)`.

Reference: G. Grimmett, *The Random-Cluster Model*, Springer (2006), Section 5.1.

Formalized by `StatMech.FK.fkPc_pos`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 564](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#fk-pc-pos).

## Positive random-cluster critical point for $d \ge 2$, $q \ge 1$

`fkPc_pos` for `d ≥ 2`.

Formalized by `StatMech.FK.fkPc_pos_of_two_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/PcNontrivial.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html#fk-pc-pos-of-two-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Positivity of the random-cluster critical point](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/critical-point-of-the-random-cluster-model/positivity-of-the-random-cluster-critical-point)
