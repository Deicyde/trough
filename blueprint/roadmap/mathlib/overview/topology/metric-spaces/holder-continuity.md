---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: HolderWith
mathlib_file: Mathlib/Topology/MetricSpace/Holder.lean
---

# Hölder continuity

A function `f : X → Y` between two `PseudoEMetricSpace`s is Hölder continuous with constant
`C : ℝ≥0` and exponent `r : ℝ≥0`, if `edist (f x) (f y) ≤ C * edist x y ^ r` for all `x y : X`.

```lean
HolderWith.{u_1, u_2} {X : Type u_1} {Y : Type u_2} [PseudoEMetricSpace X] [PseudoEMetricSpace Y]
  (C r : NNReal) (f : X → Y) : Prop
```

## Depends on

- [Induced topology](../general-topology/part-01/induced-topology.md)
- [Power functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/power-functions.md)
- [Uniform space](../uniform-notions/uniform-space.md)

## Sources

- [Mathlib documentation: `HolderWith`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Holder.html#HolderWith)
- [Source of `HolderWith` in Mathlib/Topology/MetricSpace/Holder.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Holder.lean#L49)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L265)
