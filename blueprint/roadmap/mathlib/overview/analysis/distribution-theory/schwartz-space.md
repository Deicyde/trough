# Schwartz space

A function is a Schwartz function if it is smooth and all derivatives decay faster than
any power of `‖x‖`.

```lean
SchwartzMap.{u_5, u_6} (E : Type u_5) (F : Type u_6) [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] : Type (max u_5 u_6)
```

## Depends on

- [$C^k$ function](../differentiability/c-k-function.md)
- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)

## Sources

- [Mathlib documentation: `SchwartzMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/SchwartzSpace/Basic.html#SchwartzMap)
- [Source of `SchwartzMap` in Mathlib/Analysis/Distribution/SchwartzSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Distribution/SchwartzSpace/Basic.lean#L73)
- [Mathlib overview: Analysis › Distribution theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L380)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{S}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L607)
