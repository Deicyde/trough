---
declaration: section
origin: cited
lean: Deformation.quotient_satisfiesRS, Deformation.quotient_isDeformationCategory, Deformation.quotientInfinitesimalBoundary_exact, Deformation.quotientTangentEquiv
statement: formalized
proof: formalized
---

# 90.24 Deformation categories as quotients of groupoids in functors

Section 90.24 of the Stacks Project, [Tag 06KS](https://stacks.math.columbia.edu/tag/06KS). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06KT, a lemma

[Tag 06KT](https://stacks.math.columbia.edu/tag/06KT) in the Stacks Project.

**`Deformation.quotient_satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/RimSchlessinger.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/GroupoidQuotient/RimSchlessinger.lean#L150).

> The quotient of a smooth groupoid in functors whose object and arrow functors satisfy
> condition (RS) also satisfies condition (RS).

```lean
public theorem quotient_satisfiesRS
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (G : GroupoidInFunctors (ArtinianLocalAlgCat.{u, v, w} Λ k))
    (hG : GroupoidInFunctors.IsSmooth G)
    (hU : SatisfiesRS (Functor.Elements.π G.objects))
    (hR : SatisfiesRS (Functor.Elements.π G.arrows)) :
    SatisfiesRS (Grothendieck.forget (evaluationFunctor G))
```

## Tag 06KU, a lemma

[Tag 06KU](https://stacks.math.columbia.edu/tag/06KU) in the Stacks Project.

**`Deformation.quotient_isDeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/DeformationCategory.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/GroupoidQuotient/DeformationCategory.lean#L123). The attribute's comment: “quotient\_deformation\_category”.

> The quotient of a smooth groupoid of deformation functors is a deformation category.

```lean
public theorem quotient_isDeformationCategory
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (G : GroupoidInFunctors.{_, _, t} (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hG : GroupoidInFunctors.IsSmooth G)
    (hU : IsDeformationFunctor G.objects)
    (hR : IsDeformationFunctor G.arrows) :
    IsDeformationCategory (Grothendieck.forget (evaluationFunctor G))
```

**`Deformation.quotientInfinitesimalBoundary_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/InfinitesimalAutomorphisms.lean, line 807](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/GroupoidQuotient/InfinitesimalAutomorphisms.lean#L807). The attribute's comment: “part (3): Inf([U/R]) = Ker(ds ⊕ dt : TR → TU ⊕ TU), as the exactness of 0 → Inf([U/R]) → TR → TU ⊕ TU. The two differentials are the maps on tangent modules induced by s and t at an arbitrary coordinate module M, and Inf([U/R]) is the value at M of the k-linear lift of the infinitesimal automorphisms of the image in [U/R] of a point y₀ of U, taken with an arbitrary choice PF of pushforwards there. No hypothesis is carried beyond the tag's own: G smooth, U and R deformation functors”.

> **Stacks Project, Tag 06KU, part (3).** Let `(U, R, s, t, c)` be a smooth groupoid in
> functors on `𝒞_Λ` whose functors of objects and of arrows are deformation functors. Then the
> space of infinitesimal automorphisms of the quotient is the kernel of the differential of the
> source-and-target map,
>
> `Inf([U/R]) = Ker(ds ⊕ dt : TR → TU ⊕ TU)`,
>
> in the form of the exact sequence of `k`-vector spaces
>
> `0 → Inf([U/R]) → TR → TU ⊕ TU`:
>
> the boundary map is injective and its image is the kernel of the pair of the two differentials.
>
> The identification is the one of Tag 06L6 part (2) for the quotient morphism `q : U → [U/R]`,
> whose self `2`-fibre product `U ×_{q, [U/R], q} U` is the arrow functor: an arrow of the groupoid
> over `A` with source `x` and target `y` is an isomorphism over `A` between the images of `x` and
> of `y` in the quotient, and that comparison is an equivalence on every strict fibre, hence an
> isomorphism of tangent modules.

```lean
public theorem quotientInfinitesimalBoundary_exact
    (hG : GroupoidInFunctors.IsSmooth G)
    (hU : IsDeformationFunctor.{u, v, w} G.objects)
    (hR : IsDeformationFunctor.{u, v, w} G.arrows) {y₀ : G.objects.Elements}
    (PF : ChosenPushforwardsAt (Grothendieck.forget (evaluationFunctor G))
      ((quotientMorphism G).obj y₀))
    (M : FGModuleCat.{max v w} k) :
    Function.Injective (quotientInfinitesimalBoundary.{u, v, w, t} G hG hU hR PF M) ∧
      Function.Exact (quotientInfinitesimalBoundary.{u, v, w, t} G hG hU hR PF M)
        (LinearMap.prod
          (tangentMapAt.{u, v, w} (arrowsBasedDeformationCategory G hR)
            (objectsBasedDeformationCategory G hU) (elementsBasedFunctor G.source) M)
          (tangentMapAt.{u, v, w} (arrowsBasedDeformationCategory G hR)
            (objectsBasedDeformationCategory G hU)
            (elementsBasedFunctor G.target) M))
```

**`Deformation.quotientTangentEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/TangentSpace.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/GroupoidQuotient/TangentSpace.lean#L144). The attribute's comment: “quotient\_tangent\_space”.

> The canonical tangent space of a smooth quotient is the cokernel of
> the source-minus-target differential.

```lean
public noncomputable def quotientTangentEquiv
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (G : GroupoidInFunctors (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (hG : GroupoidInFunctors.IsSmooth G)
    (hU : IsDeformationFunctor G.objects)
    (hR : IsDeformationFunctor G.arrows) :
    let 𝓡 := BasedCategory.ofFunctor (Functor.Elements.π G.arrows)
    let 𝓤 := BasedCategory.ofFunctor (Functor.Elements.π G.objects)
    let 𝓠 := BasedCategory.ofFunctor (Grothendieck.forget (evaluationFunctor G))
    let h𝓡 := ((isDeformationCategory_iff G.arrows).2 hR).predeformation
    let h𝓤 := ((isDeformationCategory_iff G.objects).2 hU).predeformation
    let h𝓠 := quotient_isPredeformationCategory G hU hR
    let s2𝓡 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓡 h𝓡.cofibered (schlessingerConditionS2_of_satisfiesRS hR.2) (Or.inl h𝓡)
    let s2𝓤 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓤 h𝓤.cofibered (schlessingerConditionS2_of_satisfiesRS hU.2) (Or.inl h𝓤)
    let s2𝓠 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓠 h𝓠.cofibered
      (schlessingerConditionS2_of_satisfiesRS (quotient_satisfiesRS G hG hU.2 hR.2))
      (Or.inl h𝓠)
    letI : Fact (IsPredeformationCategory 𝓡.p) := ⟨h𝓡⟩
    letI : Fact (IsPredeformationCategory 𝓤.p) := ⟨h𝓤⟩
    letI : Fact (IsPredeformationCategory 𝓠.p) := ⟨h𝓠⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓡 h𝓡.cofibered))) := ⟨s2𝓡⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓤 h𝓤.cofibered))) := ⟨s2𝓤⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓠 h𝓠.cofibered))) := ⟨s2𝓠⟩
    let TR := artinianTangentSpace Λ k (isomorphismClasses 𝓡 h𝓡.cofibered)
    let TU := artinianTangentSpace Λ k (isomorphismClasses 𝓤 h𝓤.cofibered)
    let TQ := artinianTangentSpace Λ k (isomorphismClasses 𝓠 h𝓠.cofibered)
    let ds : TR →ₗ[k] TU := IsLinearMap.mk'
      (differential h𝓡.cofibered h𝓤.cofibered (elementsBasedFunctor G.source))
      (differential_isLinearMap 𝓡 𝓤 h𝓡 h𝓤 s2𝓡 s2𝓤 (elementsBasedFunctor G.source))
    let dt : TR →ₗ[k] TU := IsLinearMap.mk'
      (differential h𝓡.cofibered h𝓤.cofibered (elementsBasedFunctor G.target))
      (differential_isLinearMap 𝓡 𝓤 h𝓡 h𝓤 s2𝓡 s2𝓤 (elementsBasedFunctor G.target))
    let dq : TU →ₗ[k] TQ := IsLinearMap.mk'
      (differential h𝓤.cofibered h𝓠.cofibered
        (⟨quotientMorphism G, quotientMorphism_over G⟩ : BasedFunctor 𝓤 𝓠))
      (differential_isLinearMap 𝓤 𝓠 h𝓤 h𝓠 s2𝓤 s2𝓠
        (⟨quotientMorphism G, quotientMorphism_over G⟩ : BasedFunctor 𝓤 𝓠))
    { e : (TU ⧸ LinearMap.range (ds - dt)) ≃ₗ[k] TQ //
      ∀ x : TU, e (Submodule.Quotient.mk x) = dq x }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.24, Tag 06KS](https://stacks.math.columbia.edu/tag/06KS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
