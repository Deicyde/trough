---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_spinKacWardIdentities, StatMech.Onsager.ons_spinKacWardMatrixIdentities
statement: formalized
proof: formalized
---

# From the spin Kac-Ward identities to Onsager's formula

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/from-the-spin-kac-ward-identities-to-onsager-s-f/index.html).

## Spin Kac-Ward identities at inverse temperature $\beta$

The spin Kac-Ward identities at inverse temperature `β`: on every `L × L` torus with `L > 2`,
each signed sector sum at `tanh β` squares to the corresponding sector determinant.

Formalized by `StatMech.Onsager.ons_spinKacWardIdentities`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinKacWardResidue.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinKacWardResidue.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/from-the-spin-kac-ward-identities-to-onsager-s-f/index.html#ons-spin-kac-ward-identities).

## Spin Kac-Ward identities via twisted Kac-Ward determinants

The spin Kac-Ward identities written with the twisted Kac-Ward determinants `det (1 - Λ_{ab})`
at `x = tanh β`.

Formalized by `StatMech.Onsager.ons_spinKacWardMatrixIdentities`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinKacWardResidue.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinKacWardResidue.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/from-the-spin-kac-ward-identities-to-onsager-s-f/index.html#ons-spin-kac-ward-matrix-identities).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: From the spin Kac-Ward identities to Onsager's formula](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/from-the-spin-kac-ward-identities-to-onsager-s-f/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/from-the-spin-kac-ward-identities-to-onsager-s-f)
