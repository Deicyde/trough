---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.GrothendieckTopology
mathlib_file: Mathlib/CategoryTheory/Sites/Grothendieck.lean
---

# Grothendieck topology

The definition of a Grothendieck topology: a set of sieves `J X` on each object `X` satisfying
three axioms:
1. For every object `X`, the maximal sieve is in `J X`.
2. If `S ∈ J X` then its pullback along any `h : Y ⟶ X` is in `J Y`.
3. If `S ∈ J X` and `R` is a sieve on `X`, then provided that the pullback of `R` along any arrow
   `f : Y ⟶ X` in `S` is in `J Y`, we have that `R` itself is in `J X`.

A sieve `S` on `X` is referred to as `J`-covering, (or just covering), if `S ∈ J X`.

See also [nlab] or [MM92] Chapter III, Section 2, Definition 1.

```lean
CategoryTheory.GrothendieckTopology.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C] :
  Type (max u v)
```

## Depends on

- [Category](category.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `CategoryTheory.GrothendieckTopology`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology)
- [Source of `CategoryTheory.GrothendieckTopology` in Mathlib/CategoryTheory/Sites/Grothendieck.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Sites/Grothendieck.lean#L61)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L18)
