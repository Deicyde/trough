---
declaration: def
origin: cited
lean: TauCeti.dolbeaultCohomology.map
statement: formalized
---

# TauCeti.dolbeaultCohomology.map

The complex-linear map on Dolbeault cohomology induced by a holomorphic map `f`, given as a
smooth map of the underlying real manifolds whose differential is complex-linear: it pulls back
classes along `f`.

```lean
TauCeti.dolbeaultCohomology.map.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {M : Type u_2} [TopologicalSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℂ F] {E' : Type u_4} [NormedAddCommGroup E'] [NormedSpace ℂ E'] {M' : Type u_5}
  [TopologicalSpace M'] [ChartedSpace E' M'] [IsManifold (modelWithCornersSelf ℂ E') (↑⊤) M']
  {f : M → M'} (hf : ContMDiff (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E') (↑⊤) f)
  (hJ :
    TauCeti.IsPseudoholomorphic (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold E M)
      (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold E' M') f)
  (p q : ℕ) : TauCeti.dolbeaultCohomology E' M' F p q →ₗ[ℂ] TauCeti.dolbeaultCohomology E M F p q
```

## Depends on

- [TauCeti.dolbeaultCohomology](tauceti-dolbeaultcohomology.md)

## Proof depends on

- [`∂bar² = 0` on a complex manifold](bar2-0-on-a-complex-manifold.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dolbeaultCohomology.map`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Cohomology.html#TauCeti.dolbeaultCohomology.map).

## Sources

- [Tau Ceti documentation: `TauCeti.dolbeaultCohomology.map`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Cohomology.html#TauCeti.dolbeaultCohomology.map)
- [Source of `TauCeti.dolbeaultCohomology.map` in TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Cohomology.lean#L234)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
