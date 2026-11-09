---
declaration: theorem
origin: cited
lean: CovariantDerivative.secondCovariantDerivative_sub_swap_of_isTorsionFree, CovariantDerivative.secondCovariantDerivative_sub_swap, TauCeti.Manifold.mvfderiv_hessian_sub_swap
statement: formalized
proof: formalized
---

# The Ricci identity

For a torsion-free connection `∇ᵀ` on the tangent bundle, the
antisymmetric part of the second covariant derivative of a smooth section `σ` is the curvature
of `∇` applied to `σ`: `∇²σ(u, v) - ∇²σ(v, u) = R(u, v) σ`.

```lean
CovariantDerivative.secondCovariantDerivative_sub_swap_of_isTorsionFree.{u_1, u_2, u_3, u_4, u_5}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] {V : M → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)]
  [∀ (x : M), IsTopologicalAddGroup (V x)] [∀ (x : M), ContinuousSMul ℝ (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] (cov : CovariantDerivative I F V) [cov.ContMDiffCovariantDerivative ↑⊤]
  (covT : CovariantDerivative I E (TangentSpace I)) {σ : (y : M) → V y} [FiniteDimensional ℝ E]
  [T2Space M] [FiniteDimensional ℝ F] [ContMDiffVectorBundle (↑⊤) F V I] (ht : covT.IsTorsionFree)
  (hσ : ContMDiff I (I.prod (modelWithCornersSelf ℝ F)) ↑⊤ fun y => ⟨y, σ y⟩) (x : M)
  (u v : TangentSpace I x) :
  ((cov.secondCovariantDerivative covT σ x) u) v - ((cov.secondCovariantDerivative covT σ x) v) u =
    (((cov.curvatureTensor x) u) v) (σ x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.secondCovariantDerivative_sub_swap_of_isTorsionFree`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondCovariantDerivative.html#CovariantDerivative.secondCovariantDerivative_sub_swap_of_isTorsionFree).

## Other forms

**The Ricci identity, with its torsion correction.** Formalized in Tau Ceti as [`CovariantDerivative.secondCovariantDerivative_sub_swap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondCovariantDerivative.html#CovariantDerivative.secondCovariantDerivative_sub_swap).

```lean
CovariantDerivative.secondCovariantDerivative_sub_swap.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] {V : M → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)]
  [∀ (x : M), IsTopologicalAddGroup (V x)] [∀ (x : M), ContinuousSMul ℝ (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] (cov : CovariantDerivative I F V) [cov.ContMDiffCovariantDerivative ↑⊤]
  (covT : CovariantDerivative I E (TangentSpace I)) {σ : (y : M) → V y} [FiniteDimensional ℝ E]
  [T2Space M] [FiniteDimensional ℝ F] [ContMDiffVectorBundle (↑⊤) F V I]
  (hσ : ContMDiff I (I.prod (modelWithCornersSelf ℝ F)) ↑⊤ fun y => ⟨y, σ y⟩) (x : M)
  (u v : TangentSpace I x) :
  ((cov.secondCovariantDerivative covT σ x) u) v - ((cov.secondCovariantDerivative covT σ x) v) u =
    (((cov.curvatureTensor x) u) v) (σ x) - (↑cov σ x) (((covT.torsion x) u) v)
```

**The Ricci identity for the Hessian.** Formalized in Tau Ceti as [`TauCeti.Manifold.mvfderiv_hessian_sub_swap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Hessian.html#TauCeti.Manifold.mvfderiv_hessian_sub_swap).

```lean
TauCeti.Manifold.mvfderiv_hessian_sub_swap.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {φ : M → ℝ}
  (hφ : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) φ) {X Y Z : (x : M) → TangentSpace I x}
  (hX : ContMDiff I I.tangent ↑⊤ fun x => ⟨x, X x⟩)
  (hY : ContMDiff I I.tangent ↑⊤ fun x => ⟨x, Y x⟩)
  (hZ : ContMDiff I I.tangent ↑⊤ fun x => ⟨x, Z x⟩) (x : M) :
  ((d% fun y => TauCeti.Manifold.hessian I φ y (X y) (Y y)) x) (Z x) -
              ((d% fun y => TauCeti.Manifold.hessian I φ y (X y) (Z y)) x) (Y x) -
            TauCeti.Manifold.hessian I φ x
              ((↑(CovariantDerivative.leviCivitaConnection I M) X x) (Z x)) (Y x) -
          TauCeti.Manifold.hessian I φ x (X x)
            ((↑(CovariantDerivative.leviCivitaConnection I M) Y x) (Z x)) +
        TauCeti.Manifold.hessian I φ x ((↑(CovariantDerivative.leviCivitaConnection I M) X x) (Y x))
          (Z x) +
      TauCeti.Manifold.hessian I φ x (X x)
        ((↑(CovariantDerivative.leviCivitaConnection I M) Z x) (Y x)) =
    inner ℝ
      (((((CovariantDerivative.leviCivitaConnection I M).curvatureTensor x) (Z x)) (Y x))
        (TauCeti.Manifold.mgradient I φ x))
      (X x)
```

## Sources

- [Tau Ceti documentation: `CovariantDerivative.secondCovariantDerivative_sub_swap_of_isTorsionFree`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondCovariantDerivative.html#CovariantDerivative.secondCovariantDerivative_sub_swap_of_isTorsionFree)
- [Source of `CovariantDerivative.secondCovariantDerivative_sub_swap_of_isTorsionFree` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondCovariantDerivative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/SecondCovariantDerivative.lean#L89)
