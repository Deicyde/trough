# Halting problem

The **Halting problem** is not computable

```lean
ComputablePred.halting_problem (n : ℕ) : ¬ComputablePred fun c => (c.eval n).Dom
```

## Depends on

- [In terms of general recursive functions](computable-function/in-terms-of-general-recursive-functions.md)

## Proof depends on

- [Rice theorem](rice-theorem.md)

## Sources

- [Mathlib documentation: `ComputablePred.halting_problem`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/Halting.html#ComputablePred.halting_problem)
- [Source of `ComputablePred.halting_problem` in Mathlib/Computability/Halting.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Computability/Halting.lean#L63)
- [Mathlib overview: Logic and computation › Computability](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L607)
