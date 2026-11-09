# Uniform space

A uniform space is a generalization of the "uniform" topological aspects of a
metric space. It consists of a filter on `α × α` called the "uniformity", which
satisfies properties analogous to the reflexivity, symmetry, and triangle properties
of a metric.

A metric space has a natural uniformity, and a uniform space has a natural topology.
A topological group also has a natural uniformity, even when it is not metrizable.

```lean
UniformSpace.{u} (α : Type u) : Type u
```

## Depends on

- [Limit of a map with respect to filters](../general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Topological space](../general-topology/part-01/topological-space.md)

## Sources

- [Mathlib documentation: `UniformSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/Defs.html#UniformSpace)
- [Source of `UniformSpace` in Mathlib/Topology/UniformSpace/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/UniformSpace/Defs.lean#L187)
- [Mathlib overview: Topology › Uniform notions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L238)
