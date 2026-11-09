# Inner product space $l^2$

Mathlib states this as `lp.instInnerProductSpace`.

```lean
lp.instInnerProductSpace.{u_1, u_2, u_4} {ι : Type u_1} {𝕜 : Type u_2} [RCLike 𝕜] {G : ι → Type u_4}
  [(i : ι) → NormedAddCommGroup (G i)] [(i : ι) → InnerProductSpace 𝕜 (G i)] :
  InnerProductSpace 𝕜 ↥(lp G 2)
```

## Depends on

- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Sources

- [Mathlib documentation: `lp.instInnerProductSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/l2Space.html#lp.instInnerProductSpace)
- [Source of `lp.instInnerProductSpace` in Mathlib/Analysis/InnerProductSpace/l2Space.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/InnerProductSpace/l2Space.lean#L116)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L442)
