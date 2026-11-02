---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Module.End.invtSubmodule
mathlib_file: Mathlib/Algebra/Module/Submodule/Invariant.lean
---

# Invariant subspaces of an endomorphism

Given an endomorphism, `f` of some module, this is the sublattice of all `f`-invariant
submodules.

```lean
Module.End.invtSubmodule.{u_1, u_2} {R : Type u_1} {M : Type u_2} [Semiring R] [AddCommMonoid M]
  [_root_.Module R M] (f : Module.End R M) : Sublattice (Submodule R M)
```

## Depends on

- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Sum of subspaces](../fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `Module.End.invtSubmodule`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Submodule/Invariant.html#Module.End.invtSubmodule)
- [Source of `Module.End.invtSubmodule` in Mathlib/Algebra/Module/Submodule/Invariant.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Module/Submodule/Invariant.lean#L32)
- [Mathlib undergraduate list: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L63)
