---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Equiv.Perm.subgroupOfMulAction
mathlib_file: Mathlib/GroupTheory/Perm/Subgroup.lean
---

# Cayley's theorem

**Cayley's theorem**: Every group G is isomorphic to a subgroup of the symmetric group acting on
`G`. Note that we generalize this to an arbitrary "faithful" group action by `G`. Setting `H = G`
recovers the usual statement of Cayley's theorem via `RightCancelMonoid.faithfulSMul`

```lean
Equiv.Perm.subgroupOfMulAction.{u_1, u_2} (G : Type u_1) (H : Type u_2) [Group G] [MulAction G H]
  [FaithfulSMul G H] : G ≃* ↥(MulAction.toPermHom G H).range
```

## Depends on

- [Group action](../part-01/group-action.md)
- [Group morphism](../part-01/group-morphism.md)
- [Permutation group of a type](permutation-group-of-a-type.md)
- [Subgroup](../part-01/subgroup.md)

## Sources

- [Mathlib documentation: `Equiv.Perm.subgroupOfMulAction`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Subgroup.html#Equiv.Perm.subgroupOfMulAction)
- [Source of `Equiv.Perm.subgroupOfMulAction` in Mathlib/GroupTheory/Perm/Subgroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Perm/Subgroup.lean#L68)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L54)
- [1000+ theorems list: Q179208](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L80)
- [1000+ theorems project: Q179208](https://1000-plus.github.io/all.html?length=-1#Q179208)
- [Wikipedia: Cayley's theorem](https://en.wikipedia.org/wiki/Cayley's_theorem)
- [Wikidata: Q179208](https://www.wikidata.org/wiki/Q179208)
