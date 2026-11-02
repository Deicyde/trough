---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Subspace
mathlib_file: Mathlib/Algebra/Module/Submodule/Basic.lean
---

# Vector subspace

Subspace of a vector space. Defined to equal `Submodule`.

```lean
Subspace.{u, v} (R : Type u) (M : Type v) [DivisionRing R] [AddCommGroup M] [_root_.Module R M] :
  Type v
```

## Depends on

- [Module](../../../overview/linear-algebra/fundamentals/module.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Subspace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Submodule/Basic.html#Subspace)
- [Source of `Subspace` in Mathlib/Algebra/Module/Submodule/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Module/Submodule/Basic.lean#L177)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L9)
