---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: instIsManifoldIcc
mathlib_file: Mathlib/Geometry/Manifold/Instances/Real.lean
---

# Closed interval

The manifold structure on `[x, y]` is smooth.

```lean
instIsManifoldIcc (x y : ℝ) [Fact (x < y)] {n : WithTop ℕ∞} :
  IsManifold (modelWithCornersEuclideanHalfSpace 1) n ↑(Set.Icc x y)
```

## Depends on

- [Inner product space, over $R$ or $C$](../../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Smooth or analytic manifold (with boundary and corners)](../part-01/smooth-or-analytic-manifold-with-boundary-and-co.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)
- [Ordered ring](../../../general-algebra/rings/ordered-ring.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `instIsManifoldIcc`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Instances/Real.html#instIsManifoldIcc)
- [Source of `instIsManifoldIcc` in Mathlib/Geometry/Manifold/Instances/Real.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/Instances/Real.lean#L553)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L461)
