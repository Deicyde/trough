---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.exists_abs_inner_mfderiv_riemannianExp_sub_le
statement: formalized
proof: formalized
---

# Uniform quadratic expansion of the exponential metric

The error is bounded by
`C ‖v‖³ ‖w‖ ‖z‖` on one tangent ball, independently of `w` and `z`. The ball lies in the
natural exponential domain; no completeness assumption is needed.

```lean
TauCeti.Manifold.exists_abs_inner_mfderiv_riemannianExp_sub_le.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] (p : M) :
  ∃ r > 0,
    ∃ C > 0,
      Metric.ball 0 r ⊆ TauCeti.Manifold.expDomain I M p ∧
        ∀ v ∈ Metric.ball 0 r,
          ∀ (w z : TangentSpace I p),
            |inner ℝ ((mfderiv% (TauCeti.Manifold.riemannianExp I M p) v) w)
                      ((mfderiv% (TauCeti.Manifold.riemannianExp I M p) v) z) -
                    inner ℝ w z +
                  1 / 3 *
                    inner ℝ
                      (((((CovariantDerivative.leviCivitaConnection I M).curvatureTensor p) w) v) v)
                      z| ≤
              C * ‖v‖ ^ 3 * ‖w‖ * ‖z‖
```

## Depends on

- [TauCeti.Manifold.riemannianExp](../geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Proof depends on

- [The inverse function theorem for manifolds](../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)
- [TauCeti.Manifold.IsJacobiFieldOn](tauceti-manifold-isjacobifieldon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.exists_abs_inner_mfderiv_riemannianExp_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Normal/Expansion.html#TauCeti.Manifold.exists_abs_inner_mfderiv_riemannianExp_sub_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.exists_abs_inner_mfderiv_riemannianExp_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Normal/Expansion.html#TauCeti.Manifold.exists_abs_inner_mfderiv_riemannianExp_sub_le)
- [Source of `TauCeti.Manifold.exists_abs_inner_mfderiv_riemannianExp_sub_le` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Normal/Expansion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Normal/Expansion.lean#L180)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
