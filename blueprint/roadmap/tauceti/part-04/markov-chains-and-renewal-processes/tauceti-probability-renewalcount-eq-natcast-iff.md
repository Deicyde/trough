---
declaration: theorem
origin: cited
lean: TauCeti.Probability.renewalCount_eq_natCast_iff
statement: formalized
proof: formalized
---

# TauCeti.Probability.renewalCount_eq_natCast_iff

The count at time `t` equals `n` exactly when `arrival T n ω ≤ t < arrival T (n + 1) ω`.

```lean
TauCeti.Probability.renewalCount_eq_natCast_iff.{u_1} {Ω : Type u_1} {T : ℕ → Ω → NNReal}
  {t : NNReal} {ω : Ω} {n : ℕ} :
  TauCeti.Probability.renewalCount T t ω = ↑n ↔
    TauCeti.Probability.arrival T n ω ≤ t ∧ t < TauCeti.Probability.arrival T (n + 1) ω
```

## Depends on

- [TauCeti.Probability.renewalCount](tauceti-probability-renewalcount.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.renewalCount_eq_natCast_iff`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Basic.html#TauCeti.Probability.renewalCount_eq_natCast_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.renewalCount_eq_natCast_iff`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Basic.html#TauCeti.Probability.renewalCount_eq_natCast_iff)
- [Source of `TauCeti.Probability.renewalCount_eq_natCast_iff` in TauCeti/Probability/Renewal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Renewal/Basic.lean#L187)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
