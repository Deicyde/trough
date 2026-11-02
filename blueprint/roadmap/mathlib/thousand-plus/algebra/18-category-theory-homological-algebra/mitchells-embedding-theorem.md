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
- [Array](../../../overview/data-structures/list-like-structures/array.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Comma category](../../../overview/general-algebra/category-theory/comma-category.md)
- [Fundamental sequences](../../../overview/logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Monoidal category](../../../overview/general-algebra/category-theory/monoidal-category.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [Well-ordering theorem](../../general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)
- [Yoneda embedding](../../../overview/general-algebra/category-theory/yoneda-embedding.md)

## Sources

- [Mathlib documentation: `CategoryTheory.Abelian.freyd_mitchell`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Abelian/FreydMitchell.html#CategoryTheory.Abelian.freyd_mitchell)
- [Source of `CategoryTheory.Abelian.freyd_mitchell` in Mathlib/CategoryTheory/Abelian/FreydMitchell.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/CategoryTheory/Abelian/FreydMitchell.lean#L165)
- [1000+ theorems list: Q1148215](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1438)
- [1000+ theorems project: Q1148215](https://1000-plus.github.io/?length=-1#Q1148215)
- [Wikipedia: Mitchell's embedding theorem](https://en.wikipedia.org/wiki/Mitchell's_embedding_theorem)
- [Wikidata: Q1148215](https://www.wikidata.org/wiki/Q1148215)
