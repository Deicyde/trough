---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: AnalyticAt.eventually_eq_zero_or_eventually_ne_zero
mathlib_file: Mathlib/Analysis/Analytic/IsolatedZeros.lean
---

# Principle of isolated zeros

The *principle of isolated zeros* for an analytic function, local version: if a function is
analytic at `z₀`, then either it is identically zero in a neighborhood of `z₀`, or it does not
vanish in a punctured neighborhood of `z₀`.

```lean
AnalyticAt.eventually_eq_zero_or_eventually_ne_zero.{u_1, u_2} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {f : 𝕜 → E}
  {z₀ : 𝕜} (hf : AnalyticAt 𝕜 f z₀) :
  (∀ᶠ (z : 𝕜) in nhds z₀, f z = 0) ∨ ∀ᶠ (z : 𝕜) in nhdsWithin z₀ {z₀}ᶜ, f z ≠ 0
```

## Depends on

- [Analytic function](../differentiability/analytic-function.md)

## Proof depends on

- [Affine space](../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Continuity (Complex-valued series)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/continuity.md)
- [Derivative at a point](../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable function between normed vector spaces](../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Limit point](../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Norm of a continuous linear map](../normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)

## Sources

- [Mathlib documentation: `AnalyticAt.eventually_eq_zero_or_eventually_ne_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/IsolatedZeros.html#AnalyticAt.eventually_eq_zero_or_eventually_ne_zero)
- [Source of `AnalyticAt.eventually_eq_zero_or_eventually_ne_zero` in Mathlib/Analysis/Analytic/IsolatedZeros.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Analytic/IsolatedZeros.lean#L109)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L369)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L392)
