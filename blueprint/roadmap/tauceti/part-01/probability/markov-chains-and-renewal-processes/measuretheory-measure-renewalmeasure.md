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
- [Source of `MeasureTheory.Measure.renewalMeasure` in TauCeti/Probability/Renewal/Measure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Renewal/Measure.lean#L80)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
