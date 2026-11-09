# Adjoint operator

The adjoint operator as a partially defined linear operator, denoted as `T†`.

```lean
LinearPMap.adjoint.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  (T : E →ₗ.[𝕜] F) [CompleteSpace E] : F →ₗ.[𝕜] E
```

## Depends on

- [Extension by continuity](../../topology/general-topology/part-01/extension-by-continuity.md)
- [Fréchet-Riesz representation of the dual of a Hilbert space](frechet-riesz-representation-of-the-dual-of-a-hi.md)

## Sources

- [Mathlib documentation: `LinearPMap.adjoint`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/LinearPMap.html#LinearPMap.adjoint)
- [Source of `LinearPMap.adjoint` in Mathlib/Analysis/InnerProductSpace/LinearPMap.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/InnerProductSpace/LinearPMap.lean#L149)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L296)
