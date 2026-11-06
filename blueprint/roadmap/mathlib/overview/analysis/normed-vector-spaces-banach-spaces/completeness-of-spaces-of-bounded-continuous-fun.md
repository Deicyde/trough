---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: BoundedContinuousFunction.instCompleteSpace
mathlib_file: Mathlib/Topology/ContinuousMap/Bounded/Basic.lean
---

# Completeness of spaces of bounded continuous functions

Bounded continuous functions taking values in a complete space form a complete space.

```lean
BoundedContinuousFunction.instCompleteSpace.{u, v} {α : Type u} {β : Type v} [TopologicalSpace α]
  [PseudoMetricSpace β] [CompleteSpace β] : CompleteSpace (BoundedContinuousFunction α β)
```

## Depends on

- [Bornology](../topological-vector-spaces/bornology.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Complete metric spaces](../../../undergraduate/topology/topology-and-metric-spaces/complete-metric-spaces.md)
- [Limits of sequences](../../../undergraduate/topology/topology-and-metric-spaces/limits-of-sequences.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-02/squeeze-theorem.md)
- [Uniform convergence](../../topology/uniform-notions/uniform-convergence.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `BoundedContinuousFunction.instCompleteSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/ContinuousMap/Bounded/Basic.html#BoundedContinuousFunction.instCompleteSpace)
- [Source of `BoundedContinuousFunction.instCompleteSpace` in Mathlib/Topology/ContinuousMap/Bounded/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/ContinuousMap/Bounded/Basic.lean#L295)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L291)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L433)
