---
declaration: def
origin: cited
lean: TauCeti.Toric.Fan.analyticTorusPartialDiffeomorph
statement: formalized
---

# TauCeti.Toric.Fan.analyticTorusPartialDiffeomorph

The canonical torus inclusion into the realization of a nonempty regular fan is a
biholomorphism from the complex torus onto the analytic dense torus, an open subset of the
realization.

```lean
TauCeti.Toric.Fan.analyticTorusPartialDiffeomorph.{u, u_1} {N V : Type u} {ι : Type u_1}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] [Fintype ι] {i : N →+ V}
  (Φ : TauCeti.Toric.Fan i) (hΦ : Φ.IsRegular) (hΦ0 : Nonempty ↑Φ.cones)
  (e : TauCeti.Toric.IntegralCharacter N ≃+ (ι →₀ ℤ)) (n : WithTop ℕ∞) :
  have x := TauCeti.Toric.complexTorusChartedSpace e;
  PartialDiffeomorph (modelWithCornersSelf ℂ (ι → ℂ))
    (modelWithCornersSelf ℂ (Fin (Module.finrank ℤ N) → ℂ)) (TauCeti.Toric.ComplexTorus N)
    (↑(Φ.analyticRealization hΦ)) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's lemma for lattice points](../scattering-diagrams-wall-crossing-and-theta-func/gordans-lemma-for-lattice-points.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.analyticTorusPartialDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/ZeroCone.html#TauCeti.Toric.Fan.analyticTorusPartialDiffeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.analyticTorusPartialDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/ZeroCone.html#TauCeti.Toric.Fan.analyticTorusPartialDiffeomorph)
- [Source of `TauCeti.Toric.Fan.analyticTorusPartialDiffeomorph` in TauCeti/Geometry/Toric/Analytic/Fan/ZeroCone.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Analytic/Fan/ZeroCone.lean#L189)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AnalyticToricGeometry/STATUS.md)
