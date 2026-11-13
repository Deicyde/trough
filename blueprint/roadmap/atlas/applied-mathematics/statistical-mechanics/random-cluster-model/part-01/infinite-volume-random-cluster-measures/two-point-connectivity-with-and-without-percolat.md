---
declaration: section
origin: cited
lean: StatMech.FK.infiniteTwoPointReal, StatMech.FK.clusterInfiniteEvent, StatMech.FK.two_infinite_clusters_of_not_connected, StatMech.FK.infinite_cluster_inter_le_twoPoint, StatMech.FK.infiniteTwoPoint_uniform_pos_of_fkg_unique, StatMech.FK.crossingEvent_real_tendsto_percolation, StatMech.FK.boxBdryConnEvent_real_tendsto_percolation, StatMech.FK.connectionEvent_subset_boxBdryConnEvent
statement: formalized
proof: formalized
---

# Two-point connectivity with and without percolation

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html).

## A. Two-point connectivity and infinite clusters

## Two-point connectivity of a bond measure on $\mathbb{Z}^d$

The two-point connectivity `μ(x ↔ y)` of a measure on bond configurations of `ℤ^d`.

Formalized by `StatMech.FK.infiniteTwoPointReal`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#infinite-two-point-real).

## Event that the open cluster of a site is infinite

The event `{x ↔ ∞}` that the open cluster of `x` is infinite.

Formalized by `StatMech.FK.clusterInfiniteEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#cluster-infinite-event).

## Disconnected sites in infinite clusters give two infinite clusters

If `x` and `y` both lie in infinite clusters, either they are connected or there are at least
two infinite clusters.

Formalized by `StatMech.FK.two_infinite_clusters_of_not_connected`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#two-infinite-clusters-of-not-connected).

## Joint percolation at most connectivity given no two infinite clusters

With at most one infinite cluster almost surely, `μ(x ↔ ∞, y ↔ ∞) ≤ μ(x ↔ y)`.

Formalized by `StatMech.FK.infinite_cluster_inter_le_twoPoint`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#infinite-cluster-inter-le-two-point).

## Two-point lower bound from FKG, invariance, uniqueness and percolation

If `μ` satisfies the FKG inequality for the events `{x ↔ ∞}` (`hPA`), is translation
invariant on them (`hTI`), has at most one infinite cluster almost surely (`huniq`), and
percolates (`htheta`), then `μ(0 ↔ x) ≥ θ²` for every `x`.

Formalized by `StatMech.FK.infiniteTwoPoint_uniform_pos_of_fkg_unique`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#infinite-two-point-uniform-pos-of-fkg-un).

## Crossing probabilities converge to the percolation probability

For any finite measure, the probability that the origin is connected to the complement of the
box of radius `n - 1` tends to the percolation probability.

Formalized by `StatMech.FK.crossingEvent_real_tendsto_percolation`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#crossing-event-real-tendsto-percolation).

## Box-boundary connection probability tends to percolation probability

For any finite measure, the probability that the origin is connected to the boundary of the box
of radius `n` inside the box tends to the percolation probability.

Formalized by `StatMech.FK.boxBdryConnEvent_real_tendsto_percolation`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#box-bdry-conn-event-real-tendsto-percola).

## A connection to outside the box passes through the box boundary

A connection from the origin to a site outside the box passes through the box boundary.

Formalized by `StatMech.FK.connectionEvent_subset_boxBdryConnEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#connection-event-subset-box-bdry-conn-ev).

## Uniform decay of two-point connectivity without percolation

Without percolation, the two-point connectivity from the origin tends to zero uniformly: for
every `ε > 0` there is `n` with `μ(0 ↔ x) < ε` for all `x` outside the box of radius `n`.

Formalized by `StatMech.FK.infiniteTwoPoint_uniform_decay_of_no_percolation`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/TwoPointConnectivity.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html#infinite-two-point-uniform-decay-of-no-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-point connectivity with and without percolation](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/two-point-connectivity-with-and-without-percolat)
