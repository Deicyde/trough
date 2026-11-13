---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Tm.close, Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseModel, Cslib.Languages.LambdaCalculus.FOmega.Tm.close_var, Cslib.Languages.LambdaCalculus.FOmega.Tm.close_app, Cslib.Languages.LambdaCalculus.FOmega.Tm.close_tabs, Cslib.Languages.LambdaCalculus.FOmega.Tm.close_tapp, Cslib.Languages.LambdaCalculus.FOmega.Tm.close_tySubst, Cslib.Languages.LambdaCalculus.FOmega.Tm.close_beta
statement: formalized
proof: formalized
---

# Fω closing instances in the single existing term model

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html).

## Closing Fω terms in the System F term model

Close scoped Fω variables in exactly the existing System F term model.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close).

## Erasure of closed Fω terms to the term model

Erase a closed-term Fω expression, with an arbitrary type telescope.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.eraseModel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#erase-model).

## Closing an Fω variable

Closing a variable returns its actual model environment image.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_var`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close-var).

## Closing an Fω application

Closing preserves the existing model application constructor.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_app`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close-app).

## Closing erases type abstraction

Type abstraction adds no binder to an erased closing instance.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_tabs`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close-tabs).

## Closing erases type application

Type application adds no application to an erased closing instance.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_tapp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close-tapp).

## Closing is invariant under type substitution

Any kind-correct type substitution leaves closing instances unchanged.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_tySubst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close-ty-subst).

## Beta conversion of a closed Fω lambda application

Applying an erased Fω lambda beta-converts to its extended body instance.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_beta`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close-beta).

## Closing commutes with Fω term substitution

Closing composes actual Fω term substitutions with model environments.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close-subst).

## Closing an instantiated Fω term binder

Actual term-binder discharge extends the same model closing environment.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.close_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Closing.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html#close-instantiate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fω closing instances in the single existing term model](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/f-closing-instances-in-the-single-existing-term)
