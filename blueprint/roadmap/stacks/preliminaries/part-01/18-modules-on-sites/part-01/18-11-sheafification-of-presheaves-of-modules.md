---
declaration: section
origin: cited
lean: PresheafOfModules.sheafify, PresheafOfModules.Sheafify.instUniqueSMulCandidate, PresheafOfModules.toSheafify, PresheafOfModules.sheafifyHomEquiv, PresheafOfModules.instPreservesFiniteLimitsSheafOfModulesSheafification, PresheafOfModules.instIsLeftAdjointSheafOfModulesSheafification, Stacks.SheafOfModules.ChangeOfRings.extendRestrictScalarsAdjunction, Stacks.Sheaves.RingedToposModules.extendRestrictScalarsAdjunction
statement: formalized
proof: formalized
---

# 18.11 Sheafification of presheaves of modules

Section 18.11 of the Stacks Project, [Tag 03CX](https://stacks.math.columbia.edu/tag/03CX). 4 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03CY, a lemma

[Tag 03CY](https://stacks.math.columbia.edu/tag/03CY) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules.sheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.sheafify#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L57) (StacksFrontier): “existence: the sheafification of the underlying abelian presheaf is a sheaf of O^#-modules”. References: EGA I (1.3.13), “more general”; SGA 4 IV (12.4).
- [`PresheafOfModules.Sheafify.instUniqueSMulCandidate`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.Sheafify.instUniqueSMulCandidate#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L59) (StacksFrontier): “uniqueness of the O^#-module structure compatible with the square”.
- [`PresheafOfModules.toSheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.toSheafify#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L61) (StacksFrontier): “the commutative square F ⟶ F^#”.
- [`PresheafOfModules.sheafifyHomEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.sheafifyHomEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L62) (StacksFrontier): “in addition: maps to sheaves of O^#-modules factor uniquely through F^#”.

## Tag 03EI, a lemma

[Tag 03EI](https://stacks.math.columbia.edu/tag/03EI) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules.instPreservesFiniteLimitsSheafOfModulesSheafification`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instPreservesFiniteLimitsSheafOfModulesSheafification#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L65) (StacksFrontier): “left exact: sheafification preserves finite limits”.
- [`PresheafOfModules.instIsLeftAdjointSheafOfModulesSheafification`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instIsLeftAdjointSheafOfModulesSheafification#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L67) (StacksFrontier): “right exact: sheafification is a left adjoint, so it preserves colimits”. References: SGA 7 VI (3.1(a)), “partial”.

## Tag 03CZ, a lemma

[Tag 03CZ](https://stacks.math.columbia.edu/tag/03CZ) in the Stacks Project.

**`Stacks.SheafOfModules.ChangeOfRings.extendRestrictScalarsAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtendScalarsAdjunction.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtendScalarsAdjunction.lean#L192).

> **Stacks 03CZ**: extension of scalars along a morphism `α : R ⟶ R'` of sheaves of rings
> is left adjoint to restriction of scalars along `α`. Concretely, for a sheaf of `R`-modules
> `G` and a sheaf of `R'`-modules `F` there is a bijection
> `Hom_{R'}(R' ⊗_R G, F) = Hom_R(G, F_R)`, natural in `G` and `F`.

```lean
noncomputable def extendRestrictScalarsAdjunction :
    extendScalars.{v} α ⊣ SheafOfModules.restrictScalars.{v} α
```

Declarations registered for the tag:

- [`Stacks.Sheaves.RingedToposModules.extendRestrictScalarsAdjunction`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean#L694), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ChangeOfRingsSheafification.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ChangeOfRingsSheafification.lean#L100) (StacksFrontier).

## Tag 0930, a lemma

[Tag 0930](https://stacks.math.columbia.edu/tag/0930) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.restrictScalars_fullyFaithful_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/HomAfterLocalization.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/HomAfterLocalization.lean#L229). The attribute's comment: “rings commutative as in Stacks: the epimorphism is one of sheaves of commutative rings, `Sheaf J CommRingCat`”.

> **Stacks Tag 0930.** Restriction of scalars along an epimorphism `f : 𝒪 ⟶ 𝒪'` of sheaves
> of commutative rings on a site is fully faithful: for `𝒪'`-modules `𝒢₁, 𝒢₂`,
> `Hom_𝒪'(𝒢₁, 𝒢₂) = Hom_𝒪(𝒢₁, 𝒢₂)`.
>
> Unlike `Stacks.NoncommChangeOfRings.Silver.restrictScalars_fullyFaithful_of_epi`, the
> noncommutative variant, which proves the same for an epimorphism of sheaves of not necessarily
> commutative rings, the epimorphism is asked for in the
> category of sheaves of commutative rings — which is the category [Stacks, Tag 0996] localizes in
> — and no smallness hypothesis on the site is needed. The argument is that a local section `r` of
> `𝒪'` satisfies `r ⊗ 1 = 1 ⊗ r` locally, which says exactly that an additive map of the
> restrictions is already `𝒪'`-linear.

```lean
theorem restrictScalars_fullyFaithful_of_epi [Epi f] :
    Nonempty (SheafOfModules.restrictScalars.{u} (R := Stacks.SheafOfModules.Tensor.ringSheaf O)
      (R' := Stacks.SheafOfModules.Tensor.ringSheaf S)
      (ObjectProperty.homMk
        (Functor.whiskerRight f.hom (forget₂ CommRingCat RingCat)))).FullyFaithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.11, Tag 03CX](https://stacks.math.columbia.edu/tag/03CX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
