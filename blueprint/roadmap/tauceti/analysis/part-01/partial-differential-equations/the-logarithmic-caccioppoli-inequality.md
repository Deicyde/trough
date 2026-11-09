---
declaration: theorem
origin: cited
lean: TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_div_value_sq_le, TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_div_sq_le, TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_div_sq_le
statement: formalized
proof: formalized
---

# The logarithmic Caccioppoli inequality

Let `a` be measurable and uniformly elliptic on
`Ω` with constants `0 < λ ≤ Λ`, and let `u ∈ H¹(Ω)` be a weak supersolution of
`-∂ᵢ(aⁱʲ ∂ⱼu) ≥ 0`, that is `a(u, v) ≥ 0` for every nonnegative `v ∈ H¹₀(Ω)`, with `u ≥ ε`
almost everywhere for some `ε > 0`. Then for every smooth `ψ` compactly supported in `Ω`,

`∫_Ω ψ² (‖∇u‖ / u)² ≤ (2Λ/λ)² ∫_Ω ‖∇ψ‖²`.

The integrand on the left is `ψ² ‖∇ log u‖²`, and the right side depends on neither `u` nor
`ε`.

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_div_value_sq_le.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ}
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega)) {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v)
  {ε : ℝ} (hε : 0 < ε)
  (hεu : ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, ε ≤ ↑↑(TauCeti.W1p.value u) x)
  {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) :
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
      ψ x ^ 2 * (‖↑↑(TauCeti.W1p.gradient u) x‖ / ↑↑(TauCeti.W1p.value u) x) ^ 2 ∂mu ≤
    (2 * Lam / lam) ^ 2 * ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ‖gradient ψ x‖ ^ 2 ∂mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Caccioppoli inequality](../../part-02/pde/part-01/the-caccioppoli-inequality.md)
- [TauCeti.Wkp](tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_div_value_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Logarithm.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_div_value_sq_le).

## Other forms

**The logarithmic Caccioppoli inequality.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_div_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Logarithmic.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_div_sq_le).

```lean
TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_sq_div_sq_le.{u_1} {ι : Type u_1}
  [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {lam Lam : ℝ} [DecidableEq ι] (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega)) {u : ↥(TauCeti.W1p mu Omega 2)}
  (hu :
    ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
        0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v)
  {ψ : EuclideanSpace ℝ ι → ℝ} (hψ : ContDiff ℝ (↑⊤) ψ) (hcpt : HasCompactSupport ψ)
  (hts : tsupport ψ ⊆ ↑Omega) {m : ℝ} (hm : 0 < m)
  (hum : ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (tsupport ψ), m ≤ ↑↑(TauCeti.W1p.value u) x) :
  ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
      ψ x ^ 2 * ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2 / ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu ≤
    (2 * Lam / lam) ^ 2 * ∫ (x : EuclideanSpace ℝ ι) in ↑Omega, ‖gradient ψ x‖ ^ 2 ∂mu
```

**The logarithmic Caccioppoli inequality on concentric balls.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_div_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Caccioppoli/Logarithmic.html#TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_div_sq_le).

```lean
TauCeti.PDE.exists_setIntegral_ball_norm_gradient_sq_div_sq_le.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] :
  ∃ c,
    0 < c ∧
      ∀ {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [inst : mu.IsAddHaarMeasure]
        {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
        {x₀ : EuclideanSpace ℝ ι} {r R m : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                  0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v) →
              0 < r →
                r < R →
                  Metric.ball x₀ R ⊆ ↑Omega →
                    0 < m →
                      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ R),
                          m ≤ ↑↑(TauCeti.W1p.value u) x) →
                        ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                            ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2 / ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu ≤
                          (2 * Lam / lam) ^ 2 * (c / (R - r)) ^ 2 * mu.real (Metric.ball x₀ R)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_div_value_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Logarithm.html#TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_div_value_sq_le)
- [Source of `TauCeti.PDE.UniformlyEllipticOn.setIntegral_sq_mul_norm_gradient_div_value_sq_le` in TauCeti/Analysis/PDE/Regularity/Logarithm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Logarithm.lean#L83)
