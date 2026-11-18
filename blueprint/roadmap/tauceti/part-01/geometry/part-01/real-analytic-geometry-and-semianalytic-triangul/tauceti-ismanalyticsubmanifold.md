---
declaration: def
origin: cited
lean: TauCeti.IsMAnalyticSubmanifold
statement: formalized
---

# TauCeti.IsMAnalyticSubmanifold

A subset `s` of a charted space `M` is a `d`-dimensional *analytic submanifold* with respect to
`I : ModelWithCorners 𝕜 E H` and `e : E ≃L[𝕜] Fin n → 𝕜` if `s` is nonempty and, around every
`x ∈ s`, the image of `s ∩ (extChartAt I x).source` under `e ∘ extChartAt I x` is a `d`-dimensional
analytic submanifold of `Fin n → 𝕜`.

```lean
TauCeti.IsMAnalyticSubmanifold.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M] {n : ℕ} (I : ModelWithCorners 𝕜 E H)
  (e : E ≃L[𝕜] Fin n → 𝕜) (d : ℕ) (s : Set M) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMAnalyticSubmanifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/AnalyticSubmanifold/Basic.html#TauCeti.IsMAnalyticSubmanifold).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMAnalyticSubmanifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/AnalyticSubmanifold/Basic.html#TauCeti.IsMAnalyticSubmanifold)
- [Source of `TauCeti.IsMAnalyticSubmanifold` in TauCeti/Geometry/Manifold/AnalyticSubmanifold/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/AnalyticSubmanifold/Basic.lean#L97)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
