---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Abelian.freyd_mitchell
mathlib_file: Mathlib/CategoryTheory/Abelian/FreydMitchell.lean
---

# Mitchell's embedding theorem

The Freyd-Mitchell embedding theorem. See also `FreydMitchell.functor` for a functor which
has the relevant instances.

```lean
CategoryTheory.Abelian.freyd_mitchell.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] :
  ∃ R x F,
    F.Full ∧
      F.Faithful ∧
        CategoryTheory.Limits.PreservesFiniteLimits F ∧
          CategoryTheory.Limits.PreservesFiniteColimits F
```

## Depends on

- [Abelian category](../../../overview/general-algebra/category-theory/abelian-category.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Set](../../../overview/data-structures/sets/set.md)
- [The category of modules over a ring](../../../overview/linear-algebra/fundamentals/the-category-of-modules-over-a-ring.md)

## Proof depends on

- [Adjunction](../../../overview/general-algebra/category-theory/adjunction.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Monoidal category](../../../overview/general-algebra/category-theory/monoidal-category.md)
- [Yoneda embedding](../../../overview/general-algebra/category-theory/yoneda-embedding.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Abelian.freyd_mitchell`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Abelian/FreydMitchell.html#CategoryTheory.Abelian.freyd_mitchell)
- [Source of `CategoryTheory.Abelian.freyd_mitchell` in Mathlib/CategoryTheory/Abelian/FreydMitchell.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Abelian/FreydMitchell.lean#L165)
- [1000+ theorems list: Q1148215](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1438)
- [1000+ theorems project: Q1148215](https://1000-plus.github.io/all.html?length=-1#Q1148215)
- [Wikipedia: Mitchell's embedding theorem](https://en.wikipedia.org/wiki/Mitchell's_embedding_theorem)
- [Wikidata: Q1148215](https://www.wikidata.org/wiki/Q1148215)
