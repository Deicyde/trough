---
declaration: theorem
origin: cited
lean: TauCeti.enorm_integral_mul_le, TauCeti.enorm_integral_inner_le, TauCeti.rpow_lintegral_le_measure_univ_rpow_mul
statement: formalized
proof: formalized
---

# Hölder's inequality for the integral of a product

`‖∫ u v‖ ≤ ‖u‖_p ‖v‖_q` for Hölder
conjugate exponents `p` and `q`.

```lean
TauCeti.enorm_integral_mul_le.{u_1, u_4} {α : Type u_1} {mα : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {𝕜 : Type u_4} [NonUnitalNormedRing 𝕜] [NormedSpace ℝ 𝕜]
  {p q : ENNReal} [p.HolderConjugate q] {u v : α → 𝕜} :
  ‖∫ (x : α), u x * v x ∂μ‖ₑ ≤ MeasureTheory.eLpNorm u p μ * MeasureTheory.eLpNorm v q μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.enorm_integral_mul_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Duality.html#TauCeti.enorm_integral_mul_le).

## Other forms

**Hölder's inequality for the integral of an inner product.** Formalized in Tau Ceti as [`TauCeti.enorm_integral_inner_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Duality.html#TauCeti.enorm_integral_inner_le).

```lean
TauCeti.enorm_integral_inner_le.{u_1, u_4, u_5} {α : Type u_1} {mα : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {𝕜 : Type u_4} {H : Type u_5} [RCLike 𝕜] [NormedAddCommGroup H]
  [InnerProductSpace 𝕜 H] {p q : ENNReal} [p.HolderConjugate q] {u v : α → H} :
  ‖∫ (x : α), inner 𝕜 (u x) (v x) ∂μ‖ₑ ≤ MeasureTheory.eLpNorm u p μ * MeasureTheory.eLpNorm v q μ
```

**Hölder's inequality in extended-valued `∫⁻` form, raised to the power `r`.** Formalized in Tau Ceti as [`TauCeti.rpow_lintegral_le_measure_univ_rpow_mul`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/LIntegralRpow.html#TauCeti.rpow_lintegral_le_measure_univ_rpow_mul).

```lean
TauCeti.rpow_lintegral_le_measure_univ_rpow_mul.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {u : α → ENNReal} (hu : AEMeasurable u μ) {r : ℝ} (hr : 1 ≤ r) :
  (∫⁻ (x : α), u x ∂μ) ^ r ≤ μ Set.univ ^ (r - 1) * ∫⁻ (x : α), u x ^ r ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.enorm_integral_mul_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/Duality.html#TauCeti.enorm_integral_mul_le)
- [Source of `TauCeti.enorm_integral_mul_le` in TauCeti/MeasureTheory/Function/Lp/Duality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/Lp/Duality.lean#L103)
