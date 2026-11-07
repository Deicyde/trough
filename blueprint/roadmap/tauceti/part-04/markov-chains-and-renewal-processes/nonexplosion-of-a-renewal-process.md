---
declaration: theorem
origin: cited
lean: TauCeti.Probability.ae_tendsto_arrival_atTop
statement: formalized
proof: formalized
---

# Nonexplosion of a renewal process

If the increments are independent, identically
distributed and not almost surely zero, then almost surely the arrival times tend to infinity.

```lean
TauCeti.Probability.ae_tendsto_arrival_atTop.{u_1} {Ω : Type u_1} {T : ℕ → Ω → NNReal}
  [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω} (hindep : ProbabilityTheory.iIndepFun T P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P)
  (hzero : P {ω | T 0 ω = 0} < 1) :
  ∀ᵐ (ω : Ω) ∂P,
    Filter.Tendsto (fun n => TauCeti.Probability.arrival T n ω) Filter.atTop Filter.atTop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.ae_tendsto_arrival_atTop`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Basic.html#TauCeti.Probability.ae_tendsto_arrival_atTop).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.ae_tendsto_arrival_atTop`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Basic.html#TauCeti.Probability.ae_tendsto_arrival_atTop)
- [Source of `TauCeti.Probability.ae_tendsto_arrival_atTop` in TauCeti/Probability/Renewal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Renewal/Basic.lean#L278)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
