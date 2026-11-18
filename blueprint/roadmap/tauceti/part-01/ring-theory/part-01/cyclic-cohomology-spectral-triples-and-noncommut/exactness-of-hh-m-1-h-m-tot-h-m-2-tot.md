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
- [Source of `TauCeti.exact_cyclicTotalHomologyConnesB_cyclicTotalHomologyPeriodicity` in TauCeti/RingTheory/CyclicCohomology/ExactSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/CyclicCohomology/ExactSequence.lean#L406)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
