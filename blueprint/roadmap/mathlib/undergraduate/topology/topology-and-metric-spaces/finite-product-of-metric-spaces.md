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
- [Source of `metricSpacePi` in Mathlib/Topology/MetricSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Basic.lean#L156)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L407)
