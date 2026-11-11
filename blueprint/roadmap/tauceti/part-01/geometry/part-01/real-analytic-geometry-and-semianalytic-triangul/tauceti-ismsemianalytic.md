---
declaration: def
origin: cited
lean: TauCeti.IsMSemianalytic
statement: formalized
---

# TauCeti.IsMSemianalytic

A set on a manifold is semianalytic if it is semianalytic at every ambient point.

```lean
TauCeti.IsMSemianalytic.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {H : Type u_2} [TopologicalSpace H] {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  (I : ModelWithCorners ℝ E H) (s : Set M) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMSemianalytic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Manifold.html#TauCeti.IsMSemianalytic).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMSemianalytic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Manifold.html#TauCeti.IsMSemianalytic)
- [Source of `TauCeti.IsMSemianalytic` in TauCeti/Geometry/RealAnalytic/Semianalytic/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAnalytic/Semianalytic/Manifold.lean#L143)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
