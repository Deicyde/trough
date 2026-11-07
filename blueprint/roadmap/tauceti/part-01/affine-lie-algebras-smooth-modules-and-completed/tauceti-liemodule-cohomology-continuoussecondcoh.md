---
declaration: abbrev
origin: cited
lean: TauCeti.LieModule.Cohomology.continuousSecondCohomology
statement: formalized
---

# TauCeti.LieModule.Cohomology.continuousSecondCohomology

Continuous second Lie algebra cohomology with discrete coefficients: continuous two-cocycles
modulo the continuous coboundaries of continuous one-cochains.

```lean
TauCeti.LieModule.Cohomology.continuousSecondCohomology.{u_1, u_2, u_3} (R : Type u_1)
  (L : Type u_2) (M : Type u_3) [CommRing R] [LieRing L] [LieAlgebra R L] [TopologicalSpace L]
  [AddCommGroup M] [_root_.Module R M] [LieRingModule L M] [LieModule R L M] : Type (max u_2 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LieModule.Cohomology.continuousSecondCohomology`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/Continuous/Basic.html#TauCeti.LieModule.Cohomology.continuousSecondCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.LieModule.Cohomology.continuousSecondCohomology`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/Continuous/Basic.html#TauCeti.LieModule.Cohomology.continuousSecondCohomology)
- [Source of `TauCeti.LieModule.Cohomology.continuousSecondCohomology` in TauCeti/Algebra/Lie/Cohomology/Continuous/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Cohomology/Continuous/Basic.lean#L230)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
