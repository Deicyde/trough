---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsSmooth, AlgebraicGeometry.Space.IsSmoothAt, AlgebraicGeometry.Space.isSmooth_comp, AlgebraicGeometry.Space.isSmooth_isStableUnderBaseChange, AlgebraicGeometry.Space.isSmooth_tfae, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isSmooth, AlgebraicGeometry.Space.isLocallyOfFiniteType_of_isSmooth, AlgebraicGeometry.Space.isFlat_of_isSmooth
statement: formalized
proof: formalized
---

# 67.37 Smooth morphisms

Section 67.37 of the Stacks Project, [Tag 03ZB](https://stacks.math.columbia.edu/tag/03ZB). 10 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03ZC, a definition

[Tag 03ZC](https://stacks.math.columbia.edu/tag/03ZC) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Smooth.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Smooth.lean#L43). The attribute's comment: “part (1): smooth morphisms”.

> A morphism of algebraic spaces over `S` is *smooth* when the scheme morphism underlying every
> commuting square of étale scheme charts of it is smooth.

```lean
abbrev IsSmooth (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsSmoothAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Smooth.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Smooth.lean#L50). The attribute's comment: “part (2): smooth at a point”.

> A morphism of algebraic spaces over `S` is *smooth at* a point `x` of its source when it is
> smooth on some open subspace of the source having a point over `x`.

```lean
abbrev IsSmoothAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

## Tag 03ZD, a lemma

[Tag 03ZD](https://stacks.math.columbia.edu/tag/03ZD) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothMorphismProperty.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmoothMorphismProperty.lean#L72). References: EGA IV (17.3.3), “more general”; EGA IV (6.8.3), “more general”.

> **Stacks 03ZD.** The composite of two smooth morphisms of algebraic spaces over `S` is
> smooth: this is Stacks 0AML applied to the smooth property of morphisms of schemes, which is
> étale local on the source and target and stable under composition.

```lean
theorem isSmooth_comp {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsSmooth B S hS f) (hg : IsSmooth B S hS g) :
    IsSmooth B S hS (f ≫ g)
```

## Tag 03ZE, a lemma

[Tag 03ZE](https://stacks.math.columbia.edu/tag/03ZE) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/SmoothLocalAtSource.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/SmoothLocalAtSource.lean#L119). References: SGA 1 II (1.3), “(ii)”.

> **Stacks Project, Tag 03ZE.** Smoothness of morphisms of algebraic spaces over `S` is
> stable under base change.

```lean
theorem isSmooth_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsSmooth B S hS f.hom)
```

## Tag 03ZF, a lemma

[Tag 03ZF](https://stacks.math.columbia.edu/tag/03ZF) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothTfae.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmoothTfae.lean#L479).

> The pointwise, scheme-local, étale-local, and Zariski-local criteria for
> smoothness of a morphism of algebraic spaces.

```lean
theorem isSmooth_tfae
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [
      IsSmooth B S hS f,
      (∀ x : points B S hS X, IsSmoothAt B S hS f x),
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsSmooth B S hS (pullback.snd f g)),
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          IsSmooth B S hS (pullback.snd f g)),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        IsSmooth B S hS (pullback.snd f g)),
      (∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf p ∧
        IsSmooth B S hS (p ≫ f)),
      HoldsOnEveryEtaleChart B S hS
        (@Smooth.{u} : MorphismProperty Scheme.{u}) f,
      HoldsOnSurjectiveEtaleChart B S hS
        (@Smooth.{u} : MorphismProperty Scheme.{u}) f,
      (∃ (I : Type u) (V : I → Subfunctor Y),
        IsZariskiCover B S hS I V ∧
        ∀ i, ∃ (J : Type u)
          (U : J → Subfunctor (pullback f (V i).ι)),
          IsZariskiCover B S hS J U ∧
          ∀ j, IsSmooth B S hS
            ((U j).ι ≫ pullback.snd f (V i).ι))
    ]
```

## Tag 04AJ, a lemma

[Tag 04AJ](https://stacks.math.columbia.edu/tag/04AJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean#L94).

> **Stacks 04AJ.** A smooth morphism of algebraic spaces over `S` is locally of finite
> presentation.

```lean
theorem isLocallyOfFinitePresentation_of_isSmooth
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G}
    (hf : IsSmooth B S hS f) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 06MH, a lemma

[Tag 06MH](https://stacks.math.columbia.edu/tag/06MH) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean#L125).

> **Stacks 06MH.** A smooth morphism of algebraic spaces over `S` is locally of finite
> type.

```lean
theorem isLocallyOfFiniteType_of_isSmooth
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G}
    (hf : IsSmooth B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 04TA, a lemma

[Tag 04TA](https://stacks.math.columbia.edu/tag/04TA) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothFlat.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmoothFlat.lean#L48).

> **Stacks 04TA.** A smooth morphism of algebraic spaces over `S` is flat: on each commuting
> square of étale scheme charts the underlying scheme morphism is smooth, hence flat.

```lean
theorem isFlat_of_isSmooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (hf : IsSmooth B S hS f) :
    IsFlat B S hS f
```

## Tag 06CP, a lemma

[Tag 06CP](https://stacks.math.columbia.edu/tag/06CP) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomic_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean#L190).

> **Stacks 06CP.** A smooth morphism of algebraic spaces over `S` is syntomic.
>
> On each commuting square of étale charts the underlying morphism of schemes is smooth, hence
> syntomic by `AlgebraicGeometry.syntomic_of_smooth`, which is Stacks 01VD.

```lean
theorem isSyntomic_of_isSmooth (f : X ⟶ Y) (hf : IsSmooth B S hS f) :
    IsSyntomic B S hS f
```

## Tag 0DZI, a lemma

[Tag 0DZI](https://stacks.math.columbia.edu/tag/0DZI) in the Stacks Project.

**`AlgebraicGeometry.Space.le_maximalSmoothOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean#L271). The attribute's comment: “maximality of the smooth locus”.

> **Stacks 0DZI, maximality.** Every open subspace on which `f` is smooth is contained in the
> smooth locus: it is a member of the family the smooth locus is the supremum of.

```lean
theorem le_maximalSmoothOpen (f : X ⟶ Y) {U : Subfunctor X}
    (hU : IsOpenSubspace B S hS U) (hUf : IsSmooth B S hS (U.ι ≫ f)) :
    U ≤ maximalSmoothOpen B S hS f
```

**`AlgebraicGeometry.Space.isOpenSubspace_maximalSmoothOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean#L411). The attribute's comment: “the smooth locus is an open subspace”.

> **Stacks 0DZI, openness.** The smooth locus of a morphism of algebraic spaces over `S` is
> an open subspace.

```lean
theorem isOpenSubspace_maximalSmoothOpen (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsOpenSubspace B S hS (maximalSmoothOpen B S hS f)
```

**`AlgebraicGeometry.Space.isSmooth_maximalSmoothOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean#L419). The attribute's comment: “the morphism is smooth on its smooth locus”.

> **Stacks 0DZI, smoothness on the open.** A morphism of algebraic spaces over `S` is smooth
> on its smooth locus.

```lean
theorem isSmooth_maximalSmoothOpen (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsSmooth B S hS ((maximalSmoothOpen B S hS f).ι ≫ f)
```

**`AlgebraicGeometry.Space.maximalSmoothOpen_eq_preimage_of_isFlat_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean, line 738](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean#L738). The attribute's comment: “part (1): base change by a flat morphism locally of finite presentation”. References: EGA IV (17.7.4), “more general”.

> **Stacks 0DZI, part (1).** Formation of the smooth locus commutes with base change by a
> morphism which is flat and locally of finite presentation.

```lean
theorem maximalSmoothOpen_eq_preimage_of_isFlat_isLocallyOfFinitePresentation
    (sq : IsPullback g' f' f g) (hgflat : IsFlat B S hS g.hom)
    (hglfp : IsLocallyOfFinitePresentation B S hS g.hom) :
    maximalSmoothOpen B S hS f'.hom = (maximalSmoothOpen B S hS f.hom).preimage g'.hom
```

**`AlgebraicGeometry.Space.maximalSmoothOpen_eq_preimage_of_isLocallyOfFinitePresentation_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean, line 749](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Smooth.lean#L749). The attribute's comment: “part (2): flat base change of a morphism locally of finite presentation”. References: EGA IV (17.7.4), “(v), special case”.

> **Stacks 0DZI, part (2).** For a morphism locally of finite presentation, formation of the
> smooth locus commutes with every flat base change.

```lean
theorem maximalSmoothOpen_eq_preimage_of_isLocallyOfFinitePresentation_isFlat
    (sq : IsPullback g' f' f g) (hflfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (hgflat : IsFlat B S hS g.hom) :
    maximalSmoothOpen B S hS f'.hom = (maximalSmoothOpen B S hS f.hom).preimage g'.hom
```

## Tag 0AFI, a lemma

[Tag 0AFI](https://stacks.math.columbia.edu/tag/0AFI) in the Stacks Project.

**`AlgebraicGeometry.Space.dimensionAtPoint_eq_add_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SmoothDimensionFormula.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SmoothDimensionFormula.lean#L70).

> **Stacks 0AFI.** Let `f : X ⟶ Y` be a smooth morphism of locally Noetherian algebraic
> spaces over `S`. For every point `x` of `X` with image `y` in `Y` we have
> `dim_x(X) = dim_y(Y) + dim_x(X_y)`, where `dim_x(X_y)` is the relative dimension `d` of `f`
> at `x` in the sense of Tag 04NM.

```lean
public theorem dimensionAtPoint_eq_add_of_isSmooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (_hNX : HasEtaleLocalProperty B S hS X (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (hNY : HasEtaleLocalProperty B S hS Y (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (f : X ⟶ Y) (hf : IsSmooth B S hS f) {d : ℕ∞} (x : points B S hS X)
    (hd : HasRelativeDimensionAt d B S hS f x) :
    dimensionAtPoint B S hS X hX x =
      dimensionAtPoint B S hS Y hY (pointsMap B S hS X f x) + (d : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.37, Tag 03ZB](https://stacks.math.columbia.edu/tag/03ZB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
