---
declaration: def
origin: cited
lean: TauCeti.perimeter
statement: formalized
---

# TauCeti.perimeter

The **perimeter** of a set `s` in the open set `Ω`, relative to the measure `μ`: the total
variation of the indicator of `s` on `Ω`. For a null-measurable `s` it is the extended supremum
of `∫_s div φ ∂μ` over test vector fields `φ ∈ 𝓓(Ω, E)` with `‖φ x‖ ≤ 1` everywhere
(`TauCeti.perimeter_eq_iSup`).

```lean
TauCeti.perimeter.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] (μ : MeasureTheory.Measure E)
  (Ω : TopologicalSpace.Opens E) (s : Set E) : ENNReal
```

## Depends on

- [TauCeti.totalVariationOn](tauceti-totalvariationon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Perimeter.html#TauCeti.perimeter).

## Sources

- [Tau Ceti documentation: `TauCeti.perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Perimeter.html#TauCeti.perimeter)
- [Source of `TauCeti.perimeter` in TauCeti/Analysis/BoundedVariation/Perimeter.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/Perimeter.lean#L60)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
