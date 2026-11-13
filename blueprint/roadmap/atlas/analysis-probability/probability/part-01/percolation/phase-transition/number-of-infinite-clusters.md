---
declaration: section
origin: cited
lean: StatMech.ConfigSpace.ergodic_ae_const_of_shiftInvariant, StatMech.Percolation.translateHom, StatMech.Percolation.translateHomInv, StatMech.Percolation.infiniteClusters, StatMech.Percolation.numInfiniteClusters, StatMech.Percolation.measurableSet_crossingEvent, StatMech.Percolation.repSet, StatMech.Percolation.numInfiniteClusters_ae_const
statement: formalized
proof: formalized
---

# Number of infinite clusters

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html).

## Shift-invariant countably valued functions are a.s. constant under ergodicity

A measurable function with countable values that is invariant under all shifts is almost
surely constant under an ergodic probability measure. See also Mathlib's `ErgodicSMul` and
`aeconst_of_forall_preimage_smul_ae_eq`, which state ergodicity of a group action through
a.e.-invariant sets.

Formalized by `StatMech.ConfigSpace.ergodic_ae_const_of_shiftInvariant`, a theorem declared in [MathlibExt/Probability/Percolation/InfiniteClusterCount.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/InfiniteClusterCount.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#ergodic-ae-const-of-shift-invariant).

## Translation of the open subgraph as a graph homomorphism

Translation by `g` as a graph homomorphism between the open subgraphs of `ω` and of its
shift.

Formalized by `StatMech.Percolation.translateHom`, a definition declared in [MathlibExt/Probability/Percolation/InfiniteClusterCount.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/InfiniteClusterCount.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#translate-hom).

## Inverse translation of the open subgraph

The inverse of `translateHom`.

Formalized by `StatMech.Percolation.translateHomInv`, a definition declared in [MathlibExt/Probability/Percolation/InfiniteClusterCount.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/InfiniteClusterCount.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#translate-hom-inv).

## Set of infinite open clusters

The set of infinite open clusters of `ω`.

Formalized by `StatMech.Percolation.infiniteClusters`, a definition declared in [MathlibExt/Probability/Percolation/InfiniteClusterCount.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/InfiniteClusterCount.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#infinite-clusters).

## Number of infinite open clusters

The number `N(ω) ∈ ℕ∞` of infinite open clusters of `ω`.

Formalized by `StatMech.Percolation.numInfiniteClusters`, a definition declared in [MathlibExt/Probability/Percolation/InfiniteClusterCount.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/InfiniteClusterCount.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#num-infinite-clusters).

## Measurability of the one-arm event

The one-arm event `crossingEvent d n` (the origin is connected to a site outside
`box d (n - 1)`) is measurable.

Formalized by `StatMech.Percolation.measurableSet_crossingEvent`, a theorem declared in [MathlibExt/Probability/Percolation/InfiniteClusterCount.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/InfiniteClusterCount.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#measurable-set-crossing-event).

## Representative sites of the infinite clusters

The set of sites `x` in an infinite cluster that are the `Encodable`-least site of their
cluster (one representative per infinite cluster).

Formalized by `StatMech.Percolation.repSet`, a definition declared in [MathlibExt/Probability/Percolation/InfiniteClusterCount.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/InfiniteClusterCount.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#rep-set).

## Number of infinite clusters is almost surely constant

The number of infinite clusters is almost surely constant (Newman–Schulman 1981) for any
translation-ergodic probability measure on bond configurations of `ℤ^d`.

Formalized by `StatMech.Percolation.numInfiniteClusters_ae_const`, a theorem declared in [MathlibExt/Probability/Percolation/InfiniteClusterCount.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/InfiniteClusterCount.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#num-infinite-clusters-ae-const).

## Event of at least two infinite open clusters

The event that there are at least two infinite open clusters.

Formalized by `StatMech.Percolation.atLeastTwoInfinite`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneErgodic.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneErgodic.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#at-least-two-infinite).

## Configuration with a finite edge set forced open

The configuration obtained from `ω` by opening every edge of `F`.

Formalized by `StatMech.Percolation.forceOpenFinset`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneMerge.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneMerge.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#force-open-finset).

## Endpoints of a finite edge set

The endpoints of the edges of `F`.

Formalized by `StatMech.Percolation.anchorSites`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneMerge.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneMerge.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#anchor-sites).

## Configurations with $k$ infinite clusters, two merged by opening $F$

Configurations with exactly `k` infinite clusters in which opening `F` connects two distinct
infinite clusters.

Formalized by `StatMech.Percolation.MergeWitness`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneMerge.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneMerge.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#merge-witness).

## Finite energy for opening finite edge sets

Finite energy for opening edges: for every finite edge set `F`, the law of
`forceOpenFinset F ω` is absolutely continuous with respect to `μ`.

Formalized by `StatMech.Percolation.HasFiniteEnergyMerge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneMerge.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneMerge.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#has-finite-energy-merge).

## Zero or one infinite cluster, given ergodicity and $\mu(N \ge 2) = 0$

For an ergodic measure with `μ(N ≥ 2) = 0`, either a.s. `N = 0` or a.s. `N = 1`.

Formalized by `StatMech.Percolation.numInfiniteClusters_zero_or_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneZeroOrOne.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneZeroOrOne.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html#num-infinite-clusters-zero-or-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Number of infinite clusters](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/phase-transition/number-of-infinite-clusters)
