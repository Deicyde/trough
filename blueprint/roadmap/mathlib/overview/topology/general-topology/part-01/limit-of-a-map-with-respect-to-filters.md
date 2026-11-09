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
- [Source of `Filter.Tendsto` in Mathlib/Order/Filter/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Order/Filter/Defs.lean#L412)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L216)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences of real numbers](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L284)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real-valued functions defined on a subset of $\R$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L308)
