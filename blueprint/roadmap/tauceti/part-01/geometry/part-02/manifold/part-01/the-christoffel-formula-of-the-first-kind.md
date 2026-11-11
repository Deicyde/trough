---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.two_mul_leviCivitaConnection_model_space
statement: formalized
proof: formalized
---

# The Christoffel formula of the first kind

If the Riemannian metric of the model space
`F` is the field of bilinear forms `g`, differentiable at `x`, then the Levi-Civita derivative of
a vector field `V` differentiable at `x` satisfies
`2 g(∇_u V, w) = 2 g(DV(u), w) + (Dg(u))(V, w) + (Dg(V))(w, u) - (Dg(w))(u, V)`.
Tangent vectors are read in the model space through `tangentSpaceCastModel`.

```lean
TauCeti.Manifold.two_mul_leviCivitaConnection_model_space.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F]
  [Bundle.RiemannianBundle fun x => TangentSpace (modelWithCornersSelf ℝ F) x]
  [IsContMDiffRiemannianBundle (modelWithCornersSelf ℝ F) 1 F fun x =>
      TangentSpace (modelWithCornersSelf ℝ F) x]
  {g : F → F →L[ℝ] F →L[ℝ] ℝ} {x : F} {V : (y : F) → TangentSpace (modelWithCornersSelf ℝ F) y}
  (hg :
    ∀ (y : F) (v w : TangentSpace (modelWithCornersSelf ℝ F) y),
      inner ℝ v w =
        ((g y) ((tangentSpaceCastModel (modelWithCornersSelf ℝ F) y) v))
          ((tangentSpaceCastModel (modelWithCornersSelf ℝ F) y) w))
  (hgx : DifferentiableAt ℝ g x) (hV : DifferentiableAt ℝ V x) (u w : F) :
  2 *
      ((g x)
          ((tangentSpaceCastModel (modelWithCornersSelf ℝ F) x)
            ((↑(CovariantDerivative.leviCivitaConnection (modelWithCornersSelf ℝ F) F) V x)
              ((tangentSpaceCastModel (modelWithCornersSelf ℝ F) x).symm u))))
        w =
    2 * ((g x) ((fderiv ℝ V x) u)) w +
          (((fderiv ℝ g x) u) ((tangentSpaceCastModel (modelWithCornersSelf ℝ F) x) (V x))) w +
        (((fderiv ℝ g x) ((tangentSpaceCastModel (modelWithCornersSelf ℝ F) x) (V x))) w) u -
      (((fderiv ℝ g x) w) u) ((tangentSpaceCastModel (modelWithCornersSelf ℝ F) x) (V x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.two_mul_leviCivitaConnection_model_space`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/VectorSpace.html#TauCeti.Manifold.two_mul_leviCivitaConnection_model_space).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.two_mul_leviCivitaConnection_model_space`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/VectorSpace.html#TauCeti.Manifold.two_mul_leviCivitaConnection_model_space)
- [Source of `TauCeti.Manifold.two_mul_leviCivitaConnection_model_space` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/VectorSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/VectorSpace.lean#L77)
