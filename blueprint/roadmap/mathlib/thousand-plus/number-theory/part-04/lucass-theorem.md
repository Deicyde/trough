---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Choose.lucas_theorem
mathlib_file: Mathlib/Data/Nat/Choose/Lucas.lean
---

# Lucas's theorem

**Alias** of `Choose.choose_modEq_prod_range_choose`.

---

**Lucas's Theorem**: For primes `p`, `choose n k` is congruent to the product of
`choose (⌊n / p ^ i⌋ % p) (⌊k / p ^ i⌋ % p)` over `i` modulo `p`.

```lean
Choose.lucas_theorem {n k p : ℕ} [Fact (Nat.Prime p)] {a : ℕ} (ha₁ : n < p ^ a) (ha₂ : k < p ^ a) :
  ↑(n.choose k) ≡ ∏ i ∈ Finset.range a, ↑((n / p ^ i % p).choose (k / p ^ i % p)) [ZMOD ↑p]
```

## Depends on

- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)
- [The Binomial Theorem](../../../hundred-theorems/part-03/the-binomial-theorem.md)

## Sources

- [Mathlib documentation: `Choose.lucas_theorem`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Lucas.html#Choose.lucas_theorem)
- [Source of `Choose.lucas_theorem` in Mathlib/Data/Nat/Choose/Lucas.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Nat/Choose/Lucas.lean#L102)
- [1000+ theorems list: Q1186808](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1487)
- [1000+ theorems project: Q1186808](https://1000-plus.github.io/?length=-1#Q1186808)
- [Wikipedia: Lucas's theorem](https://en.wikipedia.org/wiki/Lucas's_theorem)
- [Wikidata: Q1186808](https://www.wikidata.org/wiki/Q1186808)
