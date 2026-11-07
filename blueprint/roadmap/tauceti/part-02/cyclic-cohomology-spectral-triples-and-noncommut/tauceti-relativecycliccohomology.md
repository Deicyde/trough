---
declaration: abbrev
origin: cited
lean: TauCeti.relativeCyclicCohomology
statement: formalized
---

# TauCeti.relativeCyclicCohomology

The relative cyclic cohomology of a nonunital algebra: the reduced cyclic cohomology of its
forced unitization, the cohomology of the kernel of scalar restriction on the cyclic cochain
complex of the forced unitization.

```lean
TauCeti.relativeCyclicCohomology.{u, u_1, u_2} (R : Type u_1) (A : Type u) (M : Type u_2)
  [CommRing R] [NonUnitalSemiring A] [_root_.Module R A] [IsScalarTower R A A] [SMulCommClass R A A]
  [AddCommGroup M] [_root_.Module R M] (n : ℕ) : ModuleCat R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.relativeCyclicCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Relative/Basic.html#TauCeti.relativeCyclicCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.relativeCyclicCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Relative/Basic.html#TauCeti.relativeCyclicCohomology)
- [Source of `TauCeti.relativeCyclicCohomology` in TauCeti/RingTheory/CyclicCohomology/Relative/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/Relative/Basic.lean#L125)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
