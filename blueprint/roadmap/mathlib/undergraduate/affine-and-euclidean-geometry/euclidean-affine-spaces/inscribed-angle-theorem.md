---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Orientation.two_zsmul_oangle_sub_eq_two_zsmul_oangle_sub_of_norm_eq
mathlib_file: Mathlib/Geometry/Euclidean/Angle/Sphere.lean
---

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
- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Determinant of vectors](../../linear-algebra/multilinearity/determinant-of-vectors.md)
- [Existence of orthonormal basis](../../../overview/linear-algebra/finite-dimensional-inner-product-spaces-see-also/existence-of-orthonormal-basis.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Isomorphism with $K^n$](../../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Orientation of a $\R$-vector space](../../linear-algebra/multilinearity/orientation-of-a-r-vector-space.md)
- [Range of a linear map](../../linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Orientation.two_zsmul_oangle_sub_eq_two_zsmul_oangle_sub_of_norm_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Angle/Sphere.html#Orientation.two_zsmul_oangle_sub_eq_two_zsmul_oangle_sub_of_norm_eq)
- [Source of `Orientation.two_zsmul_oangle_sub_eq_two_zsmul_oangle_sub_of_norm_eq` in Mathlib/Geometry/Euclidean/Angle/Sphere.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L58)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Euclidean affine spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L266)
