---
declaration: class
origin: cited
lean: TauCeti.Amenable
statement: formalized
---

# TauCeti.Amenable

A topological group `G` is amenable when `UCB G` carries a left-invariant mean.

```lean
TauCeti.Amenable.{u_1} (G : Type u_1) [Group G] [TopologicalSpace G] [IsTopologicalGroup G] : Prop
```

## Depends on

- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Basic.html#TauCeti.Amenable).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Basic.html#TauCeti.Amenable)
- [Source of `TauCeti.Amenable` in TauCeti/GroupTheory/Amenable/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/Basic.lean#L135)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
