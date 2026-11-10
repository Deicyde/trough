---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.UniversallyOpen, AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_iff_isRepresentableByAlgebraicSpace_pt, AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_isRepresentableByAlgebraicSpace_pt, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isTwoFibreProduct, AlgebraicGeometry.Stack.hasRelativeProperty_iff_forall_space_baseChange, AlgebraicGeometry.Stack.hasRelativeProperty_iff_prop_representingMap_of_fppf, AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_fppfCover, AlgebraicGeometry.Stack.hasRelativeProperty_of_comp_of_cover
statement: formalized
proof: formalized
---

# 100.3 Properties of morphisms representable by algebraic spaces

Section 100.3 of the Stacks Project, [Tag 04XB](https://stacks.math.columbia.edu/tag/04XB). 8 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04XB, the section

[Tag 04XB](https://stacks.math.columbia.edu/tag/04XB) in the Stacks Project.

**`AlgebraicGeometry.Stack.UniversallyOpen`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyOpenCriterion.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyOpenCriterion.lean#L143). The attribute's comment: “RESTRICTED: the section's relative property at universal openness”.

> A 1-morphism of categories fibred in groupoids over the big fppf site of `S` which is
> representable by algebraic spaces *is universally open* when every algebraic space representing
> its base change along a scheme-valued point of the target has universally open structural
> morphism, read as a morphism of algebraic spaces over `S`. This is the notion of Stacks 04XB for
> `AlgebraicGeometry.Space.UniversallyOpen`, and it is the condition Stacks 06U1 part (1) names.
>
> It is *not* `AlgebraicGeometry.Stack.AlgebraicStacks.UniversallyOpen`, which is Stacks 06U2
> part (2) and tests openness of base changes on the topological spaces of points; the equivalence
> of the two is Stacks 06U1.

```lean
abbrev UniversallyOpen {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 04ZP, a lemma

[Tag 04ZP](https://stacks.math.columbia.edu/tag/04ZP) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_iff_isRepresentableByAlgebraicSpace_pt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableBySpacesOfFppfCover.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableBySpacesOfFppfCover.lean#L271).

> **Stacks 04ZP.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`, let `𝒲` be
> represented by an algebraic space `W` and let `g : 𝒲 ⟶ 𝒴` be surjective, flat and locally of
> finite presentation. Then `f` is representable by algebraic spaces if and only if the apex
> `W ×_𝒴 𝒳` of a 2-fibre product square over the cospan `(g, f)` is represented by an algebraic
> space.
>
> The implication (1) ⟹ (2) is Stacks 0300,
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isTwoFibreProduct`, which needs none
> of the hypotheses on `g`; the converse is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_isTwoFibreProduct_of_bootstrap`.

```lean
theorem isRepresentableByAlgebraicSpaces_iff_isRepresentableByAlgebraicSpace_pt
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS}
    (𝒲 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒲 : IsRepresentableByAlgebraicSpace B S hS 𝒲)
    (f : 𝒳 ⟶ 𝒴) (g : 𝒲 ⟶ 𝒴.val)
    (hg : ∀ (V : BigFppfOver B S hS)
      (yv : BigFppfOver B V.left.1 V.left.2 ⥤ 𝒴.val.val.obj)
      (_hyv : yv ⋙ 𝒴.val.val.p = Over.map V.hom)
      (F : (BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B V.left.1 V.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map V.hom) 𝒲.val.p 𝒴.val.val.p yv
          (CatFiberedInGroupoids.homFunctor g))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      (let h := (algebraicSpaceMap B S hS V
        ((spacesOverSmallerBaseFunctor B V.left.1 S V.left.2 hS V.hom).obj ⟨F, hF⟩)).hom
       Space.IsSurjective B S hS h ∧ Space.IsFlat B S hS h ∧
         Space.IsLocallyOfFinitePresentation B S hS h))
    (Q : Bicategory.TwoCommSq g f.hom) (hQ : Bicategory.IsTwoFibreProduct Q) :
    IsRepresentableByAlgebraicSpaces B S hS f.hom.hom ↔
      IsRepresentableByAlgebraicSpace B S hS Q.pt
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_isRepresentableByAlgebraicSpace_pt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableOfFlatCoverBaseChange.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableOfFlatCoverBaseChange.lean#L101). The attribute's comment: “the implication (2) ⟹ (1)”.

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`, let `g : 𝒲 ⟶ 𝒴` be
> surjective, flat and locally of finite presentation with `𝒲` an algebraic space, and suppose a
> 2-fibre product `𝒲 ×_𝒴 𝒳` of the cospan `(g, f)` is an algebraic space. Then `f` is
> representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_of_isRepresentableByAlgebraicSpace_pt
    {𝒳 𝒴 𝒲 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒲 ⟶ 𝒴)
    (h𝒲 : IsRepresentableByAlgebraicSpace B S hS 𝒲.val)
    (hSurj : IsSurjective B S hS g) (hFlat : AlgebraicStacks.IsFlat B S hS g)
    (hLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (Q : Bicategory.TwoCommSq g f) (hQ : Bicategory.IsTwoFibreProduct Q)
    (hQpt : IsRepresentableByAlgebraicSpace B S hS Q.pt.val) :
    IsRepresentableByAlgebraicSpaces B S hS f.hom.hom
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isTwoFibreProduct`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeRepresentableBySpace.lean#L172), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeRepresentableBySpace.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeRepresentableBySpace.lean#L186) (StacksFrontier): “the implication (1) ⟹ (2)”.

## Tag 04XC, a lemma

[Tag 04XC](https://stacks.math.columbia.edu/tag/04XC) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_iff_forall_space_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertySpaceBaseChange.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertySpaceBaseChange.lean#L265).

> **Stacks 04XC.** A 1-morphism of categories fibred in groupoids over the big fppf site of `S`
> which is representable by algebraic spaces has the relative property `P` exactly when, for every
> 2-fibre product square over a 1-morphism out of a stack representable by an algebraic space, the
> morphism of representing presheaves induced by the first projection of that square has `P` as a
> morphism of algebraic spaces over `S`.
>
> The chosen representing equivalences are universally quantified, so the condition does not depend
> on them; and algebraicity of `𝒳` and `𝒴` is not needed, only representability of `f` by algebraic
> spaces.

```lean
theorem hasRelativeProperty_iff_forall_space_baseChange :
    HasRelativeProperty B S hS P f hf ↔
      ∀ (𝒵 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
        (_h𝒵 : IsRepresentableByAlgebraicSpace B S hS 𝒵)
        (g : 𝒵 ⟶ 𝒴) (Q : Bicategory.TwoCommSq g f)
        (_hQ : Bicategory.IsTwoFibreProduct Q)
        (F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
        (eF : StacksRepresentableCFG.EquivalenceOver
          Q.pt.val.p (presheafOfCategories (F ⋙ typeToCat)).p)
        (eG : StacksRepresentableCFG.EquivalenceOver
          𝒵.val.p (presheafOfCategories (G ⋙ typeToCat)).p),
        P (ObjectProperty.homMk (representingMap B S hS Q.pt 𝒵 F G eF eG Q.fst) :
          (⟨F, hF⟩ : AlgebraicSpaces B S hS) ⟶ (⟨G, hG⟩ : AlgebraicSpaces B S hS))
```

## Tag 04XD, a lemma

[Tag 04XD](https://stacks.math.columbia.edu/tag/04XD) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_iff_prop_representingMap_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalEssentialSurjectivity.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalEssentialSurjectivity.lean#L493).

> **Properties of Stacks, Lemma 04XD.** In the situation above, `f` has the relative property
> `P` of Stacks 03YK exactly when the morphism `V ⟶ W` of representing presheaves induced by the
> first projection of the square has `P` as a morphism of algebraic spaces over `S`.
>
> The forward implication is Stacks 04XC and uses no hypothesis on `g`; the backward one is
> `AlgebraicGeometry.Stack.hasRelativeProperty_of_prop_representingMap_of_fppf`.

```lean
theorem hasRelativeProperty_iff_prop_representingMap_of_fppf
    (P : MorphismProperty (AlgebraicSpaces B S hS)) [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, max u t} B S hS)]
    (𝒳 𝒴 𝒲 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (f : 𝒳 ⟶ 𝒴) (g : 𝒲 ⟶ 𝒴) (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hgr : IsRepresentableByAlgebraicSpaces B S hS g.hom)
    (hg : ∀ (V : BigFppfOver B S hS)
      (yv : BigFppfOver B V.left.1 V.left.2 ⥤ 𝒴.val.obj)
      (_hyv : yv ⋙ 𝒴.val.p = Over.map V.hom)
      (F : (BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B V.left.1 V.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map V.hom) 𝒲.val.p 𝒴.val.p yv
          (CatFiberedInGroupoids.homFunctor g))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      (let h := (algebraicSpaceMap B S hS V
        ((spacesOverSmallerBaseFunctor B V.left.1 S V.left.2 hS V.hom).obj ⟨F, hF⟩)).hom
       Space.IsSurjective B S hS h ∧ Space.IsFlat B S hS h ∧
         Space.IsLocallyOfFinitePresentation B S hS h))
    (Q : Bicategory.TwoCommSq g f) (hQ : Bicategory.IsTwoFibreProduct Q)
    (V W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hV : IsAlgebraicSpace B S hS V) (hW : IsAlgebraicSpace B S hS W)
    (eV : StacksRepresentableCFG.EquivalenceOver
      Q.pt.val.p (presheafOfCategories (V ⋙ typeToCat)).p)
    (eW : StacksRepresentableCFG.EquivalenceOver
      𝒲.val.p (presheafOfCategories (W ⋙ typeToCat)).p) :
    HasRelativeProperty.{u, u, u + 1, max u t} B S hS P f hf ↔
      P (ObjectProperty.homMk (representingMap B S hS Q.pt 𝒲 V W eV eW Q.fst) :
        (⟨V, hV⟩ : AlgebraicSpaces B S hS) ⟶ (⟨W, hW⟩ : AlgebraicSpaces B S hS))
```

## Tag 06TY, a lemma

[Tag 06TY](https://stacks.math.columbia.edu/tag/06TY) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_fppfCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyFppfCover.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyFppfCover.lean#L102).

> Let `P` be a property of morphisms of algebraic spaces over `S` which is stable under base
> change and local on the target for the fppf precoverage, let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of
> algebraic stacks over `S` representable by algebraic spaces, and let `g : 𝒵 ⟶ 𝒴` be
> representable by algebraic spaces, surjective, flat and locally of finite presentation. Then `f`
> has the relative property `P` of Stacks 03YK if and only if the projection to `𝒵` of a 2-fibre
> product of the cospan `(g, f)` has it.

```lean
theorem hasRelativeProperty_iff_of_fppfCover
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, u} B S hS)]
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hg : IsRepresentableByAlgebraicSpaces B S hS g.hom.hom)
    (hSurj : IsSurjective B S hS g)
    (hFlat : AlgebraicStacks.IsFlat B S hS g)
    (hLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (Q : Bicategory.TwoCommSq g f)
    (hQ : Bicategory.IsTwoFibreProduct Q) :
    HasRelativeProperty B S hS P f.hom hf ↔
      ∃ hfst : IsRepresentableByAlgebraicSpaces B S hS Q.fst.hom.hom,
        HasRelativeProperty B S hS P Q.fst.hom hfst
```

## Tag 06M2, a lemma

[Tag 06M2](https://stacks.math.columbia.edu/tag/06M2) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_of_comp_of_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyCancelSourceLocal.lean, line 879](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyCancelSourceLocal.lean#L879).

> A relative property local on the source descends along a representable
> covering of the intermediate fibred category.

```lean
public theorem hasRelativeProperty_of_comp_of_cover
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicGeometry.AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (AlgebraicGeometry.Space.Topology.fppf.precoverage B S hS)]
    (τ : AlgebraicGeometry.Space.Topology)
    (hτ : τ = .etale ∨ τ = .smooth ∨ τ = .syntomic ∨ τ = .fppf)
    [P.IsLocalAtSource (τ.precoverage B S hS)]
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, v, u + 1, w}
      (AlgebraicGeometry.BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hg : AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces B S hS g.hom)
    (hcover :
      ∀ (U : AlgebraicGeometry.BigFppfOver B S hS)
        (y : AlgebraicGeometry.BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.based.obj)
        (_hy : y ⋙ 𝒴.based.p = Over.map U.hom)
        (F : (AlgebraicGeometry.BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : AlgebraicGeometry.IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.based.p 𝒴.based.p y
            (CatFiberedInGroupoids.homFunctor f))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        let a := AlgebraicGeometry.algebraicSpaceMap B S hS U
          ((AlgebraicGeometry.spacesOverSmallerBaseFunctor B U.left.1 S U.left.2
            hS U.hom).obj ⟨F, hF⟩)
        (AlgebraicGeometry.Space.IsSurjective B S hS a.hom ∧
          (match τ with
          | .etale => AlgebraicGeometry.Space.IsEtale B S hS a.hom
          | .smooth => AlgebraicGeometry.Space.IsSmooth B S hS a.hom
          | .syntomic => AlgebraicGeometry.Space.IsSyntomic B S hS a.hom
          | .fppf =>
              AlgebraicGeometry.Space.IsFlat B S hS a.hom ∧
                AlgebraicGeometry.Space.IsLocallyOfFinitePresentation B S hS a.hom
          | .fpqc => False)))
    (hcomp : AlgebraicGeometry.Stack.HasRelativeProperty B S hS P (f ≫ g)
      (AlgebraicGeometry.isRepresentableByAlgebraicSpaces_comp B S hS f g hf hg)) :
    AlgebraicGeometry.Stack.HasRelativeProperty B S hS P g hg
```

## Tag 04Y6, a lemma

[Tag 04Y6](https://stacks.math.columbia.edu/tag/04Y6) in the Stacks Project.

**`AlgebraicGeometry.Stack.GroupoidPresentation.pr`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeProjection.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeProjection.lean#L454). The attribute's comment: “assertion (3): the morphism of groupoids pr : (U', R', s', t', c') ⟶ (U, R, s, t, c)”.

> **Stacks 04Y6, assertion (3).** The morphism of groupoids in algebraic spaces
> `pr : (U', R', s', t', c') ⟶ (U, R, s, t, c)`: on objects the projection `U' = U ×_𝒳 𝒳' ⟶ U`, on
> arrows the map carrying `(u₁, x₁, ψ₁), (u₂, x₂, ψ₂), φ` to `(u₁, u₂, ψ₁ ≫ g(φ) ≫ ψ₂⁻¹)`. The
> identity clause is not a hypothesis of
> `AlgebraicGeometry.GroupoidInAlgebraicSpaces.Hom.mk'`, and the two clauses over the base are free,
> the base being final.

```lean
noncomputable def pr : GroupoidInAlgebraicSpaces.Hom
    (baseChangedPresentation P g h𝒳 h𝒳' eU' eR').groupoid P.groupoid
```

**`AlgebraicGeometry.Stack.GroupoidPresentation.quotientStackPr`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeProjection.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeProjection.lean#L475). The attribute's comment: “assertion (3): the induced morphism [pr] of quotient stacks”.

> **Stacks 04Y6, assertion (3).** The 1-morphism `[pr] : [U'/R'] ⟶ [U/R]` of quotient stacks
> induced by `pr` through Stacks 046Q.

```lean
noncomputable def quotientStackPr :
    BasedFunctor (quotientStack (baseChangedPresentation P g h𝒳 h𝒳' eU' eR').groupoid)
      (quotientStack P.groupoid)
```

**`AlgebraicGeometry.Stack.GroupoidPresentation.exists_baseChangedPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeRelation.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeRelation.lean#L164). The attribute's comment: “assertions (1) and (2): a groupoid of the form (U', R', s', t', c') and a presentation [U'/R'] -> X'; the 2-commutative square of assertions (3) and (4) is not claimed”.

> Let `g : 𝒳' ⟶ 𝒳` be a 1-morphism of algebraic stacks over `S` representable by algebraic
> spaces and let `[U/R] ⟶ 𝒳` be a presentation. Then there is a presentation `[U'/R'] ⟶ 𝒳'` whose
> presenting groupoid is of the form `(U', R', s', t', c')`: its object space represents
> `U' = U ×_𝒳 𝒳'` and its arrow space represents `R' = R ×_𝒳 𝒳'`, where `R` is the
> self-intersection `U ×_𝒳 U` of the atlas.

```lean
theorem exists_baseChangedPresentation
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (h𝒳' : IsAlgebraicStack.{u, w} B S hS 𝒳'.val)
    (hg : IsRepresentableByAlgebraicSpaces B S hS g.hom) :
    ∃ (P' : GroupoidPresentation B S hS 𝒳'.val),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (baseChangedAtlasSquare P g).pt.val.p
        (presheafOfCategories (P'.groupoid.objects.obj ⋙ typeToCat)).p) ∧
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (atlasRelationBaseChangeSquare P g).pt.val.p
        (presheafOfCategories (P'.groupoid.arrows.obj ⋙ typeToCat)).p)
```

**`AlgebraicGeometry.Stack.GroupoidPresentation.nonempty_bcSquareIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeSquare.lean, line 1060](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeSquare.lean#L1060). The attribute's comment: “assertion (4): the square [U'/R'] -> X' -> X and [U'/R'] -> [U/R] -> X 2-commutes”.

> **Stacks 04Y6, assertion (4).** The square
>
> ```
> [U'/R'] ---ε'---> 𝒳'
>    |               |
>   [pr]             g
>    v               v
>  [U/R] ----ε----> 𝒳
> ```
>
> 2-commutes: the presenting 1-morphism of the base-changed presentation followed by `g` is
> 2-isomorphic, over the big fppf site, to the morphism `[pr]` of quotient stacks induced by `pr`
> followed by the presenting 1-morphism of `P`.

```lean
theorem nonempty_bcSquareIso :
    Nonempty (BasedFunctor.comp
        (baseChangedPresentation P g h𝒳 h𝒳' eU' eR').basedFunctor g.hom ≅
      BasedFunctor.comp (quotientStackPr P g eU' eR' h𝒳 h𝒳') P.basedFunctor)
```

**`AlgebraicGeometry.Stack.GroupoidPresentation.exists_baseChangedPresentationSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeSquare.lean, line 1095](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresentationBaseChangeSquare.lean#L1095). The attribute's comment: “the whole statement: assertions (1), (2), (3) and (4) conjoined”.

> **Stacks 04Y6, the whole statement.** Let `g : 𝒳' ⟶ 𝒳` be a 1-morphism of algebraic stacks
> over `S` representable by algebraic spaces and let `[U/R] ⟶ 𝒳` be a presentation. Then there are a
> presentation `[U'/R'] ⟶ 𝒳'` of the form `(U', R', s', t', c')` — its object space representing
> `U' = U ×_𝒳 𝒳'` and its arrow space representing `R' = R ×_𝒳 𝒳'` — and a morphism of groupoids
> `pr : (U', R', s', t', c') ⟶ (U, R, s, t, c)` for which the square
>
> ```
> [U'/R'] ---ε'---> 𝒳'
>    |               |
>   [pr]             g
>    v               v
>  [U/R] ----ε----> 𝒳
> ```
>
> 2-commutes.
>
> The four assertions are
> `AlgebraicGeometry.Stack.GroupoidPresentation.exists_baseChangedPresentation`,
> `...pr`, `...quotientStackPr` and
> `AlgebraicGeometry.Stack.GroupoidPresentation.nonempty_bcSquareIso`; this is their conjunction.
> The 2-commutativity is a `Nonempty` of an isomorphism of 1-morphisms over the site, an
> isomorphism being data while a conjunct must be a proposition — and asserting that a square
> 2-commutes *is* asserting that such an isomorphism exists.

```lean
theorem exists_baseChangedPresentationSquare
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (h𝒳' : IsAlgebraicStack.{u, w} B S hS 𝒳'.val)
    (hg : IsRepresentableByAlgebraicSpaces B S hS g.hom) :
    ∃ P' : GroupoidPresentation B S hS 𝒳'.val,
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (baseChangedAtlasSquare P g).pt.val.p
        (presheafOfCategories (P'.groupoid.objects.obj ⋙ typeToCat)).p) ∧
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (atlasRelationBaseChangeSquare P g).pt.val.p
        (presheafOfCategories (P'.groupoid.arrows.obj ⋙ typeToCat)).p) ∧
      ∃ pr' : GroupoidInAlgebraicSpaces.Hom P'.groupoid P.groupoid,
        Nonempty (BasedFunctor.comp P'.basedFunctor g.hom ≅
          BasedFunctor.comp (quotientStackMap pr') P.basedFunctor)
```

**`CategoryTheory.CatFiberedInGroupoids.RepresentablePresentation.isTwoFibreProduct_relationBaseChangeSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentablePresentationBaseChange.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentablePresentationBaseChange.lean#L168). The attribute's comment: “R' = R ×_𝒳 𝒳' for the canonical squares; no hypothesis carried”.

> **Stacks 04Y6.** The canonical `R ×_{s, 𝒰} U'` is a base change of the relation `R` along
> `g`: pasted onto the square of `U' = 𝒰 ×_𝒳 𝒳'`, it is a 2-fibre product of the cospan
> `(s ≫ f, g)`. This is the `R' = R ×_𝒳 𝒳'` of the statement of the lemma.

```lean
noncomputable def isTwoFibreProduct_relationBaseChangeSquare :
    Bicategory.IsTwoFibreProduct
      ((atlasBaseChangeSquare f g).pasteFst (relationBaseChangeSquare f g))
```

**`CategoryTheory.CatFiberedInGroupoids.RepresentablePresentation.nonempty_iso_baseChangedRelationSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentablePresentationBaseChange.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentablePresentationBaseChange.lean#L180). The attribute's comment: “R ×_𝒳 𝒳' = U' ×_{𝒳'} U' for the canonical squares; nothing carried”.

> **Stacks 04Y6.** The displayed chain of the proof, for the canonical 2-fibre products:
> `R ×_𝒳 𝒳' = 𝒰 ×_𝒳 𝒰 ×_𝒳 𝒳' = (𝒰 ×_𝒳 𝒳') ×_{𝒳'} (𝒰 ×_𝒳 𝒳')`. The base change of the relation
> and the self-intersection of the base-changed atlas are isomorphic as 2-commutative squares over
> the triple product, hence compatibly with the projections `pr_R` and `s'`.

```lean
theorem nonempty_iso_baseChangedRelationSquare :
    Nonempty ((atlasBaseChangeSquare f g).baseChangedSelfIntersection
        (baseChangedRelationSquare f g) ≅
      (relationSquare f).paste (relationBaseChangeSquare f g))
```

## Tag 04ZQ, a remark

[Tag 04ZQ](https://stacks.math.columbia.edu/tag/04ZQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.SpacesOverStack`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean#L59). The attribute's comment: “the objects”.

> An object of the 2-category `Spaces/𝒴`: an algebraic stack over `S` together with a
> 1-morphism to `𝒴` which is representable by algebraic spaces.

```lean
structure SpacesOverStack
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒴 : AlgebraicStacks.{u, w} B S hS)
```

**`AlgebraicGeometry.Stack.SpacesOverStack.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean#L77). The attribute's comment: “the 1-morphisms”.

> A 1-morphism of `Spaces/𝒴`: a 1-morphism of the source stacks together with a 2-morphism
> from the structure morphism of the source to its composite with that of the target.

```lean
structure Hom (F G : SpacesOverStack B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.SpacesOverStack.Hom₂`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean#L86). The attribute's comment: “the 2-morphisms”.

> A 2-morphism of `Spaces/𝒴`: a 2-morphism of the underlying 1-morphisms of source stacks,
> compatible with the two comparison 2-morphisms.

```lean
structure Hom₂ {F G : SpacesOverStack B S hS 𝒴} (f g : Hom F G)
```

**`AlgebraicGeometry.Stack.SpacesOverStack.instCategoryStruct`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean#L148). The attribute's comment: “composition of 1-morphisms”.

> The 1-morphisms of `Spaces/𝒴`, with their identities and composition.

```lean
instance instCategoryStruct : CategoryStruct.{u + 1} (SpacesOverStack B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.SpacesOverStack.instHomCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean#L156). The attribute's comment: “the hom-categories”.

> The category of 1-morphisms and 2-morphisms of `Spaces/𝒴` between two fixed objects: the
> hom-category of its 2-category structure.

```lean
instance instHomCategory (F G : SpacesOverStack B S hS 𝒴) : Category.{u + 1} (F ⟶ G)
```

**`AlgebraicGeometry.Stack.SpacesOverStack.instBicategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStack.lean#L229). The attribute's comment: “the 2-category structure”.

> The 2-category `Spaces/𝒴` of algebraic spaces over the algebraic stack `𝒴`, with the
> objects `SpacesOverStack`, the 1-morphisms `Hom` and the 2-morphisms `Hom₂`.

```lean
instance instBicategory : Bicategory.{u + 1, u + 1} (SpacesOverStack B S hS 𝒴)
```

**`AlgebraicGeometry.Stack.SpacesOverStack.isSetoidCategory_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStackSetoid.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStackSetoid.lean#L136). The attribute's comment: “the hom-categories are setoids”.

> **Stacks 04ZQ.** Every hom-category of `Spaces/𝒴` is a setoid in the sense of Stacks 02XZ:
> it is a groupoid and it is thin, so a 1-morphism of `Spaces/𝒴` has no automorphism but the
> identity. This is the source's claim that the morphism categories
> `Mor_{Spaces/𝒴}((f₁ : 𝒳₁ ⟶ 𝒴), (f₂ : 𝒳₂ ⟶ 𝒴))` are all setoids.

```lean
theorem isSetoidCategory_hom (F G : SpacesOverStack B S hS 𝒴) :
    IsSetoidCategory (F ⟶ G)
```

**`AlgebraicGeometry.Stack.SpacesOverStack.isoClassCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStackSetoid.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SpacesOverAlgebraicStackSetoid.lean#L155). The attribute's comment: “the category of isomorphism classes of 1-morphisms”.

> **Stacks 04ZQ.** Replacing the 1-morphisms of `Spaces/𝒴` by their isomorphism classes gives a
> category: the objects are those of `Spaces/𝒴`, a morphism `F ⟶ G` is an isomorphism class of
> 1-morphisms `F ⟶ G` of the 2-category, and the identities and the composition are induced by
> those of the 2-category.
>
> Composition descends because whiskering turns a pair of isomorphic 1-morphisms into isomorphic
> composites, and the three category laws hold because the unitors and the associator of
> `Spaces/𝒴` become equalities of isomorphism classes.

```lean
def isoClassCategory : Category.{u + 1} (SpacesOverStack B S hS 𝒴)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.3, Tag 04XB](https://stacks.math.columbia.edu/tag/04XB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
