---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: TensorProduct
mathlib_file: Mathlib/LinearAlgebra/TensorProduct/Defs.lean
---

# Tensor product

The tensor product of two modules `M` and `N` over the same commutative semiring `R`.
The localized notations are `M ⊗ N` and `M ⊗[R] N`, accessed by `open scoped TensorProduct`.

```lean
TensorProduct.{u_1, u_5, u_6} (R : Type u_1) [CommSemiring R] (M : Type u_5) (N : Type u_6)
  [AddCommMonoid M] [AddCommMonoid N] [_root_.Module R M] [_root_.Module R N] : Type (max u_5 u_6)
```

## Depends on

- [Module](module.md)

## Sources

- [Mathlib documentation: `TensorProduct`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Defs.html#TensorProduct)
- [Source of `TensorProduct` in Mathlib/LinearAlgebra/TensorProduct/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/TensorProduct/Defs.lean#L70)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L174)
