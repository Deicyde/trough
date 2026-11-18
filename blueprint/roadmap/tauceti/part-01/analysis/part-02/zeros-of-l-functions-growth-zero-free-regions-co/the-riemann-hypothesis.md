---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.allOnCriticalLine_completedRiemannZeta_iff
statement: formalized
proof: formalized
---

# The Riemann hypothesis

**The Riemann hypothesis** says exactly that every zero of the completed Riemann zeta
function lies on the critical line.

```lean
TauCeti.LFunctions.allOnCriticalLine_completedRiemannZeta_iff :
  TauCeti.LFunctions.AllOnCriticalLine completedRiemannZeta Set.univ Set.univ ↔ RiemannHypothesis
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.allOnCriticalLine_completedRiemannZeta_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Zeros/CriticalLine.html#TauCeti.LFunctions.allOnCriticalLine_completedRiemannZeta_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.allOnCriticalLine_completedRiemannZeta_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Zeros/CriticalLine.html#TauCeti.LFunctions.allOnCriticalLine_completedRiemannZeta_iff)
- [Source of `TauCeti.LFunctions.allOnCriticalLine_completedRiemannZeta_iff` in TauCeti/NumberTheory/LFunctions/Zeros/CriticalLine.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Zeros/CriticalLine.lean#L109)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
