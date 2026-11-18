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
- [Source of `Module.Dual` in Mathlib/LinearAlgebra/Dual/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Dual/Defs.lean#L58)
- [Mathlib overview: Linear algebra › Duality](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L181)
- [Mathlib undergraduate list: Linear algebra › Duality](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L24)
