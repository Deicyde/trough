# Differentiable function between normed vector spaces

A function `f` has the continuous linear map `f'` as derivative at `x` if
`f x' = f x + f' (x' - x) + o (x' - x)` when `x'` tends to `x`.

```lean
HasFDerivAt.{u_1, u_2, u_3} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2}
  [AddCommGroup E] [_root_.Module 𝕜 E] [TopologicalSpace E] {F : Type u_3} [AddCommGroup F]
  [_root_.Module 𝕜 F] [TopologicalSpace F] (f : E → F) (f' : E →L[𝕜] F) (x : E) : Prop
```

## Depends on

- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)

## Sources

- [Mathlib documentation: `HasFDerivAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Defs.html#HasFDerivAt)
- [Source of `HasFDerivAt` in Mathlib/Analysis/Calculus/FDeriv/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/FDeriv/Defs.lean#L120)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L307)
