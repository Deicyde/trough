---
declaration: theorem
origin: cited
lean: Matrix.sum_det_updateRow_eq_trace_adjugate_mul, Matrix.sum_det_updateRow_mul_row, Matrix.sum_det_updateCol_eq_trace_adjugate_mul
statement: formalized
proof: formalized
---

# Jacobi's formula, by rows

Replacing the `i`-th row of `A` by the `i`-th row of `B` and
summing the determinants over `i` gives `trace (adj A * B)`, the derivative of `det` at `A` in the
direction `B`.

```lean
Matrix.sum_det_updateRow_eq_trace_adjugate_mul.{u_1, u_2} {K : Type u_1} [CommRing K] {n : Type u_2}
  [Fintype n] [DecidableEq n] (A B : Matrix n n K) :
  ∑ i, (A.updateRow i (B i)).det = (A.adjugate * B).trace
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.sum_det_updateRow_eq_trace_adjugate_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Adjugate/Basic.html#Matrix.sum_det_updateRow_eq_trace_adjugate_mul).

## Other forms

**Jacobi's formula for a determinant, in row form.** Formalized in Tau Ceti as [`Matrix.sum_det_updateRow_mul_row`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Determinant/Basic.html#Matrix.sum_det_updateRow_mul_row).

```lean
Matrix.sum_det_updateRow_mul_row.{u_1, u_2} {ι : Type u_1} [DecidableEq ι] [Fintype ι]
  {R : Type u_2} [CommRing R] (A : Matrix ι ι R) (d : ι → R) :
  ∑ k, (A.updateRow k fun j => d j * A k j).det = (∑ j, d j) * A.det
```

**Jacobi's formula, by columns.** Formalized in Tau Ceti as [`Matrix.sum_det_updateCol_eq_trace_adjugate_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Adjugate/Basic.html#Matrix.sum_det_updateCol_eq_trace_adjugate_mul).

```lean
Matrix.sum_det_updateCol_eq_trace_adjugate_mul.{u_1, u_2} {K : Type u_1} [CommRing K] {n : Type u_2}
  [Fintype n] [DecidableEq n] (A B : Matrix n n K) :
  ∑ j, (A.updateCol j fun i => B i j).det = (A.adjugate * B).trace
```

## Sources

- [Tau Ceti documentation: `Matrix.sum_det_updateRow_eq_trace_adjugate_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Adjugate/Basic.html#Matrix.sum_det_updateRow_eq_trace_adjugate_mul)
- [Source of `Matrix.sum_det_updateRow_eq_trace_adjugate_mul` in TauCeti/LinearAlgebra/Matrix/Adjugate/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/Adjugate/Basic.lean#L100)
