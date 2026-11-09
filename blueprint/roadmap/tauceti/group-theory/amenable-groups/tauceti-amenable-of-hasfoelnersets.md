---
declaration: theorem
origin: cited
lean: TauCeti.Amenable.of_hasFoelnerSets
statement: formalized
proof: formalized
---

# TauCeti.Amenable.of_hasFoelnerSets

A group with Følner sets is amenable, for every group topology.

```lean
TauCeti.Amenable.of_hasFoelnerSets.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] (h : TauCeti.HasFoelnerSets G) : TauCeti.Amenable G
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.Amenable.of_tendsto](tauceti-amenable-of-tendsto.md)
- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable.of_hasFoelnerSets`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Average.html#TauCeti.Amenable.of_hasFoelnerSets).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable.of_hasFoelnerSets`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Average.html#TauCeti.Amenable.of_hasFoelnerSets)
- [Source of `TauCeti.Amenable.of_hasFoelnerSets` in TauCeti/GroupTheory/Amenable/Average.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/Average.lean#L207)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
