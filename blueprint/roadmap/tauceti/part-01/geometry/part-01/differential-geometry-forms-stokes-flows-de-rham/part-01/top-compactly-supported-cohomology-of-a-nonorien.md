---
declaration: theorem
origin: cited
lean: TauCeti.subsingleton_compactlySupportedDeRhamCohomology_of_not_orientable
statement: formalized
proof: formalized
---

# Top compactly supported cohomology of a nonorientable manifold

On a preconnected,
nonorientable, boundaryless, Hausdorff, σ-compact finite-dimensional smooth manifold `M` of
dimension `n`, the top compactly supported de Rham cohomology `H^n_c(M)` vanishes.

```lean
TauCeti.subsingleton_compactlySupportedDeRhamCohomology_of_not_orientable.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M]
  [SigmaCompactSpace M] [PreconnectedSpace M] (h : ¬TauCeti.Orientable I M) :
  Subsingleton (TauCeti.compactlySupportedDeRhamCohomology I M (Module.finrank ℝ E))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The compactly supported Poincaré lemma on the line](../../../part-02/manifold/part-01/the-compactly-supported-poincare-lemma-on-the-li.md)
- [The Poincaré lemma on manifolds](../../../part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.subsingleton_compactlySupportedDeRhamCohomology_of_not_orientable`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/OrientationCover.html#TauCeti.subsingleton_compactlySupportedDeRhamCohomology_of_not_orientable).

## Sources

- [Tau Ceti documentation: `TauCeti.subsingleton_compactlySupportedDeRhamCohomology_of_not_orientable`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/OrientationCover.html#TauCeti.subsingleton_compactlySupportedDeRhamCohomology_of_not_orientable)
- [Source of `TauCeti.subsingleton_compactlySupportedDeRhamCohomology_of_not_orientable` in TauCeti/Geometry/Manifold/DeRham/OrientationCover.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DeRham/OrientationCover.lean#L158)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
