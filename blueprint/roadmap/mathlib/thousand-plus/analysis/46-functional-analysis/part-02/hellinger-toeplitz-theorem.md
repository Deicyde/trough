---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: LinearMap.IsSymmetric.continuous
mathlib_file: Mathlib/Analysis/InnerProductSpace/Symmetric.lean
---

# Hellinger–Toeplitz theorem

The **Hellinger--Toeplitz theorem**: if a symmetric operator is defined on a complete space,
then it is automatically continuous.

```lean
LinearMap.IsSymmetric.continuous.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E] {T : E →ₗ[𝕜] E}
  (hT : T.IsSymmetric) : Continuous ⇑T
```

## Depends on

- [Continuous function](../../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Inner product space, over $R$ or $C$](../../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)

## Proof depends on

- [Closed graph theorem](../part-01/closed-graph-theorem.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Ordered ring](../../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `LinearMap.IsSymmetric.continuous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Symmetric.html#LinearMap.IsSymmetric.continuous)
- [Source of `LinearMap.IsSymmetric.continuous` in Mathlib/Analysis/InnerProductSpace/Symmetric.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Symmetric.lean#L253)
- [1000+ theorems list: Q1472120](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1716)
- [1000+ theorems project: Q1472120](https://1000-plus.github.io/all.html?length=-1#Q1472120)
- [Wikipedia: Hellinger–Toeplitz theorem](https://en.wikipedia.org/wiki/Hellinger%E2%80%93Toeplitz_theorem)
- [Wikidata: Q1472120](https://www.wikidata.org/wiki/Q1472120)
