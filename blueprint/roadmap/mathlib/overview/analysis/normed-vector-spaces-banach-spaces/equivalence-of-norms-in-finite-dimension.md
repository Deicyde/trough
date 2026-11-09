# Equivalence of norms in finite dimension

The continuous linear equivalence induced by a linear equivalence on a finite-dimensional
space.

```lean
LinearEquiv.toContinuousLinearEquiv.{u, v, w} {𝕜 : Type u} [hnorm : NontriviallyNormedField 𝕜]
  {E : Type v} [AddCommGroup E] [_root_.Module 𝕜 E] [TopologicalSpace E] [IsTopologicalAddGroup E]
  [ContinuousSMul 𝕜 E] {F : Type w} [AddCommGroup F] [_root_.Module 𝕜 F] [TopologicalSpace F]
  [IsTopologicalAddGroup F] [ContinuousSMul 𝕜 F] [CompleteSpace 𝕜] [T2Space E] [T2Space F]
  [FiniteDimensional 𝕜 E] (e : E ≃ₗ[𝕜] F) : E ≃L[𝕜] F
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `LinearEquiv.toContinuousLinearEquiv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Module/FiniteDimension.html#LinearEquiv.toContinuousLinearEquiv)
- [Source of `LinearEquiv.toContinuousLinearEquiv` in Mathlib/Topology/Algebra/Module/FiniteDimension.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Algebra/Module/FiniteDimension.lean#L370)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L281)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L426)
