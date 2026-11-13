---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_dense_open_genericFlatness_chart, AlgebraicGeometry.Space.exists_dense_open_genericFlatness_of_isAffine, AlgebraicGeometry.Space.exists_dense_open_genericFlatness, AlgebraicGeometry.Space.exists_dense_open_genericFlatness_of_isScheme, AlgebraicGeometry.Space.exists_dense_open_genericFlatness_isFinitePresentation, AlgebraicGeometry.Space.exists_dense_open_genericFlatness_isFinitePresentation_of_isScheme
statement: formalized
proof: formalized
---

# 67.32 Generic flatness

Section 67.32 of the Stacks Project, [Tag 06QR](https://stacks.math.columbia.edu/tag/06QR). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06QS, a proposition

[Tag 06QS](https://stacks.math.columbia.edu/tag/06QS) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_dense_open_genericFlatness_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatness.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatness.lean#L179). The attribute's comment: “the one-chart core of the proof: Tag 052B read on a commuting square of affine étale charts”.

> **Stacks 06QS, the one-chart core.** On a commuting square of étale charts of `f` whose
> source and target charts are affine and whose target chart is reduced, the chart morphism
> becomes flat and locally of finite presentation over a dense open of the target chart, over
> which the module becomes flat over the target and of finite presentation.

```lean
theorem exists_dense_open_genericFlatness_chart
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X hX)
    (hqc : IsQuasicoherentOnCharts B S hS hX F)
    (hft : IsFiniteTypeOnCharts B S hS hX F)
    {U V : BigFppfOver B S hS}
    [IsAffine ((BigFppfOver.toScheme B S hS).obj U)]
    [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    [IsReduced ((BigFppfOver.toScheme B S hS).obj V)]
    {p : yoneda.obj U ⟶ X} {b : yoneda.obj V ⟶ Y} (a : U ⟶ V)
    (hpE : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf p)
    (hbE : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf b)
    (hcomm : p ≫ f = yoneda.map a ≫ b)
    (hLFT : AlgebraicGeometry.LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map a)) :
    ∃ W : ((BigFppfOver.toScheme B S hS).obj V).Opens,
      Dense (W : Set ((BigFppfOver.toScheme B S hS).obj V)) ∧
      AlgebraicGeometry.Flat (((BigFppfOver.toScheme B S hS).map a) ∣_ W) ∧
      AlgebraicGeometry.LocallyOfFinitePresentation
        (((BigFppfOver.toScheme B S hS).map a) ∣_ W) ∧
      ∀ u : (BigFppfOver.toScheme B S hS).obj U,
        ((BigFppfOver.toScheme B S hS).map a) u ∈ W →
          pointOfEtaleChart B S hS ⟨CostructuredArrow.mk p, hpE⟩ u ∈
              flatLocus B S hS hX f F ∧
            pointOfEtaleChart B S hS ⟨CostructuredArrow.mk p, hpE⟩ u ∈
              finitePresentationLocus B S hS hX F
```

**`AlgebraicGeometry.Space.exists_dense_open_genericFlatness_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatness.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatness.lean#L415). The attribute's comment: “step 3 of the proof: the case of a reduced affine base”.

> **Stacks 06QS for a reduced affine base**, step 3 of the source. A finite-type morphism of
> algebraic spaces to a reduced affine scheme of the site, together with a module which is
> quasi-coherent of finite type on charts, becomes flat, locally of finite presentation and
> quasi-compact, and the module flat over the base and of finite presentation, over a dense open
> of the base.

```lean
theorem exists_dense_open_genericFlatness_of_isAffine
    (hX : IsAlgebraicSpace B S hS X) (Z : BigFppfOver B S hS)
    [IsAffine ((BigFppfOver.toScheme B S hS).obj Z)]
    [IsReduced ((BigFppfOver.toScheme B S hS).obj Z)]
    (f : X ⟶ yoneda.obj Z) (hf : IsFiniteType B S hS f)
    (F : Modules.{u, u} B S hS X hX)
    (hqc : IsQuasicoherentOnCharts B S hS hX F)
    (hft : IsFiniteTypeOnCharts B S hS hX F) :
    ∃ W : ((BigFppfOver.toScheme B S hS).obj Z).Opens,
      Dense (W : Set ((BigFppfOver.toScheme B S hS).obj Z)) ∧
      IsFlat B S hS (pullback.snd f (yoneda.map (openSiteObjectHom B S hS Z W))) ∧
      IsLocallyOfFinitePresentation B S hS
        (pullback.snd f (yoneda.map (openSiteObjectHom B S hS Z W))) ∧
      IsQuasiCompact B S hS (pullback.snd f (yoneda.map (openSiteObjectHom B S hS Z W))) ∧
      ∀ x : points B S hS X,
        pointsEquivScheme B S hS Z (pointsMap B S hS X f x) ∈ W →
          x ∈ flatLocus B S hS hX f F ∧ x ∈ finitePresentationLocus B S hS hX F
```

**`AlgebraicGeometry.Space.exists_dense_open_genericFlatness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatness.lean, line 689](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatness.lean#L689).

> **Stacks 06QS.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` of finite type
> with `Y` reduced, and let `F` be an `𝒪_X`-module which is quasi-coherent of finite type on
> charts. Then there is a dense open subspace `W` of `Y` such that the base change of `f` over
> `W` is flat, locally of finite presentation and quasi-compact, and such that `F` is flat over
> `Y` and of finite presentation at every point of `X` lying over `W`.

```lean
theorem exists_dense_open_genericFlatness
    (hX : IsAlgebraicSpace B S hS X) {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hY : IsAlgebraicSpace B S hS Y)
    (hYred : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsReduced T))
    (f : X ⟶ Y) (hf : IsFiniteType B S hS f)
    (F : Modules.{u, u} B S hS X hX)
    (hqc : IsQuasicoherentOnCharts B S hS hX F)
    (hft : IsFiniteTypeOnCharts B S hS hX F) :
    ∃ W : Subfunctor Y, IsDenseOpenSubspace B S hS hY W ∧
      IsFlat B S hS (pullback.snd f W.ι) ∧
      IsLocallyOfFinitePresentation B S hS (pullback.snd f W.ι) ∧
      IsQuasiCompact B S hS (pullback.snd f W.ι) ∧
      ∀ x : points B S hS X,
        pointsMap B S hS X f x ∈ Set.range (pointsMap B S hS W.toFunctor W.ι) →
          x ∈ flatLocus B S hS hX f F ∧
            x ∈ finitePresentationLocus B S hS hX F
```

**`AlgebraicGeometry.Space.exists_dense_open_genericFlatness_of_isScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatness.lean, line 736](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatness.lean#L736). The attribute's comment: “step 2 of the proof: the case of a reduced scheme base”.

> **Stacks 06QS for a reduced scheme base**, step 2 of the source. This is the general
> statement for a base which is represented by an object of the site, where the identity may be
> taken as the surjective étale chart witnessing reducedness.

```lean
theorem exists_dense_open_genericFlatness_of_isScheme
    (hX : IsAlgebraicSpace B S hS X) (Z : BigFppfOver B S hS)
    [IsReduced ((BigFppfOver.toScheme B S hS).obj Z)]
    (f : X ⟶ yoneda.obj Z) (hf : IsFiniteType B S hS f)
    (F : Modules.{u, u} B S hS X hX)
    (hqc : IsQuasicoherentOnCharts B S hS hX F)
    (hft : IsFiniteTypeOnCharts B S hS hX F) :
    ∃ W : Subfunctor (yoneda.obj Z),
      IsDenseOpenSubspace B S hS (isAlgebraicSpace_yoneda B S hS Z) W ∧
      IsFlat B S hS (pullback.snd f W.ι) ∧
      IsLocallyOfFinitePresentation B S hS (pullback.snd f W.ι) ∧
      IsQuasiCompact B S hS (pullback.snd f W.ι) ∧
      ∀ x : points B S hS X,
        pointsMap B S hS X f x ∈ Set.range (pointsMap B S hS W.toFunctor W.ι) →
          x ∈ flatLocus B S hS hX f F ∧
            x ∈ finitePresentationLocus B S hS hX F
```

## Tag 06QT, a proposition

[Tag 06QT](https://stacks.math.columbia.edu/tag/06QT) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_dense_open_genericFlatness_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatnessFinitePresentation.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatnessFinitePresentation.lean#L107).

> **Stacks 06QT.** Let `f : X ⟶ Y` be a quasi-separated morphism of algebraic spaces over `S`
> of finite type with `Y` reduced, and let `F` be an `𝒪_X`-module which is quasi-coherent of
> finite type on charts. Then there is a dense open subspace `W` of `Y` such that the base change
> of `f` over `W` is flat and of finite presentation, and such that `F` is flat over `Y` and of
> finite presentation at every point of `X` lying over `W`.
>
> This is Stacks 06QS refined by the quasi-separatedness hypothesis: that proposition gives
> flatness, local finite presentation and quasi-compactness of the base change, and a base change
> of a quasi-separated morphism is quasi-separated.

```lean
theorem exists_dense_open_genericFlatness_isFinitePresentation
    (hX : IsAlgebraicSpace B S hS X) {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hY : IsAlgebraicSpace B S hS Y)
    (hYred : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsReduced T))
    (f : X ⟶ Y) (hqs : IsQuasiSeparated B S hS f) (hf : IsFiniteType B S hS f)
    (F : Modules.{u, u} B S hS X hX)
    (hqc : IsQuasicoherentOnCharts B S hS hX F)
    (hft : IsFiniteTypeOnCharts B S hS hX F) :
    ∃ W : Subfunctor Y, IsDenseOpenSubspace B S hS hY W ∧
      IsFlat B S hS (pullback.snd f W.ι) ∧
      IsFinitePresentation B S hS (pullback.snd f W.ι) ∧
      ∀ x : points B S hS X,
        pointsMap B S hS X f x ∈ Set.range (pointsMap B S hS W.toFunctor W.ι) →
          x ∈ flatLocus B S hS hX f F ∧
            x ∈ finitePresentationLocus B S hS hX F
```

**`AlgebraicGeometry.Space.exists_dense_open_genericFlatness_isFinitePresentation_of_isScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatnessFinitePresentation.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/GenericFlatnessFinitePresentation.lean#L131). The attribute's comment: “the case of a base represented by an object of the site”.

> **Stacks 06QT for a base represented by an object of the site.** This is the statement of
> the tag for a reduced scheme base, where the identity may be taken as the surjective étale
> chart witnessing reducedness.

```lean
theorem exists_dense_open_genericFlatness_isFinitePresentation_of_isScheme
    (hX : IsAlgebraicSpace B S hS X) (Z : BigFppfOver B S hS)
    [IsReduced ((BigFppfOver.toScheme B S hS).obj Z)]
    (f : X ⟶ yoneda.obj Z) (hqs : IsQuasiSeparated B S hS f) (hf : IsFiniteType B S hS f)
    (F : Modules.{u, u} B S hS X hX)
    (hqc : IsQuasicoherentOnCharts B S hS hX F)
    (hft : IsFiniteTypeOnCharts B S hS hX F) :
    ∃ W : Subfunctor (yoneda.obj Z),
      IsDenseOpenSubspace B S hS (isAlgebraicSpace_yoneda B S hS Z) W ∧
      IsFlat B S hS (pullback.snd f W.ι) ∧
      IsFinitePresentation B S hS (pullback.snd f W.ι) ∧
      ∀ x : points B S hS X,
        pointsMap B S hS X f x ∈ Set.range (pointsMap B S hS W.toFunctor W.ι) →
          x ∈ flatLocus B S hS hX f F ∧
            x ∈ finitePresentationLocus B S hS hX F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.32, Tag 06QR](https://stacks.math.columbia.edu/tag/06QR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
