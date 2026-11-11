---
declaration: theorem
origin: cited
lean: TauCeti.submersion_iff_split_mfderiv
statement: formalized
proof: formalized
---

# TauCeti.submersion_iff_split_mfderiv

A smooth map between finite-dimensional real or complex manifolds with boundaryless source is a
submersion exactly when every differential has a continuous linear right inverse.

```lean
TauCeti.submersion_iff_split_mfderiv.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} {G : Type u_4} {H : Type u_5} {M : Type u_6} {N : Type u_7}
  [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [FiniteDimensional 𝕜 F] [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H}
  [I.Boundaryless] [TopologicalSpace G] {J : ModelWithCorners 𝕜 F G} [TopologicalSpace M]
  [ChartedSpace H M] [TopologicalSpace N] [ChartedSpace G N] {n : WithTop ℕ∞} [IsManifold I n M]
  [IsManifold J n N] {f : M → N} (hf : ContMDiff I J n f) (hn : 1 ≤ n) :
  Manifold.IsSubmersion I J n f ↔ ∀ (x : M), TauCeti.IsDiffSubmersionAt I J f x
```

## Depends on

- [TauCeti.IsDiffSubmersionAt](tauceti-isdiffsubmersionat.md)

## Proof depends on

- [The inverse function theorem for manifolds](../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [TauCeti.isDiffSubmersionAt_iff_isRegularPoint](tauceti-isdiffsubmersionat-iff-isregularpoint.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.submersion_iff_split_mfderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Submersion/Split.html#TauCeti.submersion_iff_split_mfderiv).

## Sources

- [Tau Ceti documentation: `TauCeti.submersion_iff_split_mfderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Submersion/Split.html#TauCeti.submersion_iff_split_mfderiv)
- [Source of `TauCeti.submersion_iff_split_mfderiv` in TauCeti/Geometry/Manifold/Submersion/Split.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Submersion/Split.lean#L244)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
