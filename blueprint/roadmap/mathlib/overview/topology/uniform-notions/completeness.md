# Completeness

A complete space is defined here using uniformities. A uniform space
is complete if every Cauchy filter converges.

```lean
CompleteSpace.{u} (α : Type u) [UniformSpace α] : Prop
```

## Depends on

- [Cauchy filter](cauchy-filter.md)

## Sources

- [Mathlib documentation: `CompleteSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/Cauchy.html#CompleteSpace)
- [Source of `CompleteSpace` in Mathlib/Topology/UniformSpace/Cauchy.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/UniformSpace/Cauchy.lean#L366)
- [Mathlib overview: Topology › Uniform notions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L243)
