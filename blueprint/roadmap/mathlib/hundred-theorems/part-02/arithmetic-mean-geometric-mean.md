---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Real.geom_mean_le_arith_mean_weighted
mathlib_file: Mathlib/Analysis/MeanInequalities.lean
---

# Arithmetic Mean/Geometric Mean

**AM-GM inequality**: The geometric mean is less than or equal to the arithmetic mean, weighted
version for real-valued nonnegative functions.

```lean
Real.geom_mean_le_arith_mean_weighted.{u} {ι : Type u} (s : Finset ι) (w z : ι → ℝ)
  (hw : ∀ i ∈ s, 0 ≤ w i) (hw' : ∑ i ∈ s, w i = 1) (hz : ∀ i ∈ s, 0 ≤ z i) :
  ∏ i ∈ s, z i ^ w i ≤ ∑ i ∈ s, w i * z i
```

## Depends on

- [Power functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/power-functions.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cluster point](../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Intermediate value theorem](../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Jensen's inequality (finite sum version)](../../overview/analysis/convexity/jensens-inequality-finite-sum-version.md)
- [Lipschitz continuity](../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Norm of a continuous linear map](../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Squeeze theorem](../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../part-05/the-triangle-inequality.md)
- [Topological module](../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Real.geom_mean_le_arith_mean_weighted`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/MeanInequalities.html#Real.geom_mean_le_arith_mean_weighted)
- [Source of `Real.geom_mean_le_arith_mean_weighted` in Mathlib/Analysis/MeanInequalities.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/MeanInequalities.lean#L127)
- [Freek Wiedijk's 100 theorems, no. 38](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L199)
