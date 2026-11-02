---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasFPowerSeriesOnBall.continuousOn
mathlib_file: Mathlib/Analysis/Analytic/Basic.lean
---

# Continuity (Complex-valued series)

If a function admits a power series expansion on a ball, then it is continuous there.

```lean
HasFPowerSeriesOnBall.continuousOn.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {f : E → F} {p : FormalMultilinearSeries 𝕜 E F} {x : E} {r : ENNReal}
  (hf : HasFPowerSeriesOnBall f p x r) : ContinuousOn f (Metric.eball x r)
```

## Depends on

- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Radius of convergence](radius-of-convergence.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `HasFPowerSeriesOnBall.continuousOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/Basic.html#HasFPowerSeriesOnBall.continuousOn)
- [Source of `HasFPowerSeriesOnBall.continuousOn` in Mathlib/Analysis/Analytic/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Analytic/Basic.lean#L1005)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L371)
