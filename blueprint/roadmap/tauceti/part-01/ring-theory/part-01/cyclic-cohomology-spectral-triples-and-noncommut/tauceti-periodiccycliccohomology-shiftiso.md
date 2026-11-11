---
declaration: def
origin: cited
lean: TauCeti.periodicCyclicCohomology.shiftIso
statement: formalized
---

# TauCeti.periodicCyclicCohomology.shiftIso

Periodic cyclic cohomology is `2`-periodic: `HP^(n+2) ≅ HP^n`, identifying the stage
`H^(n+2+2k)(Tot)` of `HP^(n+2)` with the stage `H^(n+2(k+1))(Tot)` of `HP^n`.

```lean
TauCeti.periodicCyclicCohomology.shiftIso.{u, v, u_1} (R : Type u_1) (A : Type u) (M : Type v)
  [CommRing R] [NonUnitalSemiring A] [_root_.Module R A] [IsScalarTower R A A] [SMulCommClass R A A]
  [AddCommGroup M] [_root_.Module R M] (n : ℕ) :
  TauCeti.periodicCyclicCohomology R A M (n + 2) ≅ TauCeti.periodicCyclicCohomology R A M n
```

## Depends on

- [Periodic cyclic cohomology `HP^n(A; M)`](periodic-cyclic-cohomology-hp-n-a-m.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.periodicCyclicCohomology.shiftIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.html#TauCeti.periodicCyclicCohomology.shiftIso).

## Sources

- [Tau Ceti documentation: `TauCeti.periodicCyclicCohomology.shiftIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.html#TauCeti.periodicCyclicCohomology.shiftIso)
- [Source of `TauCeti.periodicCyclicCohomology.shiftIso` in TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.lean#L244)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
