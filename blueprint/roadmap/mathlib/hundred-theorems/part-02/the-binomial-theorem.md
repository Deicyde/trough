# The Binomial Theorem

The **binomial theorem**

```lean
add_pow.{u_1} {R : Type u_1} [CommSemiring R] (x y : R) (n : ℕ) :
  (x + y) ^ n = ∑ m ∈ Finset.range (n + 1), x ^ m * y ^ (n - m) * ↑(n.choose m)
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `add_pow`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Sum.html#add_pow)
- [Source of `add_pow` in Mathlib/Data/Nat/Choose/Sum.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Nat/Choose/Sum.lean#L75)
- [Freek Wiedijk's 100 theorems, no. 44](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L235)
- [1000+ theorems list: Q26708](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L22)
- [1000+ theorems project: Q26708](https://1000-plus.github.io/all.html?length=-1#Q26708)
- [Wikipedia: Binomial theorem](https://en.wikipedia.org/wiki/Binomial_theorem)
- [Wikidata: Q26708](https://www.wikidata.org/wiki/Q26708)
