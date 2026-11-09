---
declaration: theorem
origin: cited
lean: Graph.vertexConnectivity_le_edgeConnectivity, Graph.IsVertexConnected.isEdgeConnected
statement: formalized
proof: formalized
---

# Whitney's inequality for multigraphs

vertex connectivity is at most edge connectivity.

```lean
Graph.vertexConnectivity_le_edgeConnectivity.{u, v} {α : Type u} {β : Type v} {G : Graph α β} :
  G.vertexConnectivity ≤ G.edgeConnectivity
```

## Depends on

- [Graph.Walk](../finite-graph-connectivity-and-network-flows/graph-walk.md)

## Proof depends on

- [Whitney's inequality](../simple-graph/whitneys-inequality.md)

## Lean

Formalized in Tau Ceti as [`Graph.vertexConnectivity_le_edgeConnectivity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Whitney.html#Graph.vertexConnectivity_le_edgeConnectivity).

## Other forms

**Whitney's inequality for multigraphs, predicate form.** Formalized in Tau Ceti as [`Graph.IsVertexConnected.isEdgeConnected`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Whitney.html#Graph.IsVertexConnected.isEdgeConnected).

```lean
Graph.IsVertexConnected.isEdgeConnected.{u, v} {α : Type u} {β : Type v} {G : Graph α β} {k : ℕ}
  (h : G.IsVertexConnected k) : G.IsEdgeConnected k
```

## Sources

- [Tau Ceti documentation: `Graph.vertexConnectivity_le_edgeConnectivity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Whitney.html#Graph.vertexConnectivity_le_edgeConnectivity)
- [Source of `Graph.vertexConnectivity_le_edgeConnectivity` in TauCeti/Combinatorics/Graph/Connectivity/Whitney.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Connectivity/Whitney.lean#L112)
