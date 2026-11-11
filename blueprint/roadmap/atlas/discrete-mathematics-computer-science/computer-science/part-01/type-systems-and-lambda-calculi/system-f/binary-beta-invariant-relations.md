---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.Rel, Cslib.Languages.LambdaCalculus.SystemF.Rel.ext, Cslib.Languages.LambdaCalculus.SystemF.Rel.arrow, Cslib.Languages.LambdaCalculus.SystemF.Rel.universal, Cslib.Languages.LambdaCalculus.SystemF.Rel.empty, Cslib.Languages.LambdaCalculus.SystemF.Rel.total, Cslib.Languages.LambdaCalculus.SystemF.Rel.betaClass
statement: formalized
proof: formalized
---

# Binary beta-invariant relations

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html).

## System F

## Beta-invariant binary relations on the term model

A binary relation on the term model, invariant under beta conversion.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Rel`, a structure declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html#rel).

## Extensionality of beta-invariant relations

Admissible relations are determined by their binary predicates.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Rel.ext`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html#ext).

## Function-space relation of beta-invariant relations

Related functions send every related input pair to related outputs.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Rel.arrow`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html#arrow).

## Universal quantification over a family of relations

Universal relatedness, over any index sort, uses impredicative Prop.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Rel.universal`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html#universal).

## Empty beta-invariant relation

The empty relation is admissible and prevents vacuous universality.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Rel.empty`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html#empty).

## Total beta-invariant relation

The total binary relation is admissible.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Rel.total`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html#total).

## Relation of two terms beta-equal to a fixed term

Both arguments belong to the fixed beta-conversion class of `x`.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Rel.betaClass`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Relations.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html#beta-class).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary beta-invariant relations](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/binary-beta-invariant-relations)
