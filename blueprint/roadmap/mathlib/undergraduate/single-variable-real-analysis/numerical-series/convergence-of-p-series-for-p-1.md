---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Real.summable_one_div_nat_rpow
mathlib_file: Mathlib/Analysis/PSeries.lean
---

# Convergence of $p$-series for $p>1$

Test for convergence of the `p`-series: the real-valued series `∑' n : ℕ, 1 / n ^ p` converges
if and only if `1 < p`.

```lean
Real.summable_one_div_nat_rpow {p : ℝ} : (Summable fun n => 1 / ↑n ^ p) ↔ 1 < p
```

## Depends on

- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Order](../real-numbers/order.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/field-r-of-real-numbers.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Module](../../../overview/linear-algebra/fundamentals/module.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Real.summable_one_div_nat_rpow`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/PSeries.html#Real.summable_one_div_nat_rpow)
- [Source of `Real.summable_one_div_nat_rpow` in Mathlib/Analysis/PSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/PSeries.lean#L315)
- [Mathlib undergraduate list: Single Variable Real Analysis › Numerical series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L299)
