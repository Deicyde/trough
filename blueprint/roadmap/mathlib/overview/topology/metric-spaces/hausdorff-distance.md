# Hausdorff distance

The Hausdorff edistance between two sets is the smallest `r` such that each set
is contained in the `r`-neighborhood of the other one

```lean
Metric.hausdorffEDist.{u} {α : Type u} [PseudoEMetricSpace α] (s t : Set α) : ENNReal
```

## Depends on

- [Real number](../../general-algebra/numbers/real-number.md)

## Sources

- [Mathlib documentation: `Metric.hausdorffEDist`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/HausdorffDistance.html#Metric.hausdorffEDist)
- [Source of `Metric.hausdorffEDist` in Mathlib/Topology/MetricSpace/HausdorffDistance.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/MetricSpace/HausdorffDistance.lean#L257)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L269)
