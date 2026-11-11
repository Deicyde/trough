---
declaration: def
origin: cited
lean: TauCeti.CStarAction.FullCrossedProduct.groupMultiplier
statement: formalized
---

# TauCeti.CStarAction.FullCrossedProduct.groupMultiplier

The canonical group map `i_G` of `G` into the unitary multipliers of the full crossed
product. The multiplier `i_G(r)` acts on the left of the twisted convolution algebra by twisted
left translation, `(i_G(r) f)(s) = α r (f (r⁻¹ * s))`.

```lean
TauCeti.CStarAction.FullCrossedProduct.groupMultiplier.{u, v} {G : Type u} {A : Type v} [Group G]
  [TopologicalSpace G] [MeasurableSpace G] [NonUnitalCStarAlgebra A] (α : TauCeti.CStarAction G A)
  (μ : MeasureTheory.Measure G) [IsTopologicalGroup G] [LocallyCompactSpace G] [BorelSpace G]
  [μ.IsHaarMeasure] : G →* ↥(unitary (DoubleCentralizer ℂ (α.FullCrossedProduct μ)))
```

## Depends on

- [TauCeti.CStarAction.FullCrossedProduct](tauceti-cstaraction-fullcrossedproduct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.FullCrossedProduct.groupMultiplier`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Multiplier.html#TauCeti.CStarAction.FullCrossedProduct.groupMultiplier).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.FullCrossedProduct.groupMultiplier`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Multiplier.html#TauCeti.CStarAction.FullCrossedProduct.groupMultiplier)
- [Source of `TauCeti.CStarAction.FullCrossedProduct.groupMultiplier` in TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Multiplier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Multiplier.lean#L221)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
