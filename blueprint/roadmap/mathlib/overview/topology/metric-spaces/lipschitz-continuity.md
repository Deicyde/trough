---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: LipschitzWith
mathlib_file: Mathlib/Topology/EMetricSpace/Lipschitz.lean
---

# Lipschitz continuity

A function `f` is **Lipschitz continuous** with constant `K ≥ 0` if for all `x, y`
we have `dist (f x) (f y) ≤ K * dist x y`.

```lean
LipschitzWith.{u, v} {α : Type u} {β : Type v} [PseudoEMetricSpace α] [PseudoEMetricSpace β]
  (K : NNReal) (f : α → β) : Prop
```

## Depends on

- [Induced topology](../general-topology/part-01/induced-topology.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Uniform space](../uniform-notions/uniform-space.md)

## Sources

- [Mathlib documentation: `LipschitzWith`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/EMetricSpace/Lipschitz.html#LipschitzWith)
- [Source of `LipschitzWith` in Mathlib/Topology/EMetricSpace/Lipschitz.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/EMetricSpace/Lipschitz.lean#L57)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L264)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L417)
