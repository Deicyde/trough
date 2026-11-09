---
declaration: theorem
origin: cited
lean: Graph.isBridge_iff_componentCount_deleteEdges_eq_add_one
statement: formalized
proof: formalized
---

# Bridges by component counts

With finitely many connected components, an edge is a
bridge exactly when deleting it increases the number of connected components by one.

```lean
Graph.isBridge_iff_componentCount_deleteEdges_eq_add_one.{u, v} {α : Type u} {β : Type v}
  {G : Graph α β} {e : β} [Finite G.ConnectedComponent] :
  G.IsBridge e ↔ (G.deleteEdges {e}).componentCount = G.componentCount + 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Graph.Walk](graph-walk.md)

## Lean

Formalized in Tau Ceti as [`Graph.isBridge_iff_componentCount_deleteEdges_eq_add_one`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Bridge/Basic.html#Graph.isBridge_iff_componentCount_deleteEdges_eq_add_one).

## Sources

- [Tau Ceti documentation: `Graph.isBridge_iff_componentCount_deleteEdges_eq_add_one`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Bridge/Basic.html#Graph.isBridge_iff_componentCount_deleteEdges_eq_add_one)
- [Source of `Graph.isBridge_iff_componentCount_deleteEdges_eq_add_one` in TauCeti/Combinatorics/Graph/Connectivity/Bridge/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Connectivity/Bridge/Basic.lean#L220)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
