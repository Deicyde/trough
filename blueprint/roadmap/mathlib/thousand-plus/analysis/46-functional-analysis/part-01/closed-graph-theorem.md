---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: LinearMap.continuous_of_isClosed_graph
mathlib_file: Mathlib/Analysis/Normed/Operator/Banach.lean
---

# Closed graph theorem

The **closed graph theorem** : a linear map between two Banach spaces whose graph is closed
is continuous.

```lean
LinearMap.continuous_of_isClosed_graph.{u_1, u_3, u_5} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_3} [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] {F : Type u_5}
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F] (g : E →ₗ[𝕜] F)
  (hg : IsClosed ↑g.graph) : Continuous ⇑g
```

## Depends on

- [Completeness](../../../../overview/topology/uniform-notions/completeness.md)
- [Continuous function](../../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Induced topology](../../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)

## Proof depends on

- [Ordered ring](../../../../overview/general-algebra/rings/ordered-ring.md)
- [Range of a linear map](../../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `LinearMap.continuous_of_isClosed_graph`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Operator/Banach.html#LinearMap.continuous_of_isClosed_graph)
- [Source of `LinearMap.continuous_of_isClosed_graph` in Mathlib/Analysis/Normed/Operator/Banach.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Operator/Banach.lean#L536)
- [1000+ theorems list: Q1068085](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1309)
- [1000+ theorems project: Q1068085](https://1000-plus.github.io/?length=-1#Q1068085)
- [Wikipedia: Closed graph theorem](https://en.wikipedia.org/wiki/Closed_graph_theorem)
- [Wikidata: Q1068085](https://www.wikidata.org/wiki/Q1068085)
