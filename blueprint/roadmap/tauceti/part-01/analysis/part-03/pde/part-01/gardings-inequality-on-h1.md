---
declaration: theorem
origin: cited
lean: TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self, TauCeti.Vortex.exists_integral_gaugeFixedGradientDensity_add_mul_integral_norm_sq_le, TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm_of_norm_le, TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm
statement: formalized
proof: formalized
---

# Gårding's inequality on `H¹(Ω)`

For a uniformly elliptic principal coefficient with
lower constant `λ`, a drift bounded by `β` and a nonnegative mass coefficient,

`(λ/2)‖∇u‖²_{L²} - (β²/2λ)‖u‖²_{L²} ≤ a(u, u)`

for every `u ∈ H¹(Ω)`. The drift is absorbed by Young's inequality at the cost of half of the
ellipticity floor, which is where the negative `L²` term comes from. Under the stated general
assumption `c ≥ 0`, either a Poincaré inequality or a sufficiently positive mass lower bound is
needed to eliminate that term.

```lean
TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  {lam Lam beta gamma : ℝ} [mu.IsAddHaarMeasure] [DecidableEq ι]
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  (hc_nonneg : ∀ x ∈ ↑Omega, 0 ≤ c x) (u : ↥(TauCeti.W1p mu Omega 2)) :
  lam / 2 * ‖TauCeti.W1p.gradient u‖ ^ 2 - beta ^ 2 / (2 * lam) * ‖TauCeti.W1p.value u‖ ^ 2 ≤
    TauCeti.PDE.energyFormH1 a b c u u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weitzenböck formula at a vortex](../../../part-02/taubes-gromov-theory/the-weitzenbock-formula-at-a-vortex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self).

## Other forms

**The Gårding inequality for the gauge-fixed operator at a vortex.** Formalized in Tau Ceti as [`TauCeti.Vortex.exists_integral_gaugeFixedGradientDensity_add_mul_integral_norm_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Garding.html#TauCeti.Vortex.exists_integral_gaugeFixedGradientDensity_add_mul_integral_norm_sq_le).

```lean
TauCeti.Vortex.exists_integral_gaugeFixedGradientDensity_add_mul_integral_norm_sq_le
  {x : ℂ → EuclideanSpace ℝ (Fin 4)} {μ : MeasureTheory.Measure ℂ} [μ.IsAddHaarMeasure]
  (hx : ContDiff ℝ 1 x) (hsol : ∀ (z : ℂ), TauCeti.Vortex.equation x z = 0)
  (hlim :
    Filter.Tendsto (fun z => 4 * ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2)) (Filter.cocompact ℂ)
      (nhds 1))
  (hcov :
    Filter.Tendsto (fun z => TauCeti.Vortex.covariantDerivative x z 1) (Filter.cocompact ℂ)
      (nhds 0))
  {a : ℝ} (ha : a < 1 / 4) :
  ∃ R > 0,
    ∃ K,
      ∀ (y : ℂ → EuclideanSpace ℝ (Fin 4)),
        ContDiff ℝ 2 y →
          HasCompactSupport y →
            ∫ (z : ℂ), TauCeti.Vortex.gaugeFixedGradientDensity x y z ∂μ +
                a * ∫ (z : ℂ), ‖y z‖ ^ 2 ∂μ ≤
              ∫ (z : ℂ), ‖TauCeti.Vortex.gaugeFixedOperator x y z‖ ^ 2 ∂μ +
                K * ∫ (z : ℂ) in Metric.closedBall 0 R, ‖y z‖ ^ 2 ∂μ
```

**Gårding's inequality in `H¹`-norm form, without a sign condition on `c`.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm_of_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm_of_norm_le).

```lean
TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm_of_norm_le.{u_1} {ι : Type u_1}
  [Fintype ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  {lam Lam beta gamma : ℝ} [mu.IsAddHaarMeasure] [DecidableEq ι]
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  (u : ↥(TauCeti.W1p mu Omega 2)) :
  lam / 2 * ‖u‖ ^ 2 - (lam / 2 + gamma + beta ^ 2 / (2 * lam)) * ‖TauCeti.W1p.value u‖ ^ 2 ≤
    TauCeti.PDE.energyFormH1 a b c u u
```

**Gårding's inequality in the roadmap's `H¹`-norm form.** Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm).

```lean
TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self_norm.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ}
  {lam Lam beta gamma : ℝ} [mu.IsAddHaarMeasure] [DecidableEq ι]
  (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  (hc_nonneg : ∀ x ∈ ↑Omega, 0 ≤ c x) (u : ↥(TauCeti.W1p mu Omega 2)) :
  lam / 2 * ‖u‖ ^ 2 - (lam / 2 + beta ^ 2 / (2 * lam)) * ‖TauCeti.W1p.value u‖ ^ 2 ≤
    TauCeti.PDE.energyFormH1 a b c u u
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Sobolev.html#TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self)
- [Source of `TauCeti.PDE.UniformlyEllipticOn.garding_energyFormH1_self` in TauCeti/Analysis/PDE/EnergyForm/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/EnergyForm/Sobolev.lean#L973)
