---
declaration: theorem
origin: cited
lean: AnalyticOnNhd.le_circleAverage_log_norm
statement: formalized
proof: formalized
---

# Jensen's inequality from below

If `f` is analytic on the closed disc of radius `|r|`
about `c`, with `r ≠ 0`, the circle average of `log ‖f‖` is at least `k * log r + log ‖τ‖`, where
`k` is the order of `f` at `c` and `τ` its trailing coefficient there.

This is Jensen's formula `MeromorphicOn.circleAverage_log_norm` with the contributions of the zeros
other than `c` dropped, each of which is nonnegative.

```lean
AnalyticOnNhd.le_circleAverage_log_norm {f : ℂ → ℂ} {c : ℂ} {r : ℝ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall c |r|)) (hr : r ≠ 0) :
  ↑(analyticOrderNatAt f c) * Real.log r + Real.log ‖meromorphicTrailingCoeffAt f c‖ ≤
    Real.circleAverage (fun z => Real.log ‖f z‖) c r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticOnNhd.le_circleAverage_log_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RadialUniqueness.html#AnalyticOnNhd.le_circleAverage_log_norm).

## Sources

- [Tau Ceti documentation: `AnalyticOnNhd.le_circleAverage_log_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RadialUniqueness.html#AnalyticOnNhd.le_circleAverage_log_norm)
- [Source of `AnalyticOnNhd.le_circleAverage_log_norm` in TauCeti/Analysis/Complex/RadialUniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/RadialUniqueness.lean#L74)
