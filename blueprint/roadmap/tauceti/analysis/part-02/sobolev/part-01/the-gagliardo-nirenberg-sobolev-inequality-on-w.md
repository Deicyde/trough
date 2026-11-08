---
declaration: theorem
origin: cited
lean: TauCeti.W1p.norm_sobolevEmbeddingTopL_le, TauCeti.norm_testFunctionLp_le_mul_norm_gradientTestFunctionLp, TauCeti.D1p0.norm_sobolevEmbeddingL_le, TauCeti.W1p.eLpNorm_value_le_mul_enorm_gradient
statement: formalized
proof: formalized
---

# The Gagliardo--Nirenberg--Sobolev inequality on `W^{1,p}(E)`

The image of `u` under the
whole-space Sobolev embedding is bounded in `L^{p⋆}` by the `Lᵖ` norm of the gradient of `u`
alone, with Mathlib's constant `MeasureTheory.SNormLESNormFDerivOfEqConst`.

```lean
TauCeti.W1p.norm_sobolevEmbeddingTopL_le.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {p pstar : ENNReal} [Fact (1 ≤ p)]
  (hpstar : pstar ≠ ⊤) (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹)
  (u : ↥(TauCeti.W1p mu ⊤ p)) :
  ‖(TauCeti.W1p.sobolevEmbeddingTopL hpstar hexp) u‖ ≤
    ↑(MeasureTheory.SNormLESNormFDerivOfEqConst ℝ mu p.toReal) * ‖TauCeti.W1p.gradient u‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.norm_sobolevEmbeddingTopL_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.html#TauCeti.W1p.norm_sobolevEmbeddingTopL_le).

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

- [Tau Ceti documentation: `TauCeti.W1p.norm_sobolevEmbeddingTopL_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.html#TauCeti.W1p.norm_sobolevEmbeddingTopL_le)
- [Source of `TauCeti.W1p.norm_sobolevEmbeddingTopL_le` in TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.lean#L112)
