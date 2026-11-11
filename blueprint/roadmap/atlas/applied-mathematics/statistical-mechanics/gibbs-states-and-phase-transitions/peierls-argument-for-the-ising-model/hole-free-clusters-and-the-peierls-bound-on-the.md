---
declaration: section
origin: cited
lean: StatMech.Ising.OuterContourWinding, StatMech.Ising.IsHoleFreeBoxCluster, StatMech.Ising.holeFreeClusterFamily, StatMech.Ising.holeFreeAtLen
statement: formalized
proof: formalized
---

# Hole-free clusters and the Peierls bound on the square lattice

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/hole-free-clusters-and-the-peierls-bound-on-the/index.html).

## A. The winding hypothesis

## Winding hypothesis for outer contours on $\mathbb{Z}^2$

Every plus-boundary configuration on `Λ_n` with the origin minus has a connected contour
event through the origin whose boundary meets the positive axis within the contour length.

Formalized by `StatMech.Ising.OuterContourWinding`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsHoleFree.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsHoleFree.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/hole-free-clusters-and-the-peierls-bound-on-the/index.html#outer-contour-winding).

## Hole-free connected cluster through the origin

`K` is a connected cluster in `Λ_n` through the origin without holes.

Formalized by `StatMech.Ising.IsHoleFreeBoxCluster`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsHoleFree.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsHoleFree.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/hole-free-clusters-and-the-peierls-bound-on-the/index.html#is-hole-free-box-cluster).

## Hole-free clusters in the box through the origin

The hole-free clusters in `Λ_n` through the origin.

Formalized by `StatMech.Ising.holeFreeClusterFamily`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsHoleFree.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsHoleFree.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/hole-free-clusters-and-the-peierls-bound-on-the/index.html#hole-free-cluster-family).

## Hole-free clusters with contour length $\ell$

The hole-free clusters in `Λ_n` through the origin with contour length `ℓ`.

Formalized by `StatMech.Ising.holeFreeAtLen`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsHoleFree.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsHoleFree.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/hole-free-clusters-and-the-peierls-bound-on-the/index.html#hole-free-at-len).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hole-free clusters and the Peierls bound on the square lattice](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/hole-free-clusters-and-the-peierls-bound-on-the/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/hole-free-clusters-and-the-peierls-bound-on-the)
