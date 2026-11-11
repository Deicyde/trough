---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_ball, TauCeti.exists_pos_mul_integral_norm_sq_le_integral_norm_fderiv_sq_add_integral_mul_norm_sq, TauCeti.W1p.norm_value_le_mul_norm_gradient_of_subset_slab, TauCeti.W1p.norm_value_le_mul_norm_gradient_of_subset_ball, TauCeti.setIntegral_norm_sq_le_of_convex, TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_slab, TauCeti.W1p.setAverage_norm_value_sub_setAverage_closedBall_le
statement: formalized
proof: formalized
---

# The Poincaré inequality on a ball

A `C¹` function on `ℝ^{n+1}` supported in a ball of
radius `R` satisfies `‖u‖_p ≤ 2R ‖Du‖_p` for every `1 ≤ p ≤ ∞`.

This is the shape the estimate takes on a bounded domain: any `Ω ⊆ Metric.ball c R` sits inside a
slab of width `2R`, so the constant may be taken to be twice the radius. It is not the optimal
constant — for the ball the sharp one is smaller — but it is explicit and depends on nothing but
`R`.

```lean
TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_ball.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {n : ℕ} {u : EuclideanSpace ℝ (Fin (n + 1)) → F}
  {c : EuclideanSpace ℝ (Fin (n + 1))} {R : ℝ} (hu : ContDiff ℝ 1 u)
  (hsupp : Function.support u ⊆ Metric.ball c R) {p : ENNReal} (hp : 1 ≤ p) :
  MeasureTheory.eLpNorm u p MeasureTheory.volume ≤
    ENNReal.ofReal (2 * R) * MeasureTheory.eLpNorm (fderiv ℝ u) p MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The one-dimensional Poincaré inequality](the-one-dimensional-poincare-inequality.md)
- [The Poincaré–Wirtinger inequality on a ball](the-poincare-wirtinger-inequality-on-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Slab.html#TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_ball).

## Other forms

**Poincaré inequality for a Schrödinger form.** Formalized in Tau Ceti as [`TauCeti.exists_pos_mul_integral_norm_sq_le_integral_norm_fderiv_sq_add_integral_mul_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Schrodinger.html#TauCeti.exists_pos_mul_integral_norm_sq_le_integral_norm_fderiv_sq_add_integral_mul_norm_sq).

```lean
TauCeti.exists_pos_mul_integral_norm_sq_le_integral_norm_fderiv_sq_add_integral_mul_norm_sq.{u_1,
    u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [Nontrivial E] [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [CompleteSpace F] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {P : E → ℝ}
  (hP : MeasureTheory.LocallyIntegrable P μ) (hP₀ : ∀ᵐ (z : E) ∂μ, 0 ≤ P z) {a R : ℝ} (ha : 0 < a)
  (haP : ∀ᵐ (z : E) ∂μ, R < ‖z‖ → a ≤ P z) :
  ∃ c > 0,
    ∀ (u : E → F),
      ContDiff ℝ 1 u →
        HasCompactSupport u →
          c * ∫ (z : E), ‖u z‖ ^ 2 ∂μ ≤
            ∫ (z : E), ‖fderiv ℝ u z‖ ^ 2 ∂μ + ∫ (z : E), P z * ‖u z‖ ^ 2 ∂μ
```

**The Poincaré inequality on `W^{1,p}_0(Ω)`.** Formalized in Tau Ceti as [`TauCeti.W1p.norm_value_le_mul_norm_gradient_of_subset_slab`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/W1p0.html#TauCeti.W1p.norm_value_le_mul_norm_gradient_of_subset_slab).

```lean
TauCeti.W1p.norm_value_le_mul_norm_gradient_of_subset_slab {n : ℕ}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin (n + 1)))} {p : ENNReal} [Fact (1 ≤ p)]
  {i : Fin (n + 1)} {a b : ℝ} (hOmega : ∀ x ∈ ↑Omega, x.ofLp i ∈ Set.Icc a b)
  {u : ↥(TauCeti.W1p MeasureTheory.volume Omega p)}
  (hu : u ∈ TauCeti.w1p0Submodule MeasureTheory.volume Omega p) :
  ‖TauCeti.W1p.value u‖ ≤ (b - a) * ‖TauCeti.W1p.gradient u‖
```

**The Poincaré inequality on `W^{1,p}_0(Ω)` for a bounded domain.** Formalized in Tau Ceti as [`TauCeti.W1p.norm_value_le_mul_norm_gradient_of_subset_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/W1p0.html#TauCeti.W1p.norm_value_le_mul_norm_gradient_of_subset_ball).

```lean
TauCeti.W1p.norm_value_le_mul_norm_gradient_of_subset_ball {n : ℕ}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin (n + 1)))} {p : ENNReal} [Fact (1 ≤ p)]
  {c : EuclideanSpace ℝ (Fin (n + 1))} {R : ℝ} (hOmega : ↑Omega ⊆ Metric.ball c R)
  {u : ↥(TauCeti.W1p MeasureTheory.volume Omega p)}
  (hu : u ∈ TauCeti.w1p0Submodule MeasureTheory.volume Omega p) :
  ‖TauCeti.W1p.value u‖ ≤ 2 * R * ‖TauCeti.W1p.gradient u‖
```

**The Poincaré inequality on a convex domain, relative to a subset.** Formalized in Tau Ceti as [`TauCeti.setIntegral_norm_sq_le_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Basic.html#TauCeti.setIntegral_norm_sq_le_of_convex).

```lean
TauCeti.setIntegral_norm_sq_le_of_convex.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u : E → F} {Ω S : Set E} (hΩ : IsOpen Ω)
  (hΩc : Convex ℝ Ω) (hb : Bornology.IsBounded Ω) (hu : ContDiff ℝ 1 u) (hSm : MeasurableSet S)
  (hS : S ⊆ Ω) (hS₀ : μ S ≠ 0) :
  ∫ (x : E) in Ω, ‖u x‖ ^ 2 ∂μ ≤
    (2 + 4 * μ.real Ω / μ.real S) *
          (μ.real (Metric.ball 0 1) * Metric.diam Ω ^ (Module.finrank ℝ E + 1) / μ.real S) ^ 2 *
        ∫ (x : E) in Ω, ‖fderiv ℝ u x‖ ^ 2 ∂μ +
      4 * μ.real Ω / μ.real S * ∫ (x : E) in S, ‖u x‖ ^ 2 ∂μ
```

**The Poincaré inequality on a slab.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_slab`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Slab.html#TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_slab).

```lean
TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_slab.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {n : ℕ} {u : EuclideanSpace ℝ (Fin (n + 1)) → F} {i : Fin (n + 1)} {a b : ℝ}
  (hu : ContDiff ℝ 1 u) (hsupp : ∀ x ∈ Function.support u, x.ofLp i ∈ Set.Icc a b) {p : ENNReal}
  (hp : 1 ≤ p) :
  MeasureTheory.eLpNorm u p MeasureTheory.volume ≤
    ENNReal.ofReal (b - a) * MeasureTheory.eLpNorm (fderiv ℝ u) p MeasureTheory.volume
```

**Poincaré's inequality for the mean oscillation on a closed ball.** Formalized in Tau Ceti as [`TauCeti.W1p.setAverage_norm_value_sub_setAverage_closedBall_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.html#TauCeti.W1p.setAverage_norm_value_sub_setAverage_closedBall_le).

```lean
TauCeti.W1p.setAverage_norm_value_sub_setAverage_closedBall_le.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {x : E} {r : ℝ} (hr : 0 < r)
  (hball : Metric.ball x r ⊆ ↑Omega) (u : ↥(TauCeti.W1p mu Omega p)) :
  ⨍ (y : E) in Metric.closedBall x r,
      ‖↑↑(TauCeti.W1p.value u) y -
          ⨍ (z : E) in Metric.closedBall x r, ↑↑(TauCeti.W1p.value u) z ∂mu‖ ∂mu ≤
    2 ^ (Module.finrank ℝ E + 1) * r *
      ⨍ (y : E) in Metric.ball x r, ‖↑↑(TauCeti.W1p.gradient u) y‖ ∂mu
```

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Slab.html#TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_ball)
- [Source of `TauCeti.eLpNorm_le_eLpNorm_fderiv_of_support_subset_ball` in TauCeti/Analysis/Sobolev/Poincare/Slab.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Poincare/Slab.lean#L363)
