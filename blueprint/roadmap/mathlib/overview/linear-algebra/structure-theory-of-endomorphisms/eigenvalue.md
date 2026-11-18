# Eigenvalue

A scalar `μ` is an eigenvalue for a linear map `f` if there are nonzero vectors `x`
such that `f x = μ • x`. (Def 5.5 of [axler2024](https://leanprover-community.github.io/mathlib4_docs/references.html#ref_axler2024)).

```lean
Module.End.HasEigenvalue.{v, w} {R : Type v} {M : Type w} [CommRing R] [AddCommGroup M]
  [_root_.Module R M] (f : Module.End R M) (a : R) : Prop
```

## Depends on

- [Generalized eigenspaces](../../../undergraduate/linear-algebra/structure-theory-of-endomorphisms/generalized-eigenspaces.md)

## Sources

- [Mathlib documentation: `Module.End.HasEigenvalue`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Eigenspace/Basic.html#Module.End.HasEigenvalue)
- [Source of `Module.End.HasEigenvalue` in Mathlib/LinearAlgebra/Eigenspace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Eigenspace/Basic.lean#L441)
- [Mathlib overview: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L199)
- [Mathlib undergraduate list: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L59)
