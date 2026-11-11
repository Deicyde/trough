---
declaration: theorem
origin: cited
lean: SimpleGraph.vertexConnectivity_le_edgeConnectivity, SimpleGraph.IsVertexConnected.isEdgeConnected
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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.vertexConnectivity_le_edgeConnectivity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.vertexConnectivity_le_edgeConnectivity).

## Other forms

**Whitney's inequality, predicate form.** Formalized in Tau Ceti as [`SimpleGraph.IsVertexConnected.isEdgeConnected`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.IsVertexConnected.isEdgeConnected).

```lean
SimpleGraph.IsVertexConnected.isEdgeConnected.{u} {V : Type u} {G : SimpleGraph V} {k : ℕ∞}
  (h : G.IsVertexConnected k) : G.IsEdgeConnected k
```

## Sources

- [Tau Ceti documentation: `SimpleGraph.vertexConnectivity_le_edgeConnectivity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.vertexConnectivity_le_edgeConnectivity)
- [Source of `SimpleGraph.vertexConnectivity_le_edgeConnectivity` in TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.lean#L719)
