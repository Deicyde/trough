---
declaration: theorem
origin: cited
lean: SimpleGraph.IsBipartite.chromaticIndex_eq_maxDegree
statement: formalized
proof: formalized
---

# Kőnig's line-colouring theorem

The chromatic index of a finite bipartite simple graph
is its maximum degree. Both are zero when the vertex type is empty.

```lean
SimpleGraph.IsBipartite.chromaticIndex_eq_maxDegree.{u} {α : Type u} {H : SimpleGraph α} [Fintype α]
  [DecidableRel H.Adj] (hH : H.IsBipartite) : H.chromaticIndex = ↑H.maxDegree
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Kőnig's edge-colouring theorem](konigs-edge-colouring-theorem.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.IsBipartite.chromaticIndex_eq_maxDegree`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.html#SimpleGraph.IsBipartite.chromaticIndex_eq_maxDegree).

## Sources

- [Tau Ceti documentation: `SimpleGraph.IsBipartite.chromaticIndex_eq_maxDegree`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.html#SimpleGraph.IsBipartite.chromaticIndex_eq_maxDegree)
- [Source of `SimpleGraph.IsBipartite.chromaticIndex_eq_maxDegree` in TauCeti/Combinatorics/Graph/Matching/EdgeColoring.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.lean#L114)
