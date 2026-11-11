---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.OrientationCover.integral_map_proj_eq_zero
statement: formalized
proof: formalized
---

# TauCeti.Manifold.OrientationCover.integral_map_proj_eq_zero

Integration on top compactly supported cohomology of the orientation double cover, for its
canonical orientation, vanishes on every class pulled back from `M`.

```lean
TauCeti.Manifold.OrientationCover.integral_map_proj_eq_zero.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M] [SigmaCompactSpace M]
  (c : TauCeti.compactlySupportedDeRhamCohomology I M (Module.finrank ℝ E)) :
  (TauCeti.compactlySupportedDeRhamCohomology.integral
        TauCeti.Manifold.OrientationCover.canonicalOrientation)
      ((TauCeti.compactlySupportedDeRhamCohomology.map TauCeti.VectorBundleOrientationCover.proj ⋯ ⋯
          (Module.finrank ℝ E))
        c) =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.OrientationCover.integral_map_proj_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/OrientationCover.html#TauCeti.Manifold.OrientationCover.integral_map_proj_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.OrientationCover.integral_map_proj_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/OrientationCover.html#TauCeti.Manifold.OrientationCover.integral_map_proj_eq_zero)
- [Source of `TauCeti.Manifold.OrientationCover.integral_map_proj_eq_zero` in TauCeti/Geometry/Manifold/DeRham/OrientationCover.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DeRham/OrientationCover.lean#L124)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
