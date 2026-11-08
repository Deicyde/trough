---
declaration: theorem
origin: cited
lean: MeasureTheory.Lp.norm_convolutionL_apply_le, TauCeti.norm_convolutionLp_le, TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq
statement: formalized
proof: formalized
---

# Young's inequality for an `L¹` kernel

`‖h ⋆ f‖_p ≤ ‖h‖₁ ‖f‖_p`.

```lean
MeasureTheory.Lp.norm_convolutionL_apply_le.{u_1, u_2, u_3} {G : Type u_1} {E : Type u_2} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
  {μ : MeasureTheory.Measure G} [NormedAddCommGroup E] [NormedSpace ℝ E] [μ.IsMulLeftInvariant]
  [MeasureTheory.IsLocallyFiniteMeasure μ] [μ.InnerRegularCompactLTTop] {p : ENNReal} [Fact (1 ≤ p)]
  {𝕜 : Type u_3} [NontriviallyNormedField 𝕜] [NormedSpace 𝕜 E] [SMulCommClass ℝ 𝕜 E] {hp : p ≠ ⊤}
  (h : ↥(MeasureTheory.Lp 𝕜 1 μ)) (f : ↥(MeasureTheory.Lp E p μ)) :
  ‖((MeasureTheory.Lp.convolutionL μ p hp) h) f‖ ≤ ‖h‖ * ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for Young's exponents](../euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Lp.norm_convolutionL_apply_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/GroupConvolution.html#MeasureTheory.Lp.norm_convolutionL_apply_le).

## Other forms

**Young's inequality for convolution with an integrable kernel.** Formalized in Tau Ceti as [`TauCeti.norm_convolutionLp_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Convolution.html#TauCeti.norm_convolutionLp_le).

```lean
TauCeti.norm_convolutionLp_le.{u_1, u_2} {E : Type u_1} {F : Type u_2} [MeasurableSpace E]
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  {p : ENNReal} [Fact (1 ≤ p)] (hp : p ≠ ⊤) (k : E → ℝ) :
  ‖TauCeti.convolutionLp hp k μ‖ ≤ ∫ (y : E), ‖k y‖ ∂μ
```

**Young's inequality for integral kernels.** Formalized in Tau Ceti as [`TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SchurTest.html#TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq).

```lean
TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  [MeasurableSpace α] [MeasurableSpace β] {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} [MeasureTheory.SFinite μ] [MeasureTheory.SFinite ν]
  {k : α → β → ENNReal} (hk : AEMeasurable (Function.uncurry k) (μ.prod ν)) {g : β → ENNReal}
  (hg : AEMeasurable g ν) {p q r : ℝ} (hp : 1 ≤ p) (hpq : p ≤ q) (hr : p⁻¹ + r⁻¹ = 1 + q⁻¹)
  {A B : ENNReal} (hA : ∀ᵐ (x : α) ∂μ, ∫⁻ (y : β), k x y ^ r ∂ν ≤ A)
  (hB : ∀ᵐ (y : β) ∂ν, ∫⁻ (x : α), k x y ^ r ∂μ ≤ B) :
  ∫⁻ (x : α), (∫⁻ (y : β), k x y * g y ∂ν) ^ q ∂μ ≤
    A ^ (q * (1 - p⁻¹)) * B * (∫⁻ (y : β), g y ^ p ∂ν) ^ (q / p)
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Lp.norm_convolutionL_apply_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/GroupConvolution.html#MeasureTheory.Lp.norm_convolutionL_apply_le)
- [Source of `MeasureTheory.Lp.norm_convolutionL_apply_le` in TauCeti/MeasureTheory/Function/Lp/GroupConvolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/Lp/GroupConvolution.lean#L176)
