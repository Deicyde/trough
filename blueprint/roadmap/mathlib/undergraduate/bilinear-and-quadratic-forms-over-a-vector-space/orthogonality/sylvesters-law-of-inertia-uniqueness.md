---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: QuadraticForm.sigPos_of_equiv_weightedSumSquares
mathlib_file: Mathlib/LinearAlgebra/QuadraticForm/Signature.lean
---

# Sylvester's law of inertia (uniqueness)

Uniqueness part of **Sylvester's law of inertia** (positive part):
for any weighted sum of squares equivalent to `Q`,
the number of strictly positive weights is equal to `sigPos Q`.

```lean
QuadraticForm.sigPos_of_equiv_weightedSumSquares.{u_2, u_4, u_5} {M : Type u_2} [AddCommGroup M]
  {𝕜 : Type u_4} [Field 𝕜] [LinearOrder 𝕜] [_root_.Module 𝕜 M] {Q : QuadraticForm 𝕜 M}
  {ι : Type u_5} [Fintype ι] {w : ι → 𝕜} [IsStrictOrderedRing 𝕜]
  (hQ : QuadraticMap.Equivalent Q (QuadraticMap.weightedSumSquares 𝕜 w)) :
  sigPos Q = {i | 0 < w i}.ncard
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Quadratic form](../../../overview/linear-algebra/bilinear-and-quadratic-forms/quadratic-form.md)

## Proof depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Euclidean domain](../../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Vector subspace](../../linear-algebra/fundamentals/vector-subspace.md)

## Sources

- [Mathlib documentation: `QuadraticForm.sigPos_of_equiv_weightedSumSquares`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Signature.html#QuadraticForm.sigPos_of_equiv_weightedSumSquares)
- [Source of `QuadraticForm.sigPos_of_equiv_weightedSumSquares` in Mathlib/LinearAlgebra/QuadraticForm/Signature.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/QuadraticForm/Signature.lean#L240)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Orthogonality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L210)
