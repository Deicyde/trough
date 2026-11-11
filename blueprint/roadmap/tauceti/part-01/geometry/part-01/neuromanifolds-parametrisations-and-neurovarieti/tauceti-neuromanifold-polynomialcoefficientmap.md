---
declaration: def
origin: cited
lean: TauCeti.Neuromanifold.polynomialCoefficientMap
statement: formalized
---

# TauCeti.Neuromanifold.polynomialCoefficientMap

The polynomial coefficient presentation takes values in a fixed product of
bounded-degree spaces, even when specialization cancels some monomials.

```lean
TauCeti.Neuromanifold.polynomialCoefficientMap.{u_1, u_2, u_3, u_4} {K : Type u_1} {W : Type u_2}
  {X : Type u_3} {J : Type u_4} [CommSemiring K] [Fintype J] (P : J → MvPolynomial (W ⊕ X) K)
  (w : W → K) :
  J → ↥(MvPolynomial.restrictTotalDegree X K (TauCeti.Neuromanifold.polynomialInputDegree P))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.polynomialCoefficientMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Polynomial/Basic.html#TauCeti.Neuromanifold.polynomialCoefficientMap).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.polynomialCoefficientMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Polynomial/Basic.html#TauCeti.Neuromanifold.polynomialCoefficientMap)
- [Source of `TauCeti.Neuromanifold.polynomialCoefficientMap` in TauCeti/Geometry/Neuromanifold/Polynomial/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Neuromanifold/Polynomial/Basic.lean#L174)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Neuromanifolds/STATUS.md)
