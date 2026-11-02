---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Matrix.SpecialLinearGroup
mathlib_file: Mathlib/LinearAlgebra/Matrix/SpecialLinearGroup.lean
---

# Special linear group

`SpecialLinearGroup n R` is the group of `n` by `n` `R`-matrices with determinant equal to 1.

```lean
Matrix.SpecialLinearGroup.{u, v} (n : Type u) [DecidableEq n] [Fintype n] (R : Type v)
  [CommRing R] : Type (max 0 u v)
```

## Depends on

- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)

## Sources

- [Mathlib documentation: `Matrix.SpecialLinearGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/SpecialLinearGroup.html#Matrix.SpecialLinearGroup)
- [Source of `Matrix.SpecialLinearGroup` in Mathlib/LinearAlgebra/Matrix/SpecialLinearGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/SpecialLinearGroup.lean#L68)
- [Mathlib undergraduate list: Linear algebra › Multilinearity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L39)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L106)
