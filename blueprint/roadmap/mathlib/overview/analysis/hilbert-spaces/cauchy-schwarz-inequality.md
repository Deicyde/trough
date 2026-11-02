---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: inner_mul_inner_self_le
mathlib_file: Mathlib/Analysis/InnerProductSpace/Basic.lean
---

# Cauchy-Schwarz inequality

**Cauchy–Schwarz inequality**.

```lean
inner_mul_inner_self_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [SeminormedAddCommGroup E] [InnerProductSpace 𝕜 E] (x y : E) :
  ‖inner 𝕜 x y‖ * ‖inner 𝕜 y x‖ ≤ RCLike.re (inner 𝕜 x x) * RCLike.re (inner 𝕜 y y)
```

Freek Wiedijk's list (no. 78) also cites `norm_inner_le_norm`.

## Depends on

- [Inner product space, over $R$ or $C$](inner-product-space-over-r-or-c.md)

## Sources

- [Mathlib documentation: `inner_mul_inner_self_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Basic.html#inner_mul_inner_self_le)
- [Source of `inner_mul_inner_self_le` in Mathlib/Analysis/InnerProductSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Basic.lean#L279)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L295)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Euclidean and Hermitian spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L219)
- [Freek Wiedijk's 100 theorems, no. 78](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L395)
