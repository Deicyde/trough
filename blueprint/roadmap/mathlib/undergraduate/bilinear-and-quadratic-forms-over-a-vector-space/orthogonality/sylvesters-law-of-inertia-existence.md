---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: QuadraticForm.equivalent_one_zero_neg_one_weighted_sum_squared
mathlib_file: Mathlib/LinearAlgebra/QuadraticForm/Real.lean
---

# Sylvester's law of inertia (existence)

**Sylvester's law of inertia**: A real quadratic form is equivalent to a weighted
sum of squares with the weights being ±1 or 0.

```lean
QuadraticForm.equivalent_one_zero_neg_one_weighted_sum_squared.{u_2} {M : Type u_2} [AddCommGroup M]
  [_root_.Module ℝ M] [FiniteDimensional ℝ M] (Q : QuadraticForm ℝ M) :
  ∃ w,
    (∀ (i : Fin (Module.finrank ℝ M)), w i = -1 ∨ w i = 0 ∨ w i = 1) ∧
      QuadraticMap.Equivalent Q (QuadraticMap.weightedSumSquares ℝ w)
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Quadratic form](../../../overview/linear-algebra/bilinear-and-quadratic-forms/quadratic-form.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Invertible elements](../../ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Isomorphism with $K^n$](../../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Order (Real numbers)](../../single-variable-real-analysis/real-numbers/order.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Range of a linear map](../../linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `QuadraticForm.equivalent_one_zero_neg_one_weighted_sum_squared`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Real.html#QuadraticForm.equivalent_one_zero_neg_one_weighted_sum_squared)
- [Source of `QuadraticForm.equivalent_one_zero_neg_one_weighted_sum_squared` in Mathlib/LinearAlgebra/QuadraticForm/Real.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/QuadraticForm/Real.lean#L85)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Orthogonality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L209)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Orthogonality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L211)
- [1000+ theorems list: Q1752621](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1872)
- [1000+ theorems project: Q1752621](https://1000-plus.github.io/?length=-1#Q1752621)
- [Wikipedia: Sylvester's law of inertia](https://en.wikipedia.org/wiki/Sylvester's_law_of_inertia)
- [Wikidata: Q1752621](https://www.wikidata.org/wiki/Q1752621)
