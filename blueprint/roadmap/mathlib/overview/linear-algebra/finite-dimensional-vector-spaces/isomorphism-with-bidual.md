---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Module.evalEquiv
mathlib_file: Mathlib/LinearAlgebra/Dual/Defs.lean
---

# Isomorphism with bidual

The bijection between a reflexive module and its double dual, bundled as a `LinearEquiv`.

```lean
Module.evalEquiv.{u_1, u_2} (R : Type u_1) (M : Type u_2) [CommSemiring R] [AddCommMonoid M]
  [_root_.Module R M] [Module.IsReflexive R M] : M ≃ₗ[R] Module.Dual R (Module.Dual R M)
```

## Depends on

- [Dual vector space](../duality/dual-vector-space.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Module.evalEquiv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dual/Defs.html#Module.evalEquiv)
- [Source of `Module.evalEquiv` in Mathlib/LinearAlgebra/Dual/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Dual/Defs.lean#L215)
- [Mathlib overview: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L186)
- [Mathlib undergraduate list: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L34)
