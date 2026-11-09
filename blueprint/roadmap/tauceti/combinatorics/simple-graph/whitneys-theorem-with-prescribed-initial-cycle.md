---
declaration: theorem
origin: cited
lean: SimpleGraph.IsVertexConnected.exists_isOpen_earDecomposition_initial_eq
statement: formalized
proof: formalized
---

# Whitney's theorem with prescribed initial cycle

For any cycle `c` in a `2`-vertex-connected
simple graph on a finite vertex type, there is an open ear decomposition of `⊤` whose initial
subgraph is `c.toSubgraph`.

```lean
SimpleGraph.IsVertexConnected.exists_isOpen_earDecomposition_initial_eq.{u} {V : Type u}
  {G : SimpleGraph V} [Finite V] (hG : G.IsVertexConnected 2) {u : V} (c : G.Walk u u)
  (hc : c.IsCycle) : ∃ d, d.IsOpen ∧ d.initial = c.toSubgraph
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Menger's theorem for fans](mengers-theorem-for-fans.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.IsVertexConnected.exists_isOpen_earDecomposition_initial_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Ear/Open.html#SimpleGraph.IsVertexConnected.exists_isOpen_earDecomposition_initial_eq).

## Sources

- [Tau Ceti documentation: `SimpleGraph.IsVertexConnected.exists_isOpen_earDecomposition_initial_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Ear/Open.html#SimpleGraph.IsVertexConnected.exists_isOpen_earDecomposition_initial_eq)
- [Source of `SimpleGraph.IsVertexConnected.exists_isOpen_earDecomposition_initial_eq` in TauCeti/Combinatorics/SimpleGraph/Connectivity/Ear/Open.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/SimpleGraph/Connectivity/Ear/Open.lean#L291)
