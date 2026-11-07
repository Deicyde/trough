---
declaration: def
origin: cited
lean: Homeomorph.pullbackDiffeomorph
statement: formalized
---

# Homeomorph.pullbackDiffeomorph

A homeomorphism onto a charted space is a `C^n` diffeomorphism for the pulled-back structure:
read in a pulled-back chart and in the corresponding chart of `M`, both it and its inverse are the
identity.

```lean
Homeomorph.pullbackDiffeomorph.{u_1, u_2, u_3, u_5, u_6} {H : Type u_1} [TopologicalSpace H]
  {M : Type u_2} [TopologicalSpace M] [ChartedSpace H M] {N : Type u_3} [TopologicalSpace N]
  {𝕜 : Type u_5} [NontriviallyNormedField 𝕜] {E : Type u_6} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  (I : ModelWithCorners 𝕜 E H) (n : WithTop ℕ∞) (e : N ≃ₜ M) : Diffeomorph I I N M n
```

## Depends on

- [Homeomorph.pullbackChartedSpace](homeomorph-pullbackchartedspace.md)

## Lean

Formalized in Tau Ceti as [`Homeomorph.pullbackDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/PullbackGroupoid.html#Homeomorph.pullbackDiffeomorph).

## Sources

- [Tau Ceti documentation: `Homeomorph.pullbackDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/PullbackGroupoid.html#Homeomorph.pullbackDiffeomorph)
- [Source of `Homeomorph.pullbackDiffeomorph` in TauCeti/Geometry/Manifold/PullbackGroupoid.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/PullbackGroupoid.lean#L192)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
