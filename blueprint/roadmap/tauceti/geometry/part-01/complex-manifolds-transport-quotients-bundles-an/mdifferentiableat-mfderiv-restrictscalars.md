---
declaration: theorem
origin: cited
lean: MDifferentiableAt.mfderiv_restrictScalars
statement: formalized
proof: formalized
---

# MDifferentiableAt.mfderiv_restrictScalars

At a point where `f` is differentiable for the models over `𝕜'`, the derivative of `f` over the
smaller field `𝕜` is its derivative over `𝕜'` with scalars restricted to `𝕜`, both read in the model
spaces. For instance, the real derivative of a holomorphic map is its complex derivative.

```lean
MDifferentiableAt.mfderiv_restrictScalars.{u_1, u_2, u_3, u_4, u_5, u_6} (𝕜 : Type u_1)
  {𝕜' : Type u_2} [NontriviallyNormedField 𝕜] [NontriviallyNormedField 𝕜'] [NormedAlgebra 𝕜 𝕜']
  {E : Type u_3} [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace 𝕜' E] [IsScalarTower 𝕜 𝕜' E]
  {E' : Type u_4} [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] [NormedSpace 𝕜' E']
  [IsScalarTower 𝕜 𝕜' E'] {M : Type u_5} [TopologicalSpace M] [ChartedSpace E M] {N : Type u_6}
  [TopologicalSpace N] [ChartedSpace E' N] {f : M → N} {x : M} (h : MDiffAt f x) :
  ↑(tangentSpaceCastModel (modelWithCornersSelf 𝕜 E') (f x)) ∘SL
      mfderiv% f x ∘SL ↑(tangentSpaceCastModel (modelWithCornersSelf 𝕜 E) x).symm =
    ContinuousLinearMap.restrictScalars 𝕜
      (↑(tangentSpaceCastModel (modelWithCornersSelf 𝕜' E') (f x)) ∘SL
        mfderiv% f x ∘SL ↑(tangentSpaceCastModel (modelWithCornersSelf 𝕜' E) x).symm)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MDifferentiableAt.mfderiv_restrictScalars`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/MFDeriv/RestrictScalars.html#MDifferentiableAt.mfderiv_restrictScalars).

## Sources

- [Tau Ceti documentation: `MDifferentiableAt.mfderiv_restrictScalars`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/MFDeriv/RestrictScalars.html#MDifferentiableAt.mfderiv_restrictScalars)
- [Source of `MDifferentiableAt.mfderiv_restrictScalars` in TauCeti/Geometry/Manifold/MFDeriv/RestrictScalars.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/MFDeriv/RestrictScalars.lean#L175)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
