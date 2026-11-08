---
declaration: theorem
origin: cited
lean: TauCeti.MetricMeasureSpace.MeasureContraction.dist_le, TauCeti.MetricMeasureSpace.DistortedCurvatureDimension.diam_univ_le, TauCeti.MetricMeasureSpace.CurvatureDimension.diam_support_le, TauCeti.MetricMeasureSpace.MeasureContraction.diam_support_le
statement: formalized
proof: formalized
---

# The Bonnet–Myers diameter bound under `MCP(K, N)`

If `M` satisfies `MCP(K, N)` with
`K > 0` and `N > 0`, any two points of the support of the reference measure are at distance at
most `π √((N - 1) / K)`.

```lean
TauCeti.MetricMeasureSpace.MeasureContraction.dist_le.{u_1} {X : Type u_1} [MetricSpace X]
  [MeasurableSpace X] [CompleteSpace X] [SecondCountableTopology X] [BorelSpace X]
  {M : TauCeti.MetricMeasureSpace X} {K N : ℝ} (h : M.MeasureContraction K N) (hK : 0 < K)
  (hN : 0 < N) {x y : X} (hx : x ∈ M.support) (hy : y ∈ M.support) :
  dist x y ≤ Real.pi * √((N - 1) / K)
```

## Depends on

- [TauCeti.MetricMeasureSpace.MeasureContraction](tauceti-metricmeasurespace-measurecontraction.md)

## Proof depends on

- [The generalised Bonnet–Myers theorem under `CD(K, N)`](../../optimal-transport/the-generalised-bonnet-myers-theorem-under-cd-k.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MetricMeasureSpace.MeasureContraction.dist_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.html#TauCeti.MetricMeasureSpace.MeasureContraction.dist_le).

## Other forms

**The Bonnet–Myers diameter bound for the coefficients `β`.** Formalized in Tau Ceti as [`TauCeti.MetricMeasureSpace.DistortedCurvatureDimension.diam_univ_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Finite.html#TauCeti.MetricMeasureSpace.DistortedCurvatureDimension.diam_univ_le).

```lean
TauCeti.MetricMeasureSpace.DistortedCurvatureDimension.diam_univ_le.{u_1} {X : Type u_1}
  [MetricSpace X] [MeasurableSpace X] [CompleteSpace X] [SecondCountableTopology X] [BorelSpace X]
  {M : TauCeti.MetricMeasureSpace X} {β : ℝ → ℝ → ℝ → ENNReal} {N D : ℝ}
  (h : M.DistortedCurvatureDimension β N) (hN : 0 < N) (hD : 0 ≤ D)
  (hβ : ∀ (θ : ℝ), D < θ → β N 1 θ = ⊤) : Metric.diam Set.univ ≤ D
```

**The Bonnet–Myers diameter bound under `CD(K, N)`, for `K > 0` and `N ≥ 1`.** Formalized in Tau Ceti as [`TauCeti.MetricMeasureSpace.CurvatureDimension.diam_support_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Basic.html#TauCeti.MetricMeasureSpace.CurvatureDimension.diam_support_le).

```lean
TauCeti.MetricMeasureSpace.CurvatureDimension.diam_support_le.{u_2} {X : Type u_2} [MetricSpace X]
  [MeasurableSpace X] [CompleteSpace X] [SecondCountableTopology X] [BorelSpace X]
  {M : TauCeti.MetricMeasureSpace X} {K N : ℝ} (h : M.CurvatureDimension K N) (hK : 0 < K)
  (hN : 1 ≤ N) : Metric.diam M.support ≤ Real.pi * √((N - 1) / K)
```

**The Bonnet–Myers diameter bound under `MCP(K, N)`, for `K > 0` and `N > 0`.** Formalized in Tau Ceti as [`TauCeti.MetricMeasureSpace.MeasureContraction.diam_support_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.html#TauCeti.MetricMeasureSpace.MeasureContraction.diam_support_le).

```lean
TauCeti.MetricMeasureSpace.MeasureContraction.diam_support_le.{u_1} {X : Type u_1} [MetricSpace X]
  [MeasurableSpace X] [CompleteSpace X] [SecondCountableTopology X] [BorelSpace X]
  {M : TauCeti.MetricMeasureSpace X} {K N : ℝ} (h : M.MeasureContraction K N) (hK : 0 < K)
  (hN : 0 < N) : Metric.diam M.support ≤ Real.pi * √((N - 1) / K)
```

## Sources

- [Tau Ceti documentation: `TauCeti.MetricMeasureSpace.MeasureContraction.dist_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.html#TauCeti.MetricMeasureSpace.MeasureContraction.dist_le)
- [Source of `TauCeti.MetricMeasureSpace.MeasureContraction.dist_le` in TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.lean#L133)
