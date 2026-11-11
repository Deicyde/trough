---
declaration: theorem
origin: cited
lean: TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le
statement: formalized
proof: formalized
---

# Moser's crossover estimate (`TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le`)

There are constants `A > 0` and `C`, depending only on the
dimension `n`, such that the following holds for every additive Haar measure `μ` on
`ℝⁿ = EuclideanSpace ℝ ι`. Let `f : ℝⁿ → ℝ` be integrable on the ball `B(x₀, R)`, with mean
oscillation `⨍_B |f - f_B| ≤ M` on every ball `B ⊆ B(x₀, R)`. If `|σ| M ≤ A`, then on the
concentric ball `B' = B(x₀, R / (2√n))`,

`(∫_{B'} exp (σ f)) (∫_{B'} exp (-σ f)) ≤ C |B'|²`.

For `f = log u`, with `u` positive, this compares the averages of `u^σ` and of `u^(-σ)` over `B'`:
it is the step of Moser's proof of the Harnack inequality that links the bounds for positive
powers of a supersolution to those for its negative powers.

```lean
TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le.{u_1} {ι : Type u_1}
  [Fintype ι] :
  ∃ A,
    0 < A ∧
      ∃ C,
        ∀ {μ : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [μ.IsAddHaarMeasure]
          {f : EuclideanSpace ℝ ι → ℝ} {x₀ : EuclideanSpace ℝ ι} {R : ℝ} {M : NNReal} {σ : ℝ},
          MeasureTheory.IntegrableOn f (Metric.ball x₀ R) μ →
            (∀ (y : EuclideanSpace ℝ ι) (s : ℝ),
                Metric.ball y s ⊆ Metric.ball x₀ R →
                  ⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball y s,
                      ‖f x - ⨍ (z : EuclideanSpace ℝ ι) in Metric.ball y s, f z ∂μ‖ₑ ∂μ ≤
                    ↑M) →
              |σ| * ↑M ≤ A →
                (∫⁻ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ (R / (2 * √↑(Fintype.card ι))),
                      ENNReal.ofReal (Real.exp (σ * f x)) ∂μ) *
                    ∫⁻ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ (R / (2 * √↑(Fintype.card ι))),
                      ENNReal.ofReal (Real.exp (-(σ * f x))) ∂μ ≤
                  ↑C * μ (Metric.ball x₀ (R / (2 * √↑(Fintype.card ι)))) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The John–Nirenberg inequality in `Lᵖ` form](the-john-nirenberg-inequality-in-lp-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le)
- [Source of `TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le` in TauCeti/MeasureTheory/Integral/JohnNirenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/JohnNirenberg.lean#L1124)
