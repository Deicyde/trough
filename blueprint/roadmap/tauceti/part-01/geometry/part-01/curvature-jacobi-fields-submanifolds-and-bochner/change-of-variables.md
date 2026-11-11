---
declaration: theorem
origin: cited
lean: PartialDiffeomorph.setLIntegral_riemannianVolume_eq
statement: formalized
proof: formalized
---

# Change of variables

**Change of variables** over the target of a `C¹` partial diffeomorphism `Φ` from `F` to `M`:
the integral of a measurable `φ` over the target against the Riemannian volume is the integral of
`φ ∘ Φ` over the source, weighted by the Riemannian Jacobian, against the Haar measure of `b`.

```lean
PartialDiffeomorph.setLIntegral_riemannianVolume_eq.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {ι : Type u_5} [Fintype ι] [DecidableEq ι] [IsManifold I 1 M]
  [FiniteDimensional ℝ E] [IsContinuousRiemannianBundle E fun x => TangentSpace I x]
  [MeasurableSpace M] [BorelSpace M] [LindelofSpace M] [MeasurableSpace F] [BorelSpace F]
  (Φ : PartialDiffeomorph (modelWithCornersSelf ℝ F) I F M 1) (b : Module.Basis ι ℝ F)
  (hdim : Module.finrank ℝ F = Module.finrank ℝ E) {φ : M → ENNReal} (hφ : Measurable φ) :
  ∫⁻ (y : M) in Φ.target, φ y ∂TauCeti.riemannianVolume I M =
    ∫⁻ (x : F) in Φ.source,
      ENNReal.ofReal (TauCeti.riemannianJacobian b (↑Φ.toPartialEquiv) x) *
        φ (↑Φ.toPartialEquiv x) ∂b.addHaar
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PartialDiffeomorph.setLIntegral_riemannianVolume_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/ChangeOfVariables.html#PartialDiffeomorph.setLIntegral_riemannianVolume_eq).

## Sources

- [Tau Ceti documentation: `PartialDiffeomorph.setLIntegral_riemannianVolume_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/ChangeOfVariables.html#PartialDiffeomorph.setLIntegral_riemannianVolume_eq)
- [Source of `PartialDiffeomorph.setLIntegral_riemannianVolume_eq` in TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/ChangeOfVariables.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/VolumeDensity/ChangeOfVariables.lean#L378)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
