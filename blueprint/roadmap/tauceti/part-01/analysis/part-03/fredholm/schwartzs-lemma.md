---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.cofg_range_add_of_surjective_of_isCompactOperator
statement: formalized
proof: formalized
---

# Schwartz's lemma

A compact perturbation of a surjection between real or complex
Banach spaces has finite-dimensional cokernel, without any hypothesis on its kernel.

```lean
ContinuousLinearMap.cofg_range_add_of_surjective_of_isCompactOperator.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace E] [CompleteSpace F] (T K : E →L[𝕜] F)
  (hT : Function.Surjective ⇑T) (hK : IsCompactOperator ⇑K) : (↑(T + K)).range.CoFG
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.cofg_range_add_of_surjective_of_isCompactOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/Schwartz.html#ContinuousLinearMap.cofg_range_add_of_surjective_of_isCompactOperator).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.cofg_range_add_of_surjective_of_isCompactOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/Schwartz.html#ContinuousLinearMap.cofg_range_add_of_surjective_of_isCompactOperator)
- [Source of `ContinuousLinearMap.cofg_range_add_of_surjective_of_isCompactOperator` in TauCeti/Analysis/Fredholm/Schwartz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fredholm/Schwartz.lean#L42)
