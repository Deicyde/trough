# Adjoint endomorphism

Given the nondegenerate bilinear form `B` and the linear map `φ`,
`leftAdjointOfNondegenerate` provides the left adjoint of `φ` with respect to `B`.
The lemma proving this property is `BilinForm.isAdjointPairLeftAdjointOfNondegenerate`.

```lean
LinearMap.BilinForm.leftAdjointOfNondegenerate.{u_5, u_6} {V : Type u_5} {K : Type u_6} [Field K]
  [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V] (B : LinearMap.BilinForm K V)
  (b : B.Nondegenerate) (φ : V →ₗ[K] V) : V →ₗ[K] V
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Dual vector space](../../../overview/linear-algebra/duality/dual-vector-space.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Nondegenerate forms](../bilinear-forms/nondegenerate-forms.md)
- [Range of a linear map](../../linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `LinearMap.BilinForm.leftAdjointOfNondegenerate`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/BilinearForm/Properties.html#LinearMap.BilinForm.leftAdjointOfNondegenerate)
- [Source of `LinearMap.BilinForm.leftAdjointOfNondegenerate` in Mathlib/LinearAlgebra/BilinearForm/Properties.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/BilinearForm/Properties.lean#L455)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Orthogonality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L208)
