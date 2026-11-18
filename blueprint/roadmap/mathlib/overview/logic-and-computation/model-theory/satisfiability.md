# Satisfiability

A theory is satisfiable if a structure models it.

```lean
FirstOrder.Language.Theory.IsSatisfiable.{u, v} {L : FirstOrder.Language} (T : L.Theory) : Prop
```

## Depends on

- [First-order formula](first-order-formula.md)
- [First-order structure](first-order-structure.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.Theory.IsSatisfiable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Satisfiability.html#FirstOrder.Language.Theory.IsSatisfiable)
- [Source of `FirstOrder.Language.Theory.IsSatisfiable` in Mathlib/ModelTheory/Satisfiability.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/ModelTheory/Satisfiability.lean#L65)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L638)
