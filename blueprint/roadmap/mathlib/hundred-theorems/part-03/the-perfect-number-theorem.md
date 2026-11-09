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
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Arithmetic functions](../../overview/general-algebra/number-theory/arithmetic-functions.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Theorems100.Nat.eq_two_pow_mul_prime_mersenne_of_even_perfect`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/PerfectNumbers.html#Theorems100.Nat.eq_two_pow_mul_prime_mersenne_of_even_perfect)
- [Source of `Theorems100.Nat.eq_two_pow_mul_prime_mersenne_of_even_perfect` in Archive/Wiedijk100Theorems/PerfectNumbers.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Archive/Wiedijk100Theorems/PerfectNumbers.lean#L73)
- [Freek Wiedijk's 100 theorems, no. 70](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L354)
- [1000+ theorems list: Q18206266](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L4176)
- [1000+ theorems project: Q18206266](https://1000-plus.github.io/all.html?length=-1#Q18206266)
- [Wikipedia: Euclid–Euler theorem](https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem)
- [Wikidata: Q18206266](https://www.wikidata.org/wiki/Q18206266)
