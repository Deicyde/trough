# Orthogonal projection

The orthogonal projection onto a subspace.

```lean
Submodule.orthogonalProjectionOnto.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] (K : Submodule 𝕜 E) [K.HasOrthogonalProjection] :
  E →L[𝕜] ↥K
```

## Depends on

- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `Submodule.orthogonalProjectionOnto`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Projection/Basic.html#Submodule.orthogonalProjectionOnto)
- [Source of `Submodule.orthogonalProjectionOnto` in Mathlib/Analysis/InnerProductSpace/Projection/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/InnerProductSpace/Projection/Basic.lean#L119)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L298)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L439)
