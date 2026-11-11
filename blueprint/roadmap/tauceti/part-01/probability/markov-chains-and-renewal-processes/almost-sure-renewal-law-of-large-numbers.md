---
declaration: theorem
origin: cited
lean: TauCeti.Probability.ae_tendsto_renewalCountNat_div
statement: formalized
proof: formalized
---

# Almost-sure renewal law of large numbers

The count per unit time converges to the
reciprocal of the extended mean increment, with rate zero for infinite mean. The convergence
holds along the full nonnegative real time axis on a single event of probability one.
Pairwise independence suffices; the identical-distribution hypothesis supplies almost-everywhere
measurability of the increments.

```lean
TauCeti.Probability.ae_tendsto_renewalCountNat_div.{u_1} {Ω : Type u_1} {T : ℕ → Ω → NNReal}
  [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure P]
  (hindep : Pairwise fun i j => ProbabilityTheory.IndepFun (T i) (T j) P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P)
  (hzero : P {ω | T 0 ω = 0} < 1) :
  ∀ᵐ (ω : Ω) ∂P,
    Filter.Tendsto (fun t => ↑(TauCeti.Probability.renewalCountNat T t ω) / ↑t) Filter.atTop
      (nhds (∫⁻ (ω : Ω), ↑(T 0 ω) ∂P)⁻¹.toReal)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.ae_tendsto_renewalCountNat_div`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/StrongLaw.html#TauCeti.Probability.ae_tendsto_renewalCountNat_div).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.ae_tendsto_renewalCountNat_div`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/StrongLaw.html#TauCeti.Probability.ae_tendsto_renewalCountNat_div)
- [Source of `TauCeti.Probability.ae_tendsto_renewalCountNat_div` in TauCeti/Probability/Renewal/StrongLaw.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Renewal/StrongLaw.lean#L123)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
