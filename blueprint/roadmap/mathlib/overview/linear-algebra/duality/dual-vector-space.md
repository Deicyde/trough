# Dual vector space

The left dual space of an R-module M is the R-module of linear maps `M → R`.

```lean
Module.Dual.{u_3, u_4} (R : Type u_3) (M : Type u_4) [Semiring R] [AddCommMonoid M]
  [_root_.Module R M] : Type (max u_4 u_3)
```

## Depends on

- [Linear map](../fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `Module.Dual`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dual/Defs.html#Module.Dual)
- [Source of `Module.Dual` in Mathlib/LinearAlgebra/Dual/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Dual/Defs.lean#L59)
- [Mathlib overview: Linear algebra › Duality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L181)
- [Mathlib undergraduate list: Linear algebra › Duality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L24)
