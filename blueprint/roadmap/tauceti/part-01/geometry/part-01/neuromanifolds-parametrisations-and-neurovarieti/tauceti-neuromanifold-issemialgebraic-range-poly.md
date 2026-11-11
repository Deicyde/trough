---
declaration: theorem
origin: cited
lean: TauCeti.Neuromanifold.isSemialgebraic_range_polynomialCoefficientCoordinates
statement: formalized
proof: formalized
---

# TauCeti.Neuromanifold.isSemialgebraic_range_polynomialCoefficientCoordinates

Given projection closure, the full finite coefficient image of every jointly polynomial model
is semialgebraic, without a closed-image assumption.

```lean
TauCeti.Neuromanifold.isSemialgebraic_range_polynomialCoefficientCoordinates.{u_1, u_2, u_3, u_4}
  {R : Type u_1} [CommRing R] [LinearOrder R] [TauCeti.HasSemialgebraicProjections R] {W : Type u_2}
  {X : Type u_3} {J : Type u_4} [Finite W] [Finite X] [Fintype J] (P : J → MvPolynomial (W ⊕ X) R) :
  TauCeti.IsSemialgebraic (Set.range (TauCeti.Neuromanifold.polynomialCoefficientCoordinates P))
```

## Depends on

- [TauCeti.Neuromanifold.polynomialCoefficientMap](tauceti-neuromanifold-polynomialcoefficientmap.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.isSemialgebraic_range_polynomialCoefficientCoordinates`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Polynomial/Semialgebraic.html#TauCeti.Neuromanifold.isSemialgebraic_range_polynomialCoefficientCoordinates).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.isSemialgebraic_range_polynomialCoefficientCoordinates`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Polynomial/Semialgebraic.html#TauCeti.Neuromanifold.isSemialgebraic_range_polynomialCoefficientCoordinates)
- [Source of `TauCeti.Neuromanifold.isSemialgebraic_range_polynomialCoefficientCoordinates` in TauCeti/Geometry/Neuromanifold/Polynomial/Semialgebraic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Neuromanifold/Polynomial/Semialgebraic.lean#L53)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Neuromanifolds/STATUS.md)
