---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: fderiv_mul
mathlib_file: Mathlib/Analysis/Calculus/FDeriv/Mul.lean
---

# Leibniz formula

Mathlib states this as `fderiv_mul`.

```lean
fderiv_mul.{u_1, u_2, u_5} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {x : E} {𝔸' : Type u_5} [NormedCommRing 𝔸']
  [NormedAlgebra 𝕜 𝔸'] {c d : E → 𝔸'} (hc : DifferentiableAt 𝕜 c x) (hd : DifferentiableAt 𝕜 d x) :
  fderiv 𝕜 (c * d) x = c x • fderiv 𝕜 d x + d x • fderiv 𝕜 c x
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Differentiable function between normed vector spaces](differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Proof depends on

- [Derivative of a composition of functions](derivative-of-a-composition-of-functions.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Norm of a continuous linear map](../normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Topology on a normed vector space](../normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `fderiv_mul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Mul.html#fderiv_mul)
- [Source of `fderiv_mul` in Mathlib/Analysis/Calculus/FDeriv/Mul.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/FDeriv/Mul.lean#L266)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L314)
