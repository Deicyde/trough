---
declaration: def
origin: cited
lean: TauCeti.variationMeasure
statement: formalized
---

# TauCeti.variationMeasure

The **variation measure** `|Du|` of `u` on the open set `Ω`: if `u` is locally integrable on
`Ω` and has locally finite variation there, meaning that every compact `K ⊆ Ω` has an open
neighbourhood `U` with `totalVariationOn μ U u < ∞`, it is the regular measure on `Ω` whose value
on every open `U ⊆ Ω` is the total variation of `u` on `U`
(`TauCeti.variationMeasure_preimage_coe`). Otherwise it is `0` by convention.

```lean
TauCeti.variationMeasure.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E)
  (Ω : TopologicalSpace.Opens E) (u : E → ℝ) : MeasureTheory.Measure ↥Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.variationMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/VariationMeasure.html#TauCeti.variationMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.variationMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/VariationMeasure.html#TauCeti.variationMeasure)
- [Source of `TauCeti.variationMeasure` in TauCeti/Analysis/BoundedVariation/VariationMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/VariationMeasure.lean#L131)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
