---
declaration: def
origin: cited
lean: TauCeti.CStarAction.regularAlgebra
statement: formalized
---

# TauCeti.CStarAction.regularAlgebra

The concrete regular crossed-product algebra associated to `ρ`: the norm closure of the
integrated regular representation of compactly supported coefficients on `L²(G, H)`.

```lean
TauCeti.CStarAction.regularAlgebra.{u, v, w} {G : Type u} {A : Type v} {H : Type w} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G] [MeasurableSpace G]
  [BorelSpace G] [NonUnitalCStarAlgebra A] [NormedAddCommGroup H] [InnerProductSpace ℂ H]
  [CompleteSpace H] (α : TauCeti.CStarAction G A) (ρ : A →⋆ₙₐ[ℂ] H →L[ℂ] H)
  (μ : MeasureTheory.Measure G) [μ.IsHaarMeasure] [μ.InnerRegularCompactLTTop] :
  NonUnitalStarSubalgebra ℂ (↥(MeasureTheory.Lp H 2 μ) →L[ℂ] ↥(MeasureTheory.Lp H 2 μ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.regularAlgebra`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Regular.html#TauCeti.CStarAction.regularAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.regularAlgebra`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Regular.html#TauCeti.CStarAction.regularAlgebra)
- [Source of `TauCeti.CStarAction.regularAlgebra` in TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Regular.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Regular.lean#L54)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
