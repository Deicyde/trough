---
declaration: theorem
origin: cited
lean: CovariantDerivative.hasConstantSectionalCurvature_iff_isConstantCurvatureTensor
statement: formalized
proof: formalized
---

# CovariantDerivative.hasConstantSectionalCurvature_iff_isConstantCurvatureTensor

A metric-compatible torsion-free connection has constant sectional curvature `κ` if and only
if its curvature tensor is the constant-curvature tensor `R(w, u)v = κ (⟨u, v⟩ w - ⟨w, v⟩ u)` at
every point. Applied to the Levi-Civita connection, this identifies constant sectional curvature
of a Riemannian manifold with the constant-curvature equation.

```lean
CovariantDerivative.hasConstantSectionalCurvature_iff_isConstantCurvatureTensor.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 2 E fun x => TangentSpace I x]
  (cov : CovariantDerivative I E fun x => TangentSpace I x) [cov.ContMDiffCovariantDerivative ↑⊤]
  (hcov : cov.IsMetricCompatible) (ht : cov.torsion = 0) (κ : ℝ) :
  cov.HasConstantSectionalCurvature hcov κ ↔
    Bundle.RiemannianBundle.g.IsConstantCurvatureTensor cov ⋯ κ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CovariantDerivative.IsMetricCompatible.riemannCurvatureTensor_eq_of_forall_linearIndependent](covariantderivative-ismetriccompatible-riemanncu.md)

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.hasConstantSectionalCurvature_iff_isConstantCurvatureTensor`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Polarization.html#CovariantDerivative.hasConstantSectionalCurvature_iff_isConstantCurvatureTensor).

## Sources

- [Tau Ceti documentation: `CovariantDerivative.hasConstantSectionalCurvature_iff_isConstantCurvatureTensor`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Polarization.html#CovariantDerivative.hasConstantSectionalCurvature_iff_isConstantCurvatureTensor)
- [Source of `CovariantDerivative.hasConstantSectionalCurvature_iff_isConstantCurvatureTensor` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Polarization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Polarization.lean#L143)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
