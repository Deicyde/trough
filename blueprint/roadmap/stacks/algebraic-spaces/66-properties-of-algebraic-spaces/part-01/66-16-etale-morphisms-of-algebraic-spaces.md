---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.etale_comp_of_scheme, AlgebraicGeometry.Space.etale_of_etale_charts, AlgebraicGeometry.Space.etale_of_comp_surjective_etale, AlgebraicGeometry.Space.IsEtale, AlgebraicGeometry.Space.isEtale_iff_exists_source_chart, AlgebraicGeometry.Space.isEtale_iff_exists_target_chart, AlgebraicGeometry.Space.isEtale_iff_exists_etale_chart_square, AlgebraicGeometry.Space.isEtale_tfae
statement: formalized
proof: formalized
---

# 66.16 Étale morphisms of algebraic spaces

Section 66.16 of the Stacks Project, [Tag 03FQ](https://stacks.math.columbia.edu/tag/03FQ). 8 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03EC, a lemma

[Tag 03EC](https://stacks.math.columbia.edu/tag/03EC) in the Stacks Project.

**`AlgebraicGeometry.Space.etale_comp_of_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleCharts.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleCharts.lean#L163). The attribute's comment: “composition”.

> **Stacks 03EC.** An étale morphism of the big fppf site of `S` followed by an étale chart
> of an algebraic space is again an étale chart.

```lean
theorem etale_comp_of_scheme {U U' : BigFppfOver B S hS}
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : U ⟶ U') (g : yoneda.obj U' ⟶ F)
    (hf : AlgebraicGeometry.Etale ((BigFppfOver.toScheme B S hS).map f))
    (hg : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf g) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map f ≫ g)
```

**`AlgebraicGeometry.Space.etale_of_etale_charts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleCharts.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleCharts.lean#L186). The attribute's comment: “morphism\_between\_charts”.

> **Stacks 03EC.** A morphism of the big fppf site of `S` between two étale charts of a
> presheaf is an étale morphism of schemes.
>
> The ambient presheaf need not be an algebraic space, so the statement covers the source one:
> the second chart is étale and hence relatively representable, which is all that is used. The
> morphism factors through the fibre product of the two charts, as a section of one projection
> followed by the other. Both projections are étale by cancellation against the étale charts,
> and a section of an étale morphism is étale by
> `CategoryTheory.MorphismProperty.of_postcomp`, so no descent along an atlas is required.

```lean
theorem etale_of_etale_charts {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {U U' : BigFppfOver B S hS}
    (φ : yoneda.obj U ⟶ F) (φ' : yoneda.obj U' ⟶ F)
    (hφ : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf φ)
    (hφ' : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf φ')
    (χ : U ⟶ U') (hχ : yoneda.map χ ≫ φ' = φ) :
    AlgebraicGeometry.Etale ((BigFppfOver.toScheme B S hS).map χ)
```

**`AlgebraicGeometry.Space.etale_of_comp_surjective_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleCharts.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleCharts.lean#L220). The attribute's comment: “descent\_from\_chart”.

> **Stacks 03EC.** Étaleness of a chart of an algebraic space descends along a surjective
> étale morphism of the big fppf site of `S`: if `χ : U ⟶ U'` is surjective étale and
> `yoneda.map χ ≫ φ'` is an étale chart, then so is `φ'`.

```lean
theorem etale_of_comp_surjective_etale {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) {U U' : BigFppfOver B S hS} (χ : U ⟶ U')
    [AlgebraicGeometry.Surjective ((BigFppfOver.toScheme B S hS).map χ)]
    [AlgebraicGeometry.Etale ((BigFppfOver.toScheme B S hS).map χ)]
    (φ' : yoneda.obj U' ⟶ X)
    (hφ : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map χ ≫ φ')) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf φ'
```

## Tag 03FR, a definition

[Tag 03FR](https://stacks.math.columbia.edu/tag/03FR) in the Stacks Project.

**`AlgebraicGeometry.Space.IsEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L184).

> **Stacks 03FR.** A morphism of algebraic spaces over `S` is *étale* when its composite
> with every étale morphism from a representable presheaf into its source is again étale.

```lean
abbrev IsEtale {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

## Tag 03FS, a lemma

[Tag 03FS](https://stacks.math.columbia.edu/tag/03FS) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_iff_exists_source_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L113). The attribute's comment: “condition (2)”.

> A morphism of algebraic spaces over `S` is étale exactly when its composite with some
> surjective étale chart of its source is étale.

```lean
theorem isEtale_iff_exists_source_chart {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    IsEtale B S hS f ↔
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ F),
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        IsEtale B S hS (p ≫ f)
```

**`AlgebraicGeometry.Space.isEtale_iff_exists_target_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L155). The attribute's comment: “condition (3)”.

> A morphism of algebraic spaces over `S` is étale exactly when its base change along some
> surjective étale chart of its target is étale.

```lean
theorem isEtale_iff_exists_target_chart {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    IsEtale B S hS f ↔
      ∃ (V : BigFppfOver B S hS) (q : yoneda.obj V ⟶ G),
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf q ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf q ∧
        IsEtale B S hS (pullback.snd f q)
```

**`AlgebraicGeometry.Space.isEtale_iff_exists_etale_chart_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L222). The attribute's comment: “condition (4)”.

> A morphism of algebraic spaces over `S` is étale exactly when it fits in a commuting square
> of charts, with the chart of the source surjective and étale, the chart of the target étale, and
> the morphism of schemes between them étale.

```lean
theorem isEtale_iff_exists_etale_chart_square {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    IsEtale B S hS f ↔
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ F) (q : yoneda.obj V ⟶ G) (α : U ⟶ V),
        p ≫ f = yoneda.map α ≫ q ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf q ∧
        AlgebraicGeometry.Etale ((BigFppfOver.toScheme B S hS).map α)
```

**`AlgebraicGeometry.Space.isEtale_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleTargetChartCriterion.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleTargetChartCriterion.lean#L174).

> **Stacks 03FS.** For a morphism `f : F ⟶ G` of algebraic spaces over `S` the following four
> conditions are equivalent: `f` is étale; there is a surjective étale scheme chart of `F` whose
> composite with `f` is étale; there is a surjective étale scheme chart of `G` along which the
> base change of `f` is étale; and `f` fits into a commuting square of étale scheme charts, with
> the chart of `F` surjective, whose upper morphism of schemes is étale.
>
> Conditions (1), (2) and (4) are `AlgebraicGeometry.Space.isEtale_iff_exists_source_chart` and
> `AlgebraicGeometry.Space.isEtale_iff_exists_etale_chart_square`; condition (3) is
> `AlgebraicGeometry.Space.isEtale_iff_exists_target_chart`.

```lean
theorem isEtale_tfae (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    List.TFAE [
      IsEtale B S hS f,
      (∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ F),
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        IsEtale B S hS (p ≫ f)),
      (∃ (V : BigFppfOver B S hS) (ψ : yoneda.obj V ⟶ G),
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf ψ ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf ψ ∧
        IsEtale B S hS (pullback.snd f ψ)),
      (∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ F) (q : yoneda.obj V ⟶ G) (α : U ⟶ V),
        p ≫ f = yoneda.map α ≫ q ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf q ∧
        AlgebraicGeometry.Etale ((BigFppfOver.toScheme B S hS).map α))
    ]
```

## Tag 03FT, a lemma

[Tag 03FT](https://stacks.math.columbia.edu/tag/03FT) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L75).

> The composite of two étale morphisms of presheaves on the big fppf site of `S` is étale.

```lean
theorem isEtale_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G} {g : G ⟶ H}
    (hf : IsEtale B S hS f) (hg : IsEtale B S hS g) : IsEtale B S hS (f ≫ g)
```

## Tag 03FU, a lemma

[Tag 03FU](https://stacks.math.columbia.edu/tag/03FU) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L254). References: SGA 1 IX (1.3).

> A base change of an étale morphism of algebraic spaces over `S` is étale.

```lean
theorem isEtale_of_isPullback {X' X Z Y : AlgebraicSpaces B S hS}
    (p : X' ⟶ X) (f' : X' ⟶ Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (h : IsPullback p f' f g) (hf : IsEtale B S hS f.hom) :
    IsEtale B S hS f'.hom
```

## Tag 03FV, a lemma

[Tag 03FV](https://stacks.math.columbia.edu/tag/03FV) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_of_isEtale_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L378).

> A morphism between two algebraic spaces which are étale over a common algebraic space is
> itself étale.

```lean
theorem isEtale_of_isEtale_over {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (_hH : IsAlgebraicSpace B S hS H) (f : F ⟶ G) (g : F ⟶ H) (h : G ⟶ H)
    (hg : IsEtale B S hS g) (hh : IsEtale B S hS h) (hfg : f ≫ h = g) :
    IsEtale B S hS f
```

## Tag 03IR, a lemma

[Tag 03IR](https://stacks.math.columbia.edu/tag/03IR) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenMap_pointsMap_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleOpenOnPoints.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleOpenOnPoints.lean#L75).

> **Stacks 03IR.** An étale morphism `f : X ⟶ Y` of algebraic spaces over `S` induces an
> open map `|X| → |Y|` on the point sets of Tag 03BU, for the topology of Tag 03BX.
>
> The hypothesis `_hG` that the target is an algebraic space is retained from the source
> statement but is not used: only an étale chart of the source enters the argument.

```lean
theorem isOpenMap_pointsMap_of_isEtale (f : F ⟶ G) (hF : IsAlgebraicSpace B S hS F)
    (_hG : IsAlgebraicSpace B S hS G) (hf : IsEtale B S hS f) :
    @IsOpenMap _ _ (pointTopology B S hS F) (pointTopology B S hS G)
      (pointsMap B S hS F f)
```

## Tag 03KX, a lemma

[Tag 03KX](https://stacks.math.columbia.edu/tag/03KX) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_etale_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/EtaleOverFieldRepresentable.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/EtaleOverFieldRepresentable.lean#L305).

> **Stacks 03KX.** An algebraic space over `S` admitting an étale morphism to an object of the
> big fppf site over `S` whose underlying scheme is the spectrum of a field is representable.

```lean
theorem isRepresentable_of_etale_over_field
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (k : Type u) [Field k]
    (V : BigFppfOver B S hS)
    (eV : (BigFppfOver.toScheme B S hS).obj V ≅ Spec (.of k))
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (f : F ⟶ yoneda.obj V) (hf : IsEtale B S hS f) :
    F.IsRepresentable
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.16, Tag 03FQ](https://stacks.math.columbia.edu/tag/03FQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
