---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.Typing, Cslib.Languages.LambdaCalculus.SystemF.Typing.tySubst, Cslib.Languages.LambdaCalculus.SystemF.Typing.tyRename, Cslib.Languages.LambdaCalculus.SystemF.Typing.rename, Cslib.Languages.LambdaCalculus.SystemF.Typing.subst, Cslib.Languages.LambdaCalculus.SystemF.Typing.instantiate, Cslib.Languages.LambdaCalculus.SystemF.Typing.tyInstantiate
statement: formalized
proof: formalized
---

# The five typing rules of pure System F

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html).

## System F

## Extrinsic typing of pure System F terms

Extrinsic typing of scoped pure System F terms.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html#typing).

## Type substitution preserves typing

Type substitution preserves typing, including every context type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing.tySubst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html#ty-subst).

## Type renaming preserves typing

Type renaming preserves typing without adding term variables.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing.tyRename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html#ty-rename).

## Term renaming preserves typing

A context-respecting term renaming preserves the type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing.rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html#rename).

## Term substitution preserves typing

Correctly typed simultaneous term substitution preserves typing.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing.subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html#subst).

## Instantiating a term binder preserves typing

Discharging a term binder preserves the body type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing.instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html#instantiate).

## Instantiating a type binder preserves typing

Type binder discharge substitutes the type and restores the context.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Typing.tyInstantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/SystemF/Typing.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html#ty-instantiate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The five typing rules of pure System F](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/the-five-typing-rules-of-pure-system-f)
