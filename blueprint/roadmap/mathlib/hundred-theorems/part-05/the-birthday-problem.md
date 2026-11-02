---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.birthday, Theorems100.birthday_measure
mathlib_file: Archive/Wiedijk100Theorems/BirthdayProblem.lean
---

# The Birthday Problem

Mathlib records this with 2 declarations.

`Theorems100.birthday`: **Birthday Problem**: set cardinality interpretation.

```lean
Theorems100.birthday :
  2 * Fintype.card (Fin 23 ↪ Fin 365) < Fintype.card (Fin 23 → Fin 365) ∧
    2 * Fintype.card (Fin 22 ↪ Fin 365) > Fintype.card (Fin 22 → Fin 365)
```

`Theorems100.birthday_measure`: **Birthday Problem**: first probabilistic interpretation.

```lean
Theorems100.birthday_measure : MeasureTheory.volume {f | Function.Injective f} < 1 / 2
```

## Depends on

- [Conditional probability](../../overview/probability-theory/definitions-in-probability-theory/conditional-probability.md)
- [Counting measure](../../undergraduate/measures-and-integral-calculus/measure-theory/counting-measure.md)
- [Lebesgue measure (Measure theory)](../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Product of sigma-algebras](../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)

## Sources

- [Mathlib documentation: `Theorems100.birthday`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/BirthdayProblem.html#Theorems100.birthday)
- [Source of `Theorems100.birthday` in Archive/Wiedijk100Theorems/BirthdayProblem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/BirthdayProblem.lean#L29)
- [Mathlib documentation: `Theorems100.birthday_measure`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/BirthdayProblem.html#Theorems100.birthday_measure)
- [Source of `Theorems100.birthday_measure` in Archive/Wiedijk100Theorems/BirthdayProblem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/BirthdayProblem.lean#L48)
- [Freek Wiedijk's 100 theorems, no. 93](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L478)
