# Inscribed angle theorem

Oriented vector angle version of "angles in same segment are equal" and "opposite angles of
a cyclic quadrilateral add to π", for oriented angles mod π (for which those are the same
result), represented here as equality of twice the angles.

```lean
Orientation.two_zsmul_oangle_sub_eq_two_zsmul_oangle_sub_of_norm_eq.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [Fact (Module.finrank ℝ V = 2)]
  (o : Orientation ℝ V (Fin 2)) {x₁ x₂ y z : V} (hx₁yne : x₁ ≠ y) (hx₁zne : x₁ ≠ z)
  (hx₂yne : x₂ ≠ y) (hx₂zne : x₂ ≠ z) {r : ℝ} (hx₁ : ‖x₁‖ = r) (hx₂ : ‖x₂‖ = r) (hy : ‖y‖ = r)
  (hz : ‖z‖ = r) : 2 • o.oangle (y - x₁) (z - x₁) = 2 • o.oangle (y - x₂) (z - x₂)
```

## Depends on

- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Determinant of vectors](../../linear-algebra/multilinearity/determinant-of-vectors.md)
- [Existence of orthonormal basis](../../../overview/linear-algebra/finite-dimensional-inner-product-spaces-see-also/existence-of-orthonormal-basis.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inverse trigonometric functions](../../../overview/analysis/special-functions/inverse-trigonometric-functions.md)
- [Isomorphism with $K^n$](../../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Orientation of a $\R$-vector space](../../linear-algebra/multilinearity/orientation-of-a-r-vector-space.md)
- [Range of a linear map](../../linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Orientation.two_zsmul_oangle_sub_eq_two_zsmul_oangle_sub_of_norm_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Angle/Sphere.html#Orientation.two_zsmul_oangle_sub_eq_two_zsmul_oangle_sub_of_norm_eq)
- [Source of `Orientation.two_zsmul_oangle_sub_eq_two_zsmul_oangle_sub_of_norm_eq` in Mathlib/Geometry/Euclidean/Angle/Sphere.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L58)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Euclidean affine spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L266)
