---
declaration: theorem
origin: cited
lean: MeasureTheory.Lp.norm_convolutionL_apply_le, TauCeti.norm_convolutionLp_le
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

## Sources

- [Tau Ceti documentation: `MeasureTheory.Lp.norm_convolutionL_apply_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/GroupConvolution.html#MeasureTheory.Lp.norm_convolutionL_apply_le)
- [Source of `MeasureTheory.Lp.norm_convolutionL_apply_le` in TauCeti/MeasureTheory/Function/Lp/GroupConvolution.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Lp/GroupConvolution.lean#L177)
