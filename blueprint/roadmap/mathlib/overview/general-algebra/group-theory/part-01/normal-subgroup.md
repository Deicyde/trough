---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Subgroup.Normal
mathlib_file: Mathlib/Algebra/Group/Subgroup/Defs.lean
---

# Normal subgroup

A subgroup `H` is normal if whenever `n ∈ H`, then `g * n * g⁻¹ ∈ H` for every `g : G`

[Wikidata Q743179](https://www.wikidata.org/wiki/Q743179)

```lean
Subgroup.Normal.{u_1} {G : Type u_1} [Group G] (H : Subgroup G) : Prop
```

## Depends on

- [Subgroup](subgroup.md)

## Sources

- [Mathlib documentation: `Subgroup.Normal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Defs.html#Subgroup.Normal)
- [Source of `Subgroup.Normal` in Mathlib/Algebra/Group/Subgroup/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Subgroup/Defs.lean#L605)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L40)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L85)
