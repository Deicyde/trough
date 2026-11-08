---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.curvatureOperator_leviCivitaConnection_rescale
statement: formalized
proof: formalized
---

# Curvature under conformal change

Let `∇` be a Levi-Civita connection of a `C¹` metric `g`
and `A` the conformal connection tensor of a positive function `f`. Then the curvature of the
Levi-Civita connection of `f g` is

`R^(f g)(X, Y) Z = R^∇(X, Y) Z + (∇_X A)(Z, Y) - (∇_Y A)(Z, X) + A(A(Z, Y), X) - A(A(Z, X), Y)`,

with `(∇_X A)(Z, Y) = ∇_X (A(Z, Y)) - A(∇_X Z, Y) - A(Z, ∇_X Y)`. The metric `g` and the
function `f` are assumed `Cⁿ` on all of `M` for some `1 ≤ n`, and `Z` differentiable on all of `M`;
the remaining hypotheses are differentiability at `x` of `X`, `Y`, `∇_X Z`, `∇_Y Z`, `A(Z, X)` and
`A(Z, Y)`.

```lean
Bundle.ContMDiffRiemannianMetric.curvatureOperator_leviCivitaConnection_rescale.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I 2 M] {n : WithTop ℕ∞}
  (g : Bundle.ContMDiffRiemannianMetric I n E fun x => TangentSpace I x) (hn : 1 ≤ n) {f : M → ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) n f) (hf_pos : ∀ (x : M), 0 < f x)
  {cov : CovariantDerivative I E fun x => TangentSpace I x}
  (hcov : CovariantDerivative.IsLeviCivitaConnection I cov) {X Y Z : (x : M) → TangentSpace I x}
  {x : M} (hX : (MDiffAt fun x => ⟨x, X x⟩) x) (hY : (MDiffAt fun x => ⟨x, Y x⟩) x)
  (hZ : MDiff fun x => ⟨x, Z x⟩) (hXZ : (MDiffAt fun y => ⟨y, (↑cov Z y) (X y)⟩) x)
  (hYZ : (MDiffAt fun y => ⟨y, (↑cov Z y) (Y y)⟩) x)
  (hAX : (MDiffAt fun y => ⟨y, ((TauCeti.Manifold.conformalConnectionTensor I f y) (Z y)) (X y)⟩) x)
  (hAY :
    (MDiffAt fun y => ⟨y, ((TauCeti.Manifold.conformalConnectionTensor I f y) (Z y)) (Y y)⟩) x) :
  (CovariantDerivative.leviCivitaConnection I M).curvatureOperator X Y Z x =
    cov.curvatureOperator X Y Z x +
          ((↑cov (fun y => ((TauCeti.Manifold.conformalConnectionTensor I f y) (Z y)) (Y y)) x)
                (X x) -
              ((TauCeti.Manifold.conformalConnectionTensor I f x) ((↑cov Z x) (X x))) (Y x) -
            ((TauCeti.Manifold.conformalConnectionTensor I f x) (Z x)) ((↑cov Y x) (X x))) -
        ((↑cov (fun y => ((TauCeti.Manifold.conformalConnectionTensor I f y) (Z y)) (X y)) x)
              (Y x) -
            ((TauCeti.Manifold.conformalConnectionTensor I f x) ((↑cov Z x) (Y x))) (X x) -
          ((TauCeti.Manifold.conformalConnectionTensor I f x) (Z x)) ((↑cov X x) (Y x))) +
      (((TauCeti.Manifold.conformalConnectionTensor I f x)
            (((TauCeti.Manifold.conformalConnectionTensor I f x) (Z x)) (Y x)))
          (X x) -
        ((TauCeti.Manifold.conformalConnectionTensor I f x)
            (((TauCeti.Manifold.conformalConnectionTensor I f x) (Z x)) (X x)))
          (Y x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Curvature of a connection plus a one-form](curvature-of-a-connection-plus-a-one-form.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.curvatureOperator_leviCivitaConnection_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Conformal/Basic.html#Bundle.ContMDiffRiemannianMetric.curvatureOperator_leviCivitaConnection_rescale).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.curvatureOperator_leviCivitaConnection_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Conformal/Basic.html#Bundle.ContMDiffRiemannianMetric.curvatureOperator_leviCivitaConnection_rescale)
- [Source of `Bundle.ContMDiffRiemannianMetric.curvatureOperator_leviCivitaConnection_rescale` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Conformal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Conformal/Basic.lean#L139)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
