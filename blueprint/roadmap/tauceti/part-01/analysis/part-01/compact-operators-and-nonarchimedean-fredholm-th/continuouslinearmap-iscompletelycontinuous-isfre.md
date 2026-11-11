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
- [Source of `ContinuousLinearMap.IsCompletelyContinuous.isFredholm_one_sub` in TauCeti/Analysis/Fredholm/CompletelyContinuous.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fredholm/CompletelyContinuous.lean#L71)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
