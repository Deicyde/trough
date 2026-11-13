---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.shiftAt, Cslib.Languages.LambdaCalculus.SystemF.liftRaw, Cslib.Languages.LambdaCalculus.SystemF.shiftAt_closed, Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith, Cslib.Languages.LambdaCalculus.SystemF.Tm.erase, Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith_lcAt, Cslib.Languages.LambdaCalculus.SystemF.Tm.close, Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseModel
statement: formalized
proof: formalized
---

# System F erasure and closing environments

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html).

## System F

## Shift of untyped bound indices above a cutoff

Shift free bound indices in CSLib syntax, preserving indices below `c`.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.shiftAt`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#shift-at).

## Lifting a raw erasure environment under a binder

Lift a raw erasure environment beneath one scoped term binder.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.liftRaw`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#lift-raw).

## Shifting leaves locally closed terms unchanged

Introducing a binder does not shift an already locally closed term.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.shiftAt_closed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#shift-at-closed).

## Type erasure under an untyped environment

Erase a scoped term under an arbitrary simultaneous untyped environment.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase-with).

## Type erasure of System F terms to untyped terms

Type erasure into the existing untyped de Bruijn syntax.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.erase`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase).

## Erasure with locally closed images is locally closed

Erasure preserves the closure invariant of its environment images.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith_lcAt`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase-with-lc-at).

## Closing System F terms in the term model

Close every scoped term variable with a locally closed model term.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close).

## Erasure of closed System F terms to the term model

Erase a term with no free term variables into the existing term model.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseModel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase-model).

## Opening commutes with erasure under an environment

Opening an erased instance opens exactly its raw environment images.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith_openRec`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase-with-open-rec).

## Untyped erasure is invariant under type substitution

Type substitution changes no part of the erased untyped term.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith_tySubst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase-with-ty-subst).

## Closing a System F variable

Closing a variable returns exactly its environment image.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close_var`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close-var).

## Closing a System F application

Closing commutes with the upstream model's application.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close_app`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close-app).

## Closing erases System F type abstraction

A type lambda contributes no untyped binder.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close_tabs`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close-tabs).

## Closing erases System F type application

A type argument contributes no untyped application.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close_tapp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close-tapp).

## System F closing is invariant under type substitution

Closing is independent of every type substitution.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close_tySubst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close-ty-subst).

## Beta conversion of a closed System F lambda application

An erased lambda application beta-converts to its extended body instance.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close_beta`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close-beta).

## Shifting commutes with erasure under an environment

Shifting an erased instance shifts exactly its raw environment images.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith_shift`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase-with-shift).

## Erasure of a term-variable renaming

Erasing a term-variable renaming precomposes the raw environment.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase-with-rename).

## Erasure of a term substitution

Actual term substitution erases by composing raw environments.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.eraseWith_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#erase-with-subst).

## Closing commutes with System F term substitution

Closing an actual substitution composes its model-valued environments.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close-subst).

## Closing an instantiated System F term binder

Actual binder discharge agrees with extending the closing environment.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.close_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Erasure.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html#close-instantiate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: System F erasure and closing environments](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/system-f-erasure-and-closing-environments)
