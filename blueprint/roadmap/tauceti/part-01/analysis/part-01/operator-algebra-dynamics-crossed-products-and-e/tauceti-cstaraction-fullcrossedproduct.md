---
declaration: def
origin: cited
lean: TauCeti.CStarAction.FullCrossedProduct
statement: formalized
---

# TauCeti.CStarAction.FullCrossedProduct

The full crossed product `A ⋊_α G` of the C⋆-dynamical system `(A, G, α)`: the completion of
the twisted convolution algebra in the full C⋆-seminorm. It is a nonunital C⋆-algebra, and
the canonical map `FullCrossedProduct.of` from the twisted convolution algebra has dense range.

```lean
TauCeti.CStarAction.FullCrossedProduct.{u, v} {G : Type u} {A : Type v} [Group G]
  [TopologicalSpace G] [MeasurableSpace G] [NonUnitalCStarAlgebra A] (α : TauCeti.CStarAction G A)
  (μ : MeasureTheory.Measure G) [IsTopologicalGroup G] [LocallyCompactSpace G] [BorelSpace G]
  [μ.IsHaarMeasure] : Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.FullCrossedProduct`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Full.html#TauCeti.CStarAction.FullCrossedProduct).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.FullCrossedProduct`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Full.html#TauCeti.CStarAction.FullCrossedProduct)
- [Source of `TauCeti.CStarAction.FullCrossedProduct` in TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Full.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Full.lean#L263)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
