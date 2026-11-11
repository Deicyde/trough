---
declaration: theorem
origin: cited
lean: TauCeti.exists_setLAverage_enorm_sub_setAverage_rpow_le_mul_bmoSeminorm_rpow, TauCeti.measure_lt_norm_sub_setAverage_closedBall_le, TauCeti.measure_lt_norm_sub_setAverage_le, TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le_of_bmoSeminorm_le, TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le
statement: formalized
proof: formalized
---

# The John–Nirenberg inequality in `Lᵖ` form

For every exponent `0 < p` there is a
constant `C`, depending only on the dimension `n ≥ 1` and on `p`, such that the following holds
for every additive Haar measure `μ` on `ℝⁿ = EuclideanSpace ℝ ι`. If `f : ℝⁿ → E` is locally
integrable, then on every ball `B`

`⨍_B ‖f - f_B‖ ^ p ≤ C ‖f‖_{BMO} ^ p`.

```lean
TauCeti.exists_setLAverage_enorm_sub_setAverage_rpow_le_mul_bmoSeminorm_rpow.{u_1, u_3}
  {ι : Type u_1} [Fintype ι] {p : ℝ} (hp : 0 < p) :
  ∃ C,
    ∀ {E : Type u_3} [inst : NormedAddCommGroup E] [inst_1 : NormedSpace ℝ E] [CompleteSpace E]
      {μ : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [μ.IsAddHaarMeasure]
      {f : EuclideanSpace ℝ ι → E},
      MeasureTheory.LocallyIntegrable f μ →
        ∀ (x₀ : EuclideanSpace ℝ ι) (r : ℝ),
          ⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
              ‖f x - ⨍ (y : EuclideanSpace ℝ ι) in Metric.ball x₀ r, f y ∂μ‖ₑ ^ p ∂μ ≤
            ↑C * TauCeti.bmoSeminorm f μ ^ p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lebesgue's differentiation theorem along dyadic cubes](../../measure/lebesgues-differentiation-theorem-along-dyadic-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_setLAverage_enorm_sub_setAverage_rpow_le_mul_bmoSeminorm_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.exists_setLAverage_enorm_sub_setAverage_rpow_le_mul_bmoSeminorm_rpow).

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

**The John–Nirenberg inequality for functions of bounded mean oscillation.** Formalized in Tau Ceti as [`TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le_of_bmoSeminorm_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le_of_bmoSeminorm_le).

```lean
TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le_of_bmoSeminorm_le.{u_1, u_3}
  {ι : Type u_1} [Fintype ι] :
  ∃ A,
    0 < A ∧
      ∃ C,
        ∀ {E : Type u_3} [inst : NormedAddCommGroup E] [inst_1 : NormedSpace ℝ E] [CompleteSpace E]
          {μ : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [μ.IsAddHaarMeasure]
          {f : EuclideanSpace ℝ ι → E} {M : NNReal} {σ : ℝ},
          MeasureTheory.LocallyIntegrable f μ →
            TauCeti.bmoSeminorm f μ ≤ ↑M →
              σ * ↑M ≤ A →
                ∀ (x₀ : EuclideanSpace ℝ ι) (r : ℝ),
                  ∫⁻ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                      ENNReal.ofReal
                        (Real.exp
                          (σ * ‖f x - ⨍ (y : EuclideanSpace ℝ ι) in Metric.ball x₀ r, f y ∂μ‖)) ∂μ ≤
                    ↑C * μ (Metric.ball x₀ r)
```

**The John–Nirenberg inequality on Euclidean balls.** Formalized in Tau Ceti as [`TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.exists_setLIntegral_exp_mul_norm_sub_setAverage_ball_le).

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

## Sources

- [Tau Ceti documentation: `TauCeti.exists_setLAverage_enorm_sub_setAverage_rpow_le_mul_bmoSeminorm_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.exists_setLAverage_enorm_sub_setAverage_rpow_le_mul_bmoSeminorm_rpow)
- [Source of `TauCeti.exists_setLAverage_enorm_sub_setAverage_rpow_le_mul_bmoSeminorm_rpow` in TauCeti/MeasureTheory/Integral/JohnNirenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/JohnNirenberg.lean#L1238)
