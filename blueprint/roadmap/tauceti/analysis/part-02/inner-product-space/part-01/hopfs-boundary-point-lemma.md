---
declaration: theorem
origin: cited
lean: TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere, TauCeti.fderiv_pos_of_mul_le_laplacian_add_fderiv_of_lt_ball_of_le_sphere, TauCeti.fderiv_neg_of_laplacian_add_fderiv_le_mul_of_gt_ball_of_ge_sphere, TauCeti.fderiv_pos_of_harmonicOnNhd_of_lt_closedBall, TauCeti.fderiv_neg_of_harmonicOnNhd_of_gt_closedBall, TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_closedBall, TauCeti.fderiv_neg_of_laplacian_nonpos_of_gt_ball_of_ge_sphere, TauCeti.fderiv_neg_of_laplacian_nonpos_of_gt_closedBall
statement: formalized
proof: formalized
---

# Hopf's boundary-point lemma

Let `B = ball y R` be a ball in a finite-dimensional real
inner product space, let `e` be a unit vector, and let `x₀ = y + R • e` be the point where the
outward ray in direction `e` meets the sphere `∂B`. If `u` is continuous on `closedBall y R`, twice
continuously differentiable on `B`, and differentiable at `x₀`, is subharmonic on `B` (`0 ≤ Δ u`),
stays strictly below the value `u x₀`
inside `B` and weakly below it on the sphere `∂B`, then `u` leaves `x₀` in the direction `e` at a
strictly positive rate: `0 < fderiv ℝ u x₀ e`.

The strict inequality is needed only inside the ball, so the theorem applies directly when the
boundary sphere has merely a weak bound. The classical form, with a strict maximum over the whole
closed ball, is `TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_closedBall`.

```lean
TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u : E → ℝ} {y : E} {R : ℝ}
  {e : E} (hR : 0 < R) (he : ‖e‖ = 1) (hucont : ContinuousOn u (Metric.closedBall y R))
  (huinterior : ∀ x ∈ Metric.ball y R, ContDiffAt ℝ 2 u x)
  (hderiv : DifferentiableAt ℝ u (y + R • e))
  (hlap : ∀ x ∈ Metric.ball y R, 0 ≤ Laplacian.laplacian u x)
  (hlt : ∀ x ∈ Metric.ball y R, u x < u (y + R • e))
  (hle : ∀ x ∈ Metric.sphere y R, u x ≤ u (y + R • e)) : 0 < (fderiv ℝ u (y + R • e)) e
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere).

## Other forms

**Hopf's boundary-point lemma for `-Δ - b·∇ + c`.** Formalized in Tau Ceti as [`TauCeti.fderiv_pos_of_mul_le_laplacian_add_fderiv_of_lt_ball_of_le_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_pos_of_mul_le_laplacian_add_fderiv_of_lt_ball_of_le_sphere).

```lean
TauCeti.fderiv_pos_of_mul_le_laplacian_add_fderiv_of_lt_ball_of_le_sphere.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u c : E → ℝ} {b : E → E}
  {y e : E} {R β γ : ℝ} (hR : 0 < R) (he : ‖e‖ = 1)
  (hucont : ContinuousOn u (Metric.closedBall y R))
  (huinterior : ∀ x ∈ Metric.ball y R, ContDiffAt ℝ 2 u x)
  (hderiv : DifferentiableAt ℝ u (y + R • e)) (hc : ∀ x ∈ Metric.ball y R, 0 ≤ c x)
  (hcγ : ∀ x ∈ Metric.ball y R, c x ≤ γ) (hb : ∀ x ∈ Metric.ball y R, ‖b x‖ ≤ β)
  (hsub : ∀ x ∈ Metric.ball y R, c x * u x ≤ Laplacian.laplacian u x + (fderiv ℝ u x) (b x))
  (hnonneg : 0 ≤ u (y + R • e)) (hlt : ∀ x ∈ Metric.ball y R, u x < u (y + R • e))
  (hle : ∀ x ∈ Metric.sphere y R, u x ≤ u (y + R • e)) : 0 < (fderiv ℝ u (y + R • e)) e
```

**Hopf's boundary-point lemma for `-Δ - b·∇ + c`, minimum form.** Formalized in Tau Ceti as [`TauCeti.fderiv_neg_of_laplacian_add_fderiv_le_mul_of_gt_ball_of_ge_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_neg_of_laplacian_add_fderiv_le_mul_of_gt_ball_of_ge_sphere).

```lean
TauCeti.fderiv_neg_of_laplacian_add_fderiv_le_mul_of_gt_ball_of_ge_sphere.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u c : E → ℝ} {b : E → E}
  {y e : E} {R β γ : ℝ} (hR : 0 < R) (he : ‖e‖ = 1)
  (hucont : ContinuousOn u (Metric.closedBall y R))
  (huinterior : ∀ x ∈ Metric.ball y R, ContDiffAt ℝ 2 u x)
  (hderiv : DifferentiableAt ℝ u (y + R • e)) (hc : ∀ x ∈ Metric.ball y R, 0 ≤ c x)
  (hcγ : ∀ x ∈ Metric.ball y R, c x ≤ γ) (hb : ∀ x ∈ Metric.ball y R, ‖b x‖ ≤ β)
  (hsuper : ∀ x ∈ Metric.ball y R, Laplacian.laplacian u x + (fderiv ℝ u x) (b x) ≤ c x * u x)
  (hnonpos : u (y + R • e) ≤ 0) (hgt : ∀ x ∈ Metric.ball y R, u (y + R • e) < u x)
  (hge : ∀ x ∈ Metric.sphere y R, u (y + R • e) ≤ u x) : (fderiv ℝ u (y + R • e)) e < 0
```

**Hopf's boundary-point lemma for harmonic functions.** Formalized in Tau Ceti as [`TauCeti.fderiv_pos_of_harmonicOnNhd_of_lt_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_pos_of_harmonicOnNhd_of_lt_closedBall).

```lean
TauCeti.fderiv_pos_of_harmonicOnNhd_of_lt_closedBall.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u : E → ℝ} {y : E} {R : ℝ} {e : E} (hR : 0 < R)
  (he : ‖e‖ = 1) (hucont : ContinuousOn u (Metric.closedBall y R))
  (hderiv : DifferentiableAt ℝ u (y + R • e))
  (hharm : InnerProductSpace.HarmonicOnNhd u (Metric.ball y R))
  (hmax : ∀ x ∈ Metric.closedBall y R, x ≠ y + R • e → u x < u (y + R • e)) :
  0 < (fderiv ℝ u (y + R • e)) e
```

**Hopf's boundary-point lemma for harmonic functions, minimum form.** Formalized in Tau Ceti as [`TauCeti.fderiv_neg_of_harmonicOnNhd_of_gt_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_neg_of_harmonicOnNhd_of_gt_closedBall).

```lean
TauCeti.fderiv_neg_of_harmonicOnNhd_of_gt_closedBall.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u : E → ℝ} {y : E} {R : ℝ} {e : E} (hR : 0 < R)
  (he : ‖e‖ = 1) (hucont : ContinuousOn u (Metric.closedBall y R))
  (hderiv : DifferentiableAt ℝ u (y + R • e))
  (hharm : InnerProductSpace.HarmonicOnNhd u (Metric.ball y R))
  (hmin : ∀ x ∈ Metric.closedBall y R, x ≠ y + R • e → u (y + R • e) < u x) :
  (fderiv ℝ u (y + R • e)) e < 0
```

**Hopf's boundary-point lemma, classical form.** Formalized in Tau Ceti as [`TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_closedBall).

```lean
TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_closedBall.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u : E → ℝ} {y : E} {R : ℝ} {e : E} (hR : 0 < R)
  (he : ‖e‖ = 1) (hucont : ContinuousOn u (Metric.closedBall y R))
  (huinterior : ∀ x ∈ Metric.ball y R, ContDiffAt ℝ 2 u x)
  (hderiv : DifferentiableAt ℝ u (y + R • e))
  (hlap : ∀ x ∈ Metric.ball y R, 0 ≤ Laplacian.laplacian u x)
  (hmax : ∀ x ∈ Metric.closedBall y R, x ≠ y + R • e → u x < u (y + R • e)) :
  0 < (fderiv ℝ u (y + R • e)) e
```

**Hopf's boundary-point lemma, minimum form.** Formalized in Tau Ceti as [`TauCeti.fderiv_neg_of_laplacian_nonpos_of_gt_ball_of_ge_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_neg_of_laplacian_nonpos_of_gt_ball_of_ge_sphere).

```lean
TauCeti.fderiv_neg_of_laplacian_nonpos_of_gt_ball_of_ge_sphere.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u : E → ℝ} {y : E} {R : ℝ}
  {e : E} (hR : 0 < R) (he : ‖e‖ = 1) (hucont : ContinuousOn u (Metric.closedBall y R))
  (huinterior : ∀ x ∈ Metric.ball y R, ContDiffAt ℝ 2 u x)
  (hderiv : DifferentiableAt ℝ u (y + R • e))
  (hlap : ∀ x ∈ Metric.ball y R, Laplacian.laplacian u x ≤ 0)
  (hgt : ∀ x ∈ Metric.ball y R, u (y + R • e) < u x)
  (hge : ∀ x ∈ Metric.sphere y R, u (y + R • e) ≤ u x) : (fderiv ℝ u (y + R • e)) e < 0
```

**Hopf's boundary-point lemma, minimum form.** Formalized in Tau Ceti as [`TauCeti.fderiv_neg_of_laplacian_nonpos_of_gt_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_neg_of_laplacian_nonpos_of_gt_closedBall).

```lean
TauCeti.fderiv_neg_of_laplacian_nonpos_of_gt_closedBall.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u : E → ℝ} {y : E} {R : ℝ} {e : E} (hR : 0 < R)
  (he : ‖e‖ = 1) (hucont : ContinuousOn u (Metric.closedBall y R))
  (huinterior : ∀ x ∈ Metric.ball y R, ContDiffAt ℝ 2 u x)
  (hderiv : DifferentiableAt ℝ u (y + R • e))
  (hlap : ∀ x ∈ Metric.ball y R, Laplacian.laplacian u x ≤ 0)
  (hmin : ∀ x ∈ Metric.closedBall y R, x ≠ y + R • e → u (y + R • e) < u x) :
  (fderiv ℝ u (y + R • e)) e < 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.html#TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere)
- [Source of `TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere` in TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Laplacian/HopfLemma.lean#L435)
