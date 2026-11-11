---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.nuclearENorm_le_tsum_of_hasSum
statement: formalized
proof: formalized
---

# Fatou inequality for the trace-class gauge

For a series converging in operator norm,
the gauge of its sum is at most the sum of the gauges, even when that sum is infinite.

```lean
ContinuousLinearMap.nuclearENorm_le_tsum_of_hasSum.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [CompleteSpace E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] {ι : Type u_4}
  {T : ι → E →L[𝕜] F} {S : E →L[𝕜] F} (hT : HasSum T S) :
  S.nuclearENorm ≤ ∑' (i : ι), (T i).nuclearENorm
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ky Fan triangle inequality](ky-fan-triangle-inequality.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.nuclearENorm_le_tsum_of_hasSum`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Nuclear/Basic.html#ContinuousLinearMap.nuclearENorm_le_tsum_of_hasSum).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.nuclearENorm_le_tsum_of_hasSum`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Nuclear/Basic.html#ContinuousLinearMap.nuclearENorm_le_tsum_of_hasSum)
- [Source of `ContinuousLinearMap.nuclearENorm_le_tsum_of_hasSum` in TauCeti/Analysis/OperatorIdeal/Nuclear/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/OperatorIdeal/Nuclear/Basic.lean#L216)
