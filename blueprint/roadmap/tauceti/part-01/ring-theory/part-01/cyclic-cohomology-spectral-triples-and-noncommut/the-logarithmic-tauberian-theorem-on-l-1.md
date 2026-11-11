---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_kyFanLogMean_iff_tendsto_sub_one_mul_tsum_rpow
statement: formalized
proof: formalized
---

# The logarithmic Tauberian theorem on `L^(1,∞)`

For `T` in the logarithmic ideal, the
logarithmic means of `T` tend to `L` exactly when `(s - 1) ∑ⱼ aⱼ(T) ^ s` tends to `L` as `s ↓ 1`;
the series converges for every `s > 1`.

```lean
TauCeti.tendsto_kyFanLogMean_iff_tendsto_sub_one_mul_tsum_rpow.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [CompleteSpace E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F] {T : E →L[𝕜] F}
  (hT : T ∈ ((TauCeti.OperatorIdealFamily.logarithmic 𝕜).operatorGauge E F).finiteSubmodule)
  {L : ℝ} :
  Filter.Tendsto T.kyFanLogMean Filter.atTop (nhds L) ↔
    Filter.Tendsto (fun s => (s - 1) * ∑' (j : ℕ), ↑(T.singularValue j) ^ s)
      (nhdsWithin 1 (Set.Ioi 1)) (nhds L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ky Fan triangle inequality](../../../analysis/part-03/operator-ideal/ky-fan-triangle-inequality.md)
- [Ky Fan two-sided ideal inequality](../../../analysis/part-03/operator-ideal/ky-fan-two-sided-ideal-inequality.md)
- [The logarithmic Tauberian theorem](../../../analysis/part-03/specific-limits/the-logarithmic-tauberian-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_kyFanLogMean_iff_tendsto_sub_one_mul_tsum_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Basic.html#TauCeti.tendsto_kyFanLogMean_iff_tendsto_sub_one_mul_tsum_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_kyFanLogMean_iff_tendsto_sub_one_mul_tsum_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Basic.html#TauCeti.tendsto_kyFanLogMean_iff_tendsto_sub_one_mul_tsum_rpow)
- [Source of `TauCeti.tendsto_kyFanLogMean_iff_tendsto_sub_one_mul_tsum_rpow` in TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/OperatorIdeal/Family/DixmierTrace/Basic.lean#L311)
