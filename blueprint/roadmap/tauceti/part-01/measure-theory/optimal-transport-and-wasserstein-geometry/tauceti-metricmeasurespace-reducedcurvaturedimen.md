---
declaration: def
origin: cited
lean: TauCeti.MetricMeasureSpace.ReducedCurvatureDimension
statement: formalized
---

# TauCeti.MetricMeasureSpace.ReducedCurvatureDimension

The **reduced curvature-dimension condition** `CD*(K, N)` of Bacher and Sturm: the condition
`CD(K, N)` (`TauCeti.MetricMeasureSpace.CurvatureDimension`) with the distortion coefficient
`σ_{K,N'}` (`TauCeti.distortionSigma`) in place of `τ_{K,N'}`. That is, `m` has full support, and
any two laws `μ₀`, `μ₁` of bounded support, absolutely continuous with respect to `m`, admit an
optimal coupling `q` for the quadratic cost and a `W₂`-geodesic `(μ_t)` of such laws along which
`S_{N'}(μ_t | m) ≤ T_{σ_{K,N'}}^{(t)}(q | m)` for every `t ∈ [0, 1]` and every `N' ≥ N`.

The condition is meant for `N ≥ 1`, where the coefficients carry their geometric meaning.

```lean
TauCeti.MetricMeasureSpace.ReducedCurvatureDimension.{u_1} {X : Type u_1} [MetricSpace X]
  [MeasurableSpace X] [CompleteSpace X] [SecondCountableTopology X] [BorelSpace X]
  (M : TauCeti.MetricMeasureSpace X) (K N : ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MetricMeasureSpace.ReducedCurvatureDimension`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Finite.html#TauCeti.MetricMeasureSpace.ReducedCurvatureDimension).

## Sources

- [Tau Ceti documentation: `TauCeti.MetricMeasureSpace.ReducedCurvatureDimension`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Finite.html#TauCeti.MetricMeasureSpace.ReducedCurvatureDimension)
- [Source of `TauCeti.MetricMeasureSpace.ReducedCurvatureDimension` in TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Finite.lean#L131)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OptimalTransport/STATUS.md)
