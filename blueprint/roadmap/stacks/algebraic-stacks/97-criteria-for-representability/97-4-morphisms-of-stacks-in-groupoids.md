---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_comp, AlgebraicGeometry.Stack.isEtale_algebraicSpaceMap_of_comp, AlgebraicGeometry.Stack.isStackInSetoids_of_fppf_baseChange, AlgebraicGeometry.Stack.hasRepresentableDiagonal_of_flatPresentation, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_secondDiagonal_iff
statement: formalized
proof: formalized
---

# 97.4 Morphisms of stacks in groupoids

Section 97.4 of the Stacks Project, [Tag 05XJ](https://stacks.math.columbia.edu/tag/05XJ). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05XK, a lemma

[Tag 05XK](https://stacks.math.columbia.edu/tag/05XK) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/EtalePermanence.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/EtalePermanence.lean#L94). The attribute's comment: “representability”.

> **Stacks 05XK.** Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be 1-morphisms of categories fibred in
> groupoids over the big fppf site of `S`. If `f ≫ g` and `g` are representable by algebraic
> spaces, then so is `f`.
>
> This is cancellation of a representable postcomposition,
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_postcomp`, applied to the triangle
> formed by `f`, `g` and `f ≫ g`, whose comparison 2-cell is the identity.

```lean
theorem isRepresentableByAlgebraicSpaces_of_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsRepresentableByAlgebraicSpaces B S hS (f ≫ g).hom)
    (hg : IsRepresentableByAlgebraicSpaces B S hS g.hom) :
    IsRepresentableByAlgebraicSpaces B S hS f.hom
```

**`AlgebraicGeometry.Stack.isEtale_algebraicSpaceMap_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/EtalePermanence.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/EtalePermanence.lean#L115). The attribute's comment: “étaleness”.

> **Stacks 05XK.** Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be 1-morphisms of categories fibred in
> groupoids over the big fppf site of `S`, with `f ≫ g` and `g` representable by algebraic spaces.
> If every algebraic space representing a base change of `f ≫ g`, respectively of `g`, along a
> scheme-valued point of `𝒵` has étale structural morphism, then so does every algebraic space
> representing a base change of `f` along a scheme-valued point of `𝒴`.
>
> Together with `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_comp` this is the
> statement that an intervening 1-morphism of a factorization through an étale representable
> 1-morphism is itself representable and étale, in the sense of Stacks 04XB at
> `AlgebraicGeometry.Space.IsEtale`.

```lean
theorem isEtale_algebraicSpaceMap_of_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsRepresentableByAlgebraicSpaces B S hS (f ≫ g).hom)
    (hg : IsRepresentableByAlgebraicSpaces B S hS g.hom)
    (hEfg : ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒵.val.obj)
      (_hz : z ⋙ 𝒵.val.p = Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒵.val.p z
          (CatFiberedInGroupoids.homFunctor (f ≫ g)))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      Space.IsEtale B S hS (algebraicSpaceMap B S hS U
        ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom)
    (hEg : ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒵.val.obj)
      (_hz : z ⋙ 𝒵.val.p = Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map U.hom) 𝒴.val.p 𝒵.val.p z
          (CatFiberedInGroupoids.homFunctor g))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      Space.IsEtale B S hS (algebraicSpaceMap B S hS U
        ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom) :
    ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
      (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
          (CatFiberedInGroupoids.homFunctor f))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      Space.IsEtale B S hS (algebraicSpaceMap B S hS U
        ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

## Tag 05XL, a lemma

[Tag 05XL](https://stacks.math.columbia.edu/tag/05XL) in the Stacks Project.

**`AlgebraicGeometry.Stack.isStackInSetoids_of_fppf_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/StackInSetoidsDescent.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/StackInSetoidsDescent.lean#L202).

> **Stacks 05XL.** Let `𝒳 ⟶ 𝒵` and `𝒴 ⟶ 𝒵` be 1-morphisms of categories fibred in groupoids over
> the big fppf site of `S`, with `𝒳` a stack. If `𝒴` and `𝒵` are represented by algebraic spaces `Y`
> and `Z` over `S` through chosen equivalences over the site, the morphism `a : Y ⟶ Z` these
> equivalences associate to `𝒴 ⟶ 𝒵` is surjective, flat and locally of finite presentation, and the
> 2-fibre product `𝒴 ×_𝒵 𝒳` is a stack in setoids, then `𝒳` is a stack in setoids.

```lean
theorem isStackInSetoids_of_fppf_baseChange
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, u, u + 1, w} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵)
    (h𝒳 : 𝒳.val.p.IsStack (BigFppfOver.topology B S hS))
    (Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z)
    (eY : StacksRepresentableCFG.EquivalenceOver 𝒴.val.p
      (presheafOfCategories (Y ⋙ typeToCat)).p)
    (eZ : StacksRepresentableCFG.EquivalenceOver 𝒵.val.p
      (presheafOfCategories (Z ⋙ typeToCat)).p)
    (a : Y ⟶ Z)
    (ha : ∀ y : 𝒴.val.obj,
      a.app (op (𝒴.val.p.obj y)) (PresheafOfCategories.sectionOfObj eY y rfl) =
        PresheafOfCategories.sectionOfObj eZ ((CatFiberedInGroupoids.homFunctor g).obj y)
          (Functor.congr_obj (CatFiberedInGroupoids.homFunctor_comp_p g) y))
    (hsurj : Space.IsSurjective B S hS a) (hflat : Space.IsFlat B S hS a)
    (hlfp : Space.IsLocallyOfFinitePresentation B S hS a)
    (hP : (TwoFibreProductOver.structureFunctor 𝒴.val.p 𝒳.val.p 𝒵.val.p
        (CatFiberedInGroupoids.homFunctor g) (CatFiberedInGroupoids.homFunctor f)).IsStackInSetoids
      (BigFppfOver.topology B S hS)) :
    𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS)
```

## Tag 05XW, a lemma

[Tag 05XW](https://stacks.math.columbia.edu/tag/05XW) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRepresentableDiagonal_of_flatPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatPresentationRepresentableDiagonal.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatPresentationRepresentableDiagonal.lean#L174).

> Let `u : 𝒰 ⟶ 𝒳` be a 1-morphism of categories fibred in groupoids over the
> big fppf site of `S` with `𝒳` a stack, `𝒰` representable by an algebraic space and `u`
> representable by algebraic spaces, surjective, flat and locally of finite presentation. Then
> the diagonal of `𝒳` is representable by algebraic spaces.

```lean
theorem hasRepresentableDiagonal_of_flatPresentation (u : 𝒰 ⟶ 𝒳)
    (h𝒳 : 𝒳.val.p.IsStack (BigFppfOver.topology B S hS))
    (h𝒰 : IsRepresentableByAlgebraicSpace B S hS 𝒰)
    (hu : IsRepresentableByAlgebraicSpaces B S hS u.hom)
    (hsurj : HasRelativeProperty B S hS (Space.surjectiveMorphismProperty B S hS) u hu)
    (hflat : @HasRelativeProperty.{u, u, u + 1, u + 1} B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (k : X ⟶ Y) => Space.IsFlat B S hS k.hom)
      (Space.isFlat_isStableUnderBaseChange B S hS)
      ((Space.isFlat_isLocalAtTarget_fpqc B S hS).of_le
        (Space.fppfPrecoverage_le_fpqcPrecoverage B S hS))
      𝒰 𝒳 u hu)
    (hlfp : HasRelativeProperty B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (k : X ⟶ Y) =>
        Space.IsLocallyOfFinitePresentation B S hS k.hom) u hu) :
    HasRepresentableDiagonal B S hS 𝒳
```

## Tag 07WG, a lemma

[Tag 07WG](https://stacks.math.columbia.edu/tag/07WG) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_secondDiagonal_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalCriterion.lean, line 724](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalCriterion.lean#L724).

> **Stacks 07WG.** The second diagonal of a category fibred in groupoids `𝒳` over the big fppf
> site of `S` — the relative diagonal of its diagonal — is representable by algebraic spaces if and
> only if, for every representable category fibred in groupoids `𝒱` over the site and every
> 1-morphism `g : 𝒱 ⟶ 𝒳 × 𝒳`, the diagonal of the base change `𝒴 = 𝒳 ×_{Δ, 𝒳 × 𝒳, g} 𝒱` is
> representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_secondDiagonal_iff :
    IsRepresentableByAlgebraicSpaces B S hS
      (relativeDiagonalBasedFunctor B S hS 𝒳 (CatFiberedInGroupoids.product 𝒳 𝒳)
        (diagonalBasedFunctor B S hS 𝒳)) ↔
    ∀ (𝒱 : CatFiberedInGroupoids.{u, max u v', u + 1, max (u + 1) w'}
        (BigFppfOver B S hS))
      (_h𝒱 : Stacks.RepresentableMorphism.IsRepresentableCFG 𝒱.val.p)
      (g : 𝒱.val ⥤ᵇ (CatFiberedInGroupoids.product 𝒳 𝒳).val),
      let 𝒴 := twoFibreProduct B S hS (CatFiberedInGroupoids.product 𝒳 𝒳) 𝒳 𝒱
        (diagonalBasedFunctor B S hS 𝒳) g
      IsRepresentableByAlgebraicSpaces B S hS (diagonalBasedFunctor B S hS 𝒴)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.4, Tag 05XJ](https://stacks.math.columbia.edu/tag/05XJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
