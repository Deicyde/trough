---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: CharZero
mathlib_file: Mathlib/Algebra/CharZero/Defs.lean
---

# Characteristic zero

Typeclass for monoids with characteristic zero.
  (This is usually stated on fields but it makes sense for any additive monoid with 1.)

*Warning*: for a semiring `R`, `CharZero R` and `CharP R 0` need not coincide.
* `CharZero R` requires an injection `ℕ ↪ R`;
* `CharP R 0` asks that only `0 : ℕ` maps to `0 : R` under the map `ℕ → R`.
  For instance, endowing `{0, 1}` with addition given by `max` (i.e. `1` is absorbing), shows that
  `CharZero {0, 1}` does not hold and yet `CharP {0, 1} 0` does.
  This example is formalized in `Counterexamples/CharPZeroNeCharZero.lean`.

```lean
CharZero.{u_1} (R : Type u_1) [AddMonoidWithOne R] : Prop
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `CharZero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharZero/Defs.html#CharZero)
- [Source of `CharZero` in Mathlib/Algebra/CharZero/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/CharZero/Defs.lean#L34)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L123)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L173)
