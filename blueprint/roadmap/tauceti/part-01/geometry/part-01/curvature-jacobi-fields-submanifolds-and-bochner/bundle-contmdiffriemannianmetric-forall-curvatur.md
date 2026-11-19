---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.forall_curvatureTensor_leviCivitaConnection_eq_zero_iff
statement: formalized
proof: formalized
---

# Bundle.ContMDiffRiemannianMetric.forall_curvatureTensor_leviCivitaConnection_eq_zero_iff

For a bundled smooth Riemannian metric `g` on a boundaryless manifold, vanishing of the
curvature tensor on an open set `U` is equivalent to a local Euclidean isometry around every point
of `U`.

```lean
Bundle.ContMDiffRiemannianMetric.forall_curvatureTensor_leviCivitaConnection_eq_zero_iff.{u_1, u_2,
    u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] [BoundarylessManifold I M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x) {U : Set M}
  (hU : IsOpen U) :
  (∀ x ∈ U, (CovariantDerivative.leviCivitaConnection I M).curvatureTensor x = 0) ↔
    ∀ x ∈ U, ∃ W, ∃ (hxW : x ∈ W), ∃ r, ∃ (_ : 0 < r), ∃ Ψ, ↑W ⊆ U ∧ ↑(Ψ ⟨x, hxW⟩) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for manifolds](../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](../../part-02/manifold/part-03/the-koszul-formula.md)
- [The Poincaré lemma on manifolds](../../part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.forall_curvatureTensor_leviCivitaConnection_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Isometry/Flat.html#Bundle.ContMDiffRiemannianMetric.forall_curvatureTensor_leviCivitaConnection_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.forall_curvatureTensor_leviCivitaConnection_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Isometry/Flat.html#Bundle.ContMDiffRiemannianMetric.forall_curvatureTensor_leviCivitaConnection_eq_zero_iff)
- [Source of `Bundle.ContMDiffRiemannianMetric.forall_curvatureTensor_leviCivitaConnection_eq_zero_iff` in TauCeti/Geometry/Manifold/Riemannian/Isometry/Flat.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Isometry/Flat.lean#L477)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
