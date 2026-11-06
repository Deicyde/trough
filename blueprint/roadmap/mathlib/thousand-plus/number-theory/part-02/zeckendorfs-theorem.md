# Zeckendorf's theorem

**Zeckendorf's Theorem** as an equivalence between natural numbers and Zeckendorf
representations. Every natural number can be written uniquely as a sum of non-consecutive Fibonacci
numbers (if we forget about the first two terms `F₀ = 0`, `F₁ = 1`).

```lean
Nat.zeckendorfEquiv : ℕ ≃ { l // l.IsZeckendorfRep }
```

## Depends on

- [List](../../../overview/data-structures/list-like-structures/list.md)
- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Nat.zeckendorfEquiv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Fib/Zeckendorf.html#Nat.zeckendorfEquiv)
- [Source of `Nat.zeckendorfEquiv` in Mathlib/Data/Nat/Fib/Zeckendorf.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Nat/Fib/Zeckendorf.lean#L172)
- [1000+ theorems list: Q1188392](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1499)
- [1000+ theorems project: Q1188392](https://1000-plus.github.io/all.html?length=-1#Q1188392)
- [Wikipedia: Zeckendorf's theorem](https://en.wikipedia.org/wiki/Zeckendorf's_theorem)
- [Wikidata: Q1188392](https://www.wikidata.org/wiki/Q1188392)
