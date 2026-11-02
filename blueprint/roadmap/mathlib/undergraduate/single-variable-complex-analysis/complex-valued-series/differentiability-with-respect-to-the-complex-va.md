---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasFPowerSeriesOnBall.differentiableOn
mathlib_file: Mathlib/Analysis/Calculus/FDeriv/Analytic.lean
---

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

- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Analytic function](../../../overview/analysis/differentiability/analytic-function.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closed map](../../../overview/topology/general-topology/part-01/closed-map.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Existence of bases](../../linear-algebra/fundamentals/existence-of-bases.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Kernel of a linear map](../../linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Limit point](../../single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Sum of subspaces](../../linear-algebra/fundamentals/sum-of-subspaces.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `HasFPowerSeriesOnBall.differentiableOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Analytic.html#HasFPowerSeriesOnBall.differentiableOn)
- [Source of `HasFPowerSeriesOnBall.differentiableOn` in Mathlib/Analysis/Calculus/FDeriv/Analytic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/FDeriv/Analytic.lean#L167)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L372)
