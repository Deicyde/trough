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
- [Source of `Finmap` in Mathlib/Data/Finmap.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Finmap.lean#L67)
- [Mathlib overview: Data structures › Maps](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L590)
