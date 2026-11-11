---
declaration: theorem
origin: cited
lean: TauCeti.exact_cyclicTotalHomologyConnesB_cyclicTotalHomologyPeriodicity
statement: formalized
proof: formalized
---

# Exactness of `HH^(m+1) → H^m(Tot) → H^(m+2)(Tot)`

For a unital algebra, a class in the
cohomology of the total cyclic bicomplex is killed by the periodicity map exactly when it is the
image under `B` of a Hochschild class.

```lean
TauCeti.exact_cyclicTotalHomologyConnesB_cyclicTotalHomologyPeriodicity.{u, u_1, u_2} {R : Type u_1}
  {A : Type u} {M : Type u_2} [CommRing R] [Ring A] [Algebra R A] [AddCommGroup M]
  [_root_.Module R M] (m : ℕ) :
  Function.Exact ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.cyclicTotalHomologyConnesB R A M m))
    ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.cyclicTotalHomologyPeriodicity R A M m))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exact_cyclicTotalHomologyConnesB_cyclicTotalHomologyPeriodicity`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/ExactSequence.html#TauCeti.exact_cyclicTotalHomologyConnesB_cyclicTotalHomologyPeriodicity).

## Sources

- [Tau Ceti documentation: `TauCeti.exact_cyclicTotalHomologyConnesB_cyclicTotalHomologyPeriodicity`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/ExactSequence.html#TauCeti.exact_cyclicTotalHomologyConnesB_cyclicTotalHomologyPeriodicity)
- [Source of `TauCeti.exact_cyclicTotalHomologyConnesB_cyclicTotalHomologyPeriodicity` in TauCeti/RingTheory/CyclicCohomology/ExactSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/ExactSequence.lean#L392)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
