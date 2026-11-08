---
declaration: theorem
origin: cited
lean: TauCeti.det_submatrix_hsymmToeplitz
statement: formalized
proof: formalized
---

# Jacobi's complementary-minor identity for the two Toeplitz matrices of symmetric polynomials

A minor of `(h_{j - i})` on the rows `ρ (p)` and the columns `π (p)` is the
complementary minor of `((-1)^{j - i} e_{j - i})`, on the rows `π (m)` and the columns `ρ (m)`,
signed by `π` and `ρ`.

```lean
TauCeti.det_submatrix_hsymmToeplitz.{u_1, u_2, u_3, u_4} (σ : Type u_1) [Fintype σ] [DecidableEq σ]
  (R : Type u_2) [CommRing R] {m : Type u_3} {p : Type u_4} [Fintype m] [Fintype p] [DecidableEq m]
  [DecidableEq p] (N : ℕ) (e : m ⊕ p ≃ Fin N) (π ρ : Equiv.Perm (Fin N)) :
  ((TauCeti.hsymmToeplitz σ R N).submatrix (⇑ρ ∘ ⇑e ∘ Sum.inr) (⇑π ∘ ⇑e ∘ Sum.inr)).det =
    ↑↑(Equiv.Perm.sign π) * ↑↑(Equiv.Perm.sign ρ) *
      ((TauCeti.esymmToeplitz σ R N).submatrix (⇑π ∘ ⇑e ∘ Sum.inl) (⇑ρ ∘ ⇑e ∘ Sum.inl)).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's complementary-minor identity](../../../linear-algebra/matrix/jacobis-complementary-minor-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.det_submatrix_hsymmToeplitz`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Complete/ToeplitzMinor.html#TauCeti.det_submatrix_hsymmToeplitz).

## Sources

- [Tau Ceti documentation: `TauCeti.det_submatrix_hsymmToeplitz`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Complete/ToeplitzMinor.html#TauCeti.det_submatrix_hsymmToeplitz)
- [Source of `TauCeti.det_submatrix_hsymmToeplitz` in TauCeti/RingTheory/MvPolynomial/Symmetric/Complete/ToeplitzMinor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPolynomial/Symmetric/Complete/ToeplitzMinor.lean#L52)
