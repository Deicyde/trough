# Intermediate value theorem

**Intermediate Value Theorem** for continuous functions on closed intervals, case
`f a ≤ t ≤ f b`.

```lean
intermediate_value_Icc.{u, u_1} {α : Type u} [TopologicalSpace α]
  [ConditionallyCompleteLinearOrder α] [OrderTopology α] [DenselyOrdered α] {δ : Type u_1}
  [LinearOrder δ] [TopologicalSpace δ] [OrderClosedTopology δ] {a b : α} (hab : a ≤ b) {f : α → δ}
  (hf : ContinuousOn f (Set.Icc a b)) : Set.Icc (f a) (f b) ⊆ f '' Set.Icc a b
```

## Depends on

- [Limit of a map with respect to filters](../general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Order topology](order-topology.md)

## Proof depends on

- [Closure](../general-topology/part-01/closure.md)
- [Continuous function](../general-topology/part-01/continuous-function.md)

## Sources

- [Mathlib documentation: `intermediate_value_Icc`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/IntermediateValue.html#intermediate_value_Icc)
- [Source of `intermediate_value_Icc` in Mathlib/Topology/Order/IntermediateValue.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Order/IntermediateValue.lean#L584)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L248)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real-valued functions defined on a subset of $\R$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L309)
- [Freek Wiedijk's 100 theorems, no. 79](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L401)
- [1000+ theorems list: Q245098](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L263)
- [1000+ theorems project: Q245098](https://1000-plus.github.io/all.html?length=-1#Q245098)
- [Wikipedia: Intermediate value theorem](https://en.wikipedia.org/wiki/Intermediate_value_theorem)
- [Wikidata: Q245098](https://www.wikidata.org/wiki/Q245098)
