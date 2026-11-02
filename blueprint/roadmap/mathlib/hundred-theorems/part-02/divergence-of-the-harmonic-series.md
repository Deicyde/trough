---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Real.tendsto_sum_range_one_div_nat_succ_atTop
mathlib_file: Mathlib/Analysis/PSeries.lean
---

# Divergence of the Harmonic Series

**Divergence of the Harmonic Series**

```lean
Real.tendsto_sum_range_one_div_nat_succ_atTop :
  Filter.Tendsto (fun n => ∑ i ∈ Finset.range n, 1 / (↑i + 1)) Filter.atTop Filter.atTop
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Limit of a map with respect to filters](../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Real number](../../overview/general-algebra/numbers/real-number.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Infinite sum](../../overview/topology/topological-algebra/infinite-sum.md)
- [Intermediate value theorem](../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Limit point](../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Lipschitz continuity](../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Norm of a continuous linear map](../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Power functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/power-functions.md)
- [Squeeze theorem](../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../part-05/the-triangle-inequality.md)
- [Topological module](../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Real.tendsto_sum_range_one_div_nat_succ_atTop`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/PSeries.html#Real.tendsto_sum_range_one_div_nat_succ_atTop)
- [Source of `Real.tendsto_sum_range_one_div_nat_succ_atTop` in Mathlib/Analysis/PSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/PSeries.lean#L360)
- [Freek Wiedijk's 100 theorems, no. 34](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L179)
