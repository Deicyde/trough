# NFA

An NFA is a set of states (`σ`), a transition function from state to state labelled by the
alphabet (`step`), a set of starting states (`start`) and a set of acceptance states (`accept`).
Note the transition function sends a state to a `Set` of states. These are the states that it
may be sent to.

```lean
NFA.{u, v} (α : Type u) (σ : Type v) : Type (max u v)
```

## Depends on

- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `NFA`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/NFA.html#NFA)
- [Source of `NFA` in Mathlib/Computability/NFA.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Computability/NFA.lean#L51)
- [Mathlib overview: Logic and computation › Formal languages](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L617)
