---
declaration: theorem
origin: cited
lean: Matrix.hasDerivAt_det_of_entries_adjugate, Matrix.fderiv_det_apply_adjugate, Matrix.hasDerivWithinAt_det_of_entries_adjugate
statement: formalized
proof: formalized
---

# Jacobi's adjugate formula along a curve

If every entry of a matrix curve `A` has
derivative given by the corresponding entry of `A'` at `t`, then `det A` has derivative
`trace (adjugate (A t) * A')` at `t`. The matrix `A t` may be singular.

```lean
Matrix.hasDerivAt_det_of_entries_adjugate.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [NontriviallyNormedField 𝕜] [Fintype ι] [DecidableEq ι] {A : 𝕜 → Matrix ι ι 𝕜} {A' : Matrix ι ι 𝕜}
  {t : 𝕜} (hA : ∀ (i j : ι), HasDerivAt (fun τ => A τ i j) (A' i j) t) :
  HasDerivAt (fun τ => (A τ).det) ((A t).adjugate * A').trace t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's formula, by rows](../../../linear-algebra/part-01/matrix/jacobis-formula-by-rows.md)

## Lean

Formalized in Tau Ceti as [`Matrix.hasDerivAt_det_of_entries_adjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Deriv/Matrix.html#Matrix.hasDerivAt_det_of_entries_adjugate).

## Other forms

**Jacobi's adjugate formula, valid at singular as well as invertible matrices.** Formalized in Tau Ceti as [`Matrix.fderiv_det_apply_adjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Det/Basic.html#Matrix.fderiv_det_apply_adjugate).

```lean
Matrix.fderiv_det_apply_adjugate.{u_1, u_2} {n : Type u_1} [Fintype n] [DecidableEq n]
  {𝕜 : Type u_2} [NontriviallyNormedField 𝕜] (A H : Matrix n n 𝕜) :
  (fderiv 𝕜 Matrix.det A) H = (A.adjugate * H).trace
```

**Jacobi's adjugate formula along a curve.** Formalized in Tau Ceti as [`Matrix.hasDerivWithinAt_det_of_entries_adjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Deriv/Matrix.html#Matrix.hasDerivWithinAt_det_of_entries_adjugate).

```lean
Matrix.hasDerivWithinAt_det_of_entries_adjugate.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [NontriviallyNormedField 𝕜] [Fintype ι] [DecidableEq ι] {A : 𝕜 → Matrix ι ι 𝕜} {A' : Matrix ι ι 𝕜}
  {t : 𝕜} {s : Set 𝕜} (hA : ∀ (i j : ι), HasDerivWithinAt (fun τ => A τ i j) (A' i j) s t) :
  HasDerivWithinAt (fun τ => (A τ).det) ((A t).adjugate * A').trace s t
```

## Sources

- [Tau Ceti documentation: `Matrix.hasDerivAt_det_of_entries_adjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Deriv/Matrix.html#Matrix.hasDerivAt_det_of_entries_adjugate)
- [Source of `Matrix.hasDerivAt_det_of_entries_adjugate` in TauCeti/Analysis/Calculus/Deriv/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/Deriv/Matrix.lean#L66)
