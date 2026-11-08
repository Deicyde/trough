---
declaration: theorem
origin: cited
lean: TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le, TauCeti.measure_lt_norm_sub_setAverage_closedBall_le, TauCeti.measure_lt_norm_sub_setAverage_le
statement: formalized
proof: formalized
---

# The John–Nirenberg inequality on Euclidean balls

There are constants `A > 0` and `C`,
depending only on the dimension `n`, such that the following holds for every additive Haar
measure `μ` on `ℝⁿ = EuclideanSpace ℝ ι`. Let `f : ℝⁿ → E` be integrable on the ball `B(x₀, R)`,
with mean oscillation `⨍_B ‖f - f_B‖ ≤ M` on every ball `B ⊆ B(x₀, R)`. If `σ M ≤ A`, then on the
concentric ball `B' = B(x₀, R / (2√n))`,

`∫_{B'} exp (σ ‖f - f_{B'}‖) ≤ C |B'|`.

```lean
TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le.{u_1, u_3} {ι : Type u_1}
  [Fintype ι] :
  ∃ A,
    0 < A ∧
      ∃ C,
        ∀ {E : Type u_3} [inst : NormedAddCommGroup E] [inst_1 : NormedSpace ℝ E] [CompleteSpace E]
          {μ : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [μ.IsAddHaarMeasure]
          {f : EuclideanSpace ℝ ι → E} {x₀ : EuclideanSpace ℝ ι} {R : ℝ} {M : NNReal} {σ : ℝ},
          MeasureTheory.IntegrableOn f (Metric.ball x₀ R) μ →
            (∀ (y : EuclideanSpace ℝ ι) (s : ℝ),
                Metric.ball y s ⊆ Metric.ball x₀ R →
                  ⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball y s,
                      ‖f x - ⨍ (z : EuclideanSpace ℝ ι) in Metric.ball y s, f z ∂μ‖ₑ ∂μ ≤
                    ↑M) →
              σ * ↑M ≤ A →
                ∫⁻ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ (R / (2 * √↑(Fintype.card ι))),
                    ENNReal.ofReal
                      (Real.exp
                        (σ *
                          ‖f x -
                              ⨍ (y : EuclideanSpace ℝ ι) in
                                Metric.ball x₀ (R / (2 * √↑(Fintype.card ι))), f y ∂μ‖)) ∂μ ≤
                  ↑C * μ (Metric.ball x₀ (R / (2 * √↑(Fintype.card ι))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lebesgue's differentiation theorem along dyadic cubes](../../../number-theory/part-01/heights-units-and-s-units-of-number-fields/part-01/lebesgues-differentiation-theorem-along-dyadic-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le).

## Other forms

**The John–Nirenberg inequality on a cube, for any additive Haar measure.** Formalized in Tau Ceti as [`TauCeti.measure_lt_norm_sub_setAverage_closedBall_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.measure_lt_norm_sub_setAverage_closedBall_le).

```lean
TauCeti.measure_lt_norm_sub_setAverage_closedBall_le.{u_1, u_2} {ι : Type u_1} [Fintype ι]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] {f : (ι → ℝ) → E} {M : NNReal} {c : ι → ℝ}
  {r : ℝ} [CompleteSpace E] {μ : MeasureTheory.Measure (ι → ℝ)} [μ.IsAddHaarMeasure]
  (hf : MeasureTheory.IntegrableOn f (Metric.closedBall c r) μ)
  (hM :
    ∀ (y : ι → ℝ) (ρ : ℝ),
      Metric.closedBall y ρ ⊆ Metric.closedBall c r →
        ⨍⁻ (x : ι → ℝ) in Metric.closedBall y ρ,
            ‖f x - ⨍ (z : ι → ℝ) in Metric.closedBall y ρ, f z ∂μ‖ₑ ∂μ ≤
          ↑M)
  (s : ℝ) :
  μ {x | x ∈ Metric.closedBall c r ∧ s < ‖f x - ⨍ (y : ι → ℝ) in Metric.closedBall c r, f y ∂μ‖} ≤
    ENNReal.ofReal (2 * Real.exp (-(Real.log 2 * s / (2 ^ (Fintype.card ι + 1) * ↑M)))) *
      μ (Metric.closedBall c r)
```

**The John–Nirenberg inequality on a dyadic cube, for any additive Haar measure.** Formalized in Tau Ceti as [`TauCeti.measure_lt_norm_sub_setAverage_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.measure_lt_norm_sub_setAverage_le).

```lean
TauCeti.measure_lt_norm_sub_setAverage_le.{u_1, u_2} {ι : Type u_1} [Fintype ι] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {f : (ι → ℝ) → E} {q₀ : ℤ × (ι → ℤ)} {M : NNReal}
  [CompleteSpace E] {μ : MeasureTheory.Measure (ι → ℝ)} [μ.IsAddHaarMeasure]
  (hf : MeasureTheory.IntegrableOn f (TauCeti.dyadicCube q₀.1 q₀.2) μ)
  (hM :
    ∀ (q : ℤ × (ι → ℤ)),
      TauCeti.dyadicCube q.1 q.2 ⊆ TauCeti.dyadicCube q₀.1 q₀.2 →
        ⨍⁻ (x : ι → ℝ) in TauCeti.dyadicCube q.1 q.2,
            ‖f x - ⨍ (y : ι → ℝ) in TauCeti.dyadicCube q.1 q.2, f y ∂μ‖ₑ ∂μ ≤
          ↑M)
  (s : ℝ) :
  μ
      {x |
        x ∈ TauCeti.dyadicCube q₀.1 q₀.2 ∧
          s < ‖f x - ⨍ (y : ι → ℝ) in TauCeti.dyadicCube q₀.1 q₀.2, f y ∂μ‖} ≤
    ENNReal.ofReal (2 * Real.exp (-(Real.log 2 * s / (2 ^ (Fintype.card ι + 1) * ↑M)))) *
      μ (TauCeti.dyadicCube q₀.1 q₀.2)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le)
- [Source of `TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le` in TauCeti/MeasureTheory/Integral/JohnNirenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/JohnNirenberg.lean#L1017)
