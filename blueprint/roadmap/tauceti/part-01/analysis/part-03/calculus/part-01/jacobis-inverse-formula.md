---
declaration: theorem
origin: cited
lean: Matrix.hasFDerivAt_det, Matrix.fderiv_det_apply
statement: formalized
proof: formalized
---

# Jacobi's inverse formula

At a matrix with invertible determinant, the differential is
`H ↦ det A * trace (A⁻¹ * H)`.

```lean
Matrix.hasFDerivAt_det.{u_1, u_2} {n : Type u_1} [Fintype n] [DecidableEq n] {𝕜 : Type u_2}
  [NontriviallyNormedField 𝕜] {A : Matrix n n 𝕜} (hA : IsUnit A.det) :
  HasFDerivAt Matrix.det
    (A.det •
      { toLinearMap := Matrix.traceLinearMap n 𝕜 𝕜, cont := ⋯ } ∘SL
        (ContinuousLinearMap.mul 𝕜 (Matrix n n 𝕜)) A⁻¹)
    A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's adjugate formula along a curve](../../../part-02/ricci-flow-preserved-curvature-cones-and-sphere/jacobis-adjugate-formula-along-a-curve.md)

## Lean

Formalized in Tau Ceti as [`Matrix.hasFDerivAt_det`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Det/Basic.html#Matrix.hasFDerivAt_det).

## Other forms

**Jacobi's inverse formula, evaluated on a direction at an invertible matrix.** Formalized in Tau Ceti as [`Matrix.fderiv_det_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Det/Basic.html#Matrix.fderiv_det_apply).

```lean
Matrix.fderiv_det_apply.{u_1, u_2} {n : Type u_1} [Fintype n] [DecidableEq n] {𝕜 : Type u_2}
  [NontriviallyNormedField 𝕜] {A : Matrix n n 𝕜} (hA : IsUnit A.det) (H : Matrix n n 𝕜) :
  (fderiv 𝕜 Matrix.det A) H = A.det * (A⁻¹ * H).trace
```

## Sources

- [Tau Ceti documentation: `Matrix.hasFDerivAt_det`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Det/Basic.html#Matrix.hasFDerivAt_det)
- [Source of `Matrix.hasFDerivAt_det` in TauCeti/Analysis/Calculus/FDeriv/Det/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/FDeriv/Det/Basic.lean#L208)
