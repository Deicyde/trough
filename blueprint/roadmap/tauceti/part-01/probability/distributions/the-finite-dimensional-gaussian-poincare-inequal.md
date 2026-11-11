---
declaration: theorem
origin: cited
lean: TauCeti.Probability.variance_le_sum_integral_fderiv_sq_pi
statement: formalized
proof: formalized
---

# The finite-dimensional Gaussian Poincaré inequality

For a continuously differentiable
function `f` on `ι → ℝ` with bounded values and bounded partial derivatives, its variance under
the product of standard Gaussian laws is at most the expectation of the squared Euclidean norm
of its gradient, `∑ i, (∂ᵢ f)²`.

```lean
TauCeti.Probability.variance_le_sum_integral_fderiv_sq_pi.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {f : (ι → ℝ) → ℝ} (hf : ContDiff ℝ 1 f) (hfb : ∃ A, ∀ (x : ι → ℝ), |f x| ≤ A)
  (hdb : ∃ B, ∀ (x : ι → ℝ) (i : ι), |(fderiv ℝ f x) (Pi.single i 1)| ≤ B) :
  ProbabilityTheory.variance f
      (MeasureTheory.Measure.pi fun x => ProbabilityTheory.gaussianReal 0 1) ≤
    ∑ i,
      ∫ (x : ι → ℝ),
        (fderiv ℝ f x) (Pi.single i 1) ^
          2 ∂MeasureTheory.Measure.pi fun x => ProbabilityTheory.gaussianReal 0 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Efron–Stein inequality on `Measure.pi` over a finite index type](../other-results/the-efron-stein-inequality-on-measure-pi-over-a.md)
- [The Gaussian Poincaré inequality on `ℝ`](the-gaussian-poincare-inequality-on-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.variance_le_sum_integral_fderiv_sq_pi`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Poincare.html#TauCeti.Probability.variance_le_sum_integral_fderiv_sq_pi).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.variance_le_sum_integral_fderiv_sq_pi`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Poincare.html#TauCeti.Probability.variance_le_sum_integral_fderiv_sq_pi)
- [Source of `TauCeti.Probability.variance_le_sum_integral_fderiv_sq_pi` in TauCeti/Probability/Distributions/Gaussian/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Gaussian/Poincare.lean#L317)
