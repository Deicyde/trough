---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.Ty, Cslib.Languages.LambdaCalculus.SystemF.liftRen, Cslib.Languages.LambdaCalculus.SystemF.liftRen_zero, Cslib.Languages.LambdaCalculus.SystemF.liftRen_succ, Cslib.Languages.LambdaCalculus.SystemF.Ty.rename, Cslib.Languages.LambdaCalculus.SystemF.Ty.liftSub, Cslib.Languages.LambdaCalculus.SystemF.Ty.subst, Cslib.Languages.LambdaCalculus.SystemF.Ty.instantiate
statement: formalized
proof: formalized
---

# Scoped pure System F

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html).

## System F

## Scoped types of pure System F

Pure System F types with `n` available type variables.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#ty).

## Lifting a scoped renaming under a binder

Extend a scoped renaming, preserving the newly bound variable.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.liftRen`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#lift-ren).

## Lifted renaming fixes the newly bound variable

The new variable is unaffected by a lifted renaming.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.liftRen_zero`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#lift-ren-zero).

## Lifted renaming shifts each renamed old variable

A lifted renaming shifts every renamed old variable.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.liftRen_succ`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#lift-ren-succ).

## Type-variable renaming in System F types

Capture-avoiding renaming of type variables.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#rename).

## Lifting a type substitution under a type binder

Lift a type substitution under one type binder.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.liftSub`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#lift-sub).

## Simultaneous type substitution in System F types

Simultaneous, capture-avoiding type substitution.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.subst`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#subst).

## Instantiating the newest type binder of a type

Discharge the newest type binder by an arbitrary type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.instantiate`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#instantiate).

## Lifted type substitution fixes the fresh variable

The fresh type variable is fixed by a lifted substitution.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.liftSub_zero`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#lift-sub-zero).

## Lifted type substitution weakens old images

Old type-substitution images are weakened under a binder.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.liftSub_succ`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#lift-sub-succ).

## Scoped terms of pure System F

Pure terms with `n` type variables and `m` term variables.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#tm).

## Term variable contexts of System F

An ordered, unrestricted term context over `n` type variables.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ctx`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#ctx).

## Type substitution in System F terms

Substitute type variables in annotations, arguments, and type binders.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.tySubst`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#ty-subst).

## Term-variable renaming in System F terms

Rename term variables, lifting only at term binders.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#rename-2).

## Type-variable renaming in System F terms

Rename type variables without changing term variables.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.tyRename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#ty-rename).

## Lifting a term substitution under a term lambda

Lift a simultaneous term substitution beneath a term lambda.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.liftSub`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#lift-sub-2).

## Simultaneous term substitution in System F terms

Simultaneous term substitution, avoiding both sorts of capture.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.subst`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#subst-2).

## Instantiating the newest term binder of a term

Replace the newest term variable and discharge its binder.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Tm.instantiate`, a definition declared in [CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/Syntax.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html#instantiate-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Scoped pure System F](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/scoped-pure-system-f)
