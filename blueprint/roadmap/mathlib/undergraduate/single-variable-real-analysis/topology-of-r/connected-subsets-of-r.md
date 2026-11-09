# Connected subsets of $\R$

In a dense conditionally complete linear order, the set of preconnected sets is exactly
the set of the intervals `Icc`, `Ico`, `Ioc`, `Ioo`, `Ici`, `Ioi`, `Iic`, `Iio`, `(-∞, +∞)`,
or `∅`. Though one can represent `∅` as `(sInf s, sInf s)`, we include it into the list of
possible cases to improve readability.

```lean
setOfPred_isPreconnected_eq_of_ordered.{u} {α : Type u} [TopologicalSpace α]
  [ConditionallyCompleteLinearOrder α] [OrderTopology α] [DenselyOrdered α] :
  {s | IsPreconnected s} =
    Set.range (Function.uncurry Set.Icc) ∪ Set.range (Function.uncurry Set.Ico) ∪
          Set.range (Function.uncurry Set.Ioc) ∪
        Set.range (Function.uncurry Set.Ioo) ∪
      (Set.range Set.Ici ∪ Set.range Set.Ioi ∪ Set.range Set.Iic ∪ Set.range Set.Iio ∪
        {Set.univ, ∅})
```

## Depends on

- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)

## Proof depends on

- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Limit of a map with respect to filters](../../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Sources

- [Mathlib documentation: `setOfPred_isPreconnected_eq_of_ordered`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/IntermediateValue.html#setOfPred_isPreconnected_eq_of_ordered)
- [Source of `setOfPred_isPreconnected_eq_of_ordered` in Mathlib/Topology/Order/IntermediateValue.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Order/IntermediateValue.lean#L541)
- [Mathlib undergraduate list: Single Variable Real Analysis › Topology of R](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L294)
