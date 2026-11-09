---
declaration: theorem
origin: cited
lean: TauCeti.Probability.lintegral_renewalCount_pow_lt_top
statement: formalized
proof: formalized
---

# Finite moments of the renewal counts

For independent, identically distributed increments
that are not almost surely zero, every count `renewalCount T t` has a finite moment of every
order `p`. No assumption is made on the mean of the increments.

```lean
TauCeti.Probability.lintegral_renewalCount_pow_lt_top.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  {P : MeasureTheory.Measure Ω} {T : ℕ → Ω → NNReal} (hT : ∀ (n : ℕ), Measurable (T n))
  (hindep : ProbabilityTheory.iIndepFun T P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P) (hzero : P {ω | T 0 ω = 0} < 1)
  (t : NNReal) (p : ℕ) : ∫⁻ (ω : Ω), TauCeti.Probability.renewalCount T t ω ^ p ∂P < ⊤
```

## Depends on

- [TauCeti.Probability.renewalCount](tauceti-probability-renewalcount.md)

## Proof depends on

- [Chernoff bound for the arrival times](chernoff-bound-for-the-arrival-times.md)
- [Finiteness of the renewal counts](finiteness-of-the-renewal-counts.md)
- [TauCeti.Probability.renewalCount_eq_natCast_iff](tauceti-probability-renewalcount-eq-natcast-iff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.lintegral_renewalCount_pow_lt_top`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Moments.html#TauCeti.Probability.lintegral_renewalCount_pow_lt_top).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.lintegral_renewalCount_pow_lt_top`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Moments.html#TauCeti.Probability.lintegral_renewalCount_pow_lt_top)
- [Source of `TauCeti.Probability.lintegral_renewalCount_pow_lt_top` in TauCeti/Probability/Renewal/Moments.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Renewal/Moments.lean#L214)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
