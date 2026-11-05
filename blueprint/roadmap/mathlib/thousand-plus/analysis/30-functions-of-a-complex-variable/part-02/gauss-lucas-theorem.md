---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Polynomial.rootSet_derivative_subset_convexHull_rootSet, Polynomial.eq_centerMass_of_eval_derivative_eq_zero
mathlib_file: Mathlib/Analysis/Complex/Polynomial/GaussLucas.lean
---

# Gauss–Lucas theorem

Mathlib records this with 2 declarations.

`Polynomial.rootSet_derivative_subset_convexHull_rootSet`: *Gauss-Lucas Theorem*: if $P$ is a nonconstant polynomial with complex coefficients,
then all zeros of $P'$ belong to the convex hull of the set of zeros of $P$.

See also `eq_centerMass_of_eval_derivative_eq_zero`
for a version that provides explicit coefficients of the convex combination.

```lean
Polynomial.rootSet_derivative_subset_convexHull_rootSet {P : Polynomial ℂ} (h₀ : 0 < P.degree) :
  (Polynomial.derivative P).rootSet ℂ ⊆ (convexHull ℝ) (P.rootSet ℂ)
```

`Polynomial.eq_centerMass_of_eval_derivative_eq_zero`: *Gauss-Lucas Theorem*: if $P$ is a nonconstant polynomial with complex coefficients,
then all zeros of $P'$ belong to the convex hull of the set of zeros of $P$.

This version provides explicit formulas for the coefficients of the convex combination.
See also `rootSet_derivative_subset_convexHull_rootSet` below.

```lean
Polynomial.eq_centerMass_of_eval_derivative_eq_zero {P : Polynomial ℂ} {z : ℂ} (hP : 0 < P.degree)
  (hz : Polynomial.eval z (Polynomial.derivative P) = 0) :
  z = P.roots.toFinset.centerMass (P.derivRootWeight z) id
```

## Depends on

- [Convex hull of a subset of an affine real space](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Inner product space, over $R$ or $C$](../../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Polynomial derivative](../../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Roots of a polynomial](../../../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)

## Proof depends on

- [Fundamental theorem of algebra](../../../../overview/analysis/complex-analysis/fundamental-theorem-of-algebra.md)

## Sources

- [Mathlib documentation: `Polynomial.rootSet_derivative_subset_convexHull_rootSet`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/GaussLucas.html#Polynomial.rootSet_derivative_subset_convexHull_rootSet)
- [Source of `Polynomial.rootSet_derivative_subset_convexHull_rootSet` in Mathlib/Analysis/Complex/Polynomial/GaussLucas.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/Polynomial/GaussLucas.lean#L91)
- [Mathlib documentation: `Polynomial.eq_centerMass_of_eval_derivative_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/GaussLucas.html#Polynomial.eq_centerMass_of_eval_derivative_eq_zero)
- [Source of `Polynomial.eq_centerMass_of_eval_derivative_eq_zero` in Mathlib/Analysis/Complex/Polynomial/GaussLucas.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/Polynomial/GaussLucas.lean#L54)
- [1000+ theorems list: Q1008566](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1197)
- [1000+ theorems project: Q1008566](https://1000-plus.github.io/all.html?length=-1#Q1008566)
- [Wikipedia: Gauss–Lucas theorem](https://en.wikipedia.org/wiki/Gauss%E2%80%93Lucas_theorem)
- [Wikidata: Q1008566](https://www.wikidata.org/wiki/Q1008566)
