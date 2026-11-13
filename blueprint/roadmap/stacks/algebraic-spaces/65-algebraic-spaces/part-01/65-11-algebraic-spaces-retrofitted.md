---
declaration: section
origin: cited
lean: AlgebraicGeometry.isAlgebraicSpace_of_surjective_etale_atlas, AlgebraicGeometry.isAlgebraicSpace_of_relativelyRepresentable_surjective_etale, AlgebraicGeometry.Space.isAlgebraicSpaceULift_of_relative_surjective_etale, AlgebraicGeometry.isAlgebraicSpace_of_relativelyRepresentable, AlgebraicGeometry.presheaf_inverseImage_iff_atlas_snd, AlgebraicGeometry.Space.isAlgebraicSpace_and_presheaf_of_surjectiveEtaleChart, AlgebraicGeometry.Space.exists_surjective_etale_chart_lift
statement: formalized
proof: formalized
---

# 65.11 Algebraic spaces, retrofitted

Section 65.11 of the Stacks Project, [Tag 02WX](https://stacks.math.columbia.edu/tag/02WX). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BGQ, a lemma

[Tag 0BGQ](https://stacks.math.columbia.edu/tag/0BGQ) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_of_surjective_etale_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleAtlasCriterionUnconditional.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleAtlasCriterionUnconditional.lean#L84).

> **Stacks 0BGQ.** A sheaf `F` on the big fppf site over `S` admitting a representable,
> surjective, étale morphism `f : h_U ⟶ F` from an object `U` of the site is an algebraic space
> over `S`.
>
> The kernel pair `R = U ×_F U` of `f` is an object of the site with étale projections forming an
> étale equivalence relation, so the quotient sheaf `U/R` is an algebraic space by Stacks 02WW;
> both `F` and `U/R` are the coequalizer of the two projections in fppf sheaves of sets, hence
> isomorphic.

```lean
theorem isAlgebraicSpace_of_surjective_etale_atlas
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ F)
    (hsurj : MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS)) f)
    (hetale : MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS)) f) :
    IsAlgebraicSpace B S hS F
```

## Tag 0BGR, a lemma

[Tag 0BGR](https://stacks.math.columbia.edu/tag/0BGR) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_of_relativelyRepresentable_surjective_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleAtlasCriterionUnconditional.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleAtlasCriterionUnconditional.lean#L102).

> **Stacks 0BGR.** A sheaf `F` on the big fppf site over `S` admitting a representable,
> surjective, étale morphism `a : G ⟶ F` from an algebraic space `G` over `S` is an algebraic space
> over `S`.
>
> A surjective étale atlas `h_U ⟶ G` of `G` by an object of the site is representable because `G`
> has representable diagonal, and composing it with `a` gives an atlas of the same kind for `F`.

```lean
theorem isAlgebraicSpace_of_relativelyRepresentable_surjective_etale
    {G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hG : IsAlgebraicSpace B S hS G)
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F) (a : G ⟶ F)
    (hs : MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS)) a)
    (he : MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS)) a) :
    IsAlgebraicSpace B S hS F
```

**`AlgebraicGeometry.Space.isAlgebraicSpaceULift_of_relative_surjective_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedEtaleAtlas.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedEtaleAtlas.lean#L96). The attribute's comment: “in an arbitrary value universe”.

> **Stacks 0BGR** for presheaves with values in a universe `max w u` independent of the
> universe `u` of the schemes. A sheaf `F` on the big fppf site of `S` admitting a morphism
> `a : G ⟶ F` from an algebraic space `G` over `S` which is representable by objects of the site,
> surjective and étale is an algebraic space over `S`.
>
> Both presheaves are pointwise `u`-small — the source because it is an algebraic space, the
> target because its sections lift along `a` after a surjective étale base change — so they are
> universe lifts of presheaves of `Type u` and the statement is the one in the value universe of
> the site transported along the lift.

```lean
theorem isAlgebraicSpaceULift_of_relative_surjective_etale
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (hG : IsAlgebraicSpaceULift.{w} B S hS G) (a : G ⟶ F)
    (hs : (surjectiveOnSite B S hS).relative (uliftYoneda.{w}) a)
    (he : (etaleOnSite B S hS).relative (uliftYoneda.{w}) a) :
    IsAlgebraicSpaceULift.{w} B S hS F
```

## Tag 02WY, a lemma

[Tag 02WY](https://stacks.math.columbia.edu/tag/02WY) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable.lean#L212).

> A representable transformation to an algebraic space over `S` has an
> algebraic space over `S` as its source.

```lean
theorem isAlgebraicSpace_of_relativelyRepresentable
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : G ⟶ F) (ha : yoneda.relativelyRepresentable a)
    (hF : IsAlgebraicSpace B S hS F) :
    IsAlgebraicSpace B S hS G
```

## Tag 02WZ, a lemma

[Tag 02WZ](https://stacks.math.columbia.edu/tag/02WZ) in the Stacks Project.

**`AlgebraicGeometry.presheaf_inverseImage_iff_atlas_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableAtlasTest.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableAtlasTest.lean#L75).

> **Stacks 02WZ.** A representable transformation of presheaves on the big fppf site of `S`
> has a base-change stable, fppf local relative property exactly when its base change along one
> surjective étale representable transformation to the target has it. The presheaves are
> arbitrary: no algebraic space condition on `F` or `G` enters the argument.

```lean
theorem presheaf_inverseImage_iff_atlas_snd
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty Scheme.{u})
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : G ⟶ F) (hf : yoneda.relativelyRepresentable f)
    (U : BigFppfOver B S hS) (q : yoneda.obj U ⟶ F)
    (hq_surj : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) q)
    (hq_etale : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) q) :
    (MorphismProperty.presheaf
      (P.inverseImage (BigFppfOver.toScheme B S hS))) f ↔
      P ((BigFppfOver.toScheme B S hS).map (hf.snd q))
```

## Tag 03I2, a lemma

[Tag 03I2](https://stacks.math.columbia.edu/tag/03I2) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_and_presheaf_of_surjectiveEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleDescentFromFppfDescent.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleDescentFromFppfDescent.lean#L411).

> **Stacks 03I2.** Let `S` be a scheme contained in a big fppf site and let `P` be a property
> of morphisms of schemes which is preserved by arbitrary base change, is fppf local on the base,
> and is such that morphisms with `P` satisfy descent for fppf coverings. Let `f : X ⟶ Y` be a
> morphism of presheaves on the big fppf site of `S` with `X` a sheaf and `Y` an algebraic space
> over `S`, and suppose some surjective étale chart `g : yoneda.obj U ⟶ Y` of `Y` makes the base
> change of `f` representable with `P`. Then `X` is an algebraic space over `S`, and `f` is
> representable and has `P`.
>
> The three conclusions of the source are the two conjuncts: the second,
> `(P.inverseImage _).presheaf f`, is representability of `f` together with `P` for every
> represented base change of it.

```lean
theorem isAlgebraicSpace_and_presheaf_of_surjectiveEtaleChart
    {P : MorphismProperty Scheme.{u}} [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    (hP : SatisfiesDescent.{u, 0} P Scheme.fppfPrecoverage)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : Presheaf.IsSheaf (BigFppfOver.topology B S hS) X)
    (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    {U : BigFppfOver B S hS} {g : yoneda.obj U ⟶ Y}
    (hs : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) g)
    (he : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) g)
    (hV : (P.inverseImage (BigFppfOver.toScheme B S hS)).presheaf (pullback.snd f g)) :
    IsAlgebraicSpace B S hS X ∧
      (P.inverseImage (BigFppfOver.toScheme B S hS)).presheaf f
```

## Tag 02X1, a lemma

[Tag 02X1](https://stacks.math.columbia.edu/tag/02X1) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_surjective_etale_chart_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocal.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocal.lean#L77).

> Let `a : F ⟶ G` be a morphism of presheaves on the big fppf site of `S` with `F` an
> algebraic space over `S`. Every surjective étale scheme chart `q : yoneda.obj V ⟶ G` is
> dominated by a surjective étale scheme chart of `F`: there are an object `U` of the site, a
> surjective étale chart `p : yoneda.obj U ⟶ F` and a morphism `α : U ⟶ V` making the square
> commute.

```lean
theorem exists_surjective_etale_chart_lift {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (a : F ⟶ G) (V : BigFppfOver B S hS)
    (q : yoneda.obj V ⟶ G)
    (hq_surjective : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf q)
    (hq_etale : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf q) :
    ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ F) (α : U ⟶ V),
      p ≫ a = yoneda.map α ≫ q ∧
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf p ∧
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.11, Tag 02WX](https://stacks.math.columbia.edu/tag/02WX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
