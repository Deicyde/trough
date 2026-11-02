---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_hilbertBasis
mathlib_file: Mathlib/Analysis/InnerProductSpace/l2Space.lean
---

# Existence of Hilbert basis

A Hilbert space admits a Hilbert basis.

```lean
exists_hilbertBasis.{u_2, u_3} (𝕜 : Type u_2) [RCLike 𝕜] (E : Type u_3) [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [CompleteSpace E] : ∃ w b, ⇑b = Subtype.val
```

## Depends on

- [Hilbert bases](../../../undergraduate/topology/hilbert-spaces/hilbert-bases.md)

## Proof depends on

- [Closure](../../topology/general-topology/part-01/closure.md)
- [Completeness of $l^2$](../../../undergraduate/topology/hilbert-spaces/completeness-of-l-2.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [Topology on a normed vector space](../normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `exists_hilbertBasis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/l2Space.html#exists_hilbertBasis)
- [Source of `exists_hilbertBasis` in Mathlib/Analysis/InnerProductSpace/l2Space.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/l2Space.lean#L592)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L301)
