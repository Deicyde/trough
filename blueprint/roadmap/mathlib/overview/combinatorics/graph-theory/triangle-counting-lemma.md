---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: SimpleGraph.triangle_counting
mathlib_file: Mathlib/Combinatorics/SimpleGraph/Triangle/Counting.lean
---

# Triangle counting lemma

The **Triangle Counting Lemma**. If `G` is a graph and `s`, `t`, `u` are disjoint sets of
vertices such that each pair is `ε`-uniform and `2 * ε`-dense, then `G` contains at least
`(1 - 2 * ε) * ε ^ 3 * |s| * |t| * |u|` triangles.

```lean
SimpleGraph.triangle_counting.{u_1} {α : Type u_1} (G : SimpleGraph α) [DecidableRel G.Adj] {ε : ℝ}
  {s t u : Finset α} [DecidableEq α] [Fintype α] (dst : 2 * ε ≤ ↑(G.edgeDensity s t))
  (ust : G.IsUniform ε s t) (hst : Disjoint s t) (dsu : 2 * ε ≤ ↑(G.edgeDensity s u))
  (usu : G.IsUniform ε s u) (hsu : Disjoint s u) (dtu : 2 * ε ≤ ↑(G.edgeDensity t u))
  (utu : G.IsUniform ε t u) (htu : Disjoint t u) :
  (1 - 2 * ε) * ε ^ 3 * ↑s.card * ↑t.card * ↑u.card ≤ ↑(G.cliqueFinset 3).card
```

## Depends on

- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Simple graph](simple-graph.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `SimpleGraph.triangle_counting`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Triangle/Counting.html#SimpleGraph.triangle_counting)
- [Source of `SimpleGraph.triangle_counting` in Mathlib/Combinatorics/SimpleGraph/Triangle/Counting.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/Triangle/Counting.lean#L149)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L531)
