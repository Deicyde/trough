---
declaration: section
origin: cited
lean: StatMech.Lattice.regionDel, StatMech.Lattice.ccb_contourFiber, StatMech.Lattice.ccb_ContourEncodingExists
statement: formalized
proof: formalized
---

# Contours of clusters in a box and closed-walk encodings

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-clusters-in-a-box-and-closed-walk-en/index.html).

## A. Contours of clusters in a box

## Sites reachable from the origin after deleting edges

The set of sites reachable from the origin in the hypercubic lattice after deleting the edges in
`F`.

Formalized by `StatMech.Lattice.regionDel`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterContourBijection.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterContourBijection.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-clusters-in-a-box-and-closed-walk-en/index.html#region-del).

## Connected clusters in a box with contour length $\ell$

The connected clusters in the box `Λ_n` whose contour has exactly `ℓ` bonds.

Formalized by `StatMech.Lattice.ccb_contourFiber`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterContourBijection.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterContourBijection.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-clusters-in-a-box-and-closed-walk-en/index.html#ccb-contour-fiber).

## Injective closed-walk encoding of clusters of contour length $\ell$

The clusters with contour length `ℓ` admit an injective encoding by closed lattice walks of
length `ℓ` based at one of at most `ℓ` anchor sites.

Formalized by `StatMech.Lattice.ccb_ContourEncodingExists`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterContourBijection.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterContourBijection.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-clusters-in-a-box-and-closed-walk-en/index.html#ccb-contour-encoding-exists).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Contours of clusters in a box and closed-walk encodings](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-clusters-in-a-box-and-closed-walk-en/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/contours-of-clusters-in-a-box-and-closed-walk-en)
