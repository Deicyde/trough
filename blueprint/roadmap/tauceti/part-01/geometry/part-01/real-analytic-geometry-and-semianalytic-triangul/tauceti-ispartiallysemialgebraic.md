---
declaration: def
origin: cited
lean: TauCeti.IsPartiallySemialgebraic
statement: formalized
---

# TauCeti.IsPartiallySemialgebraic

A set `s ⊆ E × (ι → ℝ)` is *partially semialgebraic* if it is partially semialgebraic over
every base point: over a neighbourhood `U` of every point of `E`, it agrees with a finite Boolean
combination of zero sets and positivity sets of polynomials in the fibre coordinates with
coefficients analytic on `U`.

```lean
TauCeti.IsPartiallySemialgebraic.{u_1, u_3} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {ι : Type u_3} (s : Set (E × (ι → ℝ))) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsPartiallySemialgebraic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic.html#TauCeti.IsPartiallySemialgebraic).

## Sources

- [Tau Ceti documentation: `TauCeti.IsPartiallySemialgebraic`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic.html#TauCeti.IsPartiallySemialgebraic)
- [Source of `TauCeti.IsPartiallySemialgebraic` in TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic.lean#L627)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
