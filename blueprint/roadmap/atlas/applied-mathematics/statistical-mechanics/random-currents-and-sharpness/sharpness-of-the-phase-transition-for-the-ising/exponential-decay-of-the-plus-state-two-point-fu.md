---
declaration: section
origin: cited
lean: StatMech.Sharpness.isingSimonRadius, StatMech.Sharpness.plusCorrTailSet, StatMech.Sharpness.plusCorrTailSup
statement: formalized
proof: formalized
---

# Exponential decay of the plus-state two-point function below β̃\_c

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/exponential-decay-of-the-plus-state-two-point-fu/index.html).

## B. Distances and the Simon radius

## Simon radius of a finite set

One more than the largest `ℓ¹` distance from the origin of a point of `T` or of the outer
endpoint of a boundary edge of `T`.

Formalized by `StatMech.Sharpness.isingSimonRadius`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingExponentialPlus.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingExponentialPlus.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/exponential-decay-of-the-plus-state-two-point-fu/index.html#ising-simon-radius).

## Tail set of plus-state correlations

The set of values `⟨σ_0σ_z⟩^+_β` with `‖z‖₁ ≥ n`, together with `0`.

Formalized by `StatMech.Sharpness.plusCorrTailSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingExponentialPlus.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingExponentialPlus.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/exponential-decay-of-the-plus-state-two-point-fu/index.html#plus-corr-tail-set).

## Tail supremum of plus-state correlations

The tail supremum `sup {⟨σ_0σ_z⟩^+_β | ‖z‖₁ ≥ n}` (and `0`).

Formalized by `StatMech.Sharpness.plusCorrTailSup`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingExponentialPlus.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingExponentialPlus.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/exponential-decay-of-the-plus-state-two-point-fu/index.html#plus-corr-tail-sup).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential decay of the plus-state two-point function below β̃_c](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/exponential-decay-of-the-plus-state-two-point-fu/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/exponential-decay-of-the-plus-state-two-point-fu)
