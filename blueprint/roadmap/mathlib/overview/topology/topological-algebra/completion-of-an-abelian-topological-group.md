# Completion of an abelian topological group

Mathlib states this as `UniformSpace.Completion.instAddCommGroup`.

```lean
UniformSpace.Completion.instAddCommGroup.{u_3} {α : Type u_3} [UniformSpace α] [AddCommGroup α]
  [IsUniformAddGroup α] : AddCommGroup (UniformSpace.Completion α)
```

## Depends on

- [Completion](../uniform-notions/completion.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `UniformSpace.Completion.instAddCommGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/GroupCompletion.html#UniformSpace.Completion.instAddCommGroup)
- [Source of `UniformSpace.Completion.instAddCommGroup` in Mathlib/Topology/Algebra/GroupCompletion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/GroupCompletion.lean#L185)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L252)
