---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: FirstOrder.Language.Theory.IsSatisfiable
mathlib_file: Mathlib/ModelTheory/Satisfiability.lean
---

# Satisfiability

A theory is satisfiable if a structure models it.

```lean
FirstOrder.Language.Theory.IsSatisfiable.{u, v} {L : FirstOrder.Language} (T : L.Theory) : Prop
```

## Depends on

- [First-order formula](first-order-formula.md)
- [First-order structure](first-order-structure.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.Theory.IsSatisfiable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Satisfiability.html#FirstOrder.Language.Theory.IsSatisfiable)
- [Source of `FirstOrder.Language.Theory.IsSatisfiable` in Mathlib/ModelTheory/Satisfiability.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/ModelTheory/Satisfiability.lean#L65)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L638)
