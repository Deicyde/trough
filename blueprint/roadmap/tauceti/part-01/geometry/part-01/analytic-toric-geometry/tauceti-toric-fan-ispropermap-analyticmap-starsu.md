---
declaration: theorem
origin: cited
lean: TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong
statement: formalized
proof: formalized
---

# TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong

The star subdivision of a regular fan `Φ` along a nonzero cone `σ` of `Φ` induces a proper
analytic map to the realization of `Φ`, because the two fans have the same support.

```lean
TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong.{u} {N V : Type u} [AddCommGroup N]
  [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} (Φ : TauCeti.Toric.Fan i) (hΦ : Φ.IsRegular)
  {σ : PointedCone ℝ V} (hσ : σ ∈ Φ.cones) (hσ0 : σ ≠ ⊥) :
  IsProperMap ⇑(CategoryTheory.ConcreteCategory.hom (⋯.toFanHom.analyticMap ⋯ hΦ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's lemma for lattice points](../scattering-diagrams-wall-crossing-and-theta-func/gordans-lemma-for-lattice-points.md)
- [Hoffman's error bound for a polyhedral cone](../../part-02/convex/hoffmans-error-bound-for-a-polyhedral-cone.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Map/Subdivision.html#TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Map/Subdivision.html#TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong)
- [Source of `TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong` in TauCeti/Geometry/Toric/Analytic/Fan/Map/Subdivision.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Analytic/Fan/Map/Subdivision.lean#L86)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AnalyticToricGeometry/STATUS.md)
