---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Field
mathlib_file: Mathlib/Algebra/Field/Defs.lean
---

# Field

A `Field` is a `CommRing` with multiplicative inverses for nonzero elements.

An instance of `Field K` includes maps `ratCast : ℚ → K` and `qsmul : ℚ → K → K`.
Those two fields are needed to implement the `DivisionRing K → Algebra ℚ K` instance since we need
to control the specific definitions for some special cases of `K` (in particular `K = ℚ` itself).
See also note [forgetful inheritance].

If the field has positive characteristic `p`, our division by zero convention forces
`ratCast (1 / p) = 1 / 0 = 0`.

```lean
Field.{u} (K : Type u) : Type u
```

## Depends on

- [Rational number](../numbers/rational-number.md)
- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `Field`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html#Field)
- [Source of `Field` in Mathlib/Algebra/Field/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Field/Defs.lean#L170)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L120)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L171)
