---
declaration: def
origin: cited
lean: TauCeti.MetricMeasureSpace.MeasureContraction
statement: formalized
---

# TauCeti.MetricMeasureSpace.MeasureContraction

The **measure-contraction property** `MCP(K, N)` of Ohta and Sturm, in the form of
Cavalletti–Mondino: for every point `o` of the support of the reference measure `m` and every
measurable `A` with `0 < m(A) < ∞`, some dynamic plan `η` concentrated on geodesics has law
`m[|A] = m(A)⁻¹ m|_A` at time `0` and law `δ_o` at time `1`, and for every time `t` the law at
time `t` of `η` weighted by `τ_{K,N}^{(1-t)}(d(γ₀, γ₁))^N` is at most `m(A)⁻¹ m`.

Such a plan is automatically optimal, since `m[|A]` and `δ_o` have only one coupling.

```lean
TauCeti.MetricMeasureSpace.MeasureContraction.{u_1} {X : Type u_1} [MetricSpace X]
  [MeasurableSpace X] [CompleteSpace X] [SecondCountableTopology X] [BorelSpace X]
  (M : TauCeti.MetricMeasureSpace X) (K N : ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MetricMeasureSpace.MeasureContraction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.html#TauCeti.MetricMeasureSpace.MeasureContraction).

## Sources

- [Tau Ceti documentation: `TauCeti.MetricMeasureSpace.MeasureContraction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.html#TauCeti.MetricMeasureSpace.MeasureContraction)
- [Source of `TauCeti.MetricMeasureSpace.MeasureContraction` in TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/MeasureContraction.lean#L97)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
