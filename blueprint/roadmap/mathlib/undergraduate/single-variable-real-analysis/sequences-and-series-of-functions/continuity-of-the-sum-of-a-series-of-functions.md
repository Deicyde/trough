---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: continuous_tsum
mathlib_file: Mathlib/Analysis/Normed/Group/FunctionSeries.lean
---

# Continuity of the sum of a series of functions

An infinite sum of functions with summable sup norm is continuous if each individual
function is.

```lean
continuous_tsum.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2} {F : Type u_3} [NormedAddCommGroup F]
  [CompleteSpace F] {u : α → ℝ} [TopologicalSpace β] {f : α → β → F}
  (hf : ∀ (i : α), Continuous (f i)) (hu : Summable u) (hfu : ∀ (n : α) (x : β), ‖f n x‖ ≤ u n) :
  Continuous fun x => ∑' (n : α), f n x
```

## Depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `continuous_tsum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Group/FunctionSeries.html#continuous_tsum)
- [Source of `continuous_tsum` in Mathlib/Analysis/Normed/Group/FunctionSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Group/FunctionSeries.lean#L122)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L353)
