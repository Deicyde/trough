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
- [Source of `Turing.TM2Computable` in Mathlib/Computability/TuringMachine/Computable.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Computability/TuringMachine/Computable.lean#L150)
- [Mathlib overview: Logic and computation › Computability › computable function](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L603)
