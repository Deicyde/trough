---
declaration: theorem
origin: cited
lean: TauCeti.isDiffSubmersionAt_iff_isRegularPoint
statement: formalized
proof: formalized
---

# TauCeti.isDiffSubmersionAt_iff_isRegularPoint

For finite-dimensional targets, splitting the derivative is equivalent to being a regular
point. No differentiability or finite-dimensionality of the source is needed.

```lean
TauCeti.isDiffSubmersionAt_iff_isRegularPoint.{u_1, u_2, u_3, u_5, u_6, u_8, u_9} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} {H : Type u_5} {G : Type u_6} {M : Type u_8} {N : Type u_9}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [TopologicalSpace H] [TopologicalSpace G] {I : ModelWithCorners 𝕜 E H}
  {J : ModelWithCorners 𝕜 F G} [TopologicalSpace M] [ChartedSpace H M] [TopologicalSpace N]
  [ChartedSpace G N] {f : M → N} {x : M} [CompleteSpace 𝕜] [FiniteDimensional 𝕜 F] :
  TauCeti.IsDiffSubmersionAt I J f x ↔ TauCeti.IsRegularPoint I J f x
```

## Depends on

- [TauCeti.IsDiffSubmersionAt](tauceti-isdiffsubmersionat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isDiffSubmersionAt_iff_isRegularPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Submersion/Split.html#TauCeti.isDiffSubmersionAt_iff_isRegularPoint).

## Sources

- [Tau Ceti documentation: `TauCeti.isDiffSubmersionAt_iff_isRegularPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Submersion/Split.html#TauCeti.isDiffSubmersionAt_iff_isRegularPoint)
- [Source of `TauCeti.isDiffSubmersionAt_iff_isRegularPoint` in TauCeti/Geometry/Manifold/Submersion/Split.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Submersion/Split.lean#L83)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
