---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.FOmega.liftTypes, Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF, Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_congr, Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_target_rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_target_subst, Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_source_rename, Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_source_subst, Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_instantiate
statement: formalized
proof: formalized
---

# The star/forall System F fragment inside pure Fω

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html).

## Type translation

## Lifting System F type-variable images under a star binder

Extend images of System F type variables under a star-kinded binder.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.liftTypes`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#lift-types).

## Translation of System F types into Fω

Translate System F types with arbitrary kind-`star` variable images.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f).

## Type translation depends only on variable images

The translation depends only on the images of free type variables.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-congr).

## Type translation commutes with target renaming

Target kind-preserving renaming commutes with the System F translation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_target_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-target-rename).

## Type translation commutes with target substitution

Target type substitution commutes with the System F translation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_target_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-target-subst).

## Type translation of a source renaming

Source type renaming is precomposition of the translated variable images.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_source_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-source-rename).

## Type translation of a source substitution

Source type substitution translates to simultaneous operator images.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_source_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-source-subst).

## Type translation commutes with type-binder instantiation

The System F translation commutes with type-binder instantiation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.fromSystemF_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-instantiate).

## Translation of System F terms into Fω

Translate all five System F term constructors, retaining type binders.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-2).

## Term translation preserves System F typing

Every System F typing derivation is preserved by the star translation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_typing`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-typing).

## Star-kinded variable of an all-star telescope

The corresponding star-kinded variable in an `n`-star telescope.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.KVar.ofFin`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#of-fin).

## Canonical embedding of System F types into Fω

The canonical variable-for-variable embedding of System F types.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Ty.embed`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#embed).

## Canonical embedding of System F terms into Fω

The canonical scoped embedding of System F terms into pure Fω.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.embed`, a definition declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#embed-2).

## Canonical embedding preserves System F typing

Canonical embedding preserves every System F typing derivation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.embed_typing`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#embed-typing).

## Term translation depends only on type-variable images

Term translation depends only on the images of its free type variables.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-congr-2).

## Term translation commutes with target type substitution

Operator substitution commutes with translating System F terms.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_target_tySubst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-target-ty-subst).

## Term translation of a source type substitution

Source type substitution commutes with the pure-term translation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_source_tySubst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-source-ty-subst).

## Term translation commutes with weakening under a type binder

Weakening beneath a type binder agrees in both calculus presentations.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_tyRename_succ`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-ty-rename-succ).

## Term translation commutes with term-variable renaming

Term-variable renaming commutes with the System F translation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-rename).

## Term translation commutes with term substitution

Simultaneous term substitution commutes with the System F translation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-subst).

## Term translation commutes with term-binder instantiation

Term-binder instantiation commutes with the System F translation.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-instantiate-2).

## Term translation commutes with type-binder instantiation

Type-binder discharge agrees for translated System F terms.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_tyInstantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-ty-instantiate).

## Term translation preserves weak call-by-value values

The System F translation preserves both weak-CBV value forms.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_value`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-value).

## Term translation simulates each weak call-by-value step

Every System F weak-CBV step is simulated by one Fω weak-CBV step.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.fromSystemF_step`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#from-system-f-step).

## Canonical embedding preserves single evaluation steps

The canonical embedding preserves individual System F evaluation steps.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.embed_step`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#embed-step).

## Canonical embedding preserves multistep evaluation

The canonical embedding preserves finite System F evaluation sequences.

Formalized by `Cslib.Languages.LambdaCalculus.FOmega.Tm.embed_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/FOmega/Embedding.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html#embed-steps).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The star/forall System F fragment inside pure Fω](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/system-f-2/the-star-forall-system-f-fragment-inside-pure-f)
