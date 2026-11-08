---
declaration: theorem
origin: cited
lean: SimpleGraph.vertexConnectivity_le_edgeConnectivity, SimpleGraph.IsVertexConnected.isEdgeConnected, Graph.IsVertexConnected.isEdgeConnected, Graph.vertexConnectivity_le_edgeConnectivity
statement: formalized
proof: formalized
---

# Whitney's inequality

the vertex connectivity of a simple graph is at most its edge
connectivity.

```lean
SimpleGraph.vertexConnectivity_le_edgeConnectivity.{u} {V : Type u} {G : SimpleGraph V} :
  G.vertexConnectivity ≤ G.edgeConnectivity
```

## Depends on

- [Graph.Walk](../finite-graph-connectivity-and-network-flows/graph-walk.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.vertexConnectivity_le_edgeConnectivity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.vertexConnectivity_le_edgeConnectivity).

## Other forms

**Whitney's inequality, predicate form.** Formalized in Tau Ceti as [`SimpleGraph.IsVertexConnected.isEdgeConnected`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.IsVertexConnected.isEdgeConnected).

```lean
SimpleGraph.IsVertexConnected.isEdgeConnected.{u} {V : Type u} {G : SimpleGraph V} {k : ℕ∞}
  (h : G.IsVertexConnected k) : G.IsEdgeConnected k
```

**Whitney's inequality for multigraphs, predicate form.** Formalized in Tau Ceti as [`Graph.IsVertexConnected.isEdgeConnected`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Whitney.html#Graph.IsVertexConnected.isEdgeConnected).

```lean
Graph.IsVertexConnected.isEdgeConnected.{u, v} {α : Type u} {β : Type v} {G : Graph α β} {k : ℕ}
  (h : G.IsVertexConnected k) : G.IsEdgeConnected k
```

**Whitney's inequality for multigraphs.** Formalized in Tau Ceti as [`Graph.vertexConnectivity_le_edgeConnectivity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Whitney.html#Graph.vertexConnectivity_le_edgeConnectivity).

```lean
Graph.vertexConnectivity_le_edgeConnectivity.{u, v} {α : Type u} {β : Type v} {G : Graph α β} :
  G.vertexConnectivity ≤ G.edgeConnectivity
```

## Sources

- [Tau Ceti documentation: `SimpleGraph.vertexConnectivity_le_edgeConnectivity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.vertexConnectivity_le_edgeConnectivity)
- [Source of `SimpleGraph.vertexConnectivity_le_edgeConnectivity` in TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.lean#L685)
