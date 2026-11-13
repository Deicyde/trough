---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exact_moduleChartDirectImage, AlgebraicGeometry.Space.modulePushforward_comp_overFunctorIso, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_isClosedImmersion, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_qcqs
statement: formalized
proof: formalized
---

# 67.11 Pushforward of quasi-coherent sheaves

Section 67.11 of the Stacks Project, [Tag 03M7](https://stacks.math.columbia.edu/tag/03M7). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03M8, a lemma

[Tag 03M8](https://stacks.math.columbia.edu/tag/03M8) in the Stacks Project.

**`AlgebraicGeometry.Space.exact_moduleChartDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModulePushforwardPresentationExactSequence.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModulePushforwardPresentationExactSequence.lean#L459).

> **Stacks 03M8.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, let `U` be a
> surjective étale scheme chart of `X` with structure morphism `τ`, let `R = U ×_X U` (the
> cartesian square `hR` in the spaces-étale site of `X`) with its two projections `t, s : R ⟶ U`
> and structure morphism `ρ`, and put `a = τ ≫ f`, `b = ρ ≫ f`.  For every `𝒪_X`-module `F` the
> sequence
>
> `0 → f_*F → a_*(F|_U) → b_*(F|_R)`
>
> of `𝒪_Y`-modules, whose first arrow is `AlgebraicGeometry.Space.moduleChartDirectImageUnitArrow`
> and whose second arrow is the difference `t^* - s^*` of the two arrows
> `AlgebraicGeometry.Space.moduleChartDirectImageParallelArrow`, is exact: the short complex is
> exact and its first arrow is a monomorphism.

```lean
theorem exact_moduleChartDirectImage (hU : IsSurjective B S hS U.1.hom) {t s : R ⟶ U}
    (hR : IsPullback ((comparisonFunctor B S hS X).map t) ((comparisonFunctor B S hS X).map s)
      ((SpacesEtale.isTerminal_idObj B S hS X).from ((comparisonFunctor B S hS X).obj U))
      ((SpacesEtale.isTerminal_idObj B S hS X).from ((comparisonFunctor B S hS X).obj U)))
    (F : Modules.{u, u} B S hS X.1 X.2) :
    (ShortComplex.mk
        (moduleChartDirectImageUnitArrow B S hS f ((comparisonFunctor B S hS X).obj U).2 F)
        (moduleChartDirectImageParallelArrow B S hS f ((comparisonFunctor B S hS X).obj U).2
            (isEtale_chartMap B S hS X t) ((comparisonFunctor B S hS X).obj R).2
            (Over.w ((comparisonFunctor B S hS X).map t).hom) F -
          moduleChartDirectImageParallelArrow B S hS f ((comparisonFunctor B S hS X).obj U).2
            (isEtale_chartMap B S hS X s) ((comparisonFunctor B S hS X).obj R).2
            (Over.w ((comparisonFunctor B S hS X).map s).hom) F)
        (moduleChartDirectImage_comp_sub_eq_zero B S hS f t s F)).Exact ∧
      Mono (moduleChartDirectImageUnitArrow B S hS f ((comparisonFunctor B S hS X).obj U).2 F)
```

## Tag 04CF, an equation

[Tag 04CF](https://stacks.math.columbia.edu/tag/04CF) in the Stacks Project.

**`AlgebraicGeometry.Space.modulePushforward_comp_overFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModulePushforwardChartRestriction.lean, line 484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModulePushforwardChartRestriction.lean#L484). The attribute's comment: “for an arbitrary morphism of algebraic spaces, with the restriction to the base-changed chart taken on the slice of the spaces-étale site”.

> **Stacks 04CF, for an arbitrary morphism of algebraic spaces.** Let `f : X ⟶ Y` be a
> morphism of algebraic spaces over `S` and let `V` be an étale scheme chart of `Y`.  Write
> `U = V ×_Y X` for the base change of the chart, an étale algebraic space over `X`, and
> `f' : U ⟶ V` for the base change of `f`.  Then for every `𝒪_X`-module `F`
>
> `f'_*(F|_U) = (f_*F)|_V`.
>
> The restriction `(-)|_V` is restriction to the slice of the small étale site of `Y` at `V`, the
> restriction `(-)|_U` is restriction to the slice of the *spaces-étale* site of `X` at `U` — both
> readings of Stacks' Equation 03LW — and `f'_*` is the direct image along the localized
> base-change functor of Stacks 03CF with the localized structure map
> `AlgebraicGeometry.Space.chartLocalizedStructureSharp` of Stacks 04J0, part (1).
>
> No representability hypothesis is made on `f`; this is the form in which the proof of
> Stacks 03M9 invokes the identity.  It is an isomorphism rather than an equality of functors
> because `AlgebraicGeometry.Space.smallEtaleDirectImage` is conjugated by the comparison
> equivalence of Stacks 03G1; for a representable `f` an equality is available in the reading of
> `AlgebraicGeometry.Space.overFunctor_comp_smallBaseChangeModulePushforward`.

```lean
noncomputable def modulePushforward_comp_overFunctorIso (f : X ⟶ Y)
    (V : SmallEtale B S hS Y.1) :
    modulePushforward B S hS f ⋙
        SheafOfModules.overFunctor.{u} (structureRingSheaf B S hS Y) V ≅
      moduleChartBaseChangeRestriction B S hS f V ⋙
        chartLocalizedModulePushforward B S hS f V
```

## Tag 03M9, a lemma

[Tag 03M9](https://stacks.math.columbia.edu/tag/03M9) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentPushforward.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentPushforward.lean#L110). The attribute's comment: “the direct image along a closed immersion of algebraic spaces”.

> **Stacks 03M9 along a closed immersion of algebraic spaces.**  The direct image `i_*G` of a
> quasi-coherent `𝒪_Z`-module along a closed immersion `i : Z ⟶ X` is quasi-coherent.
>
> A closed immersion is representable and affine, so its direct image is computed on base-changed
> charts by `AlgebraicGeometry.Space.modulePushforwardChartIso` and that one is cartesian on affine
> charts.

```lean
theorem isQuasicoherentOnSite_modulePushforward_of_isClosedImmersion (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) (G : Modules.{u, u} B S hS Z.1 Z.2)
    (hG : G.IsQuasicoherentOnSite) :
    ((modulePushforward B S hS i).obj G).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentPushforwardQcqs.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentPushforwardQcqs.lean#L202).

> **Stacks 03M9.**  Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> algebraic spaces over `S`.  Then the direct image `f_*F` of a quasi-coherent `𝒪_X`-module `F` is
> quasi-coherent.
>
> Quasi-coherence of `f_*F` is tested on the affine étale charts `V` of `Y`, over which `f_*F`
> restricts to the direct image along the base change `V ×_Y X ⟶ V` of the restriction of `F`
> (`AlgebraicGeometry.Space.pushforward_isQuasicoherentOnSite_of_forall_affine_chart`); that base
> change is quasi-separated with quasi-compact source, and the affine-base case is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_affine_target`.

```lean
theorem isQuasicoherentOnSite_modulePushforward_of_qcqs (f : X ⟶ Y)
    (quasiCompact : IsQuasiCompact B S hS f.hom)
    (quasiSeparated : IsQuasiSeparated B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (F_qcoh : F.IsQuasicoherentOnSite) :
    ((modulePushforward B S hS f).obj F).IsQuasicoherentOnSite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.11, Tag 03M7](https://stacks.math.columbia.edu/tag/03M7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
