---
declaration: corollary
origin: cited
lean: MeasureTheory.Martingale.submartingale_norm
statement: formalized
proof: formalized
---

# Martingale.submartingale_norm

Let $X : T \rightarrow \Omega \rightarrow E$ a martingale with values in a normed space $E$. Then $\Vert X \Vert$ is a sub-martingale.

## Depends on

- [Martingale](../../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Submartingale](def-submartingale.md)

## Proof depends on

- [norm_condExp_le](cor-norm-condexp-le.md)

## Proof

Same proof as Lemma [Martingale.submartingale_convex_comp](lem-martingale-submartingale-convex-comp.md), specialized to $\phi = \Vert \cdot \Vert$, for which we can use Corollary [norm_condExp_le](cor-norm-condexp-le.md).

## Lean

Formalized as [`MeasureTheory.Martingale.submartingale_norm`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Martingale.submartingale_norm).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 204](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L204)
