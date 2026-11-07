---
declaration: def
origin: cited
lean: TauCeti.Probability.renewalCount
statement: formalized
---

# TauCeti.Probability.renewalCount

The number `#{n ≥ 1 | arrival T n ω ≤ t}` of arrivals in `[0, t]`, counted with multiplicity,
as an extended nonnegative number. The artificial arrival `arrival T 0 = 0` is not counted.

```lean
TauCeti.Probability.renewalCount.{u_1} {Ω : Type u_1} (T : ℕ → Ω → NNReal) (t : NNReal) (ω : Ω) :
  ENNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.renewalCount`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Basic.html#TauCeti.Probability.renewalCount).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.renewalCount`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/Basic.html#TauCeti.Probability.renewalCount)
- [Source of `TauCeti.Probability.renewalCount` in TauCeti/Probability/Renewal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Renewal/Basic.lean#L141)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
