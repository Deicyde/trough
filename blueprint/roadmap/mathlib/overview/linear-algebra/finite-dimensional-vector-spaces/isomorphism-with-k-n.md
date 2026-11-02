---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Module.Basis.equivFun
mathlib_file: Mathlib/LinearAlgebra/Basis/Defs.lean
---

# Isomorphism with $K^n$

A module over `R` with a finite basis is linearly equivalent to functions from its basis to `R`.

```lean
Module.Basis.equivFun.{u_1, u_3, u_4} {ι : Type u_1} {R : Type u_3} {M : Type u_4} [Semiring R]
  [AddCommMonoid M] [_root_.Module R M] [Finite ι] (b : Module.Basis ι R M) : M ≃ₗ[R] ι → R
```

## Depends on

- [Basis](../fundamentals/basis.md)

## Sources

- [Mathlib documentation: `Module.Basis.equivFun`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Basis/Defs.html#Module.Basis.equivFun)
- [Source of `Module.Basis.equivFun` in Mathlib/LinearAlgebra/Basis/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Basis/Defs.lean#L220)
- [Mathlib overview: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L185)
- [Mathlib undergraduate list: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L30)
