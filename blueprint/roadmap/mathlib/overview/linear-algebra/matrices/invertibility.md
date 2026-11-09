# Invertibility

The inverse of a square matrix, when it is invertible (and zero otherwise).

```lean
Matrix.inv.{u', v} {n : Type u'} {α : Type v} [Fintype n] [DecidableEq n] [CommRing α] :
  Inv (Matrix n n α)
```

## Depends on

- [Determinant](determinant.md)

## Sources

- [Mathlib documentation: `Matrix.inv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/NonsingularInverse.html#Matrix.inv)
- [Source of `Matrix.inv` in Mathlib/LinearAlgebra/Matrix/NonsingularInverse.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Matrix/NonsingularInverse.lean#L166)
- [Mathlib overview: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L193)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L48)
