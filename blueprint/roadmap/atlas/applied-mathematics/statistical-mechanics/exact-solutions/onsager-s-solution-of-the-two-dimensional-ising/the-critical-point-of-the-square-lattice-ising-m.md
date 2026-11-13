---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_gInt, StatMech.Onsager.ons_betaC, StatMech.Onsager.ons_betaC_sinh, StatMech.Onsager.ons_betaC_unique
statement: formalized
proof: formalized
---

# The critical point of the square-lattice Ising model

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-critical-point-of-the-square-lattice-ising-m/index.html).

## A. The Onsager integrand

## Onsager integrand of the square-lattice Ising model

The Onsager integrand `cosh² 2β - sinh 2β (cos k₁ + cos k₂)` at inverse temperature `β` and
momentum `(k₁, k₂)`.

Formalized by `StatMech.Onsager.ons_gInt`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalPoint.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalPoint.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-critical-point-of-the-square-lattice-ising-m/index.html#ons-g-int).

## Critical inverse temperature ½ log(1 + √2) of the square lattice

The critical inverse temperature `β_c = ½ log (1 + √2)` of the square-lattice Ising model with
unit couplings.

Formalized by `StatMech.Onsager.ons_betaC`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalPoint.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalPoint.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-critical-point-of-the-square-lattice-ising-m/index.html#ons-beta-c).

## Kramers-Wannier critical point

`sinh 2β_c = 1` (H. A. Kramers and G. H. Wannier,
*Statistics of the two-dimensional ferromagnet. Part I*, 1941).

Formalized by `StatMech.Onsager.ons_betaC_sinh`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalPoint.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalPoint.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-critical-point-of-the-square-lattice-ising-m/index.html#ons-beta-c-sinh).

## β_c is the unique positive solution of sinh 2β = 1

`β_c` is the unique positive inverse temperature with `sinh 2β = 1`, the self-dual point of the
Kramers-Wannier duality.

Formalized by `StatMech.Onsager.ons_betaC_unique`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalPoint.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalPoint.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-critical-point-of-the-square-lattice-ising-m/index.html#ons-beta-c-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The critical point of the square-lattice Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-critical-point-of-the-square-lattice-ising-m/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-critical-point-of-the-square-lattice-ising-m)
