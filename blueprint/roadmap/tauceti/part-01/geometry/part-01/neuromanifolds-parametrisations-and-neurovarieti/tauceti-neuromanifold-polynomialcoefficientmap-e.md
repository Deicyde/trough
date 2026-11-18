---
declaration: theorem
origin: cited
lean: TauCeti.Neuromanifold.polynomialCoefficientMap_eq_iff
statement: formalized
proof: formalized
---

# TauCeti.Neuromanifold.polynomialCoefficientMap_eq_iff

Over an infinite integral domain, parameters of a jointly polynomial tuple realize the same
function exactly when they have the same input coefficients.

```lean
TauCeti.Neuromanifold.polynomialCoefficientMap_eq_iff.{u_1, u_2, u_3, u_4} {W : Type u_1}
  {X : Type u_2} {J : Type u_3} [Fintype J] {K : Type u_4} [CommRing K] [IsDomain K] [Infinite K]
  (P : J → MvPolynomial (W ⊕ X) K) {w v : W → K} :
  TauCeti.Neuromanifold.polynomialCoefficientMap P w =
      TauCeti.Neuromanifold.polynomialCoefficientMap P v ↔
    TauCeti.Neuromanifold.polynomialRealization P w =
      TauCeti.Neuromanifold.polynomialRealization P v
```

## Depends on

- [TauCeti.Neuromanifold.polynomialCoefficientMap](tauceti-neuromanifold-polynomialcoefficientmap.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.polynomialCoefficientMap_eq_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Polynomial/Presentation.html#TauCeti.Neuromanifold.polynomialCoefficientMap_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.polynomialCoefficientMap_eq_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Polynomial/Presentation.html#TauCeti.Neuromanifold.polynomialCoefficientMap_eq_iff)
- [Source of `TauCeti.Neuromanifold.polynomialCoefficientMap_eq_iff` in TauCeti/Geometry/Neuromanifold/Polynomial/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Neuromanifold/Polynomial/Presentation.lean#L56)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Neuromanifolds/STATUS.md)
