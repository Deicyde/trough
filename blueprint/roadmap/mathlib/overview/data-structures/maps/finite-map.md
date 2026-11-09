# Finite map

`Finmap β` is the type of finite maps over a multiset. It is effectively
a quotient of `AList β` by permutation of the underlying list.

```lean
Finmap.{u, v} {α : Type u} (β : α → Type v) : Type (max u v)
```

## Depends on

- [Multiset](../sets/multiset.md)

## Sources

- [Mathlib documentation: `Finmap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finmap.html#Finmap)
- [Source of `Finmap` in Mathlib/Data/Finmap.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Data/Finmap.lean#L67)
- [Mathlib overview: Data structures › Maps](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L590)
