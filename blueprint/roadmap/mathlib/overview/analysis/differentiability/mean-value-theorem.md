---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_ratio_deriv_eq_ratio_slope
mathlib_file: Mathlib/Analysis/Calculus/Deriv/MeanValue.lean
---

# Mean value theorem

Cauchy's Mean Value Theorem, `deriv` version.

```lean
exists_ratio_deriv_eq_ratio_slope (f : ℝ → ℝ) {a b : ℝ} (hab : a < b)
  (hfc : ContinuousOn f (Set.Icc a b)) (hfd : DifferentiableOn ℝ f (Set.Ioo a b)) (g : ℝ → ℝ)
  (hgc : ContinuousOn g (Set.Icc a b)) (hgd : DifferentiableOn ℝ g (Set.Ioo a b)) :
  ∃ c ∈ Set.Ioo a b, (g b - g a) * deriv f c = (f b - f a) * deriv g c
```

## Depends on

- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Derivative at a point](../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable function between normed vector spaces](differentiable-function-between-normed-vector-sp.md)
- [Dual of a normed space](../normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Extreme value theorem](../../topology/topological-algebra/extreme-value-theorem.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Open map](../../topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `exists_ratio_deriv_eq_ratio_slope`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/MeanValue.html#exists_ratio_deriv_eq_ratio_slope)
- [Source of `exists_ratio_deriv_eq_ratio_slope` in Mathlib/Analysis/Calculus/Deriv/MeanValue.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Deriv/MeanValue.lean#L133)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L311)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L319)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L463)
