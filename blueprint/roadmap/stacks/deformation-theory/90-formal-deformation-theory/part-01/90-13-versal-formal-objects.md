---
declaration: section
origin: cited
lean: Deformation.schlessingerConditionS1_of_versal, Deformation.isVersal_iff_differential_surjective_and_base_lifts, Deformation.exists_least_lifting_ideal, Deformation.exists_versalFormalObject, Deformation.exists_versalFormalObject_of_schlessingerConditions
statement: formalized
proof: formalized
---

# 90.13 Versal formal objects

Section 90.13 of the Stacks Project, [Tag 06SX](https://stacks.math.columbia.edu/tag/06SX). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06SY, a lemma

[Tag 06SY](https://stacks.math.columbia.edu/tag/06SY) in the Stacks Project.

**`Deformation.schlessingerConditionS1_of_versal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Basic.lean, line 788](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Basic.lean#L788).

> A predeformation category with a versal formal object satisfies
> Schlessinger's condition (S1).

```lean
public theorem schlessingerConditionS1_of_versal
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p)
    (ξ : FormalObject p)
    (hξ : IsVersal hp.cofibered ξ) :
    SchlessingerConditionS1 p
```

## Tag 06IU, a lemma

[Tag 06IU](https://stacks.math.columbia.edu/tag/06IU) in the Stacks Project.

**`Deformation.isVersal_iff_differential_surjective_and_base_lifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/VersalCriterion.lean, line 1263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/VersalCriterion.lean#L1263).

> Surjectivity on tangent spaces together with lifting the map of underlying
> complete local algebras across every small-extension triangle characterizes
> versality for a predeformation category satisfying (S1) and (S2).

```lean
public theorem isVersal_iff_differential_surjective_and_base_lifts
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hpre : IsPredeformationCategory 𝓕.p)
    (hS1 : SchlessingerConditionS1 𝓕.p)
    (hS2 : SchlessingerConditionS2 𝓕.p)
    (ξ : FormalObject 𝓕.p)
    (pushforwards : ChosenPushforwards 𝓕.p) :
    IsVersal hpre.cofibered ξ ↔
      (Function.Surjective
        (mapIsomorphismClasses
          (categoryOfElements_projection_isCofibered
            (restrictedCoyoneda ξ.base))
          hpre.cofibered
          (associatedMorphism
            hpre.cofibered ξ pushforwards).toBasedFunctor
          (artinianDualNumbers Λ k)) ∧
       ∀ ⦃B A : ArtinianLocalAlgCat.{u, max v w, w} Λ k⦄ (f : B ⟶ A),
         InfinitesimalLifting.IsSmallExtension
           (CommRingCat.ofHom f.hom.toRingHom) →
         ∀ ⦃y x : FormalObject 𝓕.p⦄ (g : y ⟶ x),
           (FormalObject.projection (p := 𝓕.p)).IsHomLift
             (artinianToComplete.map f) g →
         ∀ (a : ξ ⟶ x), ∃ b : ξ.base ⟶ y.base,
             b ≫ g.base = a.base)
```

## Tag 06SZ, a lemma

[Tag 06SZ](https://stacks.math.columbia.edu/tag/06SZ) in the Stacks Project.

**`Deformation.exists_least_lifting_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/LeastLiftingIdeal.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/LeastLiftingIdeal.lean#L126).

> The ideals of the kernel of a surjection `B ⟶ A` over whose quotients
> an object over `A` lifts have a least member when (S1) holds.

```lean
theorem exists_least_lifting_ideal
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    (hS1 : SchlessingerConditionS1 p)
    {B : ArtinianLocalAlgCat.{u, v, w} Λ k} (x : F)
    (f : B ⟶ p.obj x) (hf : Function.Surjective f.hom)
    (hI : maximalIdeal B * RingHom.ker f.hom.toRingHom = ⊥) :
    let lifts : Set (Ideal B) :=
      {J | J ≤ RingHom.ker f.hom.toRingHom ∧
        ∃ (C : ArtinianLocalAlgCat.{u, v, w} Λ k)
          (q : B ⟶ C) (g : C ⟶ p.obj x),
          Function.Surjective q.hom ∧
          RingHom.ker q.hom.toRingHom = J ∧
          q ≫ g = f ∧
          ∃ (y : F) (hy : p.obj y = C) (a : y ⟶ x),
            p.map a = eqToHom hy ≫ g};
    ∃ J : Ideal B, J ∈ lifts ∧ (∀ K : Ideal B, K ∈ lifts → J ≤ K)
```

## Tag 06IW, a lemma

[Tag 06IW](https://stacks.math.columbia.edu/tag/06IW) in the Stacks Project.

**`Deformation.exists_versalFormalObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/VersalExistence.lean, line 1981](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/VersalExistence.lean#L1981). The attribute's comment: “existence of a versal formal object”. References: SGA 7 VI (1.11), “(i)+(ii) => versal”.

> **Schlessinger's existence theorem.** A predeformation category over `𝒞_Λ` which satisfies
> his conditions (S1) and (S2) and whose tangent space is finite dimensional has a versal formal
> object. The formal object is the limit of the tower of presentations of Stacks 06SZ over a
> power series algebra on a basis of the tangent space, taken over a complete local algebra which
> is formally smooth over `Λ`; versality is checked through the criterion of Stacks 06IU, whose
> condition (1) comes from the choice of the bottom stage of the tower and whose condition (2) is
> the key lifting step.
>
> The finite-dimensionality hypothesis speaks about the canonical `k`-vector space structure of
> Stacks 06IH on the tangent space, which is available as soon as `𝓕` is a predeformation
> category whose functor of isomorphism classes satisfies (S2); both of those are consequences
> of the hypotheses — the second is `Deformation.schlessingerConditionS2_of_isIsomorphismClasses`
> applied to `hS2` — so they are installed by the `letI` prefix of `hfin` rather than assumed.

```lean
public theorem exists_versalFormalObject
    (Λ : Type u) (k : Type w) [CommRing Λ] [IsNoetherianRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hpre : IsPredeformationCategory.{u, v, w} 𝓕.p)
    (hS1 : SchlessingerConditionS1 𝓕.p)
    (hS2 : SchlessingerConditionS2 𝓕.p)
    (hfin :
      letI : Fact (IsPredeformationCategory.{u, v, w} 𝓕.p) := ⟨hpre⟩
      letI : Fact (SchlessingerConditionS2
          (CategoryOfElements.π (isomorphismClasses 𝓕 hpre.cofibered))) :=
        ⟨schlessingerConditionS2_of_isIsomorphismClasses 𝓕 hpre.cofibered hS2 (Or.inl hpre)⟩
      FiniteDimensional k (tangentSpaceArtinian.{u, w, v} Λ k
        (isomorphismClasses 𝓕 hpre.cofibered))) :
    ∃ ξ : FormalObject 𝓕.p, IsVersal hpre.cofibered ξ
```

## Tag 0D3G, a remark

[Tag 0D3G](https://stacks.math.columbia.edu/tag/0D3G) in the Stacks Project.

**`Deformation.exists_versalFormalObject_of_schlessingerConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/SetValuedExistence.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/SetValuedExistence.lean#L307). The attribute's comment: “(H1) + (H2) + (H3) implies a versal formal object exists”. References: SGA 7 VI (1.11), “set-valued functor”.

> **Stacks Project, Tag 0D3G.** A set-valued predeformation functor on `𝒞_Λ` satisfying
> Schlessinger's conditions (H1) and (H2) — that is, (S1) and (S2) in the elementary form of
> Stacks 06HY — and his condition (H3), the finite-dimensionality of the tangent space, has a
> versal formal object.
>
> This is Stacks 06IW read through the identifications of Stacks 06GT and 06HY: the category of
> elements of `F` is a predeformation category satisfying (S1) and (S2), and its functor of
> isomorphism classes is a copy of `F` by `Deformation.elementsIsomorphismClassesEquiv`, so the
> tangent space whose dimension is bounded is `TF`.
>
> Condition (H3) is stated about `TF = F(k[ε])` itself, for the canonical `k`-vector-space
> structure of Stacks 06IH transported to it by
> `Deformation.setValuedTangentSpaceLinearEquiv`; the form Stacks 06IW consumes is obtained
> inside the proof by `Deformation.finiteDimensional_tangentSpace_isomorphismClasses_of_setValued`.
> The predeformation and (S2) properties that structure needs are the images of `hpre` and `hH2`
> under Stacks 06GT and 06HY, the latter followed by
> `Deformation.schlessingerConditionS2_of_isIsomorphismClasses`, so the statement installs them
> itself rather than assuming them.

```lean
public theorem exists_versalFormalObject_of_schlessingerConditions
    (Λ : Type u) (k : Type w) [CommRing Λ] [IsNoetherianRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k]
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t)
    (hpre : IsPredeformationFunctor.{u, v, w, t} F)
    (hH1 : ∀ ⦃A₁ A₂ A A₁₂ : ArtinianLocalAlgCat.{u, max v w, w} Λ k⦄
      (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A), Function.Surjective f₂.hom →
        ∀ (g₁ : A₁₂ ⟶ A₁) (g₂ : A₁₂ ⟶ A₂) (hPB : IsPullback g₂ g₁ f₂ f₁),
          Function.Surjective (fibreProductComparison F g₁ g₂ f₁ f₂ hPB.w))
    (hH2 : ∀ ⦃A A₀ Aε B : ArtinianLocalAlgCat.{u, max v w, w} Λ k⦄
      (d : A ⟶ A₀) (e : Aε ⟶ A₀), IsDualNumberProjection e →
        ∀ (g : B ⟶ A) (gε : B ⟶ Aε) (hPB : IsPullback gε g e d),
          Function.Bijective (fibreProductComparison F g gε d e hPB.w))
    (hH3 :
      letI : Fact (IsPredeformationCategory.{u, v, w}
          (BasedCategory.ofFunctor (CategoryOfElements.π F)).p) :=
        ⟨(isPredeformationCategory_iff F).2 hpre⟩
      letI : Fact (SchlessingerConditionS2 (CategoryOfElements.π
          (isomorphismClasses (BasedCategory.ofFunctor (CategoryOfElements.π F))
            ((isPredeformationCategory_iff F).2 hpre).cofibered))) :=
        ⟨schlessingerConditionS2_of_isIsomorphismClasses
          (BasedCategory.ofFunctor (CategoryOfElements.π F))
          ((isPredeformationCategory_iff F).2 hpre).cofibered
          ((schlessingerConditionS2_elements_iff F).2 hH2)
          (Or.inl ((isPredeformationCategory_iff F).2 hpre))⟩
      letI := setValuedTangentSpaceAddCommGroup.{u, v, w, t} F
        ((isPredeformationCategory_iff F).2 hpre)
      letI := setValuedTangentSpaceModule.{u, v, w, t} F
        ((isPredeformationCategory_iff F).2 hpre)
      FiniteDimensional k (tangentSpaceArtinian.{u, w, v} Λ k F)) :
    ∃ ξ : FormalObject (CategoryOfElements.π F),
      IsVersal ((isPredeformationCategory_iff F).2 hpre).cofibered ξ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.13, Tag 06SX](https://stacks.math.columbia.edu/tag/06SX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
