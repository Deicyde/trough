---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.integral_tendsto_of_tendsto_of_antitone, MeasureTheory.lintegral_tendsto_of_tendsto_of_monotone
mathlib_file: Mathlib/MeasureTheory/Integral/Bochner/Basic.lean
---

# Monotone convergence theorem

Mathlib records this with 2 declarations.

`MeasureTheory.integral_tendsto_of_tendsto_of_antitone`: Monotone convergence theorem for real-valued functions and Bochner integrals

```lean
MeasureTheory.integral_tendsto_of_tendsto_of_antitone.{u_1} {α : Type u_1} {m : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {f : ℕ → α → ℝ} {F : α → ℝ}
  (hf : ∀ (n : ℕ), MeasureTheory.Integrable (f n) μ) (hF : MeasureTheory.Integrable F μ)
  (h_mono : ∀ᵐ (x : α) ∂μ, Antitone fun n => f n x)
  (h_tendsto : ∀ᵐ (x : α) ∂μ, Filter.Tendsto (fun n => f n x) Filter.atTop (nhds (F x))) :
  Filter.Tendsto (fun n => ∫ (x : α), f n x ∂μ) Filter.atTop (nhds (∫ (x : α), F x ∂μ))
```

`MeasureTheory.lintegral_tendsto_of_tendsto_of_monotone`: **Monotone convergence theorem** expressed with limits.

```lean
MeasureTheory.lintegral_tendsto_of_tendsto_of_monotone.{u_1} {α : Type u_1} {m : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {f : ℕ → α → ENNReal} {F : α → ENNReal}
  (hf : ∀ (n : ℕ), AEMeasurable (f n) μ) (h_mono : ∀ᵐ (x : α) ∂μ, Monotone fun n => f n x)
  (h_tendsto : ∀ᵐ (x : α) ∂μ, Filter.Tendsto (fun n => f n x) Filter.atTop (nhds (F x))) :
  Filter.Tendsto (fun n => ∫⁻ (x : α), f n x ∂μ) Filter.atTop (nhds (∫⁻ (x : α), F x ∂μ))
```

## Depends on

- [Bochner integral](../../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Approximation by step functions](../../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../../overview/topology/general-topology/part-01/closed-map.md)
- [Fatou's lemma](../../../../overview/analysis/measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Monotone convergence theorem](../../../../overview/analysis/measures-and-integral-calculus/part-01/monotone-convergence-theorem.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)

## Sources

- [Mathlib documentation: `MeasureTheory.integral_tendsto_of_tendsto_of_antitone`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Bochner/Basic.html#MeasureTheory.integral_tendsto_of_tendsto_of_antitone)
- [Source of `MeasureTheory.integral_tendsto_of_tendsto_of_antitone` in Mathlib/MeasureTheory/Integral/Bochner/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/Bochner/Basic.lean#L839)
- [Mathlib documentation: `MeasureTheory.lintegral_tendsto_of_tendsto_of_monotone`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Lebesgue/Add.html#MeasureTheory.lintegral_tendsto_of_tendsto_of_monotone)
- [Source of `MeasureTheory.lintegral_tendsto_of_tendsto_of_monotone` in Mathlib/MeasureTheory/Integral/Lebesgue/Add.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/Lebesgue/Add.lean#L117)
- [1000+ theorems list: Q1153584](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1466)
- [1000+ theorems project: Q1153584](https://1000-plus.github.io/?length=-1#Q1153584)
- [Wikipedia: Monotone convergence theorem](https://en.wikipedia.org/wiki/Monotone_convergence_theorem)
- [Wikidata: Q1153584](https://www.wikidata.org/wiki/Q1153584)
