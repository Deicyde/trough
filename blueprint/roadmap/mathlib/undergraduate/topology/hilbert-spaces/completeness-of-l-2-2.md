# Completeness of $L^2$

`Lp` is complete for `1 ≤ p`.

```lean
MeasureTheory.Lp.instCompleteSpace.{u_1, u_3} {α : Type u_1} {m : MeasurableSpace α} {p : ENNReal}
  {μ : MeasureTheory.Measure α} {E : Type u_3} [NormedAddCommGroup E] [CompleteSpace E]
  [hp : Fact (1 ≤ p)] : CompleteSpace ↥(MeasureTheory.Lp E p μ)
```

## Depends on

- [$L^p$ space](../../../overview/analysis/measures-and-integral-calculus/part-01/l-p-space.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)

## Proof depends on

- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Pointwise convergence](../../single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Lp.instCompleteSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/LpSpace/Complete.html#MeasureTheory.Lp.instCompleteSpace)
- [Source of `MeasureTheory.Lp.instCompleteSpace` in Mathlib/MeasureTheory/Function/LpSpace/Complete.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/LpSpace/Complete.lean#L386)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L445)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L522)
