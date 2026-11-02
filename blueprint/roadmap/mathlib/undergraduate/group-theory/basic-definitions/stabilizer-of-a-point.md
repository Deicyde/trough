---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MulAction.stabilizer
mathlib_file: Mathlib/GroupTheory/GroupAction/Defs.lean
---

# Stabilizer of a point

The stabilizer of an element under an action, i.e. what sends the element to itself.
A subgroup.

```lean
MulAction.stabilizer.{u_1, u_2} (G : Type u_1) {α : Type u_2} [Group G] [MulAction G α] (a : α) :
  Subgroup G
```

## Depends on

- [Group action](../../../overview/general-algebra/group-theory/part-01/group-action.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `MulAction.stabilizer`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.stabilizer)
- [Source of `MulAction.stabilizer` in Mathlib/GroupTheory/GroupAction/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/GroupAction/Defs.lean#L511)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L88)
