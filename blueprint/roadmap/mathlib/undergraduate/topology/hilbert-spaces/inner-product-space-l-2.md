---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: lp.instInnerProductSpace
mathlib_file: Mathlib/Analysis/InnerProductSpace/l2Space.lean
---

# Inner product space $l^2$

Mathlib states this as `lp.instInnerProductSpace`.

```lean
lp.instInnerProductSpace.{u_1, u_2, u_4} {ι : Type u_1} {𝕜 : Type u_2} [RCLike 𝕜] {G : ι → Type u_4}
  [(i : ι) → NormedAddCommGroup (G i)] [(i : ι) → InnerProductSpace 𝕜 (G i)] :
  InnerProductSpace 𝕜 ↥(lp G 2)
```

## Depends on

- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Power functions](../../single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/power-functions.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure.md)

## Sources

- [Mathlib documentation: `lp.instInnerProductSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/l2Space.html#lp.instInnerProductSpace)
- [Source of `lp.instInnerProductSpace` in Mathlib/Analysis/InnerProductSpace/l2Space.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/l2Space.lean#L116)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L442)
