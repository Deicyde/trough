---
declaration: theorem
origin: cited
lean: TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus for a smooth `1`-simplex

The integral of the
differential of a `C¹` function over a smooth `1`-simplex `σ` is the difference of its values at
the endpoints `σ(1)` and `σ(0)`. This fixes the sign convention of
`TauCeti.SmoothSimplex.integral_mextDeriv`: the face `∂₀σ` is the endpoint and `∂₁σ` the initial
point.

```lean
TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction.{u, u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u} [TopologicalSpace M] [ChartedSpace H M] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [IsManifold I 2 M] [CompleteSpace F] (σ : TauCeti.SmoothSimplex I M 1)
  {f : M → F} (hf : ContMDiff I (modelWithCornersSelf ℝ F) 1 f) :
  σ.integral (TauCeti.mextDeriv (TauCeti.RoughForm.ofFunction I f)) =
    f
        (σ.toContinuousMap
          ⟨EuclideanSpace.single 0 1,
            TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction._proof_1⟩) -
      f (σ.toContinuousMap ⟨0, ⋯⟩)
```

## Depends on

- [TauCeti.SmoothSimplex.integral](tauceti-smoothsimplex-integral.md)
- [TauCeti.smoothSingularSubcomplex](tauceti-smoothsingularsubcomplex.md)

## Proof depends on

- [Stokes' theorem on singular `1`-chains](../../part-02/manifold/part-03/stokes-theorem-on-singular-1-chains.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction)
- [Source of `TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction` in TauCeti/Geometry/Manifold/SmoothSingular/Stokes.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.lean#L136)
