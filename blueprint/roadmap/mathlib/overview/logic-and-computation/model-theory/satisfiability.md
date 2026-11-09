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
- [Source of `FirstOrder.Language.Theory.IsSatisfiable` in Mathlib/ModelTheory/Satisfiability.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/ModelTheory/Satisfiability.lean#L65)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L638)
