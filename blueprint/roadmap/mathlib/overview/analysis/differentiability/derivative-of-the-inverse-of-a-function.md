# Derivative of the inverse of a function (Analysis)

If `f (g x) = x` for `x` in some neighborhood of `a`, `g` is continuous at `a`,
and `f` has an invertible derivative `f'` at `g a`, then `g` has the derivative `f'⁻¹` at `a`.

This is one of the easy parts of the inverse function theorem: it assumes that we already have
an inverse function.

```lean
HasFDerivAt.of_local_left_inverse.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {g : E → F} {f : F → E} {f' : F ≃L[𝕜] E} {a : E} (hg : ContinuousAt g a)
  (hf : HasFDerivAt f (↑f') (g a)) (hfg : ∀ᶠ (y : E) in nhds a, f (g y) = y) :
  HasFDerivAt g (↑f'.symm) a
```

## Depends on

- [Differentiable function between normed vector spaces](differentiable-function-between-normed-vector-sp.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `HasFDerivAt.of_local_left_inverse`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/OfCompLeft.html#HasFDerivAt.of_local_left_inverse)
- [Source of `HasFDerivAt.of_local_left_inverse` in Mathlib/Analysis/Calculus/FDeriv/OfCompLeft.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/FDeriv/OfCompLeft.lean#L161)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L309)
