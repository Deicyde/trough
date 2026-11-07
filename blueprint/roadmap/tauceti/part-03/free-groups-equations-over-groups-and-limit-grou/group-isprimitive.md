---
declaration: def
origin: cited
lean: Group.IsPrimitive
statement: formalized
---

# Group.IsPrimitive

An element of a group is primitive when it belongs to some free basis of the group.

```lean
Group.IsPrimitive.{u} {G : Type u} [Group G] (x : G) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Group.IsPrimitive`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Primitive.html#Group.IsPrimitive).

## Sources

- [Tau Ceti documentation: `Group.IsPrimitive`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Primitive.html#Group.IsPrimitive)
- [Source of `Group.IsPrimitive` in TauCeti/GroupTheory/FreeGroup/Primitive.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/FreeGroup/Primitive.lean#L33)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
