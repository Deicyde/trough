---
declaration: theorem
origin: cited
lean: TauCeti.measure_lt_maximalFunction_le, TauCeti.eLpNorm_maximalFunction_le, TauCeti.lintegral_rpow_maximalFunction_le, TauCeti.mul_measure_lt_maximalFunction_le
statement: formalized
proof: formalized
---

# The Hardy–Littlewood maximal inequality, in quotient form

```lean
TauCeti.measure_lt_maximalFunction_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E]
  [FiniteDimensional ℝ E] [ENorm F] {t : ENNReal} (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure]
  (f : E → F) (ht : t ≠ 0) :
  μ {x | t < TauCeti.maximalFunction μ f x} ≤ (4 ^ Module.finrank ℝ E * ∫⁻ (x : E), ‖f x‖ₑ ∂μ) / t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Vitali covering estimate](../part-02/the-vitali-covering-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.measure_lt_maximalFunction_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MaximalFunction.html#TauCeti.measure_lt_maximalFunction_le).

## Other forms

**The Hardy–Littlewood maximal inequality, the strong-type `(p, p)` bound for `1 < p < ∞`, in terms of representative-level `Lᵖ` seminorms.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_maximalFunction_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MaximalFunction.html#TauCeti.eLpNorm_maximalFunction_le).

```lean
TauCeti.eLpNorm_maximalFunction_le.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] [FiniteDimensional ℝ E] [ENorm F]
  [TopologicalSpace F] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] {f : E → F}
  (hf : AEMeasurable (fun x => ‖f x‖ₑ) μ) {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm (TauCeti.maximalFunction μ f) p μ ≤
    (ENNReal.ofReal (2 * p.toReal * 2 ^ (p.toReal - 1) / (p.toReal - 1)) * 4 ^ Module.finrank ℝ E) ^
        (1 / p.toReal) *
      MeasureTheory.eLpNorm f p μ
```

**The Hardy–Littlewood maximal inequality, the strong-type `(p, p)` bound for `1 < p < ∞`, as an inequality between the integrals `∫⁻ ‖·‖ₑ ^ p`.** Formalized in Tau Ceti as [`TauCeti.lintegral_rpow_maximalFunction_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MaximalFunction.html#TauCeti.lintegral_rpow_maximalFunction_le).

```lean
TauCeti.lintegral_rpow_maximalFunction_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E]
  [FiniteDimensional ℝ E] [ENorm F] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] {f : E → F}
  (hf : AEMeasurable (fun x => ‖f x‖ₑ) μ) {p : ℝ} (hp : 1 < p) :
  ∫⁻ (x : E), TauCeti.maximalFunction μ f x ^ p ∂μ ≤
    ENNReal.ofReal (2 * p * 2 ^ (p - 1) / (p - 1)) * 4 ^ Module.finrank ℝ E *
      ∫⁻ (x : E), ‖f x‖ₑ ^ p ∂μ
```

**The Hardy–Littlewood maximal inequality, the weak-type `(1,1)` bound.** Formalized in Tau Ceti as [`TauCeti.mul_measure_lt_maximalFunction_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MaximalFunction.html#TauCeti.mul_measure_lt_maximalFunction_le).

```lean
TauCeti.mul_measure_lt_maximalFunction_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E]
  [FiniteDimensional ℝ E] [ENorm F] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] (f : E → F)
  (t : ENNReal) :
  t * μ {x | t < TauCeti.maximalFunction μ f x} ≤ 4 ^ Module.finrank ℝ E * ∫⁻ (x : E), ‖f x‖ₑ ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.measure_lt_maximalFunction_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/MaximalFunction.html#TauCeti.measure_lt_maximalFunction_le)
- [Source of `TauCeti.measure_lt_maximalFunction_le` in TauCeti/MeasureTheory/Integral/MaximalFunction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/MaximalFunction.lean#L396)
