---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Units.instLieGroupModelWithCornersSelf
mathlib_file: Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.lean
---

# General linear group as a Lie group

The units of a complete normed ring form a Lie group.

```lean
Units.instLieGroupModelWithCornersSelf.{u_1, u_2} {R : Type u_1} [NormedRing R] [CompleteSpace R]
  {n : WithTop ℕ∞} {𝕜 : Type u_2} [NontriviallyNormedField 𝕜] [NormedAlgebra 𝕜 R] :
  LieGroup (modelWithCornersSelf 𝕜 R) n Rˣ
```

## Depends on

- [Lie group](../part-01/lie-group.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)
- [Induced topology](../../../topology/general-topology/part-01/induced-topology.md)
- [Invertible elements](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Open map](../../../topology/general-topology/part-01/open-map.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `Units.instLieGroupModelWithCornersSelf`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.html#Units.instLieGroupModelWithCornersSelf)
- [Source of `Units.instLieGroupModelWithCornersSelf` in Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.lean#L63)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L462)
