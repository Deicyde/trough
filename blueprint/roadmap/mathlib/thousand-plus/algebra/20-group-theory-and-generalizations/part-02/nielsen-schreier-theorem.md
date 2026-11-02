---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Subgroup.isFreeGroupOfIsFreeGroup
mathlib_file: Mathlib/GroupTheory/FreeGroup/NielsenSchreier.lean
---

# Nielsen–Schreier theorem

The Nielsen-Schreier theorem: a subgroup of a free group is free.

```lean
Subgroup.isFreeGroupOfIsFreeGroup.{u} {G : Type u} [Group G] [IsFreeGroup G] (H : Subgroup G) :
  IsFreeGroup ↥H
```

## Depends on

- [Free group](../../../../overview/general-algebra/group-theory/part-01/free-group.md)
- [Subgroup](../../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Proof depends on

- [Group morphism](../../../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Isomorphism](../../../../overview/general-algebra/category-theory/isomorphism.md)
- [Natural transformation](../../../../overview/general-algebra/category-theory/natural-transformation.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Small category](../../../../overview/general-algebra/category-theory/small-category.md)
- [Stabilizer of a point](../../../../undergraduate/group-theory/basic-definitions/stabilizer-of-a-point.md)

## Sources

- [Mathlib documentation: `Subgroup.isFreeGroupOfIsFreeGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FreeGroup/NielsenSchreier.html#Subgroup.isFreeGroupOfIsFreeGroup)
- [Source of `Subgroup.isFreeGroupOfIsFreeGroup` in Mathlib/GroupTheory/FreeGroup/NielsenSchreier.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/FreeGroup/NielsenSchreier.lean#L325)
- [1000+ theorems list: Q1259814](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1576)
- [1000+ theorems project: Q1259814](https://1000-plus.github.io/?length=-1#Q1259814)
- [Wikipedia: Nielsen–Schreier theorem](https://en.wikipedia.org/wiki/Nielsen%E2%80%93Schreier_theorem)
- [Wikidata: Q1259814](https://www.wikidata.org/wiki/Q1259814)
