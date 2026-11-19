---
declaration: theorem
origin: cited
lean: Graph.exists_stronglyConnected_orientation_iff, Graph.isEdgeConnected_two_iff_exists_stronglyConnected_orientation, SimpleGraph.exists_stronglyConnected_orientation_iff, SimpleGraph.isEdgeConnected_two_iff_exists_stronglyConnected_orientation, Graph.Connected.exists_stronglyConnected_orientation_iff, Graph.exists_componentwiseStrong_orientation_iff
statement: formalized
proof: formalized
---

# Robbins' theorem

A multigraph with finitely many actual edges has a strongly connected
orientation exactly when it is `2`-edge-connected. Loops and parallel edges are allowed, and no
connectedness or size assumption is needed: both sides hold when there is at most one actual
vertex.

```lean
Graph.exists_stronglyConnected_orientation_iff.{u, v} {V : Type u} {E : Type v} {G : Graph V E}
  [Finite ↑G.edgeSet] : (∃ o, Quiver.IsStronglyConnected ↑G.vertexSet) ↔ G.IsEdgeConnected 2
```

## Depends on

- [Graph.Orientation](graph-orientation.md)

## Proof depends on

- [Graph.EarDecomposition](graph-eardecomposition.md)

## Lean

Formalized in Tau Ceti as [`Graph.exists_stronglyConnected_orientation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.html#Graph.exists_stronglyConnected_orientation_iff).

## Other forms

**Robbins' theorem.** Formalized in Tau Ceti as [`Graph.isEdgeConnected_two_iff_exists_stronglyConnected_orientation`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Robbins.html#Graph.isEdgeConnected_two_iff_exists_stronglyConnected_orientation).

```lean
Graph.isEdgeConnected_two_iff_exists_stronglyConnected_orientation.{u, v} {α : Type u} {β : Type v}
  {G : Graph α β} [Finite ↑G.edgeSet] :
  G.IsEdgeConnected 2 ↔ ∃ o, Quiver.IsStronglyConnected ↑G.vertexSet
```

**Robbins' theorem for simple graphs.** Formalized in Tau Ceti as [`SimpleGraph.exists_stronglyConnected_orientation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.html#SimpleGraph.exists_stronglyConnected_orientation_iff).

```lean
SimpleGraph.exists_stronglyConnected_orientation_iff.{u} {V : Type u} {G : SimpleGraph V}
  [Finite ↑G.edgeSet] :
  (∃ o, Quiver.IsStronglyConnected (TauCeti.DoubledQuiver.OrientedQuiver G o)) ↔ G.IsEdgeConnected 2
```

**Robbins' theorem for simple graphs.** Formalized in Tau Ceti as [`SimpleGraph.isEdgeConnected_two_iff_exists_stronglyConnected_orientation`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Robbins.html#SimpleGraph.isEdgeConnected_two_iff_exists_stronglyConnected_orientation).

```lean
SimpleGraph.isEdgeConnected_two_iff_exists_stronglyConnected_orientation.{u} {V : Type u}
  {G : SimpleGraph V} [Finite V] :
  G.IsEdgeConnected 2 ↔ ∃ o, Quiver.IsStronglyConnected (TauCeti.DoubledQuiver.OrientedQuiver G o)
```

**Robbins' theorem, classical form.** Formalized in Tau Ceti as [`Graph.Connected.exists_stronglyConnected_orientation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.html#Graph.Connected.exists_stronglyConnected_orientation_iff).

```lean
Graph.Connected.exists_stronglyConnected_orientation_iff.{u, v} {V : Type u} {E : Type v}
  {G : Graph V E} [Finite ↑G.edgeSet] (hG : G.Connected) :
  (∃ o, Quiver.IsStronglyConnected ↑G.vertexSet) ↔ ∀ (e : E), ¬G.IsBridge e
```

**Robbins' theorem, componentwise form.** Formalized in Tau Ceti as [`Graph.exists_componentwiseStrong_orientation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.html#Graph.exists_componentwiseStrong_orientation_iff).

```lean
Graph.exists_componentwiseStrong_orientation_iff.{u, v} {V : Type u} {E : Type v} {G : Graph V E}
  [Finite ↑G.edgeSet] :
  (∃ o, ∀ (x y : ↑G.vertexSet), G.Reachable ↑x ↑y → Nonempty (TauCeti.ArrowWalk o.Hom x y)) ↔
    ∀ (e : E), ¬G.IsBridge e
```

## Sources

- [Tau Ceti documentation: `Graph.exists_stronglyConnected_orientation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.html#Graph.exists_stronglyConnected_orientation_iff)
- [Source of `Graph.exists_stronglyConnected_orientation_iff` in TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.lean#L273)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
