---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv, Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.sound, Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.subst, Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.subst_congr, Cslib.Languages.LambdaCalculus.FOmega.Ty.not_conv_arr_all
statement: formalized
proof: formalized
---

# Proved type-beta conversion for pure Fω

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f/index.html).

## Type-beta conversion in Fω

Type-beta conversion at a fixed context and kind.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f/index.html#conv).

## Soundness of type-beta conversion in kind algebras

Every type-beta conversion is sound in every semantic kind algebra.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.sound`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f/index.html#sound).

## Type-beta conversion is stable under renaming

Kind-preserving renaming respects proved type-beta conversion.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f/index.html#rename).

## Type-beta conversion is stable under substitution

Kind-preserving substitution respects proved type-beta conversion.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f/index.html#subst).

## Pointwise convertible substitutions give convertible results

Pointwise convertible substitution images give convertible results.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Conv.subst_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f/index.html#subst-congr).

## Function types are not convertible to quantified types

Term-function arrows cannot convert to quantified types, at any kind.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.not_conv_arr_all`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Conversion.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f/index.html#not-conv-arr-all).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Proved type-beta conversion for pure Fω](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/proved-type-beta-conversion-for-pure-f)
