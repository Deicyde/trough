---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.CoherentSituation.coherentRelativeDiagonal_affine_finitePresentation, AlgebraicGeometry.Space.CoherentSituation.isFiberedQuasiSeparated_and_isLocallyOfFinitePresentation_toBaseCFG, StacksDraft.CoherentGenericFibre.exists_submodule_finite_flat_isLocalizedModule, AlgebraicGeometry.Space.CoherentSituation.fiberedValuativeExistence_toBaseCFG, AlgebraicGeometry.Space.CoherentPushforwardSituation.cohPushforward, AlgebraicGeometry.Space.isFinite_of_comp_isProper_of_isSeparated_of_isLocallyQuasiFinite, AlgebraicGeometry.Space.isFinitePresentation_of_comp_isProper_of_isSeparated, AlgebraicGeometry.Space.isFinite_comp_of_isLocallyQuasiFinite_of_comp_isProper_of_isSeparated
statement: formalized
proof: formalized
---

# 108.4 Properties of the stack of coherent sheaves

Section 108.4 of the Stacks Project, [Tag 0DLX](https://stacks.math.columbia.edu/tag/0DLX). 10 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DLY, a lemma

[Tag 0DLY](https://stacks.math.columbia.edu/tag/0DLY) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.coherentRelativeDiagonal_affine_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackDiagonalAffineFinitePresentation.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackDiagonalAffineFinitePresentation.lean#L175).

> **The diagonal of `Coh_{X/B}` over `B` is affine and of finite presentation** (Stacks 0DLY).
> The relative diagonal of the projection `Coh_{X/B} ⟶ 𝒮_B` is representable by algebraic spaces,
> and every algebraic space representing one of its base changes along a scheme-valued point over
> `U` is affine and of finite presentation over `U`: that base change is the isomorphism sheaf of
> two objects over one point of `B`
> (`exists_isAlgebraicSpace_isomPresheaf_affineFinitePresentation`).

```lean
theorem coherentRelativeDiagonal_affine_finitePresentation :
    ∃ _hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS
        (Stack.relativeDiagonalBasedFunctor B S hS (coherentCFG D) (baseCFG D.Y)
          (coherentToBase D.categoryData)),
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (Stack.twoFibreProduct B S hS (baseCFG D.Y) (coherentCFG D) (coherentCFG D)
            (coherentToBase D.categoryData) (coherentToBase D.categoryData)).val.obj)
        (_hy : y ⋙ (Stack.twoFibreProduct B S hS (baseCFG D.Y) (coherentCFG D) (coherentCFG D)
            (coherentToBase D.categoryData) (coherentToBase D.categoryData)).val.p =
          Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) (coherentCFG D).val.p
            (Stack.twoFibreProduct B S hS (baseCFG D.Y) (coherentCFG D) (coherentCFG D)
              (coherentToBase D.categoryData) (coherentToBase D.categoryData)).val.p y
            (Stack.relativeDiagonalBasedFunctor B S hS (coherentCFG D) (baseCFG D.Y)
              (coherentToBase D.categoryData)).toFunctor)
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        IsAffineHom B S hS (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom ∧
          IsFinitePresentation B S hS (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

## Tag 0DLZ, a lemma

[Tag 0DLZ](https://stacks.math.columbia.edu/tag/0DLZ) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.isFiberedQuasiSeparated_and_isLocallyOfFinitePresentation_toBaseCFG`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackQuasiSeparatedFinitePresentation.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackQuasiSeparatedFinitePresentation.lean#L86). The attribute's comment: “quasi-separated as Stacks 04YW for a 1-morphism of categories fibred in groupoids; locally of finite presentation as Stacks 06Q2 (1) for the small models, Coh\_\{X/B} having its hom types one universe above the site”.

> Let `f : X ⟶ B` be a morphism of algebraic spaces of finite presentation. Then the morphism
> `Coh_{X/B} ⟶ B` is quasi-separated and locally of finite presentation.
>
> Quasi-separatedness is `AlgebraicGeometry.Stack.IsFiberedQuasiSeparated`, Stacks 04YW for a
> 1-morphism of categories fibred in groupoids; local finite presentation is part (1) of Stacks 06Q2
> for the induced 1-morphism of small models (`AlgebraicGeometry.Stack.smallHomsModelMap`), the
> hom types of `Coh_{X/B}` lying one universe above those of the site. See the implementation notes
> of the file.

```lean
theorem isFiberedQuasiSeparated_and_isLocallyOfFinitePresentation_toBaseCFG
    (D : CoherentSituation B S hS) :
    Stack.IsFiberedQuasiSeparated.{u, u + 1, u + 1} B S hS D.toBaseCFG ∧
      letI := locallySmall_coherentCFG D
      letI := locallySmall_baseCFG D.Y
      Stack.HasPropertyOnEverySmoothDiagram B S hS
        (fun _ _ h => Space.IsLocallyOfFinitePresentation B S hS h)
        (Stack.smallHomsModelMap D.toBaseCFG)
```

## Tag 0DM0, a lemma

[Tag 0DM0](https://stacks.math.columbia.edu/tag/0DM0) in the Stacks Project.

**`StacksDraft.CoherentGenericFibre.exists_submodule_finite_flat_isLocalizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackValuativeChart.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackValuativeChart.lean#L246). The attribute's comment: “the affine-chart case: over a valuation ring a module of finite type on the chart of the generic fibre is the generic fibre of a module of finite type on the chart which is flat over the valuation ring, its flatness being Stacks 0539 and its generic fibre being identified by a localization; the base-change reduction of the first step, the gluing of the chart-wise extensions over Stacks 0829, the proper support, the finite presentation of Stacks 0DLR, and hence the statement for the 1-morphism Cohstack\_\{X/B} -> B in the sense of Stacks 0CLK are not covered”.

> **Stacks 0DM0, on an affine chart over a valuation ring.**  Let `R` be a valuation ring, `A`
> an `R`-algebra and `A_K` the localization of `A` at the nonzero elements of `R`, that is, the
> chart of the generic fibre.  Let `N` be an `A_K`-module of finite type, the coherent module on
> the generic fibre.  Then there is an `A`-submodule `M` of `N` which is of finite type over `A`,
> flat over `R`, and whose generic fibre is `N`, in that `N` is the localization of `M` at the
> nonzero elements of `R`.
>
> This is the chart-wise content of the source's proof: `M` is generated over `A` by a finite
> `A_K`-generating family of `N`, it is flat over `R` because it is torsion free and `R` is a
> valuation ring (Stacks 0539), and its generic fibre is all of `N` because denominators can be
> cleared.

```lean
theorem exists_submodule_finite_flat_isLocalizedModule [IsDomain R] [ValuationRing R]
    [Module.Finite AK N] :
    ∃ M : Submodule A N, Module.Finite A M ∧ Module.Flat R M ∧
      IsLocalizedModule R⁰ (LinearMap.restrictScalars R M.subtype)
```

**`AlgebraicGeometry.Space.CoherentSituation.fiberedValuativeExistence_toBaseCFG`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackValuativeCriterion.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackValuativeCriterion.lean#L100).

> Let `f : X ⟶ B` be a morphism of algebraic spaces which is proper and of finite presentation.
> Then `Coh_{X/B} ⟶ B` satisfies the existence part of the valuative criterion (Stacks 0CLK): every
> 2-commutative square with left edge `Spec K ⟶ Spec R`, for a valuation ring `R` with fraction field
> `K`, admits a dotted arrow after an extension `K'/K` and passage to a valuation ring `R' ⊂ K'`
> dominating `R` — here already with `K' = K` and `R' = R`.
>
> The criterion is `AlgebraicGeometry.Stack.FiberedValuativeExistence`, the data of Stacks 0CLK
> for a 1-morphism of categories fibred in groupoids; it agrees with
> `AlgebraicGeometry.Stack.ValuativeCriterion.Existence` on 1-morphisms of algebraic stacks by
> `AlgebraicGeometry.Stack.valuativeCriterionExistence_iff_fiberedValuativeExistence`.

```lean
theorem CoherentSituation.fiberedValuativeExistence_toBaseCFG (D : CoherentSituation B S hS)
    (hp : IsProper B S hS D.f.hom) :
    Stack.FiberedValuativeExistence.{u, u + 1, u + 1} B S hS D.toBaseCFG
```

## Tag 0DN9, a lemma

[Tag 0DN9](https://stacks.math.columbia.edu/tag/0DN9) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentPushforwardSituation.cohPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardQuasiFinite.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardQuasiFinite.lean#L301).

> Let `B` be an algebraic space and let `π : X ⟶ Y` be a quasi-finite
> morphism of algebraic spaces which are separated and of finite presentation over `B`.  Then `π_*`
> induces a morphism `Coh_{X/B} ⟶ Coh_{Y/B}`: the 1-morphism of categories over the big fppf site
> sending an object `(T, ℱ)` to `(T, π_{T,*}ℱ)` and a morphism `(h, φ)`, with `φ : X_h^*ℱ' ⟶ ℱ`, to
> `(h, θ_h ≫ π_{T,*}φ)`, where `θ_h : Y_h^*π_{T',*}ℱ' ⟶ π_{T,*}X_h^*ℱ'` is the base change map.

```lean
def cohPushforward :
    coherentBasedCategory D.source.categoryData ⥤ᵇ coherentBasedCategory D.target.categoryData
```

**`AlgebraicGeometry.Space.isFinite_of_comp_isProper_of_isSeparated_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardReduction.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardReduction.lean#L56). The attribute's comment: “the reduction of the proof to the finite case: a locally quasi-finite morphism whose source is proper and whose target is separated over the base is finite”.

> Let `π : X ⟶ Y` and `pY : Y ⟶ Z` be morphisms of algebraic spaces over `S`. If the composite
> `X ⟶ Z` is proper, `pY` is separated and `π` is locally quasi-finite, then `π` is finite.

```lean
theorem isFinite_of_comp_isProper_of_isSeparated_of_isLocallyQuasiFinite
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (π : X ⟶ Y) (pY : Y ⟶ Z)
    (hXZ : IsProper B S hS (π ≫ pY)) (hpY : IsSeparated B S hS pY)
    (hπ : IsLocallyQuasiFinite B S hS π) :
    IsFinite B S hS π
```

**`AlgebraicGeometry.Space.isFinitePresentation_of_comp_isProper_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardReduction.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardReduction.lean#L69). The attribute's comment: “the finite presentation of π in the reduction to the finite case”.

> Let `π : X ⟶ Y` and `pY : Y ⟶ Z` be morphisms of algebraic spaces over `S`. If the composite
> `X ⟶ Z` is locally of finite presentation and proper and `pY` is locally of finite type and
> separated, then `π` is of finite presentation.

```lean
theorem isFinitePresentation_of_comp_isProper_of_isSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (π : X ⟶ Y) (pY : Y ⟶ Z)
    (hXZfp : IsLocallyOfFinitePresentation B S hS (π ≫ pY))
    (hXZ : IsProper B S hS (π ≫ pY)) (hpYft : IsLocallyOfFiniteType B S hS pY)
    (hpY : IsSeparated B S hS pY) :
    IsFinitePresentation B S hS π
```

**`AlgebraicGeometry.Space.isFinite_comp_of_isLocallyQuasiFinite_of_comp_isProper_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardReduction.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardReduction.lean#L85). The attribute's comment: “the finiteness of the composite Z ⟶ X\_T ⟶ Y\_T in the first paragraph of the proof, the composite being locally quasi-finite”.

> Let `i : W ⟶ X`, `π : X ⟶ Y` and `pY : Y ⟶ Z` be morphisms of algebraic spaces over `S`. If
> `i` and `π` are locally quasi-finite, the composite `W ⟶ Z` is proper and `pY` is separated, then
> `i ≫ π` is finite.

```lean
theorem isFinite_comp_of_isLocallyQuasiFinite_of_comp_isProper_of_isSeparated
    {W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hW : IsAlgebraicSpace B S hS W)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (i : W ⟶ X) (π : X ⟶ Y) (pY : Y ⟶ Z)
    (hi : IsLocallyQuasiFinite B S hS i) (hπ : IsLocallyQuasiFinite B S hS π)
    (hWZ : IsProper B S hS (i ≫ π ≫ pY)) (hpY : IsSeparated B S hS pY) :
    IsFinite B S hS (i ≫ π)
```

## Tag 0DNA, a lemma

[Tag 0DNA](https://stacks.math.columbia.edu/tag/0DNA) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.isOpenSubspace_supportFactorizationLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackOpenImmersion.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackOpenImmersion.lean#L176). The attribute's comment: “an ingredient only: the open locus of the source's hint, namely the locus in T above which Supp(F) lands in X\_T. The conclusion itself is not stated, the 1-morphism Coh\_\{X/B} ⟶ Coh\_\{Y/B} of 0DN9 not being constructed in this development”.

> For an object `(T, g, F)` of `Coh_{Y/B}` the locus in `T` above which `Supp(F)` lands in
> the open subspace `X_T ⊆ Y_T` is an open subspace of `T`.

```lean
theorem isOpenSubspace_supportFactorizationLocus (hπ : π ≫ D.f = bX)
    (hopen : IsOpenImmersion B S hS π.hom) (obj : CoherentObject D)
    (hU : IsClosed (D.support obj.T obj.F)) :
    IsOpenSubspace B S hS (supportFactorizationLocus D hπ obj hU)
```

**`AlgebraicGeometry.Space.CoherentSituation.factorsThrough_supportFactorizationLocus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackOpenImmersion.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackOpenImmersion.lean#L190). The attribute's comment: “an ingredient only: the universal property of that locus, a test object factoring through it exactly when the base change of Supp(F) lands in X\_T. The residues are the 1-morphism of 0DN9 and the algebraicity of Coh of 09DS”.

> A morphism `T' ⟶ T` from an algebraic space factors through the locus exactly when the
> base change of `Supp(F)` to `T'` lands in `X_T`.

```lean
theorem factorsThrough_supportFactorizationLocus_iff (hπ : π ≫ D.f = bX)
    (hopen : IsOpenImmersion B S hS π.hom) (obj : CoherentObject D)
    (hU : IsClosed (D.support obj.T obj.F))
    {T' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hT' : IsAlgebraicSpace B S hS T')
    (g : T' ⟶ ((schemeSpaceFunctor B S hS).obj obj.T.left).1) :
    (∃ l : T' ⟶ (supportFactorizationLocus D hπ obj hU).toFunctor,
        l ≫ (supportFactorizationLocus D hπ obj hU).ι = g) ↔
      ∃ l : pullback ((supportSubspace D obj hU).ι ≫ (D.projection obj.T).hom) g ⟶
          (baseChangeSpace bX obj.T).1,
        l ≫ (baseChangeOfMap D hπ obj.T).hom =
          pullback.fst ((supportSubspace D obj hU).ι ≫ (D.projection obj.T).hom) g ≫
            (supportSubspace D obj hU).ι
```

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_and_isOpenImmersion_cohPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardOpenImmersion.lean, line 668](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardOpenImmersion.lean#L668). The attribute's comment: “the whole statement: for an open immersion π : X → Y of algebraic spaces separated and of finite presentation over B, the morphism Cohstack\_\{X/B} → Cohstack\_\{Y/B} of Tag 0DN9 is representable by algebraic spaces and an open immersion in the sense of Tag 04XB, which together are representability by open immersions (Tag 04YL (1))”.

> **Stacks 0DNA.**  Let `B` be an algebraic space and let `π : X ⟶ Y` be an open immersion of
> algebraic spaces which are separated and of finite presentation over `B`, the structure morphism
> of `X` being `π ≫ f` for the structure morphism `f : Y ⟶ B`.  Then the morphism
> `Coh_{X/B} ⟶ Coh_{Y/B}` of Stacks 0DN9,
> `AlgebraicGeometry.Space.CoherentPushforwardSituation.cohPushforward`, is an open immersion: it
> is representable by algebraic spaces, and every algebraic space representing its base change
> along a scheme-valued point of `Coh_{Y/B}` is an open subspace of that scheme (Stacks 04XB at open
> immersions), which together are Stacks 04YL (1).
>
> The morphism is fully faithful because `π_{T,*}` is, `π_T` being an open immersion; its essential
> image over a test scheme `T` is the objects `(T, G)` with `Supp(G) ⊆ |X_T|`; and over every
> scheme-valued point `(T₀, G)` of `Coh_{Y/B}` that condition is cut out by the open subscheme on
> `{t ∈ |T₀| : Supp(G) ∩ |Y_t| ⊆ |X_t|}`, the locus of the source's hint.

```lean
theorem isRepresentableByAlgebraicSpaces_and_isOpenImmersion_cohPushforward
    {A X Y : AlgebraicSpaces B S hS} (π : X ⟶ Y) (f : Y ⟶ A)
    (hopen : IsOpenImmersion B S hS π.hom)
    (hsepX : IsSeparated B S hS (π ≫ f).hom) (hfpX : IsFinitePresentation B S hS (π ≫ f).hom)
    (hsepY : IsSeparated B S hS f.hom) (hfpY : IsFinitePresentation B S hS f.hom) :
    let D := CoherentPushforwardSituation.ofIsOpenImmersion π f hopen hsepX hfpX hsepY hfpY
    Stack.IsRepresentableByAlgebraicSpaces B S hS
        (Bicategory.InducedBicategory.mkHom D.cohPushforward :
          coherentCFG D.source ⟶ coherentCFG D.target).hom ∧
      Stack.IsOpenImmersion B S hS
        (Bicategory.InducedBicategory.mkHom D.cohPushforward :
          coherentCFG D.source ⟶ coherentCFG D.target)
```

## Tag 0DNB, a lemma

[Tag 0DNB](https://stacks.math.columbia.edu/tag/0DNB) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_and_isClosedImmersion_cohPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardClosedImmersion.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushforwardClosedImmersion.lean#L460). The attribute's comment: “the whole statement: for a closed immersion π : X → Y of algebraic spaces separated and of finite presentation over B, the morphism Cohstack\_\{X/B} → Cohstack\_\{Y/B} of Tag 0DN9 is representable by algebraic spaces and a closed immersion in the sense of Tag 04XB, which together are representability by closed immersions (Tag 04YL (2))”.

> **Stacks 0DNB.**  Let `B` be an algebraic space and let `π : X ⟶ Y` be a closed immersion of
> algebraic spaces which are separated and of finite presentation over `B`, the structure morphism
> of `X` being `π ≫ f` for the structure morphism `f : Y ⟶ B`.  Then the morphism
> `Coh_{X/B} ⟶ Coh_{Y/B}` of Stacks 0DN9,
> `AlgebraicGeometry.Space.CoherentPushforwardSituation.cohPushforward`, is a closed immersion: it
> is representable by algebraic spaces, and every algebraic space representing its base change
> along a scheme-valued point of `Coh_{Y/B}` is a closed subspace of that scheme (Stacks 04XB at
> closed immersions), which together are Stacks 04YL (2).
>
> The proof is the source's.  The morphism is fully faithful because `π_{T,*}` is, `π_T` being a
> closed immersion (Stacks 04CJ); its essential image over a test scheme `T` is the objects
> `(T, G)` with `G` a direct image along `π_T`, which is the vanishing of the inclusion
> `ker(G ⟶ π_{T,*}π_T^*G) ⟶ G`, and that vanishing after base change is cut out by a closed
> subspace of `T` by Stacks 083M.

```lean
theorem isRepresentableByAlgebraicSpaces_and_isClosedImmersion_cohPushforward
    {A X Y : AlgebraicSpaces B S hS} (π : X ⟶ Y) (f : Y ⟶ A)
    (hclosed : IsClosedImmersion B S hS π.hom)
    (hsepX : IsSeparated B S hS (π ≫ f).hom) (hfpX : IsFinitePresentation B S hS (π ≫ f).hom)
    (hsepY : IsSeparated B S hS f.hom) (hfpY : IsFinitePresentation B S hS f.hom) :
    let D := CoherentPushforwardSituation.ofIsClosedImmersion π f hclosed hsepX hfpX hsepY hfpY
    Stack.IsRepresentableByAlgebraicSpaces B S hS
        (Bicategory.InducedBicategory.mkHom D.cohPushforward :
          coherentCFG D.source ⟶ coherentCFG D.target).hom ∧
      Stack.IsClosedImmersion B S hS
        (Bicategory.InducedBicategory.mkHom D.cohPushforward :
          coherentCFG D.source ⟶ coherentCFG D.target)
```

## Tag 0DNC, a situation

[Tag 0DNC](https://stacks.math.columbia.edu/tag/0DNC) in the Stacks Project.

**`AlgebraicGeometry.Space.NumericalSituation.numericalDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalDirectImage.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalDirectImage.lean#L116). The attribute's comment: “the object `K_i = Rf_{T,*}(E_{i,T} ⊗^𝐋 𝓕)` of `D(𝒪_T)`”.

> For an object `(T, 𝓕)` of `Coh_{X/B}` and `i ∈ I`, the object
> `K_i = Rf_{T,*}(E_{i,T} ⊗^𝐋_{𝒪_{X_T}} 𝓕)` of `D(𝒪_T)`, where `f_T : X_T ⟶ T` is the projection of
> the base change and `E_{i,T}` the derived pullback of `E_i` to `X_T`.

```lean
def numericalDirectImage (i : N.I) :
    DerivedCategory (Modules.{u, u} B S hS (testSpace A).1 (testSpace A).2)
```

**`AlgebraicGeometry.Space.NumericalSituation.numericalEuler`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalDirectImage.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalDirectImage.lean#L124). The attribute's comment: “the function `χ_i : |T| → ℤ`, `t ↦ χ(K_i ⊗^𝐋 κ(t))`”.

> The function `χ_i : |T| → ℤ` whose value at a point `t` of `T` is the Euler characteristic
> `χ(K_i ⊗^𝐋 κ(t)) = ∑ (-1)^n dim H^n(K_i ⊗^𝐋 κ(t))` of the derived fibre of `K_i` at `t`.

```lean
def numericalEuler (i : N.I) : points B S hS (testSpace A).1 → ℤ
```

**`AlgebraicGeometry.Space.NumericalSituation.numericalSubstack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalDirectImage.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalDirectImage.lean#L135). The attribute's comment: “the substack `Coh^P_{X/B} ⊆ Coh_{X/B}` cut out by `χ_i(t) = P(i)`”.

> The substack `Coh^P_{X/B} ⊆ Coh_{X/B}`: the full subcategory of `Coh_{X/B}` on the objects
> `(T, 𝓕)` with `χ_i(t) = P(i)` for all `i ∈ I` and all `t ∈ |T|`.

```lean
abbrev numericalSubstack : Type (u + 1)
```

**`AlgebraicGeometry.Space.NumericalSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariants.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariants.lean#L100). The attribute's comment: “the standing data: separatedness of the relative space, the index set, the family of perfect objects of `D(𝒪_X)`, and the prescribed numerical invariants”.

> **Stacks 0DNC, the standing data.**  Over a morphism `f : X ⟶ Y` of algebraic spaces of
> finite presentation: separatedness of `f`, a set `I`, a perfect object of `D(𝒪_X)` for each
> `i ∈ I`, and the prescribed numerical invariants `P : I → ℤ`.

```lean
structure NumericalSituation
```

## Tag 0DND, a lemma

[Tag 0DND](https://stacks.math.columbia.edu/tag/0DND) in the Stacks Project.

**`AlgebraicGeometry.Space.NumericalSituation.isAlgebraicStack_and_numericalSubstackι_isFlatClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalSubstackAlgebraicFlatClosed.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalSubstackAlgebraicFlatClosed.lean#L62). The attribute's comment: “Coh^P\_\{X/B} is algebraic and Coh^P\_\{X/B} -> Coh\_\{X/B} is a flat closed immersion”.

> In Situation 0DNC the substack `Coh^P_{X/B}` of `Coh_{X/B}` cut out by `χ_i = P(i)` is an
> algebraic stack, and its inclusion into `Coh_{X/B}` is a flat closed immersion: representable by
> algebraic spaces, a closed immersion and flat (Properties of Stacks, Section 04XB).

```lean
theorem isAlgebraicStack_and_numericalSubstackι_isFlatClosedImmersion :
    Stack.IsAlgebraicStack.{u, w} B S hS
        (D.conditionCFG N.HasNumericalInvariants N.hasNumericalInvariants_inherited).val ∧
      Stack.IsRepresentableByAlgebraicSpaces B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited).hom ∧
      Stack.IsClosedImmersion B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited) ∧
      Stack.IsFlat B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited)
```

**`AlgebraicGeometry.Space.NumericalSituation.numericalSubstackι_isOpenAndClosedImmersion_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalSubstackOpenClosedImmersion.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalSubstackOpenClosedImmersion.lean#L80). The attribute's comment: “the case I finite: Coh^P\_\{X/B} is an open and closed substack of Coh\_\{X/B}”.

> If `I` is finite, `Coh^P_{X/B}` is an open and closed substack of `Coh_{X/B}`: its inclusion
> is representable by algebraic spaces, an open immersion and a closed immersion.

```lean
theorem numericalSubstackι_isOpenAndClosedImmersion_of_finite [Finite N.I] :
    Stack.IsRepresentableByAlgebraicSpaces B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited).hom ∧
      Stack.IsOpenImmersion B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited) ∧
      Stack.IsClosedImmersion B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited)
```

**`AlgebraicGeometry.Space.NumericalSituation.numericalSubstackι_isOpenAndClosedImmersion_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalSubstackOpenClosedImmersion.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalSubstackOpenClosedImmersion.lean#L96). The attribute's comment: “the case B locally Noetherian: Coh^P\_\{X/B} is an open and closed substack of Coh\_\{X/B}”.

> If `B` is locally Noetherian (`hB`) and `I` is arbitrary, `Coh^P_{X/B}` is an open and closed
> substack of `Coh_{X/B}`: its inclusion is representable by algebraic spaces, an open immersion and
> a closed immersion.

```lean
theorem numericalSubstackι_isOpenAndClosedImmersion_of_isLocallyNoetherian
    (hB : IsLocallyNoetherian B S hS D.Y.1) :
    Stack.IsRepresentableByAlgebraicSpaces B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited).hom ∧
      Stack.IsOpenImmersion B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited) ∧
      Stack.IsClosedImmersion B S hS
        (D.conditionι N.HasNumericalInvariants N.hasNumericalInvariants_inherited)
```

## Tag 0DNE, a lemma

[Tag 0DNE](https://stacks.math.columbia.edu/tag/0DNE) in the Stacks Project.

**`AlgebraicGeometry.Space.NumericalSituation.isClopen_setOf_chi_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalSubstack.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalSubstack.lean#L131). The attribute's comment: “the open-and-closed clause only, at the level of the locus in |T| cut out by the condition chi\_i = P i; Coh\_\{X/B} is no category here, so no substack claim is made”.

> **Stacks 0DNE, the open-and-closed clause, at the level of the locus in `|T|`.**  For an
> object `(T, 𝓕)` of `Coh_{X/B}` and an index `i`, the subset of `|T|` on which the numerical
> invariant `χ_i` takes the prescribed value `P i` is open and closed: `χ_i` is locally constant by
> Stacks 0D1Z (`AlgebraicGeometry.Space.isLocallyConstant_of_isEtaleLocallyDerivedFibreChi`), and
> the fibres of a locally constant function are open and closed.

```lean
theorem isClopen_setOf_chi_eq (c : ChiData B S hS D N) (A : CoherentObject D) (i : N.I) :
    IsClopen {t : testPoints B S hS D A | c.chi A i t = N.P i}
```

**`AlgebraicGeometry.Space.NumericalSituation.isOpenAndClosedCondition_ofDerivedTensorPowerProducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalTensorPowerProductsOpenClosed.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalTensorPowerProductsOpenClosed.lean#L63).

> Let `f : X ⟶ B` be a separated morphism of finite presentation of algebraic spaces,
> `E_1, …, E_r` perfect objects of `D(𝒪_X)` and `P : ℤ^{⊕ r} ⟶ ℤ`.  Then the subcategory
> `Coh^P_{X/B} ⊆ Coh_{X/B}` of the objects `(T, 𝓕)` with
> `χ(X_t, (E_1^{⊗ n_1} ⊗ ⋯ ⊗ E_r^{⊗ n_r})_t ⊗^𝐋 𝓕_t) = P(n)` for all `n ∈ ℤ^{⊕ r}` and all
> `t ∈ T` is an open and closed substack.

```lean
theorem isOpenAndClosedCondition_ofDerivedTensorPowerProducts (hf : IsSeparated B S hS D.f.hom)
    {r : ℕ}
    (E : Fin r → @DerivedCategory (Modules.{u, u} B S hS D.X.1 D.X.2) _ _
      (HasDerivedCategory.standard _))
    (hE : ∀ j, letI := HasDerivedCategory.standard (Modules.{u, u} B S hS D.X.1 D.X.2)
      (smallEtaleRingedSite B S hS D.X.1 D.X.2).IsPerfect (E j))
    (P : (Fin r → ℤ) → ℤ) :
    IsOpenAndClosedCondition D (ofDerivedTensorPowerProducts hf E hE P).HasNumericalInvariants
```

## Tag 0DNF, an example

[Tag 0DNF](https://stacks.math.columbia.edu/tag/0DNF) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.exists_hilbertPolynomialι_obj_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialSubstack.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialSubstack.lean#L104). The attribute's comment: “an object `(T ⟶ B, 𝓕)` of `Coh_{X/B}` lies in `Coh^P_{X/B}` iff `P(n) = χ(X_t, 𝓕_t ⊗ L_t^{⊗ n})` for all `n ∈ ℤ` and `t ∈ T`”.

> An object `(T ⟶ B, 𝓕)` of `Coh_{X/B}` lies in `Coh^P_{X/B} = Coh^{P, L}_{X/B}` (is the image of
> an object of it) exactly when `P(n) = χ(X_t, 𝓕_t ⊗_{𝒪_{X_t}} L_t^{⊗ n})` for every `n ∈ ℤ` and
> every `t ∈ T`.

```lean
theorem exists_hilbertPolynomialι_obj_eq_iff (A : CoherentObject D) :
    (∃ X, (CatFiberedInGroupoids.homFunctor (D.hilbertPolynomialι L P)).obj X = A) ↔
      ∀ (n : ℤ) (t : A.testScheme), P n = CoherentObject.twistedEuler L A t n
```

**`AlgebraicGeometry.Space.CoherentSituation.hilbertPolynomialι_isOpenAndClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialSubstack.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialSubstack.lean#L119). The attribute's comment: “`Coh^P_{X/B} = Coh^{P,L}_{X/B} ⊂ Coh_{X/B}` is an open and closed substack”.

> `Coh^P_{X/B} ⊆ Coh_{X/B}` is an open and closed substack: the inclusion
> `Coh^{P, L}_{X/B} ⟶ Coh_{X/B}` is representable by algebraic spaces, an open immersion and a closed
> immersion (Stacks 0DNE for `I = ℤ` and `E_n = L^{⊗ n}`).

```lean
theorem hilbertPolynomialι_isOpenAndClosedImmersion :
    Stack.IsRepresentableByAlgebraicSpaces B S hS (D.hilbertPolynomialι L P).hom ∧
      Stack.IsOpenImmersion B S hS (D.hilbertPolynomialι L P) ∧
      Stack.IsClosedImmersion B S hS (D.hilbertPolynomialι L P)
```

**`AlgebraicGeometry.Space.CoherentSituation.isAlgebraicStack_hilbertPolynomialCFG`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialSubstack.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialSubstack.lean#L141). The attribute's comment: “for `f : X ⟶ B` separated and of finite presentation, `Coh^P_{X/B}` is an algebraic stack”.

> For a separated morphism `f : X ⟶ B` of finite presentation, `Coh^{P, L}_{X/B}` is an algebraic
> stack: `Coh_{X/B}` is algebraic (Stacks 09DS, with Grothendieck's existence theorem Stacks 0CXB),
> and the inclusion of `Coh^{P, L}_{X/B}` is representable by algebraic spaces (Stacks 05UM).

```lean
theorem isAlgebraicStack_hilbertPolynomialCFG (hsep : IsSeparated B S hS D.f.hom) :
    Stack.IsAlgebraicStack.{u, w} B S hS (D.hilbertPolynomialCFG L P).val
```

**`AlgebraicGeometry.Space.CoherentSituation.hilbertPolynomialLocus_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialSubstack.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialSubstack.lean#L156). The attribute's comment: “`Coh_{X/B} = ∐_{P numerical polynomial} Coh^P_{X/B}` is a disjoint union decomposition, read on each object `(T, 𝓕)`: the loci of the numerical polynomials are open and closed, pairwise disjoint, cover `T`, and the locus of `P` cuts out `Coh^P_{X/B}`”.

> The disjoint union decomposition `Coh_{X/B} = ∐_P Coh^P_{X/B}`, read on each object
> `A = (T, 𝓕)` of `Coh_{X/B}`: the loci of the functions `P : ℤ → ℤ`
> (`AlgebraicGeometry.Space.CoherentObject.hilbertPolynomialLocus`) are open and closed in `T`,
> pairwise disjoint, and those of the numerical polynomials cover `T` (Stacks 0DN4); a morphism
> `A' ⟶ A` of `Coh_{X/B}` has its source in `Coh^{P, L}_{X/B}` exactly when its map of test schemes
> lands in the locus of `P`.

```lean
theorem hilbertPolynomialLocus_decomposition (A : CoherentObject D) :
    (∀ P : ℤ → ℤ, IsClopen (A.hilbertPolynomialLocus L P)) ∧
      (⋃ P : {P : ℤ → ℤ // ∃ p : Polynomial ℚ, ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ)},
        A.hilbertPolynomialLocus L P.1) = Set.univ ∧
      Pairwise (fun P Q : ℤ → ℤ =>
        Disjoint (A.hilbertPolynomialLocus L P) (A.hilbertPolynomialLocus L Q)) ∧
      ∀ (P : ℤ → ℤ) (A' : CoherentObject D) (φ : CoherentHom A' A),
        CoherentObject.HasHilbertPolynomial L P A' ↔
          Set.range φ.baseScheme ⊆ A.hilbertPolynomialLocus L P
```

**`AlgebraicGeometry.Space.NumericalSituation.ofInvertibleTwists`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariantsTwist.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariantsTwist.lean#L186). The attribute's comment: “the substack as the specialisation of Situation 0DNC to the index set `ℤ` and the family `n ↦ L^{⊗ n}`; perfectness of those twists is a hypothesis, and openness and closedness (Lemma 0DNE) and the disjoint union decomposition are not established”.

> **Stacks 0DNF, the specialisation of Situation 0DNC.**  Over a separated morphism
> `f : X ⟶ B` of algebraic spaces of finite presentation, an invertible `𝒪_X`-module `L` and a
> map `P : ℤ → ℤ`, the standing data of Stacks 0DNC with index set `I = ℤ` and with the family
> `n ↦ L^{⊗ n}` of perfect objects of `D(𝒪_X)`.  This is the datum relative to which the source's
> `Coh^P_{X/B} = Coh^{P,L}_{X/B}` is formed.
>
> Perfectness of the twists `L^{⊗ n}` is the hypothesis `perfect`: the source takes it for granted
> for an invertible module, and this development has no route to it on the small étale ringed site
> of an algebraic space.  Nothing here asserts that the resulting substack is open and closed —
> that is Lemma 0DNE, which is absent — nor that `P` is a numerical polynomial, which the source
> assumes but which no clause of the specialisation uses.

```lean
def NumericalSituation.ofInvertibleTwists (separated : IsSeparated B S hS D.f.hom)
    (L : Modules.{u, u} B S hS D.X.1 D.X.2)
    [hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS D.X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B S hS D.X.1 D.X.2).O)).property L]
    (perfect : ∀ n : ℤ, (smallEtaleRingedSite B S hS D.X.1 D.X.2).IsPerfect
      (invertibleTwistObject B S hS D.X.1 D.X.2 L n))
    (P : ℤ → ℤ) : NumericalSituation.{u, 0, u} B S hS D
```

**`AlgebraicGeometry.Space.IsPrescribedTwistedEuler`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariantsTwist.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariantsTwist.lean#L243). The attribute's comment: “the membership condition `P(n) = χ(X_t, 𝓕_t ⊗ L_t^{⊗ n})`, stated for a given family of fibrewise twisted Euler characteristics, which this development cannot construct”.

> **Stacks 0DNF, the membership condition.**  An object `(T ⟶ B, 𝓕)` of `Coh_{X/B}` lies in
> `Coh^P_{X/B} = Coh^{P,L}_{X/B}` exactly when
>
> `P(n) = χ(X_t, 𝓕_t ⊗_{𝒪_{X_t}} L_t^{⊗ n})`
>
> holds for every `n ∈ ℤ` and every `t ∈ T`.  Here `ι` is the type of points of the test scheme and
> `χ t n` is the Euler characteristic above.  That family is *given*: the Euler characteristic of a
> perfect object on an algebraic space cannot be constructed in this development, for the reason
> recorded in the implementation notes of
> `StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariants.lean`, and the same device is used by
> `AlgebraicGeometry.Space.IsEtaleLocallyDerivedFibreChi`.

```lean
def IsPrescribedTwistedEuler {ι : Type v} (P : ℤ → ℤ) (χ : ι → ℤ → ℤ) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.4, Tag 0DLX](https://stacks.math.columbia.edu/tag/0DLX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
