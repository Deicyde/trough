---
declaration: def
origin: cited
lean: TauCeti.CStarAction.FullCrossedProduct.coefficientMultiplier
statement: formalized
---

# TauCeti.CStarAction.FullCrossedProduct.coefficientMultiplier

The canonical coefficient map `i_A` of `A` into the multiplier algebra of the full crossed
product. The multiplier `i_A(a)` acts on the left of the twisted convolution algebra by
`(i_A(a) f)(s) = a * f(s)`.

```lean
TauCeti.CStarAction.FullCrossedProduct.coefficientMultiplier.{u, v} {G : Type u} {A : Type v}
  [Group G] [TopologicalSpace G] [MeasurableSpace G] [NonUnitalCStarAlgebra A]
  (α : TauCeti.CStarAction G A) (μ : MeasureTheory.Measure G) [IsTopologicalGroup G]
  [LocallyCompactSpace G] [BorelSpace G] [μ.IsHaarMeasure] :
  A →⋆ₙₐ[ℂ] DoubleCentralizer ℂ (α.FullCrossedProduct μ)
```

## Depends on

- [TauCeti.CStarAction.FullCrossedProduct](tauceti-cstaraction-fullcrossedproduct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.FullCrossedProduct.coefficientMultiplier`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Multiplier.html#TauCeti.CStarAction.FullCrossedProduct.coefficientMultiplier).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.FullCrossedProduct.coefficientMultiplier`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Multiplier.html#TauCeti.CStarAction.FullCrossedProduct.coefficientMultiplier)
- [Source of `TauCeti.CStarAction.FullCrossedProduct.coefficientMultiplier` in TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Multiplier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Multiplier.lean#L141)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
