---
declaration: theorem
origin: cited
lean: AnalyticOnNhd.sum_divisor_le_analyticOrderNatAt_add
statement: formalized
proof: formalized
---

# Jensen's bound at a zero of the centre

Let `f` be analytic on `closedBall c R`, bounded
by `M ≥ 1` on `sphere c R`, and of finite order `m` at `c` with trailing coefficient `a`. Then for
`0 < r < R` the number of zeros of `f` in `closedBall c r`, counted with multiplicity, is at most
`m + (log (M / ‖a‖) - m log R) / log (R / r)`.

This follows from Jensen's formula `MeromorphicOn.circleAverage_log_norm`, in which the centre
contributes `m log R + log ‖a‖` and every other zero of the smaller disc at least
`log (R / r)`.

```lean
AnalyticOnNhd.sum_divisor_le_analyticOrderNatAt_add {c : ℂ} {r R : ℝ} {f : ℂ → ℂ} {M : ℝ}
  (hr : 0 < r) (hrR : r < R) (hM : 1 ≤ M) (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R))
  (hfc : analyticOrderAt f c ≠ ⊤) (hbound : ∀ z ∈ Metric.sphere c R, ‖f z‖ ≤ M) :
  ↑(∑ᶠ (u : ℂ), (MeromorphicOn.divisor f (Metric.closedBall c r)) u) ≤
    ↑(analyticOrderNatAt f c) +
      (Real.log (M / ‖meromorphicTrailingCoeffAt f c‖) - ↑(analyticOrderNatAt f c) * Real.log R) /
        Real.log (R / r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticOnNhd.sum_divisor_le_analyticOrderNatAt_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/JensenFormula.html#AnalyticOnNhd.sum_divisor_le_analyticOrderNatAt_add).

## Sources

- [Tau Ceti documentation: `AnalyticOnNhd.sum_divisor_le_analyticOrderNatAt_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/JensenFormula.html#AnalyticOnNhd.sum_divisor_le_analyticOrderNatAt_add)
- [Source of `AnalyticOnNhd.sum_divisor_le_analyticOrderNatAt_add` in TauCeti/Analysis/Complex/JensenFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/JensenFormula.lean#L108)
