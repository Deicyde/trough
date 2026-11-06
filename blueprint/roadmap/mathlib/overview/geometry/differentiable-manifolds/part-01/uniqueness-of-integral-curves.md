---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless
mathlib_file: Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.lean
---

# Uniqueness of integral curves

Mathlib states this as `isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless`.

```lean
isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I 1 M] {γ γ' : ℝ → M} {v : (x : M) → TangentSpace I x} {t₀ : ℝ} [T2Space M] {a b : ℝ}
  [BoundarylessManifold I M] (ht₀ : t₀ ∈ Set.Ioo a b)
  (hv : ContMDiff I I.tangent 1 fun x => ⟨x, v x⟩) (hγ : IsMIntegralCurveOn γ v (Set.Ioo a b))
  (hγ' : IsMIntegralCurveOn γ' v (Set.Ioo a b)) (h : γ t₀ = γ' t₀) : Set.EqOn γ γ' (Set.Ioo a b)
```

## Depends on

- [Hausdorff space](../../../topology/general-topology/part-01/hausdorff-space.md)
- [Smooth map between manifolds](smooth-map-between-manifolds.md)
- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Tangent bundle](tangent-bundle.md)
- [Topological fiber bundle](../../../topology/general-topology/part-01/topological-fiber-bundle.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.html#isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless)
- [Source of `isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless` in Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.lean#L228)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L457)
