---
declaration: theorem
origin: cited
lean: CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero, CovariantDerivative.derivCurvatureTensor_cyclic_eq_zero, CovariantDerivative.exteriorCovariantDerivativeTwo_curvatureForm, CovariantDerivative.derivCurvatureTensor_cyclic_eq_neg_torsion
statement: formalized
proof: formalized
---

# The second Bianchi identity

Let `∇` be a smooth connection on a vector bundle and
`∇ᵀ` a smooth torsion-free connection on the tangent bundle. Writing
`(∇_X R)(Y, Z) σ = ∇_X (R(Y, Z) σ) - R(∇ᵀ_X Y, Z) σ - R(Y, ∇ᵀ_X Z) σ - R(Y, Z) (∇_X σ)`, the
cyclic sum `(∇_X R)(Y, Z) σ + (∇_Y R)(Z, X) σ + (∇_Z R)(X, Y) σ` vanishes.

```lean
CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero.{u_1, u_2, u_3, u_4, u_5}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F]
  {V : M → Type u_5} [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)]
  [∀ (x : M), IsTopologicalAddGroup (V x)] [∀ (x : M), ContinuousSMul ℝ (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] (cov : CovariantDerivative I F V) [cov.ContMDiffCovariantDerivative ↑⊤]
  {X Y Z : (x : M) → TangentSpace I x} {σ : (x : M) → V x}
  (covT : CovariantDerivative I E (TangentSpace I)) [covT.ContMDiffCovariantDerivative ↑⊤]
  (ht : covT.IsTorsionFree) (hX : ContMDiff I I.tangent ↑⊤ fun x => ⟨x, X x⟩)
  (hY : ContMDiff I I.tangent ↑⊤ fun x => ⟨x, Y x⟩)
  (hZ : ContMDiff I I.tangent ↑⊤ fun x => ⟨x, Z x⟩)
  (hσ : ContMDiff I (I.prod (modelWithCornersSelf ℝ F)) ↑⊤ fun x => ⟨x, σ x⟩) (x : M) :
  (↑cov (cov.curvatureOperator Y Z σ) x) (X x) -
              cov.curvatureOperator (fun y => (↑covT Y y) (X y)) Z σ x -
            cov.curvatureOperator Y (fun y => (↑covT Z y) (X y)) σ x -
          cov.curvatureOperator Y Z (fun y => (↑cov σ y) (X y)) x +
        ((↑cov (cov.curvatureOperator Z X σ) x) (Y x) -
              cov.curvatureOperator (fun y => (↑covT Z y) (Y y)) X σ x -
            cov.curvatureOperator Z (fun y => (↑covT X y) (Y y)) σ x -
          cov.curvatureOperator Z X (fun y => (↑cov σ y) (Y y)) x) +
      ((↑cov (cov.curvatureOperator X Y σ) x) (Z x) -
            cov.curvatureOperator (fun y => (↑covT X y) (Z y)) Y σ x -
          cov.curvatureOperator X (fun y => (↑covT Y y) (Z y)) σ x -
        cov.curvatureOperator X Y (fun y => (↑cov σ y) (Z y)) x) =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondBianchi.html#CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero).

## Other forms

**The second Bianchi identity, pointwise.** Formalized in Tau Ceti as [`CovariantDerivative.derivCurvatureTensor_cyclic_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Derivative/Basic.html#CovariantDerivative.derivCurvatureTensor_cyclic_eq_zero).

```lean
CovariantDerivative.derivCurvatureTensor_cyclic_eq_zero.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {V : M → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)]
  [∀ (x : M), IsTopologicalAddGroup (V x)] [∀ (x : M), ContinuousSMul ℝ (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] [ContMDiffVectorBundle (↑⊤) F V I] (cov : CovariantDerivative I F V)
  [cov.ContMDiffCovariantDerivative ↑⊤] (covT : CovariantDerivative I E (TangentSpace I))
  [covT.ContMDiffCovariantDerivative ↑⊤] (ht : covT.torsion = 0) (x : M)
  (u v w : TangentSpace I x) :
  (((cov.derivCurvatureTensor covT x) u) v) w + (((cov.derivCurvatureTensor covT x) v) w) u +
      (((cov.derivCurvatureTensor covT x) w) u) v =
    0
```

**The second Bianchi identity as covariant closedness of the curvature form.** Formalized in Tau Ceti as [`CovariantDerivative.exteriorCovariantDerivativeTwo_curvatureForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Exterior/Two.html#CovariantDerivative.exteriorCovariantDerivativeTwo_curvatureForm).

```lean
CovariantDerivative.exteriorCovariantDerivativeTwo_curvatureForm.{u_1, u_2, u_3, u_4, u_5}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {V : M → Type u_5} [TopologicalSpace (Bundle.TotalSpace F V)]
  [(x : M) → NormedAddCommGroup (V x)] [(x : M) → NormedSpace ℝ (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] [ContMDiffVectorBundle (↑⊤) F V I] (cov : CovariantDerivative I F V)
  (covT : CovariantDerivative I E (TangentSpace I)) [cov.ContMDiffCovariantDerivative ↑⊤]
  [FiniteDimensional ℝ F] :
  ((cov.hom cov).exteriorCovariantDerivativeTwo covT) cov.curvatureForm = 0
```

**The second Bianchi identity with torsion.** Formalized in Tau Ceti as [`CovariantDerivative.derivCurvatureTensor_cyclic_eq_neg_torsion`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Derivative/Torsion.html#CovariantDerivative.derivCurvatureTensor_cyclic_eq_neg_torsion).

```lean
CovariantDerivative.derivCurvatureTensor_cyclic_eq_neg_torsion.{u_1, u_2, u_3, u_4, u_5}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {V : M → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)]
  [∀ (x : M), IsTopologicalAddGroup (V x)] [∀ (x : M), ContinuousSMul ℝ (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] [ContMDiffVectorBundle (↑⊤) F V I] (cov : CovariantDerivative I F V)
  [cov.ContMDiffCovariantDerivative ↑⊤] (covT : CovariantDerivative I E (TangentSpace I)) (x : M)
  (u v w : TangentSpace I x) :
  (((cov.derivCurvatureTensor covT x) u) v) w + (((cov.derivCurvatureTensor covT x) v) w) u +
      (((cov.derivCurvatureTensor covT x) w) u) v =
    -(((cov.curvatureTensor x) (((covT.torsion x) u) v)) w +
          ((cov.curvatureTensor x) (((covT.torsion x) v) w)) u +
        ((cov.curvatureTensor x) (((covT.torsion x) w) u)) v)
```

## Sources

- [Tau Ceti documentation: `CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondBianchi.html#CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero)
- [Source of `CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondBianchi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondBianchi.lean#L123)
