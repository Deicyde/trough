---
declaration: theorem
origin: cited
lean: TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction_of_contMDiffAt
statement: formalized
proof: formalized
---

# Fundamental theorem of calculus for smooth `1`-simplices (pointwise `C¹` function)

Over a
smooth `1`-simplex `σ` of any charted space `M`, the integral of `df` for a function `f : M → F`
that is `C¹` at each point of the image of `σ` equals the difference of the values of `f` at the
endpoints `σ(e₀)` and `σ(0)`.

```lean
TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction_of_contMDiffAt.{u, u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u} [TopologicalSpace M] [ChartedSpace H M] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] (σ : TauCeti.SmoothSimplex I M 1)
  {f : M → F}
  (hf :
    ∀ (x : ↑(TauCeti.fullSimplex 1)),
      ContMDiffAt I (modelWithCornersSelf ℝ F) 1 f (σ.toContinuousMap x)) :
  σ.integral (TauCeti.mextDeriv (TauCeti.RoughForm.ofFunction I f)) =
    f (σ.toContinuousMap ⟨EuclideanSpace.single 0 1, ⋯⟩) - f (σ.toContinuousMap ⟨0, ⋯⟩)
```

## Depends on

- [TauCeti.smoothSingularSubcomplex](tauceti-smoothsingularsubcomplex.md)

## Proof depends on

- [The fundamental theorem of calculus along a coordinate of the standard simplex](../../../../measure-theory/integral/part-01/the-fundamental-theorem-of-calculus-along-a-coor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction_of_contMDiffAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction_of_contMDiffAt).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction_of_contMDiffAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.html#TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction_of_contMDiffAt)
- [Source of `TauCeti.SmoothSimplex.integral_mextDeriv_ofFunction_of_contMDiffAt` in TauCeti/Geometry/Manifold/SmoothSingular/Stokes.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothSingular/Stokes.lean#L212)
