---
declaration: def
origin: cited
lean: TauCeti.continuousCyclicCochains
statement: formalized
---

# TauCeti.continuousCyclicCochains

The submodule of jointly continuous cochains satisfying the signed cyclic relation.

```lean
TauCeti.continuousCyclicCochains.{u_1, u_2, u_3} (R : Type u_1) (A : Type u_2) (M : Type u_3)
  [Semiring R] [AddCommMonoid A] [_root_.Module R A] [TopologicalSpace A] [AddCommGroup M]
  [_root_.Module R M] [SMulCommClass R R M] [TopologicalSpace M] [ContinuousConstSMul R M]
  [ContinuousAdd M] (n : ℕ) : Submodule R (A [×n + 1]→L[R] M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuousCyclicCochains`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Continuous/Basic.html#TauCeti.continuousCyclicCochains).

## Sources

- [Tau Ceti documentation: `TauCeti.continuousCyclicCochains`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Continuous/Basic.html#TauCeti.continuousCyclicCochains)
- [Source of `TauCeti.continuousCyclicCochains` in TauCeti/RingTheory/CyclicCohomology/Continuous/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/Continuous/Basic.lean#L336)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
