# Derivative at a point

`f` has the derivative `f'` at the point `x`.

That is, `f x' = f x + (x' - x) • f' + o(x' - x)` where `x'` converges to `x`.

```lean
HasDerivAt.{u, v} {𝕜 : Type u} [NontriviallyNormedField 𝕜] {F : Type v} [AddCommGroup F]
  [_root_.Module 𝕜 F] [TopologicalSpace F] [ContinuousSMul 𝕜 F] (f : 𝕜 → F) (f' : F) (x : 𝕜) : Prop
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `HasDerivAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/Basic.html#HasDerivAt)
- [Source of `HasDerivAt` in Mathlib/Analysis/Calculus/Deriv/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/Deriv/Basic.lean#L126)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L314)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L315)
