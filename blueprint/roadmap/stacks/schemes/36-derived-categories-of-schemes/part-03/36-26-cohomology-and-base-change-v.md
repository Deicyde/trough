---
declaration: section
origin: cited
lean: AlgebraicGeometry.baseChangeCohomologyMap, AlgebraicGeometry.BaseChangeChart, AlgebraicGeometry.BaseChangeChart.isOpenImmersion_incU', AlgebraicGeometry.BaseChangeChart.ofAffineOpens, AlgebraicGeometry.exists_baseChangeChart_covering, AlgebraicGeometry.exists_coveringFamily_of_forall_baseChangeChart, AlgebraicGeometry.BaseChangeChart.cohomologyComparison, AlgebraicGeometry.BaseChangeChart.cohomologyComparison_tmul_one
statement: formalized
proof: formalized
---

# 36.26 Cohomology and base change, V

Section 36.26 of the Stacks Project, [Tag 0DJ6](https://stacks.math.columbia.edu/tag/0DJ6). 6 tags here are carried by 35 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DJ7, an equation

[Tag 0DJ7](https://stacks.math.columbia.edu/tag/0DJ7) in the Stacks Project.

**`AlgebraicGeometry.baseChangeCohomologyMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/StalkCohomologyMap.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/StalkCohomologyMap.lean#L106).

> **Stacks 0DJ7.** The canonical pointwise base-change map on stalkwise cohomology induced by
> a morphism `φ : L(g')^* K ⟶ K'` over a commutative square of schemes. No flatness,
> cartesianness or Tor independence is required.

```lean
def baseChangeCohomologyMap {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S)
    (f' : X' ⟶ S') (g' : X' ⟶ X) (w : g' ≫ f = f' ≫ g)
    [HasDerivedCategory.{w'} X.Modules] [HasDerivedCategory.{w'} X'.Modules]
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      g'.toLRSHom.toShHom).obj K ⟶ K')
    (x' : X')
    [HasDerivedCategory.{w'} (ModuleCat.{u} (S.presheaf.stalk (f (g' x'))))]
    [HasDerivedCategory.{w'} (ModuleCat.{u} (X.presheaf.stalk (g' x')))]
    [HasDerivedCategory.{w'} (ModuleCat.{u} (S'.presheaf.stalk (f' x')))]
    [HasDerivedCategory.{w'} (ModuleCat.{u} (X'.presheaf.stalk x'))]
    (n : ℤ)
```

## Tag 0DJ8, a lemma

[Tag 0DJ8](https://stacks.math.columbia.edu/tag/0DJ8) in the Stacks Project.

**`AlgebraicGeometry.BaseChangeChart`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean#L80). The attribute's comment: “the Cartesian affine-open chart quantified over in (2) and (3)”.

> **A Cartesian affine-open chart for a base-change square of schemes.** This is the
> quadruple `U, V, V', U'` of Stacks 0DJ8 (2): affine opens `U ⊆ X` and `V' ⊆ S'` both mapping
> into an affine open `V ⊆ S`, together with `U' = V' ×_V U`, the last expressed by the pushout
> square of coordinate rings.

```lean
public structure BaseChangeChart {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S)
    (f' : X' ⟶ S') (g' : X' ⟶ X)
```

**`AlgebraicGeometry.BaseChangeChart.isOpenImmersion_incU'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean#L146). The attribute's comment: “the U' of a chart is an open of X'”.

> **`U'` is an open of `X'`.** The structure imposes no open-immersion hypothesis on
> `Spec 𝒪_{X'}(U') ⟶ X'`: once the outer square is cartesian the chart data determine that
> morphism uniquely, and it is then automatically an open immersion, being the base change of
> `U ⊆ X` and `V' ⊆ S'` over `V ⊆ S`.

```lean
public theorem isOpenImmersion_incU' (sq : IsPullback g' f' f g)
    (ch : BaseChangeChart f g f' g') : IsOpenImmersion ch.incU'
```

**`AlgebraicGeometry.BaseChangeChart.ofAffineOpens`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean#L177). The attribute's comment: “the chart on a triple of affine opens”.

> **The chart on given affine opens.** For affine opens `U ⊆ X`, `V ⊆ S`, `V' ⊆ S'` with
> `f(U) ⊆ V` and `g(V') ⊆ V`, the coordinate rings and the tensor product
> `𝒪_X(U) ⊗_{𝒪_S(V)} 𝒪_{S'}(V')` form a chart, its `U'` being the canonical open
> `V' ×_V U` of `X'`.

```lean
public def ofAffineOpens (sq : IsPullback g' f' f g)
    (U : X.Opens) (V : S.Opens) (V' : S'.Opens)
    (hU : IsAffineOpen U) (hV : IsAffineOpen V) (hV' : IsAffineOpen V')
    (hUV : U ≤ f ⁻¹ᵁ V) (hV'V : V' ≤ g ⁻¹ᵁ V) : BaseChangeChart f g f' g'
```

**`AlgebraicGeometry.exists_baseChangeChart_covering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean#L239). The attribute's comment: “every point of X' lies in the U' of a chart, the covering input to (2) ⟹ (3)”.

> **Every point of `X'` lies in the `U'` of a chart.** Choose an affine open `V ⊆ S` around
> `f(g' x')`, then an affine open `U ⊆ X` around `g' x'` inside `f⁻¹V`, then an affine open
> `V' ⊆ S'` around `f' x'` inside `g⁻¹V`; the resulting chart's `U' = V' ×_V U` contains `x'`,
> because `x'` corresponds to a point of `U ×_V V'` under the cartesian square.
>
> This is the covering input to the step (2) ⟹ (3) of Stacks 0DJ8.

```lean
public theorem exists_baseChangeChart_covering {X X' S S' : Scheme.{u}} {f : X ⟶ S}
    {g : S' ⟶ S} {f' : X' ⟶ S'} {g' : X' ⟶ X} (sq : IsPullback g' f' f g) (x' : X') :
    ∃ ch : BaseChangeChart f g f' g', ∃ y : Spec ch.A', ch.incU' y = x'
```

**`AlgebraicGeometry.exists_coveringFamily_of_forall_baseChangeChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChart.lean#L328). The attribute's comment: “(2) ⟹ (3), for an arbitrary property of charts”.

> **The step (2) ⟹ (3) of Stacks 0DJ8.** If a property of charts holds for every chart then
> there is a family of charts on which it holds whose opens `U'` cover `X'`: take the family of
> all charts and apply `exists_baseChangeChart_covering`.
>
> The property is left abstract because this step uses nothing about it. Reading `P ch` as
> "the comparison map of `ch` is an isomorphism" turns this into the implication (2) ⟹ (3) of
> the source, which is the only use intended.

```lean
public theorem exists_coveringFamily_of_forall_baseChangeChart {X X' S S' : Scheme.{u}}
    {f : X ⟶ S} {g : S' ⟶ S} {f' : X' ⟶ S'} {g' : X' ⟶ X} (sq : IsPullback g' f' f g)
    (P : BaseChangeChart f g f' g' → Prop) (h : ∀ ch : BaseChangeChart f g f' g', P ch) :
    ∃ 𝒞 : Set (BaseChangeChart f g f' g'), (∀ ch ∈ 𝒞, P ch) ∧
      ∀ x' : X', ∃ ch ∈ 𝒞, ∃ y : Spec ch.A', ch.incU' y = x'
```

**`AlgebraicGeometry.BaseChangeChart.cohomologyComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartCohomologyComparison.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartCohomologyComparison.lean#L248). The attribute's comment: “the comparison map of (2) on a Cartesian affine-open chart, in degree n: the A'-linear map of Tag 0DJ7's ring form for the chart's pushout square of rings”.

> The chart comparison in degree `n`: on a chart with coordinate rings `R`, `A`, `R'`, `A'`,
> the `A'`-linear map
>
> `A' ⊗_{A ⊗_R R'} H^n(RΓ(U,K) ⊗ᴸ_R R') ⟶ H^n(RΓ(U',K'))`
>
> given by `ringCohomologyComparison` for the chart's pushout square of rings.

```lean
public def cohomologyComparison (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') (n : ℤ)
```

**`AlgebraicGeometry.BaseChangeChart.cohomologyComparison_tmul_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartCohomologyComparison.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartCohomologyComparison.lean#L286). The attribute's comment: “the degree-n map of a chart is H^n of the comparison map of (2)”.

> The degree-`n` map of a chart is `H^n` of the chart comparison: its value on `1 ⊗ m` is
> `H^n(comparison)` of `m`, read through the identification of the cohomology of a complex of
> `A'`-modules with the cohomology of its restriction to `R'`.

```lean
public theorem cohomologyComparison_tmul_one (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') (n : ℤ) :
    letI : Algebra ch.R ch.A := ch.a.hom.toAlgebra
    letI : Algebra ch.R ch.R' := ch.b.hom.toAlgebra
    letI : Algebra ch.R ch.A' := (ch.c.hom.comp ch.a.hom).toAlgebra
    letI : Algebra ch.A ch.A' := ch.c.hom.toAlgebra
    letI : Algebra ch.R' ch.A' := ch.d.hom.toAlgebra
    letI : IsScalarTower ch.R ch.A ch.A' := IsScalarTower.of_algebraMap_eq' rfl
    letI : IsScalarTower ch.R ch.R' ch.A' := IsScalarTower.of_algebraMap_eq' ch.isPushout_hom
    ∀ m : baseChangeCohomology (R := ch.R) (R' := ch.R')
      ((affineDerivedSections ch.incU).obj K) n,
      let B := ch.A ⊗[ch.R] ch.R'
      let k : B →+* ch.A' :=
        (Algebra.TensorProduct.lift (IsScalarTower.toAlgHom ch.R ch.A ch.A')
          (IsScalarTower.toAlgHom ch.R ch.R' ch.A') (fun _ _ => Commute.all _ _)).toRingHom
      (ch.cohomologyComparison K K' φ n).hom ((1 : ch.A') ⊗ₜ[B, k] m) =
        (((ModuleCat.restrictScalars ch.d.hom).mapDerivedCategoryHomologyIso n).app
            ((affineDerivedSections ch.incU').obj K')).hom.hom
          (((DerivedCategory.homologyFunctor (ModuleCat.{u} ch.R') n).map
            (ch.comparison K K' φ)).hom m)
```

**`AlgebraicGeometry.BaseChangeChart.isIso_comparison_iff_forall_isIso_cohomologyComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartCohomologyComparison.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartCohomologyComparison.lean#L332). The attribute's comment: “condition (2) at a Cartesian affine-open chart, read degree by degree: the chart comparison is invertible exactly when the A'-linear base-change maps on cohomology of the chart's pushout square of rings are invertible in every degree”.

> The chart comparison
>
> `RΓ(U,K) ⊗ᴸ_{𝒪_S(V)} 𝒪_{S'}(V') ⟶ RΓ(U',K')`
>
> is an isomorphism exactly when, in every degree `n`, the `A'`-linear map
>
> `A' ⊗_{A ⊗_R R'} H^n(RΓ(U,K) ⊗ᴸ_R R') ⟶ H^n(RΓ(U',K'))`
>
> of the chart's pushout square of rings is.

```lean
public theorem isIso_comparison_iff_forall_isIso_cohomologyComparison
    (ch : BaseChangeChart f g f' g') (K : DerivedCategory X.Modules)
    (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') :
    IsIso (ch.comparison K K' φ) ↔
      ∀ n : ℤ, IsIso (ch.cohomologyComparison K K' φ n)
```

**`AlgebraicGeometry.BaseChangeChart.isIso_comparison_iff_forall_localized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartCohomologyComparison.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartCohomologyComparison.lean#L356). The attribute's comment: “condition (2) at a Cartesian affine-open chart is a pointwise condition on the points of U': invertibility of the localization at each prime of A' of each degree-n map”.

> The chart comparison is an isomorphism exactly when, at every prime `y` of
> `A' = 𝒪_{X'}(U')` (that is, at every point of `U'`) and in every degree `n`, the localization at
> `y` of the degree-`n` map of the chart is an isomorphism.

```lean
public theorem isIso_comparison_iff_forall_localized (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') :
    IsIso (ch.comparison K K' φ) ↔
      ∀ (y : PrimeSpectrum ch.A') (n : ℤ),
        IsIso ((ModuleCat.localizedModuleFunctor.{u} y.asIdeal.primeCompl).map
          (ch.cohomologyComparison K K' φ n))
```

**`AlgebraicGeometry.BaseChangeChart.sectionsBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparisonMap.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparisonMap.lean#L103). The attribute's comment: “the second arrow of the composition in (2): the identification RΓ(U,K) ⊗ᴸ\_\{𝒪\_X(U)} 𝒪\_\{X'}(U') = RΓ(U', L(g')^*K)”.

> **The identification in condition (2).** On a chart, derived sections of `K` over `U` base
> changed along `𝒪_X(U) ⟶ 𝒪_{X'}(U')` compare with derived sections over `U'` of the derived
> pullback of `K`: `RΓ(U, K) ⊗ᴸ_{𝒪_X(U)} 𝒪_{X'}(U') ⟶ RΓ(U', L(g')^*K)`.

```lean
public def sectionsBaseChangeMap (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules) :
    (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
        ch.c.hom).functor.obj ((affineDerivedSections ch.incU).obj K) ⟶
      (affineDerivedSections ch.incU').obj ((Stacks.Duality.derivedPullback g').obj K)
```

**`AlgebraicGeometry.BaseChangeChart.isIso_sectionsBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparisonMap.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparisonMap.lean#L132). The attribute's comment: “the second arrow of the composition in (2) is an isomorphism for K with quasi-coherent cohomology, so (2) tests the composition the source displays”.

> **The identification `sectionsBaseChangeMap` is an isomorphism** when every cohomology sheaf
> of `K` is quasi-coherent.

```lean
public theorem isIso_sectionsBaseChangeMap (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules)
    (hK : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent) :
    IsIso (ch.sectionsBaseChangeMap K)
```

**`AlgebraicGeometry.BaseChangeChart.comparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparisonMap.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparisonMap.lean#L191). The attribute's comment: “the comparison map on a Cartesian affine-open chart: the morphism whose invertibility is condition (2), and, asked only of a family of charts whose opens U' cover X', condition (3)”.

> **The chart comparison map.** On a chart, the composition
>
> `RΓ(U,K) ⊗ᴸ_{𝒪_S(V)} 𝒪_{S'}(V') ⟶ RΓ(U,K) ⊗ᴸ_{𝒪_X(U)} 𝒪_{X'}(U') ⟶ RΓ(U',K')`
>
> in `D(𝒪_{S'}(V'))`: `pullbackComparison` followed by `RΓ(U', -)` applied to the given morphism
> `φ : L(g')^*K ⟶ K'`.

```lean
public def comparison (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') :
    (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
        ch.b.hom).functor.obj
        ((ModuleCat.restrictScalars ch.a.hom).mapDerivedCategory.obj
          ((affineDerivedSections ch.incU).obj K)) ⟶
      (ModuleCat.restrictScalars ch.d.hom).mapDerivedCategory.obj
        ((affineDerivedSections ch.incU').obj K')
```

**`AlgebraicGeometry.exists_coveringFamily_isIso_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparisonMap.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparisonMap.lean#L251). The attribute's comment: “(2) ⟹ (3) for the comparison map itself, which is the step of the three-way equivalence that needs no affine reduction: take the family of all charts”.

> **The step (2) ⟹ (3).** If the comparison map of every Cartesian affine-open chart is an
> isomorphism, then there is a family of charts on which it is, whose opens `U'` cover `X'`.

```lean
public theorem exists_coveringFamily_isIso_comparison {X X' S S' : Scheme.{u}}
    {f : X ⟶ S} {g : S' ⟶ S} {f' : X' ⟶ S'} {g' : X' ⟶ X} (sq : IsPullback g' f' f g)
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K')
    (h : ∀ ch : BaseChangeChart f g f' g', IsIso (ch.comparison K K' φ)) :
    ∃ 𝒞 : Set (BaseChangeChart f g f' g'), (∀ ch ∈ 𝒞, IsIso (ch.comparison K K' φ)) ∧
      ∀ x' : X', ∃ ch ∈ 𝒞, ∃ y : Spec ch.A', ch.incU' y = x'
```

**`AlgebraicGeometry.BaseChangeChart.comparison_eq_ringComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartPrimeCriterion.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartPrimeCriterion.lean#L240). The attribute's comment: “the comparison map of (2) is the ring-level comparison of the chart's square”.

> The comparison map of a chart is the ring-level comparison of the chart's square of
> coordinate rings, applied to the morphism `RΓ(U,K) ⊗ᴸ_{𝒪_X(U)} 𝒪_{X'}(U') ⟶ RΓ(U',K')` assembled
> from the identification `sectionsBaseChangeMap` and `RΓ(U', φ)`.

```lean
theorem comparison_eq_ringComparison (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') :
    letI := ch.a.hom.toAlgebra
    letI := ch.b.hom.toAlgebra
    letI := ch.c.hom.toAlgebra
    letI := ch.d.hom.toAlgebra
    letI := (ch.c.hom.comp ch.a.hom).toAlgebra
    haveI : IsScalarTower ch.R ch.A ch.A' := IsScalarTower.of_algebraMap_eq fun _ => rfl
    haveI : IsScalarTower ch.R ch.R' ch.A' :=
      IsScalarTower.of_algebraMap_eq fun r => DFunLike.congr_fun ch.isPushout_hom r
    ch.comparison K K' φ =
      RingTheory.TorIndependence.ringComparison
        (R := ch.R) (R' := ch.R')
        ((affineDerivedSections ch.incU).obj K)
        ((affineDerivedSections ch.incU').obj K')
        (ch.sectionsBaseChangeMap K ≫ (affineDerivedSections ch.incU').map φ)
```

**`AlgebraicGeometry.BaseChangeChart.isIso_comparison_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartPrimeCriterion.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartPrimeCriterion.lean#L265). The attribute's comment: “(2) at one chart, reduced to the primes of the chart's coordinate ring”.

> The comparison map of a Cartesian affine-open chart is an isomorphism exactly when, in
> every degree, the induced map on cohomology is bijective after localizing at every prime of
> `𝒪_X(U) ⊗_{𝒪_S(V)} 𝒪_{S'}(V')`.

```lean
theorem isIso_comparison_iff (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') :
    letI := ch.a.hom.toAlgebra
    letI := ch.b.hom.toAlgebra
    letI := ch.c.hom.toAlgebra
    letI := ch.d.hom.toAlgebra
    letI := (ch.c.hom.comp ch.a.hom).toAlgebra
    haveI : IsScalarTower ch.R ch.A ch.A' := IsScalarTower.of_algebraMap_eq fun _ => rfl
    haveI : IsScalarTower ch.R ch.R' ch.A' :=
      IsScalarTower.of_algebraMap_eq fun r => DFunLike.congr_fun ch.isPushout_hom r
    (IsIso (ch.comparison K K' φ) ↔
      ∀ (n : ℤ) (q : Ideal (ch.A ⊗[ch.R] ch.R')) (_ : q.IsPrime),
        Function.Bijective (LocalizedModule.map q.primeCompl
          (RingTheory.TorIndependence.cohomologyComparisonLinearMapGeneral
            (R := ch.R) (R' := ch.R')
            ((affineDerivedSections ch.incU).obj K)
            ((affineDerivedSections ch.incU').obj K')
            (ch.sectionsBaseChangeMap K ≫ (affineDerivedSections ch.incU').map φ) n).hom))
```

**`AlgebraicGeometry.BaseChangeChart.isIso_comparison_iff_forall_isIso_ringBaseChangeCohomologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartPrimeCriterion.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartPrimeCriterion.lean#L292). The attribute's comment: “(2) at one chart is the invertibility, in every degree, of the ring-level map of Stacks 0DJ7 for the chart's rings: the affine reduction of the source proof”.

> The comparison map of a Cartesian affine-open chart is an isomorphism exactly when the
> ring-level map `RingTheory.TorIndependence.ringBaseChangeCohomologyMapGeneral` of Stacks 0DJ7 for
> the chart's square of coordinate rings is invertible in every degree.

```lean
theorem isIso_comparison_iff_forall_isIso_ringBaseChangeCohomologyMap
    (ch : BaseChangeChart f g f' g')
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') :
    letI := ch.a.hom.toAlgebra
    letI := ch.b.hom.toAlgebra
    letI := ch.c.hom.toAlgebra
    letI := ch.d.hom.toAlgebra
    letI := (ch.c.hom.comp ch.a.hom).toAlgebra
    haveI : IsScalarTower ch.R ch.A ch.A' := IsScalarTower.of_algebraMap_eq fun _ => rfl
    haveI : IsScalarTower ch.R ch.R' ch.A' :=
      IsScalarTower.of_algebraMap_eq fun r => DFunLike.congr_fun ch.isPushout_hom r
    (IsIso (ch.comparison K K' φ) ↔
      ∀ n : ℤ, IsIso (RingTheory.TorIndependence.ringBaseChangeCohomologyMapGeneral
        (R := ch.R) (R' := ch.R')
        ((affineDerivedSections ch.incU).obj K)
        ((affineDerivedSections ch.incU').obj K')
        (ch.sectionsBaseChangeMap K ≫ (affineDerivedSections ch.incU').map φ) n))
```

**`AlgebraicGeometry.baseChange_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/BaseChangeTFAEFinal.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/BaseChangeTFAEFinal.lean#L492).

> **Stacks 0DJ8.** Let
>
> `X' ⟶ X`, `X' ⟶ S'`, `X ⟶ S`, `S' ⟶ S`
>
> be a Cartesian square of schemes, `K` an object of `D(𝒪_X)` with quasi-coherent cohomology
> sheaves, `K'` an object of `D(𝒪_{X'}')` with quasi-coherent cohomology sheaves, and
> `φ : L(g')^*K ⟶ K'`. Then the following are equivalent.
>
> 1. The pointwise map of Stacks 0DJ7 is an isomorphism at every point of `X'` and in every
>    degree.
> 2. The comparison map of every Cartesian affine-open chart is an isomorphism.
> 3. The comparison map of every chart in some family whose opens `U'` cover `X'` is an
>    isomorphism.
>
> The implications are read off the source bridge
> `AlgebraicGeometry.baseChange_tfae_of_sourceBridge`: at a chart, a point `y` of
> `Spec 𝒪_{X'}(U')` and a degree, `AlgebraicGeometry.BaseChangeChart.sourceBridgeMap` is a
> bijection of the two maps' sources — `AlgebraicGeometry.BaseChangeChart.bijective_sourceBridgeMap`
> — commuting with them through the identification of their targets, by
> `AlgebraicGeometry.BaseChangeChart.baseChangeCohomologyMap_sourceBridgeMap`.

```lean
public theorem baseChange_tfae {X X' S S' : Scheme.{u}}
    (f : X ⟶ S) (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X) (sq : IsPullback g' f' f g)
    (K : DerivedCategory X.Modules) (K' : DerivedCategory X'.Modules)
    (hK : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent)
    (hK' : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X'.Modules n).obj K').IsQuasicoherent)
    (φ : (Stacks.Duality.derivedPullback g').obj K ⟶ K') :
    List.TFAE
      [∀ (x' : X') (i : ℤ), IsIso (baseChangeCohomologyMap f g f' g' sq.w K K' φ x' i),
       ∀ ch : BaseChangeChart f g f' g', IsIso (ch.comparison K K' φ),
       ∃ 𝒞 : Set (BaseChangeChart f g f' g'),
         (∀ ch ∈ 𝒞, IsIso (ch.comparison K K' φ)) ∧
           ∀ x' : X', ∃ ch ∈ 𝒞, ∃ y : Spec ch.A', ch.incU' y = x']
```

**`AlgebraicGeometry.isIso_baseChangeCohomologyMap_derivedPullbackNatTrans_of_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/FlatOverModel.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/FlatOverModel.lean#L488). The attribute's comment: “condition (1), at every point and in every degree, for the derived-to-ordinary comparison L(g')^*G ⟶ (g')^*G of a bounded-above complex G whose terms are flat over S, over a cartesian square: the stalk check the proof of Tag 0A1D performs”.

> **The stalk check of Stacks 0DJ8 for a complex flat over the base, at one point.**  For a
> cartesian square of schemes and a bounded-above complex `𝒢^•` of `𝒪_X`-modules whose terms are
> flat over `S`, the map of Stacks 0DJ7 at the derived-to-ordinary comparison
> `L(g')^*𝒢^• ⟶ (g')^*𝒢^•` is an isomorphism at `x'` in degree `n`.

```lean
theorem isIso_baseChangeCohomologyMap_derivedPullbackNatTrans_of_isFlatOver
    (hpb : IsPullback g' f' f g) (w : g' ≫ f = f' ≫ g) (G : CochainComplex X.Modules ℤ)
    (hG : CochainComplex.minus X.Modules G)
    (hflat : ∀ n : ℤ, IsFlatOver f.toLRSHom.toShHom (G.X n)) (x' : X') (n : ℤ) :
    IsIso (baseChangeCohomologyMap f g f' g' w (DerivedCategory.Q.obj G)
      (DerivedCategory.Q.obj ((pullbackComplex g'.toLRSHom.toShHom).obj G))
      ((derivedPullbackNatTrans g'.toLRSHom.toShHom).app G) x' n)
```

**`AlgebraicGeometry.derivedStalkAffineSectionsIsoToStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedStalk.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedStalk.lean#L321). The attribute's comment: “the first of the two inputs still needed to turn condition (1) into condition (2): the derived stalk of K at a point of an affine open, identified with the derived localization of RGamma(U,K) there. This is that identification only; the compatibility of the base-change comparison of Tag 065Z with localization, which is the second input, is not proved anywhere, so condition (1) implies condition (2) is NOT formalized”.

> **The derived stalk at a point of an affine open is the derived localization of the sections
> over that open.** Let `i : Spec R ⟶ X` be a morphism of schemes out of an affine scheme, `y` a
> point of `Spec R`, and `K ∈ D(𝒪_X)` an object with quasi-coherent cohomology sheaves. Then
>
> `RΓ(U, K) ⊗ᴸ_R 𝒪_{Spec R, y} ≅ (K_{i y}) ⊗ᴸ_{𝒪_{X, i y}} 𝒪_{Spec R, y}`,
>
> where `RΓ(U, K)` is `AlgebraicGeometry.affineDerivedSections i` applied to `K`.  When `i` is an
> open immersion with image `U` the extension of scalars on the right is along the germ
> isomorphism `𝒪_{X, i y} ≅ 𝒪_{Spec R, y}`, so the right-hand side *is* the derived stalk of `K`
> at the point `i y` of `U`, and the two sides are the two readings of that derived stalk; the
> statement itself asks nothing of `i`.
>
> The left-hand side is the derived localization at `y` of the derived global sections of the
> derived pullback of `K` to `Spec R`, which has quasi-coherent cohomology by Stacks 08DW, so
> `affineDerivedStalkSectionsIso` identifies it with the derived stalk at `y` of that pullback;
> `AlgebraicGeometry.derivedPullbackStalkIso` then moves the stalk from `Spec R` to `X`.

```lean
public def derivedStalkAffineSectionsIsoToStalk {X : Scheme.{u}} {A : CommRingCat.{u}}
    (i : Spec A ⟶ X) (y : Spec A) (K : DerivedCategory X.Modules)
    (hK : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent) :
    (totalDerivedExtensionScalars.{u, u, u}
        (A := ((Spec A).presheaf.stalk y : Type u))
        (StructureSheaf.toStalk A y).hom).functor.obj
        ((affineDerivedSections i).obj K) ≅
      (totalDerivedExtensionScalars.{u, u, u} (i.stalkMap y).hom).functor.obj
        ((derivedStalkFunctor (i y)).obj K)
```

**`AlgebraicGeometry.localizedHomologyAffineSectionsStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedStalkHomology.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedStalkHomology.lean#L119). The attribute's comment: “the degreewise reading of the first of the two inputs needed to turn condition (1) into condition (2): the localization at a prime of the degree-n cohomology of RGamma(U,K) is the degree-n cohomology of the derived stalk there. The identification of this localized module with the localization of the degree-n chart map of condition (2), which needs the compatibility of the base-change comparison of Tag 065Z with localizing ALL FOUR rings of the chart's square and not only its right-hand column, is not proved anywhere, so condition (1) implies condition (2) is NOT formalized”.

> **The derived stalk at a point of an affine open, read degree by degree.**  For
> `i : Spec A ⟶ X`, a point `y` of `Spec A` and `K ∈ D(𝒪_X)` with quasi-coherent cohomology
> sheaves, the localization at `y` of the degree-`n` cohomology of `RΓ(U,K)` is the degree-`n`
> cohomology of the derived stalk of `K` at `i y`, base changed to `𝒪_{Spec A,y}`:
>
> `(Hⁿ RΓ(U,K))_y ≅ Hⁿ(K_{i y} ⊗ᴸ_{𝒪_{X, i y}} 𝒪_{Spec A,y})`.
>
> When `i` is an open immersion `𝒪_{X, i y} ⟶ 𝒪_{Spec A,y}` is invertible and the right-hand side
> is the degree-`n` cohomology of the derived stalk itself; the statement asks nothing of `i`.
>
> This is `AlgebraicGeometry.derivedStalkAffineSectionsIsoToStalk` with `Hⁿ` applied, the left-hand
> side being recognized as a localization because the germ map is one.

```lean
public def localizedHomologyAffineSectionsStalkIso {X : Scheme.{u}} {A : CommRingCat.{u}}
    (i : Spec A ⟶ X) (y : Spec A) (K : DerivedCategory X.Modules)
    (hK : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent)
    (n : ℤ) :
    (CochainComplex.DerivedTensor.localizedModuleFunctor.{u, u}
        (show PrimeSpectrum (A : Type u) from y).asIdeal.primeCompl).obj
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} (A : Type u)) n).obj
          ((affineDerivedSections i).obj K)) ≅
      (ModuleCat.restrictScalars.{u, u, u} (StructureSheaf.toStalk A y).hom).obj
        ((DerivedCategory.homologyFunctor
            (ModuleCat.{u} ((Spec A).presheaf.stalk y : Type u)) n).obj
          ((totalDerivedExtensionScalars.{u, u, u} (i.stalkMap y).hom).functor.obj
            ((derivedStalkFunctor (i y)).obj K)))
```

## Tag 0DJ9, a lemma

[Tag 0DJ9](https://stacks.math.columbia.edu/tag/0DJ9) in the Stacks Project.

**`AlgebraicGeometry.globalBaseChangeIsIsoOfPointwise`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TensorFlatPushforwardBaseChangeCartesian.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TensorFlatPushforwardBaseChangeCartesian.lean#L67). The attribute's comment: “the conclusion over every cartesian square at once, in the spelling of GlobalBaseChangeIsIsoOfPointwise, with the conditions of Tag 0DJ8 read in form (1)”.

> **`GlobalBaseChangeIsIsoOfPointwise` holds**: it is Stacks 0DJ9,
> `AlgebraicGeometry.isIso_derivedBaseChangeComp_of_pointwiseBaseChange`, quantified over all
> cartesian squares.

```lean
theorem globalBaseChangeIsIsoOfPointwise : GlobalBaseChangeIsIsoOfPointwise.{u}
```

**`AlgebraicGeometry.isIso_derivedBaseChangeComp_of_pointwiseBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/PointwiseBaseChangeIso.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/PointwiseBaseChangeIso.lean#L58).

> **Stacks 0DJ9.** For a cartesian square of schemes with `f` quasi-compact and
> quasi-separated, an object `K` of `D_QCoh(𝒪_X)` and a morphism `φ : L(g')^*K ⟶ K'` to an object
> of `D_QCoh(𝒪_{X'})` whose pointwise maps of Stacks 0DJ7 are invertible at every point of `X'` and
> in every degree, the composition `Lg^*Rf_*K ⟶ Rf'_*L(g')^*K ⟶ Rf'_*K'` is an isomorphism.

```lean
theorem isIso_derivedBaseChangeComp_of_pointwiseBaseChange (sq : IsPullback g' f' f g)
    [QuasiCompact f] [QuasiSeparated f] (K : DerivedCategory X.Modules)
    (K' : DerivedCategory X'.Modules) (φ : (derivedPullback g'.toLRSHom.toShHom).obj K ⟶ K')
    (hK : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent)
    (hK' : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X'.Modules n).obj K').IsQuasicoherent)
    (hp : PointwiseBaseChange f g f' g' sq.w K K' φ) :
    IsIso (derivedBaseChangeComp f g f' g' sq.w K K' φ)
```

## Tag 0DJA, a lemma

[Tag 0DJA](https://stacks.math.columbia.edu/tag/0DJA) in the Stacks Project.

**`AlgebraicGeometry.pointwiseBaseChangeTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TensorFlatPushforwardBaseChangeCartesian.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TensorFlatPushforwardBaseChangeCartesian.lean#L88). The attribute's comment: “(1), over every cartesian square at once, with the conditions of Tag 0DJ8 read in form (1)”.

> **`PointwiseBaseChangeTensor` holds**: it is Stacks 0DJA (1),
> `AlgebraicGeometry.isIso_baseChangeCohomologyMap_baseChangeTensorComparison_of_isPullback`.
>
> Cartesianness of the square is needed: for `X = S = S' = Spec ℤ/4`, `X' = Spec ℤ/2`,
> `f = g = 𝟙`, `g' = f'` the quotient map, `K = 𝒪_X`, `K' = 𝒪_{X'}` and `φ` the canonical
> isomorphism, the map of Stacks 0DJ7 is `ℤ/2 ⟶ ℤ/2`, while for `E = (ℤ/2)~` it is
> `0 ⟶ Tor_1^{ℤ/4}(ℤ/2, ℤ/2) = ℤ/2` in degree `-1`.

```lean
theorem pointwiseBaseChangeTensor : PointwiseBaseChangeTensor.{u}
```

**`AlgebraicGeometry.isIso_baseChangeCohomologyMap_baseChangeSheafHomComparison_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/DerivedSheafHom.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/DerivedSheafHom.lean#L68). The attribute's comment: “(2)”.

> **Stacks 0DJA (2).** For a cartesian square of schemes, if the map of Stacks 0DJ7 at
> `(K, K', φ)` is an isomorphism at every point of `X'` and in every degree, then so is the one at
> the comparison `L(g')^*R𝓗om(E, K) ⟶ R𝓗om(L(g')^*E, K')`, for every perfect `E` in `D(𝒪_X)`.

```lean
theorem isIso_baseChangeCohomologyMap_baseChangeSheafHomComparison_of_isPerfect
    (hpb : IsPullback g' f' f g) (E K : DerivedCategory X.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (K' : DerivedCategory X'.Modules) (φ : (derivedPullback g'.toLRSHom.toShHom).obj K ⟶ K')
    (h : ∀ (x' : X') (n : ℤ), IsIso (baseChangeCohomologyMap f g f' g' hpb.w K K' φ x' n))
    (x' : X') (n : ℤ) :
    IsIso (baseChangeCohomologyMap f g f' g' hpb.w
      (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op E)).obj K)
      (((Stacks.SheafOfModules.derivedSheafHom X'.sheaf).obj
        (op ((derivedPullback g'.toLRSHom.toShHom).obj E))).obj K')
      (Stacks.Cohomology.DerivedBaseChangeComparison.baseChangeSheafHomComparison
        g'.toLRSHom.toShHom E K K' φ) x' n)
```

**`AlgebraicGeometry.not_pointwiseBaseChangeSheafHomOfPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/DerivedSheafHomPseudoCoherentCounterexample.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/DerivedSheafHomPseudoCoherentCounterexample.lean#L308). The attribute's comment: “(3) as written is false: the statement of part (3), with no condition on g, fails by a counterexample over ℤ/4 with g : Spec ℤ/2 ⟶ Spec ℤ/4, K the structure sheaf and E the periodic resolution of ℤ/2”.

> The statement of part (3) of Stacks 0DJA, with the equivalent conditions of Stacks 0DJ8 read in
> form (1) and `g` an arbitrary morphism, fails: for `A = ℤ/4`, the cartesian square with
> `g : Spec ℤ/2 ⟶ Spec ℤ/4` the closed immersion and identities as vertical arrows,
> `K = 𝒪_{Spec ℤ/4}`, `K' = L g^* K`, `φ = id`, and `E` the pseudo-coherent object attached to the
> resolution `⋯ --2--> ℤ/4 --2--> ℤ/4` of `ℤ/2`, condition (1) of Stacks 0DJ8 holds for `φ` but
> fails for `L g^* R𝓗om(E, K) ⟶ R𝓗om(L g^* E, K')`, whose source has cohomology
> `Tor_1^{ℤ/4}(ℤ/2, ℤ/2) ≠ 0` in degree `-1` while its target lies in degrees `≥ 0`.

```lean
theorem not_pointwiseBaseChangeSheafHomOfPseudoCoherent :
    ¬ (∀ {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X),
      IsPullback g' f' f g →
      ∀ (w : g' ≫ f = f' ≫ g) (E K : DerivedCategory X.Modules)
        (K' : DerivedCategory X'.Modules)
        (φ : (derivedPullback g'.toLRSHom.toShHom).obj K ⟶ K'),
        RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E →
        (∃ (L : CochainComplex X.Modules ℤ) (a : ℤ), L.IsStrictlyGE a ∧
          Nonempty (DerivedCategory.Q.obj L ≅ K)) →
        (∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent) →
        (∀ n : ℤ, ((DerivedCategory.homologyFunctor X'.Modules n).obj K').IsQuasicoherent) →
        PointwiseBaseChangeIsIso f g f' g' w K K' φ →
        PointwiseBaseChangeIsIso f g f' g' w
          (((derivedSheafHom X.sheaf).obj (op E)).obj K)
          (((derivedSheafHom X'.sheaf).obj
            (op ((derivedPullback g'.toLRSHom.toShHom).obj E))).obj K')
          (baseChangeSheafHomComparison g'.toLRSHom.toShHom E K K' φ))
```

**`AlgebraicGeometry.isIso_baseChangeCohomologyMap_baseChangeSheafHomComparison_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/DerivedSheafHomPseudoCoherentTorDimension.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/DerivedSheafHomPseudoCoherentTorDimension.lean#L107). The attribute's comment: “(3), corrected: g of finite Tor dimension added (every local ring of S' of Tor amplitude in a fixed interval over the local ring of S below it); with no condition on g part (3) is false, see AlgebraicGeometry.not\_pointwiseBaseChangeSheafHomOfPseudoCoherent”.

> **Stacks 0DJA (3), corrected: `g` of finite Tor dimension.** For a cartesian square of
> schemes with `g` of finite Tor dimension (every `𝒪_{S', s'}` of Tor amplitude in a fixed
> interval `[a, b]` over `𝒪_{S, g s'}`), if the map of Stacks 0DJ7 at `(K, K', φ)` is an
> isomorphism at every point of `X'` and in every degree and `K` is bounded below, then so is the
> one at the comparison `L(g')^*R𝓗om(E, K) ⟶ R𝓗om(L(g')^*E, K')`, for every pseudo-coherent `E`
> in `D(𝒪_X)`.
>
> As printed, with no condition on `g`, part (3) is false:
> `AlgebraicGeometry.not_pointwiseBaseChangeSheafHomOfPseudoCoherent` is a counterexample with
> `g : Spec ℤ/2 ⟶ Spec ℤ/4`.

```lean
theorem isIso_baseChangeCohomologyMap_baseChangeSheafHomComparison_of_hasTorAmplitude
    (hpb : IsPullback g' f' f g)
    (hg : ∃ a b : ℤ, ∀ s' : S',
      letI := (g.stalkMap s').hom.toAlgebra
      StacksDraft.TorAmplitude.HasTorAmplitudeCanonical (S.presheaf.stalk (g s'))
        (DerivedCategory.Q.obj ((CochainComplex.singleFunctor
          (ModuleCat.{u} (S.presheaf.stalk (g s'))) 0).obj
            (ModuleCat.of (S.presheaf.stalk (g s')) (S'.presheaf.stalk s')))) a b)
    (E K : DerivedCategory X.Modules)
    (hE : AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherent (X := X.toRingedSpace) E)
    (hK : DerivedCategoryB.IsBoundedBelow K)
    (K' : DerivedCategory X'.Modules) (φ : (derivedPullback g'.toLRSHom.toShHom).obj K ⟶ K')
    (h : ∀ (x' : X') (n : ℤ), IsIso (baseChangeCohomologyMap f g f' g' hpb.w K K' φ x' n))
    (x' : X') (n : ℤ) :
    IsIso (baseChangeCohomologyMap f g f' g' hpb.w
      (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op E)).obj K)
      (((Stacks.SheafOfModules.derivedSheafHom X'.sheaf).obj
        (op ((derivedPullback g'.toLRSHom.toShHom).obj E))).obj K')
      (Stacks.Cohomology.DerivedBaseChangeComparison.baseChangeSheafHomComparison
        g'.toLRSHom.toShHom E K K' φ) x' n)
```

**`AlgebraicGeometry.isIso_baseChangeCohomologyMap_baseChangeTensorComparison_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/DerivedTensor.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TensorBaseChange/DerivedTensor.lean#L130). The attribute's comment: “(1)”.

> **Stacks 0DJA (1).** For a cartesian square of schemes, if the map of Stacks 0DJ7 at
> `(K, K', φ)` is an isomorphism at every point of `X'` and in every degree, then so is the one at
> the comparison `L(g')^*(E ⊗^L K) ⟶ L(g')^*E ⊗^L K'`, for every `E` in `D(𝒪_X)`.

```lean
theorem isIso_baseChangeCohomologyMap_baseChangeTensorComparison_of_isPullback
    (hpb : IsPullback g' f' f g) (E K : DerivedCategory X.Modules)
    (K' : DerivedCategory X'.Modules) (φ : (derivedPullback g'.toLRSHom.toShHom).obj K ⟶ K')
    (h : ∀ (x' : X') (n : ℤ), IsIso (baseChangeCohomologyMap f g f' g' hpb.w K K' φ x' n))
    (x' : X') (n : ℤ) :
    IsIso (baseChangeCohomologyMap f g f' g' hpb.w
      (((derivedTensorProductFunctor X.sheaf).obj E).obj K)
      (((derivedTensorProductFunctor X'.sheaf).obj
        ((derivedPullback g'.toLRSHom.toShHom).obj E)).obj K')
      (Stacks.Cohomology.DerivedBaseChangeComparison.baseChangeTensorComparison
        g'.toLRSHom.toShHom E K K' φ) x' n)
```

## Tag 0A1D, a lemma

[Tag 0A1D](https://stacks.math.columbia.edu/tag/0A1D) in the Stacks Project.

**`AlgebraicGeometry.isIso_tensorFlatBaseChangeMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/FlatOverBase/TensorFlat.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/FlatOverBase/TensorFlat.lean#L62).

> **Stacks 0A1D.** Let `f : X ⟶ S` be a quasi-compact and quasi-separated morphism of schemes,
> `E` an object of `D_QCoh(𝒪_X)` and `𝒢^•` a bounded above complex of quasi-coherent
> `𝒪_X`-modules flat over `S`. For every cartesian square the canonical map
>
> `Lg^*Rf_*(E ⊗^L_{𝒪_X} 𝒢^•) ⟶ Rf'_*(L(g')^*E ⊗^L_{𝒪_{X'}} (g')^*𝒢^•)`
>
> of `tensorFlatBaseChangeMap`, with the ordinary pullback of `𝒢^•` on the right, is an
> isomorphism.

```lean
theorem isIso_tensorFlatBaseChangeMap_of_isPullback {X X' S S' : Scheme.{u}} (f : X ⟶ S)
    (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X) (hsq : IsPullback g' f' f g)
    (hqc : QuasiCompact f) (hqs : QuasiSeparated f)
    (sq : g'.toLRSHom.toShHom ≫ f.toLRSHom.toShHom =
      f'.toLRSHom.toShHom ≫ g.toLRSHom.toShHom)
    (E : DerivedCategory X.Modules)
    (hE : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj E).IsQuasicoherent)
    (G : CochainComplex X.Modules ℤ)
    (hGminus : CochainComplex.minus X.Modules G)
    (hGqcoh : ∀ n : ℤ, (G.X n).IsQuasicoherent)
    (hGflat : ∀ n : ℤ, IsFlatOver f.toLRSHom.toShHom (G.X n)) :
    IsIso (tensorFlatBaseChangeMap f g f' g' sq E G)
```

**`AlgebraicGeometry.tensorFlatBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TensorFlatPushforwardBaseChange.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TensorFlatPushforwardBaseChange.lean#L137). The attribute's comment: “the canonical map whose invertibility is the tag's conclusion, as the precise statement in the proof displays it: the derived base-change map of Stacks 08HY at E ⊗^L 𝒢^•, followed by Rf'\_* of the base-change comparison of Stacks 0DJA taken at the derived-to-ordinary comparison L(g')^*𝒢^• ⟶ (g')^*𝒢^•. The target uses the ORDINARY pullback (g')^*𝒢^•, which the source sets in bold, and the derived-to-ordinary comparison is not assumed invertible”.

> **The canonical map of Stacks 0A1D**, as the precise statement in the source's proof
> displays it:
>
> `Lg^*Rf_*(E ⊗^L_{𝒪_X} 𝒢^•) ⟶ Rf'_*(L(g')^*E ⊗^L_{𝒪_{X'}} (g')^*𝒢^•)`.
>
> It is the derived base-change map of Stacks 08HY at `E ⊗^L_{𝒪_X} 𝒢^•`, followed by `Rf'_*` of
> the base-change comparison for a derived tensor product of Stacks 0DJA, taken at the
> derived-to-ordinary comparison `L(g')^*𝒢^• ⟶ (g')^*𝒢^•`.
>
> On the right-hand side the complex `𝒢^•` is pulled back by the **ordinary** functor `(g')^*`,
> which is what the source's boldface insists on; the derived-to-ordinary comparison that makes
> this possible is the `φ` of the second factor, and it is never assumed invertible.

```lean
public def tensorFlatBaseChangeMap {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S)
    (f' : X' ⟶ S') (g' : X' ⟶ X)
    (sq : g'.toLRSHom.toShHom ≫ f.toLRSHom.toShHom =
      f'.toLRSHom.toShHom ≫ g.toLRSHom.toShHom)
    (E : DerivedCategory X.Modules) (G : CochainComplex X.Modules ℤ) :
    (derivedPullback g.toLRSHom.toShHom).obj
        ((derivedPushforward f.toLRSHom.toShHom).obj
          (((derivedTensorProductFunctor X.sheaf).obj E).obj (DerivedCategory.Q.obj G))) ⟶
      (derivedPushforward f'.toLRSHom.toShHom).obj
        (((derivedTensorProductFunctor X'.sheaf).obj
            ((derivedPullback g'.toLRSHom.toShHom).obj E)).obj
          (DerivedCategory.Q.obj ((pullbackComplex g'.toLRSHom.toShHom).obj G)))
```

## Tag 08IE, a lemma

[Tag 08IE](https://stacks.math.columbia.edu/tag/08IE) in the Stacks Project.

**`AlgebraicGeometry.sheafHomFlatBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomFlatPushforwardBaseChange.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomFlatPushforwardBaseChange.lean#L135). The attribute's comment: “the canonical map whose invertibility is the tag's conclusion: the derived base-change map of Stacks 08HY at R𝓗om(E, 𝒢^•), followed by Rf'\_* of the base-change comparison of Stacks 0DJA taken at the derived-to-ordinary comparison L(g')^*𝒢^• ⟶ (g')^*𝒢^•. The target uses the ORDINARY pullback (g')^*𝒢^•, which the source sets in bold, and the derived-to-ordinary comparison is not assumed invertible”.

> **The canonical map of Stacks 08IE**:
>
> `Lg^*Rf_*R𝓗om_{𝒪_X}(E, 𝒢^•) ⟶ Rf'_*R𝓗om_{𝒪_{X'}}(L(g')^*E, (g')^*𝒢^•)`.
>
> It is the derived base-change map of Stacks 08HY at `R𝓗om_{𝒪_X}(E, 𝒢^•)`, followed by `Rf'_*`
> of the base-change comparison for a derived internal hom of Stacks 0DJA, taken at the
> derived-to-ordinary comparison `L(g')^*𝒢^• ⟶ (g')^*𝒢^•`.
>
> On the right-hand side the complex `𝒢^•` is pulled back by the **ordinary** functor `(g')^*`,
> which is what the source's boldface insists on; the derived-to-ordinary comparison that makes
> this possible is the `φ` of the second factor, and it is never assumed invertible.

```lean
public def sheafHomFlatBaseChangeMap {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S)
    (f' : X' ⟶ S') (g' : X' ⟶ X)
    (sq : g'.toLRSHom.toShHom ≫ f.toLRSHom.toShHom =
      f'.toLRSHom.toShHom ≫ g.toLRSHom.toShHom)
    (E : DerivedCategory X.Modules) (G : CochainComplex X.Modules ℤ) :
    (derivedPullback g.toLRSHom.toShHom).obj
        ((derivedPushforward f.toLRSHom.toShHom).obj
          (((derivedSheafHom X.sheaf).obj (op E)).obj (DerivedCategory.Q.obj G))) ⟶
      (derivedPushforward f'.toLRSHom.toShHom).obj
        (((derivedSheafHom X'.sheaf).obj
            (op ((derivedPullback g'.toLRSHom.toShHom).obj E))).obj
          (DerivedCategory.Q.obj ((pullbackComplex g'.toLRSHom.toShHom).obj G)))
```

**`AlgebraicGeometry.isIso_sheafHomFlatBaseChangeMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomPerfectFlatPushforwardBaseChange.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomPerfectFlatPushforwardBaseChange.lean#L120). The attribute's comment: “case (1): E perfect, 𝒢^• bounded above with terms quasi-coherent and flat over S, f quasi-compact and quasi-separated, an arbitrary cartesian square; the canonical map of the source's proof, with the ORDINARY pullback (g')^*𝒢^• on the right, is an isomorphism. Case (2) is false as stated (errata.md, entry 08IE(2)); its corrected form, for g of finite Tor dimension, is `isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent_of_hasFiniteTorDimension`”.

> **Stacks 08IE, case (1).** Let `f : X ⟶ S` be a quasi-compact and quasi-separated morphism
> of schemes, let `E` be a perfect object of `D(𝒪_X)` and let `𝒢^•` be a bounded above complex of
> quasi-coherent `𝒪_X`-modules whose terms are flat over `S`. For every cartesian square
>
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> S' --g---> S
> ```
>
> the canonical map
>
> `Lg^*Rf_*R𝓗om(E, 𝒢^•) ⟶ Rf'_*R𝓗om(L(g')^*E, (g')^*𝒢^•)`
>
> of `AlgebraicGeometry.sheafHomFlatBaseChangeMap`, with the **ordinary** pullback `(g')^*𝒢^•` on
> the right as the source insists, is an isomorphism: the formation of `Rf_*R𝓗om(E, 𝒢^•)`
> commutes with arbitrary base change.

```lean
public theorem isIso_sheafHomFlatBaseChangeMap_of_isPerfect
    {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
    (hsq : IsPullback g' f' f g) (hqc : QuasiCompact f) (hqs : QuasiSeparated f)
    (sq : g'.toLRSHom.toShHom ≫ f.toLRSHom.toShHom =
      f'.toLRSHom.toShHom ≫ g.toLRSHom.toShHom)
    (E : DerivedCategory X.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (G : CochainComplex X.Modules ℤ)
    (hGminus : CochainComplex.minus X.Modules G)
    (hGqcoh : ∀ n : ℤ, (G.X n).IsQuasicoherent)
    (hGflat : ∀ n : ℤ, IsFlatOver f.toLRSHom.toShHom (G.X n)) :
    IsIso (sheafHomFlatBaseChangeMap f g f' g' sq E G)
```

**`AlgebraicGeometry.isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent_of_hasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomPseudoCoherentFiniteTorDimensionBaseChange.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomPseudoCoherentFiniteTorDimensionBaseChange.lean#L248). The attribute's comment: “case (2), with the correction of errata.md (entry 08IE(2)): f quasi-compact and quasi-separated, E pseudo-coherent, 𝒢^• bounded with terms quasi-coherent and flat over S, and g of finite Tor dimension, read at the stalks (each 𝒪\_\{S', s'} of finite Tor dimension over 𝒪\_\{S, g(s')}, which finite Tor dimension of g implies); the canonical map of the source's proof, with the ORDINARY pullback (g')^*𝒢^• on the right, is an isomorphism. Without the condition on g case (2) is false (the counterexample over ℤ/4 of the erratum)”.

> **Stacks 08IE, case (2), corrected.** Let `f : X ⟶ S` be a quasi-compact and quasi-separated
> morphism of schemes, let `E` be a pseudo-coherent object of `D(𝒪_X)` and let `𝒢^•` be a bounded
> complex of quasi-coherent `𝒪_X`-modules whose terms are flat over `S`. For every cartesian square
>
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> S' --g---> S
> ```
>
> in which `g` has finite Tor dimension at the stalks — every local ring `𝒪_{S', s'}` has finite Tor
> dimension over `𝒪_{S, g(s')}`, the correction of case (2) recorded in `errata.md` (entry
> **08IE(2)**) — the canonical map
>
> `Lg^*Rf_*R𝓗om(E, 𝒢^•) ⟶ Rf'_*R𝓗om(L(g')^*E, (g')^*𝒢^•)`
>
> of `AlgebraicGeometry.sheafHomFlatBaseChangeMap`, with the **ordinary** pullback `(g')^*𝒢^•` on
> the right, is an isomorphism. Without the condition on `g` the statement is false:
> `not_forall_isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent` in
> `Stacks.Examples.SheafHomCounterexample`.
>
> The condition on `g` is the stalkwise form of "`𝒪_{S'}` has finite Tor dimension over
> `g⁻¹𝒪_S`": it is implied by that condition, and also by its local version (Tor amplitude is a
> stalkwise condition, Stacks 09U9).

```lean
public theorem isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent_of_hasFiniteTorDimension
    {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
    (hsq : IsPullback g' f' f g) (hqc : QuasiCompact f) (hqs : QuasiSeparated f)
    (hg : ∀ s' : S', HasFiniteTorDimensionRingHom (g.stalkMap s').hom)
    (sq : g'.toLRSHom.toShHom ≫ f.toLRSHom.toShHom =
      f'.toLRSHom.toShHom ≫ g.toLRSHom.toShHom)
    (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E)
    (G : CochainComplex X.Modules ℤ) (a b : ℤ) (hGge : G.IsStrictlyGE a)
    (hGle : G.IsStrictlyLE b)
    (hGqcoh : ∀ n : ℤ, (G.X n).IsQuasicoherent)
    (hGflat : ∀ n : ℤ, IsFlatOver f.toLRSHom.toShHom (G.X n)) :
    IsIso (sheafHomFlatBaseChangeMap f g f' g' sq E G)
```

**`AlgebraicGeometry.isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent_of_hasFiniteTorDimension_appLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomPseudoCoherentFiniteTorDimensionBaseChange.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomPseudoCoherentFiniteTorDimensionBaseChange.lean#L297). The attribute's comment: “case (2), with the correction of errata.md (entry 08IE(2)) in the affine-open form the erratum spells out: for affine opens V ⊆ S and V' ⊆ g⁻¹(V), 𝒪\_\{S'}(V') has finite Tor dimension over 𝒪\_S(V); f quasi-compact and quasi-separated, E pseudo-coherent, 𝒢^• bounded with terms quasi-coherent and flat over S; the canonical map, with the ORDINARY pullback (g')^*𝒢^•, is an isomorphism”.

> **Stacks 08IE, case (2), corrected, with the condition on `g` on affine opens.** This is
> `isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent_of_hasFiniteTorDimension` with the correction
> of `errata.md` (entry **08IE(2)**) read on affine opens as the erratum spells it out: for all affine
> opens `V ⊆ S` and `V' ⊆ g⁻¹(V)` the ring `𝒪_{S'}(V')` has finite Tor dimension over `𝒪_S(V)`. The
> hypotheses on `f`, `E` and `𝒢^•` are those of the source.

```lean
public theorem isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent_of_hasFiniteTorDimension_appLE
    {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
    (hsq : IsPullback g' f' f g) (hqc : QuasiCompact f) (hqs : QuasiSeparated f)
    (hg : ∀ (V : S.Opens) (V' : S'.Opens), IsAffineOpen V → IsAffineOpen V' →
      ∀ hle : V' ≤ g ⁻¹ᵁ V, HasFiniteTorDimensionRingHom (g.appLE V V' hle).hom)
    (sq : g'.toLRSHom.toShHom ≫ f.toLRSHom.toShHom =
      f'.toLRSHom.toShHom ≫ g.toLRSHom.toShHom)
    (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E)
    (G : CochainComplex X.Modules ℤ) (a b : ℤ) (hGge : G.IsStrictlyGE a)
    (hGle : G.IsStrictlyLE b)
    (hGqcoh : ∀ n : ℤ, (G.X n).IsQuasicoherent)
    (hGflat : ∀ n : ℤ, IsFlatOver f.toLRSHom.toShHom (G.X n)) :
    IsIso (sheafHomFlatBaseChangeMap f g f' g' sq E G)
```

**`Stacks.Examples.SheafHomCounterexample.not_forall_isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/BaseChange/SheafHomPseudoCoherentCounterexample.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/BaseChange/SheafHomPseudoCoherentCounterexample.lean#L297). The attribute's comment: “the erratum's counterexample: case (2) for an ARBITRARY base change is false; it fails for S = X = Spec ℤ/4, f = id, E = (ℤ/2)~, 𝒢^• = 𝒪\_X and g : Spec ℤ/2 ⟶ Spec ℤ/4”.

> It is not true that for every quasi-compact
> and quasi-separated `f : X ⟶ S`, every pseudo-coherent `E ∈ D(𝒪_X)`, every bounded complex
> `𝒢^•` of quasi-coherent `𝒪_X`-modules flat over `S` and every cartesian square, the canonical map
> `Lg^*Rf_*R𝓗om(E, 𝒢^•) ⟶ Rf'_*R𝓗om(L(g')^*E, (g')^*𝒢^•)` of
> `AlgebraicGeometry.sheafHomFlatBaseChangeMap` is an isomorphism.

```lean
theorem not_forall_isIso_sheafHomFlatBaseChangeMap_of_isPseudoCoherent :
    ¬ ∀ {X X' S S' : Scheme.{0}} (f : X ⟶ S) (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
      (_ : IsPullback g' f' f g) (_ : QuasiCompact f) (_ : QuasiSeparated f)
      (sq : g'.toLRSHom.toShHom ≫ f.toLRSHom.toShHom =
        f'.toLRSHom.toShHom ≫ g.toLRSHom.toShHom)
      (E : DerivedCategory X.Modules) (_ : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E)
      (G : CochainComplex X.Modules ℤ) (a b : ℤ) (_ : G.IsStrictlyGE a) (_ : G.IsStrictlyLE b)
      (_ : ∀ n : ℤ, (G.X n).IsQuasicoherent)
      (_ : ∀ n : ℤ, IsFlatOver f.toLRSHom.toShHom (G.X n)),
      IsIso (sheafHomFlatBaseChangeMap f g f' g' sq E G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.26, Tag 0DJ6](https://stacks.math.columbia.edu/tag/0DJ6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
