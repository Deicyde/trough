---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: Submodule.hasQuotient
mathlib_file: Mathlib/LinearAlgebra/Quotient/Defs.lean
---

# Quotient space (Fundamentals)

The quotient of a module `M` by a submodule `p ⊆ M`.

```lean
Submodule.hasQuotient.{u_1, u_2} {R : Type u_1} {M : Type u_2} [Ring R] [AddCommGroup M]
  [_root_.Module R M] : HasQuotient M (Submodule R M)
```

## Depends on

- [Module](module.md)
- [Ring](../../general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `Submodule.hasQuotient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Quotient/Defs.html#Submodule.hasQuotient)
- [Source of `Submodule.hasQuotient` in Mathlib/LinearAlgebra/Quotient/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Quotient/Defs.lean#L54)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L173)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L10)
