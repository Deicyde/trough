# Uniform time existence

If there exists `ε > 0` such that the local integral curve at each point `x : M` is defined at
least on an open interval `Ioo (-ε) ε`, then every point on `M` has a global integral curve
passing through it.

See Lemma 9.15, [J.M. Lee (2012)][lee2012].

```lean
exists_isMIntegralCurve_of_isMIntegralCurveOn.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] [T2Space M] [BoundarylessManifold I M]
  {v : (x : M) → TangentSpace I x} (hv : ContMDiff I I.tangent 1 fun x => ⟨x, v x⟩) {ε : ℝ}
  (hε : 0 < ε) (h : ∀ (x : M), ∃ γ, γ 0 = x ∧ IsMIntegralCurveOn γ v (Set.Ioo (-ε) ε)) (x : M) :
  ∃ γ, γ 0 = x ∧ IsMIntegralCurve γ v
```

## Depends on

- [Hausdorff space](../../../topology/general-topology/part-01/hausdorff-space.md)
- [Integral curves](integral-curves.md)
- [Smooth map between manifolds](smooth-map-between-manifolds.md)
- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Tangent bundle](tangent-bundle.md)
- [Topological fiber bundle](../../../topology/general-topology/part-01/topological-fiber-bundle.md)

## Proof depends on

- [Characteristic zero](../../../general-algebra/field-theory/characteristic-zero.md)
- [Ordered ring](../../../general-algebra/rings/ordered-ring.md)
- [Uniqueness of integral curves](uniqueness-of-integral-curves.md)

## Sources

- [Mathlib documentation: `exists_isMIntegralCurve_of_isMIntegralCurveOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IntegralCurve/UniformTime.html#exists_isMIntegralCurve_of_isMIntegralCurveOn)
- [Source of `exists_isMIntegralCurve_of_isMIntegralCurveOn` in Mathlib/Geometry/Manifold/IntegralCurve/UniformTime.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Manifold/IntegralCurve/UniformTime.lean#L163)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L455)
