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
- [Source of `Nat.gcd_eq_gcd_ab` in Mathlib/Data/Int/GCD.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Data/Int/GCD.lean#L121)
- [Freek Wiedijk's 100 theorems, no. 60](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L307)
- [1000+ theorems list: Q513028](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L3040)
- [1000+ theorems project: Q513028](https://1000-plus.github.io/all.html?length=-1#Q513028)
- [Wikidata: Q513028](https://www.wikidata.org/wiki/Q513028)
