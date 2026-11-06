# Matching

The subgraph `M` of `G` is a matching if every vertex of `M` is incident to exactly one edge in `M`.
We say that the vertices in `M.support` are *matched* or *saturated*.

```lean
SimpleGraph.Subgraph.IsMatching.{u_1} {V : Type u_1} {G : SimpleGraph V} (M : G.Subgraph) : Prop
```

## Depends on

- [Set](../../data-structures/sets/set.md)
- [Simple graph](simple-graph.md)

## Sources

- [Mathlib documentation: `SimpleGraph.Subgraph.IsMatching`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Matching.html#SimpleGraph.Subgraph.IsMatching)
- [Source of `SimpleGraph.Subgraph.IsMatching` in Mathlib/Combinatorics/SimpleGraph/Matching.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/Matching.lean#L63)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L525)
