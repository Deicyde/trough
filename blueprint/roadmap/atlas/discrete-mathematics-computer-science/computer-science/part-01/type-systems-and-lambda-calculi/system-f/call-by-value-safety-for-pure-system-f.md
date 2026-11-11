---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.Value, Cslib.Languages.LambdaCalculus.SystemF.Step, Cslib.Languages.LambdaCalculus.SystemF.Steps, Cslib.Languages.LambdaCalculus.SystemF.preservation, Cslib.Languages.LambdaCalculus.SystemF.Typing.canonical_lam, Cslib.Languages.LambdaCalculus.SystemF.Typing.canonical_tabs, Cslib.Languages.LambdaCalculus.SystemF.progress, Cslib.Languages.LambdaCalculus.SystemF.preservation_steps
statement: formalized
proof: formalized
---

# Call-by-value safety for pure System F

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html).

## Value forms of pure System F

The two value forms of pure System F.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Value`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#value).

## One-step call-by-value evaluation

One step of weak, left-to-right call-by-value evaluation.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Step`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#step).

## Multi-step call-by-value evaluation

Zero or more call-by-value evaluation steps.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Steps`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#steps).

## Type preservation for a call-by-value step

A call-by-value step preserves the exact type in arbitrary open contexts.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.preservation`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#preservation).

## Canonical forms of function-typed values

A function-typed value is a term lambda with the declared argument type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing.canonical_lam`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#canonical-lam).

## Canonical forms of universally typed values

A universally typed value is a type lambda.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing.canonical_tabs`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#canonical-tabs).

## Progress for well-typed terms without free term variables

A well-typed term with no free term variables is a value or can step.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.progress`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#progress).

## Type preservation along evaluation sequences

Every finite evaluation sequence preserves the exact type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.preservation_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#preservation-steps).

## Type safety for closed well-typed terms

No term reachable from a closed well-typed term is stuck.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.safety`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Semantics.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html#safety).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Call-by-value safety for pure System F](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/call-by-value-safety-for-pure-system-f)
