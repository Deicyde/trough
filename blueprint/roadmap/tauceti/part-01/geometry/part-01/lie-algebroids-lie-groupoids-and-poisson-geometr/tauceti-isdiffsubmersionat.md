---
declaration: def
origin: cited
lean: TauCeti.IsDiffSubmersionAt
statement: formalized
---

# TauCeti.IsDiffSubmersionAt

A map is a differential submersion at a point if its manifold derivative admits a continuous
linear right inverse. Unlike the chart normal form, this predicate does not require smoothness.

```lean
TauCeti.IsDiffSubmersionAt.{u_1, u_2, u_3, u_5, u_6, u_8, u_9} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} {H : Type u_5} {G : Type u_6} {M : Type u_8} {N : Type u_9}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [TopologicalSpace H] [TopologicalSpace G] [TopologicalSpace M]
  [ChartedSpace H M] [TopologicalSpace N] [ChartedSpace G N] (I : ModelWithCorners 𝕜 E H)
  (J : ModelWithCorners 𝕜 F G) (f : M → N) (x : M) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDiffSubmersionAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Submersion/Split.html#TauCeti.IsDiffSubmersionAt).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDiffSubmersionAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Submersion/Split.html#TauCeti.IsDiffSubmersionAt)
- [Source of `TauCeti.IsDiffSubmersionAt` in TauCeti/Geometry/Manifold/Submersion/Split.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Submersion/Split.lean#L57)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
