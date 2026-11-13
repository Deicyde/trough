---
declaration: section
origin: cited
lean: StatMech.Lattice.RealisedContourWalkEncoding, StatMech.Ising.ConnectedContourCount
statement: formalized
proof: formalized
---

# Peierls argument for the Ising model: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/index.html).

## Closed-walk encoding of realised contours of length $\ell$

Every realised contour of length `ℓ` in `Λ_n` is decoded from a closed lattice walk of length
`ℓ` based at one of at most `ℓ` anchor sites.

Formalized by `StatMech.Lattice.RealisedContourWalkEncoding`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ContourSubsetCount.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/ContourSubsetCount.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/index.html#realised-contour-walk-encoding).

## Peierls count of connected clusters by contour length

For every `ℓ`, at most `ℓ (2d)^ℓ` connected clusters through the origin in `Λ_n` have contour
length `ℓ`.

Formalized by `StatMech.Ising.ConnectedContourCount`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsConnectedCount.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PeierlsConnectedCount.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/index.html#connected-contour-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Peierls argument for the Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model)
