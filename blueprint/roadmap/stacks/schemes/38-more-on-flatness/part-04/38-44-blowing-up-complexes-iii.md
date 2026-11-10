---
declaration: section
origin: cited
lean: AlgebraicGeometry.ComplexAndDivisorSituation.nonempty_etaDerivedPullbackRestrict_divisorComplement, Stacks.Chow.exists_closedImmersion_graphObjectRestrict, Stacks.Chow.isIso_pullback_snd_graphBlowupToBase, Stacks.Chow.isIso_resLE_graphBlowupToBase, Stacks.Chow.nonempty_derivedPullback_modificationSectionAtZero_graphObject, Stacks.Chow.nonempty_derivedPullback_graphObject_of_comp_eq, Stacks.Chow.exists_isLocallyBoundedFiniteLocallyFree_graphObject, AlgebraicGeometry.ComplexAndDivisorSituation.isIso_resLE_projectiveLineTriple
statement: formalized
proof: formalized
---

# 38.44 Blowing up complexes, III

Section 38.44 of the Stacks Project, [Tag 0F8Z](https://stacks.math.columbia.edu/tag/0F8Z). 1 tag here is carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F90, a lemma

[Tag 0F90](https://stacks.math.columbia.edu/tag/0F90) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.nonempty_etaDerivedPullbackRestrict_divisorComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/EtaDerivedDivisorComplement.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/EtaDerivedDivisorComplement.lean#L129). The attribute's comment: “clause (2): the restriction of Q to A^1\_X is the pullback of E”.

> **Clause (2) of Stacks tag 0F90.**  Let `(X, D, M)` be a triple as in Situation 0F8S, let
> `b : X' ⟶ X` be a morphism along which `D' = b⁻¹D` is defined, and let `Q = Lη_{ℐ'}Lb^*M` be the
> object of Stacks tag 0F8U.  The restriction of `Q` to the preimage of the complement `X ∖ D` of
> the support of the divisor is the pullback of `M`:
>
> `Lj^*Q ≅ L(b ∘ j)^*M`, where `j : b⁻¹(X ∖ D) ⟶ X'`.
>
> In the graph construction the scheme is `𝐏¹_X`, the divisor is `(𝐏¹_X)_∞`, the complement of its
> support is the chart `𝐀¹_X`, and the object of the triple is `Lp^*E`; so the displayed
> isomorphism says that the restriction of `Q` to `𝐀¹_X` is the pullback of `E`.  The morphism `b`
> is arbitrary: nothing beyond the definedness of `b⁻¹D` is asked of it, so the statement holds
> in particular for the morphism of Stacks tag 0GTY, `goodBlowupToBase`; the graph construction
> itself is `Stacks.Chow.graphTriple` in `GraphConstructionTriple.lean`.

```lean
theorem nonempty_etaDerivedPullbackRestrict_divisorComplement
    (S : ComplexAndDivisorSituation.{u, d}) {X' : Scheme.{u}} (b : X' ⟶ S.X)
    (hD : Stacks.Divisors.IsPullbackDefined b S.D) :
    Nonempty (S.etaDerivedPullbackRestrict b hD (b ⁻¹ᵁ S.divisorComplement).ι ≅
      S.derivedPullbackObject ((b ⁻¹ᵁ S.divisorComplement).ι ≫ b))
```

**`Stacks.Chow.exists_closedImmersion_graphObjectRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionSubscheme.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionSubscheme.lean#L193). The attribute's comment: “clauses (3) and (4)”.

> For the morphism `b : W ⟶ 𝐏¹_X` of the graph construction and `Q = Lη_ℐ Lb^*Lp^*E`, there is
> a closed immersion `t : T ⟶ W_∞` of finite presentation such that
> * the cohomology sheaves of `L(t ≫ i_∞)^*Q` are finite locally free,
> * (3) every point of `W_∞` lying over an open `V ⊆ X` on which all the cohomology sheaves of `E`
>   are finite locally free lies in `T`, and
> * (4) at a point of `T` lying over such an open `V`, the rank of `H^n(L(t ≫ i_∞)^*Q)` is the rank
>   `r` of `H^n(E)` on `V`.

```lean
theorem exists_closedImmersion_graphObjectRestrict :
    ∃ (T : Scheme.{u}) (t : T ⟶ modificationFibreAtInfinity f (graphBlowupToBase f E hE)),
      IsClosedImmersion t ∧ LocallyOfFinitePresentation t ∧
      ∃ hH : ∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
          ((DerivedCategory.homologyFunctor T.Modules n).obj
            ((derivedPullback (t ≫ modificationInclusionAtInfinity f
              (graphBlowupToBase f E hE)).toLRSHom.toShHom).obj (graphObject f E hE))),
        (∀ (w) (V : X.Opens),
          modificationProjectionAtInfinity f (graphBlowupToBase f E hE) w ∈ V →
          (∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
            ((Scheme.Modules.pullback V.ι).obj
              ((DerivedCategory.homologyFunctor X.Modules n).obj E))) →
          w ∈ Set.range t) ∧
        ∀ (τ : T) (V : X.Opens) (n : ℤ) (r : ℕ),
          modificationProjectionAtInfinity f (graphBlowupToBase f E hE) (t τ) ∈ V →
          (∀ m : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
            ((Scheme.Modules.pullback V.ι).obj
              ((DerivedCategory.homologyFunctor X.Modules m).obj E))) →
          AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
            ((Scheme.Modules.pullback V.ι).obj
              ((DerivedCategory.homologyFunctor X.Modules n).obj E)) r →
          @Scheme.Modules.finiteLocallyFreeRank T _ (hH n) τ = r
```

**`Stacks.Chow.isIso_pullback_snd_graphBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean#L189). The attribute's comment: “clause (1), over A^1\_X, as the base change of b along A^1\_X ⟶ P^1\_X”.

> **Clause (1) of Stacks tag 0F90, over `𝐀¹_X`.** The base change of `b : W ⟶ 𝐏¹_X` along
> the chart `𝐀¹_X ⟶ 𝐏¹_X` is an isomorphism.

```lean
theorem isIso_pullback_snd_graphBlowupToBase :
    IsIso (pullback.snd (graphBlowupToBase f E hE) (projectiveLineAffineChart f))
```

**`Stacks.Chow.isIso_resLE_graphBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean#L201). The attribute's comment: “clause (1)”.

> **Clause (1) of Stacks tag 0F90.** The morphism `b : W ⟶ 𝐏¹_X` is an isomorphism over
> `𝐏¹_U ∪ 𝐀¹_X = p⁻¹U ∪ 𝐀¹_X`, where `U ⊆ X` is the maximal open over which the cohomology
> sheaves of `E` are locally free.

```lean
theorem isIso_resLE_graphBlowupToBase :
    IsIso ((graphBlowupToBase f E hE).resLE
      (pullback.fst f (relativeProjectiveLine S ↘ S) ⁻¹ᵁ
          ⟨RingedSpace.cohomologyFiniteFreeLocus E,
            RingedSpace.isOpen_cohomologyFiniteFreeLocus E hE⟩ ⊔
        (projectiveLineAffineChart f).opensRange)
      (graphBlowupToBase f E hE ⁻¹ᵁ
        (pullback.fst f (relativeProjectiveLine S ↘ S) ⁻¹ᵁ
          ⟨RingedSpace.cohomologyFiniteFreeLocus E,
            RingedSpace.isOpen_cohomologyFiniteFreeLocus E hE⟩ ⊔
        (projectiveLineAffineChart f).opensRange)) le_rfl)
```

**`Stacks.Chow.nonempty_derivedPullback_modificationSectionAtZero_graphObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean#L264). The attribute's comment: “clause (2), restricted along the section at zero X ⟶ W”.

> **Clause (2) of Stacks tag 0F90, along the section at zero.** The pullback of `Q` along the
> section at zero `i_0 : X ⟶ W`, which exists because `b` is an isomorphism over `𝐀¹_X`, is
> `E`.

```lean
theorem nonempty_derivedPullback_modificationSectionAtZero_graphObject :
    Nonempty ((derivedPullback (modificationSectionAtZero f (graphBlowupToBase f E hE)
        (isIso_modificationFibreAtZeroProjection f _
          (isIso_pullback_snd_graphBlowupToBase f E hE))).toLRSHom.toShHom).obj
        (graphObject f E hE) ≅ E)
```

**`Stacks.Chow.nonempty_derivedPullback_graphObject_of_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean#L287). The attribute's comment: “clause (2)”.

> **Clause (2) of Stacks tag 0F90.** The restriction of `Q` to `𝐀¹_X` is the pullback of `E`:
> for the open immersion `a : 𝐀¹_X ⟶ W` lifting the chart `𝐀¹_X ⟶ 𝐏¹_X` (it exists by
> `Stacks.Chow.isIso_pullback_snd_graphBlowupToBase`), `La^*Q` is the pullback of `E` along the
> projection `𝐀¹_X ⟶ X`.

```lean
theorem nonempty_derivedPullback_graphObject_of_comp_eq
    (a : affineLineOver X ⟶ graphBlowup f E hE)
    (ha : a ≫ graphBlowupToBase f E hE = projectiveLineAffineChart f) :
    Nonempty ((derivedPullback a.toLRSHom.toShHom).obj (graphObject f E hE) ≅
      (derivedPullback (pullback.fst (terminal.from X)
        (terminal.from (Spec (.of (Polynomial (ULift.{u} ℤ)))))).toLRSHom.toShHom).obj E)
```

**`Stacks.Chow.exists_isLocallyBoundedFiniteLocallyFree_graphObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GraphConstructionTriple.lean#L302). The attribute's comment: “clause (5)”.

> **Clause (5) of Stacks tag 0F90.** If `E` is represented by a locally bounded complex of
> finite locally free `𝒪_X`-modules, then `Q` is represented by a locally bounded complex of
> finite locally free `𝒪_W`-modules. The pullback along `p` of a representative of `E` represents
> `Lp^*E`, and Stacks tag 0GU0 applies.

```lean
theorem exists_isLocallyBoundedFiniteLocallyFree_graphObject
    (hrep : ∃ ℳ : CochainComplex X.Modules ℤ, IsLocallyBoundedFiniteLocallyFree ℳ ∧
      Nonempty (DerivedCategory.Q.obj ℳ ≅ E)) :
    ∃ 𝒬 : CochainComplex (graphBlowup f E hE).Modules ℤ,
      IsLocallyBoundedFiniteLocallyFree 𝒬 ∧
        Nonempty (DerivedCategory.Q.obj 𝒬 ≅ graphObject f E hE)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isIso_resLE_projectiveLineTriple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/MacphersonGraph.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/MacphersonGraph.lean#L134). The attribute's comment: “clause (1): `b` is an isomorphism over `𝐏¹_U ∪ 𝐀¹_X`, with `𝐀¹_X` the complement of `(𝐏¹_X)_∞`”.

> **Clause (1) of Stacks tag 0F90.**  The morphism `b : W ⟶ 𝐏¹_X` of Stacks tag 0GTY for the
> triple `(𝐏¹_X, (𝐏¹_X)_∞, Lp^*E)` is an isomorphism over `𝐏¹_U ∪ 𝐀¹_X`.

```lean
theorem isIso_resLE_projectiveLineTriple :
    IsIso ((projectiveLineTriple X E hE).goodBlowupToBase.resLE
      ((Stacks.Chow.relativeProjectiveLine X ↘ X) ⁻¹ᵁ cohomologyLocallyFreeOpen X E hE ⊔
        (projectiveLineTriple X E hE).divisorComplement)
      ((projectiveLineTriple X E hE).goodBlowupToBase ⁻¹ᵁ
        ((Stacks.Chow.relativeProjectiveLine X ↘ X) ⁻¹ᵁ cohomologyLocallyFreeOpen X E hE ⊔
          (projectiveLineTriple X E hE).divisorComplement)) le_rfl)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.nonempty_etaDerivedPullbackRestrict_projectiveLineTriple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/MacphersonGraph.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/MacphersonGraph.lean#L153). The attribute's comment: “clause (2): the restriction of `Q` to `𝐀¹_X` is the pullback of `E`”.

> **Clause (2) of Stacks tag 0F90.**  The restriction of `Q = Lη_ℐ Lb^*Lp^*E` to the preimage
> `j : b⁻¹(𝐀¹_X) ⟶ W` of `𝐀¹_X` is the pullback of `E`: `Lj^*Q ≅ L(p ∘ b ∘ j)^*E`.  By clause (1)
> `b⁻¹(𝐀¹_X) ⟶ 𝐀¹_X` is an isomorphism.

```lean
theorem nonempty_etaDerivedPullbackRestrict_projectiveLineTriple :
    Nonempty ((projectiveLineTriple X E hE).etaDerivedPullbackRestrict
        (projectiveLineTriple X E hE).goodBlowupToBase
        (projectiveLineTriple X E hE).isPullbackDefined_goodBlowupToBase
        ((projectiveLineTriple X E hE).goodBlowupToBase ⁻¹ᵁ
          (projectiveLineTriple X E hE).divisorComplement).ι ≅
      (derivedPullback (((projectiveLineTriple X E hE).goodBlowupToBase ⁻¹ᵁ
          (projectiveLineTriple X E hE).divisorComplement).ι ≫
          (projectiveLineTriple X E hE).goodBlowupToBase ≫
          (Stacks.Chow.relativeProjectiveLine X ↘ X)).toLRSHom.toShHom).obj E)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_isLocallyBoundedFiniteLocallyFree_projectiveLineTriple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/MacphersonGraph.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/MacphersonGraph.lean#L184). The attribute's comment: “clause (5): a locally bounded finite locally free representative of `E` gives one of `Q`”.

> **Clause (5) of Stacks tag 0F90.**  If `E` is represented by a locally bounded complex of
> finite locally free `𝒪_X`-modules, then `Q = Lη_ℐ Lb^*Lp^*E` is represented by a locally bounded
> complex of finite locally free `𝒪_W`-modules.

```lean
theorem exists_isLocallyBoundedFiniteLocallyFree_projectiveLineTriple
    (hrep : ∃ P : CochainComplex (OXMod.{u, u} X.toRingedSpace) ℤ,
      Stacks.Chow.IsLocallyBoundedFiniteLocallyFree P ∧ Nonempty (DerivedCategory.Q.obj P ≅ E)) :
    ∃ 𝒬 : CochainComplex (projectiveLineTriple X E hE).goodBlowup.Modules ℤ,
      Stacks.Chow.IsLocallyBoundedFiniteLocallyFree 𝒬 ∧
        Nonempty (DerivedCategory.Q.obj 𝒬 ≅
          (projectiveLineTriple X E hE).etaDerivedPullbackObject
            (projectiveLineTriple X E hE).goodBlowupToBase
            (projectiveLineTriple X E hE).isPullbackDefined_goodBlowupToBase)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_closedSubscheme_projectiveLineTriple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/MacphersonGraph.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/MacphersonGraph.lean#L222). The attribute's comment: “clauses (3) and (4): the closed immersion `i : T → W_∞` locally of finite presentation, with `(W_∞ → X)⁻¹U ⊆ T` scheme theoretically, `Li^*Q` with finite locally free cohomology sheaves, and for `t ∈ T` over `x ∈ U` the stalk `H^n(Li^*Q)_t` free over `𝒪_{T,t}` of the rank (Module.finrank) of `H^n(E)_x` over `𝒪_{X,x}`; `Li^*Q` is etaDerivedPullbackRestrict along `T → W_∞ → W`”.

> **Clauses (3) and (4) of Stacks tag 0F90.**  For the morphism `b : W ⟶ 𝐏¹_X` of tag 0GTY
> for the triple `(𝐏¹_X, (𝐏¹_X)_∞, Lp^*E)`, with `W_∞ = b⁻¹(𝐏¹_X)_∞` and `Q = Lη_ℐ Lb^*Lp^*E`,
> there is a closed immersion `i : T ⟶ W_∞` locally of finite presentation such that
> * (3) `(W_∞ ⟶ X)⁻¹U ⊆ T` scheme theoretically and the cohomology sheaves of `Li^*Q` are finite
>   locally free, and
> * (4) for `t ∈ T` with image `x ∈ U` in `X`, the stalk `H^n(Li^*Q)_t` is free over `𝒪_{T,t}` of
>   the rank of `H^n(E)_x` over `𝒪_{X,x}`.
>
> This is tag 0F8X for the triple, read through `H^n(Lp^*E)_y = 𝒪_{𝐏¹_X,y} ⊗ H^n(E)_{p y}`, `p`
> being flat, and the inclusion of `𝐏¹_U` in the locus where the cohomology of `Lp^*E` is locally
> free.

```lean
theorem exists_closedSubscheme_projectiveLineTriple :
    ∃ T : ((projectiveLineTriple X E hE).D.comap
        (projectiveLineTriple X E hE).goodBlowupToBase).subscheme.IdealSheafData,
      LocallyOfFinitePresentation T.subschemeι ∧
      T.comap ((((projectiveLineTriple X E hE).D.comap
          (projectiveLineTriple X E hE).goodBlowupToBase).subschemeι ≫
          (projectiveLineTriple X E hE).goodBlowupToBase ≫
          (Stacks.Chow.relativeProjectiveLine X ↘ X)) ⁻¹ᵁ
            cohomologyLocallyFreeOpen X E hE).ι = ⊥ ∧
      (∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        ((projectiveLineTriple X E hE).etaDerivedPullbackRestrictHomology
          (projectiveLineTriple X E hE).goodBlowupToBase
          (projectiveLineTriple X E hE).isGoodOver_goodBlowupToBase.pullbackDefined
          (T.subschemeι ≫ ((projectiveLineTriple X E hE).D.comap
            (projectiveLineTriple X E hE).goodBlowupToBase).subschemeι) n)) ∧
      ∀ (n : ℤ) (t : T.subscheme)
        (_ : ((T.subschemeι ≫ ((projectiveLineTriple X E hE).D.comap
          (projectiveLineTriple X E hE).goodBlowupToBase).subschemeι) ≫
          (projectiveLineTriple X E hE).goodBlowupToBase ≫
          (Stacks.Chow.relativeProjectiveLine X ↘ X)).base t ∈ cohomologyLocallyFreeOpen X E hE),
        letI F := (projectiveLineTriple X E hE).etaDerivedPullbackRestrictHomology
          (projectiveLineTriple X E hE).goodBlowupToBase
          (projectiveLineTriple X E hE).isGoodOver_goodBlowupToBase.pullbackDefined
          (T.subschemeι ≫ ((projectiveLineTriple X E hE).D.comap
            (projectiveLineTriple X E hE).goodBlowupToBase).subschemeι) n
        letI x := ((T.subschemeι ≫ ((projectiveLineTriple X E hE).D.comap
          (projectiveLineTriple X E hE).goodBlowupToBase).subschemeι) ≫
          (projectiveLineTriple X E hE).goodBlowupToBase ≫
          (Stacks.Chow.relativeProjectiveLine X ↘ X)).base t
        letI : Module (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
            (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) :=
          RingedSpace.moduleStalk (X := T.subscheme.toRingedSpace) F t
        letI : Module (ToType (X.presheaf.stalk x))
            (ToType (TopCat.Presheaf.stalk ((DerivedCategory.homologyFunctor
              (OXMod.{u, u} X.toRingedSpace) n).obj E).val.presheaf x)) :=
          RingedSpace.moduleStalk (X := X.toRingedSpace)
            ((DerivedCategory.homologyFunctor (OXMod.{u, u} X.toRingedSpace) n).obj E) x
        Module.Free (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
            (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) ∧
          Module.finrank (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
              (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) =
            Module.finrank (ToType (X.presheaf.stalk x))
              (ToType (TopCat.Presheaf.stalk ((DerivedCategory.homologyFunctor
                (OXMod.{u, u} X.toRingedSpace) n).obj E).val.presheaf x))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.44, Tag 0F8Z](https://stacks.math.columbia.edu/tag/0F8Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
