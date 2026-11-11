---
declaration: def
origin: cited
lean: MeasureTheory.Measure.renewalMeasure
statement: formalized
---

# MeasureTheory.Measure.renewalMeasure

The renewal measure `∑ n, μ^{∗n}` of a measure `μ`: the sum of all its convolution powers,
including the point mass `μ^{∗0} = δ₀`. For the law `μ` of the increments of a renewal process,
its mass on `[0, t]` is one more than the expected number of arrivals in `[0, t]`
(`renewalMeasure_Iic` and `TauCeti.Probability.lintegral_renewalCount`).

```lean
MeasureTheory.Measure.renewalMeasure.{u_1} {α : Type u_1} [MeasurableSpace α] [AddMonoid α]
  (μ : MeasureTheory.Measure α) : MeasureTheory.Measure α
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.renewalMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Measure.html#MeasureTheory.Measure.renewalMeasure).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.renewalMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Measure.html#MeasureTheory.Measure.renewalMeasure)
- [Source of `MeasureTheory.Measure.renewalMeasure` in TauCeti/Probability/Renewal/Measure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Renewal/Measure.lean#L78)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
