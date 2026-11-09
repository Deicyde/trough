# Jordan–Hölder theorem

The **Jordan-Hölder** theorem, stated for any `JordanHolderLattice`.
If two composition series start and finish at the same place, they are equivalent.

```lean
CompositionSeries.jordan_holder.{u} {X : Type u} [Lattice X] [JordanHolderLattice X]
  (s₁ s₂ : CompositionSeries X) (hb : RelSeries.head s₁ = RelSeries.head s₂)
  (ht : RelSeries.last s₁ = RelSeries.last s₂) : s₁.Equivalent s₂
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)

## Sources

- [Mathlib documentation: `CompositionSeries.jordan_holder`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/JordanHolder.html#CompositionSeries.jordan_holder)
- [Source of `CompositionSeries.jordan_holder` in Mathlib/Order/JordanHolder.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Order/JordanHolder.lean#L453)
- [1000+ theorems list: Q2525646](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2249)
- [1000+ theorems project: Q2525646](https://1000-plus.github.io/all.html?length=-1#Q2525646)
- [Wikipedia: Jordan–Hölder theorem](https://en.wikipedia.org/wiki/Jordan%E2%80%93H%C3%B6lder_theorem)
- [Wikidata: Q2525646](https://www.wikidata.org/wiki/Q2525646)
