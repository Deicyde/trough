---
declaration: def
origin: cited
lean: TauCeti.periodicCyclicCohomology
statement: formalized
---

# Periodic cyclic cohomology `HP^n(A; M)`

the direct limit of the cohomology groups
`H^(n+2k)(Tot)` of the total cyclic bicomplex under the periodicity maps `S`.

```lean
TauCeti.periodicCyclicCohomology.{u, v, u_1} (R : Type u_1) (A : Type u) (M : Type v) [CommRing R]
  [NonUnitalSemiring A] [_root_.Module R A] [IsScalarTower R A A] [SMulCommClass R A A]
  [AddCommGroup M] [_root_.Module R M] (n : ℕ) : ModuleCat R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.periodicCyclicCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.html#TauCeti.periodicCyclicCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.periodicCyclicCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.html#TauCeti.periodicCyclicCohomology)
- [Source of `TauCeti.periodicCyclicCohomology` in TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.lean#L117)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
