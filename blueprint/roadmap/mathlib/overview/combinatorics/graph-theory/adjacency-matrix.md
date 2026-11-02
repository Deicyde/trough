---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: SimpleGraph.adjMatrix
mathlib_file: Mathlib/Combinatorics/SimpleGraph/AdjMatrix.lean
---

# Adjacency matrix

`adjMatrix G α` is the matrix `A` such that `A i j = (1 : α)` if `i` and `j` are
adjacent in the simple graph `G`, and otherwise `A i j = 0`.

```lean
SimpleGraph.adjMatrix.{u_1, u_2} (α : Type u_1) {V : Type u_2} (G : SimpleGraph V)
  [DecidableRel G.Adj] [Zero α] [One α] : Matrix V V α
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Ring-valued matrix](../../linear-algebra/matrices/ring-valued-matrix.md)
- [Simple graph](simple-graph.md)

## Sources

- [Mathlib documentation: `SimpleGraph.adjMatrix`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/AdjMatrix.html#SimpleGraph.adjMatrix)
- [Source of `SimpleGraph.adjMatrix` in Mathlib/Combinatorics/SimpleGraph/AdjMatrix.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/AdjMatrix.lean#L235)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L526)
