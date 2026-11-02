---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Filter.Tendsto
mathlib_file: Mathlib/Order/Filter/Defs.lean
---

# Limit of a map with respect to filters

`Filter.Tendsto` is the generic "limit of a function" predicate.
`Tendsto f l₁ l₂` asserts that for every `l₂` neighborhood `a`,
the `f`-preimage of `a` is an `l₁` neighborhood.

```lean
Filter.Tendsto.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : α → β) (l₁ : Filter α)
  (l₂ : Filter β) : Prop
```

## Depends on

- [Filter](filter.md)

## Sources

- [Mathlib documentation: `Filter.Tendsto`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Filter/Defs.html#Filter.Tendsto)
- [Source of `Filter.Tendsto` in Mathlib/Order/Filter/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Order/Filter/Defs.lean#L418)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L216)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences of real numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L284)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real-valued functions defined on a subset of $\R$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L308)
