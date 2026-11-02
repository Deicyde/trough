---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: CharP
mathlib_file: Mathlib/Algebra/CharP/Defs.lean
---

# Characteristic p

The generator of the kernel of the unique homomorphism ℕ → R for a semiring R.

*Warning*: for a semiring `R`, `CharP R 0` and `CharZero R` need not coincide.
* `CharP R 0` asks that only `0 : ℕ` maps to `0 : R` under the map `ℕ → R`;
* `CharZero R` requires an injection `ℕ ↪ R`.

For instance, endowing `{0, 1}` with addition given by `max` (i.e. `1` is absorbing), shows that
`CharZero {0, 1}` does not hold and yet `CharP {0, 1} 0` does.
This example is formalized in `Counterexamples/CharPZeroNeCharZero.lean`.

```lean
CharP.{u_2} (R : Type u_2) [AddMonoidWithOne R] (p : outParam ℕ) : Prop
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `CharP`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP)
- [Source of `CharP` in Mathlib/Algebra/CharP/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/CharP/Defs.lean#L36)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L124)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L174)
