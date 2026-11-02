---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Sylow.exists_subgroup_card_pow_prime, Sylow.isPretransitive_of_finite, Sylow.card_dvd_index, card_sylow_modEq_one
mathlib_file: Mathlib/GroupTheory/Sylow.lean
---

# First Sylow theorem

Mathlib records this with 4 declarations.

`Sylow.exists_subgroup_card_pow_prime`: A generalisation of **Sylow's first theorem**. If `p ^ n` divides
the cardinality of `G`, then there is a subgroup of cardinality `p ^ n`

```lean
Sylow.exists_subgroup_card_pow_prime.{u} {G : Type u} [Group G] [Finite G] (p : ℕ) {n : ℕ}
  [Fact (Nat.Prime p)] (hdvd : p ^ n ∣ Nat.card G) : ∃ K, Nat.card ↥K = p ^ n
```

`Sylow.isPretransitive_of_finite`: A generalization of **Sylow's second theorem**.
If the number of Sylow `p`-subgroups is finite, then all Sylow `p`-subgroups are conjugate.

```lean
Sylow.isPretransitive_of_finite.{u_1} {p : ℕ} {G : Type u_1} [Group G] [hp : Fact (Nat.Prime p)]
  [Finite (Sylow p G)] : MulAction.IsPretransitive G (Sylow p G)
```

`Sylow.card_dvd_index`.

```lean
Sylow.card_dvd_index.{u_1} {p : ℕ} {G : Type u_1} [Group G] [Fact (Nat.Prime p)]
  [Finite (Sylow p G)] (P : Sylow p G) : Nat.card (Sylow p G) ∣ (↑P).index
```

`card_sylow_modEq_one`: A generalization of **Sylow's third theorem**.
If the number of Sylow `p`-subgroups is finite, then it is congruent to `1` modulo `p`.

```lean
card_sylow_modEq_one.{u_1} (p : ℕ) (G : Type u_1) [Group G] [Fact (Nat.Prime p)]
  [Finite (Sylow p G)] : Nat.card (Sylow p G) ≡ 1 [MOD p]
```

## Depends on

- [Index of a subgroup](../part-01/index-of-a-subgroup.md)
- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Second Sylow theorem](second-sylow-theorem.md)

## Sources

- [Mathlib documentation: `Sylow.exists_subgroup_card_pow_prime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.exists_subgroup_card_pow_prime)
- [Source of `Sylow.exists_subgroup_card_pow_prime` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L721)
- [Mathlib documentation: `Sylow.isPretransitive_of_finite`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.isPretransitive_of_finite)
- [Source of `Sylow.isPretransitive_of_finite` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L345)
- [Mathlib documentation: `Sylow.card_dvd_index`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.card_dvd_index)
- [Source of `Sylow.card_dvd_index` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L459)
- [Mathlib documentation: `card_sylow_modEq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#card_sylow_modEq_one)
- [Source of `card_sylow_modEq_one` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L373)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L60)
- [Freek Wiedijk's 100 theorems, no. 72](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L362)
- [1000+ theorems list: Q1057919](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1269)
- [1000+ theorems project: Q1057919](https://1000-plus.github.io/?length=-1#Q1057919)
- [Wikipedia: Sylow theorems](https://en.wikipedia.org/wiki/Sylow_theorems)
- [Wikidata: Q1057919](https://www.wikidata.org/wiki/Q1057919)
