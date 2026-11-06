# Analytic function

Given a function `f : E → F`, we say that `f` is analytic at `x` if it admits a convergent power
series expansion around `x`.

```lean
AnalyticAt.{u_1, u_2, u_3} (𝕜 : Type u_1) {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F] [NormedSpace 𝕜 F] (f : E → F)
  (x : E) : Prop
```

## Depends on

- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Radius of convergence](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)

## Sources

- [Mathlib documentation: `AnalyticAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/Basic.html#AnalyticAt)
- [Source of `AnalyticAt` in Mathlib/Analysis/Analytic/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Analytic/Basic.lean#L107)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L318)
