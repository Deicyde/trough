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

- [TauCeti.Complexification](../../../../part-01/analysis/part-02/one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.metricChangeCompositionCorrection`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Composition.html#ContinuousLinearMap.metricChangeCompositionCorrection).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.metricChangeCompositionCorrection`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Composition.html#ContinuousLinearMap.metricChangeCompositionCorrection)
- [Source of `ContinuousLinearMap.metricChangeCompositionCorrection` in TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Composition.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Positive/MetricChange/Composition.lean#L206)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
