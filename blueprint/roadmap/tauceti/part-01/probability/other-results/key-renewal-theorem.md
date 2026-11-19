---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.tendsto_renewalConv, MeasureTheory.Measure.tendsto_renewalConv_sub_dirac
statement: formalized
proof: formalized
---

# Key renewal theorem

For nonnegative decreasing integrable forcing and a
nonlattice interarrival law, convolution against the full renewal measure converges
to the forcing integral times the reciprocal extended mean. This includes infinite
mean and interarrival laws with an atom at zero.

```lean
MeasureTheory.Measure.tendsto_renewalConv (F : MeasureTheory.Measure NNReal)
  [MeasureTheory.IsProbabilityMeasure F] (hNL : ¬F.IsLattice) {h : NNReal → ℝ} (hh : Antitone h)
  (h₀ : ∀ (x : NNReal), 0 ≤ h x)
  (hint : MeasureTheory.IntegrableOn (fun x => h x.toNNReal) (Set.Ioi 0) MeasureTheory.volume) :
  Filter.Tendsto (TauCeti.Probability.renewalConv h F.renewalMeasure) Filter.atTop
    (nhds ((∫⁻ (x : NNReal), ↑x ∂F)⁻¹.toReal * ∫ (x : ℝ) in Set.Ioi 0, h x.toNNReal))
```

## Depends on

- [MeasureTheory.Measure.renewalMeasure](../markov-chains-and-renewal-processes/measuretheory-measure-renewalmeasure.md)

## Proof depends on

- [Nonlattice Blackwell theorem](../markov-chains-and-renewal-processes/nonlattice-blackwell-theorem.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.tendsto_renewalConv`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/KeyTheorem.html#MeasureTheory.Measure.tendsto_renewalConv).

## Other forms

**Key renewal theorem, excluding the artificial arrival.** Formalized in Tau Ceti as [`MeasureTheory.Measure.tendsto_renewalConv_sub_dirac`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/KeyTheorem.html#MeasureTheory.Measure.tendsto_renewalConv_sub_dirac).

```lean
MeasureTheory.Measure.tendsto_renewalConv_sub_dirac (F : MeasureTheory.Measure NNReal)
  [MeasureTheory.IsProbabilityMeasure F] (hNL : ¬F.IsLattice) {h : NNReal → ℝ} (hh : Antitone h)
  (h₀ : ∀ (x : NNReal), 0 ≤ h x)
  (hint : MeasureTheory.IntegrableOn (fun x => h x.toNNReal) (Set.Ioi 0) MeasureTheory.volume) :
  Filter.Tendsto
    (TauCeti.Probability.renewalConv h (F.renewalMeasure - MeasureTheory.Measure.dirac 0))
    Filter.atTop (nhds ((∫⁻ (x : NNReal), ↑x ∂F)⁻¹.toReal * ∫ (x : ℝ) in Set.Ioi 0, h x.toNNReal))
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.tendsto_renewalConv`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/KeyTheorem.html#MeasureTheory.Measure.tendsto_renewalConv)
- [Source of `MeasureTheory.Measure.tendsto_renewalConv` in TauCeti/Probability/Renewal/KeyTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Renewal/KeyTheorem.lean#L60)
