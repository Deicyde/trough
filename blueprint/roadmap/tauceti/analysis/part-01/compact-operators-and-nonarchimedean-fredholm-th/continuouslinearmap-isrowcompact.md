---
declaration: def
origin: cited
lean: ContinuousLinearMap.IsRowCompact
statement: formalized
---

# ContinuousLinearMap.IsRowCompact

A continuous linear map between model spaces is **row compact** if the entries of its matrix
are uniformly bounded and its row norms tend to zero along the cofinite filter of output indices.
The bound is automatic over Tate scalars (`ContinuousLinearMap.isRowCompact_iff_tendsto_rowNorm`);
it is part of the definition so that the real suprema defining the row norms are meaningful.

```lean
ContinuousLinearMap.IsRowCompact.{u_1, u_2, u_5} {I : Type u_1} {J : Type u_2} {R : Type u_5}
  [TopologicalSpace I] [TopologicalSpace J] [DiscreteTopology J] [DecidableEq J] [SeminormedRing R]
  (u : ZeroAtInftyContinuousMap J R →L[R] ZeroAtInftyContinuousMap I R) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact.html#ContinuousLinearMap.IsRowCompact).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact.html#ContinuousLinearMap.IsRowCompact)
- [Source of `ContinuousLinearMap.IsRowCompact` in TauCeti/Analysis/Normed/Operator/RowCompact.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/RowCompact.lean#L115)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
