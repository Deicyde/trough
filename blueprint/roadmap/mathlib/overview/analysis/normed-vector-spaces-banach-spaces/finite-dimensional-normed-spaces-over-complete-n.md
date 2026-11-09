# Finite-dimensional normed spaces over complete normed fields are complete

A finite-dimensional subspace is complete.

```lean
Submodule.isComplete_of_finiteDimensional.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
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

- [Affine space](../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Isomorphism with $K^n$](../../linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Local ring](../../general-algebra/rings/local-ring.md)
- [Quotient space (Fundamentals)](../../linear-algebra/fundamentals/quotient-space.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Submodule.isComplete_of_finiteDimensional`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Module/FiniteDimension.html#Submodule.isComplete_of_finiteDimensional)
- [Source of `Submodule.isComplete_of_finiteDimensional` in Mathlib/Topology/Algebra/Module/FiniteDimension.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Algebra/Module/FiniteDimension.lean#L551)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L282)
