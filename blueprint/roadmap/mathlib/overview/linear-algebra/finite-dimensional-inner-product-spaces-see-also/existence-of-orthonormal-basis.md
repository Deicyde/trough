# Existence of orthonormal basis

An orthonormal basis on E is an identification of `E` with its dimensional-matching
`EuclideanSpace 𝕜 ι`.

```lean
OrthonormalBasis.{u_1, u_3, u_4} (ι : Type u_1) (𝕜 : Type u_3) [RCLike 𝕜] (E : Type u_4)
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] : Type (max (max u_1 u_3) u_4)
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Linear map](../fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `OrthonormalBasis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/PiL2.html#OrthonormalBasis)
- [Source of `OrthonormalBasis` in Mathlib/Analysis/InnerProductSpace/PiL2.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/PiL2.lean#L368)
- [Mathlib overview: Linear algebra › Finite-dimensional inner product spaces (see also Hilbert spaces, below)](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L210)
