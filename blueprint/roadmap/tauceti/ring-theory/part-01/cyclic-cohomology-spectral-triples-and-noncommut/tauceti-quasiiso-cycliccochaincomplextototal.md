---
declaration: theorem
origin: cited
lean: TauCeti.quasiIso_cyclicCochainComplexToTotal
statement: formalized
proof: formalized
---

# TauCeti.quasiIso_cyclicCochainComplexToTotal

Over a ring containing `ℚ`, the inclusion of Connes' cyclic cochain complex into the total
complex of the cyclic bicomplex is a quasi-isomorphism: cyclic cohomology defined by cyclic cochains
is the cohomology of the total cyclic bicomplex.

```lean
TauCeti.quasiIso_cyclicCochainComplexToTotal.{u, u_1, u_2} (R : Type u_1) (A : Type u)
  (M : Type u_2) [CommRing R] [NonUnitalSemiring A] [_root_.Module R A] [IsScalarTower R A A]
  [SMulCommClass R A A] [AddCommGroup M] [_root_.Module R M] [Algebra ℚ R] :
  QuasiIso (TauCeti.cyclicCochainComplexToTotal R A M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.quasiIso_cyclicCochainComplexToTotal`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Bicomplex.html#TauCeti.quasiIso_cyclicCochainComplexToTotal).

## Sources

- [Tau Ceti documentation: `TauCeti.quasiIso_cyclicCochainComplexToTotal`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Bicomplex.html#TauCeti.quasiIso_cyclicCochainComplexToTotal)
- [Source of `TauCeti.quasiIso_cyclicCochainComplexToTotal` in TauCeti/RingTheory/CyclicCohomology/Bicomplex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/Bicomplex.lean#L812)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
