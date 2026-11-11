---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isSeparated_of_elementaryDistinguishedSquare, AlgebraicGeometry.Space.not_forall_isSeparated_of_isElementaryDistinguishedSquare, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_separating_strictTransforms_and_closures, AlgebraicGeometry.Space.exists_isBlowupAlong_isIso_strictTransformSpaceToBlowUp_over_closure, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_surjective_finite_flat_etaleLocalRing, AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_le_strictTransformInAmbient, AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_eq_strictTransformInAmbient_unconditional, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_isProper_extension_of_isEtale
statement: formalized
proof: formalized
---

# 81.14 Compactifications

Section 81.14 of the Stacks Project, [Tag 0F44](https://stacks.math.columbia.edu/tag/0F44). 9 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F45, a lemma

[Tag 0F45](https://stacks.math.columbia.edu/tag/0F45) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_of_elementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SeparatedFromElementarySquare.lean, line 1235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SeparatedFromElementarySquare.lean#L1235). The attribute's comment: “with the additional hypothesis that V ×\_X V ⟶ V ×\_Y V is closed; the source's hypothesis list is insufficient, see the counterexample in the module docstring”.

> **Stacks 0F45.** A morphism of algebraic spaces `g : X ⟶ Y` over `S` is separated once an
> elementary distinguished square `(U ⊆ X, f : V ⟶ X)` has `U ⟶ Y` and `V ⟶ Y` separated and
> has the comparison maps `U ×_X V ⟶ U ×_Y V` and `V ×_X V ⟶ V ×_Y V` closed.
>
> The second comparison map is **not** among the source's hypotheses: Lemma 81.14.1 asks only for
> `U ×_X V ⟶ U ×_Y V` to be closed, and its proof asserts that
> `(V ×_Y V) ×_{X ×_Y X, Δ} X = V`, which is false — that base change is `V ×_X V`. The source's
> hypothesis list is insufficient, and the counterexample in this module's docstring shows the
> extra hypothesis cannot be dropped. This statement is therefore the repaired one.

```lean
public theorem isSeparated_of_elementaryDistinguishedSquare
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X V Y : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Y)
    (g : X ⟶ Y) (U : Subfunctor X) (f : V ⟶ X)
    (hsq : AlgebraicGeometry.Space.IsElementaryDistinguishedSquare B S hS hX U f)
    (hU : AlgebraicGeometry.Space.IsSeparated B S hS (U.ι ≫ g))
    (hV : AlgebraicGeometry.Space.IsSeparated B S hS (f ≫ g))
    (hUV : IsClosedMorphism B S hS (pullback.mapDesc U.ι f g))
    (hVV : IsClosedMorphism B S hS (pullback.mapDesc f f g)) :
    AlgebraicGeometry.Space.IsSeparated B S hS g
```

**`AlgebraicGeometry.Space.not_forall_isSeparated_of_isElementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SeparatedFromElementarySquareCounterexample.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SeparatedFromElementarySquareCounterexample.lean#L553). The attribute's comment: “counterexample: the statement as published is false; the corrected statement, with V ×\_X V ⟶ V ×\_Y V also closed, is isSeparated\_of\_elementaryDistinguishedSquare”.

> **Stacks 0F45 as published is false.** It is not true that a morphism `g : X ⟶ Y` of
> algebraic spaces over `S` is separated as soon as an elementary distinguished square
> `(U ⊆ X, f : V ⟶ X)` has `U ⟶ Y` and `V ⟶ Y` separated and `U ×_X V ⟶ U ×_Y V` closed. The
> counterexample is
> `AlgebraicGeometry.AffineLineInvolution.exists_isElementaryDistinguishedSquare_not_isSeparated`,
> over the field `ℚ`. The statement with the further hypothesis that `V ×_X V ⟶ V ×_Y V` is closed
> is `AlgebraicGeometry.Space.isSeparated_of_elementaryDistinguishedSquare`.

```lean
theorem not_forall_isSeparated_of_isElementaryDistinguishedSquare :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      {X V Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
      (_hY : IsAlgebraicSpace B S hS Y) (g : X ⟶ Y) (U : Subfunctor X) (f : V ⟶ X),
      IsElementaryDistinguishedSquare B S hS hX U f →
      IsSeparated B S hS (U.ι ≫ g) → IsSeparated B S hS (f ≫ g) →
      IsClosedMorphism B S hS (pullback.mapDesc U.ι f g) → IsSeparated B S hS g
```

## Tag 0F46, a lemma

[Tag 0F46](https://stacks.math.columbia.edu/tag/0F46) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_separating_strictTransforms_and_closures`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupStrictTransformSeparationQcqs.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupStrictTransformSeparationQcqs.lean#L62).

> **Stacks 0F46.**  Let `S` be a scheme, let `X` be a quasi-compact and quasi-separated
> algebraic space over `S` and let `U ⊆ X` be a quasi-compact open subspace.
>
> 1. If `Z₁, Z₂ ⊆ X` are closed subspaces of finite presentation with `Z₁ ∩ Z₂ ∩ U = ∅`, then
>    there is a `U`-admissible blowup `b : X' ⟶ X` such that the strict transforms of `Z₁` and
>    `Z₂` are disjoint.  The blowup is recorded with its centre `Y`, a finitely presented closed
>    subspace of `X` disjoint from `U` in which `b` is the blowup, and the strict transforms are
>    taken relative to the exceptional divisor `b⁻¹Y`.
> 2. If `T₁, T₂ ⊆ |U|` are disjoint constructible closed subsets, then there is a `U`-admissible
>    blowup `b : X' ⟶ X` such that the closures of `T₁` and `T₂` in `|X'|` are disjoint, `Tᵢ`
>    being read in `|X'|` through `b`, which is an isomorphism over `U`.

```lean
theorem exists_isAdmissibleBlowup_separating_strictTransforms_and_closures
    (hZ : B.Contains (⊤_ Scheme.{u})) {X : AlgebraicSpaces B S hS}
    (hXqc : IsQuasiCompactSpace B S hS X.1) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (U : OpenSubspaces B S hS X.1) (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor) :
    (∀ Z₁ Z₂ : ClosedSubspaces B S hS X.1,
      IsFinitePresentation B S hS Z₁.1.ι → IsFinitePresentation B S hS Z₂.1.ι →
        Disjoint (subspacePointSet B S hS X.1 U.1 ∩ subspacePointSet B S hS X.1 Z₁.1)
          (subspacePointSet B S hS X.1 Z₂.1) →
        ∃ (X' : AlgebraicSpaces B S hS) (b : X' ⟶ X) (Y : ClosedSubspaces B S hS X.1),
          IsAdmissibleBlowup B S hS U b ∧ IsFinitePresentation B S hS Y.1.ι ∧
            Disjoint (subspacePointSet B S hS X.1 U.1) (subspacePointSet B S hS X.1 Y.1) ∧
              IsBlowupAlong B S hS Y b ∧
                Disjoint (strictTransformPointSet (closedSubspaceSpaceι X Z₁) b
                    (preimageClosedSubspace b Y).1)
                  (strictTransformPointSet (closedSubspaceSpaceι X Z₂) b
                    (preimageClosedSubspace b Y).1)) ∧
      ∀ T₁ T₂ : Set (points B S hS U.1.toFunctor), IsClosed T₁ → IsClosed T₂ →
        Topology.IsConstructible T₁ → Topology.IsConstructible T₂ → Disjoint T₁ T₂ →
        ∃ (X' : AlgebraicSpaces B S hS) (b : X' ⟶ X), IsAdmissibleBlowup B S hS U b ∧
          Disjoint (closure (pointsMap B S hS _ b.hom ⁻¹' (pointsMap B S hS _ U.1.ι '' T₁)))
            (closure (pointsMap B S hS _ b.hom ⁻¹' (pointsMap B S hS _ U.1.ι '' T₂)))
```

## Tag 0F47, a lemma

[Tag 0F47](https://stacks.math.columbia.edu/tag/0F47) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isBlowupAlong_isIso_strictTransformSpaceToBlowUp_over_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupIsoNearClosure.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupIsoNearClosure.lean#L84).

> **Stacks 0F47.**  Let `S` be a scheme, let `f : X ⟶ Y` be a proper morphism of algebraic
> spaces over `S` with `Y` quasi-compact and quasi-separated, let `V ⊆ Y` be a quasi-compact open
> subspace and let `T ⊆ |V|` be a closed subset such that `f|_{f⁻¹(V)} : f⁻¹(V) ⟶ V` is an
> isomorphism over an open neighbourhood `W` of `T` in `V`.  Then there is a `V`-admissible blowup
> `b : Y' ⟶ Y`, the blowup of `Y` in a closed subspace `Yc` of finite presentation whose points
> avoid those of `V`, such that the strict transform `f' : X' ⟶ Y'` of `f` is an isomorphism over
> an open neighbourhood `W'` of the closure of `T` in `|Y'|`.
>
> An open subspace of `V` is an open subspace `W` of `Y` with `W ≤ V`, and `f|_{f⁻¹(V)}` is an
> isomorphism over it exactly when `f` is, i.e. when `f⁻¹(W) ⟶ W` is an isomorphism.  The centre
> `Yc` is recorded, since the strict transform is taken relative to it.  The closure of `T` in
> `|Y'|` is the closure of the set of points of `Y'` mapping into the image of `T` in `|Y|`, as in
> Stacks 0F46 (`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_disjoint_closure`).  The source
> also asks `X` to be quasi-compact and quasi-separated; this follows from properness of `f` over
> the quasi-compact and quasi-separated `Y`, is not used, and is omitted.

```lean
theorem exists_isBlowupAlong_isIso_strictTransformSpaceToBlowUp_over_closure
    {X Y : AlgebraicSpaces B S hS}
    (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y.1)
    (f : X ⟶ Y) (hf : IsProper B S hS f.hom)
    (V : OpenSubspaces B S hS Y.1) (hVqc : IsQuasiCompactSpace B S hS V.1.toFunctor)
    (T : Set (points B S hS V.1.toFunctor)) (hT : IsClosed T)
    (W : OpenSubspaces B S hS Y.1) (hWV : W.1 ≤ V.1)
    (hTW : pointsMap B S hS _ V.1.ι '' T ⊆ subspacePointSet B S hS Y.1 W.1)
    (hWiso : IsIso (pullback.snd f.hom W.1.ι)) :
    ∃ (Y' : AlgebraicSpaces B S hS) (b : Y' ⟶ Y) (Yc : ClosedSubspaces B S hS Y.1),
      IsFinitePresentation B S hS Yc.1.ι ∧
        Disjoint (subspacePointSet B S hS Y.1 V.1) (subspacePointSet B S hS Y.1 Yc.1) ∧
          IsBlowupAlong B S hS Yc b ∧
            ∃ W' : OpenSubspaces B S hS Y'.1,
              closure (pointsMap B S hS _ b.hom ⁻¹' (pointsMap B S hS _ V.1.ι '' T)) ⊆
                  subspacePointSet B S hS Y'.1 W'.1 ∧
                IsIso (pullback.snd
                  (strictTransformSpaceToBlowUp B S hS f b (Yc.1.preimage b.hom)).hom
                  W'.1.ι)
```

## Tag 0F48, a lemma

[Tag 0F48](https://stacks.math.columbia.edu/tag/0F48) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_surjective_finite_flat_etaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFiniteFlatNearClosure.lean, line 781](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFiniteFlatNearClosure.lean#L781).

> **Stacks 0F48.**  Let `S` be a scheme, let `f : X ⟶ Y` be a proper morphism of quasi-compact
> and quasi-separated algebraic spaces over `S`, let `V ⊆ Y` be a quasi-compact open subspace with
> inverse image `U = f⁻¹(V)`, let `A ⊆ U` and `Bc ⊆ V` be closed subspaces such that `f`
> restricts to an isomorphism `e : A ≅ Bc`, and assume `f` is étale at every point of `A`.  Then
> there is a `V`-admissible blowup `b : Y' ⟶ Y`, with centre `Yc`, such that the strict transform
> `f' : X' ⟶ Y'` of `f` satisfies: for every geometric point `ā` of `X'` lying in the closure of
> the inverse image of `|A|` in `|X'|` there is a quotient `φ : 𝒪_{X', ā} ⟶ 𝒪`, a surjection onto
> a local ring, such that `φ ∘ (𝒪_{Y', f'(ā)} ⟶ 𝒪_{X', ā})` is finite and flat.
>
> The ring `𝒪` is the étale local ring of the strict transform `E` of a quasi-compact open `X₁₀`
> of a `U`-admissible blowup of `X`, at a geometric point over `ā`
> (`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_isFlat_cover_closure`), chosen so that the
> part of `X₁₀` over `Bc` lies over `A`.  As `A` is open in `f⁻¹(Bc)`, being the image of a section
> of `f⁻¹(Bc) ⟶ Bc` near which that morphism is étale, `E ×_{Y'} Bc ⟶ Bc` is a monomorphism, and
> `E ⟶ Y'` is étale at every point over the closure of `|Bc|`
> (`AlgebraicGeometry.Space.isEtaleAt_of_mono_pullback_snd`), which contains `f'(ā)`.  So the map
> `𝒪_{Y', f'(ā)} ⟶ 𝒪` is bijective
> (`AlgebraicGeometry.Space.bijective_etaleLocalRingMap_of_isEtaleAt`) and `φ` is surjective.

```lean
theorem exists_isAdmissibleBlowup_surjective_finite_flat_etaleLocalRing
    (hZ : B.Contains (⊤_ Scheme.{u})) {X Y : AlgebraicSpaces B S hS}
    (hXqc : IsQuasiCompactSpace B S hS X.1) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (hYqc : IsQuasiCompactSpace B S hS Y.1) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1)
    (f : X ⟶ Y) (hf : IsProper B S hS f.hom)
    (V : OpenSubspaces B S hS Y.1) (hVqc : IsQuasiCompactSpace B S hS V.1.toFunctor)
    (A : ClosedSubspaces B S hS (V.1.preimage f.hom).toFunctor)
    (Bc : ClosedSubspaces B S hS V.1.toFunctor) (e : A.1.toFunctor ≅ Bc.1.toFunctor)
    (he : e.hom ≫ Bc.1.ι = A.1.ι ≫ V.1.fromPreimage f.hom)
    (het : ∀ a : points B S hS A.1.toFunctor,
      IsEtaleAt B S hS f.hom (pointsMap B S hS _ (A.1.ι ≫ (V.1.preimage f.hom).ι) a)) :
    ∃ (Y' : AlgebraicSpaces B S hS) (b : Y' ⟶ Y) (Yc : ClosedSubspaces B S hS Y.1),
      IsAdmissibleBlowup B S hS V b ∧ IsFinitePresentation B S hS Yc.1.ι ∧
        Disjoint (subspacePointSet B S hS Y.1 V.1) (subspacePointSet B S hS Y.1 Yc.1) ∧
          IsBlowupAlong B S hS Yc b ∧
            ∀ abar : GeometricPoint B S hS
                (strictTransformSpace B S hS f b (Yc.1.preimage b.hom)).1,
              abar.image ∈ closure (pointsMap B S hS _
                  (strictTransformSpaceι B S hS f b (Yc.1.preimage b.hom) ≫
                    strictTransformPullbackToSource B S hS f b).hom ⁻¹'
                  Set.range (pointsMap B S hS _ (A.1.ι ≫ (V.1.preimage f.hom).ι))) →
              ∃ (O : CommRingCat.{u + 1})
                (φ : etaleLocalRing B S hS
                  (strictTransformSpace B S hS f b (Yc.1.preimage b.hom)).1 abar →+* O),
                IsLocalRing O ∧ Function.Surjective φ ∧
                  (φ.comp (etaleLocalRingMap
                    (strictTransformSpace B S hS f b (Yc.1.preimage b.hom)).2
                    (strictTransformSpaceToBlowUp B S hS f b (Yc.1.preimage b.hom)).hom
                    abar)).Finite ∧
                  (φ.comp (etaleLocalRingMap
                    (strictTransformSpace B S hS f b (Yc.1.preimage b.hom)).2
                    (strictTransformSpaceToBlowUp B S hS f b (Yc.1.preimage b.hom)).hom
                    abar)).Flat
```

## Tag 0F49, a lemma

[Tag 0F49](https://stacks.math.columbia.edu/tag/0F49) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_le_strictTransformInAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupPropernessAndStrictTransformImage.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupPropernessAndStrictTransformImage.lean#L339). The attribute's comment: “the inclusion of the scheme-theoretic image in the strict transform”.

> **One inclusion of Stacks 0F49, with Stacks 085T and 0863 as explicit hypotheses.**  Let
> `X ⟶ T` and `Y ⟶ T` be morphisms of algebraic spaces over `S`, let `U ⊆ X` be an open subspace,
> let `v : V ⟶ X ×_T Y` be a morphism whose composite with the first projection factors through
> `U`, and let `Z` be the scheme-theoretic image of `v`.  Let `b : X' ⟶ X` be the blowup of `X` in
> a closed subspace `Zc` of finite presentation whose points are disjoint from those of `U` — that
> is, a `U`-admissible blowup of Stacks 086B.  Then the scheme-theoretic image of the lift
> `v' : V ⟶ X' ×_T Y` is **contained in** the strict transform of `Z` with respect to `b`.
>
> Here `X' ×_T Y` is spelled `(X ×_T Y) ×_X X'`, the strict transform of Stacks 0862 is taken of
> `Z` viewed as an algebraic space over `X`, and its image in the ambient space is
> `AlgebraicGeometry.Space.strictTransformInAmbient`.
>
> Stacks 0F49 asserts that the two are equal.  This is the inclusion of the scheme-theoretic image
> in the strict transform, and only that; it is not the tag's equality, and the clause string of
> the attribute says which inclusion it is.  The reverse inclusion is the content the library
> cannot reach; see
> `AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_eq_strictTransformInAmbient`.
>
> Two hypotheses stand for inputs the library does not have, and both are *upstream* of this
> conclusion — each is the conclusion of a tag that is missing, and neither mentions the
> scheme-theoretic image of the lift:
>
> * `hfac` is the source's morphism `V ⟶ Z'`, which comes from Stacks 085T part (1): the blowup is
>   an isomorphism away from its centre, and `V` lies over `U`, which is disjoint from the centre;
> * `himm` is step (1) of the source's proof, that the strict transform is a closed subspace of
>   `X' ×_X Z`, which is Stacks 0863 part (2).
>
> Given those, the inclusion is the minimality of the scheme-theoretic image, Stacks 082X in the
> form `AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_le`: the strict transform is a
> closed subspace through which the lift factors.  Quasi-compactness of `v` is not needed for this
> half and so is not carried; the source uses it only in the reverse inclusion.

```lean
theorem schemeTheoreticImageSubfunctor_le_strictTransformInAmbient (p : X ⟶ T) (q : Y ⟶ T)
    (U : OpenSubspaces B S hS X.1) (Zc : ClosedSubspaces B S hS X.1) (b : X' ⟶ X)
    (hfp : IsFinitePresentation B S hS Zc.1.ι)
    (hdisj : Disjoint (subspacePointSet B S hS X.1 U.1)
      (subspacePointSet B S hS X.1 Zc.1))
    (hbl : IsBlowupAlong B S hS Zc b)
    (v : V ⟶ AlgebraicSpaces.fiberProduct B S hS p q)
    (v' : V.1 ⟶ (strictTransformPullback B S hS (fiberProductFirst B S hS p q) b).1)
    (hvU : Subfunctor.range (v.hom ≫ (fiberProductFirst B S hS p q).hom) ≤ U.1)
    (hfac : IsAdmissibleBlowup B S hS U b →
      Subfunctor.range (v.hom ≫ (fiberProductFirst B S hS p q).hom) ≤ U.1 →
      Subfunctor.range v' ≤ strictTransformInAmbient B S hS p q b Zc
        (schemeTheoreticImage B S hS v.hom
          (AlgebraicSpaces.fiberProduct B S hS p q).property))
    (himm : IsClosedSubspace B S hS (strictTransformInAmbient B S hS p q b Zc
      (schemeTheoreticImage B S hS v.hom
        (AlgebraicSpaces.fiberProduct B S hS p q).property))) :
    schemeTheoreticImageSubfunctor B S hS v' ≤
      strictTransformInAmbient B S hS p q b Zc
        (schemeTheoreticImage B S hS v.hom
          (AlgebraicSpaces.fiberProduct B S hS p q).property)
```

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_eq_strictTransformInAmbient_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupPropernessAndStrictTransformImageUnconditional.lean, line 1029](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupPropernessAndStrictTransformImageUnconditional.lean#L1029). The attribute's comment: “the equality of the scheme-theoretic image of the lift with the strict transform, at the source's hypotheses and with NO side condition and no part of the conclusion assumed. The properness of the admissible blowup, Stacks 085Z, is proved rather than assumed, by AlgebraicGeometry.Space.isProper\_of\_isBlowupAlong\_of\_isFinitePresentation, which itself carries no side condition”.

> **Stacks 0F49.**  Let
> `X ⟶ T` and `Y ⟶ T` be
> morphisms of algebraic spaces over `S`, let `U ⊆ X` be an open subspace, let `v : V ⟶ X ×_T Y` be
> a *quasi-compact* morphism whose composite with the first projection factors through `U`, and let
> `Z` be the scheme-theoretic image of `v`.  Let `b : X' ⟶ X` be a `U`-admissible blowup, that is,
> the blowup of `X` in a closed subspace `Zc` of finite presentation whose points are disjoint from
> those of `U`.  Then the scheme-theoretic image of the lift `v' : V ⟶ X' ×_T Y` **equals** the
> strict transform of `Z` with respect to `b`.
>
> This is the assertion of Stacks 0F49.  Both inclusions are proved:
>
> * `AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_le_strictTransformInAmbient_of_lift`
>   is steps (1) and (2) of the source's proof — the strict transform is a closed subspace of
>   `X' ×_T Y` through which the lift factors;
> * `AlgebraicGeometry.Space.strictTransformInAmbient_le_schemeTheoreticImageSubfunctor` is steps
>   (4) and (5) — `V` is scheme-theoretically dense in the part of `Z ×_X X'` lying over the
>   complement of the centre, by part (3) of Stacks 082Z, and the strict transform is cut out by
>   the ideal of sections supported on the exceptional divisor, which is the ideal-theoretic form
>   of "there are no nonzero sections of `𝒪_{Z'}` supported on `E`".
>
> Step (3) of the source's proof, the quasi-compactness of the lift, is supplied by
> `AlgebraicGeometry.Space.isQuasiCompact_of_comp_fiberProductFirst_unconditional`, which needs
> the properness of the admissible blowup, Stacks 085Z.  That is now *proved*, in
> `AlgebraicGeometry.Space.isProper_of_isBlowupAlong_of_isFinitePresentation`, and carries no side
> condition, so **nothing is assumed here beyond the source's own hypotheses**.  In particular the density
> statement, part of the tag's own conclusion, is the theorem
> `AlgebraicGeometry.Space.strictTransformInAmbient_le_schemeTheoreticImageSubfunctor`, and neither
> the existence of a proper blowup nor a surjective étale chart of `X` with the size conditions of
> Stacks 085Q is assumed.

```lean
theorem schemeTheoreticImageSubfunctor_eq_strictTransformInAmbient_unconditional
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)] (p : X ⟶ T) (q : Y ⟶ T)
    (U : OpenSubspaces B S hS X.1) (Zc : ClosedSubspaces B S hS X.1) (b : X' ⟶ X)
    (hfp : IsFinitePresentation B S hS Zc.1.ι)
    (hdisj : Disjoint (subspacePointSet B S hS X.1 U.1)
      (subspacePointSet B S hS X.1 Zc.1))
    (hbl : IsBlowupAlong B S hS Zc b)
    (v : V ⟶ AlgebraicSpaces.fiberProduct B S hS p q)
    (hv : IsQuasiCompact B S hS v.hom)
    (v' : V.1 ⟶ (strictTransformPullback B S hS (fiberProductFirst B S hS p q) b).1)
    (hv' : v' ≫ pullback.fst (fiberProductFirst B S hS p q).hom b.hom = v.hom)
    (hvU : Subfunctor.range (v.hom ≫ (fiberProductFirst B S hS p q).hom) ≤ U.1) :
    schemeTheoreticImageSubfunctor B S hS v' =
      strictTransformInAmbient B S hS p q b Zc
        (schemeTheoreticImage B S hS v.hom
          (AlgebraicSpaces.fiberProduct B S hS p q).property)
```

## Tag 0F4A, a lemma

[Tag 0F4A](https://stacks.math.columbia.edu/tag/0F4A) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_isProper_extension_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleCompactificationProperExtension.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleCompactificationProperExtension.lean#L138).

> Let `T` be a quasi-compact and quasi-separated algebraic space over `S`, let `g : U ⟶ T` be
> separated and of finite type, and let `f : V ⟶ U` be étale. Suppose `V` has a compactification
> over `T`: a quasi-compact open immersion `j : V ⟶ Y` into an algebraic space `Y` with
> `p : Y ⟶ T` proper and `j ≫ p = f ≫ g`. Then there are a `V`-admissible blowup `b : Y' ⟶ Y` and
> an open subspace `V' ⊆ Y'` containing `V` — a morphism `e : V ⟶ V'` lying over `j` whose image
> in `Y'` is the inverse image of `V` — such that `f` extends to a proper morphism `q : V' ⟶ U`
> over `T`.

```lean
theorem exists_isAdmissibleBlowup_isProper_extension_of_isEtale
    (hZ : B.Contains (⊤_ Scheme.{u})) {T U V Y : AlgebraicSpaces B S hS}
    (hTqc : IsQuasiCompactSpace B S hS T.1) (hTqs : IsAbsolutelyQuasiSeparated B S hS hZ T.1)
    (g : U.1 ⟶ T.1) (hgft : IsFiniteType B S hS g) (hgsep : IsSeparated B S hS g)
    (f : V.1 ⟶ U.1) (_hf : IsEtale B S hS f)
    (j : V.1 ⟶ Y.1) (p : Y.1 ⟶ T.1) (hj : IsOpenImmersion B S hS j)
    (hjqc : IsQuasiCompact B S hS j) (hp : IsProper B S hS p) (hcomm : j ≫ p = f ≫ g) :
    ∃ (Y' : AlgebraicSpaces B S hS) (b : Y' ⟶ Y),
      IsAdmissibleBlowup B S hS
        ⟨Subfunctor.range j, isOpenSubspace_subfunctorRange B S hS V.2 hj⟩ b ∧
      ∃ (V' : OpenSubspaces B S hS Y'.1) (e : V.1 ⟶ V'.1.toFunctor) (q : V'.1.toFunctor ⟶ U.1),
        Subfunctor.range (e ≫ V'.1.ι) = (Subfunctor.range j).preimage b.hom ∧
          e ≫ V'.1.ι ≫ b.hom = j ∧ IsProper B S hS q ∧ e ≫ q = f ∧
            q ≫ g = V'.1.ι ≫ b.hom ≫ p
```

## Tag 0F4B, a lemma

[Tag 0F4B](https://stacks.math.columbia.edu/tag/0F4B) in the Stacks Project.

**`AlgebraicGeometry.Space.hasCompactification_of_isElementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NagataCompactification/EtaleSquareCompactification.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NagataCompactification/EtaleSquareCompactification.lean#L278). The attribute's comment: “proof corrected: the source's W₁ = U ⊔\_\{U₁} (X₁ ∖ (Z̄₁₂ ∪ T̄)) need not be separated; X₁ is modified by three more admissible blowups (0F46 twice, and a blowup in I + J^M from the Nullstellensatz on the closure of the off-diagonal of U₁ ×\_U U₁), and W₁ is glued from the chart N = X₁ ∖ (closure (V₁ ∖ U₁) ∪ closure (∂ ∖ Q))”.

> **Compactifications glue across an elementary distinguished square** (Stacks 0F4B). Over a
> quasi-compact, quasi-separated algebraic space `Y` of finite type over `Spec ℤ`, let `U` be
> separated and of finite type over `Y` and `(U₂ ⊆ U, f : U₁ ⟶ U)` an elementary distinguished
> square such that `U₁` and `U₂` have compactifications over `Y` and `U₁ ×_U U₂ ⟶ U` has dense
> image. Then `U` has a compactification over `Y`.
>
> The proof is the repaired one of
> `StacksFrontier.AlgebraicGeometry.Spaces.NagataCompactification.EtaleSquareGluing`; the density of
> `U₁ ×_U U₂` in `U` is not needed.

```lean
theorem hasCompactification_of_isElementaryDistinguishedSquare (hZ : B.Contains (⊤_ Scheme.{u})) :
    Stmt0F4B (B := B) (S := S) (hS := hS) hZ
```

## Tag 0F4C, a lemma

[Tag 0F4C](https://stacks.math.columbia.edu/tag/0F4C) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_etale_isElementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleEnlargementOfOpen/Enlargement.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleEnlargementOfOpen/Enlargement.lean#L464).

> **Stacks 0F4C.** Let `U` be a dense open subspace of a Noetherian algebraic space `X`
> over `S` with `U ≠ X`. There is an affine scheme `V` and an étale morphism `V ⟶ X` such that
> the open subspace `W` whose points are those of `U` together with the image of `V` strictly
> contains `U`, the pair `(U ⊆ W, V ⟶ W)` is an elementary distinguished square, and
> `U ×_X V ⟶ U` has dense image.

```lean
theorem exists_affine_etale_isElementaryDistinguishedSquare
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hXnoeth : AlgebraicGeometry.Space.IsNoetherian B S hS hZ X)
    (U : Subfunctor X) (hU : AlgebraicGeometry.Space.IsOpenSubspace B S hS U)
    (hUproper : U ≠ ⊤)
    (_hUdense : letI : TopologicalSpace (AlgebraicGeometry.Space.points B S hS X) :=
        AlgebraicGeometry.Space.pointTopology B S hS X
      DenseRange (AlgebraicGeometry.Space.pointsMap B S hS U.toFunctor U.ι)) :
    ∃ (V : AlgebraicGeometry.BigFppfOver B S hS)
      (W : Subfunctor X)
      (hW : AlgebraicGeometry.Space.IsOpenSubspace B S hS W)
      (hUW : U < W)
      (f : yoneda.obj V ⟶ W.toFunctor),
      IsAffine ((AlgebraicGeometry.BigFppfOver.toScheme B S hS).obj V) ∧
      AlgebraicGeometry.Space.IsEtale B S hS (f ≫ W.ι) ∧
      (Set.range (AlgebraicGeometry.Space.pointsMap B S hS W.toFunctor W.ι) =
        Set.range (AlgebraicGeometry.Space.pointsMap B S hS U.toFunctor U.ι) ∪
          Set.range (AlgebraicGeometry.Space.pointsMap B S hS (yoneda.obj V) (f ≫ W.ι))) ∧
      AlgebraicGeometry.Space.IsElementaryDistinguishedSquare B S hS hW.1
        (Subfunctor.range (Subfunctor.homOfLe hUW.le)) f ∧
      (letI : TopologicalSpace (AlgebraicGeometry.Space.points B S hS U.toFunctor) :=
        AlgebraicGeometry.Space.pointTopology B S hS U.toFunctor
       DenseRange (AlgebraicGeometry.Space.pointsMap B S hS (pullback U.ι (f ≫ W.ι))
         (pullback.fst U.ι (f ≫ W.ι))))
```

## Tag 0F4D, a theorem

[Tag 0F4D](https://stacks.math.columbia.edu/tag/0F4D) in the Stacks Project.

**`AlgebraicGeometry.Space.hasCompactification_of_isSeparated_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NagataCompactification/Nagata.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NagataCompactification/Nagata.lean#L63).

> **Nagata's compactification theorem for algebraic spaces.** Let `Y` be a quasi-compact and
> quasi-separated algebraic space over `S`, and let `f : X ⟶ Y` be a separated morphism of finite
> type. Then `X` has a compactification over `Y`.

```lean
theorem hasCompactification_of_isSeparated_of_isFiniteType (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y) (f : X ⟶ Y) (hsep : IsSeparated B S hS f)
    (hft : IsFiniteType B S hS f) : HasCompactification B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.14, Tag 0F44](https://stacks.math.columbia.edu/tag/0F44)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
