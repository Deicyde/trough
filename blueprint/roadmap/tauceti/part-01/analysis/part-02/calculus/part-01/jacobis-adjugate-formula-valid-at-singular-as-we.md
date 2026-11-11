---
declaration: theorem
origin: cited
lean: Matrix.fderiv_det_apply_adjugate
statement: formalized
proof: formalized
---

# Jacobi's adjugate formula, valid at singular as well as invertible matrices

```lean
Matrix.fderiv_det_apply_adjugate.{u_1, u_2} {n : Type u_1} [Fintype n] [DecidableEq n]
  {𝕜 : Type u_2} [NontriviallyNormedField 𝕜] (A H : Matrix n n 𝕜) :
  (fderiv 𝕜 Matrix.det A) H = (A.adjugate * H).trace
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's formula, by rows](../../../../linear-algebra/matrix/jacobis-formula-by-rows.md)

## Lean

Formalized in Tau Ceti as [`Matrix.fderiv_det_apply_adjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Det/Basic.html#Matrix.fderiv_det_apply_adjugate).

## Sources

- [Tau Ceti documentation: `Matrix.fderiv_det_apply_adjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Det/Basic.html#Matrix.fderiv_det_apply_adjugate)
- [Source of `Matrix.fderiv_det_apply_adjugate` in TauCeti/Analysis/Calculus/FDeriv/Det/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/FDeriv/Det/Basic.lean#L181)
