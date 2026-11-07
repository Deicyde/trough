---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.projective_range_of_isIdempotentElem
statement: formalized
proof: formalized
---

# A row-compact idempotent has projective range

```lean
ContinuousLinearMap.IsRowCompact.projective_range_of_isIdempotentElem.{u_1, u_2} {I : Type u_1}
  {R : Type u_2} [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] [NormedRing R]
  [IsUltrametricDist R] [TauCeti.NormedRing.IsTate R] [CompleteSpace R]
  {e : ZeroAtInftyContinuousMap I R →L[R] ZeroAtInftyContinuousMap I R} (hu : e.IsRowCompact)
  (he : IsIdempotentElem e) : Module.Projective R ↥(↑e).range
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.projective_range_of_isIdempotentElem`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/Idempotent.html#ContinuousLinearMap.IsRowCompact.projective_range_of_isIdempotentElem).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.projective_range_of_isIdempotentElem`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/Idempotent.html#ContinuousLinearMap.IsRowCompact.projective_range_of_isIdempotentElem)
- [Source of `ContinuousLinearMap.IsRowCompact.projective_range_of_isIdempotentElem` in TauCeti/Analysis/Normed/Operator/RowCompact/Idempotent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/RowCompact/Idempotent.lean#L101)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
