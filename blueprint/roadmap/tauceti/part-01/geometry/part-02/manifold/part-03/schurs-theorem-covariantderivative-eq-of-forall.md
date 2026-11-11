---
declaration: theorem
origin: cited
lean: CovariantDerivative.eq_of_forall_hasSectionalCurvatureAt, CovariantDerivative.hasConstantSectionalCurvature_of_forall_hasSectionalCurvatureAt, CovariantDerivative.mfderiv_eq_zero_of_curvatureTensor_eq_smul_inner_sub
statement: formalized
proof: formalized
---

# Schur's theorem (`CovariantDerivative.eq_of_forall_hasSectionalCurvatureAt`)

Let a metric-compatible torsion-free connection on a preconnected
manifold of dimension at least three have, at every point `x`, the same sectional curvature `κ x`
on all tangent two-planes at `x`. Then `κ` is constant.

```lean
CovariantDerivative.eq_of_forall_hasSectionalCurvatureAt.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  {cov : CovariantDerivative I E fun x => TangentSpace I x} [cov.ContMDiffCovariantDerivative ↑⊤]
  [PreconnectedSpace M] (hcov : cov.IsMetricCompatible) (ht : cov.torsion = 0)
  (hdim : 3 ≤ Module.finrank ℝ E) {κ : M → ℝ}
  (hκ : ∀ (x : M), cov.HasSectionalCurvatureAt hcov x (κ x)) (x y : M) : κ x = κ y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The second Bianchi identity](the-second-bianchi-identity.md)

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.eq_of_forall_hasSectionalCurvatureAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Schur.html#CovariantDerivative.eq_of_forall_hasSectionalCurvatureAt).

## Other forms

**Schur's theorem, global form.** Formalized in Tau Ceti as [`CovariantDerivative.hasConstantSectionalCurvature_of_forall_hasSectionalCurvatureAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Schur.html#CovariantDerivative.hasConstantSectionalCurvature_of_forall_hasSectionalCurvatureAt).

```lean
CovariantDerivative.hasConstantSectionalCurvature_of_forall_hasSectionalCurvatureAt.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  {cov : CovariantDerivative I E fun x => TangentSpace I x} [cov.ContMDiffCovariantDerivative ↑⊤]
  [PreconnectedSpace M] (hcov : cov.IsMetricCompatible) (ht : cov.torsion = 0)
  (hdim : 3 ≤ Module.finrank ℝ E) {κ : M → ℝ}
  (hκ : ∀ (x : M), cov.HasSectionalCurvatureAt hcov x (κ x)) (x₀ : M) :
  cov.HasConstantSectionalCurvature hcov (κ x₀)
```

**Schur's theorem, local form.** Formalized in Tau Ceti as [`CovariantDerivative.mfderiv_eq_zero_of_curvatureTensor_eq_smul_inner_sub`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Schur.html#CovariantDerivative.mfderiv_eq_zero_of_curvatureTensor_eq_smul_inner_sub).

```lean
CovariantDerivative.mfderiv_eq_zero_of_curvatureTensor_eq_smul_inner_sub.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  {cov : CovariantDerivative I E fun x => TangentSpace I x} [cov.ContMDiffCovariantDerivative ↑⊤]
  (hcov : cov.IsMetricCompatible) (ht : cov.torsion = 0) (hdim : 3 ≤ Module.finrank ℝ E) {κ : M → ℝ}
  {x : M}
  (hκ :
    ∀ᶠ (y : M) in nhds x,
      ∀ (w u v : TangentSpace I y),
        (((cov.curvatureTensor y) w) u) v = κ y • (inner ℝ u v • w - inner ℝ w v • u)) :
  mfderiv% κ x = 0
```

## Sources

- [Tau Ceti documentation: `CovariantDerivative.eq_of_forall_hasSectionalCurvatureAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Schur.html#CovariantDerivative.eq_of_forall_hasSectionalCurvatureAt)
- [Source of `CovariantDerivative.eq_of_forall_hasSectionalCurvatureAt` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Schur.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Schur.lean#L194)
