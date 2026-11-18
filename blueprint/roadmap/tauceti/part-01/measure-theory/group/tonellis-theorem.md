---
declaration: theorem
origin: cited
lean: AEMeasurable.lintegral_lintegral_mul_comp_inv_mul_swap, AEMeasurable.lintegral_lintegral_mul_comp_inv_mul
statement: formalized
proof: formalized
---

# Tonelli's theorem

**Tonelli's theorem** (Fubini swap) for the nonnegative extended-real convolution integrand
`(x, y) ↦ h y * f (y⁻¹ * x)` on a σ-compact locally compact group.

```lean
AEMeasurable.lintegral_lintegral_mul_comp_inv_mul_swap.{u_1} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G] [SigmaCompactSpace G]
  [MeasurableSpace G] [BorelSpace G] {μ : MeasureTheory.Measure G} [μ.IsMulLeftInvariant]
  [MeasureTheory.IsLocallyFiniteMeasure μ] [μ.InnerRegularCompactLTTop] {h f : G → ENNReal}
  (hh : AEMeasurable h μ) (hf : AEMeasurable f μ) :
  ∫⁻ (x : G), ∫⁻ (y : G), h y * f (y⁻¹ * x) ∂μ ∂μ = ∫⁻ (y : G), ∫⁻ (x : G), h y * f (y⁻¹ * x) ∂μ ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Kakutani–Kodaira theorem](../../../part-02/topology/algebra/part-01/the-kakutani-kodaira-theorem.md)

## Lean

Formalized in Tau Ceti as [`AEMeasurable.lintegral_lintegral_mul_comp_inv_mul_swap`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/Convolution/Pointwise.html#AEMeasurable.lintegral_lintegral_mul_comp_inv_mul_swap).

## Other forms

**Tonelli's theorem for group convolution.** Formalized in Tau Ceti as [`AEMeasurable.lintegral_lintegral_mul_comp_inv_mul`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/Convolution/Pointwise.html#AEMeasurable.lintegral_lintegral_mul_comp_inv_mul).

```lean
AEMeasurable.lintegral_lintegral_mul_comp_inv_mul.{u_1} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G] [SigmaCompactSpace G]
  [MeasurableSpace G] [BorelSpace G] {μ : MeasureTheory.Measure G} [μ.IsMulLeftInvariant]
  [MeasureTheory.IsLocallyFiniteMeasure μ] [μ.InnerRegularCompactLTTop] {h f : G → ENNReal}
  (hh : AEMeasurable h μ) (hf : AEMeasurable f μ) :
  ∫⁻ (x : G), ∫⁻ (y : G), h y * f (y⁻¹ * x) ∂μ ∂μ = (∫⁻ (y : G), h y ∂μ) * ∫⁻ (x : G), f x ∂μ
```

## Sources

- [Tau Ceti documentation: `AEMeasurable.lintegral_lintegral_mul_comp_inv_mul_swap`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/Convolution/Pointwise.html#AEMeasurable.lintegral_lintegral_mul_comp_inv_mul_swap)
- [Source of `AEMeasurable.lintegral_lintegral_mul_comp_inv_mul_swap` in TauCeti/MeasureTheory/Group/Convolution/Pointwise.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Group/Convolution/Pointwise.lean#L660)
