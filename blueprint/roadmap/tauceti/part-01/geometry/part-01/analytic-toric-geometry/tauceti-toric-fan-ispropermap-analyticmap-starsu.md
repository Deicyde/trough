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

- [Gordan's lemma](../../part-02/other-results/gordans-lemma.md)
- [Hoffman's error bound for a polyhedral cone](../../part-02/convex/hoffmans-error-bound-for-a-polyhedral-cone.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Map/Subdivision.html#TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Map/Subdivision.html#TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong)
- [Source of `TauCeti.Toric.Fan.isProperMap_analyticMap_starSubdivisionAlong` in TauCeti/Geometry/Toric/Analytic/Fan/Map/Subdivision.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Toric/Analytic/Fan/Map/Subdivision.lean#L86)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AnalyticToricGeometry/STATUS.md)
