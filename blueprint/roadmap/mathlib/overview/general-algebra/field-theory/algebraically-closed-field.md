---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: IsAlgClosed
mathlib_file: Mathlib/FieldTheory/IsAlgClosed/Basic.lean
---

# Algebraically closed field

An algebraically closed field is one where every polynomial splits. Equivalently, all
non-constant polynomials have a root. See `IsAlgClosed.exists_root` and
`IsAlgClosed.of_exists_root`.

```lean
IsAlgClosed.{u} (k : Type u) [Field k] : Prop
```

## Depends on

- [Field](field.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `IsAlgClosed`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed)
- [Source of `IsAlgClosed` in Mathlib/FieldTheory/IsAlgClosed/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/IsAlgClosed/Basic.lean#L59)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L126)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L185)
