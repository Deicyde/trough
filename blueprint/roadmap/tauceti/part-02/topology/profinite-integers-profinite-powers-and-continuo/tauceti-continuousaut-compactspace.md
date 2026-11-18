---
declaration: theorem
origin: cited
lean: TauCeti.ContinuousAut.compactSpace
statement: formalized
proof: formalized
---

# TauCeti.ContinuousAut.compactSpace

For a topologically finitely generated profinite group, the congruence topology on the
continuous automorphisms is compact: `ContinuousAut G` is a closed subspace of the product of the
finite automorphism groups of the characteristic open quotients.

```lean
TauCeti.ContinuousAut.compactSpace.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (hG : TauCeti.IsTopologicallyFinitelyGenerated G) : CompactSpace (TauCeti.ContinuousAut G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuousAut.compactSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/Profinite.html#TauCeti.ContinuousAut.compactSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuousAut.compactSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/Profinite.html#TauCeti.ContinuousAut.compactSpace)
- [Source of `TauCeti.ContinuousAut.compactSpace` in TauCeti/Topology/Algebra/Group/ContinuousAut/Profinite.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/ContinuousAut/Profinite.lean#L217)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteArithmetic/STATUS.md)
