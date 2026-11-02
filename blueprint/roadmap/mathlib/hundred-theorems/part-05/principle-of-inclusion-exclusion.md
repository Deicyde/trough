---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Finset.inclusion_exclusion_sum_biUnion, Finset.inclusion_exclusion_card_biUnion, Finset.inclusion_exclusion_sum_inf_compl, Finset.inclusion_exclusion_card_inf_compl
mathlib_file: Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean
---

# Principle of Inclusion/Exclusion

Mathlib records this with 4 declarations.

`Finset.inclusion_exclusion_sum_biUnion`: **Inclusion-exclusion principle** for the sum of a function over a union.

The sum of a function `f` over the union of the `S i` over `i ∈ s` is the alternating sum of the
sums of `f` over the intersections of the `S i`.

```lean
Finset.inclusion_exclusion_sum_biUnion.{u_1, u_2, u_3} {ι : Type u_1} {α : Type u_2} {G : Type u_3}
  [AddCommGroup G] [DecidableEq α] (s : Finset ι) (S : ι → Finset α) (f : α → G) :
  ∑ a ∈ s.biUnion S, f a = ∑ t, (-1) ^ ((↑t).card + 1) • ∑ a ∈ (↑t).inf' ⋯ S, f a
```

`Finset.inclusion_exclusion_card_biUnion`: **Inclusion-exclusion principle** for the cardinality of a union.

The cardinality of the union of the `S i` over `i ∈ s` is the alternating sum of the cardinalities
of the intersections of the `S i`.

```lean
Finset.inclusion_exclusion_card_biUnion.{u_1, u_2} {ι : Type u_1} {α : Type u_2} [DecidableEq α]
  (s : Finset ι) (S : ι → Finset α) :
  ↑(s.biUnion S).card = ∑ t, (-1) ^ ((↑t).card + 1) * ↑((↑t).inf' ⋯ S).card
```

`Finset.inclusion_exclusion_sum_inf_compl`: **Inclusion-exclusion principle** for the sum of a function over an intersection of complements.

The sum of a function `f` over the intersection of the complements of the `S i` over `i ∈ s` is the
alternating sum of the sums of `f` over the intersections of the `S i`.

```lean
Finset.inclusion_exclusion_sum_inf_compl.{u_1, u_2, u_3} {ι : Type u_1} {α : Type u_2}
  {G : Type u_3} [AddCommGroup G] [DecidableEq α] [Fintype α] (s : Finset ι) (S : ι → Finset α)
  (f : α → G) :
  ∑ a ∈ s.inf fun i => (S i)ᶜ, f a = ∑ t ∈ s.powerset, (-1) ^ t.card • ∑ a ∈ t.inf S, f a
```

`Finset.inclusion_exclusion_card_inf_compl`: **Inclusion-exclusion principle** for the cardinality of an intersection of complements.

The cardinality of the intersection of the complements of the `S i` over `i ∈ s` is the
alternating sum of the cardinalities of the intersections of the `S i`.

```lean
Finset.inclusion_exclusion_card_inf_compl.{u_1, u_2} {ι : Type u_1} {α : Type u_2} [DecidableEq α]
  [Fintype α] (s : Finset ι) (S : ι → Finset α) :
  ↑(s.inf fun i => (S i)ᶜ).card = ∑ t ∈ s.powerset, (-1) ^ t.card * ↑(t.inf S).card
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Integer](../../overview/general-algebra/numbers/integer.md)
- [Set](../../overview/data-structures/sets/set.md)

## Proof depends on

- [Array](../../overview/data-structures/list-like-structures/array.md)
- [Module](../../overview/linear-algebra/fundamentals/module.md)
- [Ring morphism](../../overview/general-algebra/rings/ring-morphism.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `Finset.inclusion_exclusion_sum_biUnion`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/InclusionExclusion.html#Finset.inclusion_exclusion_sum_biUnion)
- [Source of `Finset.inclusion_exclusion_sum_biUnion` in Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean#L113)
- [Mathlib documentation: `Finset.inclusion_exclusion_card_biUnion`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/InclusionExclusion.html#Finset.inclusion_exclusion_card_biUnion)
- [Source of `Finset.inclusion_exclusion_card_biUnion` in Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean#L151)
- [Mathlib documentation: `Finset.inclusion_exclusion_sum_inf_compl`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/InclusionExclusion.html#Finset.inclusion_exclusion_sum_inf_compl)
- [Source of `Finset.inclusion_exclusion_sum_inf_compl` in Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean#L162)
- [Mathlib documentation: `Finset.inclusion_exclusion_card_inf_compl`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/InclusionExclusion.html#Finset.inclusion_exclusion_card_inf_compl)
- [Source of `Finset.inclusion_exclusion_card_inf_compl` in Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/InclusionExclusion.lean#L179)
- [Freek Wiedijk's 100 theorems, no. 96](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L492)
- [Outside Mathlib: github](https://github.com/NeilStrickland/lean_lib/blob/f88d162da2f990b87c4d34f5f46bbca2bbc5948e/src/combinatorics/matching.lean#L304)
