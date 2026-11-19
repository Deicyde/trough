---
declaration: def
origin: cited
lean: TauCeti.Colored3Graph.polyadEnergy
statement: formalized
---

# TauCeti.Colored3Graph.polyadEnergy

The **polyad energy** of a coloring `H` over a lower skeleton `S`: the mean, over the injective
triples `x`, of `∑ c, d_H(c | P_x)²`, where `P_x` is the polyad of `x` over `S` and
`d_H(c | P) = H.relativeDensity c P`. It is the support-weighted sum of the squared relative
densities over all polyads (`Colored3Graph.polyadEnergy_eq_sum_polyad`), and it is `0` when
`V` has fewer than three vertices.

```lean
TauCeti.Colored3Graph.polyadEnergy.{u_1, u_2, u_4} {κ : Type u_1} {κ₂ : Type u_2} {V : Type u_4}
  [Fintype V] [DecidableEq V] [DecidableEq κ] (H : TauCeti.Colored3Graph κ V) [Fintype κ]
  (S : TauCeti.PairSkeleton3 κ₂ V) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Colored3Graph.polyadEnergy`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Polyad/Energy/Basic.html#TauCeti.Colored3Graph.polyadEnergy).

## Sources

- [Tau Ceti documentation: `TauCeti.Colored3Graph.polyadEnergy`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Polyad/Energy/Basic.html#TauCeti.Colored3Graph.polyadEnergy)
- [Source of `TauCeti.Colored3Graph.polyadEnergy` in TauCeti/Combinatorics/Hypergraph/Polyad/Energy/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Hypergraph/Polyad/Energy/Basic.lean#L130)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Regularity/STATUS.md)
