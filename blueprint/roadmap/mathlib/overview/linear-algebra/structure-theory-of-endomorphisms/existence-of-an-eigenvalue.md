---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Module.End.exists_eigenvalue
mathlib_file: Mathlib/LinearAlgebra/Eigenspace/Triangularizable.lean
---

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

- [Aleph numbers](../../logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Cayley-Hamilton theorem](../endomorphism-polynomials/cayley-hamilton-theorem.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Fundamental sequences](../../logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Ideal of a commutative ring](../../general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Noetherian ring](../../general-algebra/rings/noetherian-ring.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Principal ideal domain](../../general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Roots of a polynomial](../../general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)
- [Well-ordering theorem](../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `Module.End.exists_eigenvalue`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Eigenspace/Triangularizable.html#Module.End.exists_eigenvalue)
- [Source of `Module.End.exists_eigenvalue` in Mathlib/LinearAlgebra/Eigenspace/Triangularizable.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Eigenspace/Triangularizable.lean#L60)
- [Mathlib overview: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L201)
