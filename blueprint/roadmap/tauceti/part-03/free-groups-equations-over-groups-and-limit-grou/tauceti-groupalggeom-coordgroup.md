---
declaration: abbrev
origin: cited
lean: TauCeti.GroupAlgGeom.CoordGroup
statement: formalized
---

# TauCeti.GroupAlgGeom.CoordGroup

The coordinate group `G_{R(S)} = G[X] ⧸ Rad_H(S)` of a system `S` over `H`.

```lean
TauCeti.GroupAlgGeom.CoordGroup.{u_1, u_2, u_3} {G : Type u_1} {H : Type u_2} {X : Type u_3}
  [Group G] [Group H] (ι : G →* H) (S : Set (TauCeti.GroupAlgGeom.GX G X)) : Type (max u_3 u_1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupAlgGeom.CoordGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/AlgebraicSet.html#TauCeti.GroupAlgGeom.CoordGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupAlgGeom.CoordGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/AlgebraicSet.html#TauCeti.GroupAlgGeom.CoordGroup)
- [Source of `TauCeti.GroupAlgGeom.CoordGroup` in TauCeti/GroupTheory/GroupAlgGeom/AlgebraicSet.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/GroupAlgGeom/AlgebraicSet.lean#L469)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
