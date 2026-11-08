---
declaration: theorem
origin: cited
lean: AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation, DiscreteConvolution.tsum_addRingConvolution_sq_le, DiscreteConvolution.tsum_addRingConvolution_sq_le', MeasureTheory.lintegral_lconvolution_sq_le, TauCeti.two_mul_real_inner_le_add_mul_norm_sq
statement: formalized
proof: formalized
---

# Young's inequality along a curve

the integral of `g (u r) |u'|(r)` is at most the
dissipation.

```lean
AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation.{u_1} {X : Type u_1}
  [PseudoMetricSpace X] {p q : ℝ} {g : X → ENNReal} {u : ℝ → X} {s t : ℝ}
  (hpq : p.HolderConjugate q) (hu : AbsolutelyContinuousOnInterval u s t) :
  ∫⁻ (r : ℝ) in Set.uIoc s t, g (u r) * TauCeti.metricDerivative u r ≤
    TauCeti.dissipation p q g u s t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for weak norms](../normed/part-01/holders-inequality-for-weak-norms.md)

## Lean

Formalized in Tau Ceti as [`AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MaximalSlope/Basic.html#AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation).

## Other forms

**Young's inequality `‖f ⋆ g‖₂ ≤ ‖g‖₁ ‖f‖₂` for families in `ℝ≥0∞` on an additive group, in squared form.** Formalized in Tau Ceti as [`DiscreteConvolution.tsum_addRingConvolution_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/DiscreteConvolution.html#DiscreteConvolution.tsum_addRingConvolution_sq_le).

```lean
DiscreteConvolution.tsum_addRingConvolution_sq_le.{u_1} {G : Type u_1} [AddGroup G]
  (f g : G → ENNReal) :
  ∑' (x : G), DiscreteConvolution.addRingConvolution f g x ^ 2 ≤
    (∑' (x : G), g x) ^ 2 * ∑' (x : G), f x ^ 2
```

**Young's inequality in the other orientation, `‖f ⋆ g‖₂ ≤ ‖f‖₁ ‖g‖₂`, for families in `ℝ≥0∞` on an additive group, in squared form.** Formalized in Tau Ceti as [`DiscreteConvolution.tsum_addRingConvolution_sq_le'`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/DiscreteConvolution.html#DiscreteConvolution.tsum_addRingConvolution_sq_le').

```lean
DiscreteConvolution.tsum_addRingConvolution_sq_le'.{u_1} {G : Type u_1} [AddGroup G]
  (f g : G → ENNReal) :
  ∑' (x : G), DiscreteConvolution.addRingConvolution f g x ^ 2 ≤
    (∑' (x : G), f x) ^ 2 * ∑' (x : G), g x ^ 2
```

**Young's inequality `L¹ ⋆ L² ⊆ L²`.** Formalized in Tau Ceti as [`MeasureTheory.lintegral_lconvolution_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convolution/Young.html#MeasureTheory.lintegral_lconvolution_sq_le).

```lean
MeasureTheory.lintegral_lconvolution_sq_le.{u_1} {G : Type u_1} {mG : MeasurableSpace G}
  [AddGroup G] [MeasurableAdd₂ G] [MeasurableNeg G] {μ : MeasureTheory.Measure G}
  [MeasureTheory.SFinite μ] [μ.IsAddLeftInvariant] {f g : G → ENNReal} (hf : AEMeasurable f μ)
  (hg : AEMeasurable g μ) :
  ∫⁻ (x : G), MeasureTheory.lconvolution f g μ x ^ 2 ∂μ ≤
    (∫⁻ (y : G), f y ∂μ) ^ 2 * ∫⁻ (x : G), g x ^ 2 ∂μ
```

**Young's inequality for real inner products.** Formalized in Tau Ceti as [`TauCeti.two_mul_real_inner_le_add_mul_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Young.html#TauCeti.two_mul_real_inner_le_add_mul_norm_sq).

```lean
TauCeti.two_mul_real_inner_le_add_mul_norm_sq.{u_1} {F : Type u_1} [SeminormedAddCommGroup F]
  [InnerProductSpace ℝ F] (x y : F) {ε : ℝ} (hε : 0 < ε) :
  2 * inner ℝ x y ≤ ε * ‖x‖ ^ 2 + ε⁻¹ * ‖y‖ ^ 2
```

## Sources

- [Tau Ceti documentation: `AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MaximalSlope/Basic.html#AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation)
- [Source of `AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation` in TauCeti/Analysis/GradientFlow/MaximalSlope/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/GradientFlow/MaximalSlope/Basic.lean#L162)
