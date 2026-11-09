# Leibniz formula (Single Variable Real Analysis)

Mathlib states this as `deriv_mul`.

```lean
deriv_mul.{u, u_3} {𝕜 : Type u} [NontriviallyNormedField 𝕜] {x : 𝕜} {𝔸 : Type u_3} [NormedRing 𝔸]
  [NormedAlgebra 𝕜 𝔸] {c d : 𝕜 → 𝔸} (hc : DifferentiableAt 𝕜 c x) (hd : DifferentiableAt 𝕜 d x) :
  deriv (c * d) x = deriv c x * d x + c x * deriv d x
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Derivative at a point](derivative-at-a-point.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `deriv_mul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/Mul.html#deriv_mul)
- [Source of `deriv_mul` in Mathlib/Analysis/Calculus/Deriv/Mul.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/Deriv/Mul.lean#L281)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L323)
