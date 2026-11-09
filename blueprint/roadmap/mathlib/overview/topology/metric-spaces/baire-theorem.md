# Baire theorem

**First Baire theorem**: a completely pseudometrizable topological space has Baire property.

```lean
BaireSpace.of_completelyPseudoMetrizable.{u_1} {X : Type u_1} [TopologicalSpace X]
  [TopologicalSpace.IsCompletelyPseudoMetrizableSpace X] : BaireSpace X
```

The 1000+ list (Q1052678) also cites `BaireSpace.of_t2Space_locallyCompactSpace`.

## Depends on

- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Closure](../general-topology/part-01/closure.md)
- [Completeness](../uniform-notions/completeness.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Sum of a Geometric Series](../../../hundred-theorems/part-03/sum-of-a-geometric-series.md)

## Sources

- [Mathlib documentation: `BaireSpace.of_completelyPseudoMetrizable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Baire/CompleteMetrizable.html#BaireSpace.of_completelyPseudoMetrizable)
- [Source of `BaireSpace.of_completelyPseudoMetrizable` in Mathlib/Topology/Baire/CompleteMetrizable.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Baire/CompleteMetrizable.lean#L25)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L267)
- [1000+ theorems list: Q1052678](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1254)
- [1000+ theorems project: Q1052678](https://1000-plus.github.io/all.html?length=-1#Q1052678)
- [Wikipedia: Baire category theorem](https://en.wikipedia.org/wiki/Baire_category_theorem)
- [Wikidata: Q1052678](https://www.wikidata.org/wiki/Q1052678)
