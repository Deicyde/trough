---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_freeEnergyIntegral, StatMech.Onsager.ons_pressure, StatMech.Onsager.ons_KacWardResidue
statement: formalized
proof: formalized
---

# Onsager's free energy and the torus pressure

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-free-energy-and-the-torus-pressure/index.html).

## Onsager's free-energy double integral

The integral
`(1 / (8π²)) ∫_{-π}^{π} ∫_{-π}^{π} log (cosh² 2β - sinh 2β (cos k₁ + cos k₂)) dk₁ dk₂` in Onsager's
formula.

Formalized by `StatMech.Onsager.ons_freeEnergyIntegral`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/FreeEnergy.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/FreeEnergy.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-free-energy-and-the-torus-pressure/index.html#ons-free-energy-integral).

## Onsager's pressure of the square-lattice Ising model

Onsager's pressure (minus `β` times the free energy per site) of the square-lattice Ising model:
`log 2` plus `ons_freeEnergyIntegral β`.

Formalized by `StatMech.Onsager.ons_pressure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/FreeEnergy.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/FreeEnergy.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-free-energy-and-the-torus-pressure/index.html#ons-pressure).

## Limit statement for $\log X_L(\tanh\beta)/L^2$ on the torus

The statement that `log X_L(tanh β) / L²` on the `L × L` torus converges to
`ons_freeEnergyIntegral β - 2 log cosh β` as `L → ∞`.

Formalized by `StatMech.Onsager.ons_KacWardResidue`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/FreeEnergy.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/FreeEnergy.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-free-energy-and-the-torus-pressure/index.html#ons-kac-ward-residue).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Onsager's free energy and the torus pressure](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-free-energy-and-the-torus-pressure/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-free-energy-and-the-torus-pressure)
