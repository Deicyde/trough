---
declaration: theorem
origin: cited
lean: ContMDiff.restrictScalars
statement: formalized
proof: formalized
---

# ContMDiff.restrictScalars

A `C^n` map for boundaryless models over `𝕜'` is `C^n` for their scalar restrictions
to `𝕜`. For instance, a holomorphic map between complex manifolds is smooth.

```lean
ContMDiff.restrictScalars.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8} (𝕜 : Type u_1) {𝕜' : Type u_2}
  [NontriviallyNormedField 𝕜] [NontriviallyNormedField 𝕜'] [NormedAlgebra 𝕜 𝕜'] {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace 𝕜' E] [IsScalarTower 𝕜 𝕜' E] {E' : Type u_4}
  [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] [NormedSpace 𝕜' E'] [IsScalarTower 𝕜 𝕜' E']
  {H : Type u_5} {H' : Type u_6} [TopologicalSpace H] [TopologicalSpace H']
  {I : ModelWithCorners 𝕜' E H} {I' : ModelWithCorners 𝕜' E' H'} [I.Boundaryless] [I'.Boundaryless]
  {M : Type u_7} [TopologicalSpace M] [ChartedSpace H M] {N : Type u_8} [TopologicalSpace N]
  [ChartedSpace H' N] {n : WithTop ℕ∞} {f : M → N} (h : ContMDiff I I' n f) :
  ContMDiff (ModelWithCorners.restrictScalars 𝕜 I) (ModelWithCorners.restrictScalars 𝕜 I') n f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContMDiff.restrictScalars`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiff/RestrictScalars.html#ContMDiff.restrictScalars).

## Sources

- [Tau Ceti documentation: `ContMDiff.restrictScalars`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiff/RestrictScalars.html#ContMDiff.restrictScalars)
- [Source of `ContMDiff.restrictScalars` in TauCeti/Geometry/Manifold/ContMDiff/RestrictScalars.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/ContMDiff/RestrictScalars.lean#L71)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
