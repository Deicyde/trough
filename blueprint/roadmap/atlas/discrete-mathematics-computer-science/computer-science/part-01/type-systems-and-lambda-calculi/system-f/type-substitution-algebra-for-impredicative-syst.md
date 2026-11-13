---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.SystemF.liftRen_id, Cslib.Languages.LambdaCalculus.SystemF.liftRen_comp, Cslib.Languages.LambdaCalculus.SystemF.Ty.rename_id, Cslib.Languages.LambdaCalculus.SystemF.Ty.rename_comp, Cslib.Languages.LambdaCalculus.SystemF.Ty.subst_rename, Cslib.Languages.LambdaCalculus.SystemF.Ty.rename_subst, Cslib.Languages.LambdaCalculus.SystemF.Ty.liftSub_var, Cslib.Languages.LambdaCalculus.SystemF.Ty.subst_id
statement: formalized
proof: formalized
---

# Type-substitution algebra for impredicative System F

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html).

## System F

## Lifted identity renaming is the identity

Lifting the identity renaming gives the identity.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.liftRen_id`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#lift-ren-id).

## Lifting preserves composition of renamings

Lifting preserves composition of renamings.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.liftRen_comp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#lift-ren-comp).

## Identity renaming fixes every type

Type renaming by the identity does not change a type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.rename_id`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#rename-id).

## Successive type renamings fuse into their composition

Two type renamings fuse into their composition.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.rename_comp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#rename-comp).

## Substitution after a type renaming

Substitution after renaming composes the variable environments.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.subst_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#subst-rename).

## Renaming after a type substitution

Renaming after substitution renames each substituted image.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.rename_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#rename-subst).

## Lifted identity type substitution is the identity

Lifting the variable substitution gives the variable substitution.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.liftSub_var`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#lift-sub-var).

## Identity type substitution fixes every type

Substitution of each type variable by itself is the identity.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.subst_id`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#subst-id).

## Variable-valued substitution is a type renaming

A variable-valued substitution is the corresponding type renaming.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.subst_var_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#subst-var-rename).

## Lifted type substitution commutes with weakening

Lifted type substitution commutes with weakening an old type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.subst_lift_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#subst-lift-rename).

## Successive type substitutions fuse into one substitution

Two simultaneous type substitutions fuse by substituting each image.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.subst_comp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#subst-comp).

## Type substitution commutes with instantiation

Type substitution commutes with discharging a type binder.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.subst_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#subst-instantiate).

## Instantiating a weakened type restores it

Instantiating a freshly weakened type restores the original type.

Formalized by `Cslib.Languages.LambdaCalculus.SystemF.Ty.instantiate_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/SystemF/TypeSubstitution.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html#instantiate-rename).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Type-substitution algebra for impredicative System F](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f/type-substitution-algebra-for-impredicative-syst)
