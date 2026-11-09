---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub
statement: formalized
proof: formalized
---

# ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub

A completely continuous perturbation of the identity is a Fredholm operator, over any
complete nontrivially normed field.

```lean
ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub.{u_1, u_2} {K : Type u_1}
  {E : Type u_2} [NontriviallyNormedField K] [CompleteSpace K] [NormedAddCommGroup E]
  [NormedSpace K E] [CompleteSpace E] {u : E →L[K] E} (hu : u.IsCompletelyContinuous) :
  (1 - u).IsFredholm
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/CompletelyContinuous.html#ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/CompletelyContinuous.html#ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub)
- [Source of `ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub` in TauCeti/Analysis/Fredholm/CompletelyContinuous.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fredholm/CompletelyContinuous.lean#L68)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
