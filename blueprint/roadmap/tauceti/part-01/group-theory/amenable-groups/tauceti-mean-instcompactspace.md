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
- [Source of `TauCeti.Mean.instCompactSpace` in TauCeti/GroupTheory/Amenable/WeakStar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/WeakStar.lean#L148)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
