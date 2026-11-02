---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: orderOf
mathlib_file: Mathlib/GroupTheory/OrderOfElement.lean
---

# Order of an element

`orderOf x` is the order of the element `x`, i.e. the `n ≥ 1`, s.t. `x ^ n = 1` if it exists.
Otherwise, i.e. if `x` is of infinite order, then `orderOf x` is `0` by convention.

```lean
orderOf.{u_1} {G : Type u_1} [Monoid G] (x : G) : ℕ
```

## Depends on

- [Periodic points](../../../overview/dynamics/general-theory/periodic-points.md)

## Sources

- [Mathlib documentation: `orderOf`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#orderOf)
- [Source of `orderOf` in Mathlib/GroupTheory/OrderOfElement.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/OrderOfElement.lean#L174)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L84)
