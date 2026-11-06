# Sum of a Geometric Series

Mathlib records this with 2 declarations.

`geom_sum_Ico`.

```lean
geom_sum_Ico.{u_1} {K : Type u_1} [DivisionRing K] {x : K} (hx : x ≠ 1) {m n : ℕ} (hmn : m ≤ n) :
  ∑ i ∈ Finset.Ico m n, x ^ i = (x ^ n - x ^ m) / (x - 1)
```

`NNReal.hasSum_geometric`: **Sum of a Geometric Series**

```lean
NNReal.hasSum_geometric {r : NNReal} (hr : r < 1) : HasSum (fun n => r ^ n) (1 - r)⁻¹
```

## Depends on

- [Infinite sum](../../overview/topology/topological-algebra/infinite-sum.md)
- [Real number](../../overview/general-algebra/numbers/real-number.md)

## Proof depends on

- [Bornology](../../overview/analysis/topological-vector-spaces/bornology.md)
- [Closure](../../overview/topology/general-topology/part-01/closure.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Order](../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Order topology](../../overview/topology/topological-algebra/order-topology.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `geom_sum_Ico`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/GeomSum.html#geom_sum_Ico)
- [Source of `geom_sum_Ico` in Mathlib/Algebra/Field/GeomSum.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Field/GeomSum.lean#L52)
- [Mathlib documentation: `NNReal.hasSum_geometric`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecificLimits/Basic.html#NNReal.hasSum_geometric)
- [Source of `NNReal.hasSum_geometric` in Mathlib/Analysis/SpecificLimits/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecificLimits/Basic.lean#L384)
- [Freek Wiedijk's 100 theorems, no. 66](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L331)
