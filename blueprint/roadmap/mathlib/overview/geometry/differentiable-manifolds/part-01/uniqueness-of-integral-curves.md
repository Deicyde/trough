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
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Smooth map between manifolds](smooth-map-between-manifolds.md)
- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Tangent bundle](tangent-bundle.md)
- [Topological fiber bundle](../../../topology/general-topology/part-01/topological-fiber-bundle.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../affine-and-euclidean-geometry/affine-function.md)
- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../topology/general-topology/part-01/closed-map.md)
- [Completion of an abelian topological group](../../../topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Convex function](../../../analysis/convexity/convex-function.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Existence of bases](../../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Finite product of metric spaces](../../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Grönwall lemma](../../../../undergraduate/multivariable-calculus/differential-equations/gronwall-lemma.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Inner product space, over $R$ or $C$](../../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Kernel of a linear map](../../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Sequential space](../../../topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [Sum of subspaces](../../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.html#isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless)
- [Source of `isMIntegralCurveOn_Ioo_eqOn_of_contMDiff_boundaryless` in Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IntegralCurve/ExistUnique.lean#L228)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L457)
