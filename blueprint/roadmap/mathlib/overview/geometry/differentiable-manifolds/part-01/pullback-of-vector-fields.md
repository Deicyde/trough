# Pullback of vector fields

The pullback of a vector field under a map between manifolds. If the derivative of the map is
not invertible, then pullback is given the junk value zero.

```lean
VectorField.mpullback.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {H : Type u_2} [TopologicalSpace H] {E : Type u_3} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  (I : ModelWithCorners 𝕜 E H) {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M]
  {H' : Type u_5} [TopologicalSpace H'] {E' : Type u_6} [NormedAddCommGroup E'] [NormedSpace 𝕜 E']
  (I' : ModelWithCorners 𝕜 E' H') {M' : Type u_7} [TopologicalSpace M'] [ChartedSpace H' M']
  (f : M → M') (V : (x : M') → TangentSpace I' x) (x : M) : TangentSpace I x
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Continuous linear map](../../../topology/topological-algebra/continuous-linear-map.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Normed vector space over a normed field](../../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `VectorField.mpullback`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorField/Pullback.html#VectorField.mpullback)
- [Source of `VectorField.mpullback` in Mathlib/Geometry/Manifold/VectorField/Pullback.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Geometry/Manifold/VectorField/Pullback.lean#L104)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L450)
