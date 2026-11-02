---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: lucas_lehmer_sufficiency
mathlib_file: Mathlib/NumberTheory/LucasLehmer.lean
---

# Lucas-Lehmer primality test

**Lucas–Lehmer primality test**: sufficiency direction.

```lean
lucas_lehmer_sufficiency (p : ℕ) (w : 1 < p) : LucasLehmerTest p → Nat.Prime (mersenne p)
```

## Depends on

- [Irreducible element](irreducible-element.md)
- [Ring](../rings/ring.md)

## Proof depends on

- [Characteristic zero](../field-theory/characteristic-zero.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Group morphism](../group-theory/part-01/group-morphism.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Ordered ring](../rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `lucas_lehmer_sufficiency`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#lucas_lehmer_sufficiency)
- [Source of `lucas_lehmer_sufficiency` in Mathlib/NumberTheory/LucasLehmer.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/LucasLehmer.lean#L582)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L93)
