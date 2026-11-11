---
declaration: theorem
origin: cited
lean: Graph.IsBipartition.exists_isMatching_saturating_left_iff, Graph.IsBipartition.exists_isCapacitatedMatching_saturating_left_iff
statement: formalized
proof: formalized
---

# Hall's theorem for finite bipartite multigraphs

There is an ordinary matching incident
to every vertex of `L` if and only if every `S ⊆ L` has at least `|S|` neighbours in `R`.

```lean
Graph.IsBipartition.exists_isMatching_saturating_left_iff.{u, v} {α : Type u} {β : Type v}
  {G : Graph α β} {L R : Finset ↑G.vertexSet} [Finite ↑G.edgeSet] (hLR : G.IsBipartition L R) :
  (∃ M, G.IsMatching ↑M ∧ ∀ y ∈ L, ∃ e ∈ M, G.Inc ↑e ↑y) ↔
    ∀ S ⊆ L, S.card ≤ (G.neighborsIn S R).card
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kőnig's theorem for multiset capacitated matchings](konigs-theorem-for-multiset-capacitated-matching.md)

## Lean

Formalized in Tau Ceti as [`Graph.IsBipartition.exists_isMatching_saturating_left_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/OrdinaryHall.html#Graph.IsBipartition.exists_isMatching_saturating_left_iff).

## Other forms

**Hall's theorem for multiset capacitated matchings.** Formalized in Tau Ceti as [`Graph.IsBipartition.exists_isCapacitatedMatching_saturating_left_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/Hall.html#Graph.IsBipartition.exists_isCapacitatedMatching_saturating_left_iff).

```lean
Graph.IsBipartition.exists_isCapacitatedMatching_saturating_left_iff.{u, v} {α : Type u}
  {β : Type v} {G : Graph α β} [Fintype ↑G.edgeSet] {L R : Finset ↑G.vertexSet}
  (hLR : G.IsBipartition L R) (b : ↑G.vertexSet → ℕ) :
  (∃ x, G.IsCapacitatedMatching b x ∧ ∀ v ∈ L, ∑ e ∈ G.incidentEdges {v}, x e = b v) ↔
    ∀ S ⊆ L, ∑ v ∈ S, b v ≤ ∑ v ∈ G.neighborsIn S R, b v
```

## Sources

- [Tau Ceti documentation: `Graph.IsBipartition.exists_isMatching_saturating_left_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/OrdinaryHall.html#Graph.IsBipartition.exists_isMatching_saturating_left_iff)
- [Source of `Graph.IsBipartition.exists_isMatching_saturating_left_iff` in TauCeti/Combinatorics/Graph/Matching/OrdinaryHall.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Matching/OrdinaryHall.lean#L100)
