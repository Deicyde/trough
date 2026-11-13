---
declaration: section
origin: cited
lean: StatMech.Lattice.symPrimal, StatMech.Lattice.symPrimalSym, StatMech.Lattice.flankFaces, StatMech.Lattice.flankFacesSym, StatMech.Lattice.dualWalkContour, StatMech.Lattice.PeierlsContourCircuitData, StatMech.Lattice.ContourGeometryResidue
statement: formalized
proof: formalized
---

# Dual circuits decode to contours in two dimensions

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html).

## A. Primal and dual edges

## Primal edge crossed by a dual edge

The primal edge of `ℤ²` crossed by the dual edge between the faces `f` and `g`, defined
symmetrically in `f` and `g`. See also `sharedPrimalEdge`, with which it agrees on adjacent
faces (`symPrimal_eq_shared`).

Formalized by `StatMech.Lattice.symPrimal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html#sym-primal).

## Primal edge crossed by an unordered pair of faces

`symPrimal` on unordered pairs of faces.

Formalized by `StatMech.Lattice.symPrimalSym`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html#sym-primal-sym).

## Two faces flanking a primal edge

The two faces of `ℤ²` flanking the primal edge `{p, q}`.

Formalized by `StatMech.Lattice.flankFaces`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html#flank-faces).

## Two faces flanking an unordered pair of sites

`flankFaces` on unordered pairs of sites.

Formalized by `StatMech.Lattice.flankFacesSym`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html#flank-faces-sym).

## Primal edges crossed by a closed dual walk

The set of primal edges crossed by a closed dual walk.

Formalized by `StatMech.Lattice.dualWalkContour`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html#dual-walk-contour).

## Connected face-boundary graphs at the axis for all realised contours

Every realised contour of length `ℓ` in `Λ_n ⊆ ℤ²` is the contour of a finite cluster whose
face-boundary graph is connected on `boundarySupport` and meets an axis face `(j, 0)` with `j <
ℓ`. The condition refers to the face set `boundarySupport`, which is chosen by
`Classical.choose`.

Formalized by `StatMech.Lattice.PeierlsContourCircuitData`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html#peierls-contour-circuit-data).

## Connected face-boundary graphs at the axis for all connected clusters

Every connected cluster in `Λ_n ⊆ ℤ²` with contour length `ℓ` is finite, has face-boundary graph
connected on `boundarySupport`, and meets an axis face `(j, 0)` with `j < ℓ`. The condition
refers to the face set `boundarySupport`, which is chosen by `Classical.choose`;
`TightAxisCircuitData` avoids this choice.

Formalized by `StatMech.Lattice.ContourGeometryResidue`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/DualCircuitDecoding.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html#contour-geometry-residue).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dual circuits decode to contours in two dimensions](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-decode-to-contours-in-two-dimensio)
