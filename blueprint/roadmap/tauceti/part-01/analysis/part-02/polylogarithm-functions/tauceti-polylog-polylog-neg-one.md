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
- [Source of `TauCeti.Polylog.polylog_neg_one` in TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean#L130)
- [Tau Ceti roadmap status: Polylogarithm functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PolylogarithmFunctions/STATUS.md)
