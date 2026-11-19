---
declaration: theorem
origin: cited
lean: TauCeti.Polylog.analyticOnNhd_polylog_neg_nat
statement: formalized
proof: formalized
---

# TauCeti.Polylog.analyticOnNhd_polylog_neg_nat

Nonpositive weights are holomorphic on the complement of their sole pole.

```lean
TauCeti.Polylog.analyticOnNhd_polylog_neg_nat (r : ℕ) :
  AnalyticOnNhd ℂ (TauCeti.Polylog.polylog (-↑r)) {z | z ≠ 1}
```

## Depends on

- [TauCeti.Polylog.polylog](tauceti-polylog-polylog.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Polylog.analyticOnNhd_polylog_neg_nat`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.html#TauCeti.Polylog.analyticOnNhd_polylog_neg_nat).

## Sources

- [Tau Ceti documentation: `TauCeti.Polylog.analyticOnNhd_polylog_neg_nat`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.html#TauCeti.Polylog.analyticOnNhd_polylog_neg_nat)
- [Source of `TauCeti.Polylog.analyticOnNhd_polylog_neg_nat` in TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean#L113)
- [Tau Ceti roadmap status: Polylogarithm functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PolylogarithmFunctions/STATUS.md)
