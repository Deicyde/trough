---
declaration: section
origin: cited
lean: StatMech.Ising.flipConfig, StatMech.Ising.flipInterior, StatMech.Ising.flipInteriorEquiv, StatMech.Ising.origin, StatMech.Ising.fvMagOrigin
statement: formalized
proof: formalized
---

# Spin-flip symmetry and the Peierls long-range-order criterion

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/spin-flip-symmetry-and-the-peierls-long-range-or/index.html).

## A. The global spin flip

## Global spin flip of a configuration

The global spin flip `σ ↦ -σ` of an infinite-volume configuration.

Formalized by `StatMech.Ising.flipConfig`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/spin-flip-symmetry-and-the-peierls-long-range-or/index.html#flip-config).

## Spin flip inside the box

The spin flip of a configuration inside the box `Λ_n`.

Formalized by `StatMech.Ising.flipInterior`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/spin-flip-symmetry-and-the-peierls-long-range-or/index.html#flip-interior).

## Spin flip inside the box as an involutive equivalence

The spin flip inside the box as an involutive equivalence.

Formalized by `StatMech.Ising.flipInteriorEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/spin-flip-symmetry-and-the-peierls-long-range-or/index.html#flip-interior-equiv).

## Origin of $\mathbb{Z}^d$

The origin of `ℤ^d`.

Formalized by `StatMech.Ising.origin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/spin-flip-symmetry-and-the-peierls-long-range-or/index.html#origin).

## Finite-volume magnetization at the origin

The magnetization `⟨σ_0⟩` at the origin in the finite-volume Ising measure on `Λ_n` with
boundary condition `η`, bond set `B`, inverse temperature `β` and field `h`.

Formalized by `StatMech.Ising.fvMagOrigin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/spin-flip-symmetry-and-the-peierls-long-range-or/index.html#fv-mag-origin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spin-flip symmetry and the Peierls long-range-order criterion](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/spin-flip-symmetry-and-the-peierls-long-range-or/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/spin-flip-symmetry-and-the-peierls-long-range-or)
