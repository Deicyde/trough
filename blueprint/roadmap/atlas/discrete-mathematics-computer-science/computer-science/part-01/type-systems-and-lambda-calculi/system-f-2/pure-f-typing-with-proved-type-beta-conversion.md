---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Typing, Cslib.Languages.LambdaCalculus.FOmega.Typing.tySubst, Cslib.Languages.LambdaCalculus.FOmega.Typing.tyRename, Cslib.Languages.LambdaCalculus.FOmega.Typing.rename, Cslib.Languages.LambdaCalculus.FOmega.Typing.subst, Cslib.Languages.LambdaCalculus.FOmega.Typing.instantiate, Cslib.Languages.LambdaCalculus.FOmega.Typing.tyInstantiate
statement: formalized
proof: formalized
---

# Pure Fω typing with proved type-beta conversion

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html).

## Typing rules

## Typing rules of pure Fω

The five pure term rules and the type-beta conversion rule of Fω.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html#typing).

## Type substitution preserves Fω typing

Kind-correct type substitution preserves typing in arbitrary contexts.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.tySubst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html#ty-subst).

## Type renaming preserves Fω typing

Kind-preserving type renaming preserves typing.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.tyRename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html#ty-rename).

## Term renaming preserves Fω typing

A context-respecting term-variable renaming preserves the result type.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html#rename).

## Term substitution preserves Fω typing

Arbitrary correctly typed term substitution preserves typing.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html#subst).

## Term-binder instantiation preserves Fω typing

Discharging a typed term binder retains the body result type.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html#instantiate).

## Type-binder instantiation preserves Fω typing

Discharging a type binder substitutes its result and restores context.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Typing.tyInstantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/FOmega/Typing.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html#ty-instantiate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pure Fω typing with proved type-beta conversion](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/pure-f-typing-with-proved-type-beta-conversion)
