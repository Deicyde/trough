---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_deriv_eq_slope
mathlib_file: Mathlib/Analysis/Calculus/Deriv/MeanValue.lean
---

# The Mean Value Theorem (Freek Wiedijk's 100 theorems)

Lagrange's **Mean Value Theorem**, `deriv` version.

```lean
exists_deriv_eq_slope (f : ℝ → ℝ) {a b : ℝ} (hab : a < b) (hfc : ContinuousOn f (Set.Icc a b))
  (hfd : DifferentiableOn ℝ f (Set.Ioo a b)) : ∃ c ∈ Set.Ioo a b, deriv f c = (f b - f a) / (b - a)
```

The 1000+ list (Q189136) also cites `exists_ratio_deriv_eq_ratio_slope`.

## Depends on

- [Differentials (linear tangent functions)](../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Holomorphic functions](../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Derivative at a point](../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable function between normed vector spaces](../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Permutation group of a type](../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `exists_deriv_eq_slope`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/MeanValue.html#exists_deriv_eq_slope)
- [Source of `exists_deriv_eq_slope` in Mathlib/Analysis/Calculus/Deriv/MeanValue.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Deriv/MeanValue.lean#L154)
- [Freek Wiedijk's 100 theorems, no. 75](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L379)
- [1000+ theorems list: Q189136](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L126)
- [1000+ theorems project: Q189136](https://1000-plus.github.io/all.html?length=-1#Q189136)
- [Wikipedia: Mean value theorem](https://en.wikipedia.org/wiki/Mean_value_theorem)
- [Wikidata: Q189136](https://www.wikidata.org/wiki/Q189136)
