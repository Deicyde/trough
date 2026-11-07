---
declaration: theorem
origin: cited
lean: CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor_eq_of_forall_linearIndependent
statement: formalized
proof: formalized
---

# CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor\_eq\_of\_forall\_linearIndependent

For a metric-compatible torsion-free connection, the Riemann curvature tensor at `x` is the
only quadrilinear form with the algebraic symmetries of a curvature tensor whose values
`T(u, v, v, u)` on linearly independent pairs are the sectional-curvature numerators
`⟨R(u, v)v, u⟩`.

```lean
CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor_eq_of_forall_linearIndependent.{u_1,
    u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle (TangentSpace I)]
  {cov : CovariantDerivative I E (TangentSpace I)} [cov.ContMDiffCovariantDerivative ↑⊤]
  [IsContMDiffRiemannianBundle I 2 E (TangentSpace I)] (hcov : cov.IsMetricCompatible)
  (ht : cov.torsion = 0) (x : M)
  {T :
    TangentSpace I x →ₗ[ℝ] TangentSpace I x →ₗ[ℝ] TangentSpace I x →ₗ[ℝ] TangentSpace I x →ₗ[ℝ] ℝ}
  (h₁ : ∀ (u v w z : TangentSpace I x), (((T u) v) w) z = -(((T v) u) w) z)
  (h₂ : ∀ (u v w z : TangentSpace I x), (((T u) v) w) z = -(((T u) v) z) w)
  (h₃ : ∀ (u v w z : TangentSpace I x), (((T u) v) w) z + (((T v) w) u) z + (((T w) u) v) z = 0)
  (hT :
    ∀ (u v : TangentSpace I x),
      LinearIndependent ℝ ![u, v] →
        ((((cov.riemannCurvatureTensor x) u) v) v) u = (((T u) v) v) u) :
  cov.riemannCurvatureTensor x = T
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [LinearMap.six\_mul\_apply\_eq\_of\_cyclic\_eq\_zero](linearmap-six-mul-apply-eq-of-cyclic-eq-zero.md)

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor_eq_of_forall_linearIndependent`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Riemann.html#CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor_eq_of_forall_linearIndependent).

## Sources

- [Tau Ceti documentation: `CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor_eq_of_forall_linearIndependent`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Riemann.html#CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor_eq_of_forall_linearIndependent)
- [Source of `CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor_eq_of_forall_linearIndependent` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Riemann.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Riemann.lean#L143)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
