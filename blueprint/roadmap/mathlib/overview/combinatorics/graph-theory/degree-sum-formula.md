---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: SimpleGraph.sum_degrees_eq_twice_card_edges
mathlib_file: Mathlib/Combinatorics/SimpleGraph/DegreeSum.lean
---

# Degree-sum formula

The degree-sum formula.  This is also known as the handshaking lemma, which might
more specifically refer to `SimpleGraph.even_card_odd_degree_vertices`.

```lean
SimpleGraph.sum_degrees_eq_twice_card_edges.{u} {V : Type u} (G : SimpleGraph V) [Fintype V]
  [DecidableRel G.Adj] : ∑ v, G.degree v = 2 * G.edgeFinset.card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)
- [Simple graph](simple-graph.md)

## Sources

- [Mathlib documentation: `SimpleGraph.sum_degrees_eq_twice_card_edges`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/DegreeSum.html#SimpleGraph.sum_degrees_eq_twice_card_edges)
- [Source of `SimpleGraph.sum_degrees_eq_twice_card_edges` in Mathlib/Combinatorics/SimpleGraph/DegreeSum.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/DegreeSum.lean#L99)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L524)
