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

- [$K\[X\]$ is Euclidean](../../general-algebra/polynomials-and-power-series/k-x-is-euclidean.md)
- [Aleph numbers](../../logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Algebraic extension](../../general-algebra/field-theory/algebraic-extension.md)
- [Cayley-Hamilton theorem](../../linear-algebra/endomorphism-polynomials/cayley-hamilton-theorem.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Field of fractions of an integral domain](../../general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Fundamental sequences](../../logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Going-up and going-down theorems](../../../thousand-plus/algebra/13-commutative-algebra/going-up-and-going-down-theorems.md)
- [Greatest common divisor](../../general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Least common multiple](../../general-algebra/divisibility-in-integral-domains/least-common-multiple.md)
- [Minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Noetherian ring](../../general-algebra/rings/noetherian-ring.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Roots of a polynomial](../../general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [Rupture field](../../general-algebra/field-theory/rupture-field.md)
- [Subfield](../../general-algebra/field-theory/subfield.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)
- [Well-ordering theorem](../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `MvPolynomial.vanishingIdeal_zeroLocus_eq_radical`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Nullstellensatz.html#MvPolynomial.vanishingIdeal_zeroLocus_eq_radical)
- [Source of `MvPolynomial.vanishingIdeal_zeroLocus_eq_radical` in Mathlib/RingTheory/Nullstellensatz.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Nullstellensatz.lean#L169)
- [Mathlib overview: Geometry › Algebraic geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L485)
- [1000+ theorems list: Q1068976](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1320)
- [1000+ theorems project: Q1068976](https://1000-plus.github.io/?length=-1#Q1068976)
- [Wikipedia: Hilbert's Nullstellensatz\]\] (theorem of zeroes)](https://en.wikipedia.org/wiki/Hilbert's_Nullstellensatz%5D%5D_%28theorem_of_zeroes%29)
- [Wikidata: Q1068976](https://www.wikidata.org/wiki/Q1068976)
