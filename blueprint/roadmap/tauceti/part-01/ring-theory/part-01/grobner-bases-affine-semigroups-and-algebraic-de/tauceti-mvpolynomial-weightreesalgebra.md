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
- [Source of `TauCeti.MvPolynomial.weightReesAlgebra` in TauCeti/RingTheory/MvPolynomial/WeightFiltration.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/WeightFiltration.lean#L273)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
