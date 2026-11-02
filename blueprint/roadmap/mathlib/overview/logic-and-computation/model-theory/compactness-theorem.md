---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable
mathlib_file: Mathlib/ModelTheory/Satisfiability.lean
---

# Compactness theorem

The **Compactness Theorem of first-order logic**: A theory is satisfiable if and only if it is
finitely satisfiable.

```lean
FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable.{u, v} {L : FirstOrder.Language}
  {T : L.Theory} : T.IsSatisfiable ↔ T.IsFinitelySatisfiable
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Satisfiability](satisfiability.md)

## Proof depends on

- [Łoś' theorem](../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/os-theorem.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Satisfiability.html#FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable)
- [Source of `FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable` in Mathlib/ModelTheory/Satisfiability.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/ModelTheory/Satisfiability.lean#L99)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L642)
- [1000+ theorems list: Q1149458](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1453)
- [1000+ theorems project: Q1149458](https://1000-plus.github.io/all.html?length=-1#Q1149458)
- [Wikipedia: Compactness theorem](https://en.wikipedia.org/wiki/Compactness_theorem)
- [Wikidata: Q1149458](https://www.wikidata.org/wiki/Q1149458)
