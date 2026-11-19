---
declaration: theorem
origin: cited
lean: SimpleGraph.card_oddTriangleFinset_add_sum_degree_sq
statement: formalized
proof: formalized
---

# Kozlov's odd-triangle identity

in a `3`-clique-free finite graph, the number of `3`-vertex
subsets spanning an odd number of edges plus the sum of squared vertex degrees equals
`Fintype.card V * #G.edgeFinset` (Kozlov, arXiv:1610.07136v2, equation (2.5)).

```lean
SimpleGraph.card_oddTriangleFinset_add_sum_degree_sq.{u_1} {V : Type u_1} [Fintype V]
  [DecidableEq V] {G : SimpleGraph V} [DecidableRel G.Adj] (hG : G.CliqueFree 3) :
  G.oddTriangleFinset.card + ∑ v, G.degree v ^ 2 = Fintype.card V * G.edgeFinset.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.card_oddTriangleFinset_add_sum_degree_sq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/OddTriangles.html#SimpleGraph.card_oddTriangleFinset_add_sum_degree_sq).

## Sources

- [Tau Ceti documentation: `SimpleGraph.card_oddTriangleFinset_add_sum_degree_sq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/OddTriangles.html#SimpleGraph.card_oddTriangleFinset_add_sum_degree_sq)
- [Source of `SimpleGraph.card_oddTriangleFinset_add_sum_degree_sq` in TauCeti/Combinatorics/SimpleGraph/OddTriangles.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/SimpleGraph/OddTriangles.lean#L330)
