---
declaration: theorem
origin: cited
lean: AnalyticOnNhd.sum_divisor_le_log_div_log
statement: formalized
proof: formalized
---

# Jensen's count with a relative bound

Let `f` be analytic on `closedBall z₀ R` with
`0 < r < R`, `f z₀ ≠ 0` and `‖f w‖ ≤ M ‖f z₀‖` on `sphere z₀ R`. Then the number of zeros of `f`
in `closedBall z₀ r`, counted with multiplicity, is at most `log M / log (R / r)`.

```lean
AnalyticOnNhd.sum_divisor_le_log_div_log {r R : ℝ} {f : ℂ → ℂ} {z₀ : ℂ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall z₀ R)) (hr : 0 < r) (hrR : r < R) (hz₀ : f z₀ ≠ 0)
  {M : ℝ} (hM : ∀ w ∈ Metric.sphere z₀ R, ‖f w‖ ≤ M * ‖f z₀‖) :
  ↑(∑ᶠ (u : ℂ), (MeromorphicOn.divisor f (Metric.closedBall z₀ r)) u) ≤
    Real.log M / Real.log (R / r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticOnNhd.sum_divisor_le_log_div_log`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/JensenFormula.html#AnalyticOnNhd.sum_divisor_le_log_div_log).

## Sources

- [Tau Ceti documentation: `AnalyticOnNhd.sum_divisor_le_log_div_log`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/JensenFormula.html#AnalyticOnNhd.sum_divisor_le_log_div_log)
- [Source of `AnalyticOnNhd.sum_divisor_le_log_div_log` in TauCeti/Analysis/Complex/JensenFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/JensenFormula.lean#L174)
