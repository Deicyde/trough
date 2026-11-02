---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Lp.instCompleteSpace
mathlib_file: Mathlib/MeasureTheory/Function/LpSpace/Complete.lean
---

# Completeness of $L^2$

`Lp` is complete for `1 ≤ p`.

```lean
MeasureTheory.Lp.instCompleteSpace.{u_1, u_3} {α : Type u_1} {m : MeasurableSpace α} {p : ENNReal}
  {μ : MeasureTheory.Measure α} {E : Type u_3} [NormedAddCommGroup E] [CompleteSpace E]
  [hp : Fact (1 ≤ p)] : CompleteSpace ↥(MeasureTheory.Lp E p μ)
```

## Depends on

- [$L^p$ space](../../../overview/analysis/measures-and-integral-calculus/part-01/l-p-space.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)

## Proof depends on

- [Approximation by step functions](../../measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../overview/topology/general-topology/part-01/closed-map.md)
- [Continuity of monotone functions](../../single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Pointwise convergence](../../single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Lp.instCompleteSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/LpSpace/Complete.html#MeasureTheory.Lp.instCompleteSpace)
- [Source of `MeasureTheory.Lp.instCompleteSpace` in Mathlib/MeasureTheory/Function/LpSpace/Complete.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/LpSpace/Complete.lean#L386)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L445)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L522)
