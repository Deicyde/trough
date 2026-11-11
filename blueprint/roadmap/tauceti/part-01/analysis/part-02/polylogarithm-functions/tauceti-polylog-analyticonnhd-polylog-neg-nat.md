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
- [Source of `TauCeti.Polylog.analyticOnNhd_polylog_neg_nat` in TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean#L113)
- [Tau Ceti roadmap status: Polylogarithm functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PolylogarithmFunctions/STATUS.md)
