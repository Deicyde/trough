# Cramer’s Rule

A stronger form of **Cramer's rule** that allows us to solve some instances of `A * x = b` even
if the determinant is not a unit. A sufficient (but still not necessary) condition is that `A.det`
divides `b`.

```lean
Matrix.mulVec_cramer.{v, w} {n : Type v} {α : Type w} [DecidableEq n] [Fintype n] [CommRing α]
  (A : Matrix n n α) (b : n → α) : A.mulVec (A.cramer b) = A.det • b
```

## Depends on

- [Determinant](../../overview/linear-algebra/matrices/determinant.md)

## Sources

- [Mathlib documentation: `Matrix.mulVec_cramer`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Adjugate.html#Matrix.mulVec_cramer)
- [Source of `Matrix.mulVec_cramer` in Mathlib/LinearAlgebra/Matrix/Adjugate.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Matrix/Adjugate.lean#L279)
- [Freek Wiedijk's 100 theorems, no. 97](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L502)
