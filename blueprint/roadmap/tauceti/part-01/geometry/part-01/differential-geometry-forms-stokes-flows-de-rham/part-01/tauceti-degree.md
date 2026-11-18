---
declaration: def
origin: cited
lean: TauCeti.degree
statement: formalized
---

# TauCeti.degree

The *mapping degree* of `f : M → N` with respect to orientations `o` of `M` and `o'` of `N`:
the signed count `degreeAtRegularValue o o' f y` of the fibre over a regular value `y`, chosen
arbitrarily, and `0` if `f` has no regular value. For a proper smooth map from a Hausdorff
boundaryless manifold to a connected σ-compact Hausdorff boundaryless manifold of the same
dimension the choice does not matter (`TauCeti.degree_eq_degreeAtRegularValue`).

```lean
TauCeti.degree.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]
  {E' : Type u_4} {H' : Type u_5} {N : Type u_6} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [FiniteDimensional ℝ E'] [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'} [TopologicalSpace N]
  [ChartedSpace H' N] [IsManifold J 1 N] {ι : Type u_7} [Fintype ι]
  (o : TauCeti.Manifold.Orientation I M ι) (o' : TauCeti.Manifold.Orientation J N ι) (f : M → N) : ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.degree`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/Basic.html#TauCeti.degree).

## Sources

- [Tau Ceti documentation: `TauCeti.degree`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/Basic.html#TauCeti.degree)
- [Source of `TauCeti.degree` in TauCeti/Geometry/Manifold/Degree/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Degree/Basic.lean#L193)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
