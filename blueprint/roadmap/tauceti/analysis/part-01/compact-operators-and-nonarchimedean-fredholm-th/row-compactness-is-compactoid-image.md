---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isRowCompact_iff_hasCompactoidImage
statement: formalized
proof: formalized
---

# Row compactness is compactoid image

over an ultrametric nontrivially normed field, a map
between model spaces is row compact exactly when it maps the closed unit ball to a compactoid
set.

```lean
ContinuousLinearMap.isRowCompact_iff_hasCompactoidImage.{u_1, u_2, u_3} {I : Type u_1}
  {J : Type u_2} {K : Type u_3} [TopologicalSpace I] [DiscreteTopology I] [TopologicalSpace J]
  [DiscreteTopology J] [DecidableEq J] [NontriviallyNormedField K] [IsUltrametricDist K]
  {u : ZeroAtInftyContinuousMap J K →L[K] ZeroAtInftyContinuousMap I K} :
  u.IsRowCompact ↔ u.HasCompactoidImage
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isRowCompact_iff_hasCompactoidImage`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/Compactoid.html#ContinuousLinearMap.isRowCompact_iff_hasCompactoidImage).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isRowCompact_iff_hasCompactoidImage`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/Compactoid.html#ContinuousLinearMap.isRowCompact_iff_hasCompactoidImage)
- [Source of `ContinuousLinearMap.isRowCompact_iff_hasCompactoidImage` in TauCeti/Analysis/Normed/Operator/RowCompact/Compactoid.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/RowCompact/Compactoid.lean#L91)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
