---
declaration: theorem
origin: cited
lean: MvPolynomial.exists_ne_zero_forall_aeval_eq_zero
statement: formalized
proof: formalized
---

# The dimension theorem at the origin

let `K` be an algebraically closed extension of `k`.
Fewer than `#σ` polynomials in `k[X_σ]` vanishing at the origin have a common zero in `K^σ` other
than the origin.

```lean
MvPolynomial.exists_ne_zero_forall_aeval_eq_zero.{u_1, u_2, u_3} {k : Type u_1} {K : Type u_2}
  {σ : Type u_3} [Field k] [Field K] [Algebra k K] [IsAlgClosed K] [Finite σ]
  {s : Finset (MvPolynomial σ k)} (hs : s.card < Nat.card σ)
  (h0 : ∀ p ∈ s, MvPolynomial.constantCoeff p = 0) :
  ∃ x, x ≠ 0 ∧ ∀ p ∈ s, (MvPolynomial.aeval x) p = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.exists_ne_zero_forall_aeval_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/CommonZero.html#MvPolynomial.exists_ne_zero_forall_aeval_eq_zero).

## Sources

- [Tau Ceti documentation: `MvPolynomial.exists_ne_zero_forall_aeval_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/CommonZero.html#MvPolynomial.exists_ne_zero_forall_aeval_eq_zero)
- [Source of `MvPolynomial.exists_ne_zero_forall_aeval_eq_zero` in TauCeti/RingTheory/MvPolynomial/CommonZero.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/CommonZero.lean#L67)
