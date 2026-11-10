---
declaration: section
origin: cited
lean: AlgebraicGeometry.isAlgebraicSpace_extend, AlgebraicGeometry.isIso_relocalizeOfRestricted, AlgebraicGeometry.Space.extend_representable, AlgebraicGeometry.Space.restrict_representable, AlgebraicGeometry.Space.restrict_eval, AlgebraicGeometry.Space.exists_extended_presentation, AlgebraicGeometry.baseChangePresentation, CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj
statement: formalized
proof: formalized
---

# 65.16 Change of base scheme

Section 65.16 of the Stacks Project, [Tag 03I3](https://stacks.math.columbia.edu/tag/03I3). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03I4, a lemma

[Tag 03I4](https://stacks.math.columbia.edu/tag/03I4) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_extend`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Extension.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Extension.lean#L559). The attribute's comment: “extension_algebraic_space”.

> **Stacks 03I4 (3).** Extension along a morphism `g : S ⟶ S'` of a big fppf site carries
> algebraic spaces over `S` to algebraic spaces over `S'`.

```lean
theorem isAlgebraicSpace_extend
    (B : BigFppfSite.{u}) (S S' : B.Schemes) (g : S ⟶ S')
    {L : Sheaf (B.topology.over S) (Type u) ⥤
      Sheaf (B.topology.over S') (Type u)}
    (adj : L ⊣ (Over.map g).sheafPushforwardContinuous (Type u)
      (B.topology.over S) (B.topology.over S'))
    (F : (BigFppfOver B (B.inclusion.obj S) S.property)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B (B.inclusion.obj S) S.property F) :
    IsAlgebraicSpace B (B.inclusion.obj S') S'.property
      (L.obj (⟨F, hF.isSheaf⟩ : Sheaf (B.topology.over S) (Type u))).obj
```

**`AlgebraicGeometry.isIso_relocalizeOfRestricted`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ExtensionEvaluation.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ExtensionEvaluation.lean#L109). The attribute's comment: “extension_evaluation”.

> **Stacks 03I4 (1).** For a morphism `g : S ⟶ S'` of a big fppf site and a sheaf `F` on the big
> fppf site of `S`, the canonical map from the presheaf of pairs of a factorization `T' → S → S'` and
> a section of `F` over it to the extension `j_!F` is an isomorphism.

```lean
theorem isIso_relocalizeOfRestricted
    (B : BigFppfSite.{u}) (S S' : B.Schemes) (g : S ⟶ S')
    {L : Sheaf (B.topology.over S) (Type u) ⥤
      Sheaf (B.topology.over S') (Type u)}
    (adj : L ⊣ (Over.map g).sheafPushforwardContinuous (Type u)
      (B.topology.over S) (B.topology.over S'))
    (F : Sheaf (B.topology.over S) (Type u)) :
    IsIso (OverShriek.relocalizeOfRestricted g (adj.unit.app F).hom)
```

**`AlgebraicGeometry.Space.extend_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean#L118). The attribute's comment: “extension_representable”.

> **Stacks 03I4.** Extension along `g : S ⟶ S'` carries a sheaf represented by `X / S` to
> one represented by `X / S'`.

```lean
theorem extend_representable
    (B : BigFppfSite.{u}) (S S' : B.Schemes) (g : S ⟶ S')
    {L : Sheaf (B.topology.over S) (Type u) ⥤ Sheaf (B.topology.over S') (Type u)}
    (adj : L ⊣ (Over.map g).sheafPushforwardContinuous (Type u)
      (B.topology.over S) (B.topology.over S'))
    (X : Over S) (F : Sheaf (B.topology.over S) (Type u))
    (hF : Nonempty (F.obj ≅ yoneda.obj X)) :
    Nonempty (((L.obj F).obj) ≅ yoneda.obj ((Over.map g).obj X))
```

**`AlgebraicGeometry.Space.restrict_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean#L173). The attribute's comment: “restriction_representable”.

> **Stacks 03I4.** Restricting a sheaf represented by `X' / S'` along `g : S ⟶ S'` gives a
> sheaf represented by the fibre product `S ×_{S'} X' / S`.

```lean
theorem restrict_representable
    (B : BigFppfSite.{u}) (S S' : Scheme.{u})
    (hS : B.Contains S) (hS' : B.Contains S')
    (g : B.obj hS ⟶ B.obj hS')
    (X' : BigFppfOver B S' hS')
    (F' : Sheaf (BigFppfOver.topology B S' hS') (Type u))
    (hF' : Nonempty (F'.obj ≅ yoneda.obj X')) :
    ∃ (Xbase : BigFppfOver B S hS)
      (p : Xbase.left ⟶ X'.left),
        IsPullback (B.inclusion.map p) (B.inclusion.map Xbase.hom)
          (B.inclusion.map X'.hom) (B.inclusion.map g) ∧
          Nonempty
            (((((Over.map g).sheafPushforwardContinuous (Type u)
              (B.topology.over (B.obj hS)) (B.topology.over (B.obj hS'))).obj F').obj) ≅
                yoneda.obj Xbase)
```

**`AlgebraicGeometry.Space.restrict_eval`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean#L210). The attribute's comment: “restriction_evaluation”.

> **Stacks 03I4, part (4): evaluation of a restricted sheaf.** Let `g : S ⟶ S'` be a morphism of
> a big fppf site, let `j = Over.map g` be the associated localization functor and let `F'` be a
> sheaf on the big fppf site over `S'`. For an object `T / S`, the sections of `j^{-1}F'` over
> `T / S` are the sections of `F'` over `T / S'`, that is over `T` with structure morphism the
> composite `T ⟶ S ⟶ S'`.
>
> Restriction along a continuous functor is precomposition, so this is the instance of
> `CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj` for `j`; it is recorded here to
> state the clause for the big fppf site, with `T / S'` written as the composite structure
> morphism.

```lean
theorem restrict_eval
    (B : BigFppfSite.{u}) (S S' : Scheme.{u})
    (hS : B.Contains S) (hS' : B.Contains S')
    (g : B.obj hS ⟶ B.obj hS')
    (F' : Sheaf (BigFppfOver.topology B S' hS') (Type u))
    (T : BigFppfOver B S hS) :
    (((Over.map g).sheafPushforwardContinuous (Type u)
        (B.topology.over (B.obj hS)) (B.topology.over (B.obj hS'))).obj F').obj.obj
          (Opposite.op T) = F'.obj.obj (Opposite.op (Over.mk (T.hom ≫ g)))
```

**`AlgebraicGeometry.Space.exists_extended_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean#L517). The attribute's comment: “extension_algebraic_space”.

> **Stacks 03I4, part (3): the extension of a presentation.** A chosen étale presentation `U / R`
> of an algebraic space `F` over `S` extends along `g : S ⟶ S'` to a presentation of `L F` by the
> images `j U` and `j R` of `U` and `R`, where `j = Over.map g`.
>
> The data produced is the identification `α : L h_U ≅ h_{j U}` of the extension of the representable
> `h_U`, and the extended atlas `f : h_{j U} ⟶ L F`, which is `L` of the original atlas read through
> `α`.  Its kernel pair is the pair of images `j` of the two projections of `R`; those two make `j R`
> an étale equivalence relation on `j U` over `S'`; `f` is surjective and étale after every
> representable base change; and `f` exhibits `L F` as the coequalizer of its kernel pair in sheaves
> over `S'`.
>
> The quotient is specified by this universal property rather than by a sheafification, so that no
> smallness hypothesis on sheafification is needed on either slice.

```lean
theorem exists_extended_presentation
    (B : BigFppfSite.{u}) (S S' : B.Schemes) (g : S ⟶ S')
    {L : Sheaf (B.topology.over S) (Type u) ⥤ Sheaf (B.topology.over S') (Type u)}
    (adj : L ⊣ (Over.map g).sheafPushforwardContinuous (Type u)
      (B.topology.over S) (B.topology.over S'))
    (F : (BigFppfOver B (B.inclusion.obj S) S.property)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B (B.inclusion.obj S) S.property F)
    (P : Presentation B (B.inclusion.obj S) S.property F hF) :
    let J := B.topology.over S
    let J' := BigFppfOver.topology B (B.inclusion.obj S') S'.property
    let FF : Sheaf J (Type u) := ⟨F, hF.isSheaf⟩
    let G := (L.obj FF).obj
    let target := (Over.map g).map P.target
    let source := (Over.map g).map P.source
    ∃ (hU : Presheaf.IsSheaf J (yoneda.obj P.U))
      (hU' : Presheaf.IsSheaf J' (yoneda.obj ((Over.map g).obj P.U)))
      (hR' : Presheaf.IsSheaf J' (yoneda.obj ((Over.map g).obj P.R)))
      (α : (L.obj (⟨yoneda.obj P.U, hU⟩ : Sheaf J (Type u))).obj ≅
        yoneda.obj ((Over.map g).obj P.U))
      (f : yoneda.obj ((Over.map g).obj P.U) ⟶ G)
      (hpb : IsPullback (yoneda.map target) (yoneda.map source) f f),
      let UF : Sheaf J' (Type u) := ⟨yoneda.obj ((Over.map g).obj P.U), hU'⟩
      let RF : Sheaf J' (Type u) := ⟨yoneda.obj ((Over.map g).obj P.R), hR'⟩
      let tf : RF ⟶ UF := ⟨yoneda.map target⟩
      let sf : RF ⟶ UF := ⟨yoneda.map source⟩
      let ff : UF ⟶ L.obj FF := ⟨f⟩
      let w : tf ≫ ff = sf ≫ ff := Sheaf.hom_ext hpb.w
      Stacks.Groupoids.IsEtaleEquivalenceRelation
        (prod.lift ((Over.post B.inclusion).map target)
          ((Over.post B.inclusion).map source)) ∧
      f = α.inv ≫ (L.map (⟨P.toSpace⟩ :
        (⟨yoneda.obj P.U, hU⟩ : Sheaf J (Type u)) ⟶ FF)).hom ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B (B.inclusion.obj S') S'.property))) f ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B (B.inclusion.obj S') S'.property))) f ∧
      Nonempty (IsColimit (Cofork.ofπ ff w))
```

**`AlgebraicGeometry.baseChangePresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RestrictSmallerBase.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RestrictSmallerBase.lean#L467). The attribute's comment: “part (6): restriction of a presentation”.

> **Stacks 03I4, part (6).** The restriction along `g : S ⟶ S'` of a presentation `U'/R'` of an
> algebraic space `F'` over `S'` is again a presentation, of the restriction `j⁻¹F' = F'|_S`: the
> presenting scheme and its relation are the base changes `U'_S = (Over.pullback g).obj U'` and
> `R'_S = (Over.pullback g).obj R'` along `g`, with projections the images under `Over.pullback g`
> of the original ones, and atlas the restriction of the original atlas read through
> `CategoryTheory.OverShriek.restrictYonedaIso`.

```lean
noncomputable def baseChangePresentation
    {F' : (BigFppfOver B S' hS')ᵒᵖ ⥤ Type w} {hF' : IsAlgebraicSpace B S' hS' F'}
    (P' : Space.Presentation B S' hS' F' hF') :
    Space.Presentation B S hS ((OverShriek.relocalizeRestrict g).obj F')
      (isAlgebraicSpace_relocalizeRestrict B S S' hS hS' g F' hF')
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/ChangeOfBaseScheme.lean#L682) (StacksFrontier): “restriction_evaluation”.
- [`isAlgebraicSpace_relocalizeRestrict`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isAlgebraicSpace_relocalizeRestrict#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/RestrictSmallerBase.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RestrictSmallerBase.lean#L457) (StacksFrontier): “restriction_algebraic_space, algebraicity”.

## Tag 03I5, a definition

[Tag 03I5](https://stacks.math.columbia.edu/tag/03I5) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_relocalizeRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RestrictSmallerBase.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RestrictSmallerBase.lean#L421). The attribute's comment: “part (1), algebraicity”.

> **Stacks 03I5, part (1), algebraicity.** The restriction of an algebraic space over `S'` along
> a morphism `g : S ⟶ S'` of a big fppf site is an algebraic space over `S`.

```lean
theorem isAlgebraicSpace_relocalizeRestrict
    (F' : (BigFppfOver B S' hS')ᵒᵖ ⥤ Type w) (hF' : IsAlgebraicSpace B S' hS' F') :
    IsAlgebraicSpace B S hS ((OverShriek.relocalizeRestrict g).obj F')
```

**`AlgebraicGeometry.isAlgebraicSpace_viewOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallerBase.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallerBase.lean#L161). The attribute's comment: “part (2), algebraicity”.

> **Stacks 03I5, part (2), algebraicity.** An algebraic space over `S`, viewed over `S'` along
> the lower-shriek extension of a morphism `g : S ⟶ S'` of the site, is an algebraic space over
> `S'`.
>
> This is Stacks 03I4 part (3) (`AlgebraicGeometry.isAlgebraicSpace_extend`) for the left adjoint
> `AlgebraicGeometry.relocalizeSheafFunctor`, whose value on a sheaf is the presheaf-level extension
> itself.

```lean
theorem isAlgebraicSpace_viewOver
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    IsAlgebraicSpace B S' hS' ((OverShriek.relocalizePresheafFunctor g).obj F)
```

Declarations registered for the tag:

- [`CategoryTheory.OverShriek.relocalizeRestrict`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/Relocalize.lean#L110), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L126) (StacksFrontier): “part (1), base-change construction”.
- [`CategoryTheory.OverShriek.relocalizePresheafFunctor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/Relocalize.lean#L106), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L128) (StacksFrontier): “part (2), lower-shriek construction”.

## Tag 04SG, a lemma

[Tag 04SG](https://stacks.math.columbia.edu/tag/04SG) in the Stacks Project.

**`AlgebraicGeometry.SpacesOverSmallerBase`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Category.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L283). The attribute's comment: “the category of algebraic spaces with a morphism to the smaller base”.

> **Stacks 04SG.** For a morphism `g : S ⟶ S'` of a big fppf site, the category of
> algebraic spaces over `S'` endowed with a morphism to the representable algebraic space of
> `S`.

```lean
abbrev SpacesOverSmallerBase (B : BigFppfSite.{u}) (S S' : Scheme.{u})
    (hS : B.Contains S) (hS' : B.Contains S') (g : B.obj hS ⟶ B.obj hS')
```

**`AlgebraicGeometry.spacesOverSmallerBaseFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallerBase.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallerBase.lean#L208). The attribute's comment: “the forward functor of the equivalence”.

> **Stacks 04SG, the forward functor.** An algebraic space over `S` is an algebraic space over
> `S'` with a morphism to the representable algebraic space of `S`: the lower-shriek extension, read
> in the slice over that representable presheaf.
>
> The structural morphism of the image of `F` sends a section indexed by `ψ : T ⟶ S` to `ψ`; this is
> the functor every relative-property statement of Chapters 100 and 101 is written with.

```lean
noncomputable def spacesOverSmallerBaseFunctor :
    AlgebraicSpaces B S hS ⥤ SpacesOverSmallerBase B S S' hS hS' g
```

**`AlgebraicGeometry.spacesOverSmallerBaseFunctorForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallerBase.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallerBase.lean#L222). The attribute's comment: “the forward functor is the lower-shriek extension”.

> **Stacks 04SG, the forward functor is the lower-shriek extension.** Forgetting the structural
> morphism to the representable algebraic space of `S` turns
> `AlgebraicGeometry.spacesOverSmallerBaseFunctor` into the lower-shriek extension of Stacks 03I5
> part (2).

```lean
noncomputable def spacesOverSmallerBaseFunctorForgetIso :
    (spacesOverSmallerBaseFunctor B S S' hS hS' g ⋙
        ObjectProperty.ι (fun X : Over (yoneda.obj (Over.mk g) :
          (BigFppfOver B S' hS')ᵒᵖ ⥤ Type u) => IsAlgebraicSpace B S' hS' X.left) ⋙
        Over.forget (yoneda.obj (Over.mk g))) ≅
      (ObjectProperty.ι (fun F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u =>
          IsAlgebraicSpace B S hS F) ⋙ OverShriek.relocalizePresheafFunctor g)
```

**`AlgebraicGeometry.spacesOverSmallerBaseEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallerBaseEquivalence.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallerBaseEquivalence.lean#L82). The attribute's comment: “the equivalence”.

> The category of algebraic spaces over `S` is equivalent to the category of algebraic spaces
> over `S'` equipped with a morphism to the representable algebraic space of `S`, the equivalence
> being the lower-shriek extension along `g : S ⟶ S'`.

```lean
noncomputable def spacesOverSmallerBaseEquivalence :
    AlgebraicSpaces B S hS ≌ SpacesOverSmallerBase B S S' hS hS' g
```

## Tag 04SH, a lemma

[Tag 04SH](https://stacks.math.columbia.edu/tag/04SH) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_restrict_iff_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallerBaseProduct.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallerBaseProduct.lean#L55).

> **Stacks 04SH.** The restriction of a presheaf `F'` on the big fppf site of `S'` to the big
> fppf site of `S` along `f : S ⟶ S'` is an algebraic space over `S` exactly when the product of
> `F'` with the representable presheaf of the object `S →f S'` is an algebraic space over `S'`.

```lean
theorem isAlgebraicSpace_restrict_iff_product
    (B : BigFppfSite.{u}) (S S' : Scheme.{u}) (hS : B.Contains S) (hS' : B.Contains S')
    (f : B.obj hS ⟶ B.obj hS') (F' : (BigFppfOver B S' hS')ᵒᵖ ⥤ Type u) :
    IsAlgebraicSpace B S hS ((OverShriek.relocalizeRestrict f).obj F') ↔
      IsAlgebraicSpace B S' hS' (yoneda.obj (Over.mk f) ⨯ F')
```

## Tag 03I6, a lemma

[Tag 03I6](https://stacks.math.columbia.edu/tag/03I6) in the Stacks Project.

**`AlgebraicGeometry.presheaf_property_map_base_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallerBaseProperties.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallerBaseProperties.lean#L61).

> **Stacks 03I6.** Let `g : S ⟶ S'` be a morphism of a big fppf site and let `P` be a property
> of morphisms of schemes stable under base change. For an algebraic space `F` over `S` and a
> morphism `f : h_T ⟶ F` from the representable algebraic space of an object `T` of the big fppf
> site of `S`, the morphism `P`-property of representable base changes holds for the image of `f`
> under the forward functor of Stacks 04SG exactly when it holds for `f`.

```lean
theorem presheaf_property_map_base_iff
    (B : BigFppfSite.{u}) (S S' : Scheme.{u}) (hS : B.Contains S) (hS' : B.Contains S')
    (g : B.obj hS ⟶ B.obj hS') (P : MorphismProperty Scheme.{u}) [P.IsStableUnderBaseChange]
    (T : BigFppfOver B S hS) (F : AlgebraicSpaces B S hS) (f : yoneda.obj T ⟶ F.obj) :
    MorphismProperty.presheaf (P.inverseImage (BigFppfOver.toScheme B S' hS'))
        ((spacesOverSmallerBaseFunctor B S S' hS hS' g).map
          (ObjectProperty.homMk f :
            (schemeSpace T : AlgebraicSpaces B S hS) ⟶
              F)).hom.left ↔
      MorphismProperty.presheaf (P.inverseImage (BigFppfOver.toScheme B S hS)) f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.16, Tag 03I3](https://stacks.math.columbia.edu/tag/03I3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
