---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Set.ruzsa_covering_add
mathlib_file: Mathlib/Combinatorics/Additive/RuzsaCovering.lean
---

# Ruzsa covering lemma

**Ruzsa's covering lemma** for sets. See also `Finset.ruzsa_covering_add`.

```lean
Set.ruzsa_covering_add.{u_1} {G : Type u_1} [AddGroup G] {K : ℝ} {A B : Set G} (hA : A.Finite)
  (hB : B.Finite) (hB₀ : B.Nonempty) (hK : ↑(Nat.card ↑(A + B)) ≤ K * ↑(Nat.card ↑B)) :
  ∃ F ⊆ A, ↑(Nat.card ↑F) ≤ K ∧ A ⊆ F + (B - B) ∧ F.Finite
```

## Depends on

- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Real number](../../general-algebra/numbers/real-number.md)
- [Ring morphism](../../general-algebra/rings/ring-morphism.md)

## Proof depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Sources

- [Mathlib documentation: `Set.ruzsa_covering_add`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/RuzsaCovering.html#Set.ruzsa_covering_add)
- [Source of `Set.ruzsa_covering_add` in Mathlib/Combinatorics/Additive/RuzsaCovering.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/RuzsaCovering.lean#L65)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L545)
