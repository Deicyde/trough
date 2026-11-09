---
declaration: theorem
origin: cited
lean: TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball, TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient_of_lt, TauCeti.W1p.exists_eLpNorm_value_le_of_isLipschitzDomainWith, TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv_of_lt
statement: formalized
proof: formalized
---

# The Sobolev inequality on `W^{1,p}_0` of a ball

Let `n ≥ 1` be the dimension and
`ω = μ(B(0, 1))`, and let `p ≤ q < ∞` with `δ = 1/p - 1/q < 1/n`. If `Ω = B(x₀, R)`, then every
`u ∈ W^{1,p}_0(Ω)` satisfies

`‖u‖_{L^q} ≤ n⁻¹ ω ^ (-δ) ((1 - δ) / (1/n - δ)) ^ (1 - δ) R ^ (1 - n δ) ‖∇u‖_{Lᵖ}`.

The power `R ^ (1 - n δ)` is the one dictated by scaling, so the remaining constant depends only
on `n`, `δ` and the normalization of `μ`.

```lean
TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] [Nontrivial E] (hp : p ≠ ⊤)
  {x₀ : E} {R : ℝ} (hR : 0 < R) (hOmega : ↑Omega = Metric.ball x₀ R) {q : NNReal} (hpq : p ≤ ↑q)
  {δ : ℝ} (hδ : p.toReal⁻¹ - (↑q)⁻¹ = δ) (hδn : δ < (↑(Module.finrank ℝ E))⁻¹)
  {u : ↥(TauCeti.W1p mu Omega p)} (hu : u ∈ TauCeti.w1p0Submodule mu Omega p) :
  MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value u)) (↑q) (mu.restrict ↑Omega) ≤
    ENNReal.ofReal
        ((↑(Module.finrank ℝ E))⁻¹ * mu.real (Metric.ball 0 1) ^ (-δ) *
            ((1 - δ) / ((↑(Module.finrank ℝ E))⁻¹ - δ)) ^ (1 - δ) *
          R ^ (1 - ↑(Module.finrank ℝ E) * δ)) *
      ‖TauCeti.W1p.gradient u‖ₑ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Extension theorem for bounded Lipschitz domains](../part-01/extension-theorem-for-bounded-lipschitz-domains.md)
- [The Gagliardo--Nirenberg--Sobolev inequality on `W^{1,p}(E)`](../part-01/the-gagliardo-nirenberg-sobolev-inequality-on-w.md)
- [Young's inequality for integral kernels](../../../../measure-theory/integral/part-02/youngs-inequality-for-integral-kernels.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/FiniteMeasure.html#TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball).

## Other forms

**The Sobolev inequality on `W^{1,p}_0(Ω)` for `Ω` of finite measure.** Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient_of_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/FiniteMeasure.html#TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient_of_lt).

```lean
TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient_of_lt.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] [Nontrivial E] (hp : p ≠ ⊤)
  (hOmega : mu ↑Omega ≠ ⊤) {q : NNReal} (hpq : p ≤ ↑q) {δ : ℝ} (hδ : p.toReal⁻¹ - (↑q)⁻¹ = δ)
  (hδn : δ < (↑(Module.finrank ℝ E))⁻¹) {u : ↥(TauCeti.W1p mu Omega p)}
  (hu : u ∈ TauCeti.w1p0Submodule mu Omega p) :
  MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value u)) (↑q) (mu.restrict ↑Omega) ≤
    ENNReal.ofReal
          ((↑(Module.finrank ℝ E))⁻¹ * mu.real (Metric.ball 0 1) ^ (-(↑(Module.finrank ℝ E))⁻¹) *
            ((1 - δ) / ((↑(Module.finrank ℝ E))⁻¹ - δ)) ^ (1 - δ)) *
        mu ↑Omega ^ ((↑(Module.finrank ℝ E))⁻¹ - δ) *
      ‖TauCeti.W1p.gradient u‖ₑ
```

**The Sobolev inequality on bounded Lipschitz domains.** Formalized in Tau Ceti as [`TauCeti.W1p.exists_eLpNorm_value_le_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/SobolevEmbedding.html#TauCeti.W1p.exists_eLpNorm_value_le_of_isLipschitzDomainWith).

```lean
TauCeti.W1p.exists_eLpNorm_value_le_of_isLipschitzDomainWith.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p pstar : ENNReal}
  [Fact (1 ≤ p)] (hpstar : pstar ≠ ⊤)
  (hexp : pstar⁻¹ + (↑(Module.finrank ℝ (WithLp 2 (ℝ × E))))⁻¹ = p⁻¹)
  (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω) {q : ENNReal} (hq : q ≤ pstar) :
  ∃ C,
    ∀ (u : ↥(TauCeti.W1p MeasureTheory.volume Ω p)),
      MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value u)) q (MeasureTheory.volume.restrict ↑Ω) ≤
        ↑C * ‖u‖ₑ
```

**The Sobolev inequality on sets of finite measure, for compactly supported functions.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv_of_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/FiniteMeasure.html#TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv_of_lt).

```lean
TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv_of_lt.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [Nontrivial E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u : E → F} {Ω : Set E} (hu : ContDiff ℝ 1 u)
  (h2u : HasCompactSupport u) (hΩ : MeasurableSet Ω) (hsupp : tsupport u ⊆ Ω) {p q : NNReal}
  (hp : 1 ≤ p) (hpq : p ≤ q) {δ : ℝ} (hδ : (↑p)⁻¹ - (↑q)⁻¹ = δ)
  (hδn : δ < (↑(Module.finrank ℝ E))⁻¹) :
  MeasureTheory.eLpNorm u (↑q) μ ≤
    ENNReal.ofReal
          ((↑(Module.finrank ℝ E))⁻¹ * μ.real (Metric.ball 0 1) ^ (-(↑(Module.finrank ℝ E))⁻¹) *
            ((1 - δ) / ((↑(Module.finrank ℝ E))⁻¹ - δ)) ^ (1 - δ)) *
        μ Ω ^ ((↑(Module.finrank ℝ E))⁻¹ - δ) *
      MeasureTheory.eLpNorm (fderiv ℝ u) (↑p) μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/FiniteMeasure.html#TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball)
- [Source of `TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball` in TauCeti/Analysis/Sobolev/FiniteMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/FiniteMeasure.lean#L170)
