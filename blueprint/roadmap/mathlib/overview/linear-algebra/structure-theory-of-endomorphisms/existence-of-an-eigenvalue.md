# Existence of an eigenvalue

In finite dimensions, over an algebraically closed field, every linear endomorphism has an
eigenvalue.

```lean
Module.End.exists_eigenvalue.{u_1, u_2} {K : Type u_1} {V : Type u_2} [Field K] [AddCommGroup V]
  [_root_.Module K V] [IsAlgClosed K] [FiniteDimensional K V] [Nontrivial V] (f : Module.End K V) :
  ∃ c, f.HasEigenvalue c
```

## Depends on

- [Algebraically closed field](../../general-algebra/field-theory/algebraically-closed-field.md)
- [Eigenvalue](eigenvalue.md)
- [Finite-dimensionality](../finite-dimensional-vector-spaces/finite-dimensionality.md)

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Basis](../fundamentals/basis.md)

## Sources

- [Mathlib documentation: `Module.End.exists_eigenvalue`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Eigenspace/Triangularizable.html#Module.End.exists_eigenvalue)
- [Source of `Module.End.exists_eigenvalue` in Mathlib/LinearAlgebra/Eigenspace/Triangularizable.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Eigenspace/Triangularizable.lean#L60)
- [Mathlib overview: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L201)
