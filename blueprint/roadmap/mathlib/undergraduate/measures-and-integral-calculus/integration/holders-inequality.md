---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: NNReal.lintegral_mul_le_Lp_mul_Lq
mathlib_file: Mathlib/MeasureTheory/Integral/MeanInequalities.lean
---

# Hölder's inequality

Hölder's inequality for functions `α → ℝ≥0`. The integral of the product of two functions
is bounded by the product of their `ℒp` and `ℒq` seminorms when `p` and `q` are conjugate
exponents.

```lean
NNReal.lintegral_mul_le_Lp_mul_Lq.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {p q : ℝ} (hpq : p.HolderConjugate q) {f g : α → NNReal}
  (hf : AEMeasurable f μ) (hg : AEMeasurable g μ) :
  ∫⁻ (a : α), ↑((f * g) a) ∂μ ≤
    (∫⁻ (a : α), ↑(f a) ^ p ∂μ) ^ (1 / p) * (∫⁻ (a : α), ↑(g a) ^ q ∂μ) ^ (1 / q)
```

## Depends on

- [Almost sure convergence](../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Integral of positive measurable functions](../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Power functions](../../single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closed map](../../../overview/topology/general-topology/part-01/closed-map.md)
- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuity of inverse functions](../../single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-inverse-functions.md)
- [Continuity of monotone functions](../../single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-monotone-functions.md)
- [Limit point](../../single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)

## Sources

- [Mathlib documentation: `NNReal.lintegral_mul_le_Lp_mul_Lq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/MeanInequalities.html#NNReal.lintegral_mul_le_Lp_mul_Lq)
- [Source of `NNReal.lintegral_mul_le_Lp_mul_Lq` in Mathlib/MeasureTheory/Integral/MeanInequalities.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/MeanInequalities.lean#L479)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L523)
