---
declaration: theorem
origin: cited
lean: TauCeti.Probability.measureReal_arrival_le_le_exp_mul_mgf_pow
statement: formalized
proof: formalized
---

# Chernoff bound for the arrival times

For independent, identically distributed increments
and every rate `s ≥ 0`, the probability that the `n`-th arrival is at most `t` is at most
`exp (s t)` times the `n`-th power of the Laplace transform `mgf (T 0) P (-s)` of the increment
law. By `natCast_le_renewalCount_iff` this is also a bound on `P(n ≤ renewalCount T t)`.

```lean
TauCeti.Probability.measureReal_arrival_le_le_exp_mul_mgf_pow.{u_1} {Ω : Type u_1}
  [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω} {T : ℕ → Ω → NNReal}
  (hT : ∀ (n : ℕ), Measurable (T n)) (hindep : ProbabilityTheory.iIndepFun T P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P) {s : ℝ} (hs : 0 ≤ s)
  (t : NNReal) (n : ℕ) :
  P.real {ω | TauCeti.Probability.arrival T n ω ≤ t} ≤
    Real.exp (s * ↑t) * ProbabilityTheory.mgf (fun ω => ↑(T 0 ω)) P (-s) ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.measureReal_arrival_le_le_exp_mul_mgf_pow`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Moments.html#TauCeti.Probability.measureReal_arrival_le_le_exp_mul_mgf_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.measureReal_arrival_le_le_exp_mul_mgf_pow`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Moments.html#TauCeti.Probability.measureReal_arrival_le_le_exp_mul_mgf_pow)
- [Source of `TauCeti.Probability.measureReal_arrival_le_le_exp_mul_mgf_pow` in TauCeti/Probability/Renewal/Moments.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Renewal/Moments.lean#L64)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
