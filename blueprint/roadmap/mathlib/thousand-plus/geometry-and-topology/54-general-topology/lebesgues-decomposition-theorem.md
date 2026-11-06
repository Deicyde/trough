---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.haveLebesgueDecomposition_of_sigmaFinite
mathlib_file: Mathlib/MeasureTheory/Measure/Decomposition/Lebesgue.lean
---

# Lebesgue's decomposition theorem

**The Lebesgue decomposition theorem**:
Any s-finite measure `μ` has Lebesgue decomposition with respect to any σ-finite measure `ν`.
That is to say, there exist a measure `ξ` and a measurable function `f`,
such that `ξ` is mutually singular with respect to `ν` and `μ = ξ + ν.withDensity f`

```lean
MeasureTheory.Measure.haveLebesgueDecomposition_of_sigmaFinite.{u_1} {α : Type u_1}
  {m : MeasurableSpace α} (μ ν : MeasureTheory.Measure α) [MeasureTheory.SFinite μ]
  [MeasureTheory.SigmaFinite ν] : μ.HaveLebesgueDecomposition ν
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](../../analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Integral of positive measurable functions](../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Monotone convergence theorem (1000+ theorems)](../../analysis/26-real-functions/part-01/monotone-convergence-theorem.md)
- [Squeeze theorem](../../analysis/26-real-functions/part-02/squeeze-theorem.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Measure.haveLebesgueDecomposition_of_sigmaFinite`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Decomposition/Lebesgue.html#MeasureTheory.Measure.haveLebesgueDecomposition_of_sigmaFinite)
- [Source of `MeasureTheory.Measure.haveLebesgueDecomposition_of_sigmaFinite` in Mathlib/MeasureTheory/Measure/Decomposition/Lebesgue.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Decomposition/Lebesgue.lean#L946)
- [1000+ theorems list: Q191693](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L153)
- [1000+ theorems project: Q191693](https://1000-plus.github.io/all.html?length=-1#Q191693)
- [Wikipedia: Lebesgue's decomposition theorem](https://en.wikipedia.org/wiki/Lebesgue's_decomposition_theorem)
- [Wikidata: Q191693](https://www.wikidata.org/wiki/Q191693)
