# Smooth or analytic manifold (with boundary and corners)

Typeclass defining manifolds with respect to a model with corners, over a
field `𝕜`. This definition includes the model with corners `I` (which might allow boundary, corners,
or not, so this class covers both manifolds with boundary and manifolds without boundary), and
a smoothness parameter `n : ℕ∞ω` (where `n = 0` means topological manifold, `n = ∞` means
smooth manifold and `n = ω` means analytic manifold).

```lean
IsManifold.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  (I : ModelWithCorners 𝕜 E H) (n : WithTop ℕ∞) (M : Type u_4) [TopologicalSpace M]
  [ChartedSpace H M] : Prop
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Infinite sum](../../../topology/topological-algebra/infinite-sum.md)
- [Norm of a continuous linear map](../../../analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Radius of convergence](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)

## Sources

- [Mathlib documentation: `IsManifold`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IsManifold/Basic.html#IsManifold)
- [Source of `IsManifold` in Mathlib/Geometry/Manifold/IsManifold/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Manifold/IsManifold/Basic.lean#L772)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L440)
