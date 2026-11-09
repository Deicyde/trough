# Radon–Nikodym theorem

**The Radon-Nikodym theorem**: Given two measures `μ` and `ν`, if
`HaveLebesgueDecomposition μ ν`, then `μ` is absolutely continuous to `ν` if and only if
`ν.withDensity (rnDeriv μ ν) = μ`.

```lean
MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq.{u_1} {α : Type u_1}
  {m : MeasurableSpace α} {μ ν : MeasureTheory.Measure α} [μ.HaveLebesgueDecomposition ν] :
  μ.AbsolutelyContinuous ν ↔ ν.withDensity (μ.rnDeriv ν) = μ
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](caratheodorys-theorem-measure-theory.md)
- [Integral of positive measurable functions](../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Decomposition/RadonNikodym.html#MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq)
- [Source of `MeasureTheory.Measure.absolutelyContinuous_iff_withDensity_rnDeriv_eq` in Mathlib/MeasureTheory/Measure/Decomposition/RadonNikodym.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Measure/Decomposition/RadonNikodym.lean#L66)
- [1000+ theorems list: Q1191319](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1506)
- [1000+ theorems project: Q1191319](https://1000-plus.github.io/all.html?length=-1#Q1191319)
- [Wikipedia: Radon–Nikodym theorem](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem)
- [Wikidata: Q1191319](https://www.wikidata.org/wiki/Q1191319)
