# Divergence of the Harmonic Series

**Divergence of the Harmonic Series**

```lean
Real.tendsto_sum_range_one_div_nat_succ_atTop :
  Filter.Tendsto (fun n => ∑ i ∈ Finset.range n, 1 / (↑i + 1)) Filter.atTop Filter.atTop
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Real number](../../overview/general-algebra/numbers/real-number.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Continuous function](../../overview/topology/general-topology/part-01/continuous-function.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Infinite sum](../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric space](../../overview/topology/metric-spaces/metric-space.md)
- [Module](../../overview/linear-algebra/fundamentals/module.md)
- [Order topology](../../overview/topology/topological-algebra/order-topology.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Real.tendsto_sum_range_one_div_nat_succ_atTop`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/PSeries.html#Real.tendsto_sum_range_one_div_nat_succ_atTop)
- [Source of `Real.tendsto_sum_range_one_div_nat_succ_atTop` in Mathlib/Analysis/PSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/PSeries.lean#L360)
- [Freek Wiedijk's 100 theorems, no. 34](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L179)
