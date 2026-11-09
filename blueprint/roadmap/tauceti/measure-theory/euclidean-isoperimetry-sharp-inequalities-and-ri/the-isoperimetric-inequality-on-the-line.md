---
declaration: theorem
origin: cited
lean: TauCeti.Real.two_le_perimeter
statement: formalized
proof: formalized
---

# The isoperimetric inequality on the line

A null-measurable set of positive finite measure
in `ℝ` has perimeter at least two.

```lean
TauCeti.Real.two_le_perimeter {s : Set ℝ}
  (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume) (h0 : MeasureTheory.volume s ≠ 0)
  (hfin : MeasureTheory.volume s ≠ ⊤) : 2 ≤ TauCeti.perimeter MeasureTheory.volume ⊤ s
```

## Depends on

- [TauCeti.perimeter](../../analysis/part-01/geometric-measure-theory-rectifiability-bv-and-f/tauceti-perimeter.md)

## Proof depends on

- [Lebesgue's differentiation theorem](../other-results/lebesgues-differentiation-theorem.md)
- [TauCeti.totalVariationOn](../../analysis/part-01/geometric-measure-theory-rectifiability-bv-and-f/tauceti-totalvariationon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.two_le_perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Real.html#TauCeti.Real.two_le_perimeter).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.two_le_perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Real.html#TauCeti.Real.two_le_perimeter)
- [Source of `TauCeti.Real.two_le_perimeter` in TauCeti/Analysis/BoundedVariation/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/Real.lean#L309)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Isoperimetry/STATUS.md)
