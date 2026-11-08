---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_totalVariationOn, TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient_of_lt, TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball, TauCeti.W1p.exists_eLpNorm_value_le_of_isLipschitzDomainWith, TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv_of_lt
statement: formalized
proof: formalized
---

# The Sobolev inequality for functions of bounded variation

Let `E` have dimension
`n ≥ 2` and let `p = n / (n - 1)`. Every integrable `u : E → ℝ` satisfies `‖u‖_p ≤ C |Du|(E)`,
where `|Du|(E)` is the total variation of `u` on the whole space, finite or infinite, and `C` is
the constant `MeasureTheory.eLpNormLESNormFDerivOneConst μ p` of the `C¹` Gagliardo–Nirenberg–
Sobolev inequality `MeasureTheory.eLpNorm_le_eLpNorm_fderiv_one`.

```lean
TauCeti.eLpNorm_le_totalVariationOn.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {p : NNReal} {u : E → ℝ}
  (hu : MeasureTheory.Integrable u μ) (hp : (↑(Module.finrank ℝ E)).HolderConjugate p) :
  MeasureTheory.eLpNorm u (↑p) μ ≤
    ↑(MeasureTheory.eLpNormLESNormFDerivOneConst μ ↑p) * TauCeti.totalVariationOn μ ⊤ u
```

## Depends on

- [TauCeti.totalVariationOn](tauceti-totalvariationon.md)

## Proof depends on

- [Extension theorem for bounded Lipschitz domains](../../part-02/sobolev/part-01/extension-theorem-for-bounded-lipschitz-domains.md)
- [The Gagliardo--Nirenberg--Sobolev inequality on `W^{1,p}(E)`](../../part-02/sobolev/part-01/the-gagliardo-nirenberg-sobolev-inequality-on-w.md)
- [Rademacher's theorem for locally Lipschitz functions](../calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Young's inequality for an `L¹` kernel](../../../measure-theory/function/youngs-inequality-for-an-l1-kernel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.html#TauCeti.eLpNorm_le_totalVariationOn).

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

**The Sobolev inequality on `W^{1,p}_0` of a ball.** Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/FiniteMeasure.html#TauCeti.W1p.eLpNorm_value_le_mul_rpow_mul_enorm_gradient_of_eq_ball).

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

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.html#TauCeti.eLpNorm_le_totalVariationOn)
- [Source of `TauCeti.eLpNorm_le_totalVariationOn` in TauCeti/Analysis/BoundedVariation/Sobolev/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.lean#L67)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
