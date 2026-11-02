---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ComputablePred.rice
mathlib_file: Mathlib/Computability/Halting.lean
---

# Rice theorem

**Rice's Theorem**

```lean
ComputablePred.rice (C : Set (ℕ →. ℕ)) (h : ComputablePred fun c => c.eval ∈ C) {f g : ℕ →. ℕ}
  (hf : Nat.Partrec f) (hg : Nat.Partrec g) (fC : f ∈ C) : g ∈ C
```

## Depends on

- [In terms of general recursive functions](computable-function/in-terms-of-general-recursive-functions.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Kleene's recursion theorem](../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-02/kleenes-recursion-theorem.md)

## Sources

- [Mathlib documentation: `ComputablePred.rice`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/Halting.html#ComputablePred.rice)
- [Source of `ComputablePred.rice` in Mathlib/Computability/Halting.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/Halting.lean#L31)
- [Mathlib overview: Logic and computation › Computability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L608)
- [1000+ theorems list: Q1893717](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1924)
- [1000+ theorems project: Q1893717](https://1000-plus.github.io/?length=-1#Q1893717)
- [Wikipedia: Rice's theorem](https://en.wikipedia.org/wiki/Rice's_theorem)
- [Wikidata: Q1893717](https://www.wikidata.org/wiki/Q1893717)
