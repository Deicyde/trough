---
declaration: theorem
origin: cited
lean: TauCeti.Probability.ae_renewalCount_lt_top
statement: formalized
proof: formalized
---

# Finiteness of the renewal counts

For independent, identically distributed increments
that are not almost surely zero, almost surely every count `renewalCount T t` is finite. The
almost-sure quantifier is outside the quantifier over all times.

```lean
TauCeti.Probability.ae_renewalCount_lt_top.{u_1} {Ω : Type u_1} {T : ℕ → Ω → NNReal}
  [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω} (hindep : ProbabilityTheory.iIndepFun T P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P)
  (hzero : P {ω | T 0 ω = 0} < 1) :
  ∀ᵐ (ω : Ω) ∂P, ∀ (t : NNReal), TauCeti.Probability.renewalCount T t ω < ⊤
```

## Depends on

- [TauCeti.Probability.renewalCount](tauceti-probability-renewalcount.md)

## Proof depends on

- [Nonexplosion of a renewal process](nonexplosion-of-a-renewal-process.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.ae_renewalCount_lt_top`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Basic.html#TauCeti.Probability.ae_renewalCount_lt_top).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.ae_renewalCount_lt_top`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Basic.html#TauCeti.Probability.ae_renewalCount_lt_top)
- [Source of `TauCeti.Probability.ae_renewalCount_lt_top` in TauCeti/Probability/Renewal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Renewal/Basic.lean#L320)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
