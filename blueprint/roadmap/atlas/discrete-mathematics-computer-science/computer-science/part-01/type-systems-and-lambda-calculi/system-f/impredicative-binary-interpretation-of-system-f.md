---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret, Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret_rename, Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret_subst, Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret_instantiate, Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret_weaken
statement: formalized
proof: formalized
---

# Impredicative binary interpretation of System F types

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/impredicative-binary-interpretation-of-system-f/index.html).

## Binary logical relation of a System F type

The impredicative binary logical relation denoted by a System F type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/impredicative-binary-interpretation-of-system-f/index.html#interpret).

## Relational interpretation of a renamed System F type

Interpreting a renamed type precomposes the relation environment.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/impredicative-binary-interpretation-of-system-f/index.html#interpret-rename).

## Relational interpretation of a substituted System F type

Type substitution is interpreted by substituting arbitrary relations.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/impredicative-binary-interpretation-of-system-f/index.html#interpret-subst).

## Relational interpretation of an instantiated System F type

Universal instantiation inserts the argument's whole logical relation.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/impredicative-binary-interpretation-of-system-f/index.html#interpret-instantiate).

## Relational interpretation of a weakened System F type

Weakening a type does not make it depend on the new arbitrary relation.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.interpret_weaken`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Interpretation.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/impredicative-binary-interpretation-of-system-f/index.html#interpret-weaken).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Impredicative binary interpretation of System F types](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/impredicative-binary-interpretation-of-system-f/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/impredicative-binary-interpretation-of-system-f)
