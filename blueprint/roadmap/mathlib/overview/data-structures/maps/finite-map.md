---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Finmap
mathlib_file: Mathlib/Data/Finmap.lean
---

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
- [Source of `Finmap` in Mathlib/Data/Finmap.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Finmap.lean#L67)
- [Mathlib overview: Data structures › Maps](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L590)
