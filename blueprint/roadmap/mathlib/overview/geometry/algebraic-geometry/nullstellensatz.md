---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MvPolynomial.vanishingIdeal_zeroLocus_eq_radical
mathlib_file: Mathlib/RingTheory/Nullstellensatz.lean
---

# Nullstellensatz

Main statement of the Nullstellensatz

```lean
MvPolynomial.vanishingIdeal_zeroLocus_eq_radical.{u_1, u_2, u_3} {k : Type u_1} {K : Type u_2}
  [Field k] [Field K] [Algebra k K] {σ : Type u_3} [IsAlgClosed K] [Finite σ]
  (I : Ideal (MvPolynomial σ k)) :
  MvPolynomial.vanishingIdeal k (MvPolynomial.zeroLocus K I) = I.radical
```

## Depends on

- [Algebraically closed field](../../general-algebra/field-theory/algebraically-closed-field.md)
- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Ideal of a commutative ring](../../general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Polynomial in several indeterminates](../../general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)

## Proof depends on

- [Algebraic extension](../../general-algebra/field-theory/algebraic-extension.md)
- [Field of fractions of an integral domain](../../general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Local ring](../../general-algebra/rings/local-ring.md)
- [Localization](../../general-algebra/rings/localization.md)
- [Prime ideal](../../general-algebra/ideals-and-quotients/prime-ideal.md)
- [Quotient space (Fundamentals)](../../linear-algebra/fundamentals/quotient-space.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `MvPolynomial.vanishingIdeal_zeroLocus_eq_radical`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Nullstellensatz.html#MvPolynomial.vanishingIdeal_zeroLocus_eq_radical)
- [Source of `MvPolynomial.vanishingIdeal_zeroLocus_eq_radical` in Mathlib/RingTheory/Nullstellensatz.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Nullstellensatz.lean#L169)
- [Mathlib overview: Geometry › Algebraic geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L485)
- [1000+ theorems list: Q1068976](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1320)
- [1000+ theorems project: Q1068976](https://1000-plus.github.io/all.html?length=-1#Q1068976)
- [Wikipedia: Hilbert's Nullstellensatz\]\] (theorem of zeroes)](https://en.wikipedia.org/wiki/Hilbert's_Nullstellensatz%5D%5D_%28theorem_of_zeroes%29)
- [Wikidata: Q1068976](https://www.wikidata.org/wiki/Q1068976)
