---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: UniformSpace.Completion.ring
mathlib_file: Mathlib/Topology/Algebra/UniformRing.lean
---

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
- [Source of `UniformSpace.Completion.ring` in Mathlib/Topology/Algebra/UniformRing.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/UniformRing.lean#L81)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L255)
