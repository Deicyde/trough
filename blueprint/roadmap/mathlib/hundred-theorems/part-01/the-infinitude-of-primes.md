# The Infinitude of Primes

Euclid's theorem on the **infinitude of primes**.
Here given in the form: for every `n`, there exists a prime number `p ≥ n`.

```lean
Nat.exists_infinite_primes (n : ℕ) : ∃ p, n ≤ p ∧ Nat.Prime p
```

## Depends on

- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Nat.exists_infinite_primes`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Prime/Infinite.html#Nat.exists_infinite_primes)
- [Source of `Nat.exists_infinite_primes` in Mathlib/Data/Nat/Prime/Infinite.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Nat/Prime/Infinite.lean#L33)
- [Freek Wiedijk's 100 theorems, no. 11](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/100.yaml#L58)
- [1000+ theorems list: Q1506253](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L1732)
- [1000+ theorems project: Q1506253](https://1000-plus.github.io/all.html?length=-1#Q1506253)
- [Wikipedia: Euclid's theorem](https://en.wikipedia.org/wiki/Euclid's_theorem)
- [Wikidata: Q1506253](https://www.wikidata.org/wiki/Q1506253)
