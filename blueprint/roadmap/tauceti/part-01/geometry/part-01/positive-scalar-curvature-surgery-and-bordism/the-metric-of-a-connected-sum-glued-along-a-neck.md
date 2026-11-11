---
declaration: def
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.connectedSum
statement: formalized
---

# The metric of a connected sum glued along a neck

Let `0 ≤ a < b`, and suppose that on the
neck `a < ‖v‖ < b` the gluing map `e₂ ∘ inversion 0 1 ∘ e₁⁻¹` of the connected sum carries `g₁`
to `g₂` (the hypothesis `hg`). This is the metric on `M # N` which is `g₁` on `M` outside
`e₁ (closedBall 0 a)` and `g₂` on `N` outside `e₂ (closedBall 0 b⁻¹)`
(`Bundle.ContMDiffRiemannianMetric.connectedSum_inner_mfderiv_inl`,
`Bundle.ContMDiffRiemannianMetric.connectedSum_inner_mfderiv_inr`).

```lean
Bundle.ContMDiffRiemannianMetric.connectedSum.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [T2Space M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {N : Type u_4} [TopologicalSpace N] [T2Space N]
  [ChartedSpace H N] [IsManifold I (↑⊤) N] {e₁ : E → M} {e₂ : E → N} {a b : ℝ}
  (g₁ : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x)
  (g₂ : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun y => TangentSpace I y)
  (h₁ : Topology.IsOpenEmbedding e₁) (h₂ : Topology.IsOpenEmbedding e₂)
  (d₁ : IsLocalDiffeomorph (modelWithCornersSelf ℝ E) I (↑⊤) e₁)
  (d₂ : IsLocalDiffeomorph (modelWithCornersSelf ℝ E) I (↑⊤) e₂)
  (hg :
    ∀ (v : E),
      a < ‖v‖ →
        ‖v‖ < b →
          ∀ (ξ ζ : E),
            ((g₁.inner (e₁ v)) ((mfderiv% e₁ v) ξ)) ((mfderiv% e₁ v) ζ) =
              ((g₂.inner (e₂ (EuclideanGeometry.inversion 0 1 v)))
                  ((mfderiv% e₂ (EuclideanGeometry.inversion 0 1 v))
                    ((fderiv ℝ (EuclideanGeometry.inversion 0 1) v) ξ)))
                ((mfderiv% e₂ (EuclideanGeometry.inversion 0 1 v))
                  ((fderiv ℝ (EuclideanGeometry.inversion 0 1) v) ζ)))
  (ha : 0 ≤ a) (hab : a < b) : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun p => TangentSpace I p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.connectedSum`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/ConnectedSum.html#Bundle.ContMDiffRiemannianMetric.connectedSum).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.connectedSum`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/ConnectedSum.html#Bundle.ContMDiffRiemannianMetric.connectedSum)
- [Source of `Bundle.ContMDiffRiemannianMetric.connectedSum` in TauCeti/Geometry/Manifold/Riemannian/ConnectedSum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/ConnectedSum.lean#L431)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
