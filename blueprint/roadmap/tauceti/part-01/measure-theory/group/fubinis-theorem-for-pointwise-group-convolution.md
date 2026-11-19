---
declaration: theorem
origin: cited
lean: MeasureTheory.Integrable.integral_integral_smul_comp_inv_mul
statement: formalized
proof: formalized
---

# Fubini's theorem for pointwise group convolution

for integrable `h` and `f` on a
σ-compact locally compact group,
`∫ x, ∫ y, h y • f (y⁻¹ * x) ∂μ ∂μ = (∫ y, h y ∂μ) • ∫ x, f x ∂μ`.

```lean
MeasureTheory.Integrable.integral_integral_smul_comp_inv_mul.{u_1, u_2, u_3} {G : Type u_1}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G]
  [SigmaCompactSpace G] [MeasurableSpace G] [BorelSpace G] {μ : MeasureTheory.Measure G}
  [μ.IsMulLeftInvariant] [MeasureTheory.IsLocallyFiniteMeasure μ] [μ.InnerRegularCompactLTTop]
  {𝕜 : Type u_2} {E : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedSpace 𝕜 E] [SMulCommClass ℝ 𝕜 E] [CompleteSpace E] {h : G → 𝕜}
  (hh : MeasureTheory.Integrable h μ) {f : G → E} (hf : MeasureTheory.Integrable f μ) :
  ∫ (x : G), ∫ (y : G), h y • f (y⁻¹ * x) ∂μ ∂μ = (∫ (y : G), h y ∂μ) • ∫ (x : G), f x ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Kakutani–Kodaira theorem](../../../part-02/topology/algebra/part-01/the-kakutani-kodaira-theorem.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Integrable.integral_integral_smul_comp_inv_mul`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/Convolution/Pointwise.html#MeasureTheory.Integrable.integral_integral_smul_comp_inv_mul).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Integrable.integral_integral_smul_comp_inv_mul`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/Convolution/Pointwise.html#MeasureTheory.Integrable.integral_integral_smul_comp_inv_mul)
- [Source of `MeasureTheory.Integrable.integral_integral_smul_comp_inv_mul` in TauCeti/MeasureTheory/Group/Convolution/Pointwise.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Group/Convolution/Pointwise.lean#L860)
