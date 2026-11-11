---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.OrientationCover.exists_mextDerivₗ_eq_of_mextDerivₗ_eq_mpullback_proj
statement: formalized
proof: formalized
---

# Descent of primitives along the orientation cover

If the pullback of a smooth
`(k + 1)`-form `φ` on `M` to the orientation double cover is the exterior derivative of a smooth
form `η`, then `φ` is the exterior derivative of a smooth form `ψ` on `M`, whose pullback to the
cover is the deck-invariant part `(η + τ^*η) / 2` of `η`.

```lean
TauCeti.Manifold.OrientationCover.exists_mextDerivₗ_eq_of_mextDerivₗ_eq_mpullback_proj.{u_1, u_2,
    u_3, u_4}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] {k : ℕ} [NormedAddCommGroup F] [NormedSpace ℝ F]
  [IsManifold I (↑⊤) M] {φ : TauCeti.SmoothForm I M F (k + 1)}
  {η : TauCeti.SmoothForm I (TauCeti.Manifold.OrientationCover I M) F k}
  (hη :
    (TauCeti.mextDerivₗ I k) η =
      (TauCeti.SmoothForm.mpullback TauCeti.VectorBundleOrientationCover.proj ⋯) φ) :
  ∃ ψ,
    (TauCeti.mextDerivₗ I k) ψ = φ ∧
      TauCeti.mpullback I I TauCeti.VectorBundleOrientationCover.proj ↑ψ =
        TauCeti.invariantPart ⇑TauCeti.VectorBundleOrientationCover.deck ↑η
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.OrientationCover.exists_mextDerivₗ_eq_of_mextDerivₗ_eq_mpullback_proj`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Orientation/Cover/Descent.html#TauCeti.Manifold.OrientationCover.exists_mextDeriv%E2%82%97_eq_of_mextDeriv%E2%82%97_eq_mpullback_proj).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.OrientationCover.exists_mextDerivₗ_eq_of_mextDerivₗ_eq_mpullback_proj`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Orientation/Cover/Descent.html#TauCeti.Manifold.OrientationCover.exists_mextDeriv%E2%82%97_eq_of_mextDeriv%E2%82%97_eq_mpullback_proj)
- [Source of `TauCeti.Manifold.OrientationCover.exists_mextDerivₗ_eq_of_mextDerivₗ_eq_mpullback_proj` in TauCeti/Geometry/Manifold/Orientation/Cover/Descent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Orientation/Cover/Descent.lean#L117)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
