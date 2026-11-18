---
declaration: theorem
origin: cited
lean: TauCeti.LaurentRing.isLocalization
statement: formalized
proof: formalized
---

# The Laurent ring is the localization of the polynomial ring at the variables

the
variables become units, every Laurent polynomial is a polynomial divided by a monomial in the
variables, and distinct polynomials stay distinct.

```lean
TauCeti.LaurentRing.isLocalization.{u_1, u_2} {R : Type u_1} [CommSemiring R] {K : Type u_2} :
  IsLocalization (Submonoid.closure (Set.range MvPolynomial.X)) (TauCeti.LaurentRing R K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentRing.isLocalization`](https://taucetiproject.org/docs/TauCeti/Algebra/MvPolynomial/Laurent/Polynomial.html#TauCeti.LaurentRing.isLocalization).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentRing.isLocalization`](https://taucetiproject.org/docs/TauCeti/Algebra/MvPolynomial/Laurent/Polynomial.html#TauCeti.LaurentRing.isLocalization)
- [Source of `TauCeti.LaurentRing.isLocalization` in TauCeti/Algebra/MvPolynomial/Laurent/Polynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/MvPolynomial/Laurent/Polynomial.lean#L247)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
