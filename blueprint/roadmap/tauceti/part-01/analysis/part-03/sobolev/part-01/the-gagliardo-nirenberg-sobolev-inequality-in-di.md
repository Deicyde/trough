---
declaration: theorem
origin: cited
lean: TauCeti.integral_sq_le_mul_sq_integral_norm_fderiv, TauCeti.norm_testFunctionLp_le_mul_norm_gradientTestFunctionLp, TauCeti.D1p0.norm_sobolevEmbeddingL_le, TauCeti.W1p.norm_sobolevEmbeddingTopL_le, TauCeti.W1p.eLpNorm_value_le_mul_enorm_gradient
statement: formalized
proof: formalized
---

# The Gagliardo–Nirenberg–Sobolev inequality in dimension two

**The Gagliardo–Nirenberg–Sobolev inequality in dimension two**, `∫ f² ≤ G (∫ ‖Df‖)²` for
compactly supported `C¹` real functions, as an inequality of Bochner integrals. The constant `G`
is Mathlib's `lintegralPowLePowLIntegralFDerivConst μ 2`.

```lean
TauCeti.integral_sq_le_mul_sq_integral_norm_fderiv.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] (hE : Module.finrank ℝ E = 2) {f : E → ℝ}
  (hf : ContDiff ℝ 1 f) (hfs : HasCompactSupport f) :
  ∫ (x : E), f x ^ 2 ∂μ ≤
    ↑(MeasureTheory.lintegralPowLePowLIntegralFDerivConst μ 2) * (∫ (x : E), ‖fderiv ℝ f x‖ ∂μ) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_sq_le_mul_sq_integral_norm_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Planar.html#TauCeti.integral_sq_le_mul_sq_integral_norm_fderiv).

## Other forms

**The Gagliardo--Nirenberg--Sobolev inequality between test-function classes.** Formalized in Tau Ceti as [`TauCeti.norm_testFunctionLp_le_mul_norm_gradientTestFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Embedding.html#TauCeti.norm_testFunctionLp_le_mul_norm_gradientTestFunctionLp).

```lean
TauCeti.norm_testFunctionLp_le_mul_norm_gradientTestFunctionLp.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {pstar : ENNReal}
  (hpstar : pstar ≠ ⊤) (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹)
  (phi : TestFunction Omega ℝ ⊤) :
  ‖TauCeti.testFunctionLp pstar phi‖ ≤
    ↑(MeasureTheory.SNormLESNormFDerivOfEqConst ℝ mu p.toReal) *
      ‖TauCeti.gradientTestFunctionLp p phi‖
```

**The Gagliardo--Nirenberg--Sobolev inequality on `D^{1,p}_0(Ω)`.** Formalized in Tau Ceti as [`TauCeti.D1p0.norm_sobolevEmbeddingL_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/D1p0/Basic.html#TauCeti.D1p0.norm_sobolevEmbeddingL_le).

```lean
TauCeti.D1p0.norm_sobolevEmbeddingL_le.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)]
  [mu.IsAddHaarMeasure] {pstar : ENNReal} (hpstar : pstar ≠ ⊤)
  (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹) (u : ↥(TauCeti.D1p0 mu Omega p)) :
  ‖(TauCeti.D1p0.sobolevEmbeddingL hexp) u‖ ≤
    ↑(MeasureTheory.SNormLESNormFDerivOfEqConst ℝ mu p.toReal) * ‖u‖
```

**The Gagliardo--Nirenberg--Sobolev inequality on `W^{1,p}(E)`.** Formalized in Tau Ceti as [`TauCeti.W1p.norm_sobolevEmbeddingTopL_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.html#TauCeti.W1p.norm_sobolevEmbeddingTopL_le).

```lean
TauCeti.W1p.norm_sobolevEmbeddingTopL_le.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {p pstar : ENNReal} [Fact (1 ≤ p)]
  (hpstar : pstar ≠ ⊤) (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹)
  (u : ↥(TauCeti.W1p mu ⊤ p)) :
  ‖(TauCeti.W1p.sobolevEmbeddingTopL hpstar hexp) u‖ ≤
    ↑(MeasureTheory.SNormLESNormFDerivOfEqConst ℝ mu p.toReal) * ‖TauCeti.W1p.gradient u‖
```

**The Gagliardo--Nirenberg--Sobolev inequality on `W^{1,p}_0(Ω)`.** Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_le_mul_enorm_gradient`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Embedding.html#TauCeti.W1p.eLpNorm_value_le_mul_enorm_gradient).

```lean
TauCeti.W1p.eLpNorm_value_le_mul_enorm_gradient.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E}
  {p : ENNReal} [Fact (1 ≤ p)] {pstar : ENNReal} (hpstar : pstar ≠ ⊤)
  (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹) {u : ↥(TauCeti.W1p mu Omega p)}
  (hu : u ∈ TauCeti.w1p0Submodule mu Omega p) :
  MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value u)) pstar (mu.restrict ↑Omega) ≤
    ↑(MeasureTheory.SNormLESNormFDerivOfEqConst ℝ mu p.toReal) * ‖TauCeti.W1p.gradient u‖ₑ
```

## Sources

- [Tau Ceti documentation: `TauCeti.integral_sq_le_mul_sq_integral_norm_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Planar.html#TauCeti.integral_sq_le_mul_sq_integral_norm_fderiv)
- [Source of `TauCeti.integral_sq_le_mul_sq_integral_norm_fderiv` in TauCeti/Analysis/Sobolev/Poincare/Planar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Poincare/Planar.lean#L132)
