---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.Prime.sq_add_sq
mathlib_file: Mathlib/NumberTheory/SumTwoSquares.lean
---

# Sum of two squares

**Fermat's theorem on the sum of two squares**. Every prime not congruent to 3 mod 4 is the sum
of two squares. Also known as **Fermat's Christmas theorem**.

```lean
Nat.Prime.sq_add_sq {p : ℕ} [Fact (Nat.Prime p)] (hp : p % 4 ≠ 3) : ∃ a b, a ^ 2 + b ^ 2 = p
```

## Depends on

- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Field $\Q$ of rational numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-q-of-rational-numbers.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Nat.Prime.sq_add_sq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.Prime.sq_add_sq)
- [Source of `Nat.Prime.sq_add_sq` in Mathlib/NumberTheory/SumTwoSquares.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/SumTwoSquares.lean#L34)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L142)
- [Freek Wiedijk's 100 theorems, no. 20](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L99)
- [1000+ theorems list: Q914517](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1070)
- [1000+ theorems project: Q914517](https://1000-plus.github.io/all.html?length=-1#Q914517)
- [Wikipedia: Fermat's theorem on sums of two squares](https://en.wikipedia.org/wiki/Fermat's_theorem_on_sums_of_two_squares)
- [Wikidata: Q914517](https://www.wikidata.org/wiki/Q914517)
