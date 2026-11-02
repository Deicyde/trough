---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.infinite_setOfPred_prime_and_eq_mod
mathlib_file: Mathlib/NumberTheory/LSeries/PrimesInAP.lean
---

# Dirichlet’s Theorem

**Dirichlet's Theorem** on primes in arithmetic progression: if `q` is a positive
integer and `a : ZMod q` is a unit, then there are infinitely many prime numbers `p`
such that `(p : ZMod q) = a`.

```lean
Nat.infinite_setOfPred_prime_and_eq_mod {q : ℕ} [NeZero q] {a : ZMod q} (ha : IsUnit a) :
  {p | Nat.Prime p ∧ ↑p = a}.Infinite
```

## Depends on

- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Ring](../../overview/general-algebra/rings/ring.md)
- [Set](../../overview/data-structures/sets/set.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Arithmetic functions](../../overview/general-algebra/number-theory/arithmetic-functions.md)
- [Bezout’s Theorem](bezouts-theorem.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Cyclic group](../../overview/general-algebra/group-theory/part-01/cyclic-group.md)
- [Divergence of the Prime Reciprocal Series](../part-05/divergence-of-the-prime-reciprocal-series.md)
- [Euler's totient function ($\varphi$)](../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Extended real number](../../overview/general-algebra/numbers/extended-real-number.md)
- [Fundamental theorem of algebra](../../overview/analysis/complex-analysis/fundamental-theorem-of-algebra.md)
- [Invertible elements](../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Prime numbers](../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Separable polynomial](../../overview/general-algebra/polynomials-and-power-series/separable-polynomial.md)
- [Subgroup](../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `Nat.infinite_setOfPred_prime_and_eq_mod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/PrimesInAP.html#Nat.infinite_setOfPred_prime_and_eq_mod)
- [Source of `Nat.infinite_setOfPred_prime_and_eq_mod` in Mathlib/NumberTheory/LSeries/PrimesInAP.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/LSeries/PrimesInAP.lean#L428)
- [Freek Wiedijk's 100 theorems, no. 48](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L251)
- [1000+ theorems list: Q550402](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L555)
- [1000+ theorems project: Q550402](https://1000-plus.github.io/all.html?length=-1#Q550402)
- [Wikipedia: Dirichlet's theorem on arithmetic progressions](https://en.wikipedia.org/wiki/Dirichlet's_theorem_on_arithmetic_progressions)
- [Wikidata: Q550402](https://www.wikidata.org/wiki/Q550402)
