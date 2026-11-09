# Extreme value theorem

The **extreme value theorem**: a continuous function realizes its minimum on a compact set.

```lean
IsCompact.exists_isMinOn.{u_2, u_3} {α : Type u_2} {β : Type u_3} [LinearOrder α]
  [TopologicalSpace α] [TopologicalSpace β] [ClosedIicTopology α] {s : Set β} (hs : IsCompact s)
  (ne_s : s.Nonempty) {f : β → α} (hf : ContinuousOn f s) : ∃ x ∈ s, IsMinOn f s x
```

## Depends on

- [Compactness in terms of filters](../general-topology/part-01/compactness-in-terms-of-filters.md)
- [Limit of a map with respect to filters](../general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Sources

- [Mathlib documentation: `IsCompact.exists_isMinOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/Compact.html#IsCompact.exists_isMinOn)
- [Source of `IsCompact.exists_isMinOn` in Mathlib/Topology/Order/Compact.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Order/Compact.lean#L254)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L249)
- [1000+ theorems list: Q752375](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L839)
- [1000+ theorems project: Q752375](https://1000-plus.github.io/all.html?length=-1#Q752375)
- [Wikipedia: Extreme value theorem](https://en.wikipedia.org/wiki/Extreme_value_theorem)
- [Wikidata: Q752375](https://www.wikidata.org/wiki/Q752375)
