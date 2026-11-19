---
declaration: theorem
origin: cited
lean: MeromorphicOn.circleAverage_log_norm_eq_discCounting_inv_sub_add
statement: formalized
proof: formalized
---

# Disc-local Jensen identity (Calegari–Dimitrov–Tang, §6.1, eq. (6.1.4))

for `f : ℂ → ℂ`
meromorphic on `closedBall 0 r` and `0 < r`,
`circleAverage (log ‖f ·‖) 0 r = discCounting f⁻¹ r - discCounting f r + log ‖c(f, 0)‖`,
where `c(f, 0) = meromorphicTrailingCoeffAt f 0` is the leading Laurent coefficient at `0`. Note
that when `meromorphicOrderAt f 0 = ⊤` (`f = 0` away from a discrete set), all four terms vanish by
totalization (`Real.log 0 = 0`).

```lean
MeromorphicOn.circleAverage_log_norm_eq_discCounting_inv_sub_add {f : ℂ → ℂ} {r : ℝ}
  (hf : MeromorphicOn f (Metric.closedBall 0 r)) (hr : 0 < r) :
  Real.circleAverage (fun z => Real.log ‖f z‖) 0 r =
    TauCeti.discCounting f⁻¹ r - TauCeti.discCounting f r +
      Real.log ‖meromorphicTrailingCoeffAt f 0‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeromorphicOn.circleAverage_log_norm_eq_discCounting_inv_sub_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ValueDistribution/Disc/Counting.html#MeromorphicOn.circleAverage_log_norm_eq_discCounting_inv_sub_add).

## Sources

- [Tau Ceti documentation: `MeromorphicOn.circleAverage_log_norm_eq_discCounting_inv_sub_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ValueDistribution/Disc/Counting.html#MeromorphicOn.circleAverage_log_norm_eq_discCounting_inv_sub_add)
- [Source of `MeromorphicOn.circleAverage_log_norm_eq_discCounting_inv_sub_add` in TauCeti/Analysis/Complex/ValueDistribution/Disc/Counting.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/ValueDistribution/Disc/Counting.lean#L570)
