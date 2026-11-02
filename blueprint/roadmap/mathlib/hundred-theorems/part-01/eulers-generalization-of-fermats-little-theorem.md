---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.ModEq.pow_totient
mathlib_file: Mathlib/FieldTheory/Finite/Basic.lean
---

# Euler’s Generalization of Fermat’s Little Theorem

The **Fermat-Euler totient theorem**. `ZMod.pow_totient` is an alternative statement
of the same theorem.

```lean
Nat.ModEq.pow_totient {x n : ℕ} (h : x.Coprime n) : x ^ n.totient ≡ 1 [MOD n]
```

## Depends on

- [Array](../../overview/data-structures/list-like-structures/array.md)
- [Euler's totient function ($\varphi$)](../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function.md)

## Proof depends on

- [$\Z/n\Z$ and its invertible elements](../../undergraduate/ring-theory/divisibility-in-integral-domains/n-and-its-invertible-elements.md)
- [Cantor’s Theorem](../part-04/cantors-theorem.md)
- [Cardinal](../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Congruence in $\Z$](../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in.md)
- [Group action](../../overview/general-algebra/group-theory/part-01/group-action.md)
- [Orbit](../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Order of an element](../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Ring morphism](../../overview/general-algebra/rings/ring-morphism.md)
- [Schroeder-Bernstein Theorem](../part-02/schroeder-bernstein-theorem.md)
- [Subgroup](../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `Nat.ModEq.pow_totient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#Nat.ModEq.pow_totient)
- [Source of `Nat.ModEq.pow_totient` in Mathlib/FieldTheory/Finite/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/Finite/Basic.lean#L530)
- [Freek Wiedijk's 100 theorems, no. 10](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L54)
- [1000+ theorems list: Q193910](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L182)
- [1000+ theorems project: Q193910](https://1000-plus.github.io/?length=-1#Q193910)
- [Wikipedia: Euler's theorem](https://en.wikipedia.org/wiki/Euler's_theorem)
- [Wikidata: Q193910](https://www.wikidata.org/wiki/Q193910)
