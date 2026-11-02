---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Subfield
mathlib_file: Mathlib/Algebra/Field/Subfield/Defs.lean
---

# Subfield

`Subfield R` is the type of subfields of `R`. A subfield of `R` is a subset `s` that is a
multiplicative submonoid and an additive subgroup. Note in particular that it shares the
same 0 and 1 as R.

```lean
Subfield.{u} (K : Type u) [DivisionRing K] : Type u
```

## Depends on

- [Rational number](../numbers/rational-number.md)
- [Ring](../rings/ring.md)
- [Subring](../rings/subring.md)

## Sources

- [Mathlib documentation: `Subfield`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Subfield/Defs.html#Subfield)
- [Source of `Subfield` in Mathlib/Algebra/Field/Subfield/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Field/Subfield/Defs.lean#L128)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L121)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L175)
