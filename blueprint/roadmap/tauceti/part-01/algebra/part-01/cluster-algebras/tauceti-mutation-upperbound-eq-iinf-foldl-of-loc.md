---
declaration: theorem
origin: cited
lean: TauCeti.Mutation.upperBound_eq_iInf_foldl_of_local
statement: formalized
proof: formalized
---

# TauCeti.Mutation.upperBound_eq_iInf_foldl_of_local

The local three-chart criterion identifies the upper bound with the
intersection of every reachable chart.

```lean
TauCeti.Mutation.upperBound_eq_iInf_foldl_of_local.{u_1, u_2, u_3} {K : Type u_1} {V : Type u_2}
  {A : Type u_3} [CompleteLattice A] (μ : K → V → V) (L : V → A)
  (hμ : ∀ (k : K), Function.Involutive (μ k))
  (hlocal : ∀ (s : V) (i j : K), i ≠ j → L s ⊓ L (μ i s) ⊓ L (μ j s) ≤ L (μ j (μ i s))) (s : V) :
  TauCeti.Mutation.upperBound μ L s = ⨅ w, L (List.foldl (fun t k => μ k t) s w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Mutation.upperBound_eq_iInf_foldl_of_local`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/UpperBound/Lattice.html#TauCeti.Mutation.upperBound_eq_iInf_foldl_of_local).

## Sources

- [Tau Ceti documentation: `TauCeti.Mutation.upperBound_eq_iInf_foldl_of_local`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/UpperBound/Lattice.html#TauCeti.Mutation.upperBound_eq_iInf_foldl_of_local)
- [Source of `TauCeti.Mutation.upperBound_eq_iInf_foldl_of_local` in TauCeti/Algebra/Cluster/UpperBound/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Cluster/UpperBound/Lattice.lean#L102)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
