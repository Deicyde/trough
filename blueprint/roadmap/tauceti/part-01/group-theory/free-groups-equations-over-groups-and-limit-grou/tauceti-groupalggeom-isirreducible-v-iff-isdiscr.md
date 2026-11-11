---
declaration: theorem
origin: cited
lean: TauCeti.GroupAlgGeom.isIrreducible_V_iff_isDiscriminatedBy
statement: formalized
proof: formalized
---

# TauCeti.GroupAlgGeom.isIrreducible_V_iff_isDiscriminatedBy

A solution set over arbitrary coefficients is irreducible exactly when its coordinate
group is discriminated by the target. No domain or nonemptiness hypothesis is needed:
discrimination, even on the empty finite family, supplies a point.

```lean
TauCeti.GroupAlgGeom.isIrreducible_V_iff_isDiscriminatedBy.{u_1, u_2, u_3} {G : Type u_1}
  {H : Type u_2} {X : Type u_3} [Group G] [Group H] {ι : G →* H}
  {S : Set (TauCeti.GroupAlgGeom.GX G X)} :
  IsIrreducible (TauCeti.GroupAlgGeom.V ι S) ↔
    TauCeti.GroupAlgGeom.IsDiscriminatedBy (TauCeti.GroupAlgGeom.CoordGroup.coeff ι S) ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupAlgGeom.isIrreducible_V_iff_isDiscriminatedBy`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Irreducible/Basic.html#TauCeti.GroupAlgGeom.isIrreducible_V_iff_isDiscriminatedBy).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupAlgGeom.isIrreducible_V_iff_isDiscriminatedBy`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Irreducible/Basic.html#TauCeti.GroupAlgGeom.isIrreducible_V_iff_isDiscriminatedBy)
- [Source of `TauCeti.GroupAlgGeom.isIrreducible_V_iff_isDiscriminatedBy` in TauCeti/GroupTheory/GroupAlgGeom/Irreducible/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupAlgGeom/Irreducible/Basic.lean#L117)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
