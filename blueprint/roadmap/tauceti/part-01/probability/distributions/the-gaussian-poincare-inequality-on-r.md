---
declaration: theorem
origin: cited
lean: TauCeti.Probability.variance_le_integral_deriv_sq_gaussianReal
statement: formalized
proof: formalized
---

# The Gaussian Poincaré inequality on `ℝ`

For a continuously differentiable function `f`
with bounded values and bounded derivative, the variance of `f` under the standard Gaussian law is
at most the expectation of `(f')²`. In the unrestricted classical inequality, the identity
function shows that the constant `1` is optimal; it does not satisfy the boundedness hypothesis
of this theorem.

```lean
TauCeti.Probability.variance_le_integral_deriv_sq_gaussianReal {f : ℝ → ℝ} (hf : ContDiff ℝ 1 f)
  (hfb : ∃ A, ∀ (x : ℝ), |f x| ≤ A) (hdb : ∃ B, ∀ (x : ℝ), |deriv f x| ≤ B) :
  ProbabilityTheory.variance f (ProbabilityTheory.gaussianReal 0 1) ≤
    ∫ (x : ℝ), deriv f x ^ 2 ∂ProbabilityTheory.gaussianReal 0 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.variance_le_integral_deriv_sq_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Poincare.html#TauCeti.Probability.variance_le_integral_deriv_sq_gaussianReal).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.variance_le_integral_deriv_sq_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Poincare.html#TauCeti.Probability.variance_le_integral_deriv_sq_gaussianReal)
- [Source of `TauCeti.Probability.variance_le_integral_deriv_sq_gaussianReal` in TauCeti/Probability/Distributions/Gaussian/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Gaussian/Poincare.lean#L206)
