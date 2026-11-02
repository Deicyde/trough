---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Set
mathlib_file: Mathlib/Data/Set/Defs.lean
---

# Set

A set is a collection of elements of some type `α`.

To build a set (an element of `Set α`) out of a predicate `p : α → Prop`, use the set builder
notation `{a | p a}`. To get a predicate `α → Prop` from a set `s : Set α`, use the `∈` notation,
as in `a ∈ s` or `(· ∈ s)`.

```lean
Set.{u} (α : Type u) : Type u
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `Set`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Set/Defs.html#Set)
- [Source of `Set` in Mathlib/Data/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Set/Defs.lean#L42)
- [Mathlib overview: Data structures › Sets](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L579)
