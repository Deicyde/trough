# Mean value theorem (Differentiability)

Cauchy's Mean Value Theorem, `deriv` version.

```lean
exists_ratio_deriv_eq_ratio_slope (f : ℝ → ℝ) {a b : ℝ} (hab : a < b)
  (hfc : ContinuousOn f (Set.Icc a b)) (hfd : DifferentiableOn ℝ f (Set.Ioo a b)) (g : ℝ → ℝ)
  (hgc : ContinuousOn g (Set.Icc a b)) (hgd : DifferentiableOn ℝ g (Set.Ioo a b)) :
  ∃ c ∈ Set.Ioo a b, (g b - g a) * deriv f c = (f b - f a) * deriv g c
```

## Depends on

- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Derivative at a point](../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable function between normed vector spaces](differentiable-function-between-normed-vector-sp.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `exists_ratio_deriv_eq_ratio_slope`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/MeanValue.html#exists_ratio_deriv_eq_ratio_slope)
- [Source of `exists_ratio_deriv_eq_ratio_slope` in Mathlib/Analysis/Calculus/Deriv/MeanValue.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/Deriv/MeanValue.lean#L133)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L311)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L319)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L463)
