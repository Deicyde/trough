---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Cardinal.sum_lt_prod
mathlib_file: Mathlib/SetTheory/Cardinal/Order.lean
---

# König's theorem (set theory)

**König's theorem**

```lean
Cardinal.sum_lt_prod.{u_1, u_2} {ι : Type u_1} (f g : ι → Cardinal.{u_2})
  (H : ∀ (i : ι), f i < g i) : Cardinal.sum f < Cardinal.prod g
```

## Depends on

- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)

## Proof depends on

- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)

## Sources

- [Mathlib documentation: `Cardinal.sum_lt_prod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Order.html#Cardinal.sum_lt_prod)
- [Source of `Cardinal.sum_lt_prod` in Mathlib/SetTheory/Cardinal/Order.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/SetTheory/Cardinal/Order.lean#L550)
- [1000+ theorems list: Q1077462](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1331)
- [1000+ theorems project: Q1077462](https://1000-plus.github.io/?length=-1#Q1077462)
- [Wikipedia: König's theorem (set theory)](https://en.wikipedia.org/wiki/K%C3%B6nig's_theorem_%28set_theory%29)
- [Wikidata: Q1077462](https://www.wikidata.org/wiki/Q1077462)
