---
declaration: section
origin: cited
lean: MeasureTheory.Measure.isInvInvariant_of_isMulRightInvariant, Matrix.GeneralLinearGroup.modularCharacter_fin_two_eq_one, Matrix.GeneralLinearGroup.isMulRightInvariant_and_isInvInvariant_of_isHaarMeasure_fin_two
statement: formalized
proof: formalized
---

# Unimodular groups

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/unimodular-groups/index.html).

## Right-invariant Haar measures are inversion-invariant

A right-invariant Haar measure is invariant under inversion.

Formalized by `MeasureTheory.Measure.isInvInvariant_of_isMulRightInvariant`, a theorem declared in [MathlibExt/MeasureTheory/Measure/IsInvInvariant.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Measure/IsInvInvariant.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/unimodular-groups/index.html#is-inv-invariant-of-is-mul-right-invaria).

## GL(2, F) is unimodular

The modular character of `GL (2, F)` is trivial: `GL (2, F)` is unimodular.

Formalized by `Matrix.GeneralLinearGroup.modularCharacter_fin_two_eq_one`, a theorem declared in [MathlibExt/MeasureTheory/Group/GL2Haar.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Group/GL2Haar.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/unimodular-groups/index.html#modular-character-fin-two-eq-one).

## Haar measures on GL(2, F) are right- and inversion-invariant

Every Haar measure on `GL (2, F)` is right-invariant and inversion-invariant.

Formalized by `Matrix.GeneralLinearGroup.isMulRightInvariant_and_isInvInvariant_of_isHaarMeasure_fin_two`, a theorem declared in [MathlibExt/MeasureTheory/Group/GL2Haar.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Group/GL2Haar.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/unimodular-groups/index.html#is-mul-right-invariant-and-is-inv-invari).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unimodular groups](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/unimodular-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/haar-measure/unimodular-groups)
