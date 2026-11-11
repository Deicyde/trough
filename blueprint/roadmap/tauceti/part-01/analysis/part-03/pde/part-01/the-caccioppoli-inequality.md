---
declaration: theorem
origin: cited
lean: TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le_divergence, TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_le_divergence, TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_le_sub_setAverage_divergence, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_memLp, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_rpow_mul_norm_gradient_sq_le, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le_of_ae_eq_rpow, TauCeti.PDE.exists_setIntegral_ball_norm_gradient_posPartAbove_sq_le, TauCeti.PDE.exists_setIntegral_ball_norm_gradient_posPartAbove_sq_le_lowerOrder
statement: formalized
proof: formalized
---

# The Caccioppoli inequality

Let `a` be measurable and uniformly elliptic on `Ω` with
constants `0 < λ ≤ Λ`, and let `u ∈ H¹(Ω)` be a weak solution of `-∂ᵢ(aⁱʲ ∂ⱼu) = f` in `Ω`, in
the sense that `a(u, v) = ∫_Ω f v` for every `v ∈ H¹₀(Ω)`, with no boundary condition on `u`.
Then for every smooth `ψ` compactly supported in `Ω`,

`∫_Ω ψ² ‖∇u‖² ≤ (2Λ/λ)² ∫_Ω ‖∇ψ‖² u² + (2/λ) ∫_Ω ψ² f u`.

For `f = 0` the last term vanishes, and the gradient of `u` where `ψ = 1` is bounded by `u`
itself on the support of `ψ`.

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le.{u_1} {ι : Type u_1}
  [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {lam Lam : ℝ} [DecidableEq ι] (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  {f : ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))} {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ↑↑f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu)
  {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) :
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2 ∂mu ≤
    (2 * Lam / lam) ^ 2 *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
          ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu +
      2 / lam *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ↑↑f x * ↑↑(TauCeti.W1p.value u) x ∂mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)
- [Young's inequality for inner products](../../inner-product-space/part-04/youngs-inequality-for-inner-products.md)
- [The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution](../part-03/the-zero-forcing-caccioppoli-inequality-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Basic.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le).

## Other forms

**The Caccioppoli inequality for a datum in divergence form.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Divergence.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le_divergence).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le_divergence.{u_1}
  {ι : Type u_1} [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {lam Lam : ℝ} {F : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} [DecidableEq ι]
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hF : MeasureTheory.MemLp F 2 (mu.restrict ↑Omega)) {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
        -∫ (x : EuclideanSpace ℝ ι) in ↑Omega, inner ℝ (F x) (↑↑(TauCeti.W1p.gradient ↑v) x) ∂mu)
  {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) :
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2 ∂mu ≤
    2 * ((2 * Lam / lam) ^ 2 + 1) *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
          ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu +
      12 / lam ^ 2 * ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖F x‖ ^ 2 ∂mu
```

**The Caccioppoli inequality for a datum in divergence form, on concentric balls.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_le_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Divergence.html#TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_le_divergence).

```lean
TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_le_divergence.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] :
  ∃ C,
    0 < C ∧
      ∀ {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [inst : mu.IsAddHaarMeasure]
        {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ}
        {F : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {u : ↥(TauCeti.W1p mu Omega 2)}
        {x₀ : EuclideanSpace ℝ ι} {r R : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            MeasureTheory.MemLp F 2 (mu.restrict ↑Omega) →
              (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                  TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                    -∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                        inner ℝ (F x) (↑↑(TauCeti.W1p.gradient ↑v) x) ∂mu) →
                r < R →
                  Metric.ball x₀ R ⊆ ↑Omega →
                    ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                        ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2 ∂mu ≤
                      2 * ((2 * Lam / lam) ^ 2 + 1) * (C / (R - r)) ^ 2 *
                          ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                            ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu +
                        12 / lam ^ 2 * ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R, ‖F x‖ ^ 2 ∂mu
```

**The Caccioppoli inequality for a datum in divergence form, with the mean subtracted.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_le_sub_setAverage_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Divergence.html#TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_le_sub_setAverage_divergence).

```lean
TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_le_sub_setAverage_divergence.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] :
  ∃ C,
    0 < C ∧
      ∀ {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [inst : mu.IsAddHaarMeasure]
        {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ}
        {F : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {u : ↥(TauCeti.W1p mu Omega 2)}
        {y : EuclideanSpace ℝ ι} {ρ : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            MeasureTheory.MemLp F 2 (mu.restrict ↑Omega) →
              (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                  TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                    -∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                        inner ℝ (F x) (↑↑(TauCeti.W1p.gradient ↑v) x) ∂mu) →
                0 < ρ →
                  Metric.ball y (2 * ρ) ⊆ ↑Omega →
                    ∫ (x : EuclideanSpace ℝ ι) in Metric.ball y ρ,
                        ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2 ∂mu ≤
                      2 * ((2 * Lam / lam) ^ 2 + 1) * (C / ρ) ^ 2 *
                          ∫ (x : EuclideanSpace ℝ ι) in Metric.ball y (2 * ρ),
                            (↑↑(TauCeti.W1p.value u) x -
                                ⨍ (z : EuclideanSpace ℝ ι) in Metric.ball y (2 * ρ),
                                  ↑↑(TauCeti.W1p.value u) z ∂mu) ^
                              2 ∂mu +
                        12 / lam ^ 2 *
                          ∫ (x : EuclideanSpace ℝ ι) in Metric.ball y (2 * ρ), ‖F x‖ ^ 2 ∂mu
```

**The Caccioppoli inequality for a nonnegative-level truncation of a weak subsolution.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Truncation.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ}
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  {f : ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))} {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        TauCeti.PDE.energyFormH1 a 0 0 u ↑v ≤
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ↑↑f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu)
  {k : ℝ} (hk : 0 ≤ k) {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ)
  (hcpt : HasCompactSupport ψ) (hts : tsupport ψ ⊆ ↑Omega) :
  have w :=
    TauCeti.W1p.posPartAbove
      TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp._proof_1
      hk u;
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient w) x‖ ^ 2 ∂mu ≤
    (2 * Lam / lam) ^ 2 *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
          ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu +
      2 / lam *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ↑↑f x * ↑↑(TauCeti.W1p.value w) x ∂mu
```

**The Caccioppoli inequality for a nonnegative-level truncation of a weak subsolution with lower-order terms.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/LowerOrder.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
  {c : EuclideanSpace ℝ ι → ℝ} {lam Lam beta gamma : ℝ}
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  {f : ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))} {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        TauCeti.PDE.energyFormH1 a b c u ↑v ≤
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ↑↑f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu)
  {k : ℝ} (hk : 0 ≤ k) {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ)
  (hcpt : HasCompactSupport ψ) (hts : tsupport ψ ⊆ ↑Omega) :
  have w :=
    TauCeti.W1p.posPartAbove
      TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_memLp._proof_1
      hk u;
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient w) x‖ ^ 2 ∂mu ≤
    2 * (2 * Lam / lam) ^ 2 *
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
            ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu +
        (2 * beta / lam) ^ 2 *
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu +
      4 / lam *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
          ψ x ^ 2 * (↑↑f x - c x * ↑↑(TauCeti.W1p.value u) x) * ↑↑(TauCeti.W1p.value w) x ∂mu
```

**The Caccioppoli inequality for a positive truncation of a weak subsolution.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Truncation.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ}
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  {f : ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))} {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        TauCeti.PDE.energyFormH1 a 0 0 u ↑v ≤
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ↑↑f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu)
  {k : ℝ}
  (hwLp :
    MeasureTheory.MemLp (fun x => max (↑↑(TauCeti.W1p.value u) x - k) 0) 2 (mu.restrict ↑Omega))
  {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) :
  have w :=
    TauCeti.W1p.posPartAboveOfMemLp
      TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp._proof_1
      k u hwLp;
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient w) x‖ ^ 2 ∂mu ≤
    (2 * Lam / lam) ^ 2 *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
          ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu +
      2 / lam *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ↑↑f x * ↑↑(TauCeti.W1p.value w) x ∂mu
```

**The Caccioppoli inequality for a positive truncation of a weak subsolution with lower-order terms.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_memLp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/LowerOrder.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_memLp).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_memLp.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
  {c : EuclideanSpace ℝ ι → ℝ} {lam Lam beta gamma : ℝ}
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  {f : ↥(MeasureTheory.Lp ℝ 2 (mu.restrict ↑Omega))} {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        TauCeti.PDE.energyFormH1 a b c u ↑v ≤
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ↑↑f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu)
  {k : ℝ}
  (hwLp :
    MeasureTheory.MemLp (fun x => max (↑↑(TauCeti.W1p.value u) x - k) 0) 2 (mu.restrict ↑Omega))
  {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) :
  have w :=
    TauCeti.W1p.posPartAboveOfMemLp
      TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_memLp._proof_1
      k u hwLp;
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient w) x‖ ^ 2 ∂mu ≤
    2 * (2 * Lam / lam) ^ 2 *
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
            ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu +
        (2 * beta / lam) ^ 2 *
          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu +
      4 / lam *
        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
          ψ x ^ 2 * (↑↑f x - c x * ↑↑(TauCeti.W1p.value u) x) * ↑↑(TauCeti.W1p.value w) x ∂mu
```

**The Caccioppoli inequality for powers of a positive supersolution.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_rpow_mul_norm_gradient_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Power.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_rpow_mul_norm_gradient_sq_le).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_rpow_mul_norm_gradient_sq_le.{u_1} {ι : Type u_1}
  [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {lam Lam : ℝ} [DecidableEq ι] (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega)) {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v)
  {ε : ℝ} (hε : 0 < ε)
  (hεu : ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, ε ≤ ↑↑(TauCeti.W1p.value u) x) {p : ℝ}
  (hp : p < 1) {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) :
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
      ψ x ^ 2 * (↑↑(TauCeti.W1p.value u) x ^ (p - 2) * ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2) ∂mu ≤
    (2 * Lam / ((1 - p) * lam)) ^ 2 *
      ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value u) x ^ p ∂mu
```

**The Caccioppoli inequality for the power `w = u^{p/2}` of a positive supersolution.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le_of_ae_eq_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Power.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le_of_ae_eq_rpow).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le_of_ae_eq_rpow.{u_1}
  {ι : Type u_1} [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {lam Lam : ℝ} [DecidableEq ι] (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega)) {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v)
  {ε : ℝ} (hε : 0 < ε)
  (hεu : ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, ε ≤ ↑↑(TauCeti.W1p.value u) x) {p : ℝ}
  (hp : p < 1) {w : ↥(TauCeti.W1p mu Omega 2)}
  (hwv :
    ↑↑(TauCeti.W1p.value w) =ᵐ[mu.restrict ↑Omega] fun x => ↑↑(TauCeti.W1p.value u) x ^ (p / 2))
  {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) :
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient w) x‖ ^ 2 ∂mu ≤
    (|p| * Lam / ((1 - p) * lam)) ^ 2 *
      ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ‖gradient ψ x‖ ^ 2 * ↑↑(TauCeti.W1p.value w) x ^ 2 ∂mu
```

**The Caccioppoli inequality on concentric balls.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_setIntegral_ball_norm_gradient_posPartAbove_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Truncation.html#TauCeti.PDE.exists_setIntegral_ball_norm_gradient_posPartAbove_sq_le).

```lean
TauCeti.PDE.exists_setIntegral_ball_norm_gradient_posPartAbove_sq_le.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] :
  ∃ c,
    0 < c ∧
      ∀ {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [inst : mu.IsAddHaarMeasure]
        {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
        {k : ℝ}
        (hwLp :
          MeasureTheory.MemLp (fun x => max (↑↑(TauCeti.W1p.value u) x - k) 0) 2
            (mu.restrict ↑Omega))
        {x₀ : EuclideanSpace ℝ ι} {r R : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                  TauCeti.PDE.energyFormH1 a 0 0 u ↑v ≤ 0) →
              r < R →
                Metric.ball x₀ R ⊆ ↑Omega →
                  ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                      ‖↑↑(TauCeti.W1p.gradient
                                  (TauCeti.W1p.posPartAboveOfMemLp
                                    TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_of_memLp._proof_1
                                    k u hwLp))
                            x‖ ^
                        2 ∂mu ≤
                    (2 * Lam / lam) ^ 2 * (c / (R - r)) ^ 2 *
                      ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                        max (↑↑(TauCeti.W1p.value u) x - k) 0 ^ 2 ∂mu
```

**The Caccioppoli inequality on concentric balls, with lower-order terms.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_setIntegral_ball_norm_gradient_posPartAbove_sq_le_lowerOrder`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/LowerOrder.html#TauCeti.PDE.exists_setIntegral_ball_norm_gradient_posPartAbove_sq_le_lowerOrder).

```lean
TauCeti.PDE.exists_setIntegral_ball_norm_gradient_posPartAbove_sq_le_lowerOrder.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] :
  ∃ C,
    0 < C ∧
      ∀ {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [inst : mu.IsAddHaarMeasure]
        {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
        {c : EuclideanSpace ℝ ι → ℝ} {lam Lam beta gamma : ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
        {k : ℝ} (hk : 0 ≤ k) {x₀ : EuclideanSpace ℝ ι} {r R : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega) →
              MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega) →
                (∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) →
                  (∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma) →
                    (∀ x ∈ ↑Omega, 0 ≤ c x) →
                      (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                          (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                              0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                            TauCeti.PDE.energyFormH1 a b c u ↑v ≤ 0) →
                        r < R →
                          Metric.ball x₀ R ⊆ ↑Omega →
                            ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                                ‖↑↑(TauCeti.W1p.gradient
                                            (TauCeti.W1p.posPartAbove
                                              TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_posPartAbove_sq_le_lowerOrder_of_memLp._proof_1
                                              hk u))
                                      x‖ ^
                                  2 ∂mu ≤
                              (2 * (2 * Lam / lam) ^ 2 * (C / (R - r)) ^ 2 + (2 * beta / lam) ^ 2) *
                                ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                                  max (↑↑(TauCeti.W1p.value u) x - k) 0 ^ 2 ∂mu
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Basic.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le)
- [Source of `TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_le` in TauCeti/Analysis/PDE/Caccioppoli/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Caccioppoli/Basic.lean#L404)
