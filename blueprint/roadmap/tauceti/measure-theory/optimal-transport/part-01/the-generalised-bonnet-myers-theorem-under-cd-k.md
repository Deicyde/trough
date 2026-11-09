---
declaration: theorem
origin: cited
lean: TauCeti.MetricMeasureSpace.CurvatureDimension.dist_le
statement: formalized
proof: formalized
---

# The generalised Bonnet–Myers theorem under `CD(K, N)`

If `M` satisfies `CD(K, N)` with
`K > 0` and `N ≥ 1`, any two points of the support of the reference measure are at distance at
most `π √((N - 1) / K)`.

```lean
TauCeti.MetricMeasureSpace.CurvatureDimension.dist_le.{u_2} {X : Type u_2} [MetricSpace X]
  [MeasurableSpace X] [CompleteSpace X] [SecondCountableTopology X] [BorelSpace X]
  {M : TauCeti.MetricMeasureSpace X} {K N : ℝ} (h : M.CurvatureDimension K N) (hK : 0 < K)
  (hN : 1 ≤ N) {x y : X} (hx : x ∈ M.support) (hy : y ∈ M.support) :
  dist x y ≤ Real.pi * √((N - 1) / K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MetricMeasureSpace.CurvatureDimension.dist_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Basic.html#TauCeti.MetricMeasureSpace.CurvatureDimension.dist_le).

## Sources

- [Tau Ceti documentation: `TauCeti.MetricMeasureSpace.CurvatureDimension.dist_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Basic.html#TauCeti.MetricMeasureSpace.CurvatureDimension.dist_le)
- [Source of `TauCeti.MetricMeasureSpace.CurvatureDimension.dist_le` in TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/CurvatureDimension/Basic.lean#L390)
