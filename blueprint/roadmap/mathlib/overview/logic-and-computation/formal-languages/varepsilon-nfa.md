# $\varepsilon$-NFA

An `εNFA` is a set of states (`σ`), a transition function from state to state labelled by the
alphabet (`step`), a starting state (`start`) and a set of acceptance states (`accept`).
Note the transition function sends a state to a `Set` of states and can make ε-transitions by
inputting `none`.
Since this definition allows for Automata with infinite states, a `Fintype` instance must be
supplied for true `εNFA`'s.

```lean
εNFA.{u, v} (α : Type u) (σ : Type v) : Type (max u v)
```

## Depends on

- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `εNFA`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/EpsilonNFA.html#%CE%B5NFA)
- [Source of `εNFA` in Mathlib/Computability/EpsilonNFA.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Computability/EpsilonNFA.lean#L34)
- [Mathlib overview: Logic and computation › Formal languages](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L618)
