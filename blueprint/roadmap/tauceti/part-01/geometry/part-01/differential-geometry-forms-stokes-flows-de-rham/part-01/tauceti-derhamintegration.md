---
declaration: def
origin: cited
lean: TauCeti.deRhamIntegration
statement: formalized
---

# TauCeti.deRhamIntegration

Integration of forms as a map from the de Rham complex to the dual of smooth singular
chains. Its commutation with differentials is Stokes' theorem.

```lean
TauCeti.deRhamIntegration {E H : Type} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  (I : ModelWithCorners ℝ E H) (M : Type) [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I 2 M] :
  TauCeti.deRhamComplex I M ⟶
    ((TauCeti.smoothSingularSubcomplex I M).toSSet.chainComplex ↧ℝ).linearYonedaObj ℝ ↧ℝ
```

## Depends on

- [TauCeti.smoothSingularSubcomplex](tauceti-smoothsingularsubcomplex.md)

## Proof depends on

- [Stokes' theorem on singular `1`-chains](../../../part-02/manifold/part-04/stokes-theorem-on-singular-1-chains.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.deRhamIntegration`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/DeRham.html#TauCeti.deRhamIntegration).

## Sources

- [Tau Ceti documentation: `TauCeti.deRhamIntegration`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/DeRham.html#TauCeti.deRhamIntegration)
- [Source of `TauCeti.deRhamIntegration` in TauCeti/Geometry/Manifold/SmoothSingular/DeRham.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothSingular/DeRham.lean#L59)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
