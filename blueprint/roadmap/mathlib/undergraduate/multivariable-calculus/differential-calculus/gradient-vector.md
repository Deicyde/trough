---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: gradient
mathlib_file: Mathlib/Analysis/Calculus/Gradient/Basic.lean
---

# Gradient vector

Gradient of `f` at the point `x`, if it exists.  Zero otherwise.
Denoted as `∇` within the Gradient namespace.

If the derivative exists (i.e., `∃ f', HasGradientAt f f' x`), then
`f x' = f x + ⟨f', x' - x⟩ + o (x' - x)` where `x'` converges to `x`.

```lean
gradient.{u_1, u_2} {𝕜 : Type u_1} {F : Type u_2} [RCLike 𝕜] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] [CompleteSpace F] (f : F → 𝕜) (x : F) : F
```

## Depends on

- [Differentials (linear tangent functions)](differentials-linear-tangent-functions.md)
- [Fréchet-Riesz representation of the dual of a Hilbert space](../../../overview/analysis/hilbert-spaces/frechet-riesz-representation-of-the-dual-of-a-hi.md)

## Sources

- [Mathlib documentation: `gradient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Gradient/Basic.html#gradient)
- [Source of `gradient` in Mathlib/Analysis/Calculus/Gradient/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Gradient/Basic.lean#L78)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L460)
