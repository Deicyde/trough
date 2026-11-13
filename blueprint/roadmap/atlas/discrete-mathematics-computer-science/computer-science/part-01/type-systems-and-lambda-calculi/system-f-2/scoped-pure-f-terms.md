---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Tm, Cslib.Languages.LambdaCalculus.FOmega.Ctx, Cslib.Languages.LambdaCalculus.FOmega.Tm.tySubst, Cslib.Languages.LambdaCalculus.FOmega.Tm.tyRename, Cslib.Languages.LambdaCalculus.FOmega.Tm.rename, Cslib.Languages.LambdaCalculus.FOmega.Tm.liftSub, Cslib.Languages.LambdaCalculus.FOmega.Tm.subst, Cslib.Languages.LambdaCalculus.FOmega.Tm.instantiate
statement: formalized
proof: formalized
---

# Scoped pure Fω terms

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html).

## Terms and contexts

## Scoped pure Fω terms

Pure terms at a kind telescope and a finite term-variable depth.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html#tm).

## Term contexts of pure Fω

An ordered unrestricted term context of kind-`star` types.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ctx`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html#ctx).

## Type substitution in Fω terms

Substitute kinded type variables in all annotations and type arguments.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.tySubst`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html#ty-subst).

## Type-variable renaming in Fω terms

Rename type variables without changing term variables.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.tyRename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html#ty-rename).

## Term-variable renaming in Fω terms

Rename term variables, lifting only beneath term lambdas.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html#rename).

## Lifting a term substitution under a term binder

Lift a term substitution beneath one term binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.liftSub`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html#lift-sub).

## Simultaneous term substitution in Fω

Term substitution avoids capture in both namespaces.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.subst`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html#subst).

## Instantiation of an Fω term binder

Discharge the newest term binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.instantiate`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Terms.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html#instantiate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Scoped pure Fω terms](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/scoped-pure-f-terms)
