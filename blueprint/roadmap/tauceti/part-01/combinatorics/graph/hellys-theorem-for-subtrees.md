---
declaration: theorem
origin: cited
lean: TauCeti.SerreGraph.IsTree.helly_theorem
statement: formalized
proof: formalized
---

# Helly's theorem for subtrees

In a tree, finitely many pairwise intersecting convex sets
of vertices have a common vertex.

```lean
TauCeti.SerreGraph.IsTree.helly_theorem.{u_1, u_2, u_3} {Γ : TauCeti.SerreGraph} (h : Γ.IsTree)
  {ι : Type u_1} {F : ι → Set Γ.V} {s : Finset ι} (h_convex : ∀ i ∈ s, Γ.IsConvex (F i))
  (h_inter : ∀ i ∈ s, ∀ j ∈ s, (F i ∩ F j).Nonempty) : (⋂ i ∈ s, F i).Nonempty
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SerreGraph.IsTree.helly_theorem`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Serre/Helly.html#TauCeti.SerreGraph.IsTree.helly_theorem).

## Sources

- [Tau Ceti documentation: `TauCeti.SerreGraph.IsTree.helly_theorem`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Serre/Helly.html#TauCeti.SerreGraph.IsTree.helly_theorem)
- [Source of `TauCeti.SerreGraph.IsTree.helly_theorem` in TauCeti/Combinatorics/Graph/Serre/Helly.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Graph/Serre/Helly.lean#L63)
