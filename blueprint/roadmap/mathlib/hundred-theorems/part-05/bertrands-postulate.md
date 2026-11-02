---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.bertrand
mathlib_file: Mathlib/NumberTheory/Bertrand.lean
---

# Bertrand’s Postulate

**Alias** of `Nat.exists_prime_lt_and_le_two_mul`.

---

**Bertrand's Postulate**: For any positive natural number, there is a prime which is greater than
it, but no more than twice as large.

```lean
Nat.bertrand (n : ℕ) (hn0 : n ≠ 0) : ∃ p, Nat.Prime p ∧ n < p ∧ p ≤ 2 * n
```

## Depends on

- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Convex function](../../overview/analysis/convexity/convex-function.md)
- [Finitely supported function](../../overview/data-structures/maps/finitely-supported-function.md)
- [Linear map](../../overview/linear-algebra/fundamentals/linear-map.md)
- [Power functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)

## Sources

- [Mathlib documentation: `Nat.bertrand`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Bertrand.html#Nat.bertrand)
- [Source of `Nat.bertrand` in Mathlib/NumberTheory/Bertrand.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Bertrand.lean#L243)
- [Freek Wiedijk's 100 theorems, no. 98](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L506)
- [1000+ theorems list: Q632546](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L647)
- [1000+ theorems project: Q632546](https://1000-plus.github.io/all.html?length=-1#Q632546)
- [Wikipedia: Bertrand's postulate](https://en.wikipedia.org/wiki/Bertrand's_postulate)
- [Wikidata: Q632546](https://www.wikidata.org/wiki/Q632546)
