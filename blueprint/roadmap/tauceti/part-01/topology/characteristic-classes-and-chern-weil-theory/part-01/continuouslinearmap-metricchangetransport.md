---
declaration: def
origin: cited
lean: ContinuousLinearMap.metricChangeTransport
statement: formalized
---

# ContinuousLinearMap.metricChangeTransport

The **metric change transport** of a second inner product `h` on a real Hilbert space: the
inverse square root `H ^ (-(1 / 2))` of its Riesz operator `H`, characterized by
`⟪H u, v⟫ = h u v`. When `H` is strictly positive it is an isometry from the original inner
product to `h` (`ContinuousLinearMap.apply_metricChangeTransport_metricChangeTransport`).

```lean
ContinuousLinearMap.metricChangeTransport.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [CompleteSpace E] (h : E →L[ℝ] E →L[ℝ] ℝ) : E →L[ℝ] E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Complexification](../../../analysis/part-01/one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.metricChangeTransport`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Basic.html#ContinuousLinearMap.metricChangeTransport).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.metricChangeTransport`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Basic.html#ContinuousLinearMap.metricChangeTransport)
- [Source of `ContinuousLinearMap.metricChangeTransport` in TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Basic.lean#L88)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
