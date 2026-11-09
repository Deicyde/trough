# (smooth) direct sum of vector bundles

The direct sum of two `C^n` vector bundles over the same base is a `C^n` vector bundle.

```lean
Bundle.Prod.contMDiffVectorBundle.{u_1, u_2, u_6, u_7, u_10, u_11, u_12, u_13} {n : WithTop ℕ∞}
  {𝕜 : Type u_1} {B : Type u_2} [NontriviallyNormedField 𝕜] {EB : Type u_6} [NormedAddCommGroup EB]
  [NormedSpace 𝕜 EB] {HB : Type u_7} [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB}
  [TopologicalSpace B] [ChartedSpace HB B] (F₁ : Type u_10) [NormedAddCommGroup F₁]
  [NormedSpace 𝕜 F₁] (E₁ : B → Type u_11) [TopologicalSpace (Bundle.TotalSpace F₁ E₁)]
  [(x : B) → AddCommMonoid (E₁ x)] [(x : B) → _root_.Module 𝕜 (E₁ x)] (F₂ : Type u_12)
  [NormedAddCommGroup F₂] [NormedSpace 𝕜 F₂] (E₂ : B → Type u_13)
  [TopologicalSpace (Bundle.TotalSpace F₂ E₂)] [(x : B) → AddCommMonoid (E₂ x)]
  [(x : B) → _root_.Module 𝕜 (E₂ x)] [(x : B) → TopologicalSpace (E₁ x)]
  [(x : B) → TopologicalSpace (E₂ x)] [FiberBundle F₁ E₁] [FiberBundle F₂ E₂] [VectorBundle 𝕜 F₁ E₁]
  [VectorBundle 𝕜 F₂ E₂] [ContMDiffVectorBundle n F₁ E₁ IB] [ContMDiffVectorBundle n F₂ E₂ IB] :
  ContMDiffVectorBundle n (F₁ × F₂) (fun x => E₁ x × E₂ x) IB
```

## Depends on

- [(smooth) vector bundle](smooth-vector-bundle.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)

## Sources

- [Mathlib documentation: `Bundle.Prod.contMDiffVectorBundle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Basic.html#Bundle.Prod.contMDiffVectorBundle)
- [Source of `Bundle.Prod.contMDiffVectorBundle` in Mathlib/Geometry/Manifold/VectorBundle/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Manifold/VectorBundle/Basic.lean#L652)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L470)
