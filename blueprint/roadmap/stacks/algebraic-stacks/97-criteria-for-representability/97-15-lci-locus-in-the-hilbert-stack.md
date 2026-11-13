---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.FiniteHilbert.lciLocus, AlgebraicGeometry.Stack.lciFiniteHilbertCategory, AlgebraicGeometry.Stack.lciFiniteHilbertInclusion, AlgebraicGeometry.Stack.FiniteHilbert.RelativeMapData.map_hom_ofHom, AlgebraicGeometry.Stack.FiniteHilbert.lciLocus_iff, AlgebraicGeometry.Stack.relativeObj, AlgebraicGeometry.Stack.relativeMap, AlgebraicGeometry.Stack.FiniteHilbert.RelativeMapData.exists_iso_map
statement: formalized
proof: formalized
---

# 97.15 LCI locus in the Hilbert stack

Section 97.15 of the Stacks Project, [Tag 06CJ](https://stacks.math.columbia.edu/tag/06CJ). 6 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06CJ, the section

[Tag 06CJ](https://stacks.math.columbia.edu/tag/06CJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.FiniteHilbert.lciLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocus.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocus.lean#L158). The attribute's comment: “the objects of ℋ\_d(𝒳/𝒴) with unramified Koszul relative map”.

> The objects of the relative finite Hilbert category `ℋ_d(𝒳/𝒴)` whose relative map
> `x_α : Z ⟶ X_y` of Stacks 06CK is unramified and a local complete intersection morphism, for every
> algebraic space representing the relevant 2-fibre product and every equivalence exhibiting it.

```lean
def lciLocus : ObjectProperty (Object B S hS 𝒳 𝒴 F d)
```

**`AlgebraicGeometry.Stack.lciFiniteHilbertCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocus.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocus.lean#L178). The attribute's comment: “the full subcategory ℋ\_\{d,lci}(𝒳/𝒴) of ℋ\_d(𝒳/𝒴)”.

> The local complete intersection locus `ℋ_{d,lci}(𝒳/𝒴)`: the full subcategory of the relative
> finite Hilbert category on the objects whose relative map is unramified and a local complete
> intersection morphism, regarded as a category over the big fppf site through the restriction of the
> canonical projection.

```lean
noncomputable def lciFiniteHilbertCategory : BasedCategory (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Stack.lciFiniteHilbertInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocus.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocus.lean#L187). The attribute's comment: “the inclusion ℋ\_\{d,lci}(𝒳/𝒴) ⊂ ℋ\_d(𝒳/𝒴)”.

> The inclusion `ℋ_{d,lci}(𝒳/𝒴) ⊂ ℋ_d(𝒳/𝒴)` of the local complete intersection locus into the
> relative finite Hilbert category, as a 1-morphism of categories over the big fppf site.

```lean
def lciFiniteHilbertInclusion :
    lciFiniteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d) ⥤ᵇ
      finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d)
```

**`AlgebraicGeometry.Stack.FiniteHilbert.RelativeMapData.map_hom_ofHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusBaseChange.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusBaseChange.lean#L456). The attribute's comment: “the remark preceding the definition of the locus: the relative map of the source of a morphism of quintuples is the base change of the relative map of the target along the base component”.

> The relative map of the transported data is the restriction of the original relative map
> along the base component of the morphism, read through the comparison of the representable
> presheaf of the cover of the source quintuple with the restriction of the representable presheaf
> of the cover of the target — an isomorphism by
> `AlgebraicGeometry.Stack.FiniteHilbert.RelativeMapData.isIso_restrictYonedaHom_coverComparison`,
> so that the relative map of the source *is* the base change of the relative map of the target.

```lean
theorem map_hom_ofHom :
    (ofHom φ D).map.hom =
      OverShriek.restrictYonedaHom φ.f.left (coverComparison φ) ≫
        (OverShriek.relocalizeRestrict φ.f.left).map D.map.hom
```

**`AlgebraicGeometry.Stack.FiniteHilbert.lciLocus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusChoice.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusChoice.lean#L179). The attribute's comment: “membership of the locus is testable on a single choice of the data exhibiting the relative map”.

> A quintuple lies in the local complete intersection locus exactly when the relative map
> attached to *one* set of data exhibiting it is unramified and a local complete intersection
> morphism.

```lean
theorem lciLocus_iff {P : Object B S hS 𝒳 𝒴 F d} (D : RelativeMapData P) :
    lciLocus (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d) P ↔
      (Space.IsUnramified B P.U.left.1 P.U.left.2 D.map.hom ∧
        Space.IsLocalCompleteIntersection B P.U.left.1 P.U.left.2 D.map.hom)
```

## Tag 06CK, an equation

[Tag 06CK](https://stacks.math.columbia.edu/tag/06CK) in the Stacks Project.

**`AlgebraicGeometry.Stack.relativeObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMapToRepresentingSpace.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMapToRepresentingSpace.lean#L72). The attribute's comment: “the object (Z, Z → U, x, α) of the 2-fibre product”.

> The object `ξ = (Z, Z → U, x, α)` of the 2-fibre product
> `(Sch/U)_{fppf} ×_{y, 𝒴, F} 𝒳` attached to a scheme `Z` over `U`, an object `x` of `𝒳` over `Z`
> and an isomorphism `α : y|_Z ⟶ F(x)` vertical over `Z`. It lies over `Z` for the first
> projection.

```lean
def relativeObj (Z : BigFppfOver B U.left.1 U.left.2) (x : 𝒳.obj)
    (hx : 𝒳.p.obj x = (Over.map U.hom).obj Z) (α : y.obj Z ≅ F.toFunctor.obj x)
    (hα : 𝒴.p.IsHomLift (𝟙 ((Over.map U.hom).obj Z)) α.hom) :
    TwoFibreProductOver (Over.map U.hom) 𝒳.p 𝒴.p y F.toFunctor
```

**`AlgebraicGeometry.Stack.relativeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMapToRepresentingSpace.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMapToRepresentingSpace.lean#L214). The attribute's comment: “the morphism x\_α of the left-hand diagram”.

> The morphism `x_α : Z ⟶ X_y` of algebraic spaces over `U` attached to a
> scheme `Z` over `U`, an object `x` of `𝒳` over `Z` and an isomorphism `α : y|_Z ⟶ F(x)` vertical
> over `Z`: the morphism of presheaves on the big fppf site of `U` named, under the Yoneda lemma,
> by the section of `X_y` over `Z` that `ξ = (Z, Z → U, x, α)` names.

```lean
def relativeMap (F : 𝒳 ⥤ᵇ 𝒴) (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.obj)
    (e : StacksRepresentableCFG.EquivalenceOver
      (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.p 𝒴.p y F.toFunctor)
      (presheafOfCategories (Xy ⋙ typeToCat)).p)
    (hXy : IsAlgebraicSpace B U.left.1 U.left.2 Xy)
    (Z : BigFppfOver B U.left.1 U.left.2) (x : 𝒳.obj)
    (hx : 𝒳.p.obj x = (Over.map U.hom).obj Z) (α : y.obj Z ≅ F.toFunctor.obj x)
    (hα : 𝒴.p.IsHomLift (𝟙 ((Over.map U.hom).obj Z)) α.hom) :
    (⟨yoneda.obj Z, isAlgebraicSpace_yoneda B U.left.1 U.left.2 Z⟩ :
        AlgebraicSpaces B U.left.1 U.left.2) ⟶ ⟨Xy, hXy⟩
```

**`AlgebraicGeometry.Stack.FiniteHilbert.RelativeMapData.exists_iso_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusChoice.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusChoice.lean#L153). The attribute's comment: “the remark following the tag: the relative map does not depend on the data exhibiting it”.

> Two sets of data exhibiting the relative map of one object of `ℋ_d(𝒳/𝒴)` give the same
> morphism up to an isomorphism of its target.

```lean
theorem RelativeMapData.exists_iso_map {P : Object B S hS 𝒳 𝒴 F d}
    (D₁ D₂ : RelativeMapData P) :
    ∃ i : D₁.Xy ≅ D₂.Xy, D₁.map.hom ≫ i.hom = D₂.map.hom
```

## Tag 06CL, a lemma

[Tag 06CL](https://stacks.math.columbia.edu/tag/06CL) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isOpenImmersion_representing_lciFiniteHilbertInclusion_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusRepresentable.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusRepresentable.lean#L221). The attribute's comment: “the inclusion ℋ\_\{d,lci}(𝒳/𝒴) ⊂ ℋ\_d(𝒳/𝒴) is representable, by an open subscheme of the base”.

> The inclusion `ℋ_{d,lci}(𝒳/𝒴) ⟶ ℋ_d(𝒳/𝒴)` of the local complete intersection locus is
> representable: every 2-fibre product of it with a scheme-valued point of `ℋ_d(𝒳/𝒴)` is
> represented by an object of the big fppf site of the base which is an open subscheme of it, namely
> the open subscheme cut out by the locus. This is "representable" in the sense of Stacks 04ST, by a
> scheme. The forms in `LciLocusOpen.lean` that take the open locus and its isomorphism-invariance as
> arguments carry no registration.

```lean
theorem exists_isOpenImmersion_representing_lciFiniteHilbertInclusion_of_flat
    (hFrep : IsRepresentableByAlgebraicSpaces B S hS F)
    (hFflat : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.toBasedCategory.obj),
      y ⋙ 𝒴.toBasedCategory.p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.toBasedCategory.p 𝒴.toBasedCategory.p y
            F.toFunctor) (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsFlat B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom)
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
    ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤
        (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
          (d := d)).obj),
      y ⋙ (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
        (d := d)).p = Over.map U.hom →
      ∃ V : BigFppfOver B U.left.1 U.left.2, IsOpenImmersion V.hom.hom ∧
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (lciFiniteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
              (d := d)).p
            (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
              (d := d)).p y
            (lciFiniteHilbertInclusion (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
              (d := d)).toFunctor)
          (presheafOfCategories (yoneda.obj V ⋙ typeToCat)).p)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_lciFiniteHilbertInclusion_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusRepresentable.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusRepresentable.lean#L267). The attribute's comment: “the inclusion ℋ\_\{d,lci}(𝒳/𝒴) ⊂ ℋ\_d(𝒳/𝒴) is representable by algebraic spaces”.

> The inclusion `ℋ_{d,lci}(𝒳/𝒴) ⟶ ℋ_d(𝒳/𝒴)` of the local complete intersection locus is
> representable by algebraic spaces, the representing algebraic space of a base change being the
> open subscheme of the base cut out by the locus.

```lean
theorem isRepresentableByAlgebraicSpaces_lciFiniteHilbertInclusion_of_flat
    (hFrep : IsRepresentableByAlgebraicSpaces B S hS F)
    (hFflat : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.toBasedCategory.obj),
      y ⋙ 𝒴.toBasedCategory.p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.toBasedCategory.p 𝒴.toBasedCategory.p y
            F.toFunctor) (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsFlat B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom)
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
    IsRepresentableByAlgebraicSpaces B S hS
      (lciFiniteHilbertInclusion (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
        (d := d))
```

**`AlgebraicGeometry.Stack.isOpenImmersion_lciFiniteHilbertInclusion_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusRepresentable.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusRepresentable.lean#L302). The attribute's comment: “the inclusion ℋ\_\{d,lci}(𝒳/𝒴) ⊂ ℋ\_d(𝒳/𝒴) is an open immersion”.

> The inclusion `ℋ_{d,lci}(𝒳/𝒴) ⟶ ℋ_d(𝒳/𝒴)` of the local complete intersection locus is an
> open immersion: every algebraic space representing a base change of it along a scheme-valued
> point of `ℋ_d(𝒳/𝒴)` has open immersion structural morphism, read as a morphism of algebraic
> spaces over `S`. This is the condition of Stacks 04XB at `AlgebraicGeometry.Space.IsOpenImmersion`,
> written out.

```lean
theorem isOpenImmersion_lciFiniteHilbertInclusion_of_flat
    (hFrep : IsRepresentableByAlgebraicSpaces B S hS F)
    (hFflat : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.toBasedCategory.obj),
      y ⋙ 𝒴.toBasedCategory.p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.toBasedCategory.p 𝒴.toBasedCategory.p y
            F.toFunctor) (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsFlat B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom)
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
    ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤
        (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
          (d := d)).obj),
      y ⋙ (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
        (d := d)).p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (lciFiniteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
              (d := d)).p
            (finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
              (d := d)).p y
            (lciFiniteHilbertInclusion (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
              (d := d)).toFunctor)
          (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsOpenImmersion B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom
```

**`AlgebraicGeometry.Stack.isStackInGroupoids_lciFiniteHilbertCategory_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusStack.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusStack.lean#L72). The attribute's comment: “ℋ\_\{d,lci}(𝒳/𝒴) is a stack in groupoids”.

> **Stacks 06CL.** For a 1-morphism `F : 𝒳 ⟶ 𝒴` of stacks in groupoids over the big fppf site
> of `S` which is representable by algebraic spaces, flat and locally of finite presentation, the
> local complete intersection locus `ℋ_{d,lci}(𝒳/𝒴)` is a stack in groupoids over the big fppf site
> of `S`.
>
> The ambient `ℋ_d(𝒳/𝒴)` is a stack in groupoids by Stacks 05WB, and the locus is a full
> subcategory inherited along morphisms and local on the base by the open locus of Stacks 05X8 and
> 06CE, `AlgebraicGeometry.Stack.FiniteHilbert.hasOpenLciLocus`. The form
> `AlgebraicGeometry.Stack.isStackInGroupoids_lciFiniteHilbertCategory`, which takes these inputs as
> arguments, carries no registration.

```lean
theorem isStackInGroupoids_lciFiniteHilbertCategory_of_flat
    (hFrep : IsRepresentableByAlgebraicSpaces B S hS F)
    (hFflat : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.toBasedCategory.obj),
      y ⋙ 𝒴.toBasedCategory.p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.toBasedCategory.p 𝒴.toBasedCategory.p y
            F.toFunctor) (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsFlat B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom)
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
    (lciFiniteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)
      (d := d)).p.IsStackInGroupoids.{w}
      (BigFppfOver.topology B S hS)
```

## Tag 06D8, a lemma

[Tag 06D8](https://stacks.math.columbia.edu/tag/06D8) in the Stacks Project.

**`AlgebraicGeometry.Stack.FiniteHilbert.exists_coverDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/CoverDeformationExists.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/CoverDeformationExists.lean#L80).

> **Stacks 06D8.** Let `i : U ⟶ U'` be a first-order thickening of objects of the big fppf
> site of `S` with `U` affine, let `X'` be an algebraic space over `U'` flat over `U'`, let
> `q : Z ⟶ U` be finite locally free of degree `d`, and let `f : Z ⟶ X` be an unramified local
> complete intersection morphism into the special fibre `X = U ×_{U'} X'` (the restriction of
> `X'` along `U ⟶ U'`). Then there are `q' : Z' ⟶ U'` finite locally free of degree `d`, a
> cartesian square `hg` exhibiting `Z = U ×_{U'} Z'`, and `f' : Z' ⟶ X'` restricting to `f`.
>
> The source also assumes `U'` affine; that follows from `U` affine (Stacks 06AD) and is not
> used.

```lean
theorem exists_coverDeformation (d : ℕ) {U U' : BigFppfOver B S hS} (i : U ⟶ U')
    (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (hi : Stacks.Thickenings.IsFirstOrderThickening ((BigFppfOver.toScheme B S hS).map i))
    (X' : (BigFppfOver B U'.left.1 U'.left.2)ᵒᵖ ⥤ Type u)
    (hX' : IsAlgebraicSpace B U'.left.1 U'.left.2 X')
    (hflat : Space.IsFlat B U'.left.1 U'.left.2 (Space.toYonedaId B U'.left.1 U'.left.2 X'))
    {Z : BigFppfOver B S hS} (q : Z ⟶ U)
    (hq : Stacks.Morphisms.IsFiniteLocallyFreeOfRank ((BigFppfOver.toScheme B S hS).map q) d)
    (f : yoneda.obj (Over.mk q.left : BigFppfOver B U.left.1 U.left.2) ⟶
      (OverShriek.relocalizeRestrict i.left).obj X')
    (hunr : Space.IsUnramified B U.left.1 U.left.2 f)
    (hlci : Space.IsLocalCompleteIntersection B U.left.1 U.left.2 f) :
    ∃ (Z' : BigFppfOver B S hS) (q' : Z' ⟶ U') (g : Z ⟶ Z') (hg : IsPullback g q q' i),
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank ((BigFppfOver.toScheme B S hS).map q') d ∧
        ∃ f' : yoneda.obj (Over.mk q'.left : BigFppfOver B U'.left.1 U'.left.2) ⟶ X',
          OverShriek.restrictYonedaHom i.left (coverComparisonOfSquare hg.w) ≫
              (OverShriek.relocalizeRestrict i.left).map f' = f
```

## Tag 06D9, a lemma

[Tag 06D9](https://stacks.math.columbia.edu/tag/06D9) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFormallySmoothOnObjects_lciFiniteHilbertToTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciHilbertTargetFormallySmooth.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciHilbertTargetFormallySmooth.lean#L60).

> **Stacks 06D9.** Let `F : 𝒳 ⟶ 𝒴` be a 1-morphism of stacks in groupoids over
> `(Sch/S)_fppf` which is representable by algebraic spaces, flat and locally of finite
> presentation. Then `p : ℋ_{d,lci}(𝒳/𝒴) ⟶ 𝒴` is formally smooth on objects (Stacks 06D0).
>
> This is
> `AlgebraicGeometry.Stack.isFormallySmoothOnObjects_lciFiniteHilbertToTarget_of_coverDeformations`
> with its deformation problem solved by
> `AlgebraicGeometry.Stack.FiniteHilbert.hasCoverDeformations`, the space-level Stacks 06D8.

```lean
theorem isFormallySmoothOnObjects_lciFiniteHilbertToTarget
    (hFrep : IsRepresentableByAlgebraicSpaces B S hS F)
    (hFflat : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.toBasedCategory.obj),
      y ⋙ 𝒴.toBasedCategory.p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.toBasedCategory.p 𝒴.toBasedCategory.p y
            F.toFunctor) (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsFlat B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom)
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
    IsFormallySmoothOnObjects B S hS
      (lciFiniteHilbertFibered (isFiberedInGroupoids_lciFiniteHilbertCategory
        (FiniteHilbert.hasOpenLciLocus (d := d) hFrep hFflat hFlfp)))
      (stackFibered B S hS 𝒴)
      (lciFiniteHilbertToTargetFibered (isFiberedInGroupoids_lciFiniteHilbertCategory
        (FiniteHilbert.hasOpenLciLocus (d := d) hFrep hFflat hFlfp)))
```

## Tag 06DA, a lemma

[Tag 06DA](https://stacks.math.columbia.edu/tag/06DA) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSurjectiveOnObjects_lciFiniteHilbertCoproductToTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusSurjective.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/LciLocusSurjective.lean#L264). The attribute's comment: “∐\_\{d ≥ 1} ℋ\_\{d,lci}(𝒳/𝒴) ⟶ 𝒴 is surjective on objects, for F representable by algebraic spaces, flat, surjective and locally of finite presentation”.

> Let `F : 𝒳 ⟶ 𝒴` be a 1-morphism of stacks in groupoids over the big fppf site of `S` which is
> representable by algebraic spaces, flat, surjective and locally of finite presentation. Then the
> 1-morphism `∐_{d ≥ 1} ℋ_{d,lci}(𝒳/𝒴) ⟶ 𝒴` is surjective on objects.

```lean
theorem isSurjectiveOnObjects_lciFiniteHilbertCoproductToTarget
    (hFrep : IsRepresentableByAlgebraicSpaces B S hS F)
    (hFflat : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.toBasedCategory.obj),
      y ⋙ 𝒴.toBasedCategory.p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.toBasedCategory.p 𝒴.toBasedCategory.p y
            F.toFunctor) (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsFlat B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom)
    (hFsurj : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.toBasedCategory.obj),
      y ⋙ 𝒴.toBasedCategory.p = Over.map U.hom →
      ∀ (P : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hP : IsAlgebraicSpace B U.left.1 U.left.2 P),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.toBasedCategory.p 𝒴.toBasedCategory.p y
            F.toFunctor) (presheafOfCategories (P ⋙ typeToCat)).p) →
        Space.IsSurjective B S hS (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨P, hP⟩)).hom)
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
    IsSurjectiveOnObjects B S hS
      (lciFiniteHilbertCoproductProjection (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴)
        (F := F))
      𝒴.toBasedCategory.p
      (lciFiniteHilbertCoproductToTarget (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴)
        (F := F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.15, Tag 06CJ](https://stacks.math.columbia.edu/tag/06CJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
