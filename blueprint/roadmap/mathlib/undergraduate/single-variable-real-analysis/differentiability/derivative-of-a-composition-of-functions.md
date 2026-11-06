# Derivative of a composition of functions (Single Variable Real Analysis)

Mathlib states this as `deriv_comp`.

```lean
deriv_comp.{u, u_1} {𝕜 : Type u} [NontriviallyNormedField 𝕜] (x : 𝕜) {𝕜' : Type u_1}
  [NontriviallyNormedField 𝕜'] [NormedAlgebra 𝕜 𝕜'] {h : 𝕜 → 𝕜'} {h₂ : 𝕜' → 𝕜'}
  (hh₂ : DifferentiableAt 𝕜' h₂ (h x)) (hh : DifferentiableAt 𝕜 h x) :
  deriv (h₂ ∘ h) x = deriv h₂ (h x) * deriv h x
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Derivative at a point](derivative-at-a-point.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)

## Sources

- [Mathlib documentation: `deriv_comp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/Comp.html#deriv_comp)
- [Source of `deriv_comp` in Mathlib/Analysis/Calculus/Deriv/Comp.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Deriv/Comp.lean#L299)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L316)
