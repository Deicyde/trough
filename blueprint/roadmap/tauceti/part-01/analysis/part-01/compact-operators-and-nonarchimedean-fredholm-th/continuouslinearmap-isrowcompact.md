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
- [Source of `ContinuousLinearMap.IsRowCompact` in TauCeti/Analysis/Normed/Operator/RowCompact.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/RowCompact.lean#L121)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CompactOperators/STATUS.md)
