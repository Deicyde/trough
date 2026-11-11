---
declaration: theorem
origin: cited
lean: TauCeti.Amenable.of_commGroup
statement: formalized
proof: formalized
---

# TauCeti.Amenable.of_commGroup

Every commutative topological group is amenable, whatever its group topology.

```lean
TauCeti.Amenable.of_commGroup.{u_1} {G : Type u_1} [CommGroup G] [TopologicalSpace G]
  [IsTopologicalGroup G] : TauCeti.Amenable G
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.Mean.instCompactSpace](tauceti-mean-instcompactspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable.of_commGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Abelian.html#TauCeti.Amenable.of_commGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable.of_commGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Abelian.html#TauCeti.Amenable.of_commGroup)
- [Source of `TauCeti.Amenable.of_commGroup` in TauCeti/GroupTheory/Amenable/Abelian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/Abelian.lean#L46)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
