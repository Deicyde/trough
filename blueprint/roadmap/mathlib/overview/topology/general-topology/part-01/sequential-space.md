# Sequential space

A topological space is said to be a *sequential space* if any sequentially closed set in this
space is closed. This condition is weaker than being a Fréchet-Urysohn space.

```lean
SequentialSpace.{u_1} (X : Type u_1) [TopologicalSpace X] : Prop
```

## Depends on

- [Limit of a map with respect to filters](limit-of-a-map-with-respect-to-filters.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Topological space](topological-space.md)

## Sources

- [Mathlib documentation: `SequentialSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Sequences.html#SequentialSpace)
- [Source of `SequentialSpace` in Mathlib/Topology/Defs/Sequences.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Defs/Sequences.lean#L90)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L226)
