---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.renewalMeasure_Icc_add_le
statement: formalized
proof: formalized
---

# The local renewal bound

For a probability measure `μ` on `ℝ≥0`, the renewal measure `U` of
`μ` gives the interval `[t, t + h]` at most the mass it gives `[0, h]`. Both sides count the point
mass `μ^{∗0} = δ₀`, and both may be infinite: no assumption is made on the atom of `μ` at zero or on
its mean.

```lean
MeasureTheory.Measure.renewalMeasure_Icc_add_le (μ : MeasureTheory.Measure NNReal)
  [MeasureTheory.IsProbabilityMeasure μ] (t h : NNReal) :
  μ.renewalMeasure (Set.Icc t (t + h)) ≤ μ.renewalMeasure (Set.Iic h)
```

## Depends on

- [MeasureTheory.Measure.renewalMeasure](measuretheory-measure-renewalmeasure.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.renewalMeasure_Icc_add_le`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/LocalBound.html#MeasureTheory.Measure.renewalMeasure_Icc_add_le).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.renewalMeasure_Icc_add_le`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/LocalBound.html#MeasureTheory.Measure.renewalMeasure_Icc_add_le)
- [Source of `MeasureTheory.Measure.renewalMeasure_Icc_add_le` in TauCeti/Probability/Renewal/LocalBound.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Renewal/LocalBound.lean#L176)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
