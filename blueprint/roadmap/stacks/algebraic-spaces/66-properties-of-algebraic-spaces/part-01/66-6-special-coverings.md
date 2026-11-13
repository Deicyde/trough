---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsAlgebraicSpace.exists_etale_surjective_coproduct_affine_cover, AlgebraicGeometry.IsAlgebraicSpace.exists_etale_surjective_isSeparated_cover, AlgebraicGeometry.Space.exists_etale_surjective_coproduct_affine_cover, AlgebraicGeometry.Space.exists_zariski_cover_affine_etale_atlas, AlgebraicGeometry.Space.exists_zariskiCovering_affine_etale_chart, AlgebraicGeometry.Space.exists_affine_chart_of_isQuasiCompactSpaceULift, AlgebraicGeometry.Space.isQuasiCompactSpace_iff_exists_affine_etale_surjective_cover, AlgebraicGeometry.Space.isSeparated_of_isEtale_of_scheme_isSeparated
statement: formalized
proof: formalized
---

# 66.6 Special coverings

Section 66.6 of the Stacks Project, [Tag 03FW](https://stacks.math.columbia.edu/tag/03FW). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03FX, a lemma

[Tag 03FX](https://stacks.math.columbia.edu/tag/03FX) in the Stacks Project.

**`AlgebraicGeometry.IsAlgebraicSpace.exists_etale_surjective_coproduct_affine_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineAtlas.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineAtlas.lean#L216).

> An algebraic space over `S` has a surjective étale chart whose source is a disjoint union
> of affine schemes, each mapping into an affine open of `S`.

```lean
theorem IsAlgebraicSpace.exists_etale_surjective_coproduct_affine_cover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    ∃ (U : BigFppfOver B S hS)
      (f : yoneda.obj U ⟶ F)
      (I : Type u) (Y : I → Scheme.{u})
      (e : (∐ Y) ≅ (BigFppfOver.toScheme B S hS).obj U),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f ∧
      (∀ i, IsAffine (Y i)) ∧
      (∀ i, ∃ (V : S.Opens), IsAffineOpen V ∧
        ∀ y : Y i,
          (Sigma.ι Y i ≫ e.hom ≫ B.inclusion.map U.hom) y ∈ V)
```

**`AlgebraicGeometry.IsAlgebraicSpace.exists_etale_surjective_isSeparated_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineAtlas.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineAtlas.lean#L242). The attribute's comment: “the cover may be taken separated”.

> An algebraic space over `S` has a surjective étale chart whose underlying scheme is
> separated.

```lean
theorem IsAlgebraicSpace.exists_etale_surjective_isSeparated_cover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    ∃ (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ F),
      Scheme.IsSeparated ((BigFppfOver.toScheme B S hS).obj U) ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f
```

**`AlgebraicGeometry.Space.exists_etale_surjective_coproduct_affine_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/SpecialCoverings.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/SpecialCoverings.lean#L85).

> An algebraic space has a surjective étale atlas which is a disjoint union of affine schemes,
> each mapping into an affine open of the base.

```lean
theorem exists_etale_surjective_coproduct_affine_cover
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    ∃ (U : BigFppfOver B S hS)
      (f : yoneda.obj U ⟶ F)
      (I : Type u) (Y : I → Scheme.{u})
      (e : (∐ Y) ≅ (BigFppfOver.toScheme B S hS).obj U),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f ∧
      (∀ i, IsAffine (Y i)) ∧
      (∀ i, ∃ (V : S.Opens), IsAffineOpen V ∧
        ∀ y : Y i,
          (Sigma.ι Y i ≫ e.hom ≫ B.inclusion.map U.hom) y ∈ V)
```

## Tag 03FY, a lemma

[Tag 03FY](https://stacks.math.columbia.edu/tag/03FY) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_zariski_cover_affine_etale_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoverAffineAtlas.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoverAffineAtlas.lean#L45).

> **Stacks 03FY.** An algebraic space over `S` has a Zariski covering by open subspaces,
> each of which admits a surjective étale atlas from an affine scheme and maps into an affine
> open of `S`.

```lean
theorem exists_zariski_cover_affine_etale_atlas
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    ∃ (I : Type u) (X : I → Subfunctor F),
      IsZariskiCover B S hS I X ∧
      ∀ i, ∃ (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ (X i).toFunctor) (V : S.Opens),
        IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧
        (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f ∧
        (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f ∧
        IsAffineOpen V ∧
        ∀ (T : BigFppfOver B S hS) (_ : (X i).toFunctor.obj (Opposite.op T))
          (t : (BigFppfOver.toScheme B S hS).obj T), (B.inclusion.map T.hom) t ∈ V
```

**`AlgebraicGeometry.Space.exists_zariskiCovering_affine_etale_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringAffineCharts.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringAffineCharts.lean#L219). The attribute's comment: “covering on point sets”.

> **Stacks 03FY.** An algebraic space over `S` is the union of a family of open subspaces
> each of which carries a surjective étale chart from a single affine scheme, and those affine
> schemes may be taken to map into affine opens of `S`. Surjectivity of the chart is recorded
> both on point sets (Tag 03ME) and in the relatively representable form, the two being
> equivalent by Tag 03H5.
>
> The family is indexed by the summands of the affine chart of Stacks 03FX in the form
> `AlgebraicGeometry.IsAlgebraicSpace.exists_affine_coproduct_atlas`, which keeps the summands
> as affine objects `W i` of the site. The member of the covering attached to `i` is the open
> subspace swept out by `W i`, and the chart of that member is the factorisation of
> `yoneda.map (j i) ≫ f` through it, by
> `AlgebraicGeometry.Space.isOpenSubspace_etale_surjective_lift_openSubspaceOfPoints_range`.
> The members cover because the chart `f` is surjective on points (Tag 03H5) and every point of
> its source lies in one summand.
>
> The attribute carries a part string rather than being bare because the covering clause is the
> point-set one; the bare attribute sits on
> `AlgebraicGeometry.Space.exists_zariski_cover_affine_etale_atlas`, which states the same
> thing with the covering clause in the repository's `AlgebraicGeometry.Space.IsZariskiCover`
> vocabulary of Tag 02YY. The two are interchangeable by the Zariski-coverings part of Tag
> 03BZ.

```lean
theorem exists_zariskiCovering_affine_etale_chart
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    ∃ (I : Type u) (X : I → Subfunctor F) (W : I → BigFppfOver B S hS)
      (b : ∀ i, yoneda.obj (W i) ⟶ (X i).toFunctor),
      (∀ i, IsOpenSubspace B S hS (X i)) ∧
      (⋃ i, Set.range (pointsMap B S hS (X i).toFunctor (X i).ι)) = Set.univ ∧
      (∀ i, IsAffine ((BigFppfOver.toScheme B S hS).obj (W i))) ∧
      (∀ i, (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf (b i)) ∧
      (∀ i, Function.Surjective (pointsMap B S hS (yoneda.obj (W i)) (b i))) ∧
      (∀ i, (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf (b i)) ∧
      (∀ i, ∃ V : S.Opens, IsAffineOpen V ∧
        (∀ y : (BigFppfOver.toScheme B S hS).obj (W i),
          (B.inclusion.map (W i).hom) y ∈ V) ∧
        ∀ (T : BigFppfOver B S hS) (_x : (X i).toFunctor.obj (Opposite.op T))
          (t : (BigFppfOver.toScheme B S hS).obj T),
          (B.inclusion.map T.hom) t ∈ V)
```

## Tag 03H6, a lemma

[Tag 03H6](https://stacks.math.columbia.edu/tag/03H6) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_chart_of_isQuasiCompactSpaceULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedQuasiCompactPoints.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedQuasiCompactPoints.lean#L229). The attribute's comment: “the affine chart of a quasi-compact algebraic space, in a value universe independent of the universe of the schemes”.

> **Stacks 03H6**, the forward implication, for a presheaf with values in a universe
> `max w u` independent of the universe `u` of the schemes: a quasi-compact algebraic space over
> `S` admits a surjective étale chart whose source is an object of the site with *affine*
> underlying scheme, not merely a quasi-compact one.
>
> The presheaf is isomorphic to the universe lift of a presheaf of `Type u`, which is a
> quasi-compact algebraic space; Tag 03H6 supplies an affine surjective étale chart of it, and
> the universe lift of that chart composed with the isomorphism is the required one.

```lean
theorem exists_affine_chart_of_isQuasiCompactSpaceULift
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)}
    (hF : IsAlgebraicSpaceULift.{w} B S hS F) (h : IsQuasiCompactSpaceULift.{w} B S hS F) :
    ∃ (U : BigFppfOver B S hS) (a : (uliftYoneda.{w}).obj U ⟶ F),
      IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).relative (uliftYoneda.{w}) a ∧
      IsEtaleULift.{w} B S hS a
```

**`AlgebraicGeometry.Space.isQuasiCompactSpace_iff_exists_affine_etale_surjective_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/SpecialCoverings.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/SpecialCoverings.lean#L179).

> A quasi-compact algebraic space has an affine, étale, surjective cover, and any algebraic
> space with such a cover is quasi-compact.

```lean
theorem isQuasiCompactSpace_iff_exists_affine_etale_surjective_cover
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hF : IsAlgebraicSpace B S hS F) :
    IsQuasiCompactSpace B S hS F ↔
      ∃ (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ F),
        IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧
          (MorphismProperty.inverseImage
            (@Surjective.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS)).presheaf f ∧
          IsEtale B S hS f
```

## Tag 03FZ, a lemma

[Tag 03FZ](https://stacks.math.columbia.edu/tag/03FZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_of_isEtale_of_scheme_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartSeparated.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartSeparated.lean#L99). The attribute's comment: “the étale morphism is separated”.

> **Stacks 03FZ, first assertion.** An étale morphism to an algebraic space from an object of
> the site whose underlying scheme is separated is a separated morphism of algebraic spaces.

```lean
theorem isSeparated_of_isEtale_of_scheme_isSeparated
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hX : IsAlgebraicSpace B S hS X)
    (U : BigFppfOver B S hS)
    (hU : Scheme.IsSeparated ((BigFppfOver.toScheme B S hS).obj U))
    (f : yoneda.obj U ⟶ X) (_hf : IsEtale B S hS f) :
    IsSeparated B S hS f
```

**`AlgebraicGeometry.Space.isSeparated_scheme_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartSeparated.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartSeparated.lean#L113). The attribute's comment: “the self-fibre product is a separated scheme”.

> **Stacks 03FZ, second assertion.** The object of the site representing the self-fibre
> product of an étale chart with separated underlying scheme has separated underlying scheme.
> Its second projection is a base change of the chart, hence a separated morphism, and its
> target is a separated scheme.

```lean
theorem isSeparated_scheme_pullback
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (U : BigFppfOver B S hS)
    (hU : Scheme.IsSeparated ((BigFppfOver.toScheme B S hS).obj U))
    (f : yoneda.obj U ⟶ X) (_hf : IsEtale B S hS f) :
    Scheme.IsSeparated ((BigFppfOver.toScheme B S hS).obj
      ((hX.diagonal_representable.of_diag f).pullback f))
```

## Tag 07S4, a lemma

[Tag 07S4](https://stacks.math.columbia.edu/tag/07S4) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiSeparated_of_etaleAtlas_quasiCompact_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedAbsolute.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedAbsolute.lean#L99).

> An algebraic space over `S` which admits a surjective étale morphism `q` from an object of
> the site whose underlying scheme is quasi-separated, and one of whose two kernel-pair
> projections `pullback.fst q q`, `pullback.snd q q` is quasi-compact, is quasi-separated over the
> terminal scheme.

```lean
theorem isQuasiSeparated_of_etaleAtlas_quasiCompact_projection
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hAtlas : ∃ (U : BigFppfOver B S hS)
        (q : yoneda.obj U ⟶ X),
      QuasiSeparatedSpace ((BigFppfOver.toScheme B S hS).obj U) ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) q ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) q ∧
      ((MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@QuasiCompact.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) (pullback.fst q q) ∨
       (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@QuasiCompact.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) (pullback.snd q q))) :
    IsAbsolutelyQuasiSeparated B S hS hZ X
```

## Tag 03W7, a lemma

[Tag 03W7](https://stacks.math.columbia.edu/tag/03W7) in the Stacks Project.

**`AlgebraicGeometry.Space.isZariskiLocallyQuasiSeparatedOver_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedTfae.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedTfae.lean#L498).

> **Stacks 03W7.** For an algebraic space over a scheme `S`, Zariski local
> quasi-separatedness over `S`, absolute Zariski local quasi-separatedness, and the existence of
> a Zariski covering by open subspaces carrying quasi-compact surjective étale atlases by affine
> schemes — with or without the requirement that those affine schemes map into affine opens of
> `S` — are equivalent.

```lean
theorem isZariskiLocallyQuasiSeparatedOver_tfae
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) :
    List.TFAE
      [IsZariskiLocallyQuasiSeparatedOver B S hS X,
        IsAbsolutelyZariskiLocallyQuasiSeparated B S hS hZ X,
        HasAffineQuasiCompactEtaleCover B S hS X,
        HasAffineQuasiCompactEtaleCoverIntoAffineBase B S hS X]
```

## Tag 03IJ, a lemma

[Tag 03IJ](https://stacks.math.columbia.edu/tag/03IJ) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_fiber_pointsMap_of_etale_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartFinitePoints.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartFinitePoints.lean#L193). The attribute's comment: “fibres of the presenting scheme”.

> **Stacks 03IJ, the fibres of the presenting scheme.** An étale morphism `φ : h_U ⟶ X` of
> presheaves on the big fppf site of `S` out of a representable presheaf whose self-fibre-product
> projections are quasi-compact in the sense of Stacks 03HE has finite fibres on points.
>
> Any point of a fibre of `|U| → |X|` and a fixed point of that fibre are the two projections of
> a point of the relation, so the fibre is the image of a fibre of the first projection of the
> relation.

```lean
theorem finite_fiber_pointsMap_of_etale_presentation
    (hφ : IsEtale B S hS φ) (hs : IsQuasiCompact B S hS (pullback.fst φ φ))
    (_ht : IsQuasiCompact B S hS (pullback.snd φ φ)) (x : points B S hS X) :
    (pointsMap B S hS (yoneda.obj U) φ ⁻¹' {x}).Finite
```

**`AlgebraicGeometry.Space.finite_fiber_selfPullback_pointsMap_of_etale_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartFinitePoints.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartFinitePoints.lean#L217). The attribute's comment: “fibres of the relation scheme”.

> **Stacks 03IJ, the fibres of the relation scheme.** Under the same hypotheses the relation
> `h_U ×_X h_U` has finite fibres on points over `X`.
>
> A fibre of `|R| → |X|` is the union, over the finitely many points of the corresponding fibre
> of `|U| → |X|`, of the fibres of `|R| → |U|`.

```lean
theorem finite_fiber_selfPullback_pointsMap_of_etale_presentation
    (hφ : IsEtale B S hS φ) (hs : IsQuasiCompact B S hS (pullback.fst φ φ))
    (ht : IsQuasiCompact B S hS (pullback.snd φ φ)) (x : points B S hS X) :
    (pointsMap B S hS (pullback φ φ) (pullback.fst φ φ ≫ φ) ⁻¹' {x}).Finite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.6, Tag 03FW](https://stacks.math.columbia.edu/tag/03FW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
