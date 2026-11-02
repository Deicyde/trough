---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: QuotientGroup.Quotient.group
mathlib_file: Mathlib/GroupTheory/QuotientGroup/Defs.lean
---

# Quotient group

Mathlib states this as `QuotientGroup.Quotient.group`.

```lean
QuotientGroup.Quotient.group.{u_1} {G : Type u_1} [Group G] (N : Subgroup G) [nN : N.Normal] :
  Group (G ⧸ N)
```

## Depends on

- [Group action](group-action.md)
- [Normal subgroup](normal-subgroup.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)

## Sources

- [Mathlib documentation: `QuotientGroup.Quotient.group`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Defs.html#QuotientGroup.Quotient.group)
- [Source of `QuotientGroup.Quotient.group` in Mathlib/GroupTheory/QuotientGroup/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/QuotientGroup/Defs.lean#L71)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L43)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L86)
