---
declaration: theorem
origin: cited
lean: TauCeti.measure_rpow_le_perimeter
statement: formalized
proof: formalized
---

# The nonsharp isoperimetric inequality

Let `E` have dimension `n ≥ 2` and let
`p = n / (n - 1)`. Every null-measurable set `s` of finite measure satisfies
`μ(s) ^ (1/p) ≤ C P(s; E)`, where `1/p = 1 - 1/n`, `P(s; E)` is the perimeter of `s` in the whole
space, finite or infinite, and `C` is the constant `MeasureTheory.eLpNormLESNormFDerivOneConst μ p`
of the Gagliardo–Nirenberg–Sobolev inequality.

```lean
TauCeti.measure_rpow_le_perimeter.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {p : NNReal} {s : Set E}
  (hs : MeasureTheory.NullMeasurableSet s μ) (hμs : μ s ≠ ⊤)
  (hp : (↑(Module.finrank ℝ E)).HolderConjugate p) :
  μ s ^ (↑p)⁻¹ ≤ ↑(MeasureTheory.eLpNormLESNormFDerivOneConst μ ↑p) * TauCeti.perimeter μ ⊤ s
```

## Depends on

- [TauCeti.perimeter](tauceti-perimeter.md)

## Proof depends on

- [The Sobolev inequality for functions of bounded variation](the-sobolev-inequality-for-functions-of-bounded.md)
- [TauCeti.totalVariationOn](tauceti-totalvariationon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.measure_rpow_le_perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.html#TauCeti.measure_rpow_le_perimeter).

## Sources

- [Tau Ceti documentation: `TauCeti.measure_rpow_le_perimeter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.html#TauCeti.measure_rpow_le_perimeter)
- [Source of `TauCeti.measure_rpow_le_perimeter` in TauCeti/Analysis/BoundedVariation/Sobolev/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.lean#L108)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
