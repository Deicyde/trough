---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: card_sylow_modEq_one
mathlib_file: Mathlib/GroupTheory/Sylow.lean
---

# Third Sylow theorem

A generalization of **Sylow's third theorem**.
If the number of Sylow `p`-subgroups is finite, then it is congruent to `1` modulo `p`.

```lean
card_sylow_modEq_one.{u_1} (p : ℕ) (G : Type u_1) [Group G] [Fact (Nat.Prime p)]
  [Finite (Sylow p G)] : Nat.card (Sylow p G) ≡ 1 [MOD p]
```

## Depends on

- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)
- [Ring morphism](../../rings/ring-morphism.md)
- [Subgroup](../part-01/subgroup.md)

## Proof depends on

- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cauchy's theorem (group theory)](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/part-01/cauchys-theorem-group-theory.md)
- [Characteristic p](../../field-theory/characteristic-p.md)
- [Congruence in $\Z$](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in.md)
- [Finitely supported function](../../../data-structures/maps/finitely-supported-function.md)
- [First isomorphism theorem](../part-01/first-isomorphism-theorem.md)
- [Index of a subgroup](../part-01/index-of-a-subgroup.md)
- [Ordered ring](../../rings/ordered-ring.md)
- [Quotient space](../../../../undergraduate/group-theory/basic-definitions/quotient-space.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [The Fundamental Theorem of Arithmetic](../../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `card_sylow_modEq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#card_sylow_modEq_one)
- [Source of `card_sylow_modEq_one` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L373)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L62)
