---
declaration: theorem
origin: cited
lean: TauCeti.Probability.multivariateGaussianMixtureMeasure_eq_add_withDensity
statement: formalized
proof: formalized
---

# Lebesgue decomposition

A multivariate Gaussian mixture is the sum of its weighted
components whose covariance is not positive definite, each singular with respect to Lebesgue
measure by `mutuallySingular_multivariateGaussian_volume`, and of Lebesgue measure weighted by the
mixture density.

```lean
TauCeti.Probability.multivariateGaussianMixtureMeasure_eq_add_withDensity.{u_1, u_2} {κ : Type u_1}
  {ι : Type u_2} [Fintype κ] [Fintype ι] [DecidableEq ι] (p : Convexity.StdSimplex NNReal κ)
  (m : κ → EuclideanSpace ℝ ι) (S : κ → Matrix ι ι ℝ) :
  TauCeti.Probability.multivariateGaussianMixtureMeasure p m S =
    ∑ k with ¬(S k).PosDef, ↑(p.weights k) • ProbabilityTheory.multivariateGaussian (m k) (S k) +
      MeasureTheory.volume.withDensity (TauCeti.Probability.multivariateGaussianMixturePDF p m S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.multivariateGaussianMixtureMeasure_eq_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Mixture/Multivariate.html#TauCeti.Probability.multivariateGaussianMixtureMeasure_eq_add_withDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.multivariateGaussianMixtureMeasure_eq_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Mixture/Multivariate.html#TauCeti.Probability.multivariateGaussianMixtureMeasure_eq_add_withDensity)
- [Source of `TauCeti.Probability.multivariateGaussianMixtureMeasure_eq_add_withDensity` in TauCeti/Probability/Distributions/Gaussian/Mixture/Multivariate.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Gaussian/Mixture/Multivariate.lean#L229)
