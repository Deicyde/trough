---
declaration: theorem
origin: cited
lean: MvPolynomial.linearIndependent_iff_exists_genWronskian_ne_zero
statement: formalized
proof: formalized
---

# The generalized Wronskian criterion

Over a field of characteristic zero, a family of
multivariate polynomials is linearly independent if and only if some generalized Wronskian with
admissible rows `|D k| ≤ k` is nonzero.

```lean
MvPolynomial.linearIndependent_iff_exists_genWronskian_ne_zero.{u_3, u_4} {σ : Type u_3} {m : ℕ}
  {K : Type u_4} [Field K] [CharZero K] {f : Fin m → MvPolynomial σ K} :
  LinearIndependent K f ↔
    ∃ D, (∀ (k : Fin m), Finsupp.degree (D k) ≤ ↑k) ∧ MvPolynomial.genWronskian D f ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.linearIndependent_iff_exists_genWronskian_ne_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/HasseDeriv/Wronskian.html#MvPolynomial.linearIndependent_iff_exists_genWronskian_ne_zero).

## Sources

- [Tau Ceti documentation: `MvPolynomial.linearIndependent_iff_exists_genWronskian_ne_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/HasseDeriv/Wronskian.html#MvPolynomial.linearIndependent_iff_exists_genWronskian_ne_zero)
- [Source of `MvPolynomial.linearIndependent_iff_exists_genWronskian_ne_zero` in TauCeti/RingTheory/MvPolynomial/HasseDeriv/Wronskian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/HasseDeriv/Wronskian.lean#L231)
