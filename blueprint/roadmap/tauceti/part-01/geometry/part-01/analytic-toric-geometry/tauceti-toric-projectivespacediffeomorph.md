---
declaration: def
origin: cited
lean: TauCeti.Toric.projectiveSpaceDiffeomorph
statement: formalized
---

# TauCeti.Toric.projectiveSpaceDiffeomorph

Homogeneous coordinates identify the analytic realization of the standard projective-space
fan biholomorphically with complex projective space, the circle quotient of the unit sphere with
its standard homogeneous-ratio atlas.

```lean
TauCeti.Toric.projectiveSpaceDiffeomorph.{u} {N V : Type u} [AddCommGroup N] [AddCommGroup V]
  [_root_.Module ℝ V] {n : ℕ} (b : Module.Basis (Fin n) ℤ N) {i : N →+ V}
  (hi : TauCeti.Toric.IsIntegralLattice i) (r : WithTop ℕ∞) :
  have x := (TauCeti.Toric.Fan.projectiveSpace b hi).analyticChartedSpace ⋯;
  Diffeomorph (modelWithCornersSelf ℂ (Fin (Module.finrank ℤ N) → ℂ))
    (modelWithCornersSelf ℂ (Fin n → ℂ))
    (↑((TauCeti.Toric.Fan.projectiveSpace b hi).analyticRealization ⋯))
    (TauCeti.ComplexProjectiveSpace n) r
```

## Depends on

- [TauCeti.Toric.Fan.projectiveSpace](tauceti-toric-fan-projectivespace.md)

## Proof depends on

- [Gordan's lemma](../../part-02/other-results/gordans-lemma.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.projectiveSpaceDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/ProjectiveSpace/Manifold.html#TauCeti.Toric.projectiveSpaceDiffeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.projectiveSpaceDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/ProjectiveSpace/Manifold.html#TauCeti.Toric.projectiveSpaceDiffeomorph)
- [Source of `TauCeti.Toric.projectiveSpaceDiffeomorph` in TauCeti/Geometry/Toric/Analytic/Fan/ProjectiveSpace/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Toric/Analytic/Fan/ProjectiveSpace/Manifold.lean#L140)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AnalyticToricGeometry/STATUS.md)
