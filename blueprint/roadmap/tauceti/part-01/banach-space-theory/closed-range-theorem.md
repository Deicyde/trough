---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isClosed_range_precomp_iff
statement: formalized
proof: formalized
---

# Closed-range theorem

A bounded operator between Banach spaces has closed range if and
only if its adjoint has closed range.

```lean
ContinuousLinearMap.isClosed_range_precomp_iff.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F] (T : E →L[𝕜] F) :
  IsClosed ↑(↑(ContinuousLinearMap.precomp 𝕜 T)).range ↔ IsClosed ↑(↑T).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isClosed_range_precomp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Adjoint.html#ContinuousLinearMap.isClosed_range_precomp_iff).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isClosed_range_precomp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Adjoint.html#ContinuousLinearMap.isClosed_range_precomp_iff)
- [Source of `ContinuousLinearMap.isClosed_range_precomp_iff` in TauCeti/Analysis/Normed/Module/Dual/Adjoint.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Dual/Adjoint.lean#L234)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
