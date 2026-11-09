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

- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `Choose.lucas_theorem`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Lucas.html#Choose.lucas_theorem)
- [Source of `Choose.lucas_theorem` in Mathlib/Data/Nat/Choose/Lucas.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Data/Nat/Choose/Lucas.lean#L102)
- [1000+ theorems list: Q1186808](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1487)
- [1000+ theorems project: Q1186808](https://1000-plus.github.io/all.html?length=-1#Q1186808)
- [Wikipedia: Lucas's theorem](https://en.wikipedia.org/wiki/Lucas's_theorem)
- [Wikidata: Q1186808](https://www.wikidata.org/wiki/Q1186808)
