# Heine-Borel theorem (proper metric space version)

The **Heine–Borel theorem**:
In a proper metric space, a set is compact if and only if it is closed and bounded.

```lean
Metric.isCompact_iff_isClosed_bounded.{u_2} {α : Type u_2} {s : Set α} [MetricSpace α]
  [ProperSpace α] : IsCompact s ↔ IsClosed s ∧ Bornology.IsBounded s
```

The 1000+ list (Q253214) also cites `FiniteDimensional.proper`.

## Depends on

- [Compactness in terms of filters](../general-topology/part-01/compactness-in-terms-of-filters.md)
- [Metric space](metric-space.md)

## Proof depends on

- [Ball](ball.md)
- [Hausdorff space](../general-topology/part-01/hausdorff-space.md)

## Sources

- [Mathlib documentation: `Metric.isCompact_iff_isClosed_bounded`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Bounded.html#Metric.isCompact_iff_isClosed_bounded)
- [Source of `Metric.isCompact_iff_isClosed_bounded` in Mathlib/Topology/MetricSpace/Bounded.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/MetricSpace/Bounded.lean#L332)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L263)
- [Mathlib undergraduate list: Single Variable Real Analysis › Topology of R](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L293)
- [1000+ theorems list: Q253214](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L278)
- [1000+ theorems project: Q253214](https://1000-plus.github.io/all.html?length=-1#Q253214)
- [Wikipedia: Heine–Borel theorem](https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem)
- [Wikidata: Q253214](https://www.wikidata.org/wiki/Q253214)
