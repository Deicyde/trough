---
declaration: theorem
origin: cited
lean: Matrix.det_mul_det_submatrix_adjugate
statement: formalized
proof: formalized
---

# Jacobi's complementary minor theorem

For `#I = #J = k`, the product of the determinant of
`A` and the complementary minor of the adjugate, with rows `Jᶜ` and columns `Iᶜ`, is
`(-1) ^ (∑ I + ∑ J)` times `(det A) ^ (n - k)` times the minor `A[I, J]`.

```lean
Matrix.det_mul_det_submatrix_adjugate.{u_1} {R : Type u_1} [CommRing R] {n k : ℕ}
  (A : Matrix (Fin n) (Fin n) R) {I J : Finset (Fin n)} (hI : I.card = k) (hJ : J.card = k) :
  A.det * (A.adjugate.submatrix ⇑(Jᶜ.orderEmbOfFin ⋯) ⇑(Iᶜ.orderEmbOfFin ⋯)).det =
    (-1) ^ (∑ i ∈ I, ↑i + ∑ j ∈ J, ↑j) * A.det ^ (n - k) *
      (A.submatrix ⇑(I.orderEmbOfFin hI) ⇑(J.orderEmbOfFin hJ)).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.det_mul_det_submatrix_adjugate`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Determinant/Jacobi.html#Matrix.det_mul_det_submatrix_adjugate).

## Sources

- [Tau Ceti documentation: `Matrix.det_mul_det_submatrix_adjugate`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Determinant/Jacobi.html#Matrix.det_mul_det_submatrix_adjugate)
- [Source of `Matrix.det_mul_det_submatrix_adjugate` in TauCeti/LinearAlgebra/Matrix/Determinant/Jacobi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/Determinant/Jacobi.lean#L51)
