---
declaration: theorem
origin: cited
lean: CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero
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

## Proof depends on

- [VectorField.jacobi\_identity\_mlieBracket\_apply](vectorfield-jacobi-identity-mliebracket-apply.md)

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondBianchi.html#CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero).

## Sources

- [Tau Ceti documentation: `CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondBianchi.html#CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero)
- [Source of `CovariantDerivative.covariantDerivative_curvatureOperator_cyclic_eq_zero` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondBianchi.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondBianchi.lean#L123)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
