---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Function.Embedding.schroeder_bernstein
mathlib_file: Mathlib/SetTheory/Cardinal/SchroederBernstein.lean
---

# Schroeder-Bernstein Theorem

**The Schröder-Bernstein Theorem**:
Given injections `α → β` and `β → α`, we can get a bijection `α → β`.

```lean
Function.Embedding.schroeder_bernstein.{u, v} {α : Type u} {β : Type v} {f : α → β} {g : β → α}
  (hf : Function.Injective f) (hg : Function.Injective g) : ∃ h, Function.Bijective h
```

## Depends on

Its statement uses no other concept on these lists.

## Proof depends on

- [Set](../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Function.Embedding.schroeder_bernstein`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/SchroederBernstein.html#Function.Embedding.schroeder_bernstein)
- [Source of `Function.Embedding.schroeder_bernstein` in Mathlib/SetTheory/Cardinal/SchroederBernstein.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/SetTheory/Cardinal/SchroederBernstein.lean#L88)
- [Freek Wiedijk's 100 theorems, no. 25](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L123)
- [1000+ theorems list: Q1033910](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1209)
- [1000+ theorems project: Q1033910](https://1000-plus.github.io/all.html?length=-1#Q1033910)
- [Wikipedia: Cantor–Bernstein–Schroeder theorem](https://en.wikipedia.org/wiki/Cantor%E2%80%93Bernstein%E2%80%93Schroeder_theorem)
- [Wikidata: Q1033910](https://www.wikidata.org/wiki/Q1033910)
