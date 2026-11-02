---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: SchwartzMap
mathlib_file: Mathlib/Analysis/Distribution/SchwartzSpace/Basic.lean
---

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
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)

## Sources

- [Mathlib documentation: `SchwartzMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/SchwartzSpace/Basic.html#SchwartzMap)
- [Source of `SchwartzMap` in Mathlib/Analysis/Distribution/SchwartzSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/SchwartzSpace/Basic.lean#L73)
- [Mathlib overview: Analysis › Distribution theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L380)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{S}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L607)
