---
declaration: theorem
origin: cited
lean: CovariantDerivative.curvatureOperator_addOneForm
statement: formalized
proof: formalized
---

# Curvature of a connection plus a one-form

If `A` is a one-form with values in the
endomorphisms of `V`, then

`R^(∇ + A)(X, Y) σ = R^∇(X, Y) σ + (∇_X (A(σ, Y)) - ∇_Y (A(σ, X)) - A(σ, [X, Y]))`
`    + (A(∇_Y σ, X) - A(∇_X σ, Y)) + (A(A(σ, Y), X) - A(A(σ, X), Y))`,

where `A(σ, X) = A x (σ x) (X x)`. The hypotheses are the differentiability at the point of the
four sections differentiated by the outer covariant derivatives.

```lean
CovariantDerivative.curvatureOperator_addOneForm.{u_1, u_2, u_3, u_4, u_5, u_6} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3}
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u_4} [TopologicalSpace M]
  [ChartedSpace H M] {F : Type u_5} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {V : M → Type u_6}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module 𝕜 (V x)] [(x : M) → TopologicalSpace (V x)]
  [∀ (x : M), IsTopologicalAddGroup (V x)] [∀ (x : M), ContinuousSMul 𝕜 (V x)] [FiberBundle F V]
  (cov : CovariantDerivative I F V) (A : (x : M) → V x →L[𝕜] TangentSpace I x →L[𝕜] V x)
  {X Y : (x : M) → TangentSpace I x} {σ : (x : M) → V x} {x : M}
  (hXσ : (MDiffAt fun y => ⟨y, (↑cov σ y) (X y)⟩) x)
  (hYσ : (MDiffAt fun y => ⟨y, (↑cov σ y) (Y y)⟩) x)
  (hAX : (MDiffAt fun y => ⟨y, ((A y) (σ y)) (X y)⟩) x)
  (hAY : (MDiffAt fun y => ⟨y, ((A y) (σ y)) (Y y)⟩) x) :
  (cov.addOneForm A).curvatureOperator X Y σ x =
    cov.curvatureOperator X Y σ x +
          ((↑cov (fun y => ((A y) (σ y)) (Y y)) x) (X x) -
              (↑cov (fun y => ((A y) (σ y)) (X y)) x) (Y x) -
            ((A x) (σ x)) (VectorField.mlieBracket I X Y x)) +
        (((A x) ((↑cov σ x) (Y x))) (X x) - ((A x) ((↑cov σ x) (X x))) (Y x)) +
      (((A x) (((A x) (σ x)) (Y x))) (X x) - ((A x) (((A x) (σ x)) (X x))) (Y x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.curvatureOperator_addOneForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/AddOneForm.html#CovariantDerivative.curvatureOperator_addOneForm).

## Sources

- [Tau Ceti documentation: `CovariantDerivative.curvatureOperator_addOneForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/AddOneForm.html#CovariantDerivative.curvatureOperator_addOneForm)
- [Source of `CovariantDerivative.curvatureOperator_addOneForm` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/AddOneForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/AddOneForm.lean#L75)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
