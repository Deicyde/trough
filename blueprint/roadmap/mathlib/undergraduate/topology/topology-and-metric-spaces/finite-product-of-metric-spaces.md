# Finite product of metric spaces

A finite product of metric spaces is a metric space, with the sup distance.

```lean
metricSpacePi.{v, u_2} {β : Type v} {X : β → Type u_2} [Fintype β] [(b : β) → MetricSpace (X b)] :
  MetricSpace ((b : β) → X b)
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Sources

- [Mathlib documentation: `metricSpacePi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Basic.html#metricSpacePi)
- [Source of `metricSpacePi` in Mathlib/Topology/MetricSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/MetricSpace/Basic.lean#L156)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L407)
