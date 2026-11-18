---
declaration: theorem
origin: cited
lean: TauCeti.integral_ball_conjWirtingerDeriv_eq_circleIntegral
statement: formalized
proof: formalized
---

# Stokes' formula for `\bar∂` on a disc

For `h` real `C¹` near the closed disc
`|z - c| ≤ r`, `∫_{|z - c| < r} \bar∂h dA = (2 i)⁻¹ ∮_{|z - c| = r} h dz`.

```lean
TauCeti.integral_ball_conjWirtingerDeriv_eq_circleIntegral.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {h : ℂ → E} {c : ℂ} {r : ℝ} (hr : 0 ≤ r)
  (hh : ∀ z ∈ Metric.closedBall c r, ContDiffAt ℝ 1 h z) :
  ∫ (z : ℂ) in Metric.ball c r, (TauCeti.conjWirtingerDeriv h z) 1 =
    (2 * Complex.I)⁻¹ • ∮ (z : ℂ) in C(c, r), h z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_ball_conjWirtingerDeriv_eq_circleIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Green.html#TauCeti.integral_ball_conjWirtingerDeriv_eq_circleIntegral).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_ball_conjWirtingerDeriv_eq_circleIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Green.html#TauCeti.integral_ball_conjWirtingerDeriv_eq_circleIntegral)
- [Source of `TauCeti.integral_ball_conjWirtingerDeriv_eq_circleIntegral` in TauCeti/Analysis/Complex/Wirtinger/Green.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Wirtinger/Green.lean#L88)
