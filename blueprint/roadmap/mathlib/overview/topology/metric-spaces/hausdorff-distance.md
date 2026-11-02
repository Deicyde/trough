---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Metric.hausdorffEDist
mathlib_file: Mathlib/Topology/MetricSpace/HausdorffDistance.lean
---

# Hausdorff distance

The Hausdorff edistance between two sets is the smallest `r` such that each set
is contained in the `r`-neighborhood of the other one

```lean
Metric.hausdorffEDist.{u} {α : Type u} [PseudoEMetricSpace α] (s t : Set α) : ENNReal
```

## Depends on

- [Real number](../../general-algebra/numbers/real-number.md)
- [Uniform space](../uniform-notions/uniform-space.md)

## Sources

- [Mathlib documentation: `Metric.hausdorffEDist`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/HausdorffDistance.html#Metric.hausdorffEDist)
- [Source of `Metric.hausdorffEDist` in Mathlib/Topology/MetricSpace/HausdorffDistance.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/HausdorffDistance.lean#L257)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L269)
