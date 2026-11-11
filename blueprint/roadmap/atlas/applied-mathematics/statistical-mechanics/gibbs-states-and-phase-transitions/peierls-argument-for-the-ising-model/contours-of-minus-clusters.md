---
declaration: section
origin: cited
lean: StatMech.Ising.flipOnSet, StatMech.Ising.crosses, StatMech.Ising.crossEdges, StatMech.Ising.contourLen, StatMech.Ising.crossEdgeBond, StatMech.Ising.ContourEvent, StatMech.Ising.flipInteriorOn, StatMech.Ising.flipInteriorOnEquiv
statement: formalized
proof: formalized
---

# Contours of minus clusters

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html).

## A. Flipping a set

## Configuration with the spins in a set flipped

The configuration with the spins in `K` flipped.

Formalized by `StatMech.Ising.flipOnSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#flip-on-set).

## Bond crossing the boundary of a set

The bond `e` has exactly one endpoint in `K`.

Formalized by `StatMech.Ising.crosses`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#crosses).

## Contour of a set: bonds crossing its boundary

The bonds of `B` crossing the boundary of `K` (the contour of `K`).

Formalized by `StatMech.Ising.crossEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#cross-edges).

## Contour length of a set

The number of bonds of `B` crossing the boundary of `K`.

Formalized by `StatMech.Ising.contourLen`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#contour-len).

## Bond variable of a crossing bond

The bond variable of a crossing bond.

Formalized by `StatMech.Ising.crossEdgeBond`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#cross-edge-bond).

## Contour event of a set: opposite spins across every crossing bond

Every bond of `B` crossing the boundary of `K` joins a minus spin inside to a plus spin
outside.

Formalized by `StatMech.Ising.ContourEvent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#contour-event).

## Inside configuration with the spins in a set flipped

The inside configuration with the spins in `K` flipped.

Formalized by `StatMech.Ising.flipInteriorOn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#flip-interior-on).

## Flipping spins in a set as an involutive equivalence

Flipping the spins in `K` as an involutive equivalence of inside configurations.

Formalized by `StatMech.Ising.flipInteriorOnEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#flip-interior-on-equiv).

## Probability of the contour event of a set

The probability of the contour event of `K` under the box measure.

Formalized by `StatMech.Ising.probContour`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#prob-contour).

## Set of minus sites

The set of minus sites.

Formalized by `StatMech.Ising.minusSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#minus-set).

## Nearest-neighbour graph on the minus sites

The nearest-neighbour graph on the minus sites.

Formalized by `StatMech.Ising.minusGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#minus-graph).

## Minus cluster of a site

The minus cluster of `o`: the sites joined to `o` by a path of minus sites.

Formalized by `StatMech.Ising.minusCluster`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#minus-cluster).

## Cluster family: all subsets of the box

The finite sets of sites in `Λ_n` containing the origin.

Formalized by `StatMech.Ising.clusterFamily`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#cluster-family).

## Minus cluster of the origin as a finite set

The minus cluster of the origin in a plus-boundary box configuration, as a finset.

Formalized by `StatMech.Ising.minusClusterFinset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#minus-cluster-finset).

## Peierls series bound on the cluster-family contour sum

The sum of `e^{-2β |∂K|}` over the cluster family is at most the Peierls series.

Formalized by `StatMech.Ising.ContourCountBound`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContours.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html#contour-count-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Contours of minus clusters](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-minus-clusters)
