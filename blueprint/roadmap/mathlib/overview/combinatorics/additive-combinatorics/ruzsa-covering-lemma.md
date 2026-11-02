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
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Group](../../general-algebra/group-theory/part-01/group.md)
- [Invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of rings](../../../undergraduate/ring-theory/fundamentals/product-of-rings.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)

## Sources

- [Mathlib documentation: `Set.ruzsa_covering_add`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/RuzsaCovering.html#Set.ruzsa_covering_add)
- [Source of `Set.ruzsa_covering_add` in Mathlib/Combinatorics/Additive/RuzsaCovering.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/RuzsaCovering.lean#L65)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L545)
