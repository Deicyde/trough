---
declaration: def
origin: cited
lean: TauCeti.IsSemianalytic
statement: formalized
---

# TauCeti.IsSemianalytic

A set `s ⊆ E` is *semianalytic* if it is semianalytic at every point of `E`: near every point,
it agrees with a finite Boolean combination of zero sets and positivity sets of real analytic
functions defined near that point.

```lean
TauCeti.IsSemianalytic.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] (s : Set E) :
  Prop
```

## Depends on

- [TauCeti.SemianalyticAt](tauceti-semianalyticat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsSemianalytic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.IsSemianalytic).

## Sources

- [Tau Ceti documentation: `TauCeti.IsSemianalytic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.IsSemianalytic)
- [Source of `TauCeti.IsSemianalytic` in TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean#L430)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
