---
declaration: theorem
origin: cited
lean: TauCeti.exists_hasWeakFDerivOn_iff
statement: formalized
proof: formalized
---

# Weak differentiability through the derivative measure

Against an additive Haar measure,
`u` has a weak derivative on `Ω` exactly when it is locally integrable on `Ω` with locally finite
variation there and its variation measure `|Du|` is absolutely continuous with respect to `μ` on
`Ω`.

```lean
TauCeti.exists_hasWeakFDerivOn_iff.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} {Ω : TopologicalSpace.Opens E} {u : E → ℝ} [μ.IsAddHaarMeasure] :
  (∃ U, TauCeti.HasWeakFDerivOn μ Ω u U) ↔
    MeasureTheory.LocallyIntegrableOn u (↑Ω) μ ∧
      (∀ (K : Set E), IsCompact K → K ⊆ ↑Ω → ∃ U, K ⊆ ↑U ∧ TauCeti.totalVariationOn μ U u ≠ ⊤) ∧
        (TauCeti.variationMeasure μ Ω u).AbsolutelyContinuous
          (MeasureTheory.Measure.comap Subtype.val μ)
```

## Depends on

- [TauCeti.variationMeasure](tauceti-variationmeasure.md)

## Proof depends on

- [The polar decomposition `Du = σ_u |Du|`](the-polar-decomposition-du-u-du.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_hasWeakFDerivOn_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/WeakDerivative.html#TauCeti.exists_hasWeakFDerivOn_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_hasWeakFDerivOn_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/WeakDerivative.html#TauCeti.exists_hasWeakFDerivOn_iff)
- [Source of `TauCeti.exists_hasWeakFDerivOn_iff` in TauCeti/Analysis/BoundedVariation/WeakDerivative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/WeakDerivative.lean#L210)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
