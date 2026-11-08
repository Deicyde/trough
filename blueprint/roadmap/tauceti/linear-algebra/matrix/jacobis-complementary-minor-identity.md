---
declaration: theorem
origin: cited
lean: Matrix.det_submatrix_inr_eq_sign_mul_det_mul_det_submatrix_inl, Matrix.det_submatrix_comp_inr_eq_sign_mul_det_mul_det_submatrix_comp_inl
statement: formalized
proof: formalized
---

# Jacobi's complementary-minor identity

For mutually inverse matrices `A` and `B` indexed
by `m ⊕ p`, and permutations `σ`, `τ` of that index type, the minor of `A` on the rows `τ (p)` and
the columns `σ (p)` is `det A` times the complementary minor of `B`, the one on the rows `σ (m)`
and the columns `τ (m)`, signed by `σ` and `τ`.

For `p` empty both sides read `det A * det B = 1`, and for `m` empty they read `det A = det A`;
the content is in between.

```lean
Matrix.det_submatrix_inr_eq_sign_mul_det_mul_det_submatrix_inl.{u_1, u_2, u_4} {m : Type u_1}
  {p : Type u_2} {R : Type u_4} [CommRing R] [Fintype m] [Fintype p] [DecidableEq m] [DecidableEq p]
  (A B : Matrix (m ⊕ p) (m ⊕ p) R) (hAB : A * B = 1) (σ τ : Equiv.Perm (m ⊕ p)) :
  (A.submatrix (⇑τ ∘ Sum.inr) (⇑σ ∘ Sum.inr)).det =
    ↑↑(Equiv.Perm.sign σ) * ↑↑(Equiv.Perm.sign τ) * A.det *
      (B.submatrix (⇑σ ∘ Sum.inl) (⇑τ ∘ Sum.inl)).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.det_submatrix_inr_eq_sign_mul_det_mul_det_submatrix_inl`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Determinant/ComplementaryMinor.html#Matrix.det_submatrix_inr_eq_sign_mul_det_mul_det_submatrix_inl).

## Other forms

**Jacobi's complementary-minor identity for an arbitrary index type `n`, split into two groups of indices by an equivalence `e : m ⊕ p ≃ n`.** Formalized in Tau Ceti as [`Matrix.det_submatrix_comp_inr_eq_sign_mul_det_mul_det_submatrix_comp_inl`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Determinant/ComplementaryMinor.html#Matrix.det_submatrix_comp_inr_eq_sign_mul_det_mul_det_submatrix_comp_inl).

```lean
Matrix.det_submatrix_comp_inr_eq_sign_mul_det_mul_det_submatrix_comp_inl.{u_1, u_2, u_3, u_4}
  {m : Type u_1} {p : Type u_2} {n : Type u_3} {R : Type u_4} [CommRing R] [Fintype m] [Fintype p]
  [DecidableEq m] [DecidableEq p] [Fintype n] [DecidableEq n] (A B : Matrix n n R) (hAB : A * B = 1)
  (e : m ⊕ p ≃ n) (σ τ : Equiv.Perm n) :
  (A.submatrix (⇑τ ∘ ⇑e ∘ Sum.inr) (⇑σ ∘ ⇑e ∘ Sum.inr)).det =
    ↑↑(Equiv.Perm.sign σ) * ↑↑(Equiv.Perm.sign τ) * A.det *
      (B.submatrix (⇑σ ∘ ⇑e ∘ Sum.inl) (⇑τ ∘ ⇑e ∘ Sum.inl)).det
```

## Sources

- [Tau Ceti documentation: `Matrix.det_submatrix_inr_eq_sign_mul_det_mul_det_submatrix_inl`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Determinant/ComplementaryMinor.html#Matrix.det_submatrix_inr_eq_sign_mul_det_mul_det_submatrix_inl)
- [Source of `Matrix.det_submatrix_inr_eq_sign_mul_det_mul_det_submatrix_inl` in TauCeti/LinearAlgebra/Matrix/Determinant/ComplementaryMinor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/Determinant/ComplementaryMinor.lean#L69)
