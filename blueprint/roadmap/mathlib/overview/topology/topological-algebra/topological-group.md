---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: IsTopologicalGroup
mathlib_file: Mathlib/Topology/Algebra/Group/Defs.lean
---

# Topological group

A topological group is a group in which the multiplication and inversion operations are
continuous.

When you declare an instance that does not already have a `UniformSpace` instance,
you should also provide an instance of `UniformSpace` and `IsUniformGroup` using
`IsTopologicalGroup.rightUniformSpace` and `isUniformGroup_of_commGroup`.

```lean
IsTopologicalGroup.{u_4} (G : Type u_4) [TopologicalSpace G] [Group G] : Prop
```

## Depends on

- [Continuous function](../general-topology/part-01/continuous-function.md)
- [Group](../../general-algebra/group-theory/part-01/group.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `IsTopologicalGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Group/Defs.html#IsTopologicalGroup)
- [Source of `IsTopologicalGroup` in Mathlib/Topology/Algebra/Group/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/Group/Defs.lean#L103)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L251)
