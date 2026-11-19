---
declaration: theorem
origin: cited
lean: MvPolynomial.exists_pderiv_eq
statement: formalized
proof: formalized
---

# Polynomial Poincaré lemma

Over a `ℚ`-algebra, a family `P` of polynomials in finitely
many variables of total degree at most `m` satisfying the symmetry condition `∂ⱼ Pᵢ = ∂ᵢ Pⱼ` is
the gradient of a polynomial of total degree at most `m + 1`.

```lean
MvPolynomial.exists_pderiv_eq.{u_1, u_2} {R : Type u_1} {σ : Type u_2} [CommRing R] [Algebra ℚ R]
  [Finite σ] {m : ℕ} (P : σ → MvPolynomial σ R)
  (hP : ∀ (i : σ), P i ∈ MvPolynomial.restrictTotalDegree σ R m)
  (hsymm : ∀ (i j : σ), (MvPolynomial.pderiv j) (P i) = (MvPolynomial.pderiv i) (P j)) :
  ∃ Q ∈ MvPolynomial.restrictTotalDegree σ R (m + 1), ∀ (i : σ), (MvPolynomial.pderiv i) Q = P i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.exists_pderiv_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/PoincareLemma.html#MvPolynomial.exists_pderiv_eq).

## Sources

- [Tau Ceti documentation: `MvPolynomial.exists_pderiv_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/PoincareLemma.html#MvPolynomial.exists_pderiv_eq)
- [Source of `MvPolynomial.exists_pderiv_eq` in TauCeti/RingTheory/MvPolynomial/PoincareLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/PoincareLemma.lean#L78)
