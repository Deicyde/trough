---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Finset.all_card_le_biUnion_card_iff_exists_injective, SimpleGraph.exists_isPerfectMatching_of_forall_ncard_le
mathlib_file: Mathlib/Combinatorics/Hall/Basic.lean
---

# Hall's marriage theorem

Mathlib records this with 2 declarations.

`Finset.all_card_le_biUnion_card_iff_exists_injective`: This is the version of **Hall's Marriage Theorem** in terms of indexed
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

`SimpleGraph.exists_isPerfectMatching_of_forall_ncard_le`: This is the version of **Hall's marriage theorem** for bipartite graphs that finds a perfect
matching given that the neighborhood-condition holds globally.

```lean
SimpleGraph.exists_isPerfectMatching_of_forall_ncard_le.{u_1} {V : Type u_1} {G : SimpleGraph V}
  [G.LocallyFinite] {p₁ p₂ : Set V} (h₁ : G.IsBipartiteWith p₁ p₂)
  (h₂ : ∀ (s : Set V), s.ncard ≤ (⋃ x ∈ s, G.neighborSet x).ncard) : ∃ M, M.IsPerfectMatching
```

## Depends on

- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Matching](../graph-theory/matching.md)
- [Ring morphism](../../general-algebra/rings/ring-morphism.md)

## Proof depends on

- [Adjunction](../../general-algebra/category-theory/adjunction.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Integer](../../general-algebra/numbers/integer.md)
- [Isomorphism](../../general-algebra/category-theory/isomorphism.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Small category](../../general-algebra/category-theory/small-category.md)
- [The category of topological spaces](../../topology/general-topology/part-01/the-category-of-topological-spaces.md)
- [Tychonoff's theorem](../../../thousand-plus/geometry-and-topology/54-general-topology/part-02/tychonoffs-theorem.md)

## Sources

- [Mathlib documentation: `Finset.all_card_le_biUnion_card_iff_exists_injective`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Hall/Basic.html#Finset.all_card_le_biUnion_card_iff_exists_injective)
- [Source of `Finset.all_card_le_biUnion_card_iff_exists_injective` in Mathlib/Combinatorics/Hall/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Hall/Basic.lean#L106)
- [Mathlib documentation: `SimpleGraph.exists_isPerfectMatching_of_forall_ncard_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Hall.html#SimpleGraph.exists_isPerfectMatching_of_forall_ncard_le)
- [Source of `SimpleGraph.exists_isPerfectMatching_of_forall_ncard_le` in Mathlib/Combinatorics/SimpleGraph/Hall.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/Hall.lean#L115)
- [Mathlib overview: Combinatorics › Transversals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L502)
- [1000+ theorems list: Q536640](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L538)
- [1000+ theorems project: Q536640](https://1000-plus.github.io/?length=-1#Q536640)
- [Wikipedia: Hall's marriage theorem](https://en.wikipedia.org/wiki/Hall's_marriage_theorem)
- [Wikidata: Q536640](https://www.wikidata.org/wiki/Q536640)
