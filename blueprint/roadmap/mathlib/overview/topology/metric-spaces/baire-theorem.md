---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: BaireSpace.of_completelyPseudoMetrizable, BaireSpace.of_t2Space_locallyCompactSpace
mathlib_file: Mathlib/Topology/Baire/CompleteMetrizable.lean
---

# Baire theorem

Mathlib records this with 2 declarations.

`BaireSpace.of_completelyPseudoMetrizable`: **First Baire theorem**: a completely pseudometrizable topological space has Baire property.

```lean
BaireSpace.of_completelyPseudoMetrizable.{u_1} {X : Type u_1} [TopologicalSpace X]
  [TopologicalSpace.IsCompletelyPseudoMetrizableSpace X] : BaireSpace X
```

`BaireSpace.of_t2Space_locallyCompactSpace`: **Second Baire theorem**: locally compact R₁ spaces are Baire.

```lean
BaireSpace.of_t2Space_locallyCompactSpace.{u_1} {X : Type u_1} [TopologicalSpace X] [R1Space X]
  [LocallyCompactSpace X] : BaireSpace X
```

## Depends on

- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Closure](../general-topology/part-01/closure.md)
- [Compactness in terms of filters](../general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness](../uniform-notions/completeness.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Cauchy sequence](../uniform-notions/cauchy-sequence.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Open map](../general-topology/part-01/open-map.md)
- [Sum of a Geometric Series](../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [Topological module](../topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `BaireSpace.of_completelyPseudoMetrizable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Baire/CompleteMetrizable.html#BaireSpace.of_completelyPseudoMetrizable)
- [Source of `BaireSpace.of_completelyPseudoMetrizable` in Mathlib/Topology/Baire/CompleteMetrizable.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Baire/CompleteMetrizable.lean#L25)
- [Mathlib documentation: `BaireSpace.of_t2Space_locallyCompactSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Baire/LocallyCompactRegular.html#BaireSpace.of_t2Space_locallyCompactSpace)
- [Source of `BaireSpace.of_t2Space_locallyCompactSpace` in Mathlib/Topology/Baire/LocallyCompactRegular.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Baire/LocallyCompactRegular.lean#L22)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L267)
- [1000+ theorems list: Q1052678](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1254)
- [1000+ theorems project: Q1052678](https://1000-plus.github.io/?length=-1#Q1052678)
- [Wikipedia: Baire category theorem](https://en.wikipedia.org/wiki/Baire_category_theorem)
- [Wikidata: Q1052678](https://www.wikidata.org/wiki/Q1052678)
