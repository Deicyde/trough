# Eigenvector

A nonzero element of an eigenspace is an eigenvector. (Def 5.8 of [axler2024](https://leanprover-community.github.io/mathlib4_docs/references.html#ref_axler2024))

```lean
Module.End.HasEigenvector.{v, w} {R : Type v} {M : Type w} [CommRing R] [AddCommGroup M]
  [_root_.Module R M] (f : Module.End R M) (μ : R) (x : M) : Prop
```

## Depends on

- [Generalized eigenspaces](../../../undergraduate/linear-algebra/structure-theory-of-endomorphisms/generalized-eigenspaces.md)

## Sources

- [Mathlib documentation: `Module.End.HasEigenvector`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Eigenspace/Basic.html#Module.End.HasEigenvector)
- [Source of `Module.End.HasEigenvector` in Mathlib/LinearAlgebra/Eigenspace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Eigenspace/Basic.lean#L434)
- [Mathlib overview: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L200)
- [Mathlib undergraduate list: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L60)
