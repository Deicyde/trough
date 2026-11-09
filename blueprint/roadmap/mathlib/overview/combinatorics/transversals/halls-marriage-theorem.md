# Hall's marriage theorem

This is the version of **Hall's Marriage Theorem** in terms of indexed
families of finite sets `t : ι → Finset α`.  It states that there is a
set of distinct representatives if and only if every union of `k` of the
sets has at least `k` elements.

Recall that `s.biUnion t` is the union of all the sets `t i` for `i ∈ s`.

This theorem is bootstrapped from `Finset.all_card_le_biUnion_card_iff_exists_injective'`,
which has the additional constraint that `ι` is a `Fintype`.

```lean
Finset.all_card_le_biUnion_card_iff_exists_injective.{u, v} {ι : Type u} {α : Type v}
  [DecidableEq α] (t : ι → Finset α) :
  (∀ (s : Finset ι), s.card ≤ (s.biUnion t).card) ↔ ∃ f, Function.Injective f ∧ ∀ (x : ι), f x ∈ t x
```

The 1000+ list (Q536640) also cites `SimpleGraph.exists_isPerfectMatching_of_forall_ncard_le`.

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Small category](../../general-algebra/category-theory/small-category.md)

## Sources

- [Mathlib documentation: `Finset.all_card_le_biUnion_card_iff_exists_injective`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Hall/Basic.html#Finset.all_card_le_biUnion_card_iff_exists_injective)
- [Source of `Finset.all_card_le_biUnion_card_iff_exists_injective` in Mathlib/Combinatorics/Hall/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/Hall/Basic.lean#L106)
- [Mathlib overview: Combinatorics › Transversals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L502)
- [1000+ theorems list: Q536640](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L538)
- [1000+ theorems project: Q536640](https://1000-plus.github.io/all.html?length=-1#Q536640)
- [Wikipedia: Hall's marriage theorem](https://en.wikipedia.org/wiki/Hall's_marriage_theorem)
- [Wikidata: Q536640](https://www.wikidata.org/wiki/Q536640)
