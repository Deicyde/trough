---
declaration: theorem
origin: cited
lean: AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_le_of_two_mul_le, AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_half_le
statement: formalized
proof: formalized
---

# Landau's local logarithmic-derivative lemma

Let `f` be analytic on `closedBall z₀ R`
with `‖f w‖ ≤ M ‖f z₀‖` on `sphere z₀ R`, and let `2 r ≤ R`. At every `z` with
`‖z - z₀‖ < r` and `f z ≠ 0`, the logarithmic derivative of `f` differs from `∑ m_ρ / (z - ρ)`
over the zeros `ρ` in `closedBall z₀ r`, with multiplicities `m_ρ` given by the divisor, by at
most `4 (r + ‖z - z₀‖) / (r - ‖z - z₀‖) ^ 2 * log M`.

```lean
AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_le_of_two_mul_le {f : ℂ → ℂ} {z₀ : ℂ} {r R : ℝ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall z₀ R)) (hrR : 2 * r ≤ R) {M : ℝ}
  (hM : ∀ w ∈ Metric.sphere z₀ R, ‖f w‖ ≤ M * ‖f z₀‖) {z : ℂ} (hz : ‖z - z₀‖ < r) (hfz : f z ≠ 0) :
  ‖logDeriv f z - ∑ᶠ (ρ : ℂ), ↑((MeromorphicOn.divisor f (Metric.closedBall z₀ r)) ρ) / (z - ρ)‖ ≤
    4 * (r + ‖z - z₀‖) / (r - ‖z - z₀‖) ^ 2 * Real.log M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_le_of_two_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LocalLogDeriv.html#AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_le_of_two_mul_le).

## Other forms

**Landau's local logarithmic-derivative lemma in the classical normalization.** Formalized in Tau Ceti as [`AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_half_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LocalLogDeriv.html#AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_half_le).

```lean
AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_half_le {f : ℂ → ℂ} {z₀ : ℂ} {R : ℝ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall z₀ R)) (hR : 0 < R) {M : ℝ}
  (hM : ∀ w ∈ Metric.sphere z₀ R, ‖f w‖ ≤ M * ‖f z₀‖) {z : ℂ} (hz : ‖z - z₀‖ ≤ R / 4)
  (hfz : f z ≠ 0) :
  ‖logDeriv f z -
        ∑ᶠ (ρ : ℂ), ↑((MeromorphicOn.divisor f (Metric.closedBall z₀ (R / 2))) ρ) / (z - ρ)‖ ≤
    48 / R * Real.log M
```

## Sources

- [Tau Ceti documentation: `AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_le_of_two_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LocalLogDeriv.html#AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_le_of_two_mul_le)
- [Source of `AnalyticOnNhd.norm_logDeriv_sub_finsum_divisor_le_of_two_mul_le` in TauCeti/Analysis/Complex/LocalLogDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/LocalLogDeriv.lean#L274)
