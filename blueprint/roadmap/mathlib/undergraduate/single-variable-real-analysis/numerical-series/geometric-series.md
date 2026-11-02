---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: tsum_geometric_of_norm_lt_one
mathlib_file: Mathlib/Analysis/SpecificLimits/Normed.lean
---

# Geometric series

Mathlib states this as `tsum_geometric_of_norm_lt_one`.

```lean
tsum_geometric_of_norm_lt_one.{u_4} {K : Type u_4} [NormedDivisionRing K] {ξ : K} (h : ‖ξ‖ < 1) :
  ∑' (n : ℕ), ξ ^ n = (1 - ξ)⁻¹
```

## Depends on

- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Completeness of R](../topology-of-r/completeness-of-r.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `tsum_geometric_of_norm_lt_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecificLimits/Normed.html#tsum_geometric_of_norm_lt_one)
- [Source of `tsum_geometric_of_norm_lt_one` in Mathlib/Analysis/SpecificLimits/Normed.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecificLimits/Normed.lean#L489)
- [Mathlib undergraduate list: Single Variable Real Analysis › Numerical series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L298)
