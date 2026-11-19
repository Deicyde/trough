---
declaration: theorem
origin: cited
lean: TauCeti.nontrivial_compactlySupportedDeRhamCohomology_iff_orientable
statement: formalized
proof: formalized
---

# TauCeti.nontrivial_compactlySupportedDeRhamCohomology_iff_orientable

On a connected boundaryless Hausdorff σ-compact finite-dimensional smooth manifold `M` of
dimension `n`, the top compactly supported de Rham cohomology `H^n_c(M)` is nonzero if and only
if `M` is orientable.

```lean
TauCeti.nontrivial_compactlySupportedDeRhamCohomology_iff_orientable.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M] [SigmaCompactSpace M]
  [ConnectedSpace M] :
  Nontrivial (TauCeti.compactlySupportedDeRhamCohomology I M (Module.finrank ℝ E)) ↔
    TauCeti.Orientable I M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The top compactly supported cohomology of a connected manifold](the-top-compactly-supported-cohomology-of-a-conn.md)
- [Top compactly supported cohomology of a nonorientable manifold](top-compactly-supported-cohomology-of-a-nonorien.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nontrivial_compactlySupportedDeRhamCohomology_iff_orientable`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/OrientationCover.html#TauCeti.nontrivial_compactlySupportedDeRhamCohomology_iff_orientable).

## Sources

- [Tau Ceti documentation: `TauCeti.nontrivial_compactlySupportedDeRhamCohomology_iff_orientable`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/OrientationCover.html#TauCeti.nontrivial_compactlySupportedDeRhamCohomology_iff_orientable)
- [Source of `TauCeti.nontrivial_compactlySupportedDeRhamCohomology_iff_orientable` in TauCeti/Geometry/Manifold/DeRham/OrientationCover.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DeRham/OrientationCover.lean#L181)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
