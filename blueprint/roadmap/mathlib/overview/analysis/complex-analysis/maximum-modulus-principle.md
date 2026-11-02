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

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Differentiable function between normed vector spaces](../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Cauchy integral formula](cauchy-integral-formula.md)

## Sources

- [Mathlib documentation: `Complex.eventually_eq_of_isLocalMax_norm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/AbsMax.html#Complex.eventually_eq_of_isLocalMax_norm)
- [Source of `Complex.eventually_eq_of_isLocalMax_norm` in Mathlib/Analysis/Complex/AbsMax.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/AbsMax.lean#L350)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L368)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L394)
