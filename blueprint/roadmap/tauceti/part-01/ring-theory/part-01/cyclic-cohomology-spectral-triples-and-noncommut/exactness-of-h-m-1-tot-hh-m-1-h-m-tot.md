---
declaration: theorem
origin: cited
lean: TauCeti.exact_homologyMap_cyclicTotalComplexToHochschild_cyclicTotalHomologyConnesB
statement: formalized
proof: formalized
---

# Exactness of `H^(m+1)(Tot) → HH^(m+1) → H^m(Tot)`

For a unital algebra, a Hochschild
class is killed by `B` exactly when it is the projection onto column zero of a class in the
cohomology of the total cyclic bicomplex.

```lean
TauCeti.exact_homologyMap_cyclicTotalComplexToHochschild_cyclicTotalHomologyConnesB.{u, u_1, u_2}
  {R : Type u_1} {A : Type u} {M : Type u_2} [CommRing R] [Ring A] [Algebra R A] [AddCommGroup M]
  [_root_.Module R M] (m : ℕ) :
  Function.Exact
    ⇑(CategoryTheory.ConcreteCategory.hom
        (HomologicalComplex.homologyMap (TauCeti.cyclicTotalComplexToHochschild R A M) (m + 1)))
    ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.cyclicTotalHomologyConnesB R A M m))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exact_homologyMap_cyclicTotalComplexToHochschild_cyclicTotalHomologyConnesB`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/ExactSequence.html#TauCeti.exact_homologyMap_cyclicTotalComplexToHochschild_cyclicTotalHomologyConnesB).

## Sources

- [Tau Ceti documentation: `TauCeti.exact_homologyMap_cyclicTotalComplexToHochschild_cyclicTotalHomologyConnesB`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/ExactSequence.html#TauCeti.exact_homologyMap_cyclicTotalComplexToHochschild_cyclicTotalHomologyConnesB)
- [Source of `TauCeti.exact_homologyMap_cyclicTotalComplexToHochschild_cyclicTotalHomologyConnesB` in TauCeti/RingTheory/CyclicCohomology/ExactSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/ExactSequence.lean#L348)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
