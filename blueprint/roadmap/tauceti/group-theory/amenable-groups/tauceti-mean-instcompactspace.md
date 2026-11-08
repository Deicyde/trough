---
declaration: theorem
origin: cited
lean: TauCeti.Mean.instCompactSpace
statement: formalized
proof: formalized
---

# TauCeti.Mean.instCompactSpace

The space of means is weak-* compact.

```lean
TauCeti.Mean.instCompactSpace.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] : CompactSpace (TauCeti.Mean G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Mean.instCompactSpace`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/WeakStar.html#TauCeti.Mean.instCompactSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.Mean.instCompactSpace`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/WeakStar.html#TauCeti.Mean.instCompactSpace)
- [Source of `TauCeti.Mean.instCompactSpace` in TauCeti/GroupTheory/Amenable/WeakStar.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/WeakStar.lean#L148)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
