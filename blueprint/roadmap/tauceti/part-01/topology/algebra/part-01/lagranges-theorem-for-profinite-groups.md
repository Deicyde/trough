---
declaration: theorem
origin: cited
lean: Subgroup.profiniteOrder_eq_mul_profiniteIndex
statement: formalized
proof: formalized
---

# Lagrange's theorem for profinite groups

the supernatural order of the ambient group
is the order of a closed subgroup times its supernatural index.

```lean
Subgroup.profiniteOrder_eq_mul_profiniteIndex.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] (H : Subgroup G)
  (hH : IsClosed ↑H) : TauCeti.profiniteOrder G = TauCeti.profiniteOrder ↥H * H.profiniteIndex
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.profiniteOrder_eq_mul_profiniteIndex`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Lagrange.html#Subgroup.profiniteOrder_eq_mul_profiniteIndex).

## Sources

- [Tau Ceti documentation: `Subgroup.profiniteOrder_eq_mul_profiniteIndex`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Lagrange.html#Subgroup.profiniteOrder_eq_mul_profiniteIndex)
- [Source of `Subgroup.profiniteOrder_eq_mul_profiniteIndex` in TauCeti/Topology/Algebra/Group/Profinite/Lagrange.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Lagrange.lean#L90)
