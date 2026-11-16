# W type

Given `β : α → Type*`, `WType β` is the type of finitely branching trees where nodes are labeled by
elements of `α` and the children of a node labeled `a` are indexed by elements of `β a`.

```lean
WType.{u_1, u_2} {α : Type u_1} (β : α → Type u_2) : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `WType`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/W/Basic.html#WType)
- [Source of `WType` in Mathlib/Data/W/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/W/Basic.lean#L37)
- [Mathlib overview: Data structures › Trees](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L597)
