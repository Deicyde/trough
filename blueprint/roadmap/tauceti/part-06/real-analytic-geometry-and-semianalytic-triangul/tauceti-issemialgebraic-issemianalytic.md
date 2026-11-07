---
declaration: theorem
origin: cited
lean: TauCeti.IsSemialgebraic.isSemianalytic
statement: formalized
proof: formalized
---

# TauCeti.IsSemialgebraic.isSemianalytic

A semialgebraic subset of `σ → ℝ`, for a finite type `σ`, is semianalytic: polynomial
functions are analytic.

```lean
TauCeti.IsSemialgebraic.isSemianalytic.{u_3} {σ : Type u_3} [Fintype σ] {s : Set (σ → ℝ)}
  (hs : TauCeti.IsSemialgebraic s) : TauCeti.IsSemianalytic s
```

## Depends on

- [TauCeti.IsSemianalytic](tauceti-issemianalytic.md)

## Proof depends on

- [TauCeti.SemianalyticAt](tauceti-semianalyticat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsSemialgebraic.isSemianalytic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.IsSemialgebraic.isSemianalytic).

## Sources

- [Tau Ceti documentation: `TauCeti.IsSemialgebraic.isSemianalytic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.IsSemialgebraic.isSemianalytic)
- [Source of `TauCeti.IsSemialgebraic.isSemianalytic` in TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean#L570)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
