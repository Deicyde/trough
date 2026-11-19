---
declaration: theorem
origin: cited
lean: Subgroup.profiniteIndex_subgroupOf_add_profiniteIndex
statement: formalized
proof: formalized
---

# Subgroup.profiniteIndex_subgroupOf_add_profiniteIndex

Primewise multiplicativity of profinite index through a closed intermediate subgroup.

```lean
Subgroup.profiniteIndex_subgroupOf_add_profiniteIndex.{u_1} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (H K : Subgroup G) (hHK : H ≤ K) (hK : IsClosed ↑K) (ell : Nat.Primes) :
  (H.subgroupOf K).profiniteIndex ell + K.profiniteIndex ell = H.profiniteIndex ell
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The third isomorphism theorem for coset spaces](../../../part-01/group-theory/other-results/part-02/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.profiniteIndex_subgroupOf_add_profiniteIndex`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Index/Tower.html#Subgroup.profiniteIndex_subgroupOf_add_profiniteIndex).

## Sources

- [Tau Ceti documentation: `Subgroup.profiniteIndex_subgroupOf_add_profiniteIndex`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Index/Tower.html#Subgroup.profiniteIndex_subgroupOf_add_profiniteIndex)
- [Source of `Subgroup.profiniteIndex_subgroupOf_add_profiniteIndex` in TauCeti/Topology/Algebra/Group/Profinite/Index/Tower.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/Index/Tower.lean#L143)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteProPGroups/STATUS.md)
