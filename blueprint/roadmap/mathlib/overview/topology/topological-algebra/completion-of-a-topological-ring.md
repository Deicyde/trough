# Completion of a topological ring

Mathlib states this as `UniformSpace.Completion.ring`.

```lean
UniformSpace.Completion.ring.{u_1} {α : Type u_1} [Ring α] [UniformSpace α] [IsTopologicalRing α]
  [IsUniformAddGroup α] : Ring (UniformSpace.Completion α)
```

## Depends on

- [Completion of an abelian topological group](completion-of-an-abelian-topological-group.md)
- [Ring](../../general-algebra/rings/ring.md)
- [Topological ring](topological-ring.md)

## Sources

- [Mathlib documentation: `UniformSpace.Completion.ring`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/UniformRing.html#UniformSpace.Completion.ring)
- [Source of `UniformSpace.Completion.ring` in Mathlib/Topology/Algebra/UniformRing.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Algebra/UniformRing.lean#L81)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L255)
