# In terms of Turing machines

A Turing machine + a proof it outputs `f`.

```lean
Turing.TM2Computable {α β αΓ βΓ : Type} (ea : α → List αΓ) (eb : β → List βΓ) (f : α → β) : Type 1
```

## Depends on

- [Finite set](../../../data-structures/sets/finite-set.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Turing.TM2Computable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/TuringMachine/Computable.html#Turing.TM2Computable)
- [Source of `Turing.TM2Computable` in Mathlib/Computability/TuringMachine/Computable.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Computability/TuringMachine/Computable.lean#L150)
- [Mathlib overview: Logic and computation › Computability › computable function](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L603)
