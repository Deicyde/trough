---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: FDRep
mathlib_file: Mathlib/RepresentationTheory/FDRep.lean
---

# Category of finite-dimensional representations

The category of finitely generated `R`-linear representations of a monoid `G`.

Note that `R` can be any ring,
but the main case of interest is when `R = k` is a field and `G` is a group.

```lean
FDRep.{u, v} (R : Type u) (G : Type v) [Ring R] [Monoid G] : Type (max (max (u + 1) v) u)
```

## Depends on

- [Category](../category-theory/category.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [The category of modules over a ring](../../linear-algebra/fundamentals/the-category-of-modules-over-a-ring.md)

## Sources

- [Mathlib documentation: `FDRep`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/FDRep.html#FDRep)
- [Source of `FDRep` in Mathlib/RepresentationTheory/FDRep.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RepresentationTheory/FDRep.lean#L59)
- [Mathlib overview: General algebra › Representation theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L163)
