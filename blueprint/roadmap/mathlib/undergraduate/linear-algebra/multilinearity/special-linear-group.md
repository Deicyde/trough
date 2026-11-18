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
- [Source of `Matrix.SpecialLinearGroup` in Mathlib/LinearAlgebra/Matrix/SpecialLinearGroup.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Matrix/SpecialLinearGroup.lean#L68)
- [Mathlib undergraduate list: Linear algebra › Multilinearity](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L39)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L106)
