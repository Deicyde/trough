---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax, Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax_tySubst, Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax_rename, Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax_subst, Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax_instantiate
statement: formalized
proof: formalized
---

# Erasure adapter to the existing System F scoped syntax

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/erasure-adapter-to-the-existing-system-f-scoped/index.html).

## Erasure of Fω terms to System F syntax

Erase types using the already banked System F scoped term carrier.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/erasure-adapter-to-the-existing-system-f-scoped/index.html#erase-syntax).

## Fω erasure ignores type substitution

Erasure ignores all kind-correct type substitutions.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax_tySubst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/erasure-adapter-to-the-existing-system-f-scoped/index.html#erase-syntax-ty-subst).

## Fω erasure commutes with term-variable renaming

Erasure commutes with scoped term-variable renaming.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/erasure-adapter-to-the-existing-system-f-scoped/index.html#erase-syntax-rename).

## Fω erasure commutes with term substitution

Erasure commutes with simultaneous substitution of scoped terms.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/erasure-adapter-to-the-existing-system-f-scoped/index.html#erase-syntax-subst).

## Fω erasure commutes with term-binder instantiation

Erasure commutes with discharging a term binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseSyntax_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/ErasureSyntax.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/erasure-adapter-to-the-existing-system-f-scoped/index.html#erase-syntax-instantiate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erasure adapter to the existing System F scoped syntax](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/erasure-adapter-to-the-existing-system-f-scoped/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/erasure-adapter-to-the-existing-system-f-scoped)
