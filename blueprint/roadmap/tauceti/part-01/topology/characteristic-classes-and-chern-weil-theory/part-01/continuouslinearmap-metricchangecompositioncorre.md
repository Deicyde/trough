---
declaration: def
origin: cited
lean: ContinuousLinearMap.metricChangeCompositionCorrection
statement: formalized
---

# ContinuousLinearMap.metricChangeCompositionCorrection

The explicit orthogonal correction comparing successive metric changes through `h`
with direct transport to `k`. Its operator is
`CFC.sqrt k♯ * h.metricChangeTransport *
(k.bilinearComp h.metricChangeTransport h.metricChangeTransport).metricChangeTransport`,
where `k♯` is the Riesz operator of `k`.

```lean
ContinuousLinearMap.metricChangeCompositionCorrection.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [CompleteSpace E] (h k : E →L[ℝ] E →L[ℝ] ℝ)
  (hH : IsStrictlyPositive (InnerProductSpace.continuousLinearMapOfBilin h))
  (hK : IsStrictlyPositive (InnerProductSpace.continuousLinearMapOfBilin k)) : E ≃ₗᵢ[ℝ] E
```

## Depends on

- [ContinuousLinearMap.metricChangeTransport](continuouslinearmap-metricchangetransport.md)

## Proof depends on

- [TauCeti.Complexification](../../../analysis/part-01/one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.metricChangeCompositionCorrection`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Composition.html#ContinuousLinearMap.metricChangeCompositionCorrection).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.metricChangeCompositionCorrection`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Composition.html#ContinuousLinearMap.metricChangeCompositionCorrection)
- [Source of `ContinuousLinearMap.metricChangeCompositionCorrection` in TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Composition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Composition.lean#L206)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
