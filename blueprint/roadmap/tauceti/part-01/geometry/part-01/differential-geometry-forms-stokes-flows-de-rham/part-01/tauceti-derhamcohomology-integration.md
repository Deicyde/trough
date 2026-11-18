---
declaration: def
origin: cited
lean: TauCeti.deRhamCohomology.integration
statement: formalized
---

# TauCeti.deRhamCohomology.integration

The homomorphism from de Rham cohomology to smooth singular cohomology induced by integration.
This does not identify smooth singular cohomology with ordinary singular cohomology.

```lean
TauCeti.deRhamCohomology.integration {E H : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] (I : ModelWithCorners ℝ E H) (M : Type) [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I 2 M] (k : ℕ) :
  TauCeti.deRhamCohomology I M k →ₗ[ℝ]
    ↑(HomologicalComplex.homology
        (((TauCeti.smoothSingularSubcomplex I M).toSSet.chainComplex ↧ℝ).linearYonedaObj ℝ ↧ℝ) k)
```

## Depends on

- [TauCeti.deRhamIntegration](tauceti-derhamintegration.md)
- [TauCeti.smoothSingularSubcomplex](tauceti-smoothsingularsubcomplex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.deRhamCohomology.integration`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/DeRham.html#TauCeti.deRhamCohomology.integration).

## Sources

- [Tau Ceti documentation: `TauCeti.deRhamCohomology.integration`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/DeRham.html#TauCeti.deRhamCohomology.integration)
- [Source of `TauCeti.deRhamCohomology.integration` in TauCeti/Geometry/Manifold/SmoothSingular/DeRham.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothSingular/DeRham.lean#L147)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
