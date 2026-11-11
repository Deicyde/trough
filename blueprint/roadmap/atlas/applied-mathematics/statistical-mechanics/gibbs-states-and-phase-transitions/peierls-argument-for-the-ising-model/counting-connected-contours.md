---
declaration: section
origin: cited
lean: StatMech.Ising.pcc_pairCluster, StatMech.Ising.latticeOn, StatMech.Ising.IsConnectedCluster, StatMech.Ising.connClusterFamily, StatMech.Ising.ConnectedContourCountBound
statement: formalized
proof: formalized
---

# Counting connected contours

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/counting-connected-contours/index.html).

## A. Failure of the origin bound

## Two-site set $\{0, p\}$

The two-site set `{0, p}`.

Formalized by `StatMech.Ising.pcc_pairCluster`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/counting-connected-contours/index.html#pcc-pair-cluster).

## Nearest-neighbour graph restricted to a set

The nearest-neighbour graph restricted to `K`.

Formalized by `StatMech.Ising.latticeOn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/counting-connected-contours/index.html#lattice-on).

## Connected cluster through the origin in the nearest-neighbour graph

`K` is connected in the nearest-neighbour graph.

Formalized by `StatMech.Ising.IsConnectedCluster`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/counting-connected-contours/index.html#is-connected-cluster).

## Connected clusters in the box containing the origin

The connected finite sets of sites in `Λ_n` containing the origin.

Formalized by `StatMech.Ising.connClusterFamily`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/counting-connected-contours/index.html#conn-cluster-family).

## Peierls series bound on the connected-cluster contour sum

The sum of `e^{-2β |∂K|}` over connected clusters is at most the Peierls series.

Formalized by `StatMech.Ising.ConnectedContourCountBound`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsContourCount.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/counting-connected-contours/index.html#connected-contour-count-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting connected contours](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/counting-connected-contours/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/counting-connected-contours)
