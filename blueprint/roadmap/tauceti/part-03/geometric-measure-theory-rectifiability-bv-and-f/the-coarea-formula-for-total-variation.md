---
declaration: theorem
origin: cited
lean: TauCeti.totalVariationOn_eq_lintegral_perimeter
statement: formalized
proof: formalized
---

# The coarea formula for total variation

For `u` locally integrable on `Ω`, against an
additive Haar measure, the total variation of `u` is the integral of the perimeters of its
superlevel sets: `|Du|(Ω) = ∫_ℝ P({u > t}; Ω) dt`, finite or infinite.

```lean
TauCeti.totalVariationOn_eq_lintegral_perimeter.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {Ω : TopologicalSpace.Opens E} {u : E → ℝ}
  (hu : MeasureTheory.LocallyIntegrableOn u (↑Ω) μ) :
  TauCeti.totalVariationOn μ Ω u = ∫⁻ (t : ℝ), TauCeti.perimeter μ Ω {x | t < u x}
```

## Depends on

- [TauCeti.perimeter](tauceti-perimeter.md)
- [TauCeti.totalVariationOn](tauceti-totalvariationon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.totalVariationOn_eq_lintegral_perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Coarea.html#TauCeti.totalVariationOn_eq_lintegral_perimeter).

## Sources

- [Tau Ceti documentation: `TauCeti.totalVariationOn_eq_lintegral_perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Coarea.html#TauCeti.totalVariationOn_eq_lintegral_perimeter)
- [Source of `TauCeti.totalVariationOn_eq_lintegral_perimeter` in TauCeti/Analysis/BoundedVariation/Coarea.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/Coarea.lean#L389)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
