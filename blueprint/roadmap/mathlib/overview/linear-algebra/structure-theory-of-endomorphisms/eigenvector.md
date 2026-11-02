---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Module.End.HasEigenvector
mathlib_file: Mathlib/LinearAlgebra/Eigenspace/Basic.lean
---

# Eigenvector

A nonzero element of an eigenspace is an eigenvector. (Def 5.8 of [axler2024])

```lean
Module.End.HasEigenvector.{v, w} {R : Type v} {M : Type w} [CommRing R] [AddCommGroup M]
  [_root_.Module R M] (f : Module.End R M) (μ : R) (x : M) : Prop
```

## Depends on

- [Generalized eigenspaces](../../../undergraduate/linear-algebra/structure-theory-of-endomorphisms/generalized-eigenspaces.md)

## Sources

- [Mathlib documentation: `Module.End.HasEigenvector`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Eigenspace/Basic.html#Module.End.HasEigenvector)
- [Source of `Module.End.HasEigenvector` in Mathlib/LinearAlgebra/Eigenspace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Eigenspace/Basic.lean#L434)
- [Mathlib overview: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L200)
- [Mathlib undergraduate list: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L60)
