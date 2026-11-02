---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Turing.TM0.Machine
mathlib_file: Mathlib/Computability/TuringMachine/PostTuringMachine.lean
---

# Turing machine

A Post-Turing machine with symbol type `Γ` and label type `Λ`
is a function which, given the current state `q : Λ` and
the tape head `a : Γ`, either halts (returns `none`) or returns
a new state `q' : Λ` and a `Stmt` describing what to do,
either a move left or right, or a write command.

Both `Λ` and `Γ` are required to be inhabited; the default value
for `Γ` is the "blank" tape value, and the default value of `Λ` is
the initial state.

```lean
Turing.TM0.Machine.{u_1, u_2} (Γ : Type u_1) (Λ : Type u_2) [Inhabited Λ] :
  Type (max (max u_1 u_2) u_1 u_2)
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `Turing.TM0.Machine`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/TuringMachine/PostTuringMachine.html#Turing.TM0.Machine)
- [Source of `Turing.TM0.Machine` in Mathlib/Computability/TuringMachine/PostTuringMachine.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/TuringMachine/PostTuringMachine.lean#L123)
- [Mathlib overview: Logic and computation › Computability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L606)
