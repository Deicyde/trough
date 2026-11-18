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
- [Source of `TauCeti.reducedBoundary` in TauCeti/Analysis/BoundedVariation/ReducedBoundary.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/BoundedVariation/ReducedBoundary.lean#L96)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
