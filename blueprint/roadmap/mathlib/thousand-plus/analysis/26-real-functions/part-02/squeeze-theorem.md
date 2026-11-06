---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: tendsto_of_tendsto_of_tendsto_of_le_of_le'
mathlib_file: Mathlib/Topology/Order/Basic.lean
---

# Squeeze theorem

**Squeeze theorem** (also known as **sandwich theorem**). This version assumes that inequalities
hold eventually for the filter.

```lean
tendsto_of_tendsto_of_tendsto_of_le_of_le'.{u, v} {α : Type u} {β : Type v}
  [ts : TopologicalSpace α] [Preorder α] [OrderTopology α] {f g h : β → α} {b : Filter β} {a : α}
  (hg : Filter.Tendsto g b (nhds a)) (hh : Filter.Tendsto h b (nhds a))
  (hgf : ∀ᶠ (b : β) in b, g b ≤ f b) (hfh : ∀ᶠ (b : β) in b, f b ≤ h b) :
  Filter.Tendsto f b (nhds a)
```

## Depends on

- [Limit of a map with respect to filters](../../../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Order topology](../../../../overview/topology/topological-algebra/order-topology.md)

## Proof depends on

- [Natural number](../../../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `tendsto_of_tendsto_of_tendsto_of_le_of_le'`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/Basic.html#tendsto_of_tendsto_of_tendsto_of_le_of_le')
- [Source of `tendsto_of_tendsto_of_tendsto_of_le_of_le'` in Mathlib/Topology/Order/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Order/Basic.lean#L217)
- [1000+ theorems list: Q1065257](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1287)
- [1000+ theorems project: Q1065257](https://1000-plus.github.io/all.html?length=-1#Q1065257)
- [Wikipedia: Squeeze theorem](https://en.wikipedia.org/wiki/Squeeze_theorem)
- [Wikidata: Q1065257](https://www.wikidata.org/wiki/Q1065257)
