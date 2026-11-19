---
declaration: theorem
origin: cited
lean: TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus for a smooth `1`-simplex

Over a smooth `1`-simplex `σ`
of any charted space `M`, the integral of the differential of a `C¹` function `f : M → F` is the
difference of its values at the endpoints `σ(e₀)` and `σ(0)`. This fixes the sign convention of
`TauCeti.SmoothSimplex.integral_mextDeriv`: the face `δ₀ σ` is the endpoint and `δ₁ σ` the initial
point.

```lean
TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction.{u, u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u} [TopologicalSpace M] [ChartedSpace H M] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] (σ : TauCeti.SmoothSimplex I M 1) {f : M → F}
  (hf : ContMDiff I (modelWithCornersSelf ℝ F) 1 f) :
  σ.integral (TauCeti.mextDeriv (TauCeti.RoughForm.ofFunction I f)) =
    f (σ.toContinuousMap ⟨EuclideanSpace.single 0 1, ⋯⟩) - f (σ.toContinuousMap ⟨0, ⋯⟩)
```

## Depends on

- [TauCeti.smoothSingularSubcomplex](tauceti-smoothsingularsubcomplex.md)

## Proof depends on

- [Fundamental theorem of calculus for smooth `1`-simplices (pointwise `C¹` function)](fundamental-theorem-of-calculus-for-smooth-1-sim.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction)
- [Source of `TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction` in TauCeti/Geometry/Manifold/SmoothSingular/Stokes.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.lean#L255)
