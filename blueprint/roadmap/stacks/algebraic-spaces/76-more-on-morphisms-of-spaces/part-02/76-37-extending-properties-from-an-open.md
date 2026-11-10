---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFinitePresentation_chartModule_of_isFlatOver_of_dense_open, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_fromPreimage, AlgebraicGeometry.Space.relativeDimensionLE_of_dense_open, AlgebraicGeometry.Space.isFinite_of_isFinite_over_dense_open, AlgebraicGeometry.Space.isOpenImmersion_of_isIso_pullback_snd
statement: formalized
proof: formalized
---

# 76.37 Extending properties from an open

Section 76.37 of the Stacks Project, [Tag 0875](https://stacks.math.columbia.edu/tag/0875). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0876, a lemma

[Tag 0876](https://stacks.math.columbia.edu/tag/0876) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinitePresentation_chartModule_of_isFlatOver_of_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentationFromDenseOpen.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentationFromDenseOpen.lean#L435). The attribute's comment: “hypotheses (1) and (2) and the conclusion are read on the etale scheme charts: they are the corresponding properties of the restriction of the module to the charts, as for Space.IsFlatOver of Tag 05VV. Hypothesis (4) is read on the open subscheme that V cuts out in each chart of the target, which by Space.preimage_chartOpenOfOpenSubspace is the chart-level inverse image of V. The conclusion is stated on a commuting square of charts of f rather than on an arbitrary chart of the source, since not every chart of the source is the source of such a square”.

> **Stacks 0876.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`
> contained in a big fppf site `B` which is locally of finite presentation, let `F` be an
> `𝒪_X`-module which is quasi-coherent of finite type on charts and flat over `Y`, and let `V ⊆ Y`
> be an open subspace whose inclusion is quasi-compact and which is scheme-theoretically dense in
> the sense of Tag 0834.  If `F` restricted to `f⁻¹V` is of finite presentation on charts, then on
> every commuting square of étale scheme charts the restriction of `F` to the chart of `X` is of
> finite presentation.
>
> Hypothesis (3) of the source is exactly the two hypotheses `hVqc` and `hVdense` here.  They give
> the chartwise conditions of
> `AlgebraicGeometry.Space.isFinitePresentation_chartModule_of_isFlatOver_of_dense_open_charts` by
> `AlgebraicGeometry.Space.isRetrocompactOnCharts_of_isQuasiCompact` (Stacks 03HD) and
> `AlgebraicGeometry.Space.isSchemeTheoreticallyDenseOnCharts_of_isSchemeTheoreticallyDense`
> (Stacks 0836), and on one commuting square of charts the statement is then Stacks 081N for the
> vertical morphism of schemes.

```lean
theorem isFinitePresentation_chartModule_of_isFlatOver_of_dense_open
    (hX : IsAlgebraicSpace B S hS X) {f : X ⟶ Y} (F : Modules.{u, u} B S hS X hX)
    (hf : IsLocallyOfFinitePresentation B S hS f)
    (hqc : IsQuasicoherentOnCharts B S hS hX F) (hft : IsFiniteTypeOnCharts B S hS hX F)
    (hflat : IsFlatOver B S hS hX f F)
    (V : Subfunctor Y) (hV : IsOpenSubspace B S hS V)
    (hVqc : IsQuasiCompact B S hS V.ι)
    (hVdense : IsSchemeTheoreticallyDense B S hS V)
    (hfp : IsFinitePresentationOverOpenOnCharts B S hS hX f F V hV)
    (d : ChartDiagram B S hS X Y f) :
    (chartModule B S hS hX F d.U).IsFinitePresentation
```

## Tag 0877, a lemma

[Tag 0877](https://stacks.math.columbia.edu/tag/0877) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_fromPreimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/LocallyOfFinitePresentationFromDenseOpen.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/LocallyOfFinitePresentationFromDenseOpen.lean#L194).

> **Stacks 0877.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`
> contained in a big fppf site `B` which is locally of finite type and flat, and let `V ⊆ Y` be an
> open subspace whose inclusion is quasi-compact and which is scheme-theoretically dense in the
> sense of Tag 0834.  If the restriction `f⁻¹V ⟶ V` of `f` is locally of finite presentation, then
> `f` is locally of finite presentation.
>
> Local finite presentation is the every-étale-chart condition of Tag 03MJ, so this is
> `AlgebraicGeometry.Space.locallyOfFinitePresentation_chartDiagram_of_fromPreimage` for the
> commuting square of charts given by the chart data.

```lean
theorem isLocallyOfFinitePresentation_of_fromPreimage
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hlft : IsLocallyOfFiniteType B S hS f) (hflat : IsFlat B S hS f)
    (V : Subfunctor Y) (hV : IsOpenSubspace B S hS V)
    (hVqc : IsQuasiCompact B S hS V.ι)
    (hVdense : IsSchemeTheoreticallyDense B S hS V)
    (hfV : IsLocallyOfFinitePresentation B S hS (V.fromPreimage f)) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 0878, a lemma

[Tag 0878](https://stacks.math.columbia.edu/tag/0878) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeDimensionLE_of_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimensionDenseOpen.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimensionDenseOpen.lean#L393).

> **Stacks 0878.** A flat morphism of algebraic spaces over `S` locally of finite type has
> relative dimension at most `d` if its restriction over a dense open subspace of the target does,
> provided the morphism is locally of finite presentation or the open immersion is quasi-compact.

```lean
theorem relativeDimensionLE_of_dense_open (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (V : Subfunctor Y)
    (hV : IsOpenSubspace B S hS V)
    (hVdense : Dense (Set.range (pointsMap B S hS V.toFunctor V.ι)))
    (hflat : IsFlat B S hS f) (hlft : IsLocallyOfFiniteType B S hS f) (d : ℕ)
    (hdim : HasRelativeDimensionLE d B S hS (pullback.snd f V.ι))
    (hfin : IsLocallyOfFinitePresentation B S hS f ∨ IsQuasiCompact B S hS V.ι) :
    HasRelativeDimensionLE d B S hS f
```

## Tag 0B4J, a lemma

[Tag 0B4J](https://stacks.math.columbia.edu/tag/0B4J) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_of_isFinite_over_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FiniteDenseOpen.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FiniteDenseOpen.lean#L119).

> **Stacks 0B4J.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is flat
> and proper. Let `V` be an open subspace of `Y` whose points are dense in the points of `Y` and
> such that the base change `X_V ⟶ V` of `f` is finite. If moreover `f` is locally of finite
> presentation or the open immersion `V ⟶ Y` is quasi-compact, then `f` is finite.

```lean
theorem isFinite_of_isFinite_over_dense_open
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hflat : IsFlat B S hS f) (hproper : IsProper B S hS f)
    (V : Subfunctor Y) (hV : IsOpenSubspace B S hS V)
    (hVdense : Dense (Set.range (pointsMap B S hS V.toFunctor V.ι)))
    (hfinite : IsFinite B S hS (pullback.snd f V.ι))
    (hfin : IsLocallyOfFinitePresentation B S hS f ∨ IsQuasiCompact B S hS V.ι) :
    IsFinite B S hS f
```

## Tag 0879, a lemma

[Tag 0879](https://stacks.math.columbia.edu/tag/0879) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenImmersion_of_isIso_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/OpenImmersionFromDenseOpen.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/OpenImmersionFromDenseOpen.lean#L177).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S` contained in a big fppf
> site `B` which is separated, locally of finite type and flat, and let `V ⊆ Y` be an open subspace
> such that `f^{-1}V ⟶ V` is an isomorphism and the inclusion of `V` is quasi-compact and
> scheme-theoretically dense. Then `f` is an open immersion.

```lean
theorem isOpenImmersion_of_isIso_pullback_snd (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (V : Subfunctor Y)
    (hV : IsOpenSubspace B S hS V)
    (hsep : IsSeparated B S hS f) (hlft : IsLocallyOfFiniteType B S hS f)
    (hflat : IsFlat B S hS f) (hiso : IsIso (pullback.snd f V.ι))
    (hVqc : IsQuasiCompact B S hS V.ι)
    (hVdense : IsSchemeTheoreticallyDense B S hS V) :
    IsOpenImmersion B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.37, Tag 0875](https://stacks.math.columbia.edu/tag/0875)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
