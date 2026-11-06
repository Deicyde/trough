# Local existence of integral curves

Existence of local integral curves for a $C^1$ vector field on a `C^1` manifold without
boundary.

```lean
exists_isMIntegralCurveAt_of_contMDiffAt_boundaryless.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I 1 M] {v : (x : M) → TangentSpace I x} (t₀ : ℝ) {x₀ : M} [CompleteSpace E]
  [BoundarylessManifold I M] (hv : ContMDiffAt I I.tangent 1 (fun x => ⟨x, v x⟩) x₀) :
  ∃ γ, γ t₀ = x₀ ∧ IsMIntegralCurveAt γ v t₀
```

## Depends on

- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Tangent bundle](tangent-bundle.md)
- [Topological fiber bundle](../../../topology/general-topology/part-01/topological-fiber-bundle.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Ball](../../../topology/metric-spaces/ball.md)
- [Cauchy-Lipschitz Theorem](../../../../undergraduate/multivariable-calculus/differential-equations/cauchy-lipschitz-theorem.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable function between normed vector spaces](../../../analysis/differentiability/differentiable-function-between-normed-vector-sp.md)

## Sources

- [Mathlib documentation: `exists_isMIntegralCurveAt_of_contMDiffAt_boundaryless`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.html#exists_isMIntegralCurveAt_of_contMDiffAt_boundaryless)
- [Source of `exists_isMIntegralCurveAt_of_contMDiffAt_boundaryless` in Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.lean#L119)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L454)
