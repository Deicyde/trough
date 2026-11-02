---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: SimpleGraph
mathlib_file: Mathlib/Combinatorics/SimpleGraph/Basic.lean
---

# Simple graph

A simple graph is an irreflexive symmetric relation `Adj` on a vertex type `V`.
The relation describes which pairs of vertices are adjacent.
There is exactly one edge for every pair of adjacent vertices;
see `SimpleGraph.edgeSet` for the corresponding edge set.

```lean
SimpleGraph.{u} (V : Type u) : Type u
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `SimpleGraph`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Basic.html#SimpleGraph)
- [Source of `SimpleGraph` in Mathlib/Combinatorics/SimpleGraph/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/Basic.lean#L87)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L523)
