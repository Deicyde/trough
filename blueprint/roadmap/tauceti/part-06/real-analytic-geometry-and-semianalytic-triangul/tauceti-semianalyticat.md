---
declaration: def
origin: cited
lean: TauCeti.SemianalyticAt
statement: formalized
---

# TauCeti.SemianalyticAt

A set `s ⊆ E` is *semianalytic at* `x` if on some neighbourhood `U` of `x` it agrees with a
finite Boolean combination of zero sets and positivity sets of real functions analytic on `U`.

```lean
TauCeti.SemianalyticAt.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] (s : Set E)
  (x : E) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SemianalyticAt`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.SemianalyticAt).

## Sources

- [Tau Ceti documentation: `TauCeti.SemianalyticAt`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.SemianalyticAt)
- [Source of `TauCeti.SemianalyticAt` in TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean#L240)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
