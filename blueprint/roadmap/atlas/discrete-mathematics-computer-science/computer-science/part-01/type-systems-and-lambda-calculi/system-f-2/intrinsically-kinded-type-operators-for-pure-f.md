---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Kind, Cslib.Languages.LambdaCalculus.FOmega.KVar, Cslib.Languages.LambdaCalculus.FOmega.KRen, Cslib.Languages.LambdaCalculus.FOmega.KRen.lift, Cslib.Languages.LambdaCalculus.FOmega.Ty, Cslib.Languages.LambdaCalculus.FOmega.Ty.rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.Sub, Cslib.Languages.LambdaCalculus.FOmega.Ty.liftSub
statement: formalized
proof: formalized
---

# Intrinsically kinded type operators for pure Fω

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html).

## Kinds and type variables

## Kinds of pure Fω

Kinds of pure Fω. `star` classifies types of terms.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Kind`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#kind).

## Kinded type variables of Fω

A type variable with its position and kind certified by the telescope.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.KVar`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#kvar).

## Kind-preserving renamings of type variables

Kind-preserving renamings of type variables.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.KRen`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#kren).

## Lifting a renaming under a type binder

Lift a kind-preserving renaming beneath a type binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.KRen.lift`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#lift).

## Intrinsically kinded Fω type operators

Type operators, intrinsically indexed by context and result kind.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#ty).

## Renaming of Fω type operators

Rename free type variables, lifting at both forms of type binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#rename).

## Kind-preserving simultaneous type substitutions

Kind-preserving simultaneous substitutions.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.Sub`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#sub).

## Lifting a type substitution under a type binder

Lift substitution beneath a type binder without capturing old images.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.liftSub`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#lift-sub).

## Simultaneous substitution of Fω type operators

Capture-avoiding simultaneous substitution of kinded type operators.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.subst`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#subst).

## Substitution for the newest type variable

Substitution replacing only the newest type variable.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.single`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#single).

## Instantiation of an Fω type binder

Substitute for the newest variable and discharge its binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.instantiate`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Syntax.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html#instantiate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Intrinsically kinded type operators for pure Fω](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/intrinsically-kinded-type-operators-for-pure-f)
