---
declaration: section
origin: cited
lean: PresheafOfModules.sheafify, PresheafOfModules.Sheafify.instUniqueSMulCandidate, PresheafOfModules.toSheafify, PresheafOfModules.sheafifyHomEquiv, PresheafOfModules.instPreservesFiniteLimitsSheafOfModulesSheafification, PresheafOfModules.instIsLeftAdjointSheafOfModulesSheafification, Stacks.SheafOfModules.ChangeOfRings.extendRestrictScalarsAdjunction, Stacks.Sheaves.RingedToposModules.extendRestrictScalarsAdjunction
statement: formalized
proof: formalized
---

# 18.11 Sheafification of presheaves of modules

Section 18.11 of the Stacks Project, [Tag 03CX](https://stacks.math.columbia.edu/tag/03CX). 4 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03CY, a lemma

[Tag 03CY](https://stacks.math.columbia.edu/tag/03CY) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules.sheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.sheafify#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch18.lean#L56) (StacksFrontier): “existence: the sheafification of the underlying abelian presheaf is a sheaf of O^#-modules”. References: EGA I (1.3.13), “more general”; SGA 4 IV (12.4).
- [`PresheafOfModules.Sheafify.instUniqueSMulCandidate`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.Sheafify.instUniqueSMulCandidate#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch18.lean#L58) (StacksFrontier): “uniqueness of the O^#-module structure compatible with the square”.
- [`PresheafOfModules.toSheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.toSheafify#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch18.lean#L60) (StacksFrontier): “the commutative square F ⟶ F^#”.
- [`PresheafOfModules.sheafifyHomEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.sheafifyHomEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch18.lean#L61) (StacksFrontier): “in addition: maps to sheaves of O^#-modules factor uniquely through F^#”.

## Tag 03EI, a lemma

[Tag 03EI](https://stacks.math.columbia.edu/tag/03EI) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules.instPreservesFiniteLimitsSheafOfModulesSheafification`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instPreservesFiniteLimitsSheafOfModulesSheafification#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch18.lean#L64) (StacksFrontier): “left exact: sheafification preserves finite limits”.
- [`PresheafOfModules.instIsLeftAdjointSheafOfModulesSheafification`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instIsLeftAdjointSheafOfModulesSheafification#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch18.lean#L66) (StacksFrontier): “right exact: sheafification is a left adjoint, so it preserves colimits”. References: SGA 7 VI (3.1(a)), “partial”.

## Tag 03CZ, a lemma

[Tag 03CZ](https://stacks.math.columbia.edu/tag/03CZ) in the Stacks Project.

**`Stacks.SheafOfModules.ChangeOfRings.extendRestrictScalarsAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtendScalarsAdjunction.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtendScalarsAdjunction.lean#L192).

> **Stacks 03CZ**: extension of scalars along a morphism `α : R ⟶ R'` of sheaves of rings
> is left adjoint to restriction of scalars along `α`. Concretely, for a sheaf of `R`-modules
> `G` and a sheaf of `R'`-modules `F` there is a bijection
> `Hom_{R'}(R' ⊗_R G, F) = Hom_R(G, F_R)`, natural in `G` and `F`.

```lean
noncomputable def extendRestrictScalarsAdjunction :
    extendScalars.{v} α ⊣ SheafOfModules.restrictScalars.{v} α
```

Declarations registered for the tag:

- [`Stacks.Sheaves.RingedToposModules.extendRestrictScalarsAdjunction`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean#L694), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ChangeOfRingsSheafification.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ChangeOfRingsSheafification.lean#L100) (StacksFrontier).

## Tag 0930, a lemma

[Tag 0930](https://stacks.math.columbia.edu/tag/0930) in the Stacks Project.

**`Stacks.NoncommChangeOfRings.Silver.restrictScalars_fullyFaithful_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RestrictScalarsEpiFullyFaithful.lean, line 957](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RestrictScalarsEpiFullyFaithful.lean#L957).

> Restriction of scalars along an epimorphism `α : R ⟶ R'` of sheaves of rings on a site is
> fully faithful. Equivalently, for any two sheaves of `R'`-modules every morphism of their
> restrictions to `R` is uniquely `R'`-linear. The site is assumed small relative to the universe
> of the sections of the rings (`Small.{u} C`, `LocallySmall.{u} C`).

```lean
theorem restrictScalars_fullyFaithful_of_epi [Epi α] :
    Nonempty (SheafOfModules.restrictScalars.{v} α).FullyFaithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.11, Tag 03CX](https://stacks.math.columbia.edu/tag/03CX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
