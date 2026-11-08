---
declaration: def
origin: cited
lean: SimpleGraph.walkEquivOfSimpleGraph
statement: formalized
---

# SimpleGraph.walkEquivOfSimpleGraph

Walks in a simple graph are equivalent to edge-labelled walks in its associated `Graph`.

```lean
SimpleGraph.walkEquivOfSimpleGraph.{u} {α : Type u} (H : SimpleGraph α) (x y : α) :
  H.Walk x y ≃ (Graph.ofSimpleGraph H).Walk x y
```

## Depends on

- [Graph.Walk](graph-walk.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.walkEquivOfSimpleGraph`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Walk/OfSimpleGraph.html#SimpleGraph.walkEquivOfSimpleGraph).

## Sources

- [Tau Ceti documentation: `SimpleGraph.walkEquivOfSimpleGraph`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Walk/OfSimpleGraph.html#SimpleGraph.walkEquivOfSimpleGraph)
- [Source of `SimpleGraph.walkEquivOfSimpleGraph` in TauCeti/Combinatorics/Graph/Connectivity/Walk/OfSimpleGraph.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Connectivity/Walk/OfSimpleGraph.lean#L184)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
