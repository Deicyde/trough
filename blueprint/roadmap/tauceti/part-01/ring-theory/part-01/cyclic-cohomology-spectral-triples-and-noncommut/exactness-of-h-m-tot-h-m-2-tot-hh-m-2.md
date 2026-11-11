---
declaration: theorem
origin: cited
lean: TauCeti.exact_cyclicTotalHomologyPeriodicity_homologyMap_cyclicTotalComplexToHochschild
statement: formalized
proof: formalized
---

# Exactness of `H^m(Tot) → H^(m+2)(Tot) → HH^(m+2)`

For a unital algebra, a class in the
cohomology of the total cyclic bicomplex is in the image of the periodicity map exactly when its
projection onto column zero vanishes in Hochschild cohomology.

```lean
TauCeti.exact_cyclicTotalHomologyPeriodicity_homologyMap_cyclicTotalComplexToHochschild.{u, u_1,
    u_2}
  (R : Type u_1) (A : Type u) (M : Type u_2) [CommRing R] [Semiring A] [_root_.Module R A]
  [IsScalarTower R A A] [SMulCommClass R A A] [AddCommGroup M] [_root_.Module R M] (m : ℕ) :
  Function.Exact
    ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.cyclicTotalHomologyPeriodicity R A M m))
    ⇑(CategoryTheory.ConcreteCategory.hom
        (HomologicalComplex.homologyMap (TauCeti.cyclicTotalComplexToHochschild R A M) (m + 2)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exact_cyclicTotalHomologyPeriodicity_homologyMap_cyclicTotalComplexToHochschild`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Periodicity.html#TauCeti.exact_cyclicTotalHomologyPeriodicity_homologyMap_cyclicTotalComplexToHochschild).

## Sources

- [Tau Ceti documentation: `TauCeti.exact_cyclicTotalHomologyPeriodicity_homologyMap_cyclicTotalComplexToHochschild`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Periodicity.html#TauCeti.exact_cyclicTotalHomologyPeriodicity_homologyMap_cyclicTotalComplexToHochschild)
- [Source of `TauCeti.exact_cyclicTotalHomologyPeriodicity_homologyMap_cyclicTotalComplexToHochschild` in TauCeti/RingTheory/CyclicCohomology/Periodicity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/Periodicity.lean#L494)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
