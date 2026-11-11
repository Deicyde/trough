---
declaration: theorem
origin: cited
lean: TauCeti.BV.instCompleteSpace
statement: formalized
proof: formalized
---

# TauCeti.BV.instCompleteSpace

The BV norm is complete: every Cauchy sequence for the sum of the `L¹` norm and total
variation converges in that norm.

```lean
TauCeti.BV.instCompleteSpace.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] {μ : MeasureTheory.Measure E}
  {Ω : TopologicalSpace.Opens E} [OpensMeasurableSpace E] : CompleteSpace (TauCeti.BV μ Ω)
```

## Depends on

- [TauCeti.BV](tauceti-bv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BV.instCompleteSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Space.html#TauCeti.BV.instCompleteSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.BV.instCompleteSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Space.html#TauCeti.BV.instCompleteSpace)
- [Source of `TauCeti.BV.instCompleteSpace` in TauCeti/Analysis/BoundedVariation/Space.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/Space.lean#L317)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
