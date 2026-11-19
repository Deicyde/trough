---
declaration: theorem
origin: cited
lean: AnalyticOnNhd.zeroCount_le, AnalyticOnNhd.zeroCount_le_analyticOrderNatAt_add
statement: formalized
proof: formalized
---

# Jensen's bound for a zero count

Let `f` be analytic on `closedBall c R`, bounded by
`M ≥ 1` on `sphere c R` and nonzero at `c`. For `0 < r < R`, the number of zeros of `f` in any
`S ⊆ closedBall c r`, counted with multiplicity with respect to any domain `U`, is at most
`log (M / ‖f c‖) / log (R / r)`. This is Mathlib's `AnalyticOnNhd.sum_divisor_le`.

```lean
AnalyticOnNhd.zeroCount_le {c : ℂ} {r R M : ℝ} {f : ℂ → ℂ} {S : Set ℂ} (hr : 0 < r) (hrR : r < R)
  (hM : 1 ≤ M) (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R)) (hfc : f c ≠ 0)
  (hbound : ∀ z ∈ Metric.sphere c R, ‖f z‖ ≤ M) (U : Set ℂ) (hS : S ⊆ Metric.closedBall c r) :
  ↑(TauCeti.zeroCount f U S) ≤ Real.log (M / ‖f c‖) / Real.log (R / r)
```

## Depends on

- [TauCeti.zeroCount](tauceti-zerocount.md)

## Proof depends on

- [Jensen's bound at a zero of the centre](../../part-03/complex/part-02/jensens-bound-at-a-zero-of-the-centre.md)

## Lean

Formalized in Tau Ceti as [`AnalyticOnNhd.zeroCount_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Counting/Jensen.html#AnalyticOnNhd.zeroCount_le).

## Other forms

**Jensen's bound for a zero count, trailing-coefficient form.** Formalized in Tau Ceti as [`AnalyticOnNhd.zeroCount_le_analyticOrderNatAt_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Counting/Jensen.html#AnalyticOnNhd.zeroCount_le_analyticOrderNatAt_add).

```lean
AnalyticOnNhd.zeroCount_le_analyticOrderNatAt_add {c : ℂ} {r R M : ℝ} {f : ℂ → ℂ} {S : Set ℂ}
  (hr : 0 < r) (hrR : r < R) (hM : 1 ≤ M) (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R))
  (hfc : analyticOrderAt f c ≠ ⊤) (hbound : ∀ z ∈ Metric.sphere c R, ‖f z‖ ≤ M) (U : Set ℂ)
  (hS : S ⊆ Metric.closedBall c r) :
  ↑(TauCeti.zeroCount f U S) ≤
    ↑(analyticOrderNatAt f c) +
      (Real.log (M / ‖meromorphicTrailingCoeffAt f c‖) - ↑(analyticOrderNatAt f c) * Real.log R) /
        Real.log (R / r)
```

## Sources

- [Tau Ceti documentation: `AnalyticOnNhd.zeroCount_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Counting/Jensen.html#AnalyticOnNhd.zeroCount_le)
- [Source of `AnalyticOnNhd.zeroCount_le` in TauCeti/Analysis/Meromorphic/Counting/Jensen.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Meromorphic/Counting/Jensen.lean#L47)
