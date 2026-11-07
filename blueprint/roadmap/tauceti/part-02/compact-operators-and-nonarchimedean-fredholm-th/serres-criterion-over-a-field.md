---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous
statement: formalized
proof: formalized
---

# Serre's criterion over a field

over a complete ultrametric nontrivially normed field `K`,
a continuous linear map between model spaces is row compact exactly when it is completely
continuous. Neither a discrete valuation nor spherical completeness is needed.

```lean
ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous.{u_1, u_2, u_4} {I : Type u_1}
  {J : Type u_2} [TopologicalSpace I] [DiscreteTopology I] [TopologicalSpace J] [DiscreteTopology J]
  [DecidableEq J] {K : Type u_4} [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K]
  {u : ZeroAtInftyContinuousMap J K →L[K] ZeroAtInftyContinuousMap I K} :
  u.IsRowCompact ↔ u.IsCompletelyContinuous
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.html#ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.html#ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous)
- [Source of `ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous` in TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.lean#L126)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
