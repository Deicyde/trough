---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: FirstOrder.Language.exists_elementaryEmbedding_card_eq
mathlib_file: Mathlib/ModelTheory/Satisfiability.lean
---

# Löwenheim-Skolem

The Löwenheim–Skolem Theorem: If `κ` is a cardinal greater than the cardinalities of `L`
and an infinite `L`-structure `M`, then there is an elementary embedding in the appropriate
direction between then `M` and a structure of cardinality `κ`.

```lean
FirstOrder.Language.exists_elementaryEmbedding_card_eq.{u, v, w, w'} (L : FirstOrder.Language)
  (M : Type w') [L.Structure M] [iM : Infinite M] (κ : Cardinal.{w}) (h1 : Cardinal.aleph0 ≤ κ)
  (h2 : Cardinal.lift.{w, max u v} L.card ≤ Cardinal.lift.{max u v, w} κ) :
  ∃ N,
    (Nonempty (L.ElementaryEmbedding (↑N) M) ∨ Nonempty (L.ElementaryEmbedding M ↑N)) ∧
      Cardinal.mk ↑N = κ
```

## Depends on

- [Cardinal](../set-theory/cardinals/cardinal.md)
- [Elementary embedding](elementary-embedding.md)

## Proof depends on

- [Compactness theorem](compactness-theorem.md)
- [Ordinal](../set-theory/ordinals/ordinal.md)
- [Substructure](substructure.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.exists_elementaryEmbedding_card_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Satisfiability.html#FirstOrder.Language.exists_elementaryEmbedding_card_eq)
- [Source of `FirstOrder.Language.exists_elementaryEmbedding_card_eq` in Mathlib/ModelTheory/Satisfiability.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/ModelTheory/Satisfiability.lean#L238)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L643)
- [1000+ theorems list: Q1068283](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1313)
- [1000+ theorems project: Q1068283](https://1000-plus.github.io/all.html?length=-1#Q1068283)
- [Wikipedia: Löwenheim–Skolem theorem](https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem)
- [Wikidata: Q1068283](https://www.wikidata.org/wiki/Q1068283)
