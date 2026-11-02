---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: ChainComplex
mathlib_file: Mathlib/Algebra/Homology/HomologicalComplex.lean
---

# Chain complex

An `α`-indexed chain complex is a `HomologicalComplex`
in which `d i j ≠ 0` only if `j + 1 = i`.

```lean
ChainComplex.{v, u, u_2} (V : Type u) [CategoryTheory.Category.{v, u} V]
  [CategoryTheory.Limits.HasZeroMorphisms V] (α : Type u_2) [AddRightCancelSemigroup α] [One α] :
  Type (max (max u_2 u) v)
```

## Depends on

- [Category](../category-theory/category.md)

## Sources

- [Mathlib documentation: `ChainComplex`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Homology/HomologicalComplex.html#ChainComplex)
- [Source of `ChainComplex` in Mathlib/Algebra/Homology/HomologicalComplex.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Homology/HomologicalComplex.lean#L148)
- [Mathlib overview: General algebra › Homological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L138)
