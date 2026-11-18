# Polynomial-time computation

A Turing machine + a polynomial time function +
a proof it outputs `f` in at most `time(input.length)` steps.

```lean
Turing.TM2ComputableInPolyTime {α β αΓ βΓ : Type} (ea : α → List αΓ) (eb : β → List βΓ)
  (f : α → β) : Type 1
```

## Depends on

- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)

## Sources

- [Mathlib documentation: `Turing.TM2ComputableInPolyTime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/TuringMachine/Computable.html#Turing.TM2ComputableInPolyTime)
- [Source of `Turing.TM2ComputableInPolyTime` in Mathlib/Computability/TuringMachine/Computable.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Computability/TuringMachine/Computable.lean#L172)
- [Mathlib overview: Logic and computation › Complexity](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L611)
