---
declaration: theorem
origin: cited
lean: IsFreeGroup.isGDomain_id
statement: formalized
proof: formalized
---

# Nonabelian free groups are domains

(Baumslag–Myasnikov–Remeslennikov, Corollary 1).

```lean
IsFreeGroup.isGDomain_id.{u_1} {F : Type u_1} [Group F] [IsFreeGroup F] (hF : ¬IsMulCommutative F) :
  TauCeti.GroupAlgGeom.IsGDomain (MonoidHom.id F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CSA groups are domains](csa-groups-are-domains.md)
- [Free groups are CSA](free-groups-are-csa.md)

## Lean

Formalized in Tau Ceti as [`IsFreeGroup.isGDomain_id`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Domain.html#IsFreeGroup.isGDomain_id).

## Sources

- [Tau Ceti documentation: `IsFreeGroup.isGDomain_id`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Domain.html#IsFreeGroup.isGDomain_id)
- [Source of `IsFreeGroup.isGDomain_id` in TauCeti/GroupTheory/GroupAlgGeom/Domain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/GroupAlgGeom/Domain.lean#L264)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
