# Characterization of convexity

If a function `f` is continuous on a convex set `D ⊆ ℝ`, is twice differentiable on its
interior, and `f''` is nonnegative on the interior, then `f` is convex on `D`.

```lean
convexOn_of_deriv2_nonneg {D : Set ℝ} (hD : Convex ℝ D) {f : ℝ → ℝ} (hf : ContinuousOn f D)
  (hf' : DifferentiableOn ℝ f (interior D)) (hf'' : DifferentiableOn ℝ (deriv f) (interior D))
  (hf''_nonneg : ∀ x ∈ interior D, 0 ≤ deriv^[2] f x) : ConvexOn ℝ D f
```

## Depends on

- [Convex function](convex-function.md)
- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)

## Proof depends on

- [The Mean Value Theorem (Freek Wiedijk's 100 theorems)](../../../hundred-theorems/part-03/the-mean-value-theorem.md)

## Sources

- [Mathlib documentation: `convexOn_of_deriv2_nonneg`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Deriv.html#convexOn_of_deriv2_nonneg)
- [Source of `convexOn_of_deriv2_nonneg` in Mathlib/Analysis/Convex/Deriv.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Convex/Deriv.lean#L213)
- [Mathlib overview: Analysis › Convexity](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L322)
- [Mathlib undergraduate list: Single Variable Real Analysis › Convexity](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L363)
