---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.erdos_szekeres
mathlib_file: Archive/Wiedijk100Theorems/AscendingDescendingSequences.lean
---

# Ascending or Descending Sequences (Erdős–Szekeres Theorem)

**Erdős–Szekeres Theorem**: Given a sequence of more than `r * s` distinct values, there is an
increasing sequence of length longer than `r` or a decreasing sequence of length longer than `s`.

Proof idea:
We label each value in the sequence with two numbers specifying the longest increasing
subsequence ending there, and the longest decreasing subsequence ending there.
We then show the pair of labels must be unique. Now if there is no increasing sequence longer than
`r` and no decreasing sequence longer than `s`, then there are at most `r * s` possible labels,
which is a contradiction if there are more than `r * s` elements.

```lean
Theorems100.erdos_szekeres.{u_1, u_2} {α : Type u_1} {β : Type u_2} [Fintype α] [LinearOrder α]
  [LinearOrder β] {r s : ℕ} {f : α → β} (hn : r * s < Fintype.card α) (hf : Function.Injective f) :
  (∃ t, r < t.card ∧ StrictMonoOn f ↑t) ∨ ∃ t, s < t.card ∧ StrictAntiOn f ↑t
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)
- [Set](../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Theorems100.erdos_szekeres`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/AscendingDescendingSequences.html#Theorems100.erdos_szekeres)
- [Source of `Theorems100.erdos_szekeres` in Archive/Wiedijk100Theorems/AscendingDescendingSequences.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/AscendingDescendingSequences.lean#L132)
- [Freek Wiedijk's 100 theorems, no. 73](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L370)
- [1000+ theorems list: Q976607](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1171)
- [1000+ theorems project: Q976607](https://1000-plus.github.io/all.html?length=-1#Q976607)
- [Wikipedia: Erdős–Szekeres theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem)
- [Wikidata: Q976607](https://www.wikidata.org/wiki/Q976607)
