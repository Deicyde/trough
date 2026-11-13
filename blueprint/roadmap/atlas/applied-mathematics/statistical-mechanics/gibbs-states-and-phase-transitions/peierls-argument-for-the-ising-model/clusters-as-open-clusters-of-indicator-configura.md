---
declaration: section
origin: cited
lean: StatMech.Lattice.indicatorConfig, StatMech.Lattice.ccb_anchorRow, StatMech.Lattice.ccb_AnchoredBoundaryWalkExists
statement: formalized
proof: formalized
---

# Clusters as open clusters of indicator configurations, and anchored boundary walks

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/clusters-as-open-clusters-of-indicator-configura/index.html).

## A. Indicator configurations of clusters

## Bond configuration open on the edges inside a set

The bond configuration that is open exactly on the edges with both endpoints in `K`.

Formalized by `StatMech.Lattice.indicatorConfig`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/AnchoredBoundaryWalk.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/AnchoredBoundaryWalk.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/clusters-as-open-clusters-of-indicator-configura/index.html#indicator-config).

## Anchor row of $\ell$ sites in $\mathbb{Z}^2$

The anchor row `{(j, 0) : j < ℓ}` in `ℤ²`.

Formalized by `StatMech.Lattice.ccb_anchorRow`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/AnchoredBoundaryWalk.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/AnchoredBoundaryWalk.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/clusters-as-open-clusters-of-indicator-configura/index.html#ccb-anchor-row).

## Anchored closed-walk decoding of cluster contours in $\mathbb{Z}^2$

In `ℤ²`, every connected cluster in `Λ_n` with contour length `ℓ` has its contour decoded from a
closed walk of length `ℓ` based in the anchor row.

Formalized by `StatMech.Lattice.ccb_AnchoredBoundaryWalkExists`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/AnchoredBoundaryWalk.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/AnchoredBoundaryWalk.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/clusters-as-open-clusters-of-indicator-configura/index.html#ccb-anchored-boundary-walk-exists).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Clusters as open clusters of indicator configurations, and anchored boundary walks](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/clusters-as-open-clusters-of-indicator-configura/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/clusters-as-open-clusters-of-indicator-configura)
