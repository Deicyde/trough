---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Value, Cslib.Languages.LambdaCalculus.FOmega.Step, Cslib.Languages.LambdaCalculus.FOmega.Typing.lam_inv, Cslib.Languages.LambdaCalculus.FOmega.Typing.tabs_inv, Cslib.Languages.LambdaCalculus.FOmega.Typing.preservation, Cslib.Languages.LambdaCalculus.FOmega.Value.arrow, Cslib.Languages.LambdaCalculus.FOmega.Value.all, Cslib.Languages.LambdaCalculus.FOmega.Typing.progress
statement: formalized
proof: formalized
---

# Conversion-aware weak call-by-value safety for pure Fω

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html).

## Weak call-by-value values of Fω

Weak-CBV values: neither form of lambda evaluates beneath its binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Value`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#value).

## Weak call-by-value reduction of Fω

Ordinary left-to-right weak call-by-value reduction.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Step`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#step).

## Inversion of Fω lambda typing up to conversion

Lambda typing inversion retains the annotation and a proved conversion.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.lam_inv`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#lam-inv).

## Inversion of Fω type-lambda typing up to conversion

Type-lambda inversion retains its binder kind and body conversion.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.tabs_inv`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#tabs-inv).

## Type preservation for Fω weak call-by-value reduction

Weak-CBV reduction preserves typing in unrestricted open contexts.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.preservation`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#preservation).

## Canonical forms for Fω values of function type

A value typed at an arrow, despite conversion, is a term lambda.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Value.arrow`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#arrow).

## Canonical forms for Fω values of quantified type

A value at a quantified type is a type lambda of the same binder kind.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Value.all`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#all).

## Progress for closed Fω terms

Closed-term progress, allowing an arbitrary open kinded-type telescope.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.progress`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#progress).

## Type preservation along multistep Fω reduction

Every finite weak-CBV reduction sequence preserves typing.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.preservation_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#preservation-steps).

## Type safety of Fω weak call-by-value reduction

No reachable closed well-typed term is stuck, with type variables allowed.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.safety`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Safety.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html#safety).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conversion-aware weak call-by-value safety for pure Fω](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/conversion-aware-weak-call-by-value-safety-for-p)
