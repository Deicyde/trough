---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Sylow.exists_subgroup_card_pow_prime
mathlib_file: Mathlib/GroupTheory/Sylow.lean
---

# First Sylow theorem

A generalisation of **Sylow's first theorem**. If `p ^ n` divides
the cardinality of `G`, then there is a subgroup of cardinality `p ^ n`

```lean
Sylow.exists_subgroup_card_pow_prime.{u} {G : Type u} [Group G] [Finite G] (p : ℕ) {n : ℕ}
  [Fact (Nat.Prime p)] (hdvd : p ^ n ∣ Nat.card G) : ∃ K, Nat.card ↥K = p ^ n
```

Freek Wiedijk's list (no. 72) and the 1000+ list (Q1057919) also cite `Sylow.isPretransitive_of_finite`, `Sylow.card_dvd_index`, `card_sylow_modEq_one`.

## Depends on

- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)
- [Ring morphism](../../rings/ring-morphism.md)
- [Subgroup](../part-01/subgroup.md)

## Proof depends on

- [Cauchy's theorem (group theory)](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/part-01/cauchys-theorem-group-theory.md)
- [Index of a subgroup](../part-01/index-of-a-subgroup.md)
- [Quotient group](../part-01/quotient-group.md)

## Sources

- [Mathlib documentation: `Sylow.exists_subgroup_card_pow_prime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.exists_subgroup_card_pow_prime)
- [Source of `Sylow.exists_subgroup_card_pow_prime` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L721)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L60)
- [Freek Wiedijk's 100 theorems, no. 72](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L362)
- [1000+ theorems list: Q1057919](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1269)
- [1000+ theorems project: Q1057919](https://1000-plus.github.io/all.html?length=-1#Q1057919)
- [Wikipedia: Sylow theorems](https://en.wikipedia.org/wiki/Sylow_theorems)
- [Wikidata: Q1057919](https://www.wikidata.org/wiki/Q1057919)
