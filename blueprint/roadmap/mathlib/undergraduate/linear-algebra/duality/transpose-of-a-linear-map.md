# Transpose of a linear map

The transposition of linear maps, as a linear map from `M →ₗ[R] M'` to
`Dual R M' →ₗ[R] Dual R M`.

```lean
Module.Dual.transpose.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2} [CommSemiring R]
  [AddCommMonoid M] [_root_.Module R M] {M' : Type u_3} [AddCommMonoid M'] [_root_.Module R M'] :
  (M →ₗ[R] M') →ₗ[R] Module.Dual R M' →ₗ[R] Module.Dual R M
```

## Depends on

- [Dual vector space](../../../overview/linear-algebra/duality/dual-vector-space.md)

## Sources

- [Mathlib documentation: `Module.Dual.transpose`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dual/Defs.html#Module.Dual.transpose)
- [Source of `Module.Dual.transpose` in Mathlib/LinearAlgebra/Dual/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Dual/Defs.lean#L80)
- [Mathlib undergraduate list: Linear algebra › Duality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L26)
