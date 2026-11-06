---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.eventually_eq_of_isLocalMax_norm
mathlib_file: Mathlib/Analysis/Complex/AbsMax.lean
---

# Maximum modulus principle

**Maximum modulus principle**: if `f : E → F` is complex differentiable in a neighborhood of `c`
and the norm `‖f z‖` has a local maximum at `c`, then `f` is locally constant in a neighborhood
of `c`.

```lean
Complex.eventually_eq_of_isLocalMax_norm.{u, v} {E : Type u} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {F : Type v} [NormedAddCommGroup F] [NormedSpace ℂ F] [StrictConvexSpace ℝ F]
  {f : E → F} {c : E} (hd : ∀ᶠ (z : E) in nhds c, DifferentiableAt ℂ f z)
  (hc : IsLocalMax (norm ∘ f) c) : ∀ᶠ (y : E) in nhds c, f y = f c
```

## Depends on

- [Complex number](../../general-algebra/numbers/complex-number.md)
- [Differentiable function between normed vector spaces](../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Affine function](../../geometry/affine-and-euclidean-geometry/affine-function.md)
- [Cauchy integral formula](cauchy-integral-formula.md)
- [Completion of an abelian topological group](../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Euclidean affine space](../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)

## Sources

- [Mathlib documentation: `Complex.eventually_eq_of_isLocalMax_norm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/AbsMax.html#Complex.eventually_eq_of_isLocalMax_norm)
- [Source of `Complex.eventually_eq_of_isLocalMax_norm` in Mathlib/Analysis/Complex/AbsMax.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/AbsMax.lean#L350)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L368)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L394)
