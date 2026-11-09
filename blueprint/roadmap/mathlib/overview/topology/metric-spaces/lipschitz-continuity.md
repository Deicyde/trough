# Lipschitz continuity

A function `f` is **Lipschitz continuous** with constant `K ≥ 0` if for all `x, y`
we have `dist (f x) (f y) ≤ K * dist x y`.

```lean
LipschitzWith.{u, v} {α : Type u} {β : Type v} [PseudoEMetricSpace α] [PseudoEMetricSpace β]
  (K : NNReal) (f : α → β) : Prop
```

## Depends on

- [Real number](../../general-algebra/numbers/real-number.md)

## Sources

- [Mathlib documentation: `LipschitzWith`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/EMetricSpace/Lipschitz.html#LipschitzWith)
- [Source of `LipschitzWith` in Mathlib/Topology/EMetricSpace/Lipschitz.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/EMetricSpace/Lipschitz.lean#L57)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L264)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L417)
