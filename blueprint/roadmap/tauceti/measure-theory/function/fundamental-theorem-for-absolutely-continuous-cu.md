---
declaration: theorem
origin: cited
lean: AbsolutelyContinuousOnInterval.lintegral_metricDerivative_lt_top, AbsolutelyContinuousOnInterval.ae_tendsto_metricDerivative, AbsolutelyContinuousOnInterval.edist_le_lintegral_metricDerivative
statement: formalized
proof: formalized
---

# Fundamental theorem for absolutely continuous curves, integrability

the metric derivative
of an absolutely continuous curve on `[a, b]` has finite integral over `[a, b]`.

```lean
AbsolutelyContinuousOnInterval.lintegral_metricDerivative_lt_top.{u_1} {X : Type u_1}
  [PseudoMetricSpace X] {γ : ℝ → X} {a b : ℝ} (hγ : AbsolutelyContinuousOnInterval γ a b) :
  ∫⁻ (r : ℝ) in Set.uIoc a b, TauCeti.metricDerivative γ r < ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbsolutelyContinuousOnInterval.lintegral_metricDerivative_lt_top`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/MetricDerivative/Basic.html#AbsolutelyContinuousOnInterval.lintegral_metricDerivative_lt_top).

## Other forms

**Fundamental theorem for absolutely continuous curves, existence of the metric derivative.** Formalized in Tau Ceti as [`AbsolutelyContinuousOnInterval.ae_tendsto_metricDerivative`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/MetricDerivative/Basic.html#AbsolutelyContinuousOnInterval.ae_tendsto_metricDerivative).

```lean
AbsolutelyContinuousOnInterval.ae_tendsto_metricDerivative.{u_1} {X : Type u_1}
  [PseudoMetricSpace X] {γ : ℝ → X} {a b : ℝ} (hγ : AbsolutelyContinuousOnInterval γ a b) :
  ∀ᵐ (t : ℝ),
    t ∈ Set.uIcc a b →
      Filter.Tendsto (fun s => edist (γ s) (γ t) / edist s t) (nhdsWithin t {t}ᶜ)
        (nhds (TauCeti.metricDerivative γ t))
```

**Fundamental theorem for absolutely continuous curves, the distance bound.** Formalized in Tau Ceti as [`AbsolutelyContinuousOnInterval.edist_le_lintegral_metricDerivative`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/MetricDerivative/Basic.html#AbsolutelyContinuousOnInterval.edist_le_lintegral_metricDerivative).

```lean
AbsolutelyContinuousOnInterval.edist_le_lintegral_metricDerivative.{u_1} {X : Type u_1}
  [PseudoMetricSpace X] {γ : ℝ → X} {a b : ℝ} (hγ : AbsolutelyContinuousOnInterval γ a b) {s u : ℝ}
  (hs : s ∈ Set.uIcc a b) (hu : u ∈ Set.uIcc a b) :
  edist (γ s) (γ u) ≤ ∫⁻ (r : ℝ) in Set.uIoc s u, TauCeti.metricDerivative γ r
```

## Sources

- [Tau Ceti documentation: `AbsolutelyContinuousOnInterval.lintegral_metricDerivative_lt_top`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/MetricDerivative/Basic.html#AbsolutelyContinuousOnInterval.lintegral_metricDerivative_lt_top)
- [Source of `AbsolutelyContinuousOnInterval.lintegral_metricDerivative_lt_top` in TauCeti/MeasureTheory/Function/MetricDerivative/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/MetricDerivative/Basic.lean#L373)
