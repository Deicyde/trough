---
declaration: theorem
origin: cited
lean: TauCeti.integralTopForm_mextDeriv
statement: formalized
proof: formalized
---

# TauCeti.integralTopForm_mextDeriv

Stokes' theorem for a compactly supported C1 form on an oriented smooth manifold with
boundary. The boundary carries its outward-first orientation.

```lean
TauCeti.integralTopForm_mextDeriv.{u_1} {n : ℕ} {M : Type u_1} [TopologicalSpace M]
  [ChartedSpace (EuclideanHalfSpace (n + 1)) M]
  [IsManifold (modelWithCornersEuclideanHalfSpace (n + 1)) (↑⊤) M] [T2Space M] [SigmaCompactSpace M]
  (o : TauCeti.Manifold.Orientation (modelWithCornersEuclideanHalfSpace (n + 1)) M (Fin (n + 1)))
  {φ : TauCeti.RoughForm (modelWithCornersEuclideanHalfSpace (n + 1)) M ℝ n}
  (hφ : TauCeti.IsSmoothForm (modelWithCornersEuclideanHalfSpace (n + 1)) 1 φ)
  (hc : IsCompact (tsupport φ)) :
  TauCeti.integralTopForm o (TauCeti.mextDeriv φ) =
    TauCeti.integralTopForm (TauCeti.boundaryOrientation o) (TauCeti.boundaryRestriction φ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integralTopForm_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Stokes.html#TauCeti.integralTopForm_mextDeriv).

## Sources

- [Tau Ceti documentation: `TauCeti.integralTopForm_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Stokes.html#TauCeti.integralTopForm_mextDeriv)
- [Source of `TauCeti.integralTopForm_mextDeriv` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Stokes.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Stokes.lean#L35)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
