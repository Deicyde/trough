---
declaration: theorem
origin: cited
lean: TauCeti.GroupAlgGeom.IsGDomain.of_isCSA
statement: formalized
proof: formalized
---

# CSA groups are domains (Baumslag–Myasnikov–Remeslennikov, Proposition 1)

A CSA group in
which the images of two coefficients do not commute is a domain over these coefficients.

```lean
TauCeti.GroupAlgGeom.IsGDomain.of_isCSA.{u_1, u_3} {G : Type u_1} {H : Type u_3} [Group G] [Group H]
  {ι : G →* H} (hH : Group.IsCSA H) {a b : G} (hab : ¬Commute (ι a) (ι b)) :
  TauCeti.GroupAlgGeom.IsGDomain ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupAlgGeom.IsGDomain.of_isCSA`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Domain.html#TauCeti.GroupAlgGeom.IsGDomain.of_isCSA).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupAlgGeom.IsGDomain.of_isCSA`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Domain.html#TauCeti.GroupAlgGeom.IsGDomain.of_isCSA)
- [Source of `TauCeti.GroupAlgGeom.IsGDomain.of_isCSA` in TauCeti/GroupTheory/GroupAlgGeom/Domain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/GroupAlgGeom/Domain.lean#L138)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
