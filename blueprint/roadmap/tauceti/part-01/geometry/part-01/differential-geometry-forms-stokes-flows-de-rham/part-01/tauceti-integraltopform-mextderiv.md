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

## Proof depends on

- [The Jordan–Brouwer separation theorem](../../../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integralTopForm_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Stokes.html#TauCeti.integralTopForm_mextDeriv).

## Sources

- [Tau Ceti documentation: `TauCeti.integralTopForm_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Stokes.html#TauCeti.integralTopForm_mextDeriv)
- [Source of `TauCeti.integralTopForm_mextDeriv` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Stokes.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Stokes.lean#L35)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
