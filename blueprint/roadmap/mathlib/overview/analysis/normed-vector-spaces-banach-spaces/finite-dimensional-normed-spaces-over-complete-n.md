---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Submodule.complete_of_finiteDimensional
mathlib_file: Mathlib/Topology/Algebra/Module/FiniteDimension.lean
---

# Finite-dimensional normed spaces over complete normed fields are complete

A finite-dimensional subspace is complete.

```lean
Submodule.complete_of_finiteDimensional.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜] [AddCommGroup E] [UniformSpace E] [T2Space E]
  [IsUniformAddGroup E] [_root_.Module 𝕜 E] [ContinuousSMul 𝕜 E] (s : Submodule 𝕜 E)
  [FiniteDimensional 𝕜 ↥s] : IsComplete ↑s
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Basis](../../linear-algebra/fundamentals/basis.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Equivalence of norms in finite dimension](equivalence-of-norms-in-finite-dimension.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Local ring](../../general-algebra/rings/local-ring.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Submodule.complete_of_finiteDimensional`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Module/FiniteDimension.html#Submodule.complete_of_finiteDimensional)
- [Source of `Submodule.complete_of_finiteDimensional` in Mathlib/Topology/Algebra/Module/FiniteDimension.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/Module/FiniteDimension.lean#L519)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L282)
