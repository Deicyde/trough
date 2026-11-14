---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: Convexity.iConvexComb
---

# convex_weights_product

If $(a_m)_{m \in \mathbb{N}}$ are convex weights and $(b^n_m)_{n,m \in \mathbb{N}}$ is such that for all $n$, the $(b^n_m)$ are convex weights, then we denote by $(a_\cdot) * (b^\cdot_\cdot)$ the convex weights defined by $((a_\cdot) * (b^\cdot_\cdot))_m = \sum_{k} a_k b^k_m$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Convexity.iConvexComb`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Convexity.iConvexComb).

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 95](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L95)
