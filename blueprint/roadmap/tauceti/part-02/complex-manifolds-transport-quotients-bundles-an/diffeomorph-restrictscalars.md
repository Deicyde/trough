---
declaration: def
origin: cited
lean: Diffeomorph.restrictScalars
statement: formalized
---

# Diffeomorph.restrictScalars

A `C^n` diffeomorphism for boundaryless models over `𝕜'` is a `C^n` diffeomorphism for
their scalar restrictions to `𝕜`, with the same underlying equivalence. For instance, a
biholomorphism between complex manifolds is a diffeomorphism of the underlying real manifolds.

```lean
Diffeomorph.restrictScalars.{u_1, u_2, u_3, u_4, u_6, u_7, u_9, u_10} (𝕜 : Type u_1) {𝕜' : Type u_2}
  [NontriviallyNormedField 𝕜] [NontriviallyNormedField 𝕜'] [NormedAlgebra 𝕜 𝕜'] {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace 𝕜' E] [IsScalarTower 𝕜 𝕜' E] {E' : Type u_4}
  [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] [NormedSpace 𝕜' E'] [IsScalarTower 𝕜 𝕜' E']
  {H : Type u_6} {H' : Type u_7} [TopologicalSpace H] [TopologicalSpace H']
  {I : ModelWithCorners 𝕜' E H} {I' : ModelWithCorners 𝕜' E' H'} [I.Boundaryless] [I'.Boundaryless]
  {M : Type u_9} [TopologicalSpace M] [ChartedSpace H M] {N : Type u_10} [TopologicalSpace N]
  [ChartedSpace H' N] {n : WithTop ℕ∞} (Φ : Diffeomorph I I' M N n) :
  Diffeomorph (ModelWithCorners.restrictScalars 𝕜 I) (ModelWithCorners.restrictScalars 𝕜 I') M N n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ContMDiff.restrictScalars](contmdiff-restrictscalars.md)

## Lean

Formalized in Tau Ceti as [`Diffeomorph.restrictScalars`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Diffeomorph/RestrictScalars.html#Diffeomorph.restrictScalars).

## Sources

- [Tau Ceti documentation: `Diffeomorph.restrictScalars`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Diffeomorph/RestrictScalars.html#Diffeomorph.restrictScalars)
- [Source of `Diffeomorph.restrictScalars` in TauCeti/Geometry/Manifold/Diffeomorph/RestrictScalars.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Diffeomorph/RestrictScalars.lean#L57)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
