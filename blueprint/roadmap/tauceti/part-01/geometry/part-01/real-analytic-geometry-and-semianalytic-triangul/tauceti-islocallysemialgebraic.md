---
declaration: def
origin: cited
lean: TauCeti.IsLocallySemialgebraic
statement: formalized
---

# TauCeti.IsLocallySemialgebraic

A set `s ⊆ σ → ℝ` is *locally semialgebraic* if it is semialgebraic at every point of
`σ → ℝ`: every point, whether or not it lies in `s`, has an open semialgebraic neighbourhood `U`
such that `s ∩ U` is semialgebraic.

```lean
TauCeti.IsLocallySemialgebraic.{u_1} {σ : Type u_1} (s : Set (σ → ℝ)) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocallySemialgebraic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/Local.html#TauCeti.IsLocallySemialgebraic).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocallySemialgebraic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/Local.html#TauCeti.IsLocallySemialgebraic)
- [Source of `TauCeti.IsLocallySemialgebraic` in TauCeti/Geometry/RealAlgebraic/Semialgebraic/Local.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Semialgebraic/Local.lean#L249)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
