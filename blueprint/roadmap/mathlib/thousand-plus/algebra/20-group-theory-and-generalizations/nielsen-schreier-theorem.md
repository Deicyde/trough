# Nielsen–Schreier theorem

The Nielsen-Schreier theorem: a subgroup of a free group is free.

```lean
Subgroup.isFreeGroupOfIsFreeGroup.{u} {G : Type u} [Group G] [IsFreeGroup G] (H : Subgroup G) :
  IsFreeGroup ↥H
```

## Depends on

- [Free group](../../../overview/general-algebra/group-theory/part-01/free-group.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Proof depends on

- [Isomorphism](../../../overview/general-algebra/category-theory/isomorphism.md)
- [List](../../../overview/data-structures/list-like-structures/list.md)
- [Orbit](../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Small category](../../../overview/general-algebra/category-theory/small-category.md)

## Sources

- [Mathlib documentation: `Subgroup.isFreeGroupOfIsFreeGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FreeGroup/NielsenSchreier.html#Subgroup.isFreeGroupOfIsFreeGroup)
- [Source of `Subgroup.isFreeGroupOfIsFreeGroup` in Mathlib/GroupTheory/FreeGroup/NielsenSchreier.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/GroupTheory/FreeGroup/NielsenSchreier.lean#L325)
- [1000+ theorems list: Q1259814](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1576)
- [1000+ theorems project: Q1259814](https://1000-plus.github.io/all.html?length=-1#Q1259814)
- [Wikipedia: Nielsen–Schreier theorem](https://en.wikipedia.org/wiki/Nielsen%E2%80%93Schreier_theorem)
- [Wikidata: Q1259814](https://www.wikidata.org/wiki/Q1259814)
