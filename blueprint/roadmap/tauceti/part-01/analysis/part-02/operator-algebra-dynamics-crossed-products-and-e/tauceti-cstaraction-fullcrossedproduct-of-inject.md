---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.FullCrossedProduct.of_injective
statement: formalized
proof: formalized
---

# TauCeti.CStarAction.FullCrossedProduct.of_injective

If `A` has a faithful representation on a Hilbert space `H` and `μ` is inner regular for compact
sets on sets of finite measure, the canonical map from the twisted convolution algebra into the full
crossed product is injective.

```lean
TauCeti.CStarAction.FullCrossedProduct.of_injective.{u, v, w} {G : Type u} {A : Type v} [Group G]
  [TopologicalSpace G] [MeasurableSpace G] [NonUnitalCStarAlgebra A] {α : TauCeti.CStarAction G A}
  {μ : MeasureTheory.Measure G} [IsTopologicalGroup G] [LocallyCompactSpace G] [BorelSpace G]
  [μ.IsHaarMeasure] [μ.InnerRegularCompactLTTop] {H : Type w} [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] {ρ : A →⋆ₙₐ[ℂ] H →L[ℂ] H} (hρ : Function.Injective ⇑ρ) :
  Function.Injective ⇑(TauCeti.CStarAction.FullCrossedProduct.of α μ)
```

## Depends on

- [TauCeti.CStarAction.FullCrossedProduct](tauceti-cstaraction-fullcrossedproduct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.FullCrossedProduct.of_injective`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Full.html#TauCeti.CStarAction.FullCrossedProduct.of_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.FullCrossedProduct.of_injective`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Full.html#TauCeti.CStarAction.FullCrossedProduct.of_injective)
- [Source of `TauCeti.CStarAction.FullCrossedProduct.of_injective` in TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Full.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Full.lean#L342)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
