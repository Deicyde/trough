---
declaration: def
origin: cited
lean: TauCeti.totalVariationOn
statement: formalized
---

# TauCeti.totalVariationOn

The **total variation** of `u : E → ℝ` on the open set `Ω`, relative to the measure `μ`:
the extended supremum of `∫ div φ * u ∂μ` over test vector fields `φ ∈ 𝓓(Ω, E)` with
`‖φ x‖ ≤ 1` everywhere. For `μ` an additive Haar measure this is the variation `|Du|(Ω)` of the
distributional derivative of `u` on `Ω`, defined by duality.

```lean
TauCeti.totalVariationOn.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] (μ : MeasureTheory.Measure E)
  (Ω : TopologicalSpace.Opens E) (u : E → ℝ) : ENNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/TotalVariation.html#TauCeti.totalVariationOn).

## Sources

- [Tau Ceti documentation: `TauCeti.totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/TotalVariation.html#TauCeti.totalVariationOn)
- [Source of `TauCeti.totalVariationOn` in TauCeti/Analysis/BoundedVariation/TotalVariation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/TotalVariation.lean#L98)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
