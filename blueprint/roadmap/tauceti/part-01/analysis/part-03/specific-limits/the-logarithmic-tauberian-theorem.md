---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_sub_one_mul_tsum_rpow_iff_tendsto_sum_div_log
statement: formalized
proof: formalized
---

# The logarithmic Tauberian theorem

For an antitone nonnegative sequence `μ` whose zeta
function `∑ⱼ μⱼ ^ s` converges for every `s > 1`, the residue `lim_(s ↓ 1) (s - 1) ∑ⱼ μⱼ ^ s`
equals `L` exactly when the logarithmic means `(log (N + 2))⁻¹ ∑_(j ≤ N) μⱼ` tend to `L`.

```lean
TauCeti.tendsto_sub_one_mul_tsum_rpow_iff_tendsto_sum_div_log {μ : ℕ → ℝ} (hμ0 : ∀ (j : ℕ), 0 ≤ μ j)
  (hμ : Antitone μ) (hsum : ∀ (s : ℝ), 1 < s → Summable fun j => μ j ^ s) {L : ℝ} :
  Filter.Tendsto (fun s => (s - 1) * ∑' (j : ℕ), μ j ^ s) (nhdsWithin 1 (Set.Ioi 1)) (nhds L) ↔
    Filter.Tendsto (fun N => (∑ j ∈ Finset.range (N + 1), μ j) / Real.log (↑N + 2)) Filter.atTop
      (nhds L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_sub_one_mul_tsum_rpow_iff_tendsto_sum_div_log`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecificLimits/LogarithmicTauberian.html#TauCeti.tendsto_sub_one_mul_tsum_rpow_iff_tendsto_sum_div_log).

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_sub_one_mul_tsum_rpow_iff_tendsto_sum_div_log`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecificLimits/LogarithmicTauberian.html#TauCeti.tendsto_sub_one_mul_tsum_rpow_iff_tendsto_sum_div_log)
- [Source of `TauCeti.tendsto_sub_one_mul_tsum_rpow_iff_tendsto_sum_div_log` in TauCeti/Analysis/SpecificLimits/LogarithmicTauberian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecificLimits/LogarithmicTauberian.lean#L865)
