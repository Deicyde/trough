---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.tendsto_renewalFunction_div, TauCeti.Probability.tendsto_integral_renewalCountNat_div
statement: formalized
proof: formalized
---

# The elementary renewal theorem

For a probability measure `μ` on `ℝ≥0` other than the
point mass at zero, the renewal function satisfies `m t / t → (𝔼 μ)⁻¹` as `t → ∞`, where the
reciprocal of the extended mean is taken before conversion to a real number, so that the limit is
zero for infinite mean.

```lean
MeasureTheory.Measure.tendsto_renewalFunction_div (μ : MeasureTheory.Measure NNReal)
  [MeasureTheory.IsProbabilityMeasure μ] (hμ : μ {0} < 1) :
  Filter.Tendsto (fun t => (μ.renewalFunction t).toReal / ↑t) Filter.atTop
    (nhds (∫⁻ (x : NNReal), ↑x ∂μ)⁻¹.toReal)
```

## Depends on

- [MeasureTheory.Measure.renewalMeasure](measuretheory-measure-renewalmeasure.md)

## Proof depends on

- [Almost-sure renewal law of large numbers](almost-sure-renewal-law-of-large-numbers.md)
- [De la Vallée Poussin's criterion](../../measure-theory/function/part-01/de-la-vallee-poussins-criterion.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.tendsto_renewalFunction_div`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/ElementaryTheorem.html#MeasureTheory.Measure.tendsto_renewalFunction_div).

## Other forms

**The elementary renewal theorem, on any realization of the increments.** Formalized in Tau Ceti as [`TauCeti.Probability.tendsto_integral_renewalCountNat_div`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/ElementaryTheorem.html#TauCeti.Probability.tendsto_integral_renewalCountNat_div).

```lean
TauCeti.Probability.tendsto_integral_renewalCountNat_div.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  {P : MeasureTheory.Measure Ω} {T : ℕ → Ω → NNReal} (hT : ∀ (n : ℕ), Measurable (T n))
  (hindep : ProbabilityTheory.iIndepFun T P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P)
  (hzero : P {ω | T 0 ω = 0} < 1) :
  Filter.Tendsto (fun t => (∫ (ω : Ω), ↑(TauCeti.Probability.renewalCountNat T t ω) ∂P) / ↑t)
    Filter.atTop (nhds (∫⁻ (ω : Ω), ↑(T 0 ω) ∂P)⁻¹.toReal)
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.tendsto_renewalFunction_div`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/ElementaryTheorem.html#MeasureTheory.Measure.tendsto_renewalFunction_div)
- [Source of `MeasureTheory.Measure.tendsto_renewalFunction_div` in TauCeti/Probability/Renewal/ElementaryTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Renewal/ElementaryTheorem.lean#L169)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
