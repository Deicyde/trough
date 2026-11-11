---
declaration: def
origin: cited
lean: TauCeti.reducedBoundary
statement: formalized
---

# TauCeti.reducedBoundary

The **reduced boundary** `∂*s` of `s` in the open set `Ω`: the points `x ∈ Ω` at which the
averages of the polar density `σ` of `Dχ_s` over `closedBall x r`, against the perimeter measure
`|Dχ_s|`, converge to a unit vector as `r → 0⁺`. When `|Dχ_s| (closedBall x r)` is positive and
finite, these averages are the ratios `Dχ_s (closedBall x r) / |Dχ_s| (closedBall x r)`.

```lean
TauCeti.reducedBoundary.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E)
  (Ω : TopologicalSpace.Opens E) (s : Set E) : Set E
```

## Depends on

- [TauCeti.variationMeasure](tauceti-variationmeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.reducedBoundary`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/ReducedBoundary.html#TauCeti.reducedBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.reducedBoundary`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/ReducedBoundary.html#TauCeti.reducedBoundary)
- [Source of `TauCeti.reducedBoundary` in TauCeti/Analysis/BoundedVariation/ReducedBoundary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/ReducedBoundary.lean#L92)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
