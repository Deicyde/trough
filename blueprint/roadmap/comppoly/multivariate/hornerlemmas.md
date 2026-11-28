---
catalog: module
lean: CPoly.CMvPolynomial.eval₂Horner_eq_eval₂, CPoly.CMvPolynomial.evalHorner_eq_eval
statement: formalized
proof: formalized
---

# Correctness lemmas for multivariate Horner evaluation

`CompPoly.Multivariate.HornerLemmas`, in [CompPoly/Multivariate/HornerLemmas.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/HornerLemmas.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdușa, Derek Sorensen, Dimitris Mitsios.

> This file proves that the fixed-order multivariate Horner evaluator in
> `CompPoly.Multivariate.Basic` agrees with ordinary multivariate
> evaluation.

> ### Mathematical specifications for Horner helper functions

> ### Shared list algebra

> ### Group sorting invariants

> ### Grouping preserves weighted sums

> ### Sparse Horner over evaluated groups

> ### Recursive term evaluator correctness

`CPoly.CMvPolynomial.eval₂Horner_eq_eval₂` (theorem, [line 450](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/HornerLemmas.lean#L450))

> Fixed-order multivariate Horner evaluation agrees with ordinary evaluation.

```lean
theorem eval₂Horner_eq_eval₂ {R S : Type*} {n : ℕ} [Semiring R] [CommSemiring S]
    (f : R →+* S) (vs : Fin n → S) (p : CMvPolynomial n R) :
    eval₂Horner f vs p = eval₂ f vs p
```

`CPoly.CMvPolynomial.evalHorner_eq_eval` (theorem, [line 477](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/HornerLemmas.lean#L477))

> Fixed-order multivariate Horner evaluation agrees with ordinary evaluation.

```lean
theorem evalHorner_eq_eval {R : Type*} {n : ℕ} [CommSemiring R]
    (vs : Fin n → R) (p : CMvPolynomial n R) :
    evalHorner vs p = eval vs p
```

## Depends on

- [Computable multivariate polynomials](basic.md)

## Sources

- [CompPoly/Multivariate/HornerLemmas.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/HornerLemmas.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.HornerLemmas.json)
