---
declaration: theorem
origin: cited
lean: TauCeti.Amenable.of_finite
statement: formalized
proof: formalized
---

# TauCeti.Amenable.of_finite

A finite topological group is amenable, for any group topology.

```lean
TauCeti.Amenable.of_finite.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [Finite G] : TauCeti.Amenable G
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable.of_finite`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Finite.html#TauCeti.Amenable.of_finite).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable.of_finite`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Finite.html#TauCeti.Amenable.of_finite)
- [Source of `TauCeti.Amenable.of_finite` in TauCeti/GroupTheory/Amenable/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/Finite.lean#L156)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
