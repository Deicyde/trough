---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_completionSheaf, AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_completionSheaf_of_isClosed, AlgebraicGeometry.FormalSpace.isIso_toSheafify_completionSubfunctor_affineOver, AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheaf_of_isClosed, AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheaf, AlgebraicGeometry.FormalSpace.isIso_toSheafify_completionSubfunctor, AlgebraicGeometry.FormalSpace.completionAlongClosedSubset, AlgebraicGeometry.Space.isPullback_completionSheafMap
statement: formalized
proof: formalized
---

# 87.14 Completion along a closed subset

Section 87.14 of the Stacks Project, [Tag 0AIX](https://stacks.math.columbia.edu/tag/0AIX). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AIY, a lemma

[Tag 0AIY](https://stacks.math.columbia.edu/tag/0AIY) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_completionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAffineMcQuillan.lean, line 895](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAffineMcQuillan.lean#L895). The attribute's comment: “McQuillan affine formal algebraic space”.

> **Stacks 0AIY.** Let `S` be a scheme, let `X = Spec A` be an affine scheme over `S` lying
> in the big fppf site and let `T ⊆ |X|` be a closed subset. The completion of `X` along `T` —
> the fppf sheaf attached to the functor sending `U` to the set of morphisms `f : U ⟶ X` with
> `f(|U|) ⊆ T` — is a McQuillan affine formal algebraic space: it is the directed colimit of the
> affine thickenings `Spec (A ⧸ J)` over the ideals `J` with `V(J) = T`, and the projections from
> the inverse limit of the section rings of that presentation onto each stage are surjective.

```lean
theorem hasSomeSurjectivePresentation_completionSheaf
    (T : Set ((BigFppfOver.toScheme B S hS).obj (affineOver B S hS hA f))) (hT : IsClosed T)
    (hatlas : HasStageAtlas B S hS hA f (PrimeSpectrum.vanishingIdeal T)) :
    HasSomeSurjectivePresentation B S hS
      (Space.completionSheaf B S hS (yoneda.obj (affineOver B S hS hA f))
        (supportedPoints B S hS (affineOver B S hS hA f) T))
```

**`AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_completionSheaf_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAffineStageAtlas.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAffineStageAtlas.lean#L116). The attribute's comment: “McQuillan affine formal algebraic space”.

> **Stacks 0AIY.** Let `S` be a scheme, let `X = Spec A` be an affine scheme over `S` lying
> in the big fppf site and let `T ⊆ |X|` be a closed subset. The completion of `X` along `T` —
> the fppf sheaf attached to the functor sending `U` to the set of morphisms `f : U ⟶ X` with
> `f(|U|) ⊆ T` — is a McQuillan affine formal algebraic space.
>
> This is `AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_completionSheaf` with its
> atlas hypothesis discharged by `AlgebraicGeometry.FormalSpace.hasStageAtlas`.

```lean
theorem hasSomeSurjectivePresentation_completionSheaf_of_isClosed
    (T : Set ((BigFppfOver.toScheme B S hS).obj (affineOver B S hS hA f))) (hT : IsClosed T) :
    HasSomeSurjectivePresentation B S hS
      (Space.completionSheaf B S hS (yoneda.obj (affineOver B S hS hA f))
        (supportedPoints B S hS (affineOver B S hS hA f) T))
```

**`AlgebraicGeometry.FormalSpace.isIso_toSheafify_completionSubfunctor_affineOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSetTheoretic.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSetTheoretic.lean#L386). The attribute's comment: “the functor”.

> Let `X = Spec A` be an affine scheme over `S` lying in the site and `T ⊆ |X|` a subset. The
> functor sending an object `U` of the big fppf site of `S` to the morphisms `f : U ⟶ X` with
> `f(|U|) ⊆ T` is an fppf sheaf: the map to its sheafification, the completion of
> `AlgebraicGeometry.Space.completionSheaf`, is an isomorphism.

```lean
theorem isIso_toSheafify_completionSubfunctor_affineOver {A : Type u} [CommRing A]
    (hA : B.Contains (Spec (.of A))) (f : Spec (.of A) ⟶ S)
    (T : Set ((BigFppfOver.toScheme B S hS).obj (affineOver B S hS hA f))) :
    IsIso (toSheafify (BigFppfOver.topology B S hS)
      (Space.completionSubfunctor B S hS (yoneda.obj (affineOver B S hS hA f))
        (supportedPoints B S hS (affineOver B S hS hA f) T)).toFunctor)
```

## Tag 0AIZ, a lemma

[Tag 0AIZ](https://stacks.math.columbia.edu/tag/0AIZ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheaf_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlgebraicSpaceAtlas.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlgebraicSpaceAtlas.lean#L515).

> **Stacks 0AIZ.** Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `T ⊆ |X|` be a closed subset. The completion `X_{/T}` of `X` along `T` — the fppf sheaf attached
> to the functor sending `U` to the morphisms `f : U ⟶ X` with `f(|U|) ⊆ T` — is a formal
> algebraic space over `S`.
>
> The affine étale charts of `X` are those of
> `AlgebraicGeometry.FormalSpace.exists_affine_etale_charts`, the inverse image of `T` on each is
> the set of points supported in a closed subset
> (`AlgebraicGeometry.FormalSpace.exists_isClosed_preimage_eq_supportedPoints`), the stage atlas
> of each chart completion is `AlgebraicGeometry.FormalSpace.hasStageAtlas`, and the set-theoretic
> condition is `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_completionSheaf`;
> with these the atlas argument of
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheaf` applies.

```lean
theorem isFormalAlgebraicSpace_completionSheaf_of_isClosed
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X)) (hT : @IsClosed _ (Space.pointTopology B S hS X) T) :
    IsFormalAlgebraicSpace B S hS (Space.completionSheaf B S hS X T)
```

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalAlgebraicSpace.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalAlgebraicSpace.lean#L236). The attribute's comment: “assumes the affine étale charts of X as hA, str, a, ha, hcov, their closed point sets as hTi and hTpts, the affine case's HasStageAtlas as hstage, and the 0AIS condition as hset”.

> **Stacks 0AIZ.** Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `T ⊆ |X|` be a closed subset. The completion `X_{/T}` of `X` along `T` — the fppf sheaf attached
> to the functor sending `U` to the morphisms `f : U ⟶ X` with `f(|U|) ⊆ T` — is a formal
> algebraic space over `S`: the completions of the affine charts of `X` along the inverse images
> of `T` form an atlas of `X_{/T}`, and each of them is an affine formal algebraic space by the
> affine case, Stacks 0AIY.
>
> The affine étale charts of `X`, the description of the inverse image of `T` on each of them as
> the points supported in a closed subset, the per-chart hypothesis `HasStageAtlas` of the
> affine case and the set-theoretic condition of Stacks 0AIS are carried as hypotheses; see the
> section "What is assumed" of this file.

```lean
theorem isFormalAlgebraicSpace_completionSheaf
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X))
    {Ix : Type (u + 1)} {A : Ix → Type u} [∀ i, CommRing (A i)]
    (hA : ∀ i, B.Contains (AlgebraicGeometry.Spec (.of (A i))))
    (str : ∀ i, AlgebraicGeometry.Spec (.of (A i)) ⟶ S)
    (a : ∀ i, yoneda.obj (affineOver B S hS (hA i) (str i)) ⟶ X)
    (ha : ∀ i, ∃ hai : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.sheafifiedULiftMap B S hS (a i)).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ q ↦ Space.IsEtaleULift.{u + 1} B S hS q.hom)
        (Space.sheafifiedULiftMap B S hS (a i)).hom hai)
    (hcov : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
          Sheaf.instHasColimitsOfSize
        Sheaf.IsLocallySurjective
          (Sigma.desc fun i ↦ Space.sheafifiedULiftMap B S hS (a i)))
    (Ti : ∀ i, Set ((BigFppfOver.toScheme B S hS).obj (affineOver B S hS (hA i) (str i))))
    (hTi : ∀ i, IsClosed (Ti i))
    (hTpts : ∀ i, Space.pointsMap B S hS _ (a i) ⁻¹' T =
      supportedPoints B S hS (affineOver B S hS (hA i) (str i)) (Ti i))
    (hstage : ∀ i, HasStageAtlas B S hS (hA i) (str i)
      (PrimeSpectrum.vanishingIdeal (Ti i)))
    (hset : SatisfiesSetTheoreticCondition B S hS (Space.completionSheaf B S hS X T)) :
    IsFormalAlgebraicSpace B S hS (Space.completionSheaf B S hS X T)
```

**`AlgebraicGeometry.FormalSpace.isIso_toSheafify_completionSubfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSetTheoretic.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSetTheoretic.lean#L374). The attribute's comment: “the functor”.

> Let `X` be an algebraic space over `S` and `T` a set of points of `X`. The functor sending
> an object `U` of the big fppf site of `S` to the morphisms `f : U ⟶ X` with `f(|U|) ⊆ T` is an
> fppf sheaf: the map to its sheafification, the completion `X_{/T}` of
> `AlgebraicGeometry.Space.completionSheaf`, is an isomorphism.

```lean
theorem isIso_toSheafify_completionSubfunctor
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X)) :
    IsIso (toSheafify (BigFppfOver.topology B S hS)
      (Space.completionSubfunctor B S hS X T).toFunctor)
```

## Tag 0AMC, a definition

[Tag 0AMC](https://stacks.math.columbia.edu/tag/0AMC) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.completionAlongClosedSubset`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlgebraicSpaceAtlas.lean, line 568](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlgebraicSpaceAtlas.lean#L568).

> **Stacks 0AMC.** Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `T ⊆ |X|` be a closed subset. The *completion of `X` along `T`* is the formal algebraic space
> `X_{/T}` of Stacks 0AIZ: the fppf sheaf `AlgebraicGeometry.Space.completionSheaf` attached to the
> functor sending `U` to the morphisms `f : U ⟶ X` with `f(|U|) ⊆ T`, as an object of the full
> subcategory of formal algebraic spaces over `S`, the membership being
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheaf_of_isClosed`.

```lean
def completionAlongClosedSubset {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T) :
    ObjectProperty.FullSubcategory (IsFormalAlgebraicSpace B S hS)
```

## Tag 0APV, a lemma

[Tag 0APV](https://stacks.math.columbia.edu/tag/0APV) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Completion.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Completion.lean#L230). The attribute's comment: “cartesian square”.

> **Stacks 0APV.** Completion is compatible with base change: for a morphism `f : X' ⟶ X`
> of presheaves on the big fppf site of `S` and a set `T` of points of `X`, the square formed
> by the completion of `X'` along `|f|⁻¹ T`, the completion of `X` along `T` and the two
> ambient sheaves is a cartesian square of fppf sheaves.

```lean
theorem isPullback_completionSheafMap
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X' ⟶ X)
    (T : Set (points B S hS X)) :
    IsPullback
      (completionSheafInclusion B S hS X' (pointsMap B S hS X' f ⁻¹' T))
      (completionSheafMap B S hS f T)
      (sheafifiedULiftMap B S hS f)
      (completionSheafInclusion B S hS X T)
```

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpacesULift_completionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Completion.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Completion.lean#L245). The attribute's comment: “representable by algebraic spaces”.

> **Stacks 0APV.** For a morphism `f : X' ⟶ X` of algebraic spaces over `S` and a set `T`
> of points of `X`, the induced morphism of completions `X'_{/|f|⁻¹ T} ⟶ X_{/T}` is
> representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpacesULift_completionMap
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (points B S hS X)) :
    IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
      (completionSheafMap B S hS f T).hom
```

## Tag 0GB9, a lemma

[Tag 0GB9](https://stacks.math.columbia.edu/tag/0GB9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isReduction_completionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlongClosedSubsetReduction.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlongClosedSubsetReduction.lean#L379).

> **Stacks 0GB9.** Let `X` be an algebraic space over `S` and let `T ⊆ |X|` be a closed
> subset. The reduction of the completion `X_{/T}` of `X` along `T` is the reduced induced
> closed subspace `Z` of `X` supported on `T`: the canonical morphism `Z ⟶ X_{/T}` exhibits `Z`
> as the reduction of `X_{/T}`.

```lean
theorem isReduction_completionSheaf :
    IsReduction B S hS (Space.completionSheaf B S hS X T)
      (reducedClosedSubsetSheaf B S hS hX T hT)
      (reducedClosedSubsetToCompletionSheaf B S hS hX T hT)
```

## Tag 0GBA, a lemma

[Tag 0GBA](https://stacks.math.columbia.edu/tag/0GBA) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAdicStar_completionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionTypes.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionTypes.lean#L430). The attribute's comment: “adic*”.

> **Stacks 0GBA (1).** Let `X = Spec A` be an affine scheme over `S` in the big fppf site and
> let `T ⊆ |X|` be a closed subset whose complement is quasi-compact, that is a constructible
> closed subset. Then the completion `X_{/T}` is an adic\* affine formal algebraic space.

```lean
theorem isAdicStar_completionSheaf
    (T : Set (Space.points B S hS (yoneda.obj (affineOver B S hS hA f))))
    (hT : @IsClosed _
      (Space.pointTopology B S hS (yoneda.obj (affineOver B S hS hA f))) T)
    (hqc : @IsCompact _
      (Space.pointTopology B S hS (yoneda.obj (affineOver B S hS hA f))) Tᶜ) :
    IsAdicStar B S hS
      (Space.completionSheaf B S hS (yoneda.obj (affineOver B S hS hA f)) T)
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_completionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionTypes.lean, line 447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionTypes.lean#L447). The attribute's comment: “Noetherian”.

> **Stacks 0GBA (3).** Let `X = Spec A` be a Noetherian affine scheme over `S` in the big
> fppf site and let `T ⊆ |X|` be a closed subset. Then the completion `X_{/T}` is a Noetherian
> affine formal algebraic space.

```lean
theorem isNoetherian_completionSheaf [IsNoetherianRing A]
    (T : Set (Space.points B S hS (yoneda.obj (affineOver B S hS hA f))))
    (hT : @IsClosed _
      (Space.pointTopology B S hS (yoneda.obj (affineOver B S hS hA f))) T) :
    IsNoetherian B S hS
      (Space.completionSheaf B S hS (yoneda.obj (affineOver B S hS hA f)) T)
```

**`AlgebraicGeometry.FormalSpace.isIso_completionComparison_adicQuotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineRigEtaleAlgebraization.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineRigEtaleAlgebraization.lean#L167). The attribute's comment: “formal spectrum, for the constructed quotient-system presentation `AlgebraicGeometry.FormalSpace.adicQuotientSystem` of the completion”.

> Let `X = Spec A` be an affine scheme over `S` in the big fppf site and let `T = V(I)` for a
> finitely generated ideal `I ⊆ A`. Then the canonical comparison `Spf (A^∧) ⟶ X_{/T}` is an
> isomorphism, for the presentation `adicQuotientSystem` of the `I`-adic completion `A^∧`.

```lean
theorem isIso_completionComparison_adicQuotientSystem (hA : B.Contains (Spec (.of A)))
    (f : Spec (.of A) ⟶ S) (I : Ideal A) (hI : I.FG) :
    IsIso (completionComparison B S hS hA f I (adicQuotientSystem B S hS hA f I hI)
      (quotientSystemCompatible_adicQuotientSystem B S hS hA f I hI))
```

**`AlgebraicGeometry.FormalSpace.isIso_completionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalSpectrum.lean, line 936](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalSpectrum.lean#L936). The attribute's comment: “formal spectrum”. References: EGA I (10.8.5), “affine case Spf(Â)”; EGA I (10.10.1), “Spf(A) = X\_\{/X}”; EGA III (5.1.1), “Spf(A) ≅ Ŷ”.

> **Stacks 0GBA (2).** Let `X = Spec A` be an affine scheme over `S` in the big fppf site
> and let `T = V(I)` be the zero locus of a finitely generated ideal `I ⊆ A`. Then the
> canonical comparison from the formal spectrum of the `I`-adic completion of `A` to the
> completion of `X` along `T` is an isomorphism, so `X_{/T} = Spf (A^∧)`.

```lean
theorem isIso_completionComparison
    (hI : I.FG)
    (D : AdicQuotientSystem B S hS I)
    (hD : QuotientSystemCompatible B S hS f I D) :
    IsIso (completionComparison B S hS hA f I D hD)
```

## Tag 0APW, a lemma

[Tag 0APW](https://stacks.math.columbia.edu/tag/0APW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAdicStar_zeroLocusCompletion_of_isCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedCompletionAdicStar.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedCompletionAdicStar.lean#L250). The attribute's comment: “clause (1)”.

> **Stacks 0APW (1).** Let `X = Spec A` be an affine scheme over `S` and `T = V(I)` a closed
> subset. If the formal completion `X_{/T}` is countably indexed and `T = V(e 0, e 1, …)` is cut
> out by countably many elements of `A`, then `X_{/T}` is adic\*.
>
> By `exists_isCofinalVanishingSequence_of_isCountablyIndexed` the countable indexedness gives a
> cofinal sequence `J` of ideals cutting out `T`; by `countableCompletionIsoZeroLocusCompletion`
> the completion is the colimit of the `Spec (A ⧸ J n)`, which is adic\* by
> `isAdicStar_countableCompletion`.

```lean
theorem isAdicStar_zeroLocusCompletion_of_isCountablyIndexed (I : Ideal A) (e : ℕ → A)
    (heI : PrimeSpectrum.zeroLocus (I : Set A) = PrimeSpectrum.zeroLocus (Set.range e))
    (hX : IsCountablyIndexed B S hS (zeroLocusCompletion B S hS hA f I)) :
    IsAdicStar B S hS (zeroLocusCompletion B S hS hA f I)
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_not_isAdicStar_zeroLocusCompletion_gabber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedCompletionAdicStar.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedCompletionAdicStar.lean#L268). The attribute's comment: “clause (2)”.

> **Stacks 0APW (2).** The conclusion of clause (1) fails without the countability of the
> equations: for Gabber's ring `A` and `T = V(x_α : α ∈ ω₁)`, the formal completion `X_{/T}` of
> `X = Spec A` is countably indexed but not adic\*, and so `T` is not cut out by countably many
> elements of `A`.
>
> The completion is identified with `gabberCompletionSheaf`, the colimit along the cofinal
> sequence `J_n = (x_α^(n+1))`, by `countableCompletionIsoZeroLocusCompletion`, and
> `isCountablyIndexed_not_isAdicStar_gabberCompletionSheaf` is the statement for that sheaf. The
> last conjunct follows from clause (1).

```lean
theorem isCountablyIndexed_not_isAdicStar_zeroLocusCompletion_gabber (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (hA : B.Contains (Spec (.of GabberRing.{u})))
    (f : Spec (.of GabberRing.{u}) ⟶ S) :
    IsCountablyIndexed B S hS (zeroLocusCompletion B S hS hA f gabberVanishingIdeal.{u}) ∧
      ¬ IsAdicStar B S hS (zeroLocusCompletion B S hS hA f gabberVanishingIdeal.{u}) ∧
      ¬ ∃ e : ℕ → GabberRing.{u},
        PrimeSpectrum.zeroLocus (gabberVanishingIdeal.{u} : Set GabberRing.{u}) =
          PrimeSpectrum.zeroLocus (Set.range e)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.14, Tag 0AIX](https://stacks.math.columbia.edu/tag/0AIX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
