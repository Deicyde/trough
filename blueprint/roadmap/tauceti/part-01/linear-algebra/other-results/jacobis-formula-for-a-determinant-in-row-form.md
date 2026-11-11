---
declaration: theorem
origin: cited
lean: Matrix.sum_det_updateRow_mul_row
statement: formalized
proof: formalized
---

# Jacobi's formula for a determinant, in row form

Rescale one row of a matrix entry by
entry along a fixed vector of factors, and sum the resulting determinants over the rows: the
answer is the determinant multiplied by the total of the factors.

```lean
Matrix.sum_det_updateRow_mul_row.{u_1, u_2} {ι : Type u_1} [DecidableEq ι] [Fintype ι]
  {R : Type u_2} [CommRing R] (A : Matrix ι ι R) (d : ι → R) :
  ∑ k, (A.updateRow k fun j => d j * A k j).det = (∑ j, d j) * A.det
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.sum_det_updateRow_mul_row`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Determinant/Basic.html#Matrix.sum_det_updateRow_mul_row).

## Sources

- [Tau Ceti documentation: `Matrix.sum_det_updateRow_mul_row`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Determinant/Basic.html#Matrix.sum_det_updateRow_mul_row)
- [Source of `Matrix.sum_det_updateRow_mul_row` in TauCeti/LinearAlgebra/Determinant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Determinant/Basic.lean#L416)
