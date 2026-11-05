---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Bernoulli.vonStaudt_clausen
mathlib_file: Mathlib/NumberTheory/Bernoulli.lean
---

# Von Staudt–Clausen theorem

**von Staudt-Clausen theorem:** For any natural number $k$, the sum
$$B_{2k} + \sum_{p - 1 \mid 2k} \frac{1}{p}$$ is an integer.

```lean
Bernoulli.vonStaudt_clausen (k : ℕ) :
  bernoulli (2 * k) + ∑ p ∈ Finset.range (2 * k + 2) with Nat.Prime p ∧ p - 1 ∣ 2 * k, 1 / ↑p ∈
    Set.range Int.cast
```

## Depends on

- [Bernoulli numbers](../../../overview/general-algebra/number-theory/bernoulli-numbers.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Subring](../../../overview/general-algebra/rings/subring.md)
- [Sum of kth powers](../../../hundred-theorems/part-04/sum-of-kth-powers.md)

## Sources

- [Mathlib documentation: `Bernoulli.vonStaudt_clausen`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Bernoulli.html#Bernoulli.vonStaudt_clausen)
- [Source of `Bernoulli.vonStaudt_clausen` in Mathlib/NumberTheory/Bernoulli.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Bernoulli.lean#L666)
- [1000+ theorems list: Q3527230](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2565)
- [1000+ theorems project: Q3527230](https://1000-plus.github.io/all.html?length=-1#Q3527230)
- [Wikipedia: Von Staudt–Clausen theorem](https://en.wikipedia.org/wiki/Von_Staudt%E2%80%93Clausen_theorem)
- [Wikidata: Q3527230](https://www.wikidata.org/wiki/Q3527230)
