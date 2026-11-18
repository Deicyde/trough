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
- [Source of `Metric.hausdorffEDist` in Mathlib/Topology/MetricSpace/HausdorffDistance.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/MetricSpace/HausdorffDistance.lean#L257)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L269)
