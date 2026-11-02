---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ContinuousOn.image_Icc
mathlib_file: Mathlib/Topology/Order/Compact.lean
---

# Image of a segment

Mathlib states this as `ContinuousOn.image_Icc`.

```lean
ContinuousOn.image_Icc.{u_2, u_3} {α : Type u_2} {β : Type u_3} [ConditionallyCompleteLinearOrder α]
  [TopologicalSpace α] [OrderTopology α] [TopologicalSpace β] [DenselyOrdered α]
  [ConditionallyCompleteLinearOrder β] [OrderTopology β] {f : α → β} {a b : α} (hab : a ≤ b)
  (h : ContinuousOn f (Set.Icc a b)) :
  f '' Set.Icc a b = Set.Icc (sInf (f '' Set.Icc a b)) (sSup (f '' Set.Icc a b))
```

## Depends on

- [Limit of a map with respect to filters](../../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)

## Proof depends on

- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)

## Sources

- [Mathlib documentation: `ContinuousOn.image_Icc`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/Compact.html#ContinuousOn.image_Icc)
- [Source of `ContinuousOn.image_Icc` in Mathlib/Topology/Order/Compact.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Order/Compact.lean#L546)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real-valued functions defined on a subset of $\R$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L310)
