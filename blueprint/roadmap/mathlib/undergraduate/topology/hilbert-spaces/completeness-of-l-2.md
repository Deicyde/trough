# Completeness of $l^2$

Mathlib states this as `lp.completeSpace`.

```lean
lp.completeSpace.{u_3, u_4} {α : Type u_3} {E : α → Type u_4} {p : ENNReal}
  [(i : α) → NormedAddCommGroup (E i)] [_i : Fact (1 ≤ p)] [∀ (a : α), CompleteSpace (E a)] :
  CompleteSpace ↥(lp E p)
```

## Depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Complete metric spaces](../topology-and-metric-spaces/complete-metric-spaces.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/field-r-of-real-numbers.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Pointwise convergence](../../single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `lp.completeSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Lp/lpSpace.html#lp.completeSpace)
- [Source of `lp.completeSpace` in Mathlib/Analysis/Normed/Lp/lpSpace.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Lp/lpSpace.lean#L1357)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L443)
