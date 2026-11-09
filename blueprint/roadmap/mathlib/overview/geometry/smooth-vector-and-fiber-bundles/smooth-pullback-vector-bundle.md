# (smooth) pullback vector bundle

For a `C^n` vector bundle `E` over a manifold `B` and a `C^n` map `f : B' → B`, the pullback
vector bundle `f *ᵖ E` is a `C^n` vector bundle.

```lean
ContMDiffVectorBundle.pullback.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8, u_9} {𝕜 : Type u_1}
  {B : Type u_2} {B' : Type u_3} (F : Type u_4) (E : B → Type u_5) {n : WithTop ℕ∞}
  [NontriviallyNormedField 𝕜] [(x : B) → AddCommMonoid (E x)] [(x : B) → _root_.Module 𝕜 (E x)]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [TopologicalSpace (Bundle.TotalSpace F E)]
  [(x : B) → TopologicalSpace (E x)] {EB : Type u_6} [NormedAddCommGroup EB] [NormedSpace 𝕜 EB]
  {HB : Type u_7} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB} [TopologicalSpace B]
  [ChartedSpace HB B] {EB' : Type u_8} [NormedAddCommGroup EB'] [NormedSpace 𝕜 EB'] {HB' : Type u_9}
  [TopologicalSpace HB'] (IB' : ModelWithCorners 𝕜 EB' HB') [TopologicalSpace B']
  [ChartedSpace HB' B'] [FiberBundle F E] [VectorBundle 𝕜 F E] [ContMDiffVectorBundle n F E IB]
  (f : ContMDiffMap IB' IB B' B n) : ContMDiffVectorBundle n F (⇑f *ᵖ E) IB'
```

## Depends on

- [(smooth) vector bundle](smooth-vector-bundle.md)
- [Smooth map between manifolds](../differentiable-manifolds/part-01/smooth-map-between-manifolds.md)

## Sources

- [Mathlib documentation: `ContMDiffVectorBundle.pullback`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Pullback.html#ContMDiffVectorBundle.pullback)
- [Source of `ContMDiffVectorBundle.pullback` in Mathlib/Geometry/Manifold/VectorBundle/Pullback.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Manifold/VectorBundle/Pullback.lean#L37)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L471)
