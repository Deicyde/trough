---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_deriv_eq_slope, exists_ratio_deriv_eq_ratio_slope
mathlib_file: Mathlib/Analysis/Calculus/Deriv/MeanValue.lean
---

# The Mean Value Theorem

Mathlib records this with 2 declarations.

`exists_deriv_eq_slope`: Lagrange's **Mean Value Theorem**, `deriv` version.

```lean
exists_deriv_eq_slope (f : ℝ → ℝ) {a b : ℝ} (hab : a < b) (hfc : ContinuousOn f (Set.Icc a b))
  (hfd : DifferentiableOn ℝ f (Set.Ioo a b)) : ∃ c ∈ Set.Ioo a b, deriv f c = (f b - f a) / (b - a)
```

`exists_ratio_deriv_eq_ratio_slope`: Cauchy's Mean Value Theorem, `deriv` version.

```lean
exists_ratio_deriv_eq_ratio_slope (f : ℝ → ℝ) {a b : ℝ} (hab : a < b)
  (hfc : ContinuousOn f (Set.Icc a b)) (hfd : DifferentiableOn ℝ f (Set.Ioo a b)) (g : ℝ → ℝ)
  (hgc : ContinuousOn g (Set.Icc a b)) (hgd : DifferentiableOn ℝ g (Set.Ioo a b)) :
  ∃ c ∈ Set.Ioo a b, (g b - g a) * deriv f c = (f b - f a) * deriv g c
```

## Depends on

- [Differentials (linear tangent functions)](../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Holomorphic functions](../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../../overview/topology/general-topology/part-01/closure.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Derivative at a point](../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable function between normed vector spaces](../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Dual of a normed space](../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Extreme value theorem](../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Open map](../../overview/topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../part-05/the-triangle-inequality.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `exists_deriv_eq_slope`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/MeanValue.html#exists_deriv_eq_slope)
- [Source of `exists_deriv_eq_slope` in Mathlib/Analysis/Calculus/Deriv/MeanValue.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Deriv/MeanValue.lean#L154)
- [Mathlib documentation: `exists_ratio_deriv_eq_ratio_slope`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/MeanValue.html#exists_ratio_deriv_eq_ratio_slope)
- [Source of `exists_ratio_deriv_eq_ratio_slope` in Mathlib/Analysis/Calculus/Deriv/MeanValue.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Deriv/MeanValue.lean#L133)
- [Freek Wiedijk's 100 theorems, no. 75](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L379)
- [1000+ theorems list: Q189136](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L126)
- [1000+ theorems project: Q189136](https://1000-plus.github.io/?length=-1#Q189136)
- [Wikipedia: Mean value theorem](https://en.wikipedia.org/wiki/Mean_value_theorem)
- [Wikidata: Q189136](https://www.wikidata.org/wiki/Q189136)
