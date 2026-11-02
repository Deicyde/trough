---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ComputablePred.halting_problem
mathlib_file: Mathlib/Computability/Halting.lean
---

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
- [Source of `ComputablePred.halting_problem` in Mathlib/Computability/Halting.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/Halting.lean#L63)
- [Mathlib overview: Logic and computation › Computability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L607)
