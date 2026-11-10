---
declaration: section
origin: cited
lean: Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_syntomic_of_surjective, Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_flat_lci_of_surjective, Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_isGorenstein_of_surjective, Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_syntomic, Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_flat_lci, Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_gorenstein
statement: formalized
proof: formalized
---

# 48.26 More on dualizing complexes

Section 48.26 of the Stacks Project, [Tag 0E4M](https://stacks.math.columbia.edu/tag/0E4M). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E4N, a lemma

[Tag 0E4N](https://stacks.math.columbia.edu/tag/0E4N) in the Stacks Project.

**`Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_syntomic_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexPullbackCriterion.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexPullbackCriterion.lean#L103). The attribute's comment: “case (1): f syntomic and surjective”.

> **Stacks Project, Tag 0E4N, case (1).** Let `f : X ⟶ Y` be a syntomic surjective morphism
> of locally Noetherian schemes and let `K` be an object of `D_QCoh(𝒪_Y)`. Then `K` is a dualizing
> complex on `Y` if and only if `Lf^*K` is a dualizing complex on `X`.

```lean
theorem isDualizingComplex_iff_derivedPullback_of_syntomic_of_surjective [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] (f : X ⟶ Y) [Surjective f] (hf : Syntomic f)
    (K : DerivedCategory Y.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor Y.Modules i).obj K).IsQuasicoherent) :
    IsDualizingComplex K ↔
      IsDualizingComplex
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          f.toLRSHom.toShHom).obj K)
```

**`Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_flat_lci_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexPullbackCriterion.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexPullbackCriterion.lean#L123). The attribute's comment: “case (2): f a surjective flat local complete intersection morphism”.

> **Stacks Project, Tag 0E4N, case (2).** Let `f : X ⟶ Y` be a surjective flat local complete
> intersection morphism of locally Noetherian schemes and let `K` be an object of `D_QCoh(𝒪_Y)`.
> Then `K` is a dualizing complex on `Y` if and only if `Lf^*K` is a dualizing complex on `X`.
>
> A flat local complete intersection morphism is syntomic ([Stacks, Tag 069K]), so this is
> case (1).

```lean
theorem isDualizingComplex_iff_derivedPullback_of_flat_lci_of_surjective [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] (f : X ⟶ Y) [Surjective f] [Flat f]
    (hlci : IsLocalCompleteIntersectionMorphism f) (K : DerivedCategory Y.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor Y.Modules i).obj K).IsQuasicoherent) :
    IsDualizingComplex K ↔
      IsDualizingComplex
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          f.toLRSHom.toShHom).obj K)
```

**`Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_isGorenstein_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexPullbackCriterion.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexPullbackCriterion.lean#L142). The attribute's comment: “case (3): f a surjective Gorenstein morphism of finite type”.

> **Stacks Project, Tag 0E4N, case (3).** Let `f : X ⟶ Y` be a surjective Gorenstein morphism
> of finite type of locally Noetherian schemes and let `K` be an object of `D_QCoh(𝒪_Y)`. Then `K`
> is a dualizing complex on `Y` if and only if `Lf^*K` is a dualizing complex on `X`.
>
> At an affine pair `V ⊆ f⁻¹(U)` on which `f` is still surjective, `f.appLE U V` is faithfully
> flat of finite type with Gorenstein fibre rings (`Scheme.Hom.isGorensteinRing_fiber_appLE`), and
> the ring-level statement is [Stacks, Tag 0E4D] case (3).

```lean
theorem isDualizingComplex_iff_derivedPullback_of_isGorenstein_of_surjective
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (f : X ⟶ Y) [Surjective f] [QuasiCompact f]
    [LocallyOfFiniteType f]
    (hGor : Scheme.Hom.IsGorenstein f (isLocallyNoetherian_fiber_of_locallyOfFiniteType f))
    (K : DerivedCategory Y.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor Y.Modules i).obj K).IsQuasicoherent) :
    IsDualizingComplex K ↔
      IsDualizingComplex
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          f.toLRSHom.toShHom).obj K)
```

**`Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexSyntomicDescent.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexSyntomicDescent.lean#L501). The attribute's comment: “variant: case (1) with a polynomial presentation p, the invertibility hInv and the tensor formula hTensor at each affine pair as explicit parameters; the tag is Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_syntomic_of_surjective”.

> **Stacks Project, Tag 0E4N, case (1).** Let `f : X ⟶ Y` be a syntomic surjection of locally
> Noetherian schemes and let `K` be an object of `D_QCoh(𝒪_Y)`. Then `K` is a dualizing complex on
> `Y` if and only if `Lf^*K` is a dualizing complex on `X`.
>
> Over an affine open `U ⊆ Y` and an affine open `V ⊆ f⁻¹(U)` on which `f` is still surjective the
> condition becomes the ring-level statement [Stacks, Tag 0E4D] for `f.appLE U V`, which is
> syntomic and surjective on spectra; the two sides are compared by the affine comparison square of
> [Stacks, Tag 08DW] and the globalisation is [Stacks, Tag 0A86].

```lean
theorem isDualizingComplex_iff_derivedPullback_of_syntomic [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] (f : X ⟶ Y) [Surjective f] (hf : Syntomic f)
    (p : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
      Dualizing.PolynomialPresentation (f.appLE U.1 V.1 hVU).hom)
    (hInv : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
      letI : IsNoetherianRing Γ(Y, U.1) := IsLocallyNoetherian.component_noetherian U
      letI : IsNoetherianRing Γ(X, V.1) := IsLocallyNoetherian.component_noetherian V
      letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory
        Γ(X, V.1)).choose
      MonoidalCategory.IsInvertible (Dualizing.relativeDualizingUnit (p U V hVU)))
    (hTensor : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1)
      (M : DerivedCategory (ModuleCat.{u} Γ(Y, U.1))),
      letI : IsNoetherianRing Γ(Y, U.1) := IsLocallyNoetherian.component_noetherian U
      letI : IsNoetherianRing Γ(X, V.1) := IsLocallyNoetherian.component_noetherian V
      letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory
        Γ(X, V.1)).choose
      Nonempty ((p U V hVU).upperShriekFunctor.{u, u}.obj M ≅
        ((derivedExtensionScalarsGeneral.{u, u, u}
            (f.appLE U.1 V.1 hVU).hom).functor.obj M) ⊗
          Dualizing.relativeDualizingUnit (p U V hVU)))
    (K : DerivedCategory Y.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor Y.Modules i).obj K).IsQuasicoherent) :
    IsDualizingComplex K ↔
      IsDualizingComplex ((derivedPullback f.toLRSHom.toShHom).obj K)
```

**`Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_flat_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexSyntomicDescent.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexSyntomicDescent.lean#L549). The attribute's comment: “variant: case (2) with a polynomial presentation p, the invertibility hInv and the tensor formula hTensor at each affine pair as explicit parameters; the tag is Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_flat_lci_of_surjective”.

> **Stacks Project, Tag 0E4N, case (2).** Let `f : X ⟶ Y` be a surjective flat local complete
> intersection morphism of locally Noetherian schemes and let `K` be an object of `D_QCoh(𝒪_Y)`.
> Then `K` is a dualizing complex on `Y` if and only if `Lf^*K` is a dualizing complex on `X`.
>
> A flat local complete intersection morphism is syntomic by [Stacks, Tag 069K], so this is
> case (1).

```lean
theorem isDualizingComplex_iff_derivedPullback_of_flat_lci [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] (f : X ⟶ Y) [Surjective f] [Flat f]
    (hlci : IsLocalCompleteIntersectionMorphism f)
    (p : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
      Dualizing.PolynomialPresentation (f.appLE U.1 V.1 hVU).hom)
    (hInv : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
      letI : IsNoetherianRing Γ(Y, U.1) := IsLocallyNoetherian.component_noetherian U
      letI : IsNoetherianRing Γ(X, V.1) := IsLocallyNoetherian.component_noetherian V
      letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory
        Γ(X, V.1)).choose
      MonoidalCategory.IsInvertible (Dualizing.relativeDualizingUnit (p U V hVU)))
    (hTensor : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1)
      (M : DerivedCategory (ModuleCat.{u} Γ(Y, U.1))),
      letI : IsNoetherianRing Γ(Y, U.1) := IsLocallyNoetherian.component_noetherian U
      letI : IsNoetherianRing Γ(X, V.1) := IsLocallyNoetherian.component_noetherian V
      letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory
        Γ(X, V.1)).choose
      Nonempty ((p U V hVU).upperShriekFunctor.{u, u}.obj M ≅
        ((derivedExtensionScalarsGeneral.{u, u, u}
            (f.appLE U.1 V.1 hVU).hom).functor.obj M) ⊗
          Dualizing.relativeDualizingUnit (p U V hVU)))
    (K : DerivedCategory Y.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor Y.Modules i).obj K).IsQuasicoherent) :
    IsDualizingComplex K ↔
      IsDualizingComplex ((derivedPullback f.toLRSHom.toShHom).obj K)
```

**`Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_gorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexSyntomicDescent.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DualizingComplexSyntomicDescent.lean#L589). The attribute's comment: “variant: case (3) with a polynomial presentation p, the fibre-ring Gorenstein property hGorRing and the tensor formula hTensor at each affine pair as explicit parameters; the tag is Stacks.Duality.isDualizingComplex_iff_derivedPullback_of_isGorenstein_of_surjective”.

> **Stacks Project, Tag 0E4N, case (3).** Let `f : X ⟶ Y` be a surjective Gorenstein morphism
> of finite type of locally Noetherian schemes and let `K` be an object of `D_QCoh(𝒪_Y)`. Then `K`
> is a dualizing complex on `Y` if and only if `Lf^*K` is a dualizing complex on `X`.
>
> A Gorenstein morphism is flat, and of finite type over a locally Noetherian target it is of
> finite presentation, so the reduction to affine pairs of case (1) applies verbatim; at an affine
> pair the ring-level statement is [Stacks, Tag 0E4D] case (3).

```lean
theorem isDualizingComplex_iff_derivedPullback_of_gorenstein [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] (f : X ⟶ Y) [Surjective f] [QuasiCompact f] [LocallyOfFiniteType f]
    (hF : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (hGor : Scheme.Hom.IsGorenstein f hF)
    (p : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
      letI : Algebra Γ(Y, U.1) Γ(X, V.1) := (f.appLE U.1 V.1 hVU).hom.toAlgebra
      Dualizing.PolynomialPresentation (algebraMap Γ(Y, U.1) Γ(X, V.1)))
    (hGorRing : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1)
      (q : Ideal Γ(Y, U.1)) [q.IsPrime],
      letI : Algebra Γ(Y, U.1) Γ(X, V.1) := (f.appLE U.1 V.1 hVU).hom.toAlgebra
      letI := Dualizing.isNoetherianRing_baseChange q.ResidueField (p U V hVU)
      Dualizing.IsGorensteinRing (q.Fiber Γ(X, V.1)))
    (hTensor : ∀ (U : Y.affineOpens) (V : X.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1)
      (M : DerivedCategory (ModuleCat.{u} Γ(Y, U.1))),
      letI : IsNoetherianRing Γ(Y, U.1) := IsLocallyNoetherian.component_noetherian U
      letI : IsNoetherianRing Γ(X, V.1) := IsLocallyNoetherian.component_noetherian V
      letI : Algebra Γ(Y, U.1) Γ(X, V.1) := (f.appLE U.1 V.1 hVU).hom.toAlgebra
      letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory
        Γ(X, V.1)).choose
      Nonempty ((p U V hVU).upperShriekFunctor.{u, u}.obj M ≅
        ((derivedExtensionScalarsGeneral.{u, u, u}
            (algebraMap Γ(Y, U.1) Γ(X, V.1))).functor.obj M) ⊗
          Dualizing.relativeDualizingUnit (p U V hVU)))
    (K : DerivedCategory Y.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor Y.Modules i).obj K).IsQuasicoherent) :
    IsDualizingComplex K ↔
      IsDualizingComplex ((derivedPullback f.toLRSHom.toShHom).obj K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.26, Tag 0E4M](https://stacks.math.columbia.edu/tag/0E4M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
