# Characteristic polynomial

The characteristic polynomial of a matrix `M` is given by $\det (t I - M)$.

```lean
Matrix.charpoly.{u_1, u_4} {R : Type u_1} [CommRing R] {n : Type u_4} [DecidableEq n] [Fintype n]
  (M : Matrix n n R) : Polynomial R
```

## Depends on

- [Determinant](../matrices/determinant.md)
- [Polynomial in one indeterminate](../../general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `Matrix.charpoly`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.html#Matrix.charpoly)
- [Source of `Matrix.charpoly` in Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.lean#L138)
- [Mathlib overview: Linear algebra › Endomorphism polynomials](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L196)
- [Mathlib undergraduate list: Linear algebra › Endomorphism polynomials](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L56)
