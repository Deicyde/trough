---
declaration: theorem
origin: cited
lean: TauCeti.amenable_iff_hasFoelnerSets
statement: formalized
proof: formalized
---

# TauCeti.amenable_iff_hasFoelnerSets

A discrete group is amenable exactly when it has Følner sets.

```lean
TauCeti.amenable_iff_hasFoelnerSets.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [DiscreteTopology G] : TauCeti.Amenable G ↔ TauCeti.HasFoelnerSets G
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.Mean.instCompactSpace](tauceti-mean-instcompactspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.amenable_iff_hasFoelnerSets`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/DiscreteFoelner.html#TauCeti.amenable_iff_hasFoelnerSets).

## Sources

- [Tau Ceti documentation: `TauCeti.amenable_iff_hasFoelnerSets`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/DiscreteFoelner.html#TauCeti.amenable_iff_hasFoelnerSets)
- [Source of `TauCeti.amenable_iff_hasFoelnerSets` in TauCeti/GroupTheory/Amenable/DiscreteFoelner.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Amenable/DiscreteFoelner.lean#L163)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AmenableGroups/STATUS.md)
