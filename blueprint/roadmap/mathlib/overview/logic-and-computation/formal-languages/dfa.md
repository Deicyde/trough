# DFA

A DFA is a set of states (`σ`), a transition function from state to state labelled by the
alphabet (`step`), a starting state (`start`) and a set of acceptance states (`accept`).

```lean
DFA.{u, v} (α : Type u) (σ : Type v) : Type (max u v)
```

## Depends on

- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `DFA`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/DFA.html#DFA)
- [Source of `DFA` in Mathlib/Computability/DFA.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/DFA.lean#L57)
- [Mathlib overview: Logic and computation › Formal languages](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L616)
