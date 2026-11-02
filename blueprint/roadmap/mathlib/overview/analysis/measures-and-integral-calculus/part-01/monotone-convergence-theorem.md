---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.lintegral_iInf_ae
mathlib_file: Mathlib/MeasureTheory/Integral/Lebesgue/Sub.lean
---

# Monotone convergence theorem

**Monotone convergence theorem** for nonincreasing sequences of functions.

```lean
MeasureTheory.lintegral_iInf_ae.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {f : ℕ → α → ENNReal} (h_meas : ∀ (n : ℕ), Measurable (f n))
  (h_mono : ∀ (n : ℕ), f n.succ ≤ᵐ[μ] f n) (h_fin : ∫⁻ (a : α), f 0 a ∂μ ≠ ⊤) :
  ∫⁻ (a : α), ⨅ n, f n a ∂μ = ⨅ n, ∫⁻ (a : α), f n a ∂μ
```

## Depends on

- [Almost sure convergence](../../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Integral of positive measurable functions](integral-of-positive-measurable-functions.md)
- [Measurable function](measurable-function.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](borel-sigma-algebra.md)
- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity of inverse functions](../../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-inverse-functions.md)
- [Continuity of monotone functions](../../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Hausdorff space](../../../topology/general-topology/part-01/hausdorff-space.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Linear map](../../../linear-algebra/fundamentals/linear-map.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Open map](../../../topology/general-topology/part-01/open-map.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../../topology/topological-algebra/topological-ring.md)
- [Uniformly continuous function](../../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `MeasureTheory.lintegral_iInf_ae`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Lebesgue/Sub.html#MeasureTheory.lintegral_iInf_ae)
- [Source of `MeasureTheory.lintegral_iInf_ae` in Mathlib/MeasureTheory/Integral/Lebesgue/Sub.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/Lebesgue/Sub.lean#L55)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L348)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L514)
