---
declaration: def
origin: cited
lean: ContinuousLinearMap.singularValue
statement: formalized
---

# ContinuousLinearMap.singularValue

The `n`-th approximation number `aₙ(T)` of a bounded linear map `T`: the infimum of the
operator norms `‖T - R‖` over all bounded linear maps `R` of rank at most `n`. The indexing is
zero-based, so `a₀(T) = ‖T‖` (`singularValue_zero`).

On finite-dimensional Hilbert spaces these are the singular values of `T`.

```lean
ContinuousLinearMap.singularValue.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [NontriviallyNormedField 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [SeminormedAddCommGroup F] [NormedSpace 𝕜 F] (T : E →L[𝕜] F) (n : ℕ) : NNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.singularValue`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Basic.html#ContinuousLinearMap.singularValue).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.singularValue`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Basic.html#ContinuousLinearMap.singularValue)
- [Source of `ContinuousLinearMap.singularValue` in TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Basic.lean#L72)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorTheory/STATUS.md)
