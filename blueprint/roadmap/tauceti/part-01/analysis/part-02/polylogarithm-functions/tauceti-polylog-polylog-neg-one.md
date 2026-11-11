---
declaration: theorem
origin: cited
lean: TauCeti.Polylog.polylog_neg_one
statement: formalized
proof: formalized
---

# TauCeti.Polylog.polylog_neg_one

The first Euler derivative has numerator `z`, not `1`.

```lean
TauCeti.Polylog.polylog_neg_one {z : ℂ} (hz : z ≠ 1) :
  TauCeti.Polylog.polylog (-1) z = z / (1 - z) ^ 2
```

## Depends on

- [TauCeti.Polylog.polylog](tauceti-polylog-polylog.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Polylog.polylog_neg_one`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.html#TauCeti.Polylog.polylog_neg_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Polylog.polylog_neg_one`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.html#TauCeti.Polylog.polylog_neg_one)
- [Source of `TauCeti.Polylog.polylog_neg_one` in TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean#L130)
- [Tau Ceti roadmap status: Polylogarithm functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PolylogarithmFunctions/STATUS.md)
