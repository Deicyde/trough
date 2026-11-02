---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: IsPathConnected
mathlib_file: Mathlib/Topology/Connected/PathConnected.lean
---

# Path connectedness

A set `F` is path connected if it contains a point that can be joined to all other in `F`.

```lean
IsPathConnected.{u_1} {X : Type u_1} [TopologicalSpace X] (F : Set X) : Prop
```

## Depends on

- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Order (Real numbers)](../../single-variable-real-analysis/real-numbers/order.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Sources

- [Mathlib documentation: `IsPathConnected`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Connected/PathConnected.html#IsPathConnected)
- [Source of `IsPathConnected` in Mathlib/Topology/Connected/PathConnected.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Connected/PathConnected.lean#L411)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L416)
