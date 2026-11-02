---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.gcd_eq_gcd_ab
mathlib_file: Mathlib/Data/Int/GCD.lean
---

# Bezout’s Theorem

**Bézout's lemma**: given `x y : ℕ`, `gcd x y = x * a + y * b`, where `a = gcd_a x y` and
`b = gcd_b x y` are computed by the extended Euclidean algorithm.

```lean
Nat.gcd_eq_gcd_ab (x y : ℕ) : ↑(x.gcd y) = ↑x * x.gcdA y + ↑y * x.gcdB y
```

## Depends on

- [Euclid's' algorithm](../../overview/general-algebra/divisibility-in-integral-domains/euclids-algorithm.md)

## Sources

- [Mathlib documentation: `Nat.gcd_eq_gcd_ab`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.gcd_eq_gcd_ab)
- [Source of `Nat.gcd_eq_gcd_ab` in Mathlib/Data/Int/GCD.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Int/GCD.lean#L121)
- [Freek Wiedijk's 100 theorems, no. 60](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L307)
- [1000+ theorems list: Q513028](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3040)
- [1000+ theorems project: Q513028](https://1000-plus.github.io/?length=-1#Q513028)
- [Wikidata: Q513028](https://www.wikidata.org/wiki/Q513028)
