---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Polynomial.irreducible_of_eisenstein_criterion
mathlib_file: Mathlib/RingTheory/Polynomial/Eisenstein/Criterion.lean
---

# Eisenstein's criterion

If `f` is a nonconstant polynomial with coefficients in `R`, and `P` is a prime ideal in `R`,
then if every coefficient in `R` except the leading coefficient is in `P`, and
the trailing coefficient is not in `P^2` and no nonunits in `R` divide `f`, then `f` is
irreducible.

```lean
Polynomial.irreducible_of_eisenstein_criterion.{u_1} {R : Type u_1} [CommRing R] [IsDomain R]
  {f : Polynomial R} {P : Ideal R} (hP : P.IsPrime) (hfl : f.leadingCoeff ∉ P)
  (hfP : ∀ (n : ℕ), ↑n < f.degree → f.coeff n ∈ P) (hfd0 : 0 < f.degree) (h0 : f.coeff 0 ∉ P ^ 2)
  (hu : f.IsPrimitive) : Irreducible f
```

## Depends on

- [Associative algebra over a commutative ring](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)
- [Prime ideal](../ideals-and-quotients/prime-ideal.md)
- [Ring](../rings/ring.md)

## Proof depends on

- [$K\[X\]$ is Euclidean](k-x-is-euclidean.md)
- [Localization](../rings/localization.md)
- [Quotient ring](../ideals-and-quotients/quotient-ring.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Polynomial.irreducible_of_eisenstein_criterion`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Eisenstein/Criterion.html#Polynomial.irreducible_of_eisenstein_criterion)
- [Source of `Polynomial.irreducible_of_eisenstein_criterion` in Mathlib/RingTheory/Polynomial/Eisenstein/Criterion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Polynomial/Eisenstein/Criterion.lean#L171)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L105)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L161)
