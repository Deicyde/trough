---
declaration: section
origin: cited
lean: Deformation.presentationMorphism_isEquivalence_of_isSmooth_of_fiber_essSurj, Deformation.isSmooth_presentationGroupoid, Deformation.isDeformationFunctor_twoFibreProductOver_self, Deformation.exact_selfBoundaryLinearMap_tangentProjPair, Deformation.isProrepresentable_presentationGroupoid, Deformation.hasSmoothPresentation_iff_isFiniteDimensionalDeformationCategory, Deformation.exists_isSmooth_isProrepresentable_presentation
statement: formalized
proof: formalized
---

# 90.26 Presentations of deformation categories

Section 90.26 of the Stacks Project, [Tag 06L0](https://stacks.math.columbia.edu/tag/06L0). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06L1, a lemma

[Tag 06L1](https://stacks.math.columbia.edu/tag/06L1) in the Stacks Project.

**`Deformation.presentationMorphism_isEquivalence_of_isSmooth_of_fiber_essSurj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/QuotientEquivalence.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/QuotientEquivalence.lean#L44). The attribute's comment: “quotient_equivalence”.

> The canonical quotient morphism associated to a smooth presentation is an equivalence if
> the presentation is essentially surjective over the residue field.

```lean
theorem presentationMorphism_isEquivalence_of_isSmooth_of_fiber_essSurj
    (hp : IsCofiberedInGroupoids p)
    (hf : IsSmooth f)
    (h₀ : (fiberFunctor f (residueFieldObject Λ k)).EssSurj) :
    (presentationMorphism p U f.toFunctor f.w
      (presentationGroupoid p U f.toFunctor f.w hp)).1.IsEquivalence
```

**`Deformation.isSmooth_presentationGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Smooth.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Smooth.lean#L546). The attribute's comment: “smooth_groupoid”.

> A smooth presentation has a smooth associated groupoid in functors.
>
> This is one of the two covering declarations of Stacks 06L1; the other is the equivalence
> criterion for the quotient morphism,
> `Deformation.presentationMorphism_isEquivalence_of_isSmooth_of_fiber_essSurj`. See the
> implementation notes.

```lean
theorem isSmooth_presentationGroupoid
    (hp : IsCofiberedInGroupoids p)
    (hf : IsSmooth f) :
    GroupoidInFunctors.IsSmooth
      ((presentationGroupoid p U f.toFunctor f.w hp).toGroupoidInFunctors)
```

## Tag 06L6, a lemma

[Tag 06L6](https://stacks.math.columbia.edu/tag/06L6) in the Stacks Project.

**`Deformation.isDeformationFunctor_twoFibreProductOver_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductDeformation.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Applications/TwoFibreProductDeformation.lean#L373). The attribute's comment: “part (1), that the 2-fibre product is a deformation functor; the exact sequence 0 → Inf(ℱ) → T(U ×_{f,ℱ,f} U) → TU ⊕ TU of part (2) is not covered”.

> **Stacks Project, Tag 06L6, part (1).** Let `U : 𝒞_Λ → Sets` be a deformation functor,
> `ℱ` a deformation category and `f : U → ℱ` a `1`-morphism of categories cofibered in
> groupoids over `𝒞_Λ`. Then `𝒲 = U ×_{f, ℱ, f} U` is a deformation functor: it is a
> deformation category, and every one of its infinitesimal automorphism groups vanishes, which
> by Tag 06K0 is exactly the statement that it is cofibered in setoids, i.e. that it is a
> functor.
>
> The deformation-category half is Tag 06L5 part (1),
> `Deformation.isDeformationCategory_twoFibreProductOver`, read through
> `Deformation.isDeformationCategory_iff` for the two outer legs. The vanishing is the source's
> "the fact that `Inf(U) = (0)`": the fibres of the category of elements of a set-valued functor
> are thin (`Deformation.elementsFiber_isThin`), hence so are the fibres of the `2`-fibre
> product (`Deformation.isThin_fibre_twoFibreProductOver`), and over a thin fibre there is no
> room for a nontrivial automorphism at all.
>
> The cofibered-in-groupoids witness is quantified over rather than taken from the first
> component because `Deformation.IsCofiberedInGroupoids` is a proposition, so the infinitesimal
> automorphism group does not depend on which witness is supplied.

```lean
theorem isDeformationFunctor_twoFibreProductOver_self
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (U : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t)
    {F : Type u₃} [Category.{v₃} F]
    (pF : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (f : U.Elements ⥤ F)
    (hf : f ⋙ pF = CategoryOfElements.π U)
    (hU : IsDeformationFunctor U)
    (hF : IsDeformationCategory pF) :
    let p𝒲 := TwoFibreProductOver.structureFunctor
      (CategoryOfElements.π U) (CategoryOfElements.π U) pF f f
    IsDeformationCategory p𝒲 ∧
      ∀ (hcof : IsCofiberedInGroupoids p𝒲)
        {A₀ Aε : ArtinianLocalAlgCat.{u, max v w, w} Λ k}
        {w₀ : p𝒲.Fiber A₀} {wε : p𝒲.Fiber Aε}
        (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hpair : IsCanonicalDualNumberPair g e)
        (i : w₀.1 ⟶ wε.1) (hi : p𝒲.IsHomLift g i),
        infinitesimalAutomorphisms hcof g e hpair i hi = ⊥
```

**`Deformation.exact_selfBoundaryLinearMap_tangentProjPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductSelfExact.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Applications/TwoFibreProductSelfExact.lean#L384). The attribute's comment: “part (2), the exact sequence of k-vector spaces 0 → Inf(ℱ) → T(U ×_{f,ℱ,f} U) → TU ⊕ TU”.

> **Stacks Project, Tag 06L6, part (2).** Let `U : 𝒞_Λ → Sets` be a deformation functor, `ℱ` a
> deformation category and `f : U → ℱ` a `1`-morphism of categories cofibered in groupoids over
> `𝒞_Λ`. Then the tangent space of `𝒲 = U ×_{f, ℱ, f} U` fits into an exact sequence of
> `k`-vector spaces
>
> `0 → Inf(ℱ) → T𝒲 → TU ⊕ TU`,
>
> where the first map is the `k`-linear boundary map `δ` of the six-term sequence and the second
> is the pair of the maps induced by the two projections. Exactness at `Inf(ℱ)` is injectivity of
> `δ` and exactness at `T𝒲` is the kernel-equals-image statement; both maps are `k`-linear, and
> the three terms are the `k`-vector spaces of Tag 06IH, taken at an arbitrary coordinate module.
>
> Exactness at `T𝒲` is part (2) of Tag 06L5 for the two legs
> (`Deformation.exact_boundaryLinearMap_tangentProjPair`). Exactness at `Inf(ℱ)` is what the self
> `2`-fibre product adds, and it is the source's `Inf(U) = (0)`: the fibres of the category of
> elements of a set-valued functor are thin
> (`Deformation.isThin_fiber_comp_elementsProjection`), so an isomorphism between two quadruples
> `(k[M], y'₀, y'₀, c' ∘ α ∘ b')` has both components the identity and its comparison square reads
> `α = α'`.

```lean
public theorem exact_selfBoundaryLinearMap_tangentProjPair
    (U : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t)
    (pF : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k) (f : U.Elements ⥤ F)
    (hf : f ⋙ pF = CategoryOfElements.π U) (hU : IsDeformationFunctor.{u, v, w} U)
    (hF : IsDeformationCategory.{u, v, w} pF) {y₀ : U.Elements}
    (PH : ChosenPushforwardsAt (f ⋙ pF) y₀) (PF : ChosenPushforwardsAt pF (f.obj y₀))
    (M : FGModuleCat.{max v w} k) :
    Function.Injective (selfBoundaryLinearMap.{u, v, w} pF U f
        (isDeformationCategory_comp_of_isDeformationFunctor.{u, v, w} U pF f hf hU) hF PH PF M) ∧
      Function.Exact
        (selfBoundaryLinearMap.{u, v, w} pF U f
          (isDeformationCategory_comp_of_isDeformationFunctor.{u, v, w} U pF f hf hU) hF PH PF M)
        (tangentProjPair.{u, v, w} pF f f
          (isDeformationCategory_comp_of_isDeformationFunctor.{u, v, w} U pF f hf hU)
          (isDeformationCategory_comp_of_isDeformationFunctor.{u, v, w} U pF f hf hU) hF M)
```

## Tag 06L7, a lemma

[Tag 06L7](https://stacks.math.columbia.edu/tag/06L7) in the Stacks Project.

**`Deformation.isProrepresentable_presentationGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Prorepresentable.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Prorepresentable.lean#L402). The attribute's comment: “the hom-set universe of ℱ is at most that of 𝒞_Λ: the base is written ArtinianLocalAlgCat.{u, max v v₃ w, w} with v₃ the hom-set universe of ℱ, because the criterion of 06KG part (2) is available only at value universe equal to the hom-set universe”.

> Let `ℱ` be a deformation category, let `U : 𝒞_Λ → Sets` be a prorepresentable functor and let
> `f : U → ℱ` be a `1`-morphism of categories cofibered in groupoids. Let `(U, R, s, t, c)` be the
> groupoid in functors on `𝒞_Λ` constructed from `f` in Stacks 06KY. If `dim_k Inf(ℱ) < ∞`, then
> `(U, R, s, t, c)` is prorepresentable.
>
> The finite-dimensionality hypothesis is read at one basepoint `y₀` of `U` and one choice `PF` of
> pushforwards there.

```lean
public theorem isProrepresentable_presentationGroupoid
    (hU : IsProrepresentable U) (hF : IsDeformationCategory.{u, max v v₃, w} pF)
    {y₀ : U.Elements} (PF : ChosenPushforwardsAt pF (f.obj y₀))
    (hInf : FiniteDimensional k
      ↥((infinitesimalAutomorphismLinearLift.{u, max v v₃, w} PF hF.satisfiesRS).functor.obj
        (FGModuleCat.of k (ULift.{max v v₃} k)))) :
    GroupoidInFunctors.IsProrepresentable
      ((presentationGroupoid pF U f hover hF.predeformation.cofibered).toGroupoidInFunctors)
```

## Tag 06L8, a theorem

[Tag 06L8](https://stacks.math.columbia.edu/tag/06L8) in the Stacks Project.

**`Deformation.hasSmoothPresentation_iff_isFiniteDimensionalDeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean#L532). The attribute's comment: “the tag in full: ℱ admits a presentation by a smooth prorepresentable groupoid in functors on 𝒞_Λ iff (1) ℱ is a deformation category, (2) dim_k Tℱ is finite and (3) dim_k Inf(ℱ) is finite. Both directions, at the general universes of the chapter: ℱ has hom-set universe v and the base is ArtinianLocalAlgCat.{u, max v w, w}, with no universe equation imposed. The standing hypothesis of the source that ℱ be cofibered in groupoids is not carried: it is part of condition (1) on one side, and on the other it is derived from the presentation by Deformation.isCofiberedInGroupoids_of_equivalenceOver. The forward direction goes through Stacks 06L2 rather than through the construction of Stacks 06L8 itself, which Deformation.exists_isSmooth_isProrepresentable_presentation carries at the restricted universe”. References: SGA 7 VI (2.12), “more general”.

> **Stacks Project, Tag 06L8.** Let `ℱ` be a category cofibered in groupoids over `𝒞_Λ`.
> Then `ℱ` admits a presentation by a smooth prorepresentable groupoid in functors on `𝒞_Λ` if
> and only if `ℱ` is a deformation category, `dim_k Tℱ` is finite and `dim_k Inf(ℱ)` is finite.
>
> The direction from the three conditions to a presentation is Tag 06L2, whose minimal
> presentation is in particular a smooth prorepresentable one; the converse is
> `Deformation.isFiniteDimensionalDeformationCategory_of_hasSmoothPresentation`, which is parts
> (1), (2) and (3) of Tag 06KU transported along the presentation. Being cofibered in groupoids
> is not a hypothesis here: it is part of condition (1) on one side and a consequence of the
> presentation on the other.

```lean
theorem hasSmoothPresentation_iff_isFiniteDimensionalDeformationCategory [IsNoetherianRing Λ]
    [Module.Finite Λ k] :
    HasSmoothPresentation.{u, v, w} p ↔ IsFiniteDimensionalDeformationCategory.{u, v, w} p
```

**`Deformation.exists_isSmooth_isProrepresentable_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Existence.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Existence.lean#L155). The attribute's comment: “the construction of the tag's existence direction: (1)(2)(3) ⟹ ℱ admits a presentation by a smooth prorepresentable groupoid in functors on 𝒞_Λ, built as the source builds it, from a versal formal object and the groupoid in functors of 06KY. Only that direction, and only when the hom-set universe of ℱ equals that of k, the restriction 06L7 carries here. The tag in full — the biconditional, at the general universes, both directions — is Deformation.hasSmoothPresentation_iff_isFiniteDimensionalDeformationCategory, whose existence direction goes through 06L2 instead and whose converse direction is Deformation.isFiniteDimensionalDeformationCategory_of_hasSmoothPresentation, proved from part (3) of 06KU, Inf([U/R]) = Ker(ds ⊕ dt), which the library now has as Deformation.quotientInfinitesimalBoundary_exact”.

> **Stacks Project, Tag 06L8**, the existence direction. A category `ℱ` cofibered in
> groupoids over `𝒞_Λ` which is a deformation category and whose tangent space and space of
> infinitesimal automorphisms are finite-dimensional over `k` has a presentation by a smooth
> prorepresentable groupoid in functors on `𝒞_Λ`.
>
> The proof of the source. Condition (RS) gives (S1) and (S2) by Tag 06J7, so Schlessinger's
> existence theorem, Tag 06IW, produces a versal formal object `ξ` over a complete local algebra
> `R` from the finite-dimensionality of the tangent space. Put `U = R̲|_{𝒞_Λ}`; the associated
> morphism `ξ̲ : U → ℱ` of Tag 06HC is smooth, which is what versality of `ξ` says, and the
> groupoid in functors `(U, R, s, t, c)` built from it is the one of Tag 06KY. Tag 06L1 makes it
> smooth and its quotient morphism an equivalence — the quotient morphism is an equivalence
> because `ξ̲` is essentially surjective, which follows from smoothness together with essential
> surjectivity on the special fibre, and the latter holds because the special fibre of `ℱ` is
> equivalent to a point. Tag 06L7 makes it prorepresentable from the finite-dimensionality of
> the infinitesimal automorphisms.

```lean
theorem exists_isSmooth_isProrepresentable_presentation
    (p : F ⥤ ArtinianLocalAlgCat.{u, w, w} Λ k)
    (hp : IsDeformationCategory.{u, w, w} p)
    (hT : FiniteDimensional k
      ↥(tangentModuleAt.{u, w, w} (BasedCategory.ofFunctor p) hp
        (FGModuleCat.of k (ULift.{w} k))))
    (hInf : ∀ (x : F) (P : ChosenPushforwardsAt p x),
      p.obj x = residueFieldObject.{u, w, w} Λ k →
      FiniteDimensional k
        ↥((infinitesimalAutomorphismLinearLift.{u, w, w} P hp.satisfiesRS).functor.obj
          (FGModuleCat.of k (ULift.{w} k)))) :
    ∃ G : GroupoidInFunctors.{_, w, w} (ArtinianLocalAlgCat.{u, w, w} Λ k),
      GroupoidInFunctors.IsSmooth G ∧
        GroupoidInFunctors.IsProrepresentable.{u, w, w, w} G ∧
          Nonempty (Presentation G p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.26, Tag 06L0](https://stacks.math.columbia.edu/tag/06L0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
