---
declaration: def
origin: cited
lean: TauCeti.CStarAction.RegularCrossedProduct.fourierCoeff
statement: formalized
---

# TauCeti.CStarAction.RegularCrossedProduct.fourierCoeff

The Fourier coefficient at `g`, extending `f ↦ f g` continuously from compactly supported
coefficients to the concrete regular crossed product.

```lean
TauCeti.CStarAction.RegularCrossedProduct.fourierCoeff.{u_1, u_2, u_3} {G : Type u_1} {A : Type u_2}
  {H : Type u_3} [Group G] [TopologicalSpace G] [DiscreteTopology G] [MeasurableSpace G]
  [BorelSpace G] [NonUnitalCStarAlgebra A] [NormedAddCommGroup H] [InnerProductSpace ℂ H]
  [CompleteSpace H] (α : TauCeti.CStarAction G A) (ρ : A →⋆ₙₐ[ℂ] H →L[ℂ] H)
  (_hρ : Function.Injective ⇑ρ) (g : G) : ↥(α.regularAlgebra ρ MeasureTheory.Measure.count) →L[ℂ] A
```

## Depends on

- [TauCeti.CStarAction.regularAlgebra](tauceti-cstaraction-regularalgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.RegularCrossedProduct.fourierCoeff`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Fourier.html#TauCeti.CStarAction.RegularCrossedProduct.fourierCoeff).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.RegularCrossedProduct.fourierCoeff`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Fourier.html#TauCeti.CStarAction.RegularCrossedProduct.fourierCoeff)
- [Source of `TauCeti.CStarAction.RegularCrossedProduct.fourierCoeff` in TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Fourier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/CrossedProduct/Fourier.lean#L56)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
