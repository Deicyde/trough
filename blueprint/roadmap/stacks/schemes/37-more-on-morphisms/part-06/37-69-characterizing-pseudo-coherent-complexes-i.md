---
declaration: section
origin: cited
lean: AlgebraicGeometry.torIndependent_pullback_product_of_flat, AlgebraicGeometry.exists_derivedChowDatum, AlgebraicGeometry.isClosedImmersion_chowDatumMorphism, AlgebraicGeometry.finitePresentation_chowDatumMorphism, AlgebraicGeometry.chowDatum_derivedPushforward_tensor_restrict_iso, AlgebraicGeometry.chowDatum_derivedPushforward_tensor_restrict_iso_of_isDQCoh, AlgebraicGeometry.chowDatum_fourierMukai, AlgebraicGeometry.isPseudoCoherent_of_derivedGlobalSectionsOver_tensor_isPseudoCoherent
statement: formalized
proof: formalized
---

# 37.69 Characterizing pseudo-coherent complexes, III

Section 37.69 of the Stacks Project, [Tag 0CSI](https://stacks.math.columbia.edu/tag/0CSI). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CTA, a lemma

[Tag 0CTA](https://stacks.math.columbia.edu/tag/0CTA) in the Stacks Project.

**`AlgebraicGeometry.torIndependent_pullback_product_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/TorIndependenceBaseChange.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/TorIndependenceBaseChange.lean#L272).

> In a commutative square, flatness of the right-hand object
> over the base and of the upper-left object over the lower-left object implies the indicated Tor
> independence after arbitrary base change.

```lean
theorem torIndependent_pullback_product_of_flat
    {S S' X' Y' Z' : Scheme.{u}}
    (s : S ⟶ S') (x : X' ⟶ S') (y : Y' ⟶ S')
    (zx : Z' ⟶ X') (zy : Z' ⟶ Y') (hz : zx ≫ x = zy ≫ y)
    [Flat y] [Flat zx] :
    let _X := pullback x s
    let _Y := pullback y s
    let P := pullback (pullback.snd x s) (pullback.snd y s)
    let P' := pullback x y
    let pToP' : P ⟶ P' :=
      pullback.lift
        (pullback.fst (pullback.snd x s) (pullback.snd y s) ≫ pullback.fst x s)
        (pullback.snd (pullback.snd x s) (pullback.snd y s) ≫ pullback.fst y s)
        (by
          calc
            _ = pullback.fst (pullback.snd x s) (pullback.snd y s) ≫
                (pullback.fst x s ≫ x) := Category.assoc _ _ _
            _ = pullback.fst (pullback.snd x s) (pullback.snd y s) ≫
                (pullback.snd x s ≫ s) := by rw [pullback.condition]
            _ = (pullback.fst (pullback.snd x s) (pullback.snd y s) ≫
                pullback.snd x s) ≫ s := (Category.assoc _ _ _).symm
            _ = (pullback.snd (pullback.snd x s) (pullback.snd y s) ≫
                pullback.snd y s) ≫ s := by rw [pullback.condition]
            _ = pullback.snd (pullback.snd x s) (pullback.snd y s) ≫
                (pullback.snd y s ≫ s) := Category.assoc _ _ _
            _ = pullback.snd (pullback.snd x s) (pullback.snd y s) ≫
                (pullback.fst y s ≫ y) := by rw [pullback.condition]
            _ = _ := (Category.assoc _ _ _).symm)
    let zToP' : Z' ⟶ P' := pullback.lift zx zy hz
    TorIndependent pToP' zToP'
```

## Tag 0CSJ, a lemma

[Tag 0CSJ](https://stacks.math.columbia.edu/tag/0CSJ) in the Stacks Project.

**`AlgebraicGeometry.exists_derivedChowDatum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowLemmaGeneral.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowLemmaGeneral.lean#L348).

> **Derived Chow's lemma**, [Stacks, Tag 0CSJ]. Let `A` be a ring and let `X` be a separated
> scheme of finite presentation over `A`, with structure morphism `f : X ⟶ Spec A`. For every
> point `x` of `X` there are an open neighbourhood `U` of `x`, an `m ≥ 0`, an open `V` of
> `ℙᵐ_A`, a closed subscheme `iZ : Z ⟶ X ×_A ℙᵐ_A`, a point `z` of `Z` and an object `E` of
> `D(𝒪_{X ×_A ℙᵐ_A})` such that, writing `b : Z ⟶ X` and `c : Z ⟶ ℙᵐ_A` for the two projections
> of `Z`:
>
> 1. `iZ` is of finite presentation;
> 2. `b` is an isomorphism over `U`, and `b z = x`;
> 3. `c` is a closed immersion over `V`;
> 4. `b ⁻¹ᵁ U = c ⁻¹ᵁ V`, and in particular `c z ∈ V`;
> 5. the restriction of `E` to `X ×_A V` is isomorphic to the restriction of `(b, c)_* 𝒪_Z`;
> 6. `E` is pseudo-coherent and its cohomology is supported on `Z`.
>
> The proof is the source's: write `X` as the base change of a separated scheme of finite
> presentation `X'` over a finitely generated subring `A'` of `A`, apply the Noetherian case
> `AlgebraicGeometry.exists_chowDatum_isPseudoCoherent_of_isNoetherian` to `X'`, and pull the
> datum back (`AlgebraicGeometry.hasDerivedChowDatum_of_isPullback`).

```lean
theorem exists_derivedChowDatum {A : Type u} [CommRing A] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of A)) [IsSeparated f] [LocallyOfFinitePresentation f] [QuasiCompact f]
    (x : X) :
    ∃ (U : X.Opens) (m : ℕ) (V : (projectiveSpaceOver m (Spec (.of A))).Opens) (Z : Scheme.{u})
      (iZ : Z ⟶ pullback f (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) (z : Z)
      (E : DerivedCategory
        (pullback f (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).Modules),
      x ∈ U ∧ IsClosedImmersion iZ ∧ FinitePresentation iZ ∧
        IsIso ((iZ ≫ pullback.fst f
          (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) ∣_ U) ∧
        (iZ ≫ pullback.fst f
          (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).base z = x ∧
        IsClosedImmersion ((iZ ≫ pullback.snd f
          (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) ∣_ V) ∧
        (iZ ≫ pullback.fst f
            (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) ⁻¹ᵁ U =
          (iZ ≫ pullback.snd f
            (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) ⁻¹ᵁ V ∧
        (iZ ≫ pullback.snd f
          (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).base z ∈ V ∧
        Nonempty ((derivedPullback (ofScheme (pullback.snd f
            (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A)) ⁻¹ᵁ V).ι)).obj E ≅
          (derivedPullback (ofScheme (pullback.snd f
            (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A)) ⁻¹ᵁ V).ι)).obj
            ((DerivedCategory.singleFunctor
              (pullback f (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).Modules 0).obj
              ((Scheme.Modules.pushforward iZ).obj (SheafOfModules.unit Z.ringCatSheaf)))) ∧
        RingedSpace.IsPseudoCoherent (X := (pullback f
          (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).toRingedSpace) E ∧
        CohomologySupportedOn (pullback f
            (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).ringCatSheaf
          (Set.range iZ.base) E
```

## Tag 0CSK, a lemma

[Tag 0CSK](https://stacks.math.columbia.edu/tag/0CSK) in the Stacks Project.

**`AlgebraicGeometry.isClosedImmersion_chowDatumMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukai.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukai.lean#L333). The attribute's comment: “the morphism U ⟶ V of the statement is a closed immersion; the derived comparison is chowDatum\_derivedPushforward\_tensor\_restrict\_iso”.

> **[Stacks, Tag 0CSK], first assertion: `U ⟶ V` is a closed immersion.**  It is the inverse of
> an isomorphism, a transport along an equality of opens, and the closed immersion `c|_V`.

```lean
theorem isClosedImmersion_chowDatumMorphism (hb : IsIso ((iZ ≫ p) ∣_ U))
    (hc : IsClosedImmersion ((iZ ≫ q) ∣_ V))
    (hW : (iZ ≫ p) ⁻¹ᵁ U = (iZ ≫ q) ⁻¹ᵁ V) :
    IsClosedImmersion (chowDatumMorphism p q iZ U V hb hW)
```

**`AlgebraicGeometry.finitePresentation_chowDatumMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukai.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukai.lean#L349). The attribute's comment: “the morphism U ⟶ V of the statement is of finite presentation, given that U and V are of finite presentation over the base; the derived comparison is chowDatum\_derivedPushforward\_tensor\_restrict\_iso”.

> **[Stacks, Tag 0CSK], first assertion: `U ⟶ V` is of finite presentation.**  The two
> factorization identities show that `U ⟶ V` is a morphism over the base `S`, and
> [Stacks, Tag 02FV] then deduces finite presentation of `U ⟶ V` from finite presentation of
> `U ⟶ S` and of `V ⟶ S`.

```lean
theorem finitePresentation_chowDatumMorphism {S : Scheme.{u}} (f : X ⟶ S) (g : P ⟶ S)
    (hpq : p ≫ f = q ≫ g) (hb : IsIso ((iZ ≫ p) ∣_ U))
    (hW : (iZ ≫ p) ⁻¹ᵁ U = (iZ ≫ q) ⁻¹ᵁ V)
    (hU : AlgebraicGeometry.FinitePresentation (U.ι ≫ f))
    (hV : AlgebraicGeometry.FinitePresentation (V.ι ≫ g)) :
    AlgebraicGeometry.FinitePresentation (chowDatumMorphism p q iZ U V hb hW)
```

**`AlgebraicGeometry.chowDatum_derivedPushforward_tensor_restrict_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukai.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukai.lean#L416). The attribute's comment: “the derived comparison Rq\_*(Lp^*K ⊗ᴸ E)|\_V ≅ R(U → V)\_*(K|\_U), for arbitrary K in D(O\_X) — more general than the source, which takes K in D\_QCoh(O\_X) — carrying two inputs as named hypotheses. (i) hproj is Tag 08EU, the projection formula, at the closed immersion i : W ⟶ q⁻¹V and at a GENERAL target complex: this library carries Tag 08EU only at the unit object (see the restriction on isIso\_projectionFormulaMap\_unitObject) and the source's devissage to that case is not available; it is also stated with the direct image on the right of the tensor product, so it differs from the Tag 0B53 map by the commutativity of ⊗ᴸ, which is likewise not carried. (ii) hE is clause (5) of Tag 0CSJ in the restricted form the source uses, that E restricted to q⁻¹V is Ri\_*O\_W: the library's Tag 0CSJ gives the stronger global form E ≅ (iZ)\_*O\_Z[0], but descending it to q⁻¹V needs exactness of direct image along a closed immersion and the unit comparison Lj^*(O\_T[0]) ≅ O\_W[0], which the Tag 08EU file records as unavailable. Everything else is proved here: Tag 08FE (localization of the total direct image, proved in this file for the standard functors), Tag 079U, Tags 0D5S and 0D5T, and the invertibility of the derived adjunction unit along the isomorphism b|\_U. The two geometric assertions of the statement, that U ⟶ V is a closed immersion and is of finite presentation, are isClosedImmersion\_chowDatumMorphism and finitePresentation\_chowDatumMorphism”.

> **[Stacks, Tag 0CSK], the derived comparison.**  In the situation of Chow's lemma in the
> derived category — `p : T ⟶ X` and `q : T ⟶ P` the two projections of `T = X ×_A P`,
> `iZ : Z ⟶ T` the closed subscheme, `b = iZ ≫ p` an isomorphism over the open `U ⊆ X`,
> `c = iZ ≫ q` a closed immersion over the open `V ⊆ P`, and `b ⁻¹ᵁ U = c ⁻¹ᵁ V` — for every
> `E ∈ D(𝒪_T)` and every `K ∈ D(𝒪_X)`
>
> `Rq_*(Lp^*K ⊗^𝐋 E)|_V ≅ R(c ∘ (b|_U)⁻¹)_*(K|_U)`.
>
> The two hypotheses are the inputs the source cites and this library does not carry: `hE` is
> clause (5) of [Stacks, Tag 0CSJ], that the restriction of `E` to `q ⁻¹ᵁ V` is the direct image of
> the structure sheaf of `W = c ⁻¹ᵁ V` along the closed immersion `i = iZ ∣_ (q ⁻¹ᵁ V)`; and
> `hproj` is [Stacks, Tag 08EU] at `i` and at the target complex `Lp^*K` restricted, which is the
> projection formula at a *general* complex, the case the library's [Stacks, Tag 08EU] excludes.
>
> Everything else is proved: the localization of the direct image is [Stacks, Tag 08FE], here
> `AlgebraicGeometry.DerivedChow.derivedPushforwardRestrictOpenIso`; the monoidality of derived
> pullback is [Stacks, Tag 079U]; the two composition isomorphisms are [Stacks, Tag 0D5S] and
> [Stacks, Tag 0D5T]; and the final identification uses that `b|_U` is an isomorphism, so that the
> unit of the derived adjunction of [Stacks, Tag 079W] along it is invertible.

```lean
theorem chowDatum_derivedPushforward_tensor_restrict_iso
    (hE : (derivedPullback (ofScheme (q ⁻¹ᵁ V).ι)).obj E ≅
      (derivedPushforward (ofScheme (iZ ∣_ (q ⁻¹ᵁ V)))).obj
        (structureSheafSingle (iZ ⁻¹ᵁ (q ⁻¹ᵁ V)).toScheme))
    (hproj : ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
            (q ⁻¹ᵁ V).toScheme.sheaf).obj
          ((derivedPullback (ofScheme (q ⁻¹ᵁ V).ι)).obj
            ((derivedPullback (ofScheme p)).obj K))).obj
        ((derivedPushforward (ofScheme (iZ ∣_ (q ⁻¹ᵁ V)))).obj
          (structureSheafSingle (iZ ⁻¹ᵁ (q ⁻¹ᵁ V)).toScheme)) ≅
      (derivedPushforward (ofScheme (iZ ∣_ (q ⁻¹ᵁ V)))).obj
        ((derivedPullback (ofScheme (iZ ∣_ (q ⁻¹ᵁ V)))).obj
          ((derivedPullback (ofScheme (q ⁻¹ᵁ V).ι)).obj
            ((derivedPullback (ofScheme p)).obj K)))) :
    Nonempty ((derivedPullback (ofScheme V.ι)).obj ((derivedPushforward (ofScheme q)).obj
        (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor T.sheaf).obj
          ((derivedPullback (ofScheme p)).obj K)).obj E)) ≅
      (derivedPushforward (ofScheme (chowDatumMorphism p q iZ U V hb hW))).obj
        ((derivedPullback (ofScheme U.ι)).obj K))
```

**`AlgebraicGeometry.chowDatum_derivedPushforward_tensor_restrict_iso_of_isDQCoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukaiQCoh.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukaiQCoh.lean#L200). The attribute's comment: “the derived comparison Rq\_*(Lp^*K ⊗ᴸ E)|\_V ≅ R(U → V)\_*(K|\_U) for K in D\_QCoh(O\_X), which is the condition on K that Tag 0CSK itself states. Everything else the statement fixes — p, q, iZ, U, V, E and the three conditions hb, hW, hE on them — is the datum of Lemma 0CSJ, hE being clause (5) of that lemma in the very shape exists\_derivedChowDatum produces it. Nothing further enters: the projection formula of Tag 08EU and clause (5) in the restricted form the computation reads it in are both proved here, as derivedProjectionFormulaUnitRightIso and DerivedChow.pushforwardUnitRestrictIso. The whole statement, with the two geometric assertions that U ⟶ V is a closed immersion and is of finite presentation, is chowDatum\_fourierMukai”.

> **[Stacks, Tag 0CSK], the derived comparison, at a quasi-coherent complex.**  In the
> situation of derived Chow's lemma — `p : T ⟶ X` and `q : T ⟶ P` the two projections of
> `T = X ×_A ℙⁿ_A`, `iZ : Z ⟶ T` the closed subscheme, `b = iZ ≫ p` an isomorphism over the open
> `U ⊆ X`, `c = iZ ≫ q`, and `b ⁻¹ᵁ U = c ⁻¹ᵁ V` for an open `V ⊆ P` — let `E` satisfy clause (5)
> of [Stacks, Tag 0CSJ], that its restriction to `q ⁻¹ᵁ V` agrees with that of `(iZ)_*𝒪_Z`.  Then
> for every `K ∈ D_QCoh(𝒪_X)`
>
> `Rq_*(Lp^*K ⊗^𝐋 E)|_V ≅ R(c ∘ (b|_U)⁻¹)_*(K|_U)`.
>
> This statement stands at the data of [Stacks, Tag 0CSJ] and nothing else: `hb`, `hW` and `hE`
> are clauses (2), (4) and (5) of that lemma, in the shape
> `AlgebraicGeometry.exists_derivedChowDatum` produces them, and `hK` is the quasi-coherence
> condition on `K` that [Stacks, Tag 0CSK] states.  The whole of Tag 0CSK, at the projections of
> `X ×_A ℙᵐ_A`, is `AlgebraicGeometry.chowDatum_fourierMukai` below.  The proof is
> `AlgebraicGeometry.chowDatum_derivedPushforward_tensor_restrict_iso`, whose two inputs are
> supplied by `AlgebraicGeometry.DerivedChow.pushforwardUnitRestrictIso` and by
> `AlgebraicGeometry.derivedProjectionFormulaUnitRightIso`.

```lean
theorem chowDatum_derivedPushforward_tensor_restrict_iso_of_isDQCoh
    {X P T Z : Scheme.{u}} (p : T ⟶ X) (q : T ⟶ P) (iZ : Z ⟶ T) [IsClosedImmersion iZ]
    (U : X.Opens) (V : P.Opens) (hb : IsIso ((iZ ≫ p) ∣_ U))
    (hW : (iZ ≫ p) ⁻¹ᵁ U = (iZ ≫ q) ⁻¹ᵁ V)
    (E : DerivedCategory T.Modules)
    (hE : (derivedPullback (ofScheme (q ⁻¹ᵁ V).ι)).obj E ≅
      (derivedPullback (ofScheme (q ⁻¹ᵁ V).ι)).obj
        ((DerivedCategory.singleFunctor T.Modules 0).obj
          ((Scheme.Modules.pushforward iZ).obj (SheafOfModules.unit Z.ringCatSheaf))))
    (K : DerivedCategory X.Modules)
    (hK : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent) :
    Nonempty ((derivedPullback (ofScheme V.ι)).obj ((derivedPushforward (ofScheme q)).obj
        (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor T.sheaf).obj
          ((derivedPullback (ofScheme p)).obj K)).obj E)) ≅
      (derivedPushforward (ofScheme (chowDatumMorphism p q iZ U V hb hW))).obj
        ((derivedPullback (ofScheme U.ι)).obj K))
```

**`AlgebraicGeometry.chowDatum_fourierMukai`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukaiQCoh.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukaiQCoh.lean#L288).

> **[Stacks, Tag 0CSK].**  Let `A` be a ring, let `f : X ⟶ Spec A` be locally of finite
> presentation (in the source, `X` is separated and of finite presentation over `A`), let
> `p : X ×_A ℙᵐ_A ⟶ X` and `q : X ×_A ℙᵐ_A ⟶ ℙᵐ_A` be the two projections, and let
> `U ⊆ X`, `V ⊆ ℙᵐ_A`, `iZ : Z ⟶ X ×_A ℙᵐ_A` and `E ∈ D(𝒪_{X ×_A ℙᵐ_A})` be as in
> [Stacks, Tag 0CSJ]: `iZ` is a closed immersion, `b = iZ ≫ p` is an isomorphism over `U`,
> `c = iZ ≫ q` is a closed immersion over `V`, `b ⁻¹ᵁ U = c ⁻¹ᵁ V`, and the restriction of `E` to
> `X ×_A V` is that of `(b, c)_*𝒪_Z` — each in the very shape
> `AlgebraicGeometry.exists_derivedChowDatum` produces it.  Then the morphism
> `c ∘ (b|_U)⁻¹ : U ⟶ V` is a closed immersion of finite presentation, and for every
> `K ∈ D_QCoh(𝒪_X)`
>
> `Rq_*(Lp^*K ⊗^𝐋 E)|_V ≅ R(c ∘ (b|_U)⁻¹)_*(K|_U)`.
>
> The clauses of [Stacks, Tag 0CSJ] not listed — finite presentation of `iZ`, the point `z`,
> separatedness and quasi-compactness of `X`, pseudo-coherence and support of `E` — are not used,
> so the statement is given without them.

```lean
theorem chowDatum_fourierMukai {A : Type u} [CommRing A] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of A)) [LocallyOfFinitePresentation f] (m : ℕ) (U : X.Opens)
    (V : (projectiveSpaceOver m (Spec (.of A))).Opens) {Z : Scheme.{u}}
    (iZ : Z ⟶ pullback f (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A)))
    [IsClosedImmersion iZ]
    (hb : IsIso ((iZ ≫ pullback.fst f
      (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) ∣_ U))
    (hc : IsClosedImmersion ((iZ ≫ pullback.snd f
      (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) ∣_ V))
    (hW : (iZ ≫ pullback.fst f
        (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) ⁻¹ᵁ U =
      (iZ ≫ pullback.snd f
        (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))) ⁻¹ᵁ V)
    (E : DerivedCategory
      (pullback f (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).Modules)
    (hE : Nonempty ((derivedPullback (ofScheme (pullback.snd f
        (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A)) ⁻¹ᵁ V).ι)).obj E ≅
      (derivedPullback (ofScheme (pullback.snd f
        (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A)) ⁻¹ᵁ V).ι)).obj
        ((DerivedCategory.singleFunctor
          (pullback f (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).Modules 0).obj
          ((Scheme.Modules.pushforward iZ).obj (SheafOfModules.unit Z.ringCatSheaf))))) :
    IsClosedImmersion (chowDatumMorphism (pullback.fst f _) (pullback.snd f _) iZ U V hb hW) ∧
      AlgebraicGeometry.FinitePresentation
        (chowDatumMorphism (pullback.fst f _) (pullback.snd f _) iZ U V hb hW) ∧
      ∀ K : DerivedCategory X.Modules,
        (∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent) →
        Nonempty ((derivedPullback (ofScheme V.ι)).obj
            ((derivedPushforward (ofScheme (pullback.snd f
              (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))))).obj
              (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
                  (pullback f (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))).sheaf).obj
                ((derivedPullback (ofScheme (pullback.fst f
                  (projectiveSpaceOver m (Spec (.of A)) ↘ Spec (.of A))))).obj K)).obj E)) ≅
          (derivedPushforward (ofScheme
            (chowDatumMorphism (pullback.fst f _) (pullback.snd f _) iZ U V hb hW))).obj
            ((derivedPullback (ofScheme U.ι)).obj K))
```

## Tag 0CSL, a lemma

[Tag 0CSL](https://stacks.math.columbia.edu/tag/0CSL) in the Stacks Project.

**`AlgebraicGeometry.isPseudoCoherent_of_derivedGlobalSectionsOver_tensor_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/PseudoCoherentByPseudoCoherentTwists.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/PseudoCoherentByPseudoCoherentTwists.lean#L141).

> Let `A` be a ring, let `X` be a scheme separated and of finite presentation over `A`, with
> structure morphism `f : X ⟶ Spec A`, and let `K ∈ D_QCoh(𝒪_X)`. If `RΓ(X, E ⊗^𝐋 K)` is a
> pseudo-coherent object of `D(A)` for every pseudo-coherent object `E` of `D(𝒪_X)`, then `K` is
> pseudo-coherent relative to `A`.
>
> "Separated and of finite presentation over `A`" is `IsSeparated f`, `QuasiCompact f` and
> `LocallyOfFinitePresentation f` (quasi-separatedness follows from separatedness);
> `K ∈ D_QCoh(𝒪_X)` is quasi-coherence of its cohomology sheaves; `RΓ(X, -)` is the `A`-linear
> `AlgebraicGeometry.derivedGlobalSectionsOver f`; pseudo-coherence relative to `A` is
> `AlgebraicGeometry.Scheme.Hom.IsPseudoCoherent f` (Stacks 09UI).

```lean
theorem isPseudoCoherent_of_derivedGlobalSectionsOver_tensor_isPseudoCoherent
    (f : X ⟶ Spec (.of A)) [IsSeparated f] [QuasiCompact f]
    [LocallyOfFinitePresentation f] (K : DerivedCategory X.Modules)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsQuasicoherent)
    (hpc : ∀ E : DerivedCategory X.Modules, RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E →
      StacksDraft.PseudoCoherence.IsPseudoCoherent
        ((derivedGlobalSectionsOver f).obj
          (((Stacks.SheafOfModules.derivedTensor X.sheaf).obj E).obj K))) :
    f.IsPseudoCoherent K
```

## Tag 0GES, a lemma

[Tag 0GES](https://stacks.math.columbia.edu/tag/0GES) in the Stacks Project.

**`AlgebraicGeometry.isPseudoCoherent_of_derivedGlobalSectionsOver_tensor_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/PseudoCoherentByPerfectTwists.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/PseudoCoherentByPerfectTwists.lean#L111).

> **[Stacks, Tag 0GES].** Let `A` be a ring, let `X` be a scheme separated and of finite
> presentation over `A`, with structure morphism `f : X ⟶ Spec A`, and let `K ∈ D_QCoh(𝒪_X)`. If
> `RΓ(X, E ⊗^𝐋 K)` is a pseudo-coherent object of `D(A)` for every perfect object `E` of
> `D(𝒪_X)`, then `K` is pseudo-coherent relative to `A`.

```lean
theorem isPseudoCoherent_of_derivedGlobalSectionsOver_tensor_isPerfect
    (f : X ⟶ Spec (CommRingCat.of A)) [IsSeparated f] [QuasiCompact f]
    [LocallyOfFinitePresentation f]
    (K : DerivedCategory (StructureSheafModules X.sheaf))
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (StructureSheafModules X.sheaf) i).obj K).IsQuasicoherent)
    (hpc : ∀ E : DerivedCategory (StructureSheafModules X.sheaf),
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E →
        StacksDraft.PseudoCoherence.IsPseudoCoherent
          ((derivedGlobalSectionsOver f).obj (((derivedTensor X.sheaf).obj E).obj K))) :
    f.IsPseudoCoherent K
```

## Tag 0GET, a lemma

[Tag 0GET](https://stacks.math.columbia.edu/tag/0GET) in the Stacks Project.

**`AlgebraicGeometry.eventually_subsingleton_ext_of_derivedGlobalSections_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectDetectedByGlobalSections.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectDetectedByGlobalSections.lean#L164). The attribute's comment: “ONLY the vanishing the tag's hypothesis produces: `Ext^i_X(G, K)` and `Hom(G⟦-i⟧, K)` vanish for `i ≪ 0`. That `K` is `Spec(A)`-perfect is NOT proved here; it needs Stacks 0GES, the implication (2) ⇒ (1) of Stacks 0GEH, and condition (1) of Stacks 0GEQ, none of which the library carries. See the implementation notes for what is carried.”.

> **Stacks 0GET, the vanishing that the hypothesis produces.** Let `A` be a ring, let `X` be a
> scheme separated, of finite presentation and flat over `A`, let `G` be a perfect generator of
> `D_QCoh(𝒪_X)` whose dual `G^∨` is perfect, and let `K` be an object of `D_QCoh(𝒪_X)`. If
> `RΓ(X, K ⊗^L_{𝒪_X} E)` is a perfect object of `D(A)` for every perfect object `E` of `D(𝒪_X)`,
> then `Ext^i_X(G, K)` and `Hom_{D(𝒪_X)}(G⟦-i⟧, K)` vanish for `i ≪ 0`.
>
> Perfectness of `G^∨` is Stacks 08DQ, and is a hypothesis here rather than a consequence of
> `hG`; see the implementation notes. It makes the hypothesis on perfect twists apply to `G^∨`,
> so that `RΓ(X, K ⊗^L_{𝒪_X} G^∨)` is the underlying complex of abelian groups of a perfect
> object of `D(A)`. A perfect object of `D(A)` has vanishing cohomology in all sufficiently
> negative degrees and the forgetful functor to abelian groups is exact, so
> `H^i(X, G^∨ ⊗^L_{𝒪_X} K)` vanishes for `i ≪ 0`; that is condition (5) of Stacks 0GEQ, whose
> equivalence with conditions (3) and (2) gives the two assertions.
>
> `Spec(A)`-perfectness of `K` is not proved; see the implementation notes.

```lean
public theorem eventually_subsingleton_ext_of_derivedGlobalSections_isPerfect
    (f : X ⟶ Spec (CommRingCat.of A)) [IsSeparated f] [QuasiCompact f] [Flat f]
    [LocallyOfFinitePresentation f]
    (hqc : CompactSpace X) (hqs : QuasiSeparatedSpace X)
    (G K : DerivedCategory (StructureSheafModules X.sheaf))
    (hG : (ringedSite X.sheaf).IsPerfect G)
    (hGdual : (ringedSite X.sheaf).IsPerfect (derivedDual X.sheaf G))
    (hgen : ∀ L : DerivedCategory (StructureSheafModules X.sheaf),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor
          (StructureSheafModules X.sheaf) i).obj L).IsQuasicoherent) →
        (∀ (n : ℤ) (g : G⟦n⟧ ⟶ L), g = 0) → IsZero L)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (StructureSheafModules X.sheaf) i).obj K).IsQuasicoherent)
    (h08I1 : ∀ i : ℤ, IsIso (derivedTensorDualToSheafHom X.sheaf G (K⟦i⟧)))
    (hperf : ∀ E : DerivedCategory (StructureSheafModules X.sheaf),
      (ringedSite X.sheaf).IsPerfect E →
        ∃ M : DerivedCategory (ModuleCat.{u} A), StacksDraft.Perfect.IsPerfect M ∧
          Nonempty ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
              (((derivedTensor X.sheaf).obj K).obj E) ≅
            (forget₂ (ModuleCat.{u} A) AddCommGrpCat.{u}).mapDerivedCategory.obj M)) :
    (∃ N : ℤ, ∀ i ≤ N, Subsingleton (DerivedCategory.Ext G K i)) ∧
      ∃ N : ℤ, ∀ i ≤ N, Subsingleton (G⟦-i⟧ ⟶ K)
```

**`AlgebraicGeometry.eventually_subsingleton_ext_of_derivedGlobalSections_isPerfect'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectDetectedByGlobalSectionsDual.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectDetectedByGlobalSectionsDual.lean#L121). The attribute's comment: “ONLY the vanishing the tag's hypothesis produces: `Ext^i_X(G, K)` and `Hom(G⟦-i⟧, K)` vanish for `i ≪ 0`, for a perfect generator `G`, with perfectness of the dual and invertibility of the Stacks 08I1 map proved by Stacks 08DQ. That `K` is `Spec(A)`-perfect is NOT proved here; it needs Stacks 0GES, the implication (2) ⇒ (1) of Stacks 0GEH, and condition (1) of Stacks 0GEQ.”.

> **The vanishing of Stacks 0GET, with the duality inputs proved.** Let `A` be a ring, let `X`
> be a scheme separated, of finite presentation and flat over `A`, let `G` be a perfect generator
> of `D_QCoh(𝒪_X)`, and let `K` be an object of `D_QCoh(𝒪_X)`. If `RΓ(X, K ⊗^L_{𝒪_X} E)` is a
> perfect object of `D(A)` for every perfect object `E` of `D(𝒪_X)`, then `Ext^i_X(G, K)` and
> `Hom_{D(𝒪_X)}(G⟦-i⟧, K)` vanish for `i ≪ 0`.
>
> This is `eventually_subsingleton_ext_of_derivedGlobalSections_isPerfect` with its two arguments
> about `G` discharged by [Stacks, Tag 08DQ]: the dual `G^∨` is perfect by the first assertion,
> `Stacks.SheafOfModules.isPerfect_derivedDual`, and the map of [Stacks, Tag 08I1] out of
> `K⟦i⟧ ⊗^L G^∨` is invertible for every `i` by the third,
> `Stacks.SheafOfModules.isIso_derivedTensorDualToSheafHom_of_isPerfect`.
>
> That `K` is `Spec(A)`-perfect, the conclusion of the source, is not proved; the implementation
> notes of `StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectDetectedByGlobalSections.lean`
> list the three results it rests on.

```lean
public theorem eventually_subsingleton_ext_of_derivedGlobalSections_isPerfect'
    (f : X ⟶ Spec (CommRingCat.of A)) [IsSeparated f] [QuasiCompact f] [Flat f]
    [LocallyOfFinitePresentation f]
    (hqc : CompactSpace X) (hqs : QuasiSeparatedSpace X)
    (G K : DerivedCategory (StructureSheafModules X.sheaf))
    (hG : (ringedSite X.sheaf).IsPerfect G)
    (hgen : ∀ L : DerivedCategory (StructureSheafModules X.sheaf),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor
          (StructureSheafModules X.sheaf) i).obj L).IsQuasicoherent) →
        (∀ (n : ℤ) (g : G⟦n⟧ ⟶ L), g = 0) → IsZero L)
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (StructureSheafModules X.sheaf) i).obj K).IsQuasicoherent)
    (hperf : ∀ E : DerivedCategory (StructureSheafModules X.sheaf),
      (ringedSite X.sheaf).IsPerfect E →
        ∃ M : DerivedCategory (ModuleCat.{u} A), StacksDraft.Perfect.IsPerfect M ∧
          Nonempty ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
              (((derivedTensor X.sheaf).obj K).obj E) ≅
            (forget₂ (ModuleCat.{u} A) AddCommGrpCat.{u}).mapDerivedCategory.obj M)) :
    (∃ N : ℤ, ∀ i ≤ N, Subsingleton (DerivedCategory.Ext G K i)) ∧
      ∃ N : ℤ, ∀ i ≤ N, Subsingleton (G⟦-i⟧ ⟶ K)
```

**`AlgebraicGeometry.Scheme.Hom.isRelativelyPerfect_of_isPerfect_derivedGlobalSectionsOver_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectFromGlobalSections.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativelyPerfectFromGlobalSections.lean#L93).

> **Stacks 0GET.** Let `A` be a ring and let `X` be a scheme separated, of finite presentation
> and flat over `A`, with structure morphism `f : X ⟶ Spec A`. Let `K` be an object of
> `D_QCoh(𝒪_X)`. If `RΓ(X, E ⊗^L K)` is a perfect object of `D(A)` for every perfect object `E` of
> `D(𝒪_X)`, then `K` is `Spec(A)`-perfect.
>
> `RΓ(X, -)` is the `A`-linear derived global sections `AlgebraicGeometry.derivedGlobalSectionsOver`,
> perfectness in `D(A)` is `StacksDraft.Perfect.IsPerfect`, perfectness of `E` is Stacks 08CM on the
> ringed space of `X`, and `Spec(A)`-perfectness is
> `AlgebraicGeometry.Scheme.Hom.IsRelativelyPerfect` (Stacks 0DI0). Of finite presentation is
> `[QuasiCompact f] [LocallyOfFinitePresentation f]` together with quasi-separatedness, which
> separatedness implies.

```lean
theorem Scheme.Hom.isRelativelyPerfect_of_isPerfect_derivedGlobalSectionsOver_tensor
    (f : X ⟶ Spec (CommRingCat.of A)) [IsSeparated f] [QuasiCompact f]
    [LocallyOfFinitePresentation f] [Flat f]
    (K : DerivedCategory (StructureSheafModules X.sheaf))
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (StructureSheafModules X.sheaf) i).obj K).IsQuasicoherent)
    (hperf : ∀ E : DerivedCategory (StructureSheafModules X.sheaf),
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E →
        StacksDraft.Perfect.IsPerfect
          ((derivedGlobalSectionsOver f).obj (((derivedTensor X.sheaf).obj E).obj K))) :
    f.IsRelativelyPerfect K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.69, Tag 0CSI](https://stacks.math.columbia.edu/tag/0CSI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
