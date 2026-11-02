---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.lintegral_liminf_le
mathlib_file: Mathlib/MeasureTheory/Integral/Lebesgue/Add.lean
---

# Fatou's lemma

**Fatou's lemma**, version with `Measurable` functions.

```lean
MeasureTheory.lintegral_liminf_le.{u_1, u_3} {α : Type u_1} {m : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} {ι : Type u_3} {f : ι → α → ENNReal} {u : Filter ι}
  [u.IsCountablyGenerated] (h_meas : ∀ (i : ι), Measurable (f i)) :
  ∫⁻ (a : α), Filter.liminf (fun i => f i a) u ∂μ ≤ Filter.liminf (fun i => ∫⁻ (a : α), f i a ∂μ) u
```

## Depends on

- [Integral of positive measurable functions](integral-of-positive-measurable-functions.md)
- [Measurable function](measurable-function.md)

## Proof depends on

- [Almost sure convergence](../../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Borel sigma-algebra](borel-sigma-algebra.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Cluster point](../../../topology/general-topology/part-01/cluster-point.md)
- [Induced topology](../../../topology/general-topology/part-01/induced-topology.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `MeasureTheory.lintegral_liminf_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Lebesgue/Add.html#MeasureTheory.lintegral_liminf_le)
- [Source of `MeasureTheory.lintegral_liminf_le` in Mathlib/MeasureTheory/Integral/Lebesgue/Add.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/Lebesgue/Add.lean#L236)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L349)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L515)
- [1000+ theorems list: Q5437947](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3178)
- [1000+ theorems project: Q5437947](https://1000-plus.github.io/?length=-1#Q5437947)
- [Wikipedia: Fatou–Lebesgue theorem](https://en.wikipedia.org/wiki/Fatou%E2%80%93Lebesgue_theorem)
- [Wikidata: Q5437947](https://www.wikidata.org/wiki/Q5437947)
