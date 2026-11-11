---
declaration: theorem
origin: cited
lean: TauCeti.Probability.eq_renewalConv_renewalMeasure
statement: formalized
proof: formalized
---

# Uniqueness for the renewal equation

If the renewal measure `U` of `F` is locally finite,
`h` is measurable and bounded on each `[0, t]`, and `g` is a measurable solution of
`g = h + g ∗ F` that is bounded on each `[0, t]`, then `g = h ∗ U`.

```lean
TauCeti.Probability.eq_renewalConv_renewalMeasure {h g : NNReal → ℝ}
  {μ : MeasureTheory.Measure NNReal} [MeasureTheory.IsLocallyFiniteMeasure μ.renewalMeasure]
  [MeasureTheory.SFinite μ] (hh : Measurable h) (hhb : ∀ (t : NNReal), ∃ C, ∀ s ≤ t, |h s| ≤ C)
  (hg : Measurable g) (hgb : ∀ (t : NNReal), ∃ C, ∀ s ≤ t, |g s| ≤ C)
  (hgeq : g = h + TauCeti.Probability.renewalConv g μ) :
  g = TauCeti.Probability.renewalConv h μ.renewalMeasure
```

## Depends on

- [MeasureTheory.Measure.renewalMeasure](measuretheory-measure-renewalmeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.eq_renewalConv_renewalMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Equation.html#TauCeti.Probability.eq_renewalConv_renewalMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.eq_renewalConv_renewalMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Equation.html#TauCeti.Probability.eq_renewalConv_renewalMeasure)
- [Source of `TauCeti.Probability.eq_renewalConv_renewalMeasure` in TauCeti/Probability/Renewal/Equation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Renewal/Equation.lean#L403)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
