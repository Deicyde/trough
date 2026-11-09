# Derivative of the inverse of a function (Single Variable Real Analysis)

If `f (g y) = y` for `y` in some neighborhood of `a`, `g` is continuous at `a`, and `f` has an
invertible derivative `f'` at `g a` in the strict sense, then `g` has the derivative `f'⁻¹` at `a`
in the strict sense.

This is one of the easy parts of the inverse function theorem: it assumes that we already have an
inverse function.

```lean
HasStrictDerivAt.of_local_left_inverse.{u} {𝕜 : Type u} [NontriviallyNormedField 𝕜] {f g : 𝕜 → 𝕜}
  {f' a : 𝕜} (hg : ContinuousAt g a) (hf : HasStrictDerivAt f f' (g a)) (hf' : f' ≠ 0)
  (hfg : ∀ᶠ (y : 𝕜) in nhds a, f (g y) = y) : HasStrictDerivAt g f'⁻¹ a
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `HasStrictDerivAt.of_local_left_inverse`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/Inverse.html#HasStrictDerivAt.of_local_left_inverse)
- [Source of `HasStrictDerivAt.of_local_left_inverse` in Mathlib/Analysis/Calculus/Deriv/Inverse.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/Deriv/Inverse.lean#L55)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L317)
