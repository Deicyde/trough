---
declaration: theorem
origin: cited
lean: TauCeti.nontrivial_deRhamCohomology_circle_one
statement: formalized
proof: formalized
---

# TauCeti.nontrivial\_deRhamCohomology\_circle\_one

The first de Rham cohomology of the circle is nontrivial.

```lean
TauCeti.nontrivial_deRhamCohomology_circle_one :
  Nontrivial (TauCeti.deRhamCohomology (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin 1))) Circle 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.pathIntegral](tauceti-pathintegral.md)
- [TauCeti.pathIntegral\_mextDeriv](tauceti-pathintegral-mextderiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nontrivial_deRhamCohomology_circle_one`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Circle.html#TauCeti.nontrivial_deRhamCohomology_circle_one).

## Sources

- [Tau Ceti documentation: `TauCeti.nontrivial_deRhamCohomology_circle_one`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Circle.html#TauCeti.nontrivial_deRhamCohomology_circle_one)
- [Source of `TauCeti.nontrivial_deRhamCohomology_circle_one` in TauCeti/Geometry/Manifold/DeRham/Circle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/Circle.lean#L178)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
