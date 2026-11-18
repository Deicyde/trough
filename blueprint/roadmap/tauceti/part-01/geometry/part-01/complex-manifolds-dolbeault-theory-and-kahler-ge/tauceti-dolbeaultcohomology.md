---
declaration: abbrev
origin: cited
lean: TauCeti.dolbeaultCohomology
statement: formalized
---

# TauCeti.dolbeaultCohomology

Dolbeault cohomology is the native categorical cohomology of the Dolbeault complex.

```lean
TauCeti.dolbeaultCohomology.{u_1, u_2, u_3} (E : Type u_1) [NormedAddCommGroup E] [NormedSpace ℂ E]
  (M : Type u_2) [TopologicalSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] (F : Type u_3) [NormedAddCommGroup F]
  [NormedSpace ℂ F] (p q : ℕ) : Type (max (max u_1 u_2) u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [`∂bar² = 0` on a complex manifold](bar2-0-on-a-complex-manifold.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dolbeaultCohomology`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Complex.html#TauCeti.dolbeaultCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.dolbeaultCohomology`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Complex.html#TauCeti.dolbeaultCohomology)
- [Source of `TauCeti.dolbeaultCohomology` in TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Complex.lean#L151)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
