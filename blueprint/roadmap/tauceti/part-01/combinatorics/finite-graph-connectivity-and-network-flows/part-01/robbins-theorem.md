---
declaration: theorem
origin: cited
lean: Graph.exists_stronglyConnected_orientation_iff, SimpleGraph.exists_stronglyConnected_orientation_iff, Graph.Connected.exists_stronglyConnected_orientation_iff, Graph.exists_componentwiseStrong_orientation_iff
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

## Lean

Formalized in Tau Ceti as [`Graph.exists_stronglyConnected_orientation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.html#Graph.exists_stronglyConnected_orientation_iff).

## Other forms

**Robbins' theorem for simple graphs.** Formalized in Tau Ceti as [`SimpleGraph.exists_stronglyConnected_orientation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.html#SimpleGraph.exists_stronglyConnected_orientation_iff).

```lean
SimpleGraph.exists_stronglyConnected_orientation_iff.{u} {V : Type u} {G : SimpleGraph V}
  [Finite ↑G.edgeSet] :
  (∃ o, Quiver.IsStronglyConnected (TauCeti.DoubledQuiver.OrientedQuiver G o)) ↔ G.IsEdgeConnected 2
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
- [Source of `Graph.exists_stronglyConnected_orientation_iff` in TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Orientation/StronglyConnected.lean#L273)
