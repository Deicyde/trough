---
declaration: inductive
origin: cited
lean: Graph.Walk
statement: formalized
---

# Graph.Walk

An edge-labelled walk in a multigraph. Each step records an edge together with its
incidence; a zero-length walk may be based at any ambient point.

```lean
Graph.Walk.{u, v} {α : Type u} {β : Type v} (G : Graph α β) : α → α → Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Graph.Walk`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Walk/Basic.html#Graph.Walk).

## Sources

- [Tau Ceti documentation: `Graph.Walk`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Walk/Basic.html#Graph.Walk)
- [Source of `Graph.Walk` in TauCeti/Combinatorics/Graph/Connectivity/Walk/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Connectivity/Walk/Basic.lean#L34)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
