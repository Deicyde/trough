---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.allOnCriticalLine_of_zeroCount_eq_one
statement: formalized
proof: formalized
---

# The symmetry criterion

If a region `R` and the divisor of `f` on it are invariant under
the reflection `s ↦ 1 - conj s` in the critical line, and `R` contains exactly one zero of `f`
counted with multiplicity, then that zero lies on the critical line. A zero off the line would
come with its distinct mirror image.

```lean
TauCeti.LFunctions.allOnCriticalLine_of_zeroCount_eq_one.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {f : ℂ → E} {U R : Set ℂ} (hR : ∀ s ∈ R, 1 - (starRingEnd ℂ) s ∈ R)
  (hdiv :
    ∀ s ∈ R, (MeromorphicOn.divisor f U) (1 - (starRingEnd ℂ) s) = (MeromorphicOn.divisor f U) s)
  (hcount : TauCeti.zeroCount f U R = 1) : TauCeti.LFunctions.AllOnCriticalLine f U R
```

## Depends on

- [TauCeti.zeroCount](tauceti-zerocount.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.allOnCriticalLine_of_zeroCount_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Zeros/CriticalLine.html#TauCeti.LFunctions.allOnCriticalLine_of_zeroCount_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.allOnCriticalLine_of_zeroCount_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Zeros/CriticalLine.html#TauCeti.LFunctions.allOnCriticalLine_of_zeroCount_eq_one)
- [Source of `TauCeti.LFunctions.allOnCriticalLine_of_zeroCount_eq_one` in TauCeti/NumberTheory/LFunctions/Zeros/CriticalLine.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Zeros/CriticalLine.lean#L63)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
