---
declaration: theorem
origin: cited
lean: TauCeti.norm_logGamma_sub_stirling_le
statement: formalized
proof: formalized
---

# Stirling's formula on a sector, with an explicit constant

for `0 < δ < π` and nonzero
`s` with `|arg s| ≤ π - δ`,
`‖logGamma s - ((s - 1/2) log s - s + log (2π) / 2)‖ ≤ 2 / ((1 - cos δ) ^ 3 ‖s‖)`.

```lean
TauCeti.norm_logGamma_sub_stirling_le {s : ℂ} {δ : ℝ} (hδ : 0 < δ) (hδπ : δ < Real.pi)
  (hs : |s.arg| ≤ Real.pi - δ) (hs0 : s ≠ 0) :
  ‖TauCeti.logGamma s - ((s - 1 / 2) * Complex.log s - s + ↑(Real.log (2 * Real.pi) / 2))‖ ≤
    2 / ((1 - Real.cos δ) ^ 3 * ‖s‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_logGamma_sub_stirling_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Basic.html#TauCeti.norm_logGamma_sub_stirling_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_logGamma_sub_stirling_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Basic.html#TauCeti.norm_logGamma_sub_stirling_le)
- [Source of `TauCeti.norm_logGamma_sub_stirling_le` in TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Basic.lean#L256)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
