---
declaration: theorem
origin: cited
lean: TauCeti.Contour.circleIntegral_eq_zero_of_meromorphicOrderAt_nonneg
statement: formalized
proof: formalized
---

# Cauchy–Goursat for a pole-free meromorphic function

If `A` is meromorphic on the closed
disc `closedBall c R` (`R ≥ 0`) and has non-negative meromorphic order at every point of the disc,
then `∮ z in C(c, R), A z = 0`.

```lean
TauCeti.Contour.circleIntegral_eq_zero_of_meromorphicOrderAt_nonneg.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {A : ℂ → E} {c : ℂ} {R : ℝ} (hR : 0 ≤ R)
  (hA : MeromorphicOn A (Metric.closedBall c R))
  (hord : ∀ z ∈ Metric.closedBall c R, 0 ≤ meromorphicOrderAt A z) : circleIntegral A c R = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.circleIntegral_eq_zero_of_meromorphicOrderAt_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/Goursat.html#TauCeti.Contour.circleIntegral_eq_zero_of_meromorphicOrderAt_nonneg).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.circleIntegral_eq_zero_of_meromorphicOrderAt_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/Goursat.html#TauCeti.Contour.circleIntegral_eq_zero_of_meromorphicOrderAt_nonneg)
- [Source of `TauCeti.Contour.circleIntegral_eq_zero_of_meromorphicOrderAt_nonneg` in TauCeti/Analysis/Contour/Cauchy/Goursat.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/Cauchy/Goursat.lean#L43)
