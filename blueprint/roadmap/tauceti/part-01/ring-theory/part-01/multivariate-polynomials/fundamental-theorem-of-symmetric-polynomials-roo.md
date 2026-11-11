---
declaration: theorem
origin: cited
lean: MvPolynomial.aeval_multiset_esymm_X_injective
statement: formalized
proof: formalized
---

# Fundamental theorem of symmetric polynomials, root form

if `n ≤ card σ`, a polynomial in
`n` variables is determined by its value at the elementary symmetric functions
`e₁, …, eₙ` of the multiset of variables of `σ`.

```lean
MvPolynomial.aeval_multiset_esymm_X_injective.{u_1, u_2} (R : Type u_1) [CommRing R] {σ : Type u_2}
  [Fintype σ] {n : ℕ} (hn : n ≤ Fintype.card σ) :
  Function.Injective
    ⇑(MvPolynomial.aeval fun j => (Multiset.map MvPolynomial.X Finset.univ.val).esymm (↑j + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.aeval_multiset_esymm_X_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/FundamentalTheorem.html#MvPolynomial.aeval_multiset_esymm_X_injective).

## Sources

- [Tau Ceti documentation: `MvPolynomial.aeval_multiset_esymm_X_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/FundamentalTheorem.html#MvPolynomial.aeval_multiset_esymm_X_injective)
- [Source of `MvPolynomial.aeval_multiset_esymm_X_injective` in TauCeti/RingTheory/MvPolynomial/Symmetric/FundamentalTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Symmetric/FundamentalTheorem.lean#L37)
