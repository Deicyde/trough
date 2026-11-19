---
declaration: def
origin: cited
lean: TauCeti.Toric.Fan.analyticConeOrbitTorusDiffeomorph
statement: formalized
---

# TauCeti.Toric.Fan.analyticConeOrbitTorusDiffeomorph

The canonical identification of a cone orbit with its quotient torus is biholomorphic.

```lean
TauCeti.Toric.Fan.analyticConeOrbitTorusDiffeomorph.{u, u_1} {N V : Type u} [AddCommGroup N]
  [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} (Φ : TauCeti.Toric.Fan i) (hΦ : Φ.IsRegular)
  (σ : ↑Φ.cones) {ι : Type u_1} [Fintype ι]
  (e : TauCeti.Toric.IntegralCharacter (N ⧸ TauCeti.Toric.coneSublattice i ↑σ) ≃+ (ι →₀ ℤ))
  (n : WithTop ℕ∞) :
  have this := Φ.analyticConeOrbitChartedSpace hΦ σ e;
  have this_1 := TauCeti.Toric.complexTorusChartedSpace e;
  Diffeomorph (modelWithCornersSelf ℂ (ι → ℂ)) (modelWithCornersSelf ℂ (ι → ℂ))
    (↑(Φ.analyticConeOrbit hΦ σ))
    (TauCeti.Toric.ComplexTorus (N ⧸ TauCeti.Toric.coneSublattice i ↑σ)) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's lemma for lattice points](../scattering-diagrams-wall-crossing-and-theta-func/gordans-lemma-for-lattice-points.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.analyticConeOrbitTorusDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Orbit/Complex.html#TauCeti.Toric.Fan.analyticConeOrbitTorusDiffeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.analyticConeOrbitTorusDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Orbit/Complex.html#TauCeti.Toric.Fan.analyticConeOrbitTorusDiffeomorph)
- [Source of `TauCeti.Toric.Fan.analyticConeOrbitTorusDiffeomorph` in TauCeti/Geometry/Toric/Analytic/Fan/Orbit/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Analytic/Fan/Orbit/Complex.lean#L65)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AnalyticToricGeometry/STATUS.md)
