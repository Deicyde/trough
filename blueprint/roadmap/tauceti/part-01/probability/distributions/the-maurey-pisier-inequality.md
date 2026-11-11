---
declaration: theorem
origin: cited
lean: ProbabilityTheory.IsGaussian.lintegral_exp_mul_sub_le
statement: formalized
proof: formalized
---

# The Maurey–Pisier inequality

For a centred Gaussian measure `μ` and a `C¹` function `f`,
`∫∫ exp (t (f y - f x)) dμ(x) dμ(y) ≤ ∫ exp (π² t² / 8 · Var[f' x; μ]) dμ(x)`.

```lean
ProbabilityTheory.IsGaussian.lintegral_exp_mul_sub_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] [SecondCountableTopology E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [ProbabilityTheory.IsGaussian μ] {f : E → ℝ}
  (hμ : ∫ (x : E), id x ∂μ = 0) (hf : ContDiff ℝ 1 f) (t : ℝ) :
  ∫⁻ (p : E × E), ENNReal.ofReal (Real.exp (t * (f p.2 - f p.1))) ∂μ.prod μ ≤
    ∫⁻ (x : E),
      ENNReal.ofReal
        (Real.exp (Real.pi ^ 2 * t ^ 2 / 8 * ProbabilityTheory.variance (⇑(fderiv ℝ f x)) μ)) ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.IsGaussian.lintegral_exp_mul_sub_le`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Concentration.html#ProbabilityTheory.IsGaussian.lintegral_exp_mul_sub_le).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.IsGaussian.lintegral_exp_mul_sub_le`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Concentration.html#ProbabilityTheory.IsGaussian.lintegral_exp_mul_sub_le)
- [Source of `ProbabilityTheory.IsGaussian.lintegral_exp_mul_sub_le` in TauCeti/Probability/Distributions/Gaussian/Concentration.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Gaussian/Concentration.lean#L123)
