---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_congr, Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_id, Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_congr, Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_id, Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_subst, Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_subst
statement: formalized
proof: formalized
---

# Capture-avoiding binding laws for kinded type operators

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html).

## Renaming of type operators depends only on variable images

Renaming depends only on its action on kinded variables.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#rename-congr).

## Identity renaming fixes type operators

The identity renaming fixes every type operator.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_id`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#rename-id).

## Composition of kind-preserving renamings

Successive kind-preserving renamings fuse, including beneath binders.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#rename-rename).

## Substitution of type operators depends only on variable images

Substitution depends only on the images of kinded variables.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#subst-congr).

## Identity substitution fixes type operators

Substituting each variable by itself fixes every type operator.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_id`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#subst-id).

## Substitution after renaming of type operators

Substitution after renaming is precomposition on the variable images.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#subst-rename).

## Renaming after substitution of type operators

Renaming after substitution renames each substituted type operator.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#rename-subst).

## Composition of simultaneous type-operator substitutions

Capture-avoiding simultaneous substitutions compose.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#subst-subst).

## Instantiating a weakened type operator leaves it unchanged

Discharging a fresh binder leaves a weakened operator unchanged.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.instantiate_rename_succ`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#instantiate-rename-succ).

## Substitution commutes with type-binder instantiation

Simultaneous substitution commutes with discharging a type binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#subst-instantiate).

## Renaming commutes with type-binder instantiation

Renaming commutes with discharging a type binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.rename_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#rename-instantiate).

## Renaming as substitution by variables

Renaming is substitution by the corresponding variable constructors.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_var_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#subst-var-rename).

## Lifted substitution commutes with weakening

Lifted type substitution commutes with weakening past the new binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.subst_lift_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Binding.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html#subst-lift-rename).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Capture-avoiding binding laws for kinded type operators](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/capture-avoiding-binding-laws-for-kinded-type-op)
