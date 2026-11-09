# Filter

A filter `F` on a type `α` is a collection of sets of `α` which contains the whole `α`,
is upwards-closed, and is stable under intersection. We do not forbid this collection to be
all sets of `α`.

```lean
Filter.{u_1} (α : Type u_1) : Type u_1
```

## Depends on

- [Set](../../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Filter`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Filter/Defs.html#Filter)
- [Source of `Filter` in Mathlib/Order/Filter/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Order/Filter/Defs.lean#L70)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L215)
