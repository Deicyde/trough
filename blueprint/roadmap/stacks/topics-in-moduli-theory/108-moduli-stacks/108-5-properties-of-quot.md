---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuotSituation.diagonal_quotSitePresheafToBase, AlgebraicGeometry.Space.QuotSituation.isLocallyOfFinitePresentationULift_quotSitePresheafToBase, AlgebraicGeometry.Space.QuotSituation.isSeparatedULift_and_imp_isLocallyOfFinitePresentationULift_quotSitePresheafToBase, AlgebraicGeometry.Space.QuotSituation.isSeparatedULift_quotSitePresheafToBase, StacksDraft.GenericFibre.existsUnique_submodule_flat_quotient, AlgebraicGeometry.Space.QuotSitePresheafModel.valuativeCriterionExistence_toBase, AlgebraicGeometry.Space.QuotPushforwardSituation.pushforwardQuotFunctorMap, AlgebraicGeometry.Space.QuotPushforwardSituation
statement: formalized
proof: formalized
---

# 108.5 Properties of Quot

Section 108.5 of the Stacks Project, [Tag 0DM1](https://stacks.math.columbia.edu/tag/0DM1). 11 tags here are carried by 38 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DM2, a lemma

[Tag 0DM2](https://stacks.math.columbia.edu/tag/0DM2) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.diagonal_quotSitePresheafToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorDiagonal.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorDiagonal.lean#L425).

> The diagonal of `Quot_{F/X/B} ⟶ B` is a closed immersion. If `F` is of finite type, then the
> diagonal is a closed immersion of finite presentation.
>
> The diagonal is that of the Quot presheaf of `Type (u + 1)` over the base, and being a closed
> immersion (of finite presentation) is representability by closed immersions of schemes (locally
> of finite presentation), read through `CategoryTheory.uliftYoneda`.

```lean
theorem diagonal_quotSitePresheafToBase :
    IsClosedImmersionULift.{u + 1} B S hS (pullback.diagonal D.quotSitePresheafToBase) ∧
      (SheafOfModules.IsFiniteTypeOnSite D.F →
        (closedImmersionFinitePresentation (B := B) (S := S) (hS := hS)).relative
          uliftYoneda.{u + 1} (pullback.diagonal D.quotSitePresheafToBase))
```

## Tag 0DM3, a lemma

[Tag 0DM3](https://stacks.math.columbia.edu/tag/0DM3) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.isLocallyOfFinitePresentationULift_quotSitePresheafToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorLocallyFinitePresentationOfLimits.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorLocallyFinitePresentationOfLimits.lean#L103). The attribute's comment: “the finite-presentation clause: if F is of finite presentation, Quot\_\{F/X/B} → B is locally of finite presentation”.

> If `F` is of finite presentation, then `Quot_{F/X/B} ⟶ B` is locally of finite presentation:
> the morphism of schemes underlying every commuting square of étale charts of the Quot presheaf over
> `B` is locally of finite presentation.

```lean
theorem isLocallyOfFinitePresentationULift_quotSitePresheafToBase
    (hF : D.F.IsFinitePresentationOnSite) :
    IsLocallyOfFinitePresentationULift.{u + 1} B S hS D.quotSitePresheafToBase
```

**`AlgebraicGeometry.Space.QuotSituation.isSeparatedULift_and_imp_isLocallyOfFinitePresentationULift_quotSitePresheafToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorLocallyFinitePresentationOfLimits.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorLocallyFinitePresentationOfLimits.lean#L112).

> The morphism `Quot_{F/X/B} ⟶ B` is separated, and if `F` is of finite presentation it is also
> locally of finite presentation.

```lean
theorem isSeparatedULift_and_imp_isLocallyOfFinitePresentationULift_quotSitePresheafToBase :
    IsSeparatedULift.{u + 1} B S hS D.quotSitePresheafToBase ∧
      (D.F.IsFinitePresentationOnSite →
        IsLocallyOfFinitePresentationULift.{u + 1} B S hS D.quotSitePresheafToBase)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.QuotSituation.isSeparatedULift_quotSitePresheafToBase`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorDiagonal.lean#L441), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorDiagonal.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorDiagonal.lean#L447) (StacksFrontier): “the separation clause: the diagonal of Quot over B is a closed immersion”.

## Tag 0DM4, a lemma

[Tag 0DM4](https://stacks.math.columbia.edu/tag/0DM4) in the Stacks Project.

**`StacksDraft.GenericFibre.existsUnique_submodule_flat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotValuativeAffineChart.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotValuativeAffineChart.lean#L210). The attribute's comment: “the affine-chart case: over a valuation ring a quotient of the generic fibre of a finite module extends uniquely to a quotient flat over the valuation ring and finite over the chart, the extension being the generic-kernel quotient and its flatness Stacks 0539; the etale gluing of Stacks 03M3, the proper support, and the finite presentation of Stacks 0DLR are not covered”. References: EGA IV (2.8.1.1), “special case”.

> **Stacks 0DM4, on an affine chart over a valuation ring.**  Let `R` be a valuation ring, `A`
> an `R`-algebra, `M` a finite `A`-module and `M_K` the generic fibre of `M`, that is, its
> localization at the nonzero elements of `R`.  Let `P` be the kernel of a prescribed quotient of
> `M_K`, an `A`-submodule saturated for the nonzero elements of `R`.  Then there is exactly one
> `A`-submodule `L` of `M` such that `M / L` is flat over `R` and finite over `A` and the generic
> fibre of `L` is `P`; it is the generic kernel `{x ∈ M | ι x ∈ P}`.

```lean
theorem existsUnique_submodule_flat_quotient [ValuationRing R] [Module.Finite A M]
    (hP : ∀ (s : R) {y : MK}, s ≠ 0 → s • y ∈ P → y ∈ P) :
    ∃! L : Submodule A M, (Module.Flat R (M ⧸ L) ∧ Module.Finite A (M ⧸ L)) ∧
      Submodule.localized₀ R⁰ (ι.restrictScalars R) (L.restrictScalars R)
        = P.restrictScalars R
```

**`AlgebraicGeometry.Space.QuotSitePresheafModel.valuativeCriterionExistence_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotValuativeExistence.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotValuativeExistence.lean#L397).

> Let `f : X ⟶ B` be a morphism of algebraic spaces which is proper and of finite
> presentation, and let `F` be a quasi-coherent `𝒪_X`-module of finite type.  Then
> `Quot_{F/X/B} ⟶ B` satisfies the existence part of the valuative criterion (Stacks 03IX): for
> every model of the Quot presheaf, its canonical morphism to `B` has it.  Here the Quot situation
> `D` (Stacks 09TR) records `f`, its finite presentation and the quasi-coherent module `F`.

```lean
theorem QuotSitePresheafModel.valuativeCriterionExistence_toBase (D : QuotSituation B S hS)
    (hproper : IsProper B S hS D.f.hom) (hF : SheafOfModules.IsFiniteTypeOnSite D.F)
    (N : QuotSitePresheafModel D) : ValuativeCriterion.Existence N.toBase
```

## Tag 0DP1, a lemma

[Tag 0DP1](https://stacks.math.columbia.edu/tag/0DP1) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotPushforwardSituation.pushforwardQuotFunctorMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAffinePushforward.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAffinePushforward.lean#L361).

> Let `B` be an algebraic space, let `π : X ⟶ Y` be an affine quasi-finite morphism of
> algebraic spaces which are separated and of finite presentation over `B`, and let `F` be a
> quasi-coherent `𝒪_X`-module.  Then `π_*` induces a morphism
> `Quot_{F/X/B} ⟶ Quot_{π_*F/Y/B}`: over a scheme `T` over `B` it sends a quotient `F_T ⟶ Q` to the
> quotient `(π_*F)_T ≅ π_{T,*}F_T ⟶ π_{T,*}Q`.

```lean
def pushforwardQuotFunctorMap :
    D.sourceSituation.quotFunctor ⟶ D.directImageSituation.quotFunctor
```

**`AlgebraicGeometry.Space.QuotPushforwardSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforward.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforward.lean#L130). The attribute's comment: “the standing data”.

> **Stacks 0DP1, the standing data.**  An affine quasi-finite morphism `π : X ⟶ Y` of algebraic
> spaces which are separated and of finite presentation over an algebraic space `B`, together with
> a quasi-coherent `𝒪_X`-module `F`: the data along which the direct image induces a morphism
> `Quot_{F/X/B} ⟶ Quot_{π_*F/Y/B}`.

```lean
structure QuotPushforwardSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

**`AlgebraicGeometry.Space.QuotPushforwardSituation.pushforwardQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforward.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforward.lean#L267). The attribute's comment: “the direct image of a quotient, recorded by its kernel”.

> **Stacks 0DP1, the direct image of a quotient.**  The quotient `G_T ⟶ π_{T,*}(F_T/K)` of
> `G_T` obtained from a quotient `F_T ⟶ F_T/K` by applying `π_{T,*}` and reading the result through
> the comparison `G_T ≅ π_{T,*}F_T`, recorded — as the quotients themselves are — by its kernel.

```lean
def pushforwardQuotient (h : SchemeTargetAffinePushforwardQuasicoherent B S hS)
    (c : PushforwardComparison D) (T : SchemesOver D.base)
    (K : Subobject (D.sourceSituation.baseChangeModule T)) :
    Subobject ((D.targetSituation h).baseChangeModule T)
```

**`AlgebraicGeometry.Space.QuotPushforwardSituation.pushforwardQuotient_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforward.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforward.lean#L325). The attribute's comment: “the direct image of a quotient of the Quot functor is one”.

> **Stacks 0DP1.**  The direct image of a quotient in `Quot_{F/X/B}(T)` lies in
> `Quot_{G/Y/B}(T)`: the quotient of `G_T` by it is `π_{T,*}(F_T/K)`, which is quasi-coherent, of
> finite presentation, flat over `T` and has support proper over `T` because `F_T/K` is, this being
> the morphism of stacks `Coh_{X/B} ⟶ Coh_{Y/B}` of Stacks 0DN9.

```lean
theorem pushforwardQuotient_mem (h : SchemeTargetAffinePushforwardQuasicoherent B S hS)
    (I : AffinePushforwardQuotInputs D h) (T : SchemesOver D.base)
    (K : Subobject (D.sourceSituation.baseChangeModule T))
    (hK : K ∈ D.sourceSituation.properlySupportedQuotients T) :
    D.pushforwardQuotient h I.comparison T K ∈
      (D.targetSituation h).properlySupportedQuotients T
```

**`AlgebraicGeometry.Space.QuotPushforwardSituation.quotFunctorMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforward.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforward.lean#L344). The attribute's comment: “the induced morphism of Quot functors”.

> **Stacks 0DP1.**  The morphism of Quot functors `Quot_{F/X/B} ⟶ Quot_{π_*F/Y/B}` induced by
> the direct image: over a test scheme it sends a quotient `F_T ⟶ Q` to `G_T ⟶ π_{T,*}Q`.
>
> Naturality is the compatibility of the direct image with pullback along a morphism of test
> schemes, part (b) of the proof of Stacks 0DN9.

```lean
def quotFunctorMap (h : SchemeTargetAffinePushforwardQuasicoherent B S hS)
    (I : AffinePushforwardQuotInputs D h) :
    D.sourceSituation.quotFunctor ⟶ (D.targetSituation h).quotFunctor
```

**`AlgebraicGeometry.Space.QuotPushforwardSituation.pushforwardQuotient'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforwardSupplement.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforwardSupplement.lean#L71). The attribute's comment: “the direct image of a quotient, recorded by its kernel”.

> **Stacks 0DP1, the direct image of a quotient.**  The quotient `G_T ⟶ π_{T,*}(F_T/K)` of
> `G_T` obtained from a quotient `F_T ⟶ F_T/K` by applying `π_{T,*}` and reading the result through
> the comparison `G_T ≅ π_{T,*}F_T`, recorded — as the quotients themselves are — by its kernel.

```lean
def pushforwardQuotient' (c : PushforwardComparison D) (T : SchemesOver D.base)
    (K : Subobject (D.sourceSituation.baseChangeModule T)) :
    Subobject (D.targetSituation'.baseChangeModule T)
```

**`AlgebraicGeometry.Space.QuotPushforwardSituation.pushforwardQuotient_mem'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforwardSupplement.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforwardSupplement.lean#L114). The attribute's comment: “the direct image of a quotient of the Quot functor is one”.

> **Stacks 0DP1.**  The direct image of a quotient in `Quot_{F/X/B}(T)` lies in
> `Quot_{G/Y/B}(T)`: the quotient of `G_T` by it is `π_{T,*}(F_T/K)`, which is quasi-coherent, of
> finite presentation, flat over `T` and has support proper over `T` because `F_T/K` is, this being
> the morphism of stacks `Coh_{X/B} ⟶ Coh_{Y/B}` of Stacks 0DN9.

```lean
theorem pushforwardQuotient_mem' (I : AffinePushforwardQuotInputs' D) (T : SchemesOver D.base)
    (K : Subobject (D.sourceSituation.baseChangeModule T))
    (hK : K ∈ D.sourceSituation.properlySupportedQuotients T) :
    D.pushforwardQuotient' I.comparison T K ∈
      D.targetSituation'.properlySupportedQuotients T
```

**`AlgebraicGeometry.Space.QuotPushforwardSituation.quotFunctorMap'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforwardSupplement.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPushforwardSupplement.lean#L132). The attribute's comment: “the induced morphism of Quot functors”.

> **Stacks 0DP1.**  The morphism of Quot functors `Quot_{F/X/B} ⟶ Quot_{π_*F/Y/B}` induced by
> the direct image: over a test scheme it sends a quotient `F_T ⟶ Q` to `G_T ⟶ π_{T,*}Q`.
>
> Naturality is the compatibility of the direct image with pullback along a morphism of test
> schemes, part (b) of the proof of Stacks 0DN9.

```lean
def quotFunctorMap' (I : AffinePushforwardQuotInputs' D) :
    D.sourceSituation.quotFunctor ⟶ D.targetSituation'.quotFunctor
```

## Tag 0DP2, a lemma

[Tag 0DP2](https://stacks.math.columbia.edu/tag/0DP2) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotPushforwardSituation.isOpenImmersion_pushforwardQuotModelMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAffineOpenImmersionDirectImage.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAffineOpenImmersionDirectImage.lean#L171).

> Let `B` be an algebraic space, let `π : X ⟶ Y` be an affine open immersion of algebraic spaces
> which are separated and of finite presentation over `B`, and let `F` be a quasi-coherent
> `𝒪_X`-module.  Then the morphism `Quot_{F/X/B} ⟶ Quot_{π_*F/Y/B}` of Stacks 0DP1 is an open
> immersion.
>
> The morphism is `AlgebraicGeometry.Space.QuotPushforwardSituation.pushforwardQuotFunctorMap`,
> read on the Quot presheaves of the site
> (`AlgebraicGeometry.Space.QuotPushforwardSituation.pushforwardQuotSitePresheafMap_app`) and then in
> their canonical models in the universe of the site, where being an open immersion of algebraic
> spaces is defined (Stacks 02YU).

```lean
theorem isOpenImmersion_pushforwardQuotModelMap (base X Y : AlgebraicSpaces B S hS)
    (π : X ⟶ Y) (structureX : X ⟶ base) (structureY : Y ⟶ base)
    (comp : π ≫ structureY = structureX) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (hπ : IsOpenImmersion B S hS π.hom)
    (haff : IsAffineHom B S hS π.hom) (hsepX : IsSeparated B S hS structureX.hom)
    (hsepY : IsSeparated B S hS structureY.hom)
    (hfpX : IsFinitePresentation B S hS structureX.hom)
    (hfpY : IsFinitePresentation B S hS structureY.hom) :
    IsOpenImmersion B S hS (ofAffineOpenImmersion base X Y π structureX structureY comp F hF hπ
      haff hsepX hsepY hfpX hfpY).pushforwardQuotModelMap
```

## Tag 0DP3, a lemma

[Tag 0DP3](https://stacks.math.columbia.edu/tag/0DP3) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotOpenImmersionSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenImmersionDirectImage.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenImmersionDirectImage.lean#L101). The attribute's comment: “the standing data”.

> **Stacks 0DP3, the standing data.**  An open immersion `j : X ⟶ Y` of algebraic spaces which
> are separated and of finite presentation over an algebraic space `B`, together with a
> quasi-coherent `𝒪_Y`-module `G`: the data along which the direct image induces a morphism
> `Quot_{j^*G/X/B} ⟶ Quot_{G/Y/B}`.

```lean
structure QuotOpenImmersionSituation (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
```

**`AlgebraicGeometry.Space.QuotOpenImmersionSituation.directImageQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenImmersionDirectImage.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenImmersionDirectImage.lean#L254). The attribute's comment: “the direct image of a quotient, recorded by its kernel”.

> **Stacks 0DP3, the direct image of a quotient.**  The quotient `G_T ⟶ j_{T,*}(F_T/K)` of
> `G_T`, recorded — as the quotients themselves are — by its kernel.

```lean
def directImageQuotient (ν : DirectImageInputs D) (T : SchemesOver D.base)
    (K : Subobject (D.sourceSituation.baseChangeModule T)) :
    Subobject (D.targetSituation.baseChangeModule T)
```

**`AlgebraicGeometry.Space.QuotOpenImmersionSituation.directImageQuotient_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenImmersionDirectImage.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenImmersionDirectImage.lean#L302). The attribute's comment: “the direct image of a quotient of the Quot functor is one”.

> **Stacks 0DP3.**  The direct image of a quotient in `Quot_{F/X/B}(T)` lies in
> `Quot_{G/Y/B}(T)`: the quotient of `G_T` by it is `j_{T,*}(F_T/K)`, which is quasi-coherent, of
> finite presentation, flat over `T` and has support proper over `T` because `F_T/K` is, this being
> the morphism of stacks `Coh_{X/B} ⟶ Coh_{Y/B}` of Stacks 0DN9.

```lean
theorem directImageQuotient_mem (I : QuotDirectImageInputs D) (T : SchemesOver D.base)
    (K : Subobject (D.sourceSituation.baseChangeModule T))
    (hK : K ∈ D.sourceSituation.properlySupportedQuotients T) :
    D.directImageQuotient I.projections T K ∈
      D.targetSituation.properlySupportedQuotients T
```

**`AlgebraicGeometry.Space.QuotOpenImmersionSituation.quotFunctorMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenImmersionDirectImage.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenImmersionDirectImage.lean#L322). The attribute's comment: “the morphism of Quot functors the source constructs, not its being open”.

> **Stacks 0DP3, the morphism of Quot functors.**  The morphism
> `Quot_{F/X/B} ⟶ Quot_{G/Y/B}` induced by the direct image: over a test scheme it sends a quotient
> `F_T ⟶ Q` to `G_T ⟶ j_{T,*}Q`.  This is the morphism the source constructs; that it is an open
> immersion is the half of the statement whose proof the source omits, and is not proved here.
>
> Naturality is the compatibility of the direct image with pullback along a morphism of test
> schemes, part (b) of the proof of Stacks 0DN9.

```lean
def quotFunctorMap (I : QuotDirectImageInputs D) :
    D.sourceSituation.quotFunctor ⟶ D.targetSituation.quotFunctor
```

**`AlgebraicGeometry.Space.QuotOpenSubspaceSituation.isOpenImmersion_quotSitePresheafModelMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenSubspace.lean, line 847](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenSubspace.lean#L847).

> Let `B` be an algebraic space, let `j : X ⟶ Y` be an open immersion of algebraic spaces which
> are separated and of finite presentation over `B`, let `G` be a quasi-coherent `𝒪_Y`-module and set
> `F = j^*G`.  Then the morphism `Quot_{F/X/B} ⟶ Quot_{G/Y/B}`, sending a quotient `F_T ⟶ Q` to
> `G_T ⟶ j_{T,*}Q`, is an open immersion of spaces over `B`.
>
> The Quot functors are read in their canonical models in the universe of the site
> (`AlgebraicGeometry.Space.QuotSituation.quotSitePresheafModel`); for arbitrary models this is
> `AlgebraicGeometry.Space.QuotOpenSubspaceSituation.isOpenImmersion_quotModelMap`.

```lean
theorem isOpenImmersion_quotSitePresheafModelMap :
    IsOpenImmersion B S hS
        (D.quotModelMap D.sourceSituation.quotSitePresheafModel
          D.targetSituation.quotSitePresheafModel) ∧
      D.quotModelMap D.sourceSituation.quotSitePresheafModel
          D.targetSituation.quotSitePresheafModel ≫ D.targetSituation.quotSitePresheafModel.toBase =
        D.sourceSituation.quotSitePresheafModel.toBase
```

**`AlgebraicGeometry.Space.QuotOpenSubspaceSituation.isOpenImmersion_quotSitePresheafModelMap_ofOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenSubspace.lean, line 901](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorOpenSubspace.lean#L901).

> Let `B` be an algebraic space, let `j : X ⟶ Y` be an open immersion of algebraic spaces which
> are separated and of finite presentation over `B`, let `G` be a quasi-coherent `𝒪_Y`-module and set
> `F = j^*G`.  Then the morphism `Quot_{F/X/B} ⟶ Quot_{G/Y/B}`, sending a quotient `F_T ⟶ Q` to
> `G_T ⟶ j_{T,*}Q`, is an open immersion of spaces over `B`.
>
> The situation `D` is assembled from the hypotheses by
> `AlgebraicGeometry.Space.QuotOpenSubspaceSituation.ofOpenImmersion`.  Its source Quot situation
> `D.sourceSituation` is `F/X/B` of Stacks 09TR with `F = (modulePullback B S hS j).obj G`, the
> inverse image `j^*G` (quasi-coherent by Stacks 03GA), and its target Quot situation
> `D.targetSituation` is `G/Y/B`.  The Quot functors are read in their canonical models in the
> universe of the site (`AlgebraicGeometry.Space.QuotSituation.quotSitePresheafModel`), where being
> an open immersion of algebraic spaces is defined (Stacks 02YU); for arbitrary models this is
> `AlgebraicGeometry.Space.QuotOpenSubspaceSituation.isOpenImmersion_quotModelMap`.  Over a test
> scheme the morphism takes a quotient to its direct image
> (`AlgebraicGeometry.Space.QuotOpenSubspaceSituation.familyEquiv_quotModelMap`), and the second
> conjunct says it is a morphism over `B`.

```lean
theorem isOpenImmersion_quotSitePresheafModelMap_ofOpenImmersion
    (base X Y : AlgebraicSpaces B S hS) (j : X ⟶ Y)
    (structureX : X ⟶ base) (structureY : Y ⟶ base) (comp : j ≫ structureY = structureX)
    (G : Modules.{u, u} B S hS Y.1 Y.2) (quasicoherent : G.IsQuasicoherentOnSite)
    (openImmersion : IsOpenImmersion B S hS j.hom)
    (separatedX : IsSeparated B S hS structureX.hom)
    (separatedY : IsSeparated B S hS structureY.hom)
    (finitePresentationX : IsFinitePresentation B S hS structureX.hom)
    (finitePresentationY : IsFinitePresentation B S hS structureY.hom) :
    let D := ofOpenImmersion base X Y j structureX structureY comp G quasicoherent openImmersion
      separatedX separatedY finitePresentationX finitePresentationY
    D.sourceSituation.F = (modulePullback B S hS j).obj G ∧
      IsOpenImmersion B S hS D.quotSitePresheafModelMap ∧
      D.quotSitePresheafModelMap ≫ D.targetSituation.quotSitePresheafModel.toBase =
        D.sourceSituation.quotSitePresheafModel.toBase
```

## Tag 0DP4, a lemma

[Tag 0DP4](https://stacks.math.columbia.edu/tag/0DP4) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotPushforwardSituation.isIso_pushforwardQuotFunctorMap_ofIsClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorClosedImmersionDirectImageIso.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorClosedImmersionDirectImageIso.lean#L103).

> Let `B` be an algebraic space, let `π : X ⟶ Y` be a closed immersion of algebraic spaces
> which are separated and of finite presentation over `B`, and let `F` be a quasi-coherent
> `𝒪_X`-module. Then the morphism `Quot_{F/X/B} ⟶ Quot_{π_*F/Y/B}` of Stacks 0DP1 is an
> isomorphism.

```lean
theorem isIso_pushforwardQuotFunctorMap_ofIsClosedImmersion (base X Y : AlgebraicSpaces B S hS)
    (π : X ⟶ Y) (hπ : IsClosedImmersion B S hS π.hom) (structureX : X ⟶ base)
    (structureY : Y ⟶ base) (comp : π ≫ structureY = structureX)
    (F : Modules.{u, u} B S hS X.1 X.2) (quasicoherent : F.IsQuasicoherentOnSite)
    (separatedX : IsSeparated B S hS structureX.hom)
    (separatedY : IsSeparated B S hS structureY.hom)
    (finitePresentationX : IsFinitePresentation B S hS structureX.hom)
    (finitePresentationY : IsFinitePresentation B S hS structureY.hom) :
    IsIso (ofIsClosedImmersion base X Y π hπ structureX structureY comp F quasicoherent
      separatedX separatedY finitePresentationX finitePresentationY).pushforwardQuotFunctorMap
```

**`AlgebraicGeometry.Space.QuotPushforwardSituation.isIso_quotFunctorMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorClosedImmersionPushforward.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorClosedImmersionPushforward.lean#L190). The attribute's comment: “an isomorphism, granted 04CJ (3) essential image and 0DN9 reversed”.

> **Stacks 0DP4.**  The morphism of Quot functors `Quot_{F/X/B} ⟶ Quot_{π_*F/Y/B}` induced by
> the direct image along a closed immersion is an isomorphism: over every test scheme it is a
> bijection, injectively by full faithfulness of `π_{T,*}` (Stacks 04CJ) and surjectively by the
> two carried inputs.

```lean
theorem isIso_quotFunctorMap (h : SchemeTargetAffinePushforwardQuasicoherent B S hS)
    (I : D.AffinePushforwardQuotInputs h) (J : D.ClosedImmersionQuotInputs h)
    (hπ : IsClosedImmersion B S hS D.π.hom) :
    IsIso (D.quotFunctorMap h I)
```

## Tag 0DP5, a lemma

[Tag 0DP5](https://stacks.math.columbia.edu/tag/0DP5) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.relative_closedImmersionOver_quotientInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorSurjection.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorSurjection.lean#L380).

> Let `φ : F ⟶ G` be a surjection of quasi-coherent `𝒪_X`-modules. The canonical transformation
> `Quot_{G/X/B} ⟶ Quot_{F/X/B}` of functors on the test schemes over `B`, sending a quotient
> `G_T ⟶ Q` to the quotient `F_T ⟶ G_T ⟶ Q`, is a closed immersion: it is representable by closed
> immersions of test schemes.
>
> The Quot functors take values in `Type (u + 1)`, so representability is read through
> `CategoryTheory.uliftYoneda`.

```lean
theorem relative_closedImmersionOver_quotientInclusion :
    D.closedImmersionOver.relative uliftYoneda.{u + 1} (D.quotientInclusion (hG := hG) φ)
```

## Tag 0DP6, a remark

[Tag 0DP6](https://stacks.math.columbia.edu/tag/0DP6) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.numericalQuot`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalFibreProduct.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalFibreProduct.lean#L164). The attribute's comment: “the fibre product Quot^P = Quot\_\{F/X/B} ×\_\{Coh\_\{X/B}} Coh^P\_\{X/B}, as the 2-fibre product over the site of Stacks 0040 of the morphism Quot ⟶ Coh and the inclusion Coh^P ⟶ Coh”.

> **The fibre product `Quot^P_{F/X/B} = Quot_{F/X/B} ×_{Coh_{X/B}} Coh^P_{X/B}`**, as a category
> over the big fppf site of `S`: an object over a scheme `U` is a member `F_T ⟶ 𝒬` of
> `Quot_{F/X/B}` over `U`, an object of `Coh^P_{X/B}` over `U` and a vertical isomorphism of their
> images in `Coh_{X/B}`.

```lean
def numericalQuot : BasedCategory.{u + 1, u + 1} (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Space.QuotSituation.numericalQuotSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean#L105). The attribute's comment: “Quot^P\_\{F/X/B} as the subfunctor of Quot\_\{F/X/B} of the quotients whose object of Coh\_\{X/B} lies in Coh^P\_\{X/B}; it is the fibre product numericalQuot by mem\_numericalQuotSubspace\_iff\_exists\_numericalQuot”.

> **`Quot^P_{F/X/B}`**, as the subfunctor of the Quot presheaf it is: the
> quotients `F_T ⟶ 𝒬` whose object `(T, 𝒬)` of `Coh_{X/B}` has `χ(K_i ⊗^𝐋 κ(t)) = P(i)` for all
> `i ∈ I` and `t ∈ |T|`, where `K_i = Rf_{T,*}(E_{i,T} ⊗^𝐋 𝒬)`.  It is a subfunctor because the
> numerical invariants are compatible with pullback
> (`AlgebraicGeometry.Space.NumericalSituation.numericalEuler_eq_of_hom`, from Stacks 0A1P).

```lean
def numericalQuotSubspace : Subfunctor D.quotSitePresheaf
```

**`AlgebraicGeometry.Space.QuotSituation.numericalQuotToQuot_fullyFaithful_and_mem_numericalQuotSubspace_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean#L123). The attribute's comment: “the fibre product Quot\_\{F/X/B} x\_\{Coh\_\{X/B}} Coh^P\_\{X/B} is the subfunctor numericalQuotSubspace: the left vertical arrow is fully faithful with that essential image”.

> The fibre product
> `Quot^P_{F/X/B} = Quot_{F/X/B} ×_{Coh_{X/B}} Coh^P_{X/B}` of the remark
> (`AlgebraicGeometry.Space.QuotSituation.numericalQuot`) is the subfunctor
> `AlgebraicGeometry.Space.QuotSituation.numericalQuotSubspace` of `Quot_{F/X/B}`: its projection to
> `Quot_{F/X/B}` is fully faithful, and a quotient `F_T ⟶ 𝒬` lifts to it exactly when it lies in
> the subfunctor.

```lean
theorem numericalQuotToQuot_fullyFaithful_and_mem_numericalQuotSubspace_iff :
    (D.numericalQuotToQuot N).toFunctor.Full ∧ (D.numericalQuotToQuot N).toFunctor.Faithful ∧
      ∀ {T : (BigFppfOver B S hS)ᵒᵖ} (x : D.quotSitePresheaf.obj T),
        x ∈ (D.numericalQuotSubspace N).obj T ↔
          ∃ P : D.NumericalQuotObjects N, P.x = QuotFamilyOver.toQuotObjects x
```

**`AlgebraicGeometry.Space.QuotSituation.relative_closedImmersion_flat_numericalQuotSubspace_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean#L137). The attribute's comment: “the left vertical arrow Quot^P -> Quot is a flat closed immersion”.

> **`Quot^P_{F/X/B} ⟶ Quot_{F/X/B}` is a flat closed immersion**: its base change
> to every scheme of the site is a flat closed immersion.  It is the base change of the flat closed
> immersion `Coh^P_{X/B} ⟶ Coh_{X/B}` of Lemma 0DND, the functions `χ_i` being compatible with
> pullback and locally constant (Stacks 0A1P, 0D1Z).

```lean
theorem relative_closedImmersion_flat_numericalQuotSubspace_ι :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsClosedImmersion.{u} ⊓ @Flat.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative uliftYoneda.{u + 1}
        (D.numericalQuotSubspace N).ι
```

**`AlgebraicGeometry.Space.QuotSituation.relative_openImmersion_closedImmersion_numericalQuotSubspace_ι_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean#L149). The attribute's comment: “the left vertical arrow is an open and closed immersion if I is finite”.

> **For a finite index set, `Quot^P_{F/X/B} ⟶ Quot_{F/X/B}` is an open and closed
> immersion.**

```lean
theorem relative_openImmersion_closedImmersion_numericalQuotSubspace_ι_of_finite [Finite N.I] :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsOpenImmersion.{u} ⊓
        @_root_.AlgebraicGeometry.IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative uliftYoneda.{u + 1}
        (D.numericalQuotSubspace N).ι
```

**`AlgebraicGeometry.Space.QuotSituation.relative_openImmersion_closedImmersion_numericalQuotSubspace_ι_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean#L164). The attribute's comment: “the left vertical arrow is an open and closed immersion if B is locally Noetherian”.

> **For `B` locally Noetherian, `Quot^P_{F/X/B} ⟶ Quot_{F/X/B}` is an open and
> closed immersion**, however large the index set: every object of `Coh_{X/B}` is étale locally
> pulled back from one over a Noetherian test scheme, on which the locus where every `χ_i` takes
> its prescribed value is an intersection of unions of connected components, hence open.

```lean
theorem relative_openImmersion_closedImmersion_numericalQuotSubspace_ι_of_isLocallyNoetherian
    (hB : IsLocallyNoetherian B S hS D.Y.1) :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsOpenImmersion.{u} ⊓
        @_root_.AlgebraicGeometry.IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative uliftYoneda.{u + 1}
        (D.numericalQuotSubspace N).ι
```

**`AlgebraicGeometry.Space.QuotSituation.isAlgebraicSpace_subfunctorModel_numericalQuotSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean#L183). The attribute's comment: “Quot^P\_\{F/X/B} is an algebraic space, for F etale-locally generated by fewer than mu sections with mu below the cutoff of the site (every F of finite type)”.

> **`Quot^P_{F/X/B}` is an algebraic space**, for `F` étale-locally generated by
> fewer than `μ` sections with `μ` below the cutoff of the site (for instance `F` of finite type):
> every model of `Quot^P_{F/X/B}` in the universe of the site is an algebraic space.  It maps to a
> model of `Quot_{F/X/B}`, an algebraic space by Stacks 09TU, by a flat closed immersion.  For an
> arbitrary quasi-coherent `F` the assertion fails on the size-bounded site.

```lean
theorem isAlgebraicSpace_subfunctorModel_numericalQuotSubspace
    (hF : ∃ μ < B.cutoff, IsEtaleLocallyGeneratedBelow B S hS μ D.F)
    (F : D.SubfunctorModel (D.numericalQuotSubspace N)) : IsAlgebraicSpace B S hS F.presheaf
```

**`AlgebraicGeometry.Space.QuotSituation.relative_openImmersion_closedImmersion_hilbertPolynomialQuot_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotNumericalSubspace.lean#L206). The attribute's comment: “the left vertical arrow is an open and closed immersion if I = Z and E\_i = L^\{(x) i} for an invertible L; this is Quot^\{P,L}, cut out by P(n) = chi(X\_t, Q\_t (x) L\_t^n)”.

> **For `I = ℤ` and `E_i = 𝓛^{⊗ i}`, `Quot^{P, 𝓛}_{F/X/B} ⟶ Quot_{F/X/B}` is an open and
> closed immersion.**  For an invertible `𝒪_X`-module `𝓛` and `P : ℤ → ℤ`, the subfunctor
> `Quot^{P, 𝓛}_{F/X/B}` of the quotients `F_T ⟶ 𝒬` with `P(n) = χ(X_t, 𝒬_t ⊗ 𝓛_t^{⊗ n})` for all
> `n ∈ ℤ` and `t ∈ |T|` (`AlgebraicGeometry.Space.QuotSituation.hilbertPolynomialQuot`, the
> condition of Example 0DNF) is an open and closed subfunctor: it is the base change of the open and
> closed substack `Coh^{P, 𝓛}_{X/B}`.

```lean
theorem relative_openImmersion_closedImmersion_hilbertPolynomialQuot_ι (P : ℤ → ℤ) :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsOpenImmersion.{u} ⊓
        @_root_.AlgebraicGeometry.IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative uliftYoneda.{u + 1}
        (D.hilbertPolynomialQuot L P).ι
```

**`AlgebraicGeometry.Space.QuotSituation.cohObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotToCoherentStack.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotToCoherentStack.lean#L289). The attribute's comment: “the object part of the morphism Quot\_\{F/X/B} ⟶ Coh\_\{X/B}: a quotient F\_T ⟶ Q in Quot\_\{F/X/B}(T) goes to the object Q of Coh\_\{X/B} over T. The action on morphisms of test schemes is `AlgebraicGeometry.Space.QuotSituation.cohHom`. The functor laws hold for the OBJECT part (`cohObject_quotientPullback_id`, `cohObject_quotientPullback_comp`) but are NOT established for the module comparisons, Coh\_\{X/B} not being a category in this development; and the fibre product Quot^P = Quot ×\_\{Coh} Coh^P of the remark is NOT formed: Coh^P\_\{X/B} is not constructed anywhere in this development, only the standing data of Situation 0DNC. See the module docstring for the full accounting”.

> **Stacks 0DP6, the object part of the morphism `Quot_{F/X/B} ⟶ Coh_{X/B}`.**  A `T`-point
> `F_T ⟶ 𝒬` of the Quot functor, recorded by its kernel `K`, goes to the object `(T, F_T/K)` of
> `Coh_{X/B}`: the four conditions an object of `Coh_{X/B}` over `T` satisfies — quasi-coherence,
> finite presentation, flatness over `T` and proper support over `T` — are the four conditions
> cutting `Quot_{F/X/B}(T)` out of the subobjects of `F_T`.

```lean
def cohObject (T : SchemesOver D.Y) (K : Subobject (D.baseChangeModule T))
    (hK : K ∈ D.properlySupportedQuotients T) : CoherentObject D.toCoherentSituation
```

**`AlgebraicGeometry.Space.QuotSituation.cohHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotToCoherentStack.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotToCoherentStack.lean#L313). The attribute's comment: “the action of the morphism Quot\_\{F/X/B} ⟶ Coh\_\{X/B} on morphisms of test schemes, whose object part is `AlgebraicGeometry.Space.QuotSituation.cohObject`: the base map is h itself, so the morphism lies over the identity of the schemes over B, and the module comparison is the one of Tag 03LU identifying the inverse image of F\_T/K with the quotient of F\_\{T'} by the pulled-back kernel. No hypothesis is carried: the preservation under inverse image of finite presentation (Properties of Spaces, Section 05VR) is the theorem `AlgebraicGeometry.Space.QuotientSituation.pullbackPreservesFinitePresentation`. The functor laws for the module comparisons are NOT established and the fibre product Quot^P of the remark is NOT formed; see the module docstring”.

> **Stacks 0DP6, the action of the morphism `Quot_{F/X/B} ⟶ Coh_{X/B}` on morphisms of test
> schemes.**  A morphism `h : T' ⟶ T` of test schemes over `B` and a member `K` of
> `Quot_{F/X/B}(T)` give a morphism of `Coh_{X/B}` from the object attached to the inverse image
> of `K` to the object attached to `K`: its base map is `h` itself, and its module comparison is
> the identification of the inverse image of `F_T/K` with the quotient of `F_{T'}` by the
> pulled-back kernel.

```lean
def cohHom {T' T : SchemesOver D.Y}
    (h : T' ⟶ T)
    {K : Subobject (D.baseChangeModule T)} (hK : K ∈ D.properlySupportedQuotients T) :
    CoherentHom
      (D.cohObject T' (D.quotientPullback h K)
        (D.quotientPullback_mem_properlySupportedQuotients h K hK))
      (D.cohObject T K hK)
```

**`AlgebraicGeometry.Space.QuotSituation.quotToCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotToCoherentStackFunctor.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotToCoherentStackFunctor.lean#L308). The attribute's comment: “the morphism Quot\_\{F/X/B} ⟶ Coh\_\{X/B} sending F\_T ⟶ Q to the object Q over T, as a 1-morphism of categories over the big fppf site (functor laws included)”.

> **Stacks 0DP6, the morphism `Quot_{F/X/B} ⟶ Coh_{X/B}`.**  The rule sending an element
> `F_T ⟶ 𝒬` of `Quot_{F/X/B}(T)` to the object `𝒬` of `Coh_{X/B}` over `T`, and a morphism of test
> schemes along which one quotient pulls back to another to the morphism of `Coh_{X/B}` with that
> base map identifying the inverse image of the one quotient with the other, is a 1-morphism of
> categories over the big fppf site: it respects identities and composition, by the coherences of
> the comparisons of inverse images of Stacks 03LU, and it does not change the underlying test
> scheme.

```lean
def quotToCoherent :
    D.quotBasedCategory ⥤ᵇ coherentBasedCategory D.toCoherentSituation.categoryData
```

## Tag 0DP7, a lemma

[Tag 0DP7](https://stacks.math.columbia.edu/tag/0DP7) in the Stacks Project.

**`AlgebraicGeometry.Space.isPrescribedTwistedEuler_iff_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariantsTwist.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariantsTwist.lean#L289). The attribute's comment: “the final statement at the level of membership conditions: the condition for `P` and `𝓕` is the condition for `P'(t) = P(t + 1)` and `𝓕 ⊗ L`. The isomorphism `Quot_{𝓕/X/B} ⟶ Quot_{𝓕 ⊗ L/X/B}` itself is not constructed”.

> **Stacks 0DP7, the final statement, at the level of membership conditions.**  Tensoring with
> an invertible module `L` replaces the twisted Euler characteristics `n ↦ χ(X_t, 𝓕_t ⊗ L_t^{⊗ n})`
> of `𝓕` by their shift `n ↦ χ(X_t, 𝓕_t ⊗ L_t^{⊗ (n + 1)})`, which is the hypothesis `twist`.  The
> condition cutting out `Quot^P_{𝓕/X/B}` is then the condition cutting out
> `Quot^{P'}_{𝓕 ⊗ L/X/B}` for `P'(t) = P(t + 1)`.
>
> The isomorphism `Quot_{𝓕/X/B} ⟶ Quot_{𝓕 ⊗ L/X/B}` of the first statement of the source is not
> constructed here, and neither are the two open and closed substacks it is claimed to restrict
> to.

```lean
theorem isPrescribedTwistedEuler_iff_shift {ι : Type v} {P : ℤ → ℤ} {χ χ' : ι → ℤ → ℤ}
    (twist : ∀ (t : ι) (m : ℤ), χ' t m = χ t (m + 1)) :
    IsPrescribedTwistedEuler P χ ↔ IsPrescribedTwistedEuler (fun m => P (m + 1)) χ'
```

**`AlgebraicGeometry.Space.QuotSituation.quotSitePresheafTensorInvertibleIso_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorTensorInvertible.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorTensorInvertible.lean#L553). The attribute's comment: “the isomorphism `Quot_{F/X/B} ≅ Quot_{F ⊗ L/X/B}` given by tensoring with `L`, and its restriction to `Quot^P ≅ Quot^{P'}` for `P'(t) = P(t + 1)`, membership read on the actual twisted Euler characteristics `χ(X_t, Q_t ⊗ L_t^{⊗ n})`”.

> **Stacks 0DP7.**  Let `f : X ⟶ B` be a morphism of algebraic spaces of finite presentation,
> `F` a quasi-coherent `𝒪_X`-module and `L` an invertible `𝒪_X`-module.  Tensoring with `L` is an
> isomorphism of Quot functors
> `AlgebraicGeometry.Space.QuotSituation.quotSitePresheafTensorInvertibleIso :
> Quot\_\{F/X/B} ≅ Quot\_\{F ⊗ L/X/B}`; precisely:
>
> * it lies over `B`;
> * it sends a quotient `F_T ⟶ Q` over `T` to a quotient of `(F ⊗ L)_T` with quotient module
>   `Q ⊗ L_T`;
> * for every `P : ℤ → ℤ` it carries `Quot^P_{F/X/B}` onto `Quot^{P'}_{F ⊗ L/X/B}`, where
>   `P'(n) = P(n + 1)`: a quotient lies in `Quot^P_{F/X/B}` exactly when its image lies in
>   `Quot^{P'}_{F ⊗ L/X/B}`, membership being that the object of `Coh_{X/B}` the quotient gives has
>   Hilbert polynomial `P`, respectively `P'`, with respect to `L` (Stacks 0DNF).

```lean
theorem quotSitePresheafTensorInvertibleIso_spec :
    (D.quotSitePresheafTensorInvertibleIso L).hom ≫
        (D.tensorInvertible L).quotSitePresheafToBase = D.quotSitePresheafToBase ∧
      (∀ {T : (BigFppfOver B S hS)ᵒᵖ} (x : D.quotSitePresheaf.obj T),
        Nonempty ((D.tensorInvertible L).quotientModule _
            ((D.quotSitePresheafTensorInvertibleIso L).hom.app T x).subobject ≅
          moduleTensor B S hS (D.space _) (D.quotientModule _ x.subobject)
            (D.baseChangeInvertible L _))) ∧
      ∀ (P : ℤ → ℤ) {T : (BigFppfOver B S hS)ᵒᵖ} (x : D.quotSitePresheaf.obj T),
        letI : Stacks.SheafOfModules.IsInvertible
            (structurePresheaf B S hS (D.tensorInvertible L).toCoherentSituation.X.1)
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS
              (D.tensorInvertible L).toCoherentSituation.X.1
              (D.tensorInvertible L).toCoherentSituation.X.2).O)).property L := hL
        letI : Stacks.SheafOfModules.IsInvertible
            (structurePresheaf B S hS D.toCoherentSituation.X.1)
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS
              D.toCoherentSituation.X.1 D.toCoherentSituation.X.2).O)).property L := hL
        (((D.quotSitePresheafTensorInvertibleIso L).hom.app T x).cohObject.HasHilbertPolynomial L
            (fun n ↦ P (n + 1)) ↔
          x.cohObject.HasHilbertPolynomial L P)
```

## Tag 0DP8, a lemma

[Tag 0DP8](https://stacks.math.columbia.edu/tag/0DP8) in the Stacks Project.

**`AlgebraicGeometry.Space.isPrescribedTwistedEuler_iff_reindexMul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariantsTwist.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/NumericalInvariantsTwist.lean#L307). The attribute's comment: “the equality `Quot^{P,L} = Quot^{P',L^{⊗ n}}` with `P'(t) = P(n t)`, read on the two membership conditions, for `n ≠ 0` and numerical-polynomial invariants; the substacks themselves are not constructed in this development”.

> **Stacks 0DP8, at the level of membership conditions.**  Replacing `L` by `L^{⊗ n}` replaces
> the twisted Euler characteristics `m ↦ χ(X_t, 𝓕_t ⊗ L_t^{⊗ m})` by `m ↦ χ(X_t, 𝓕_t ⊗ L_t^{⊗ n m})`,
> which is the hypothesis `twist`.  For `n ≠ 0` the condition cutting out `Quot^{P,L}_{𝓕/X/B}` is
> then the condition cutting out `Quot^{P',L^{⊗ n}}_{𝓕/X/B}` for `P'(t) = P(n t)`: this is the
> source's equality of the two substacks, read on their defining conditions.
>
> The hypotheses `hP` and `hχ` say that `P` and each `χ t` are numerical polynomials, represented by
> the rational polynomials `p` and `q t`.  They are not removable: for a general `P` the right-hand
> condition constrains only the values of `P` at the multiples of `n`.

```lean
theorem isPrescribedTwistedEuler_iff_reindexMul {ι : Type v} {P : ℤ → ℤ} {χ χ' : ι → ℤ → ℤ}
    {p : Polynomial ℚ} {q : ι → Polynomial ℚ}
    (hP : ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ))
    (hχ : ∀ (t : ι) (m : ℤ), (q t).eval (m : ℚ) = (χ t m : ℚ))
    {n : ℤ} (hn : n ≠ 0) (twist : ∀ (t : ι) (m : ℤ), χ' t m = χ t (n * m)) :
    IsPrescribedTwistedEuler P χ ↔ IsPrescribedTwistedEuler (fun m => P (n * m)) χ'
```

**`AlgebraicGeometry.Space.QuotSituation.setOf_hasHilbertPolynomial_invertibleTensorPower_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorTensorPowerReindex.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorTensorPowerReindex.lean#L106). The attribute's comment: “the equality `Quot^{P,L} = Quot^{P',L^{⊗ n}}` with `P'(t) = P(n t)`, for `n ≠ 0` and `P` a numerical polynomial, compared on the sections over every scheme of the site, membership read on the actual twisted Euler characteristics `χ(X_t, Q_t ⊗ L_t^{⊗ m})`”.

> Let `f : X ⟶ B` be a morphism of algebraic spaces of finite presentation, `F` a
> quasi-coherent `𝒪_X`-module, `L` an invertible `𝒪_X`-module, `P : ℤ → ℤ` a numerical polynomial
> (at every integer, the value of a rational polynomial) and `n` a nonzero integer.  Then
>
> `Quot^{P, L}_{F/X/B} = Quot^{P', L^{⊗ n}}_{F/X/B}`,  where `P'(t) = P(n t)`:
>
> over every scheme `T` of the site, a quotient `F_T ⟶ Q` in `Quot_{F/X/B}(T)` satisfies
> `P(m) = χ(X_t, Q_t ⊗ L_t^{⊗ m})` for all `t ∈ T` and `m ∈ ℤ` exactly when it satisfies
> `P(n m) = χ(X_t, Q_t ⊗ (L^{⊗ n})_t^{⊗ m})` for all `t ∈ T` and `m ∈ ℤ`, these being the twisted
> Euler characteristics `AlgebraicGeometry.Space.CoherentObject.twistedEuler` of the object of
> `Coh_{X/B}` the quotient gives.

```lean
theorem setOf_hasHilbertPolynomial_invertibleTensorPower_eq {P : ℤ → ℤ}
    (hP : ∃ p : Polynomial ℚ, ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ)) {n : ℤ} (hn : n ≠ 0)
    (T : (BigFppfOver B S hS)ᵒᵖ) :
    letI : Stacks.SheafOfModules.IsInvertible
        (structurePresheaf B S hS D.toCoherentSituation.X.1)
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS
          D.toCoherentSituation.X.1 D.toCoherentSituation.X.2).O)).property L := hL
    letI := isInvertible_invertibleTensorPower B S hS D.toCoherentSituation.X.1
      D.toCoherentSituation.X.2 L n
    {x : D.quotSitePresheaf.obj T | x.cohObject.HasHilbertPolynomial L P} =
      {x : D.quotSitePresheaf.obj T | x.cohObject.HasHilbertPolynomial
        (invertibleTensorPower B S hS D.toCoherentSituation.X.1 D.toCoherentSituation.X.2 L n)
        (fun m => P (n * m))}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.5, Tag 0DM1](https://stacks.math.columbia.edu/tag/0DM1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
