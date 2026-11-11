---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isClosed_range_precomp_iff, ContinuousLinearMap.range_precomp_eq_orthogonalBilin_ker, ContinuousLinearMap.isClosed_range_of_isClosed_range_precomp
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

## Proof depends on

- [Banach's lemma](../../../part-03/normed/part-01/banachs-lemma.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isClosed_range_precomp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Adjoint.html#ContinuousLinearMap.isClosed_range_precomp_iff).

## Other forms

**Closed-range theorem, range of the adjoint.** Formalized in Tau Ceti as [`ContinuousLinearMap.range_precomp_eq_orthogonalBilin_ker`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Adjoint.html#ContinuousLinearMap.range_precomp_eq_orthogonalBilin_ker).

```lean
ContinuousLinearMap.range_precomp_eq_orthogonalBilin_ker.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [IsRCLikeNormedField 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] (T : E →L[𝕜] F) (hT : IsClosed ↑(↑T).range) :
  (↑(ContinuousLinearMap.precomp 𝕜 T)).range =
    Submodule.orthogonalBilin (topDualPairing 𝕜 E).flip (↑T).ker
```

**Closed-range theorem, reverse implication.** Formalized in Tau Ceti as [`ContinuousLinearMap.isClosed_range_of_isClosed_range_precomp`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Adjoint.html#ContinuousLinearMap.isClosed_range_of_isClosed_range_precomp).

```lean
ContinuousLinearMap.isClosed_range_of_isClosed_range_precomp.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] [NormedAddCommGroup F] [NormedSpace 𝕜 F] (T : E →L[𝕜] F)
  (h : IsClosed ↑(↑(ContinuousLinearMap.precomp 𝕜 T)).range) : IsClosed ↑(↑T).range
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isClosed_range_precomp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Adjoint.html#ContinuousLinearMap.isClosed_range_precomp_iff)
- [Source of `ContinuousLinearMap.isClosed_range_precomp_iff` in TauCeti/Analysis/Normed/Module/Dual/Adjoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Dual/Adjoint.lean#L242)
