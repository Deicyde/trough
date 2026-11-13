---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_symbolDispersion, StatMech.Onsager.ons_pressureFinite, StatMech.Onsager.ons_torusPressureSeq
statement: formalized
proof: formalized
---

# Onsager's solution of the two-dimensional Ising model: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/index.html).

## Kac-Ward symbol determinant at t = tanh β

The Kac-Ward symbol determinant `(1 + t²)² - 2t(1 - t²)(cos k₁ + cos k₂)` at `t = tanh β`.

Formalized by `StatMech.Onsager.ons_symbolDispersion`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/IntegrandLimit.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/IntegrandLimit.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/index.html#ons-symbol-dispersion).

## Finite-volume pressure

The finite-volume pressure `log Z_G(β) / |V|` (the negative of `β` times the free energy per
site).

Formalized by `StatMech.Onsager.ons_pressureFinite`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/Pressure.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/Pressure.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/index.html#ons-pressure-finite).

## Torus pressure sequence of the zero-field Ising model

The pressure `log Z_L(β) / L²` of the zero-field Ising model on the `L × L` torus, as a sequence
in `L` (set to `0` for `L ≤ 2`, where the torus graph is not defined).

Formalized by `StatMech.Onsager.ons_torusPressureSeq`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalTransfer.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalTransfer.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/index.html#ons-torus-pressure-seq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Onsager's solution of the two-dimensional Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising)
