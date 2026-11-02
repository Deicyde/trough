---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.Nat.eq_two_pow_mul_prime_mersenne_of_even_perfect
mathlib_file: Archive/Wiedijk100Theorems/PerfectNumbers.lean
---

# The Perfect Number Theorem

**Perfect Number Theorem**: Euler's theorem that even perfect numbers can be factored as a
power of two times a Mersenne prime.

```lean
Theorems100.Nat.eq_two_pow_mul_prime_mersenne_of_even_perfect {n : ℕ} (ev : Even n)
  (perf : n.Perfect) : ∃ k, Nat.Prime (mersenne (k + 1)) ∧ n = 2 ^ k * mersenne (k + 1)
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Set](../../overview/data-structures/sets/set.md)

## Proof depends on

- [Arithmetic functions](../../overview/general-algebra/number-theory/arithmetic-functions.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Group action](../../overview/general-algebra/group-theory/part-01/group-action.md)
- [Integer](../../overview/general-algebra/numbers/integer.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Prime numbers](../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)

## Sources

- [Mathlib documentation: `Theorems100.Nat.eq_two_pow_mul_prime_mersenne_of_even_perfect`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/PerfectNumbers.html#Theorems100.Nat.eq_two_pow_mul_prime_mersenne_of_even_perfect)
- [Source of `Theorems100.Nat.eq_two_pow_mul_prime_mersenne_of_even_perfect` in Archive/Wiedijk100Theorems/PerfectNumbers.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/PerfectNumbers.lean#L73)
- [Freek Wiedijk's 100 theorems, no. 70](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L354)
- [1000+ theorems list: Q18206266](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L4176)
- [1000+ theorems project: Q18206266](https://1000-plus.github.io/?length=-1#Q18206266)
- [Wikipedia: Euclid–Euler theorem](https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem)
- [Wikidata: Q18206266](https://www.wikidata.org/wiki/Q18206266)
