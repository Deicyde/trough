---
declaration: abbrev
origin: cited
lean: TauCeti.MvPolynomial.weightReesAlgebra
statement: formalized
---

# TauCeti.MvPolynomial.weightReesAlgebra

The Rees algebra of the weight filtration: the polynomials `∑ bₙ tⁿ` over
`MvPolynomial σ R` such that every monomial of `bₙ` has weight at most `n`.

```lean
TauCeti.MvPolynomial.weightReesAlgebra.{u_1, u_2} {σ : Type u_1} (R : Type u_2) [CommSemiring R]
  (w : σ → ℕ) : Subalgebra R (Polynomial (MvPolynomial σ R))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPolynomial.weightReesAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/WeightFiltration.html#TauCeti.MvPolynomial.weightReesAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPolynomial.weightReesAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/WeightFiltration.html#TauCeti.MvPolynomial.weightReesAlgebra)
- [Source of `TauCeti.MvPolynomial.weightReesAlgebra` in TauCeti/RingTheory/MvPolynomial/WeightFiltration.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/WeightFiltration.lean#L273)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
