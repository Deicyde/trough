# Differentiability with respect to the complex variable

Mathlib states this as `HasFPowerSeriesOnBall.differentiableOn`.

```lean
HasFPowerSeriesOnBall.differentiableOn.{u, v, u_1} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type v} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {p : FormalMultilinearSeries 𝕜 E F} {r : ENNReal} {f : E → F} {x : E}
  [CompleteSpace F] (h : HasFPowerSeriesOnBall f p x r) : DifferentiableOn 𝕜 f (Metric.eball x r)
```

## Depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Holomorphic functions](../functions-on-one-complex-variable/holomorphic-functions.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Radius of convergence](radius-of-convergence.md)

## Proof depends on

- [Analytic function](../../../overview/analysis/differentiability/analytic-function.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `HasFPowerSeriesOnBall.differentiableOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Analytic.html#HasFPowerSeriesOnBall.differentiableOn)
- [Source of `HasFPowerSeriesOnBall.differentiableOn` in Mathlib/Analysis/Calculus/FDeriv/Analytic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/FDeriv/Analytic.lean#L167)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L372)
