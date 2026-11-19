---
declaration: theorem
origin: cited
lean: Real.abs_log_floor_factorial_sub_le
statement: formalized
proof: formalized
---

# Real.abs_log_floor_factorial_sub_le

The two-sided estimate `|log ⌊x⌋₊! - (x log x - x)| ≤ (1 / 2) log x + 1` for real `x ≥ 1`.

```lean
Real.abs_log_floor_factorial_sub_le {x : ℝ} (hx : 1 ≤ x) :
  |Real.log ↑⌊x⌋₊.factorial - (x * Real.log x - x)| ≤ Real.log x / 2 + 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Real.abs_log_floor_factorial_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Log/Factorial.html#Real.abs_log_floor_factorial_sub_le).

## Sources

- [Tau Ceti documentation: `Real.abs_log_floor_factorial_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Log/Factorial.html#Real.abs_log_floor_factorial_sub_le)
- [Source of `Real.abs_log_floor_factorial_sub_le` in TauCeti/Analysis/SpecialFunctions/Log/Factorial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Log/Factorial.lean#L94)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
