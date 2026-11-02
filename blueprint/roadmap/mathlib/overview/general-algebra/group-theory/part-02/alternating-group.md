---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: alternatingGroup
mathlib_file: Mathlib/GroupTheory/SpecificGroups/Alternating.lean
---

# Alternating group

The alternating group on a finite type, realized as a subgroup of `Equiv.Perm`.
For $A_n$, use `alternatingGroup (Fin n)`.

```lean
alternatingGroup.{u_1} (α : Type u_1) [Fintype α] [DecidableEq α] : Subgroup (Equiv.Perm α)
```

## Depends on

- [Signature](../../../../undergraduate/group-theory/permutation-group/signature.md)
- [Subgroup](../part-01/subgroup.md)

## Sources

- [Mathlib documentation: `alternatingGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#alternatingGroup)
- [Source of `alternatingGroup` in Mathlib/GroupTheory/SpecificGroups/Alternating.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/SpecificGroups/Alternating.lean#L70)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L55)
- [Mathlib undergraduate list: Group Theory › Permutation group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L103)
