---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Real.summable_one_div_nat_rpow
mathlib_file: Mathlib/Analysis/PSeries.lean
---

# Convergence of $p$-series for $p>1$

Test for convergence of the `p`-series: the real-valued series `∑' n : ℕ, 1 / n ^ p` converges
if and only if `1 < p`.

```lean
Real.summable_one_div_nat_rpow {p : ℝ} : (Summable fun n => 1 / ↑n ^ p) ↔ 1 < p
```

## Depends on

- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Power functions](../elementary-functions-trigonometric-rational-etc/power-functions.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness of R](../topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Intermediate value theorem](../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Limit point](../sequences-of-real-numbers/limit-point.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../topology-of-r/metric-structure.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Real.summable_one_div_nat_rpow`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/PSeries.html#Real.summable_one_div_nat_rpow)
- [Source of `Real.summable_one_div_nat_rpow` in Mathlib/Analysis/PSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/PSeries.lean#L315)
- [Mathlib undergraduate list: Single Variable Real Analysis › Numerical series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L299)
