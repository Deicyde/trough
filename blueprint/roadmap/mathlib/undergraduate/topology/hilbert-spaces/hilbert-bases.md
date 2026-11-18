# Hilbert bases

A Hilbert basis on `ι` for an inner product space `E` is an identification of `E` with the `lp`
space `ℓ²(ι, 𝕜)`.

```lean
HilbertBasis.{u_1, u_2, u_3} (ι : Type u_1) (𝕜 : Type u_2) [RCLike 𝕜] (E : Type u_3)
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] : Type (max (max u_1 u_2) u_3)
```

## Depends on

- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `HilbertBasis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/l2Space.html#HilbertBasis)
- [Source of `HilbertBasis` in Mathlib/Analysis/InnerProductSpace/l2Space.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Analysis/InnerProductSpace/l2Space.lean#L374)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L446)
