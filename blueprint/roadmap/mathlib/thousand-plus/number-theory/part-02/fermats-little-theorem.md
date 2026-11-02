---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ZMod.pow_card_sub_one_eq_one
mathlib_file: Mathlib/FieldTheory/Finite/Basic.lean
---

# Fermat's little theorem

**Fermat's Little Theorem**: for all nonzero `a : ZMod p`, we have `a ^ (p - 1) = 1`.

```lean
ZMod.pow_card_sub_one_eq_one {p : ℕ} [Fact (Nat.Prime p)] {a : ZMod p} (ha : a ≠ 0) :
  a ^ (p - 1) = 1
```

## Depends on

- [Euclid's' algorithm](../../../overview/general-algebra/divisibility-in-integral-domains/euclids-algorithm.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Proof depends on

- [Bezout’s Theorem](../../../hundred-theorems/part-03/bezouts-theorem.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Group action](../../../overview/general-algebra/group-theory/part-01/group-action.md)
- [Orbit](../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `ZMod.pow_card_sub_one_eq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#ZMod.pow_card_sub_one_eq_one)
- [Source of `ZMod.pow_card_sub_one_eq_one` in Mathlib/FieldTheory/Finite/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/Finite/Basic.lean#L579)
- [1000+ theorems list: Q188295](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L117)
- [1000+ theorems project: Q188295](https://1000-plus.github.io/?length=-1#Q188295)
- [Wikipedia: Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat's_little_theorem)
- [Wikidata: Q188295](https://www.wikidata.org/wiki/Q188295)
