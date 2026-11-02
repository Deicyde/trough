---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed
mathlib_file: Mathlib/LinearAlgebra/QuadraticForm/AlgClosed.lean
---

# Complex classification

A nondegenerate quadratic form on an algebraically closed field of characteristic not equal to 2
is equivalent to the sum of squares, i.e. `weightedSumSquares` with weight `fun (i : ι) => 1`.

```lean
QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed.{u_2, u_3} {K : Type u_2} [Field K]
  [IsAlgClosed K] [Invertible 2] {M : Type u_3} [AddCommGroup M] [_root_.Module K M]
  [FiniteDimensional K M] (Q : QuadraticForm K M)
  (hQ : LinearMap.SeparatingLeft (QuadraticMap.associated Q)) :
  QuadraticMap.Equivalent Q (QuadraticMap.weightedSumSquares K 1)
```

## Depends on

- [Algebraically closed field](../../../overview/general-algebra/field-theory/algebraically-closed-field.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Invertible elements](../../ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Polar form of a quadratic](../../../overview/linear-algebra/bilinear-and-quadratic-forms/polar-form-of-a-quadratic.md)
- [Quadratic form](../../../overview/linear-algebra/bilinear-and-quadratic-forms/quadratic-form.md)

## Sources

- [Mathlib documentation: `QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/AlgClosed.html#QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed)
- [Source of `QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed` in Mathlib/LinearAlgebra/QuadraticForm/AlgClosed.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/QuadraticForm/AlgClosed.lean#L50)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Orthogonality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L212)
