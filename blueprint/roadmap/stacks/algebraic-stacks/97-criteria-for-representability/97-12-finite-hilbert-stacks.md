---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.mapAbsolute, AlgebraicGeometry.Stack.mapAbsolute_comp_forgetAbsoluteStructure, AlgebraicGeometry.Stack.mapRelative, AlgebraicGeometry.Stack.mapRelative_obj_α, AlgebraicGeometry.Stack.mapRelative_comp_forgetRelativeStructure, AlgebraicGeometry.Stack.mapRelative_comp_forgetTarget, AlgebraicGeometry.Stack.mapRelative_comp_forgetRelativeToFiniteCover, AlgebraicGeometry.Stack.isEquivalence_hilbertComparison
statement: formalized
proof: formalized
---

# 97.12 Finite Hilbert stacks

Section 97.12 of the Stacks Project, [Tag 05XM](https://stacks.math.columbia.edu/tag/05XM). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05XN, a lemma

[Tag 05XN](https://stacks.math.columbia.edu/tag/05XN) in the Stacks Project.

**`AlgebraicGeometry.Stack.mapAbsolute`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L137). The attribute's comment: “the induced 1-morphism of absolute finite Hilbert stacks”.

> The 1-morphism `ℋ_d(𝒳') ⟶ ℋ_d(𝒳)` of absolute degree-`d` finite Hilbert stacks induced by a
> 1-morphism `G : 𝒳' ⟶ 𝒳` of stacks in groupoids: the canonical 1-morphism of finite Hilbert
> stacks for the 2-commutative square whose two columns are the structure morphisms of `𝒳'` and
> `𝒳`.

```lean
def mapAbsolute :
    absoluteHilbertCategory (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳') ⥤ᵇ
      absoluteHilbertCategory (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳)
```

**`AlgebraicGeometry.Stack.mapAbsolute_comp_forgetAbsoluteStructure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L146). The attribute's comment: “compatibility with the forgetful 1-morphism `ℋ_d(𝒳) ⟶ ℋ_d`”.

> The induced 1-morphism of absolute finite Hilbert stacks leaves the underlying degree-`d`
> finite locally free cover unchanged.

```lean
theorem mapAbsolute_comp_forgetAbsoluteStructure :
    BasedFunctor.comp (mapAbsolute B S hS d 𝒳' 𝒳 G)
        (forgetAbsoluteStructure (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳)) =
      forgetAbsoluteStructure (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳')
```

**`AlgebraicGeometry.Stack.mapRelative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L198). The attribute's comment: “the canonical 1-morphism”.

> The canonical 1-morphism `ℋ_d(𝒳'/𝒴') ⟶ ℋ_d(𝒳/𝒴)` of degree-`d` finite Hilbert stacks
> attached to a 2-commutative square of stacks in groupoids with horizontal arrows `G` and `H`,
> vertical arrows `F'` and `F`, and 2-isomorphism `γ : H ∘ F' ⟶ F ∘ G`.

```lean
def mapRelative :
    finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳') (𝒴 := 𝒴') (F := F') (d := d) ⥤ᵇ
      finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d)
```

**`AlgebraicGeometry.Stack.mapRelative_obj_α`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L207). The attribute's comment: “action on the identification”.

> The canonical 1-morphism sends an object with identification `α` to one whose identification
> is `α` transported across the given 2-isomorphism.

```lean
theorem mapRelative_obj_α (P : FiniteHilbert.Object B S hS 𝒳' 𝒴' F' d) :
    ((mapRelative B S hS d 𝒳' 𝒴' 𝒳 𝒴 F' F G H γ).obj P).α =
      squareComparison γ P.x ≫ H.map P.α
```

**`AlgebraicGeometry.Stack.mapRelative_comp_forgetRelativeStructure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L215). The attribute's comment: “compatibility with the forgetful 1-morphism `ℋ_d(𝒳/𝒴) ⟶ ℋ_d(𝒳)`”.

> The canonical 1-morphism is compatible with the forgetful 1-morphisms to the absolute finite
> Hilbert stacks: on them it induces the 1-morphism attached to `G`.

```lean
theorem mapRelative_comp_forgetRelativeStructure :
    BasedFunctor.comp (mapRelative B S hS d 𝒳' 𝒴' 𝒳 𝒴 F' F G H γ)
        (forgetRelativeStructure (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳) (𝒴 := 𝒴)
          (F := F)) =
      BasedFunctor.comp
        (forgetRelativeStructure (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳') (𝒴 := 𝒴')
          (F := F'))
        (mapAbsolute B S hS d 𝒳' 𝒳 G)
```

**`AlgebraicGeometry.Stack.mapRelative_comp_forgetTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L228). The attribute's comment: “compatibility with the forgetful 1-morphism `ℋ_d(𝒳/𝒴) ⟶ 𝒴`”.

> The canonical 1-morphism is compatible with the forgetful 1-morphisms to the target stacks: on
> them it induces `H`.

```lean
theorem mapRelative_comp_forgetTarget :
    BasedFunctor.comp (mapRelative B S hS d 𝒳' 𝒴' 𝒳 𝒴 F' F G H γ)
        (forgetTarget (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)) =
      BasedFunctor.comp
        (forgetTarget (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳') (𝒴 := 𝒴') (F := F')) H
```

**`AlgebraicGeometry.Stack.mapRelative_comp_forgetRelativeToFiniteCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L238). The attribute's comment: “compatibility with the forgetful 1-morphism `ℋ_d(𝒳/𝒴) ⟶ ℋ_d`”.

> The canonical 1-morphism leaves the underlying degree-`d` finite locally free cover
> unchanged.

```lean
theorem mapRelative_comp_forgetRelativeToFiniteCover :
    BasedFunctor.comp (mapRelative B S hS d 𝒳' 𝒴' 𝒳 𝒴 F' F G H γ)
        (forgetRelativeToFiniteCover (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳) (𝒴 := 𝒴)
          (F := F)) =
      forgetRelativeToFiniteCover (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳') (𝒴 := 𝒴')
        (F := F')
```

## Tag 05XP, a lemma

[Tag 05XP](https://stacks.math.columbia.edu/tag/05XP) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalence_hilbertComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L588). The attribute's comment: “the comparison functor is an equivalence”.

> If the comparison functor of the given square is an equivalence, then so is the comparison
> functor `ℋ_d(𝒳'/𝒴') ⥤ ℋ_d(𝒳/𝒴) ×_𝒴 𝒴'` of the induced square.

```lean
theorem isEquivalence_hilbertComparison
    (h : (sourceComparison B S hS 𝒳' 𝒴' 𝒳 𝒴 F' F G H γ).IsEquivalence) :
    (hilbertComparison B S hS d 𝒳' 𝒴' 𝒳 𝒴 F' F G H γ).IsEquivalence
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_hilbertSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean, line 601](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Functoriality.lean#L601).

> If the given 2-commutative square of stacks in groupoids is 2-cartesian, then so is the
> induced square of degree-`d` finite Hilbert stacks: the canonical 1-morphism
> `ℋ_d(𝒳'/𝒴') ⟶ ℋ_d(𝒳/𝒴)` and the forgetful 1-morphism `ℋ_d(𝒳'/𝒴') ⟶ 𝒴'` exhibit `ℋ_d(𝒳'/𝒴')`
> as the 2-fibre product `𝒴' ×_𝒴 ℋ_d(𝒳/𝒴)`.

```lean
noncomputable def isTwoFibreProduct_hilbertSquare
    (hcart : Bicategory.IsTwoFibreProduct (sourceSquare B S hS 𝒳' 𝒴' 𝒳 𝒴 F' F G H γ)) :
    Bicategory.IsTwoFibreProduct (hilbertSquare B S hS d 𝒳' 𝒴' 𝒳 𝒴 F' F G H γ)
```

## Tag 05YG, a lemma

[Tag 05YG](https://stacks.math.columbia.edu/tag/05YG) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_and_isEtale_mapRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbertRelativeEtale.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbertRelativeEtale.lean#L378). The attribute's comment: “part (1)”.

> Let `G : 𝒳' ⟶ 𝒳` be a 1-morphism of stacks in groupoids over the big fppf site of `S` which
> is representable by algebraic spaces and étale, and let `γ` present `𝒳' ⟶ 𝒴` as the composite of
> `G` with `F : 𝒳 ⟶ 𝒴`. Then the canonical 1-morphism `ℋ_d(𝒳'/𝒴) ⟶ ℋ_d(𝒳/𝒴)` of Stacks 05XN is
> representable by algebraic spaces and étale.
>
> The conclusion is the shape of `AlgebraicGeometry.Stack.IsRelativelyEtale` at the free universes
> of the stacks involved: representability by algebraic spaces, and étaleness over `S` of every
> algebraic space representing a fibre over a scheme-valued point. The two halves are
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_mapRelative` and
> `AlgebraicGeometry.Stack.isEtale_mapRelative`.

```lean
theorem isRepresentableByAlgebraicSpaces_and_isEtale_mapRelative
    (γ : BasedFunctor.comp F' (𝟙 𝒴.toBasedCategory) ≅ BasedFunctor.comp G F)
    (hGrep : IsRepresentableByAlgebraicSpaces B S hS G)
    (hGet : ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒳.toBasedCategory.obj)
      (_hz : z ⋙ 𝒳.toBasedCategory.p = Over.map U.hom)
      (W : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hW : IsAlgebraicSpace B U.left.1 U.left.2 W),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map U.hom) 𝒳'.toBasedCategory.p 𝒳.toBasedCategory.p z
          G.toFunctor)
        (presheafOfCategories (W ⋙ typeToCat)).p) →
      Space.IsEtale B S hS (algebraicSpaceMap B S hS U
        ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨W, hW⟩)).hom) :
    ∃ _ : IsRepresentableByAlgebraicSpaces B S hS
        (mapRelative B S hS d 𝒳' 𝒴 𝒳 𝒴 F' F G (𝟙 𝒴.toBasedCategory) γ),
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
            (d := d)).obj)
        (_hy : y ⋙ (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴)
          (F := F) (d := d)).p = Over.map U.hom)
        (A : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hA : IsAlgebraicSpace B U.left.1 U.left.2 A),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳') (𝒴 := 𝒴) (F := F')
              (d := d)).p
            (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
              (d := d)).p y
            (mapRelative B S hS d 𝒳' 𝒴 𝒳 𝒴 F' F G (𝟙 𝒴.toBasedCategory) γ).toFunctor)
          (presheafOfCategories (A ⋙ typeToCat)).p) →
        Space.IsEtale B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨A, hA⟩)).hom
```

**`AlgebraicGeometry.Stack.isSurjectiveOnObjects_mapRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbertRelativeEtale.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbertRelativeEtale.lean#L470). The attribute's comment: “part (2)”.

> If `G : 𝒳' ⟶ 𝒳` is representable by algebraic spaces, étale and surjective, then the
> canonical 1-morphism `ℋ_d(𝒳'/𝒴) ⟶ ℋ_d(𝒳/𝒴)` is surjective.
>
> By Stacks 06D7 surjectivity of a 1-morphism representable by algebraic spaces is surjectivity of
> every algebraic space representing one of its fibres over a scheme-valued point; that algebraic
> space is a space of sections of a surjective étale morphism to a finite cover of the point, which
> is surjective over the point by Stacks 05XQ.

```lean
theorem isSurjectiveOnObjects_mapRelative
    (γ : BasedFunctor.comp F' (𝟙 𝒴.toBasedCategory) ≅ BasedFunctor.comp G F)
    (hGrep : IsRepresentableByAlgebraicSpaces B S hS G)
    (hGet : ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒳.toBasedCategory.obj)
      (_hz : z ⋙ 𝒳.toBasedCategory.p = Over.map U.hom)
      (W : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hW : IsAlgebraicSpace B U.left.1 U.left.2 W),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map U.hom) 𝒳'.toBasedCategory.p 𝒳.toBasedCategory.p z
          G.toFunctor)
        (presheafOfCategories (W ⋙ typeToCat)).p) →
      Space.IsEtale B S hS (algebraicSpaceMap B S hS U
        ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨W, hW⟩)).hom)
    (hGsurj : IsSurjectiveOnObjects B S hS 𝒳'.toBasedCategory.p 𝒳.toBasedCategory.p
      G.toFunctor) :
    IsSurjectiveOnObjects B S hS
      (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳') (𝒴 := 𝒴) (F := F')
        (d := d)).p
      (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d)).p
      (mapRelative B S hS d 𝒳' 𝒴 𝒳 𝒴 F' F G (𝟙 𝒴.toBasedCategory) γ).toFunctor
```

## Tag 05XS, a lemma

[Tag 05XS](https://stacks.math.columbia.edu/tag/05XS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRelativelyEtale_mapRelativeFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FiniteHilbertEtale.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FiniteHilbertEtale.lean#L472). The attribute's comment: “part (1)”.

> **Stacks 05XS, part (1).** Let `G : 𝒳' ⟶ 𝒳` and `H : 𝒴' ⟶ 𝒴` be 1-morphisms of stacks in
> groupoids over the big fppf site of `S` which are representable by algebraic spaces and étale,
> and let `γ : H ∘ F' ⟶ F ∘ G` make the square with vertical arrows `F'`, `F` 2-commute. Then the
> canonical 1-morphism `ℋ_d(𝒳'/𝒴') ⟶ ℋ_d(𝒳/𝒴)` of Stacks 05XN is representable by algebraic
> spaces and étale.
>
> The proof is the source's. The 1-morphism is 2-isomorphic to the composite of
> `ℋ_d(𝒳'/𝒴') ⟶ ℋ_d((𝒳 ×_𝒴 𝒴')/𝒴')`, which is representable by algebraic spaces and étale by
> Stacks 05YG because `𝒳' ⟶ 𝒳 ×_𝒴 𝒴'` is by Stacks 05XK, with
> `ℋ_d((𝒳 ×_𝒴 𝒴')/𝒴') ⟶ ℋ_d(𝒳/𝒴)`, which is a base change of `H` by Stacks 05XP and therefore
> representable by algebraic spaces and étale by Stacks 045C.

```lean
theorem isRelativelyEtale_mapRelativeFibered
    (γ : BasedFunctor.comp F' H ≅ BasedFunctor.comp G F)
    (hG : IsRelativelyEtale B S hS (stackMapFibered B S hS G))
    (hH : IsRelativelyEtale B S hS (stackMapFibered B S hS H)) :
    IsRelativelyEtale B S hS (mapRelativeFibered B S hS d 𝒳 𝒴 F 𝒳' 𝒴' F' G H γ)
```

**`AlgebraicGeometry.Stack.isSurjectiveOnObjects_mapRelativeFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FiniteHilbertEtale.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FiniteHilbertEtale.lean#L497). The attribute's comment: “part (2)”.

> **Stacks 05XS, part (2).** Let `G : 𝒳' ⟶ 𝒳` and `H : 𝒴' ⟶ 𝒴` be 1-morphisms of stacks in
> groupoids over the big fppf site of `S` which are representable by algebraic spaces and étale,
> and let `γ : H ∘ F' ⟶ F ∘ G` make the square with vertical arrows `F'`, `F` 2-commute. If
> moreover `H` is surjective and the induced 1-morphism `𝒳' ⟶ 𝒳 ×_𝒴 𝒴'` to the 2-fibre product is
> surjective, then the canonical 1-morphism `ℋ_d(𝒳'/𝒴') ⟶ ℋ_d(𝒳/𝒴)` of Stacks 05XN is surjective.
>
> The induced 1-morphism is `AlgebraicGeometry.Stack.targetFibreProductComparison`, into the
> 2-fibre product over the site of Stacks 0040, which the source writes `𝒴' ×_𝒴 𝒳`. The proof is
> the source's: `ℋ_d(𝒳'/𝒴') ⟶ ℋ_d((𝒳 ×_𝒴 𝒴')/𝒴')` is surjective by Stacks 05YG, the base change
> `ℋ_d((𝒳 ×_𝒴 𝒴')/𝒴') ⟶ ℋ_d(𝒳/𝒴)` of `H` is surjective as `H` is, and composites of surjective
> 1-morphisms are surjective.

```lean
theorem isSurjectiveOnObjects_mapRelativeFibered
    (γ : BasedFunctor.comp F' H ≅ BasedFunctor.comp G F)
    (hG : IsRelativelyEtale B S hS (stackMapFibered B S hS G))
    (hH : IsRelativelyEtale B S hS (stackMapFibered B S hS H))
    (hHSurj : IsSurjectiveOnObjects B S hS (stackFibered B S hS 𝒴').val.p
      (stackFibered B S hS 𝒴).val.p
      (CatFiberedInGroupoids.homFunctor (stackMapFibered B S hS H)))
    (hcomparison : IsSurjectiveOnObjects B S hS (stackFibered B S hS 𝒳').val.p
      (stackFibered B S hS (targetFibreProduct B S hS 𝒳 𝒴 F 𝒴' H)).val.p
      (CatFiberedInGroupoids.homFunctor (stackMapFibered B S hS
        (targetFibreProductComparison B S hS 𝒳 𝒴 F 𝒳' 𝒴' F' G H γ)))) :
    IsSurjectiveOnObjects B S hS (finiteHilbertFibered B S hS d 𝒳' 𝒴' F').val.p
      (finiteHilbertFibered B S hS d 𝒳 𝒴 F).val.p
      (CatFiberedInGroupoids.homFunctor
        (mapRelativeFibered B S hS d 𝒳 𝒴 F 𝒳' 𝒴' F' G H γ))
```

## Tag 05YH, a lemma

[Tag 05YH](https://stacks.math.columbia.edu/tag/05YH) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpacesForgetToProduct_of_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/ProductFibreEquivalence.lean, line 1030](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/ProductFibreEquivalence.lean#L1030).

> Let `F : 𝒳 ⟶ 𝒴` be a 1-morphism of stacks in groupoids over the big fppf
> site of a scheme `S` and let `d` be a natural number. If the diagonal `𝒴 ⟶ 𝒴 × 𝒴` is
> representable by algebraic spaces then the 1-morphism
>
> `ℋ_d(𝒳/𝒴) ⟶ ℋ_d(𝒳) × 𝒴`
>
> of Equation 05WD is representable by algebraic spaces, in the sense of Stacks 02ZW.

```lean
theorem isRepresentableByAlgebraicSpacesForgetToProduct_of_diagonal
    (hΔ : HasRepresentableDiagonal B S hS (targetCFG (𝒴 := 𝒴))) :
    IsRepresentableByAlgebraicSpacesForgetToProduct
      (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
```

## Tag 05YJ, a lemma

[Tag 05YJ](https://stacks.math.columbia.edu/tag/05YJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_mapRelative_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbertRelativeRepresentable.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbertRelativeRepresentable.lean#L307).

> **Stacks 05YJ.** Let `G : 𝒳' ⟶ 𝒳` be a 1-morphism of stacks in groupoids over the big fppf
> site of `S` which is representable by algebraic spaces, and let `γ` present `𝒳' ⟶ 𝒴` as the
> composite of `G` with `F : 𝒳 ⟶ 𝒴`. Then the canonical 1-morphism
> `ℋ_d(𝒳'/𝒴) ⟶ ℋ_d(𝒳/𝒴)` of degree-`d` relative finite Hilbert stacks is representable by
> algebraic spaces.
>
> The fibre over the universal family of an object `ξ = (U, Z, y, x, α)` is the restriction of
> scalars along `Z ⟶ U` of an algebraic space representing the fibre of `G` over `x`, which is an
> algebraic space by Stacks 05YF; that is
> `AlgebraicGeometry.Stack.FiniteHilbert.Object.exists_isAlgebraicSpace_sectionSpace`. An arbitrary
> scheme-valued point reduces to those by the 2-Yoneda normalisation
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_universalFamilies`.

```lean
theorem isRepresentableByAlgebraicSpaces_mapRelative_of_representable
    (γ : BasedFunctor.comp F' (𝟙 𝒴.toBasedCategory) ≅ BasedFunctor.comp G F)
    (hG : IsRepresentableByAlgebraicSpaces B S hS G) :
    IsRepresentableByAlgebraicSpaces B S hS
      (mapRelative B S hS d 𝒳' 𝒴 𝒳 𝒴 F' F G (𝟙 𝒴.toBasedCategory) γ)
```

## Tag 06CH, a lemma

[Tag 06CH](https://stacks.math.columbia.edu/tag/06CH) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_finiteHilbertToTargetCFG`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LimitPreserving.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LimitPreserving.lean#L554). The attribute's comment: “p : ℋ\_d(𝒳/𝒴) ⟶ 𝒴 is limit preserving on objects”.

> **Stacks 06CH.** Let `F : 𝒳 ⟶ 𝒴` be a 1-morphism of stacks in groupoids over the big fppf
> site of `S` which is representable by algebraic spaces (Stacks 02ZW) and locally of finite
> presentation (every algebraic space representing a base change of `F` along a scheme-valued
> point of `𝒴` has locally finitely presented structural morphism, Stacks 03YK). Then
> `p : ℋ_d(𝒳/𝒴) ⟶ 𝒴` is limit preserving on objects (Stacks 06CU).
>
> The affine limits `U = lim U_i` of Stacks 06CU are indexed, as in the source, by a set: the
> index category lies in the universe of the schemes.
>
> Given an object `Ξ = (U, Z, y, x, α)` of `ℋ_d(𝒳/𝒴)` over the limit and a comparison of `y` with
> an object `y_i` of `𝒴` at the stage `i`, the cover `Z`, the object `x` and the identification `α`
> composed with that comparison spread out to a cover `Z_{i'}`, an object `x_{i'}` and an
> identification `η` at a later stage `i'` (Stacks 01ZM and the degree-`d` form of Stacks 06AC for
> the cover, Stacks 06CX for the object and the identification). Lift `y_i`
> along `U_{i'} ⟶ U_i` to `y_{i'}`; the lift is strongly cartesian, so `η` factors uniquely
> through it, giving the identification `α_{i'}` of `Ξ_{i'}`, and the comparison factors uniquely
> through it, giving the morphism of objects of `𝒴` of the morphism `Ξ ⟶ Ξ_{i'}`. The remaining
> fields of that morphism are the spread-out data, and its compatibility condition holds because
> both of its sides factor the same morphism through the lift.

```lean
theorem isLimitPreservingOnObjects_finiteHilbertToTargetCFG
    (hFrep : IsRepresentableByAlgebraicSpaces B S hS F)
    (hFlfp : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.toBasedCategory.obj),
      y ⋙ 𝒴.toBasedCategory.p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.toBasedCategory.p 𝒴.toBasedCategory.p y
            F.toFunctor) (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsLocallyOfFinitePresentation B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom) :
    BigFppfOver.IsLimitPreservingOnObjects.{u, u, u} B S hS
      (finiteHilbertCFG.{u, v, w, ws} B S hS 𝒳 𝒴 F d)
      (CatFiberedInGroupoids.mk 𝒴.toBasedCategory
        𝒴.isStackInGroupoids.isFiberedInGroupoids)
      (finiteHilbertToTargetCFG.{u, v, w, ws} B S hS 𝒳 𝒴 F d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.12, Tag 05XM](https://stacks.math.columbia.edu/tag/05XM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
