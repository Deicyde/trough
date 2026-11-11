---
declaration: theorem
origin: cited
lean: SimpleGraph.chromaticNumber_lineGraph_eq_maxDegree
statement: formalized
proof: formalized
---

# Kőnig's line-colouring theorem for simple graphs

For a finite simple graph with a
displayed covering bipartition, the chromatic number of its line graph is its maximum degree.
The maximum degree, and hence the chromatic number, is zero on the empty vertex type.

```lean
SimpleGraph.chromaticNumber_lineGraph_eq_maxDegree.{u} {α : Type u} (H : SimpleGraph α) [Fintype α]
  [DecidableRel H.Adj] {L R : Finset ↑(Graph.ofSimpleGraph H).vertexSet}
  (hLR : (Graph.ofSimpleGraph H).IsBipartition L R) : H.lineGraph.chromaticNumber = ↑H.maxDegree
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kőnig's edge-colouring theorem](konigs-edge-colouring-theorem.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.chromaticNumber_lineGraph_eq_maxDegree`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.html#SimpleGraph.chromaticNumber_lineGraph_eq_maxDegree).

## Sources

- [Tau Ceti documentation: `SimpleGraph.chromaticNumber_lineGraph_eq_maxDegree`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.html#SimpleGraph.chromaticNumber_lineGraph_eq_maxDegree)
- [Source of `SimpleGraph.chromaticNumber_lineGraph_eq_maxDegree` in TauCeti/Combinatorics/Graph/Matching/EdgeColoring.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.lean#L108)
