# Local convexity

A `LocallyConvexSpace` is a topological semimodule over an ordered semiring in which convex
neighborhoods of a point form a neighborhood basis at that point.

```lean
LocallyConvexSpace.{u_1, u_2} (𝕜 : Type u_1) (E : Type u_2) [Semiring 𝕜] [PartialOrder 𝕜]
  [AddCommMonoid E] [_root_.Module 𝕜 E] [TopologicalSpace E] : Prop
```

## Depends on

- [Convex subsets](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Filter](../../topology/general-topology/part-01/filter.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Topological space](../../topology/general-topology/part-01/topological-space.md)

## Sources

- [Mathlib documentation: `LocallyConvexSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Module/LocallyConvex.html#LocallyConvexSpace)
- [Source of `LocallyConvexSpace` in Mathlib/Topology/Algebra/Module/LocallyConvex.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/Algebra/Module/LocallyConvex.lean#L47)
- [Mathlib overview: Analysis › Topological vector spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L274)
