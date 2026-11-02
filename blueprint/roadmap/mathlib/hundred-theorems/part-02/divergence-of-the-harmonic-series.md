---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Real.tendsto_sum_range_one_div_nat_succ_atTop
mathlib_file: Mathlib/Analysis/PSeries.lean
---

# Divergence of the Harmonic Series

**Divergence of the Harmonic Series**

```lean
Real.tendsto_sum_range_one_div_nat_succ_atTop :
  Filter.Tendsto (fun n => ∑ i ∈ Finset.range n, 1 / (↑i + 1)) Filter.atTop Filter.atTop
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Limit of a map with respect to filters](../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Real number](../../overview/general-algebra/numbers/real-number.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Continuous function](../../overview/topology/general-topology/part-01/continuous-function.md)
- [Induced topology](../../overview/topology/general-topology/part-01/induced-topology.md)
- [Infinite sum](../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Module](../../overview/linear-algebra/fundamentals/module.md)
- [Order topology](../../overview/topology/topological-algebra/order-topology.md)
- [Power functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)

## Sources

- [Mathlib documentation: `Real.tendsto_sum_range_one_div_nat_succ_atTop`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/PSeries.html#Real.tendsto_sum_range_one_div_nat_succ_atTop)
- [Source of `Real.tendsto_sum_range_one_div_nat_succ_atTop` in Mathlib/Analysis/PSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/PSeries.lean#L360)
- [Freek Wiedijk's 100 theorems, no. 34](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L179)
