# (smooth) trivial vector bundle

A trivial vector bundle over a manifold is a `C^n` vector bundle.

```lean
Bundle.Trivial.contMDiffVectorBundle.{u_1, u_2, u_3, u_6, u_7} {n : WithTop ℕ∞} {𝕜 : Type u_1}
  {B : Type u_2} (F : Type u_3) [NontriviallyNormedField 𝕜] {EB : Type u_6} [NormedAddCommGroup EB]
  [NormedSpace 𝕜 EB] {HB : Type u_7} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB}
  [TopologicalSpace B] [ChartedSpace HB B] [NormedAddCommGroup F] [NormedSpace 𝕜 F] :
  ContMDiffVectorBundle n F (Bundle.Trivial B F) IB
```

## Depends on

- [(smooth) vector bundle](smooth-vector-bundle.md)

## Proof depends on

- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Smooth map between manifolds](../differentiable-manifolds/part-01/smooth-map-between-manifolds.md)

## Sources

- [Mathlib documentation: `Bundle.Trivial.contMDiffVectorBundle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Basic.html#Bundle.Trivial.contMDiffVectorBundle)
- [Source of `Bundle.Trivial.contMDiffVectorBundle` in Mathlib/Geometry/Manifold/VectorBundle/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorBundle/Basic.lean#L609)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L469)
