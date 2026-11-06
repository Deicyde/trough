# Hausdorff space

A T₂ space, also known as a Hausdorff space, is one in which for every
`x ≠ y` there exists disjoint open sets around `x` and `y`. This is
the most widely used of the separation axioms.

```lean
T2Space.{u} (X : Type u) [TopologicalSpace X] : Prop
```

## Depends on

- [Topological space](topological-space.md)

## Sources

- [Mathlib documentation: `T2Space`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Separation/Hausdorff.html#T2Space)
- [Source of `T2Space` in Mathlib/Topology/Separation/Hausdorff.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Separation/Hausdorff.lean#L80)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L225)
