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
- [Metric space](../../../topology/metric-spaces/metric-space.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)
- [Ordered ring](../../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `MeasureTheory.lintegral_liminf_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Lebesgue/Add.html#MeasureTheory.lintegral_liminf_le)
- [Source of `MeasureTheory.lintegral_liminf_le` in Mathlib/MeasureTheory/Integral/Lebesgue/Add.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Integral/Lebesgue/Add.lean#L236)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L349)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L515)
- [1000+ theorems list: Q5437947](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L3178)
- [1000+ theorems project: Q5437947](https://1000-plus.github.io/all.html?length=-1#Q5437947)
- [Wikipedia: Fatou–Lebesgue theorem](https://en.wikipedia.org/wiki/Fatou%E2%80%93Lebesgue_theorem)
- [Wikidata: Q5437947](https://www.wikidata.org/wiki/Q5437947)
