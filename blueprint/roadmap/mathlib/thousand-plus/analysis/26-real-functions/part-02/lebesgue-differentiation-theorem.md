---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: VitaliFamily.ae_tendsto_lintegral_div
mathlib_file: Mathlib/MeasureTheory/Covering/Differentiation.lean
---

# Lebesgue differentiation theorem

Mathlib states this as `VitaliFamily.ae_tendsto_lintegral_div`.

```lean
VitaliFamily.ae_tendsto_lintegral_div.{u_1} {α : Type u_1} [PseudoMetricSpace α]
  {m0 : MeasurableSpace α} {μ : MeasureTheory.Measure α} (v : VitaliFamily μ)
  [SecondCountableTopology α] [BorelSpace α] [MeasureTheory.IsLocallyFiniteMeasure μ]
  {f : α → ENNReal} (hf : AEMeasurable f μ) (h'f : ∫⁻ (y : α), f y ∂μ ≠ ⊤) :
  ∀ᵐ (x : α) ∂μ,
    Filter.Tendsto (fun a => (∫⁻ (y : α) in a, f y ∂μ) / μ a) (v.filterAt x) (nhds (f x))
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Bornology](../../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Carathéodory's theorem (measure theory)](../../28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Integral of positive measurable functions](../../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Order (Real numbers)](../../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Lebesgue's decomposition theorem](../../../geometry-and-topology/54-general-topology/part-01/lebesgues-decomposition-theorem.md)

## Sources

- [Mathlib documentation: `VitaliFamily.ae_tendsto_lintegral_div`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Covering/Differentiation.html#VitaliFamily.ae_tendsto_lintegral_div)
- [Source of `VitaliFamily.ae_tendsto_lintegral_div` in Mathlib/MeasureTheory/Covering/Differentiation.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Covering/Differentiation.lean#L725)
- [1000+ theorems list: Q2275191](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2150)
- [1000+ theorems project: Q2275191](https://1000-plus.github.io/all.html?length=-1#Q2275191)
- [Wikipedia: Lebesgue differentiation theorem](https://en.wikipedia.org/wiki/Lebesgue_differentiation_theorem)
- [Wikidata: Q2275191](https://www.wikidata.org/wiki/Q2275191)
