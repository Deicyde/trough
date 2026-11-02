---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: Pi.ring
mathlib_file: Mathlib/Algebra/Ring/Pi.lean
---

# Product of rings

Mathlib states this as `Pi.ring`.

```lean
Pi.ring.{u, v} {I : Type u} {f : I → Type v} [(i : I) → Ring (f i)] : Ring ((i : I) → f i)
```

## Depends on

- [Ring](../../../overview/general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `Pi.ring`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Pi.html#Pi.ring)
- [Source of `Pi.ring` in Mathlib/Algebra/Ring/Pi.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Ring/Pi.lean#L89)
- [Mathlib undergraduate list: Ring Theory › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L130)
