---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: HilbertBasis
mathlib_file: Mathlib/Analysis/InnerProductSpace/l2Space.lean
---

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
- [Source of `HilbertBasis` in Mathlib/Analysis/InnerProductSpace/l2Space.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/l2Space.lean#L374)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L446)
